from flask import Flask, request, jsonify,send_from_directory,send_file
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'csv','xlsx','html'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route( '/' ) 
def  home (): 
    return  'Olá, Mundo!' 

@app.route( '/upload' , methods=[ 'POST' , 'GET' ] ) 
def  fileUpload (): 
    if request.method == 'POST' : 
        file = request.files.getlist( 'files' ) 
        filename = "" 
        print (request.files, "...." ) 
        for f in file: 
            print (f.filename) 
            filename = secure_filename(f.filename) 
            print (allowed_file(filename)) 
            if allowed_file(filename): 
                f.save(os.path.join(app.config[ 'UPLOAD_FOLDER' ], filename)) 
            else : 
                return jsonify({ 'message' : 'Tipo de arquivo não permitido' }), 400 
        return jsonify({ "name" : filename, "status" : "success" },200) 
    else :
        return jsonify({ "status" : "Carregar solicitação GET da API em execução" })




@app.route('/download/<filename>')
def download_file(filename):
    # ... (código para fazer o download do arquivo)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
