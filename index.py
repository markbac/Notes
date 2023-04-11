import os
import re
import json

# Set global variables
global_info = {
    "author": "John Doe",
    "document_name": "Merged Document",
    "document_version": "1.0",
    "output_directory": "./output/",
    "protected": True,
    "compacted": True,
    "table_of_contents": True,
    "bookmarks": True
}

default_merge_order = {
    "Policy": [
        {
            "sub_category": "DataProtection",
            "merge_order": 1
        },
        {
            "sub_category": "InformationSecurity",
            "merge_order": 2
        }
    ],
    "CodeOfConduct": [
        {
            "merge_order": 1
        }
    ]
}

category_order = [
    "CodeOfConduct",
    "Policy"
]

# Create an empty list to store the file information
file_info_list = []

# Define a function to parse the filename and create a dictionary
def parse_filename(filename):
    # Use regex to extract information from the filename
    pattern = r'(?P<category>[\w\s]+)-(?P<sub_category>[\w\s]+)-v(?P<version>[\d\.]+).pdf'
    match = re.search(pattern, filename)
    
    # If regex match found, create dictionary
    if match:
        category = match.group('category').strip()
        sub_category = match.group('sub_category').strip()
        version = match.group('version').strip()
        
        document_name = category + ' ' + sub_category
        document_number = ''
        merge_order = None
        
        # Check if default merge order exists for category and sub-category
        if category in default_merge_order:
