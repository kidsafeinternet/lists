import requests
import tarfile
import os

def download_file(url, local_filename):
    """
    Downloads a file from the given URL and saves it locally.
    """
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def extract_tar_gz(tar_gz_path, extract_to='.'):
    """
    Extracts a tar.gz file to the specified directory.
    """
    with tarfile.open(tar_gz_path, 'r:gz') as tar:
        tar.extractall(path=extract_to)

def read_txt_from_tar_gz(tar_gz_path, txt_filename):
    """
    Reads a text file from a tar.gz archive.
    """
    with tarfile.open(tar_gz_path, 'r:gz') as tar:
        for member in tar.getmembers():
            if member.name.endswith(txt_filename):
                f = tar.extractfile(member)
                if f:
                    return f.read().decode('utf-8')
    return None

if __name__ == '__main__':
    url = 'https://github.com/mitchellkrogza/Phishing.Database/raw/master/ALL-phishing-domains.tar.gz'
    local_tar_gz = 'ALL-phishing-domains.tar.gz'
    txt_filename = 'ALL-phishing-domains.txt'  # Adjust this if the text file name is different

    # Download the tar.gz file
    print('Downloading file...')
    download_file(url, local_tar_gz)
    print('Download complete.')

    # Extract the tar.gz file
    print('Extracting file...')
    extract_tar_gz(local_tar_gz)
    print('Extraction complete.')

    # Read the text file from the tar.gz archive
    print('Reading text file from archive...')
    txt_content = read_txt_from_tar_gz(local_tar_gz, txt_filename)
    if txt_content:
        # Remove ALL-phishing-domains.tar.gz
        print('Text file found in the archive.')
        os.remove(local_tar_gz)
        # Rename the text file to phishing_sites.txt
        new_txt_filename = 'phishing_sites.txt'
        os.rename(txt_filename, new_txt_filename)
        print(f'Renamed {txt_filename} to {new_txt_filename}')
        # Move phishing_sites.txt to the data/malicious/ directory
        os.makedirs('data/malicious', exist_ok=True)
        os.replace(new_txt_filename, os.path.join('data/malicious', new_txt_filename))
        print(f'Moved {new_txt_filename} to data/malicious/')
    else:
        print('Text file not found in the archive.')