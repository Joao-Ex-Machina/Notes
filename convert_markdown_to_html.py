#!/usr/bin/env python

import os
import subprocess

# Function to convert Markdown to HTML if Markdown file is newer
def convert_markdown_to_html_if_newer(markdown_file):
    html_file = os.path.splitext(markdown_file)[0] + ".html"

    # Check if HTML file exists and compare modification timestamps
    if not os.path.exists(html_file) or os.path.getmtime(markdown_file) > os.path.getmtime(html_file):
        subprocess.run(
            [
                "pandoc",
                "-s",
                "--katex",
                "--lua-filter",
                "fix-links-multiple-files.lua",
                "-o",
                html_file,
                markdown_file,
            ]
        )
        #print(f"Converted {markdown_file} to {html_file}")
    #else:
        #print(f"{markdown_file} is up to date. Skipping conversion.")

# Define the root directory where your Markdown files are located
root_directory = "/home/jbcr/Desktop/IST/MEng/Notes/"

# Recursively iterate through all Markdown files in the root directory
for root, _, files in os.walk(root_directory):
    for file in files:
        if file.endswith(".md"):
            markdown_file = os.path.join(root, file)
            convert_markdown_to_html_if_newer(markdown_file)

