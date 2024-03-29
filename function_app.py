import azure.functions as func
import logging
from txt2pdf.core import txt2pdf

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.function_name(name="quackmd2pdf")
@app.route(route="convert")
def convert(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    markdown_file_path = req.params.get('md_file_path')
    if not markdown_file_path:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            markdown_file_path = req_body.get('markdown_file_path')

    if markdown_file_path:
        # txt2pdf(
        #     pdf_file_path="/home/ammon/PycharmProjects/MarkdownToPDF/output/output.pdf",
        #     md_content=None,
        #     md_file_path=markdown_file_path,
        #     css_file_path=None,
        #     base_url=None,
        #     print_html_to_stdout=False,
        # )
        return func.HttpResponse(f"Markdown file path: {markdown_file_path}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )