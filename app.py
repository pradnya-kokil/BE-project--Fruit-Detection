import os
import uuid
import flask
import urllib
from PIL import Image
from tensorflow.keras.models import load_model
from flask import Flask , render_template  , request , send_file
from tensorflow.keras.preprocessing.image import load_img , img_to_array

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = load_model(os.path.join(BASE_DIR , 'tlfinal.h5'))


ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'jfif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT

classes = os.listdir('fruits-360_dataset/fruits-360/Training')
 
 

def predict(filename , model):
    img = load_img(filename , target_size = (100, 100))
    img = img_to_array(img)
    img = img.reshape(1 , 100,100 ,3)

    img = img.astype('float32')
    img = img/255.0
    result = model.predict(img)

    dict_result = {}

    for i in range(131):
        dict_result[result[0][i]] = classes[i]
        

    res = result[0]
    res.sort()
    res = res[::-1]
    prob = res[:3]
    cal_result=[]
    prob_result = []
    class_result = []
    
    for i in range(1):
        prob_result.append((prob[i]*100).round(2))
        class_result.append(dict_result[prob[i]])
        
    if class_result[0]=="Apple Braeburn":
        cal=87
    elif class_result[0]=="Tomato 1" or class_result[0]=="Tomato 2" or class_result[0]=="Tomato 3":
        cal=33
    elif class_result[0]=="Potato White":
        cal=77
    elif class_result[0]=="Kiwi":
        cal=61
    elif class_result[0]=="Eggplant":
        cal=25
    elif class_result[0]=="Pear" or class_result[0]=="Pear 2":
        cal=57
    elif class_result[0]=="Ginger Root":
        cal=80  
    elif class_result[0]=="Grapefruit White":
        cal=42
    elif class_result[0]=="Pinapple":
        cal=50
    elif class_result[0]=="Lemon":
        cal=29
    elif class_result[0]=="Orange":
        cal=47
    elif class_result[0]=="Strawberry":
        cal=33
    elif class_result[0]=="Mango":
        cal=135
    elif class_result[0]=="Avacado":
        cal=160
    elif class_result[0]=="Apple Golden 3" or class_result[0]=="Apple Golden 1" or class_result[0]=="Apple Golden 2" :
        cal=73
    elif class_result[0]=="Blueberry":
        cal=84
    elif class_result[0]=="Apple Granny Smith":
        cal=83
    elif class_result[0]=="Apple Red 1" or class_result[0]=="Apple Red 2" or class_result[0]=="Apple Red 3" :
        cal=72
    elif class_result[0]=="Apple Red Yellow 1" or class_result[0]=="Apple Red Yellow 2" :
        cal=60
    elif class_result[0]=="Banana":
        cal=89
    elif class_result[0]=="Corn Husk":
        cal=106
    elif class_result[0]=="Plum" or class_result[0]=="Plum 2" or class_result[0]=="Plum 3" :
        cal=46
    elif class_result[0]=="Peach" or class_result[0]=="Peach 2" :
        cal=68
    elif class_result[0]=="Cucumber Ripe" or class_result[0]=="Cucumber Ripe 2" :
        cal=30
    elif class_result[0]=="Pear Stone":
        cal=101
    elif class_result[0]=="Peach Flat":
        cal=50
    elif class_result[0]=="Fig":
        cal=37
    elif class_result[0]=="Apricot":
        cal=48
    elif class_result[0]=="Watermelon":
        cal=30
    elif class_result[0]=="Nectarine":
        cal=44
    elif class_result[0]=="Cauliflower":
        cal=25
    elif class_result[0]=="Pomegranate":
        cal=64
    elif class_result[0]=="Pear Forelle":
        cal=100
    elif class_result[0]=="Papaya":
        cal=39
    elif class_result[0]=="Pepper Orange":
        cal=31
    elif class_result[0]=="Cherry 1" :
        cal=50
    elif class_result[0]=="Tomato Cherry Red":
        cal=41
    elif class_result[0]=="Onion Red":
        cal=32
    elif class_result[0]=="Carambula":
        cal=41
    elif class_result[0]=="Beetroot":
        cal=60
    elif class_result[0]=="Cactus Fruit":
        cal=42
    elif class_result[0]=="Nectarine Flat":
        cal=45
    elif class_result[0]=="Granadillla":
        cal=97
    elif class_result[0]=="Nut Forest":
        cal=514
    elif class_result[0]=="Kaki":
        cal=127
    elif class_result[0]=="Onion Red Peeled":
        cal=40
    elif class_result[0]=="Onion White":
        cal=40
    elif class_result[0]=="Kumquats":
        cal=71
    elif class_result[0]=="Potato Red":
        cal=123  
    elif class_result[0]=="Passion Fruit":
        cal=97
    elif class_result[0]=="Potato Red Washed":
        cal=151
    elif class_result[0]=="Avacado ripe":
        cal=250
    elif class_result[0]=="Quince":
        cal=57
    elif class_result[0]=="Potato White":
        cal=67
    elif class_result[0]=="Potato Sweet":
        cal=86
    elif class_result[0]=="Clementine":
        cal=47
    elif class_result[0]=="Apple Crimson Snow":
        cal=100
    elif class_result[0]=="Apple Pink Lady":
        cal=80
    elif class_result[0]=="Cocos":
        cal=150
    elif class_result[0]=="Mango Red":
        cal=70
    elif class_result[0]=="Limes":
        cal=30
    elif class_result[0]=="Pepper Red":
        cal=31
    elif class_result[0]=="Pepper Green" or class_result[0]=="Pepper Yellow" or class_result[0]=="Pepper Orange":
        cal=20
    elif class_result[0]=="Apple Red Delicious":
        cal=72
    elif class_result[0]=="Pomelo Sweetie":
        cal=231
    elif class_result[0]=="Banana Lady Finger":
        cal=140
    elif class_result[0]=="Chestnut":
        cal=131
    elif class_result[0]=="Pear Monster":
        cal=121
    elif class_result[0]=="Mangostan":
        cal=143
    elif class_result[0]=="Nut Pecan":
        cal=690
    elif class_result[0]=="Grape White" or class_result[0]=="Grape White 2" or class_result[0]=="Grape White 3" or class_result[0]=="Grape White 4" :
        cal=69
    elif class_result[0]=="Pear Kaiser":
        cal=100
    elif class_result[0]=="Tomato Yellow":
        cal=32
    elif class_result[0]=="Apple Red Yellow 1" or class_result[0]=="Apple Red Yellow 2":
        cal=252
    elif class_result[0]=="Grapefruit Pink":
        cal=52
    elif class_result[0]=="Tangelo":
        cal=47
    elif class_result[0]=="Grape Blue":
        cal=30
    elif class_result[0]=="Huckleberry":
        cal=37
    elif class_result[0]=="Raspberry":
        cal=53
    elif class_result[0]=="Plum 3" or class_result[0]=="Plum 2":
        cal=90
    elif class_result[0]=="Dates":
        cal=282
    elif class_result[0]=="Maracuja":
        cal=97
    elif class_result[0]=="Tomato Maroon":  
        cal=95.1
    elif class_result[0]=="Cherry Wax Yellow" or class_result[0]=="Cherry Wax Black" or class_result[0]=="Cherry Wax Red":
        cal=87
    elif class_result[0]=="Salak":
        cal=82
    elif class_result[0]=="Hazelnut":
        cal=628
    elif class_result[0]=="Tamarillo":
        cal=30
    elif class_result[0]=="Walnut":
        cal=654
    elif class_result[0]=="Guava":
        cal=68
    elif class_result[0]=="Lemon Meyer":
        cal=20
    elif class_result[0]=="Mulberry":
        cal=43
    elif class_result[0]=="Banana Red":
        cal=90
    elif class_result[0]=="Redcurrant":
        cal=68
    elif class_result[0]=="Pineapple Mini":
        cal=189
    elif class_result[0]=="Pepino":
        cal=46
    elif class_result[0]=="Physalis":
        cal=53
    elif class_result[0]=="Pitahaya Red":
        cal=60
    elif class_result[0]=="Physalis with Husk":
        cal=53
    elif class_result[0]=="Pear Abate":
        cal=40
    elif class_result[0]=="Rambutan":
        cal=75
    elif class_result[0]=="Pear Williams" or class_result[0]=="Pear Red" :
        cal=54
    elif class_result[0]=="Melon Piel de Sapo":
        cal=34
    elif class_result[0]=="Cantaloupe 1" or class_result[0]=="Cantaloupe 2" :
        cal=60
    elif class_result[0]=="Cherry Rainier":
        cal=90
    elif class_result[0]=="Cherry 2":
        cal=63
    elif class_result[0]=="Strawberry Wedge":
        cal=32
    elif class_result[0]=="Corn":
        cal=96

    else:
        cal=0
    
    for i in range(1):
         cal_result.append(cal)
    return class_result , prob_result , cal_result




