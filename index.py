import os
import re
import json

# Set global configuration options
config = {
    "author": "John Doe",
    "document_name": "Merged Document",
    "document_version": "1.0",
    "output_directory": "./output/",
    "protected": True,
    "compacted": True,
    "table_of_contents": True,
    "bookmarks": True
}

# Define function to parse file name and extract metadata
def parse_file_name(file_name):
    metadata = {}
    match = re.search(r'^(.+?)\s*-\s*(.+?)\s*-\s*v(.+?)\..+?$', file_name)
    if match:
        metadata["document_name"] = match.group(1).strip()
        metadata["category"] = match.group(2).strip()
        metadata["version"] = match.group(3).strip()
        match = re.search(r'^(.+?)\s*-\s*(.+?)\s*-\s*v(.+?)\.(.+?)$', file_name)
        metadata["sub_category"] = match.group(4).strip()
    else:
        metadata["file_name"] = file_name
    return metadata

# Define function to create dictionary object for a file
def create_file_dict(file_path):
    file_dict = {}
    file_dict["file_name"] = os.path.basename(file_path)
    file_dict.update(parse_file_name(file_dict["file_name"]))
    file_dict["document_number"] = "00000"
    file_dict["merge"] = True
    file_dict["watermark_present"] = False
    file_dict["page_numbers"] = True
    return file_dict

# Index all pdf files in directory and create dictionary objects
pdf_files = []
for file_name in os.listdir("."):
    if file_name.endswith(".pdf"):
        pdf_files.append(create_file_dict(file_name))

# Create JSON output in desired format
output = {
    "global": config,
    "files": pdf_files,
    "default_merge_order": {
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
    },
    "category_order": [
        "CodeOfConduct",
        "Policy"
    ]
}

# Output JSON to file
with open("output.json", "w") as f:
    json.dump(output, f, indent=2)
