from flask import Flask, request, Response
from xhtml2pdf import pisa
import os.path

app = Flask(__name__)


@app.route('/', methods=['POST'])
def query():
    html_code = request.get_data().decode('UTF-8')
    output_filename = "test.pdf"

    def convert_html_to_pdf(html_code, output_filename):

        with open(output_filename, "w+b") as res_file:
            pisa_status = pisa.CreatePDF(html_code, dest=res_file)

        return pisa_status.err

    pisa.showLogging()
    convert_html_to_pdf(html_code, output_filename)

    with open(os.path.abspath(output_filename), 'rb') as f:
        pdf_data = f.read()
    return Response(pdf_data, mimetype='application/pdf')


if __name__ == '__main__':
    app.run(debug=False, port=5000)