@app.route('/')
def home():
        return render_template("index.html")

@app.route('/success' , methods = ['GET' , 'POST'])
def success():
    error = ''
    target_img = os.path.join(os.getcwd() , 'static/images')
    if request.method == 'POST':
        if(request.form):
            link = request.form.get('link')
            try :
                resource = urllib.request.urlopen(link)
                unique_filename = str(uuid.uuid4())
                filename = unique_filename+".jpg"
                img_path = os.path.join(target_img , filename)
                output = open(img_path , "wb")
                output.write(resource.read())
                output.close()
                img = filename

                class_result , prob_result, cal_result = predict(img_path , model)

                predictions = {
                      "class1":class_result[0],
                      "prob1": prob_result[0],
                      "cal1":cal_result[0],

                }

            except Exception as e : 
                print(str(e))
                error = 'This image from this site is not accesible or inappropriate input'

            if(len(error) == 0):
                return  render_template('success.html' , img  = img , predictions = predictions)
            else:
                return render_template('index.html' , error = error) 

            
        elif (request.files):
            file = request.files['file']
            if file and allowed_file(file.filename):
                file.save(os.path.join(target_img , file.filename))
                img_path = os.path.join(target_img , file.filename)
                img = file.filename

                class_result , prob_result, cal_result = predict(img_path , model)

                predictions = {
                      "class1":class_result[0],
                       "prob1": prob_result[0],
                       "cal1":cal_result[0], 
                }

            else:
                error = "Please upload images of jpg , jpeg and png extension only"

            if(len(error) == 0):
                return  render_template('success.html' , img  = img , predictions = predictions)
            else:
                return render_template('index.html' , error = error)

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)


