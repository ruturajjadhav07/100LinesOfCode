#!/usr/bin/env python3
"""
Text to ePub Converter
Simple utility to convert plain text files to ePub format for e-readers
"""

import os
import sys
import argparse
import re
import uuid
from ebooklib import epub
from datetime import datetime

def parse_text_content(text_content):
    """Parse text content to extract title, author, and chapters"""
    title = "Untitled Book"
    author = "Unknown Author"
    
    # Try to extract title from first line
    lines = text_content.split('\n')
    if lines and lines[0].strip():
        title = lines[0].strip()
        lines = lines[1:]  # Remove title line
    
    # Try to extract author from next line if it starts with "by" or "author:"
    if lines and lines[0].strip().lower().startswith(('by ', 'author:')):
        author_line = lines[0].strip()
        author = author_line.split(' ', 1)[1].strip() if ' ' in author_line else author_line
        lines = lines[1:]  # Remove author line
    
    # Join remaining lines back
    content = '\n'.join(lines)
    
    # Split into chapters - look for chapter patterns
    chapter_pattern = re.compile(r'(?:chapter|section)\s+\d+', re.IGNORECASE)
    chapters = []
    
    # If we don't find chapters, check for double line breaks as section dividers
    if not chapter_pattern.search(content):
        parts = re.split(r'\n\s*\n\s*\n', content)
        for i, part in enumerate(parts):
            if part.strip():
                chapters.append((f"Section {i+1}", part.strip()))
    else:
        # Split by chapter headings
        parts = chapter_pattern.split(content)
        chapter_titles = chapter_pattern.findall(content)
        
        # First part is introduction if not empty
        if parts[0].strip():
            chapters.append(("Introduction", parts[0].strip()))
        
        # Add chapters
        for i, (title, content) in enumerate(zip(chapter_titles, parts[1:])):
            if content.strip():
                chapters.append((title.title(), content.strip()))
    
    return title, author, chapters

def text_to_epub(input_file, output_file=None):
    """Convert text file to ePub"""
    # Read text file
    with open(input_file, 'r', encoding='utf-8') as f:
        text_content = f.read()
    
    # Parse content
    title, author, chapters = parse_text_content(text_content)
    
    # Create ePub book
    book = epub.EpubBook()
    
    # Set metadata
    book.set_identifier(str(uuid.uuid4()))
    book.set_title(title)
    book.set_language('en')
    book.add_author(author)
    
    # Set cover
    book.set_cover("cover.jpg", open("cover.jpg", "rb").read()) if os.path.exists("cover.jpg") else None
    
    # Create chapters
    epub_chapters = []
    toc = []
    spine = ['nav']
    
    for i, (chapter_title, chapter_content) in enumerate(chapters):
        chapter_id = f'chapter_{i+1}'
        chapter = epub.EpubHtml(title=chapter_title, file_name=f'{chapter_id}.xhtml')
        chapter.content = f'<h1>{chapter_title}</h1><p>{chapter_content.replace(chr(10), "</p><p>")}</p>'
        
        book.add_item(chapter)
        epub_chapters.append(chapter)
        toc.append(epub.Link(f'{chapter_id}.xhtml', chapter_title, chapter_id))
        spine.append(chapter)
    
    # Add navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    # Define Table of Contents
    book.toc = toc
    
    # Add spine
    book.spine = spine
    
    # Generate output filename if not provided
    if not output_file:
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = f"{base_name}.epub"
    
    # Write ePub file
    epub.write_epub(output_file, book)
    print(f"Created ePub: {output_file}")
    return output_file

def main():
    parser = argparse.ArgumentParser(description='Convert text files to ePub format')
    parser.add_argument('input_file', help='Path to the input text file')
    parser.add_argument('-o', '--output', help='Path to the output ePub file (optional)')
    
    args = parser.parse_args()
    text_to_epub(args.input_file, args.output)

if __name__ == "__main__":
    main()
