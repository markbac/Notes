import os
import json

# function to extract category and subcategory from filename
def extract_category(filename):
    category, subcategory = filename.split("_")[1:3]
    return category, subcategory

# function to generate JSON schema for a given directory
def generate_json_schema(directory_path, default_category_order):
    schema = {
        "global_values": {
            "author": "John Doe",
            "document_name": "Merged Document",
            "document_version": "1.0",
            "output_directory": os.path.join(directory_path, "output"),
            "is_protected": False,
            "is_compacted": False,
            "add_table_of_contents": True,
            "add_bookmarks": True
        },
        "file_list": []
    }

    # get list of files in directory
    file_list = os.listdir(directory_path)

    # loop through files in directory
    for filename in file_list:
        # only process PDF files
        if not filename.endswith(".pdf"):
            continue

        # extract document information from filename
        doc_number, category, subcategory, version = filename[:-4].split("_")
        category = category.capitalize()
        subcategory = subcategory.capitalize()

        # get merge order for category
        if category in default_category_order:
            merge_order = default_category_order[category]
        else:
            merge_order = len(default_category_order) + 1
            default_category_order[category] = merge_order

        # create file schema
        file_schema = {
            "filename": filename,
            "doc_number": doc_number,
            "doc_name": "",
            "category": category,
            "subcategory": subcategory,
            "version": version,
            "merge": True,
            "watermark": False,
            "merge_order": merge_order,
            "add_page_numbers": True
        }

        # add file schema to JSON schema
        schema["file_list"].append(file_schema)

    # write JSON schema to file
    with open(os.path.join(directory_path, "mergeFiles.json"), "w") as f:
        json.dump(schema, f, indent=4)

    return schema

# example usage
directory_path = "/path/to/pdf/files"
default_category_order = {"Policy": 1, "Codeofconduct": 2, "Procedures": 3}
generate_json_schema(directory_path, default_category_order)
