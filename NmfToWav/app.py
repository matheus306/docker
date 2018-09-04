from flask import Flask, request, make_response
from werkzeug import secure_filename
from NMFtoWAVConverter import convert_to_wav
from subprocess import Popen, PIPE
from os.path import basename
import os
import io

app = Flask(__name__)

@app.route("/v1")
def teste():
    return "API rodando perfeitamente!"

@app.route("/v1/nmftowav/upload", methods=['POST'])
def upload_nmf():
	for file in request.files.getlist('files'):
		nome_arquivo = os.path.splitext(file.filename)[0]
		file_name = secure_filename(file.filename)
		file_target = os.path.join('/root/', file_name)
		file.save(file_target)
		convert_to_wav(os.path.join('/root/', file_name))


	with open('/root/' +nome_arquivo+ '.wav', mode='rb') as file:
		fileContent = file.read()

		response = make_response(fileContent)
		response.headers['Content-type'] = 'audio/wav'
		response.headers['Content-Disposition'] =  'attachment; filename=' + file_name + '.wav'
		response.headers['Content-Length'] = os.stat('/root/'+file_name).st_size
	return response



if __name__ == '__main__':
    app.run(debug=True, port=5000, host= '0.0.0.0')