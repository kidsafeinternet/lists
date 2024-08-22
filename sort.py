import os

def sort_files():
    nsfw_count = 0
    malware_count = 0

    # Walk through data/ directory and all its subdirectories
    for root, dirs, files in os.walk('data/'):
        for file in files:
            # Split the file name to get the extension
            filename, file_extension = os.path.splitext(file)
            # If the file extension is .txt
            if file_extension == '.txt':
                # Read the contents of the file
                with open(os.path.join(root, file), 'r') as f:
                    lines = f.readlines()
                
                # Remove empty lines and duplicates
                lines = list(set(filter(lambda x: x.strip(), lines)))
                
                # Sort the lines
                lines.sort()
                
                # Write the sorted contents back to the file
                with open(os.path.join(root, file), 'w') as f:
                    f.writelines(lines)
                
                # Count the number of lines
                if 'nsfw' in root:
                    nsfw_count += len(lines)
                elif 'malware' in root:
                    malware_count += len(lines)
                
                print(f'Sorted {file}')
    
    print('Files sorted successfully!')
    return nsfw_count, malware_count

def update_readme(nsfw_count, malware_count):
    readme_path = 'README.md'
    with open(readme_path, 'r') as f:
        lines = f.readlines()
    
    with open(readme_path, 'w') as f:
        for line in lines:
            if line.startswith('- [NSFW]'):
                f.write(f'- [NSFW](data/nsfw/nsfw_sites.txt) - {nsfw_count:,} links\n')
            elif line.startswith('- [VIRUS]'):
                f.write(f'- [VIRUS](data/malware/malware_sites.txt) - {malware_count:,} links\n')
            else:
                f.write(line)

if __name__ == '__main__':
    nsfw_count, malware_count = sort_files()
    update_readme(nsfw_count, malware_count)