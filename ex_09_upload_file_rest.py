import os
from flask import Flask, request,jsonify, send_from_directory
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/albert/tmp/filestore'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

import json

app = Flask(__name__) #Die Flask-Anwendung
api = Api(app) #Die Flask API


def allowed_file(filename):
    '''
    :param filename:
    :return: true if filename has any of the supported extensions
    '''
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class File(Resource):
    def get(self, id):
        filename = secure_filename(id)
        return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)
    def put(self, id):
        filename = secure_filename(id)
        with open(os.path.join(UPLOAD_FOLDER, filename), "wb") as fp:
            fp.write(request.data)
        return jsonify({'message' : 'file stored'})
    def delete(self,id):
        filename = secure_filename(id)
        filename = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(filename):
            os.remove(filename)
            return jsonify({'message': '%s deleted' % id})
        else:
            return jsonify({'message': 'File does not exist: %s' % id})

class Filestore(Resource):
    def get(self):
        return jsonify(os.listdir(UPLOAD_FOLDER))

api.add_resource(File, '/file/<string:id>')
api.add_resource(Filestore, '/files/')

if __name__ == '__main__':
    app.run(debug=True)
