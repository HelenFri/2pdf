from flask import Flask, request, Response, render_template
import os.path
import pdfkit


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/to_pdf', methods=['POST'])
def query_to_pdf():
    root_dir = os.getcwd()
    subfolder_dir = root_dir + '/to_pdf'

    if request.method == 'POST':
        html_code = request.get_data().decode('UTF-8')

        with open(os.path.join(subfolder_dir, 'temp.html'), 'w', encoding='utf-8') as file:
            file.write(html_code)

    path = os.path.join(subfolder_dir, 'temp.html')

    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdfkit.from_file(path, os.path.join(subfolder_dir, 'res_pdf.pdf'), configuration=config)

    with open(os.path.join(subfolder_dir, 'res_pdf.pdf'), 'rb') as f:
        pdf_data = f.read()
    return Response(pdf_data, mimetype='application/pdf')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

