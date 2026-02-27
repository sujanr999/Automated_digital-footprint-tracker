import streamlit as st

from github_collector import get_github_data
from forum_collector import get_forum_data
from instagram_collector import get_instagram_data
from pastebin_collector import get_pastebin_data
from unified_profile import build_unified_profile
from utils import detect_sensitive_data
from risk_analyzer import calculate_risk


st.set_page_config(page_title="Digital Footprint Tracker", layout="centered")

st.title("🔐 Digital Footprint Tracker")
st.write("Multi-Platform Digital Footprint & Risk Analyzer")


username = st.text_input("Enter Username")


if st.button("Analyze"):

    # ----------------------------
    # 1️⃣ Collect Data
    # ----------------------------

    github_data, repos_data = get_github_data(username)

    if github_data == "not_found":
        st.error("GitHub user does not exist.")
        st.stop()

    elif github_data == "rate_limited":
        st.error("GitHub API rate limit exceeded.")
        st.stop()

    elif github_data is None:
        st.error("Error fetching GitHub data.")
        st.stop()

    forum_data = get_forum_data(username)
    instagram_data = get_instagram_data(username)
    pastebin_data = get_pastebin_data(username)

    # ----------------------------
    # 2️⃣ Build Unified Profile
    # ----------------------------

    unified = build_unified_profile(
        github_data,
        forum_data,
        instagram_data,
        pastebin_data
    )

    # ----------------------------
    # 3️⃣ Show GitHub Activity
    # ----------------------------

    st.subheader("👤 GitHub Profile Summary")
    st.write("**Name:**", github_data.get("name"))
    st.write("**Bio:**", github_data.get("bio"))
    st.write("**Public Repositories:**", github_data.get("public_repos"))

    st.subheader("📂 GitHub Repositories")
    for repo in repos_data:
        st.write("-", repo["name"])

    # ----------------------------
    # 4️⃣ Show Linked Platforms
    # ----------------------------

    st.subheader("🌐 Linked Platforms")
    for platform in unified["platforms"]:
        st.write("-", platform)

    # ----------------------------
    # 5️⃣ Sensitive Data Detection
    # ----------------------------

    all_findings = []

    for text in unified["texts"]:
        all_findings.extend(detect_sensitive_data(text))

    st.subheader("⚠️ Sensitive Exposure")

    if all_findings:
        for finding in all_findings:
            st.warning(finding)
    else:
        st.success("No obvious sensitive exposure detected.")

    # ----------------------------
    # 6️⃣ Instagram Geotag Locations
    # ----------------------------

    if unified["locations"]:
        st.subheader("📍 Instagram Geotag Locations")
        for loc in unified["locations"]:
            st.write("-", loc)

    # ----------------------------
    # 7️⃣ Risk Scoring
    # ----------------------------

    score, level = calculate_risk(github_data, all_findings)

    st.subheader("📊 Privacy Risk Assessment")
    st.write("**Risk Score:**", score)
    st.write("**Risk Level:**", level)

    st.progress(min(score / 15, 1.0))