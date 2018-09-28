import os
import socket
import uuid

from flask import Flask, request, make_response

from NMFtoWAVConverter import convert_to_wav

app = Flask(__name__)

@app.route("/")
def info():
    return "API rodando no container " + socket.gethostname()

@app.route("/nmftowav/upload", methods=['POST'])
def upload_nmf():
    try:

        directory = os.path.join('/nmf/')

        for file in request.files.getlist('files'):
            nome_arquivo = os.path.splitext(file.filename)[0].replace(" ", "_")
            file_name_random = str(uuid.uuid4())

            convert_to_wav(file.read(), os.path.join(directory + '/', file_name_random + ".nmf"))

        with open(directory + '/' + file_name_random + '.wav', mode='rb') as file:
            file_content = file.read()
            response = make_response(file_content)
            response.headers['Content-type'] = 'audio/wav'
            response.headers['Content-Disposition'] = 'attachment; filename=' + nome_arquivo + '.wav'
            response.headers['Content-Length'] = os.stat(directory + '/' + file_name_random + '.wav').st_size

        os.remove(directory + '/' + file_name_random + ".wav")

        print ("Arquivo convertido com sucesso")
        return response
    except Exception as e:
        print (e)
        return ('{"error" : "%s" }' % e), 400


if __name__ == '__main__':
    app.run(threaded=True, port=80)
