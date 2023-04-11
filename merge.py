import fitz
import json

# Load the JSON data
with open('mergeFiles.json') as f:
    data = json.load(f)

# Get the global values from the JSON data
author = data["author"]
document_name = data["document_name"]
document_version = data["document_version"]
output_directory = data["output_directory"]
protected = data["protected"]
compacted = data["compacted"]
toc = data["toc"]
bookmarks = data["bookmarks"]

# Create a list of PDFs to merge
pdfs_to_merge = []

for file_data in data["files"]:
    file_name = file_data["file_name"]
    document_number = file_data["document_number"]
    document_category = file_data["document_category"]
    sub_category = file_data["sub_category"]
    version = file_data["version"]
    merge = file_data["merge"]
    watermark_present = file_data["watermark_present"]
    merge_order = file_data.get("merge_order") or data["default_merge_order"].get(document_category, [])
    page_number = file_data.get("page_number") or data.get("default_page_number", False)

    if merge:
        pdf = fitz.open(file_name)
        # If watermark is present, add it to every page
        if watermark_present:
            watermark = fitz.Pixmap(fitz.csgray, fitz.Rect(0, 0, 100, 100), 128)
            for page in pdf:
                page.insert_image(page.rect, pixmap=watermark)

        pdfs_to_merge.append((pdf, merge_order, document_category, sub_category, page_number))

# Sort the list of PDFs to merge based on merge order
pdfs_to_merge.sort(key=lambda x: x[1])

# Merge the PDFs
merged_pdf = fitz.open()
toc_list = []

for pdf, _, _, _, add_toc in pdfs_to_merge:
    merged_pdf.insert_pdf(pdf)
    if add_toc:
        toc_list += merged_pdf.getToC()[2:]

# Set the metadata for the merged PDF
merged_pdf.set_metadata({
    "author": author,
    "title": document_name,
    "version": document_version
})

# Set the output path for the merged PDF
output_path = f"{output_directory}/{document_name} v{document_version}.pdf"

# Save the merged PDF
if protected:
    perm = fitz.PDF_PERM_ACCESSIBILITY
    merged_pdf.save(output_path, incremental=False, permissions=perm)
else:
    merged_pdf.save(output_path, incremental=compacted)

# Create a table of contents and bookmarks if specified
if toc:
    merged_pdf.setToC(toc_list)
if bookmarks:
    for item in toc_list:
        merged_pdf.add_bookmark(item[1], pagenum=item[0])
        
merged_pdf.close()
