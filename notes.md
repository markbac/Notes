import os

def generate_book_metadata():
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    repo_url = input("Enter the repository URL: ")
    description = input("Enter the book description: ")
    language = input("Enter the language code for the book: ")
    multilingual = input("Is the book available in multiple languages? (true/false): ")
    copyright = input("Enter the copyright information for the book: ")
    edition = input("Enter the edition of the book: ")
    keywords = input("Enter the keywords for the book (comma-separated): ")
    categories = input("Enter the categories for the book (comma-separated): ")

    with open("book.toml", "w") as f:
        f.write(f"title = '{title}'\n")
        f.write(f"author = '{author}'\n")
        f.write(f"repository = '{repo_url}'\n")
        f.write(f"description = '{description}'\n")
        f.write(f"language = '{language}'\n")
        f.write(f"multilingual = {multilingual}\n")
        f.write(f"copyright = '{copyright}'\n")
        f.write(f"edition = '{edition}'\n")
        f.write(f"keywords = [{keywords}]\n")
        f.write(f"categories = [{categories}]\n")

    print("book.toml generated.")

def generate_summary():
    summary = "# Summary\n\n"

    def prompt_chapter(chapter_number):
        chapter_title = input(f"Enter the title for Chapter {chapter_number}: ")
        chapter_filename = input(f"Enter the filename for Chapter {chapter_number} (without extension): ")
        chapter_entry = f"* [{chapter_title}]({chapter_filename}.md)\n"

        while True:
            subchapters = int(input(f"Enter the number of subchapters for Chapter {chapter_number} (0 to skip): "))

            if subchapters == 0:
                break

            for subchapter_number in range(1, subchapters + 1):
                subchapter_title = input(f"Enter the title for Subchapter {chapter_number}.{subchapter_number}: ")
                subchapter_filename = input(f"Enter the filename for Subchapter {chapter_number}.{subchapter_number} (without extension): ")
                subchapter_entry = f"  * [{subchapter_title}]({subchapter_filename}.md)\n"
                chapter_entry += subchapter_entry

                while True:
                    subsubchapters = int(input(f"Enter the number of sub-subchapters for Subchapter {chapter_number}.{subchapter_number} (0 to skip): "))

                    if subsubchapters == 0:
                        break

                    for subsubchapter_number in range(1, subsubchapters + 1):
                        subsubchapter_title = input(f"Enter the title for Sub-subchapter {chapter_number}.{subchapter_number}.{subsubchapter_number}: ")
                        subsubchapter_filename = input(f"Enter the filename for Sub-subchapter {chapter_number}.{subchapter_number}.{subsubchapter_number} (without extension): ")
                        subsubchapter_entry = f"    * [{subsubchapter_title}]({subsubchapter_filename}.md)\n"
                        chapter_entry += subsubchapter_entry

        return chapter_entry

    chapter_number = 1

    while True:
        chapter_entry = prompt_chapter(chapter_number)

        if chapter_entry.strip() == "":
            break

        summary += chapter_entry
        chapter_number += 1

    with open("SUMMARY.md", "w") as f:
        f.write(summary)

    print("SUMMARY.md generated.")

def generate_book_files():
    create_toml = input("Do you want to generate book.toml? (yes/no): ")
    create_summary = input("Do you want to generate SUMMARY.md? (yes/no): ")

    if create_toml.lower() == "yes":
        generate_book_metadata()

    if create_summary.lower() == "yes":
        generate_summary()

if __name__ == "__main__":
    generate_book_files()

-----------------------------
Summary
Overview of epics
   Features
      User stories 
Architecture 
   Summary 
   Projects 
       Components
Openadr
   Pas extension
   Messages
       Xml
       Message flows (sequence diagrams) 
Apis
   Markdown of openapi yaml
------------------------------------
import argparse
import pandas as pd
import os

def excel_to_markdown(excel_file_path, output_file_path=None):
    # Read all sheets from Excel file
    sheets_dict = pd.read_excel(excel_file_path, sheet_name=None)

    # Convert each sheet to Markdown table
    for sheet_name, df in sheets_dict.items():
        markdown_table = df.to_markdown(index=False)

        # Determine output file path for each sheet
        if output_file_path is None:
            base_output_path = os.path.splitext(excel_file_path)[0]
            if len(sheets_dict) == 1:  # Only one sheet, no need to append sheet name
                output_file_path = f"{base_output_path}.md"
            else:
                output_file_path = f"{base_output_path}_{sheet_name}.md"

        # Write Markdown table to output file for each sheet
        with open(output_file_path, 'w') as f:
            f.write(markdown_table)

        print(f"Markdown table for sheet '{sheet_name}' written to {output_file_path}")
        output_file_path = None  # Reset output_file_path for next sheet (if any)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert Excel file to Markdown tables')
    parser.add_argument('input_file', help='path to the input Excel file')
    parser.add_argument('-o', '--output_file', help='base path to the output Markdown files (default: input file name)')
    args = parser.parse_args()

    # Call the function with the provided arguments
    excel_to_markdown(args.input_file, args.output_file)

if __name__ == '__main__':
    main()


    ----------------------
