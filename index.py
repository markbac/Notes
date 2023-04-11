import os
import re
import json

dir_path = "/path/to/files"

def get_file_data(file_path):
    # extract data from filename using regex
    pattern = r"(?P<document_number>\d+)_(?P<document_name>.+)_Cat(?P<category>.+)_Sub(?P<sub_category>.+)_Ver(?P<version>\d+)\.pdf"
    match = re.match(pattern, os.path.basename(file_path))
    if match:
        return {
            "file_name": os.path.basename(file_path),
            "document_number": match.group("document_number"),
            "document_name": match.group("document_name"),
            "category": match.group("category"),
            "sub_category": match.group("sub_category"),
            "version": int(match.group("version")),
            "merge": True,
            "watermark_present": False,
            "page_number_display": False
        }
    else:
        return None

def create_merge_order(files):
    merge_order = {}
    for file in files:
        if file["category"] not in merge_order:
            merge_order[file["category"]] = [{"sub_category": file["sub_category"], "merge_order": 2}]
        elif any(d.get("sub_category") == file["sub_category"] for d in merge_order[file["category"]]):
            pass
        else:
            merge_order[file["category"]].append({"sub_category": file["sub_category"], "merge_order": 2})
    return merge_order

def main():
    # get list of all pdf files in directory
    pdf_files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith(".pdf")]

    # get data for each pdf file
    files_data = [get_file_data(file) for file in pdf_files]
    files_data = list(filter(None, files_data))

    # create merge order
    default_merge_order = create_merge_order(files_data)
    category_order = list(default_merge_order.keys())

    # create dictionary with all data
    json_data = {
        "global_values": {
            "author": "",
            "document_name": "",
            "output_directory": "",
            "document_version": ""
        },
        "files": files_data,
        "options": {
            "add_table_of_contents": False,
            "add_bookmarks": False,
            "output_protected": False,
            "output_compacted": False
        },
        "default_merge_order": default_merge_order,
        "category_order": category_order
    }

    # write dictionary to json file
    with open(os.path.join(dir_path, "mergeFiles.json"), "w") as outfile:
        json.dump(json_data, outfile, indent=4)

if __name__ == "__main__":
    main()
