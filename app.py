from flask import Flask,render_template,url_for,request
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from keras.preprocessing.image import array_to_img
from numpy import expand_dims
from matplotlib import pyplot
import os
import random

app = Flask(__name__)
value = ""
FILE_NAME = ""
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')
@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')
@app.route('/canvas',methods=['GET','POST'])
def canvas():
    return render_template('upload.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    target = os.path.join(APP_ROOT, 'static/')
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        file_name = upload.filename
        destination = "/".join([target,file_name])
        print("Accept incoming file: ",file_name)
        print("Save it to: ",destination)
        upload.save(destination)
        global FILE_NAME
        FILE_NAME = file_name
    return (render_template("complete.html", image_name = file_name))


@app.route('/view',methods=['GET','POST'])
def view():
    
    value = random.randint(1,1000)
    value = str(value)
    def load_image(filename, size=(256,256)):
        # load image with the preferred size
        pixels = load_img(filename, target_size=size)
        # convert to numpy array
        pixels = img_to_array(pixels)
        # scale from [0,255] to [-1,1]
        pixels = (pixels - 127.5) / 127.5
        # reshape to 1 sample
        pixels = expand_dims(pixels, 0)
        return pixels
    if request.method == 'GET':
        #E:/256x256/sketch/tx_000000001010/shoe/n02882894_1916-1.png
        #C:/Users/BIPIN/Desktop/s2ipix/vals/img10_AB.jpg.jpg
        #"C:/Users/BIPIN/Desktop/s2i/static"
        sketch_path = os.path.join('static', FILE_NAME)
        src_image = load_image(sketch_path)
        # load model
        model = load_model('C:/Users/BIPIN/Desktop/s2i/data/model_0020640.h5')
        # generate image from source
        gen_image = model.predict(src_image)
        # scale from [-1,1] to [0,1]
        gen_image = (gen_image + 1) / 2.0
        img = (array_to_img(gen_image[0]))
        img.save("C:/Users/BIPIN/Desktop/s2i/static/GEN/gen_image%s.jpg" % (value)) #img%s.jpg" % (filename)
    PEOPLE_FOLDER = os.path.join('static', 'GEN')
    app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'gen_image%s.jpg' % (value)) #url_for("user_image", filename=user.image)
    return render_template('view.html',value=value,user_image =full_filename)

@app.route('/view2',methods=['GET','POST'])
def view2():
    
    value = random.randint(1,1000)
    value = str(value)
    def load_image(filename, size=(256,256)):
        # load image with the preferred size
        pixels = load_img(filename, target_size=size)
        # convert to numpy array
        pixels = img_to_array(pixels)
        # scale from [0,255] to [-1,1]
        pixels = (pixels - 127.5) / 127.5
        # reshape to 1 sample
        pixels = expand_dims(pixels, 0)
        return pixels
    if request.method == 'GET':
        #E:/256x256/sketch/tx_000000001010/shoe/n02882894_1916-1.png
        #C:/Users/BIPIN/Desktop/s2ipix/vals/img10_AB.jpg.jpg
        #"C:/Users/BIPIN/Desktop/s2i/static"
        sketch_path = os.path.join('static', FILE_NAME)
        src_image = load_image(sketch_path)
        # load model
        model = load_model('C:/Users/BIPIN/Desktop/s2i/data/model_0119900.h5')
        # generate image from source
        gen_image = model.predict(src_image)
        # scale from [-1,1] to [0,1]
        gen_image = (gen_image + 1) / 2.0
        img = (array_to_img(gen_image[0]))
        img.save("C:/Users/BIPIN/Desktop/s2i/static/GEN/gen_image%s.jpg" % (value)) #img%s.jpg" % (filename)
    PEOPLE_FOLDER = os.path.join('static', 'GEN')
    app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'gen_image%s.jpg' % (value)) #url_for("user_image", filename=user.image)
    return render_template('view2.html',value=value,user_image =full_filename)


if __name__ == '__main__':
    app.run(debug=True)