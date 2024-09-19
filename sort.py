import os

def sort_files():
    nsfw_total_count = 0
    nsfw_active_count = 0
    nsfw_inactive_count = 0
    nsfw_link_total_count = 0
    nsfw_link_active_count = 0
    nsfw_link_inactive_count = 0
    malware_total_count = 0
    malware_active_count = 0
    malware_inactive_count = 0
    phishing_total_count = 0
    phishing_active_count = 0
    phishing_inactive_count = 0

    # Walk through data/ directory and all its subdirectories
    for root, dirs, files in os.walk("data/"):
        for file in files:
            # Split the file name to get the extension
            filename, file_extension = os.path.splitext(file)
            # If the file extension is .txt
            if file_extension == ".txt":
                # Read the contents of the file
                with open(os.path.join(root, file), "r") as f:
                    lines = f.readlines()

                # Remove empty lines and duplicates
                lines = list(set(filter(lambda x: x.strip(), lines)))

                # Sort the lines
                lines.sort()

                # Write the sorted contents back to the file
                with open(os.path.join(root, file), "w") as f:
                    f.writelines(lines)

                # Count the number of lines
                if "nsfw" in root:
                    if file == "nsfw_sites.txt":
                        nsfw_total_count += len(lines)
                        if "ACTIVE" in file:
                            nsfw_active_count += len(lines)
                        elif "INACTIVE" in file:
                            nsfw_inactive_count += len(lines)
                    elif file == "nsfw_links.txt":
                        nsfw_link_total_count += len(lines)
                        if "ACTIVE" in file:
                            nsfw_link_active_count += len(lines)
                        elif "INACTIVE" in file:
                            nsfw_link_inactive_count += len(lines)
                elif "malicious" in root:
                    if "phishing" in file.lower():
                        phishing_total_count += len(lines)
                        if "ACTIVE" in file:
                            phishing_active_count += len(lines)
                        elif "INACTIVE" in file:
                            phishing_inactive_count += len(lines)
                    else:
                        malware_total_count += len(lines)
                        if "ACTIVE" in file:
                            malware_active_count += len(lines)
                        elif "INACTIVE" in file:
                            malware_inactive_count += len(lines)

                print(f"Sorted {file}")

    print("Files sorted successfully!")
    return (
        nsfw_total_count,
        nsfw_active_count,
        nsfw_inactive_count,
        nsfw_link_total_count,
        nsfw_link_active_count,
        nsfw_link_inactive_count,
        malware_total_count,
        malware_active_count,
        malware_inactive_count,
        phishing_total_count,
        phishing_active_count,
        phishing_inactive_count,
    )


def update_readme(
    nsfw_total_count,
    nsfw_active_count,
    nsfw_inactive_count,
    nsfw_link_total_count,
    nsfw_link_active_count,
    nsfw_link_inactive_count,
    malware_total_count,
    malware_active_count,
    malware_inactive_count,
    phishing_total_count,
    phishing_active_count,
    phishing_inactive_count,
):
    readme_path = "README.md"
    with open(readme_path, "r") as f:
        lines = f.readlines()

    with open(readme_path, "w") as f:
        skip_lines = False
        for line in lines:
            if line.startswith("- [NSFW DOMAINS]"):
                f.write(
                    f"- [NSFW DOMAINS](data/nsfw/nsfw_sites.txt) - {nsfw_total_count:,} links\n"
                )
                f.write(
                    f"  - [ACTIVE](data/nsfw/nsfw_sites_ACTIVE.txt) - {nsfw_active_count:,} links\n"
                )
                f.write(
                    f"  - [INACTIVE](data/nsfw/nsfw_sites_INACTIVE.txt) - {nsfw_inactive_count:,} links\n"
                )
                skip_lines = True
            elif line.startswith("- [NSFW LINKS]"):
                f.write(
                    f"- [NSFW LINKS](data/nsfw/nsfw_links.txt) - {nsfw_link_total_count:,} links\n"
                )
                f.write(
                    f"  - [ACTIVE](data/nsfw/nsfw_links_ACTIVE.txt) - {nsfw_link_active_count:,} links\n"
                )
                f.write(
                    f"  - [INACTIVE](data/nsfw/nsfw_links_INACTIVE.txt) - {nsfw_link_inactive_count:,} links\n"
                )
                skip_lines = True
            elif line.startswith("- [MALWARE]"):
                f.write(
                    f"- [MALWARE](data/malicious/malware_sites.txt) - {malware_total_count:,} links\n"
                )
                f.write(
                    f"  - [ACTIVE](data/malicious/malware_sites_ACTIVE.txt) - {malware_active_count:,} links\n"
                )
                f.write(
                    f"  - [INACTIVE](data/malicious/malware_sites_INACTIVE.txt) - {malware_inactive_count:,} links\n"
                )
                skip_lines = True
            elif line.startswith("- [PHISHING]"):
                f.write(
                    f"- [PHISHING](data/malicious/phishing_sites.txt) - {phishing_total_count:,} links\n"
                )
                f.write(
                    f"  - [ACTIVE](data/malicious/phishing_sites_ACTIVE.txt) - {phishing_active_count:,} links\n"
                )
                f.write(
                    f"  - [INACTIVE](data/malicious/phishing_sites_INACTIVE.txt) - {phishing_inactive_count:,} links\n"
                )
                skip_lines = True
            elif skip_lines and line.startswith("  - "):
                continue
            else:
                f.write(line)
                skip_lines = False


if __name__ == "__main__":
    (
        nsfw_total_count,
        nsfw_active_count,
        nsfw_inactive_count,
        nsfw_link_total_count,
        nsfw_link_active_count,
        nsfw_link_inactive_count,
        malware_total_count,
        malware_active_count,
        malware_inactive_count,
        phishing_total_count,
        phishing_active_count,
        phishing_inactive_count,
    ) = sort_files()
    update_readme(
        nsfw_total_count,
        nsfw_active_count,
        nsfw_inactive_count,
        nsfw_link_total_count,
        nsfw_link_active_count,
        nsfw_link_inactive_count,
        malware_total_count,
        malware_active_count,
        malware_inactive_count,
        phishing_total_count,
        phishing_active_count,
        phishing_inactive_count,
    )
