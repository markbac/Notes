import os
import re
import json

# Regular expression pattern to extract document number, name, category, sub-category, and version from filename
filename_pattern = re.compile(r"^(?P<category>\w+)\s?-?\s?(?P<sub_category>\w*)\s?-?\s?(?P<document_name>.+)\s?-?\s?v?(?P<version>\d+\.\d+)\.pdf$", re.IGNORECASE)

# Directory containing PDF files to be indexed
pdf_directory = "./pdfs"

# Global document information
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

# List to store file information
file_info = []

# Default merge order for each category and sub-category
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

# Order in which to merge each category
category_order = [
    "CodeOfConduct",
    "Policy"
]

# Loop through PDF files in directory
for filename in os.listdir(pdf_directory):
    if not filename.endswith(".pdf"):
        continue
        
    # Extract document information from filename using regular expression
    match = filename_pattern.match(filename)
    if match:
        document_number = ""
        document_name = match.group("document_name")
        category = match.group("category")
        sub_category = match.group("sub_category")
        version = match.group("version")
    else:
        document_number = ""
        document_name = ""
        category = ""
        sub_category = ""
        version = ""
        
    # Create dictionary for file information
    file_dict = {
        "file_name": filename,
        "document_number": document_number,
        "document_name": document_name,
        "category": category,
        "sub_category": sub_category,
        "version": version,
        "merge": True,
        "watermark_present": False,
        "page_numbers": True
    }
    
    # Add file dictionary to list
    file_info.append(file_dict)

# Create dictionary to store all information
merged_dict = {
    "global": global_info,
    "files": file_info,
    "default_merge_order": default_merge_order,
    "category_order": category_order
}

# Output dictionary as JSON
print(json.dumps(merged_dict, indent=4))
