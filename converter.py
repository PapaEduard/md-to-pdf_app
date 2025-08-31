import argparse
import os
import tempfile
from pathlib import Path

import markdown
from weasyprint import HTML, CSS


def convert_md_to_pdf(md_file_path, pdf_file_path):
    md_path = Path(md_file_path).absolute()
    pdf_path = Path(pdf_file_path).absolute()
    output_dir = md_path.parent

    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    html_content = markdown.markdown(
        md_content,
        extensions=['extra', 'tables', 'fenced_code', 'toc']
    )

    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
            img {{ max-width: 100%; height: auto; }}
            code {{ background: #f4f4f4; padding: 2px 5px; }}
            pre {{ background: #f4f4f4; padding: 15px; overflow: auto; }}
            table {{ border-collapse: collapse; width: 100%; }}
            table, th, td {{ border: 1px solid #ddd; padding: 8px; }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    HTML(string=full_html, base_url=str(output_dir)).write_pdf(
        pdf_path,
        stylesheets=[CSS(string='@page { margin: 1in; }')]
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF')
    parser.add_argument('input', help='Input Markdown file')
    parser.add_argument('output', help='Output PDF file')
    args = parser.parse_args()

    convert_md_to_pdf(args.input, args.output)
    print(f"Конвертация завершена: {args.output}")
