import os
import socket

from flask import Flask, request, make_response
from werkzeug import secure_filename

from NMFtoWAVConverter import convert_to_wav

app = Flask(__name__)

@app.route("/")
def info():
    return "API rodando no container " + socket.gethostname()

@app.route("/nmftowav/upload", methods=['POST'])
def upload_nmf():
    try:
        for file in request.files.getlist('files'):
            nome_arquivo = os.path.splitext(file.filename)[0].replace(" ", "_")
            file_name = secure_filename(file.filename.replace(" ", "_"))
            file_target = os.path.join('/home/', file_name)
            file.save(file_target)
            convert_to_wav(os.path.join('/home/', file_name))

        with open('/home/' + nome_arquivo + '.wav', mode='rb') as file:
            file_content = file.read()

            response = make_response(file_content)
            response.headers['Content-type'] = 'audio/wav'
            response.headers['Content-Disposition'] = 'attachment; filename=''/home/' + nome_arquivo + '.wav'
            response.headers['Content-Length'] = os.stat('/home/' + nome_arquivo + '.wav').st_size

        os.remove('/home/' + nome_arquivo + '.wav')
        os.remove('/home/' + nome_arquivo + '.nmf')

        print ("Arquivo convertido com sucesso")
        return response
    except Exception as e:
        print (e)
        return ('{"error" : "%s" }' % e), 400


if __name__ == '__main__':
    app.run()
