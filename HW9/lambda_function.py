import tflite_runtime.interpreter as tflite

import numpy as np

from io import BytesIO
from urllib import request

from PIL import Image

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

interpreter = tflite.Interpreter(model_path='bees-wasps-v2.tflite')
interpreter.allocate_tensors()

in_index = interpreter.get_input_details()[0]['index']
out_index = interpreter.get_output_details()[0]['index']

def predict(url):
    img = download_image(url)
    img = prepare_image(img, (150,150))
    img = np.array(img, dtype='float32')
    X = np.array([img])
    X /= 255
    
    interpreter.set_tensor(in_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(out_index)

    return float(preds[0][0])

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result