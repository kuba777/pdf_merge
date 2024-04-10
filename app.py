from flask import Flask, render_template, request, send_file
from io import BytesIO
from PyPDF2 import PdfMerger


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def merge_pdfs():
    if request.method == 'POST':
        
        # get the selected pdf files

        pdf_files = request.files.getlist("pdf_files")

        merger = PdfMerger()
        
        for pdf in pdf_files:
            merger.append(pdf)
            print(pdf)

        buffer = BytesIO()

        merger.write(buffer)

        buffer.seek(0)

        return send_file(buffer, as_attachment=True, download_name='merged_pdfs')

    else:
    
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
