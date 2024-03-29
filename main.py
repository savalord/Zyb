from flask import Flask, request, render_template, send_file
import os
import exsel as ex
import Zip as z

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:\\Загрузочные файлы'




@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = file.filename
        print(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        ex.upload_excel(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        fio_list = ex.save_excel()
        z.download(os.path.join(app.config['UPLOAD_FOLDER'], filename) ,fio_list)
        return 'File uploaded successfully'
    else:
        return 'No file uploaded'


@app.route('/download',methods=['GET'])
def download_file():
    return send_file('Наряд-заказы.zip', as_attachment=True)



