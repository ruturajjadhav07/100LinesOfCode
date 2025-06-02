# Text to ePub Converter

A simple utility that converts plain text files to ePub format for e-readers.

## Features

- Converts text files to ePub format compatible with most e-readers
- Automatically extracts title and author information from the text
- Detects chapters based on common patterns like "Chapter X" or double line breaks
- Formats text with proper paragraphs and headings
- Generates a table of contents
- Keeps everything under 100 lines of code!

## Requirements

- Python 3.6+
- EbookLib

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Basic usage:

```bash
python text_to_epub.py sample.txt
```

Specify output file:

```bash
python text_to_epub.py sample.txt -o my_book.epub
```

## Text Format Tips

For best results, format your text file as follows:

1. First line: Book title
2. Second line: "By Author Name" or "Author: Author Name"
3. Use "CHAPTER X" or "Section X" on their own lines to mark chapter breaks
4. Alternatively, use double blank lines to separate sections
5. For a custom cover, place a file named "cover.jpg" in the same directory

## Example

See the included `sample.txt` for an example text file that works well with this converter.

## License

This project is part of the 100LinesOfCode repository and follows its licensing.
