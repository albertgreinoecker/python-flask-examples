import base64
import requests

def encode_base64(fName):
    with open(fName, 'rb') as file:
        binary_file_data = file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        return base64_encoded_data.decode('utf-8')

def decode_Base64(fName, data):
    data_base64 = data.encode('utf-8')
    with open(fName, 'wb') as file:
        decoded_data = base64.decodebytes(data_base64)
        file.write(decoded_data)


if __name__ == '__main__':
    #Test encode and decode here:
    enc = encode_base64('test_files/htl-logo.png')
    print(enc)
    decode_Base64('/tmp/img.png', enc)

    #store encoded image with metadata
    j = {'name': 'image', 'ext': 'png', 'data': enc, 'desc': 'This is an example image'}
    response = requests.put('http://localhost:5000/img_meta/0' , json=j)
    print(response)
    res_json = response.json()
    print(res_json)
    decode_Base64('/tmp/htl-logo-from-server.png', res_json['data'])

    response = requests.get('http://localhost:5000/img_meta/3')
    res_json = response.json()
    print(res_json)
    decode_Base64('/tmp/htl-logo-from-server2.png', res_json['data'])