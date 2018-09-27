import os
import shutil
import socket
from datetime import datetime

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
        directory = '/home/' + datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]
        if not os.path.exists(directory):
            os.makedirs(directory)

        for file in request.files.getlist('files'):
            nome_arquivo = os.path.splitext(file.filename)[0].replace(" ", "_")
            file_name = secure_filename(file.filename.replace(" ", "_"))
            file_target = os.path.join(directory + '/', file_name)
            file.save(file_target)
            convert_to_wav(os.path.join(directory + '/', file_name))

        with open(directory + '/' + nome_arquivo + '.wav', mode='rb') as file:
            file_content = file.read()

            response = make_response(file_content)
            response.headers['Content-type'] = 'audio/wav'
            response.headers['Content-Disposition'] = 'attachment; filename=''/home/' + nome_arquivo + '.wav'
            response.headers['Content-Length'] = os.stat('/' + directory + '/' + nome_arquivo + '.wav').st_size

            shutil.rmtree(directory)

        print ("Arquivo convertido com sucesso")
        return response
    except Exception as e:
        print (e)
        return ('{"error" : "%s" }' % e), 400


if __name__ == '__main__':
    app.run(threaded=True)
