
## HTML CSS JavaScript Extractor
This Python script allows you to extract HTML, CSS, JavaScript, and image files from a given URL and saves them locally on your computer. It also updates the paths in the HTML file to ensure that the extracted files work correctly.

# Features
Extract HTML, CSS, JavaScript, and image files from a URL
Update paths in the HTML file to point to the locally saved files
Organize extracted files into respective directories (html_files, css, js, img)
# Usage
Install the necessary Python dependencies:
'pip install requests beautifulsoup4'
Run the script htmlcssextractor.py:
'python htmlcssextractor.py'
Enter the URL when prompted.
The extracted files will be saved in the html_files directory in your user's home directory (C:\Users\<YourUsername>\html_files on Windows or /Users/<YourUsername>/html_files on macOS/Linux).
# Dependencies
requests: Used for making HTTP requests to fetch web content.
Beautiful Soup: Used for parsing HTML content.
# Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
