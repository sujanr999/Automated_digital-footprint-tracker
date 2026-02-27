def build_unified_profile(github, forum, instagram, pastebin):
    unified = {
        "platforms": [],
        "texts": [],
        "locations": []
    }

    if github:
        unified["platforms"].append("GitHub")
        unified["texts"].append(github.get("bio", ""))

    if forum:
        unified["platforms"].append("Forum")
        unified["texts"].extend(forum.get("posts", []))

    if instagram:
        unified["platforms"].append("Instagram")
        unified["texts"].append(instagram.get("bio", ""))

        for photo in instagram.get("photos", []):
            unified["texts"].append(photo.get("caption", ""))
            unified["locations"].append(photo.get("location", ""))

    if pastebin:
        unified["platforms"].append("Pastebin")
        unified["texts"].extend(pastebin.get("mentions", []))

    return unified