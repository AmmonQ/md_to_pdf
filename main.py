from txt2pdf.core import txt2pdf

markdown_file_path = input("Enter Markdown file path: ")

txt2pdf(
    pdf_file_path="/home/ammon/PycharmProjects/MarkdownToPDF/output/output.pdf",
    md_content=None,
    md_file_path=markdown_file_path,
    css_file_path=None,
    base_url=None,
    print_html_to_stdout=False,
)