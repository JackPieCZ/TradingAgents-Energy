import os
from pathlib import Path
from markitdown import MarkItDown


def main():
    # Define directories using Windows paths as this script will be run by Windows Python
    source_dir = Path("./pdfs")
    dest_dir = Path("./mds")

    # Create destination directory if it doesn't exist
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Initialize MarkItDown converter
    md_converter = MarkItDown()

    # Find all PDFs
    pdf_files = list(source_dir.glob("*.pdf*"))

    if not pdf_files:
        print(f"No PDF files found in {source_dir}")
        return

    print(f"Found {len(pdf_files)} PDF files. Starting conversion...")

    for pdf_path in pdf_files:
        # Construct the output markdown path
        md_filename = pdf_path.stem + ".md"
        md_path = dest_dir / md_filename

        if md_path.exists() and md_path.stat().st_size > 0:
            print(f"Skipping {md_filename}, already exists")
            continue

        print(f"Converting: {pdf_path.name} -> {md_filename}")

        try:
            # Convert the file
            # In markitdown 0.1.0+, convert() handles file paths as strings or pathlib paths easily
            result = md_converter.convert(str(pdf_path))

            # Write the markdown content to the destination file
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(result.text_content)

            print(f"  Success: {md_filename}")
        except Exception as e:
            print(f"  Error converting {pdf_path.name}: {e}")

    print("Batch conversion completed.")


if __name__ == "__main__":
    main()
