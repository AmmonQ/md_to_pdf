import azure.functions as func
import logging
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.function_name(name="quackmd2pdf")
@app.route(route="convert")
def convert(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    md_content = req.params.get('md_content')
    if not md_content:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            md_content = req_body.get('md_content')

    if md_content:
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        flowables = [Paragraph(md_content, styles['Normal'])]

        doc.build(flowables)
        pdf = buffer.getvalue()
        buffer.close()

        headers = {
            "Content-Disposition": "attachment;filename=example.pdf",
            "Content-Type": "application/pdf"
        }

        return func.HttpResponse(pdf, headers=headers)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )