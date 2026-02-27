def calculate_risk(user_data, sensitive_findings):
    score = 0

    # 🔹 Repo Exposure Risk
    repo_count = user_data.get("public_repos", 0)
    
    if repo_count >= 20:
        score += 3
    elif repo_count >= 10:
        score += 2
    elif repo_count >= 5:
        score += 1

    # 🔹 Sensitive Data Risk
    score += len(sensitive_findings) * 3

    # 🔹 Bio Exposure Risk
    if user_data.get("bio"):
        score += 1

    # Risk Level Classification
    if score >= 10:
        level = "High 🔴"
    elif score >= 5:
        level = "Medium 🟠"
    else:
        level = "Low 🟢"

    return score, level