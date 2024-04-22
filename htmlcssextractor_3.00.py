import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def extract_files(url, root_dir):
    # Fetch HTML content
    response = requests.get(url)
    html_content = response.text

    # Create directories to store files
    html_dir = os.path.join(root_dir, 'html_files')
    css_dir = os.path.join(root_dir, 'html_files', 'css')
    js_dir = os.path.join(root_dir, 'html_files', 'js')
    img_dir = os.path.join(root_dir, 'html_files', 'img')
    os.makedirs(html_dir, exist_ok=True)
    os.makedirs(css_dir, exist_ok=True)
    os.makedirs(js_dir, exist_ok=True)
    os.makedirs(img_dir, exist_ok=True)

    # Save HTML content to a file
    with open(os.path.join(html_dir, 'index.html'), 'w', encoding='utf-8') as html_file:
        # Update paths of CSS, JavaScript, and images in HTML content
        updated_content = update_paths(html_content, url, root_dir)
        html_file.write(updated_content)

    # Create BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract CSS, JavaScript, and image links
    css_links = [link['href'] for link in soup.find_all('link', rel='stylesheet')]
    js_links = [script['src'] for script in soup.find_all('script', src=True)]
    img_links = [img['src'] for img in soup.find_all('img', src=True)]

    # Download CSS files
    for css_link in css_links:
        download_file(url, css_link, css_dir)

    # Download JavaScript files
    for js_link in js_links:
        download_file(url, js_link, js_dir)

    # Download images
    for img_link in img_links:
        download_file(url, img_link, img_dir)

def download_file(base_url, file_link, output_dir):
    # Check if the file link is absolute or relative
    if not urlparse(file_link).scheme:
        full_url = urljoin(base_url, file_link)  # Construct full URL
    else:
        full_url = file_link
    response = requests.get(full_url)
    with open(os.path.join(output_dir, os.path.basename(urlparse(full_url).path)), 'wb') as file:
        file.write(response.content)

def update_paths(html_content, base_url, root_dir):
    # Create BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    # Update paths of CSS links
    update_links(soup, 'link', 'href', base_url, root_dir, 'css')

    # Update paths of JavaScript links
    update_links(soup, 'script', 'src', base_url, root_dir, 'js')

    # Update paths of image links
    update_links(soup, 'img', 'src', base_url, root_dir, 'img')

    return str(soup)

def update_links(soup, tag_name, attr_name, base_url, root_dir, subdir):
    links = soup.find_all(tag_name, {attr_name: True})
    for link in links:
        if attr_name in link.attrs:
            old_path = link[attr_name]
            if not urlparse(old_path).scheme:
                new_path = os.path.relpath(os.path.join(root_dir, 'html_files', subdir, os.path.basename(urlparse(old_path).path)), os.path.dirname(os.path.join(root_dir, 'html_files', 'index.html')))
                link[attr_name] = new_path

if __name__ == "__main__":
    url = input("Enter URL: ")
    root_dir = os.path.expanduser('~')
    extract_files(url, root_dir)
    print(f"Extraction complete. HTML saved to {os.path.join(root_dir, 'html_files', 'index.html')}, CSS to {os.path.join(root_dir, 'html_files', 'css')}, JavaScript to {os.path.join(root_dir, 'html_files', 'js')}, and images to {os.path.join(root_dir, 'html_files', 'img')} directories.")
