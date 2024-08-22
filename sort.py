import os

def sort_files():
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

if __name__ == '__main__':
    sort_files()
