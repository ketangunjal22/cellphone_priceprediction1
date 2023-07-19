from Config import *
from Utils import *
from flask import Flask, jsonify, render_template, url_for, request
# from Utils.Cellphone

app = Flask(__name__)

@app.route('/Predict_price', methods = ['GET',"POST"])
def get_price():
    try:
        if request.method == 'GET':
            print("we are using GET method")

            Sale = int(request.args.get('Sale'))
            weight = float(request.args.get('weight'))
            resoloution = int(request.args.get('resoloution'))
            ppi = int(request.args.get('ppi'))
            cpu_core = int(request.args.int('cpu_core'))
            cpu_freq = float(request.args.get('cpu_freq'))
            internal_mem = int(request.args.get('internal_mem'))
            ram = float(request.args.get('ram'))
            RearCam = float(request.args.get('RearCam'))
            Front_Cam = int(request.args.get('Front_Cam'))
            battery = int(request.args.get('battery'))
            thickness = float(request.args.get('thickness'))

            cell = CellPhone()
            charges = cell.get_predictions(Sale,weight,resoloution,ppi,cpu_core,cpu_freq,internal_mem,ram,RearCam,Front_Cam,battery,thickness)

            return 'Price of Cell is:', charges
        
        if request.method == 'POST':
            print('we are using POST method')

            Sale = int(request.form.get('Sale'))
            weight = float(request.form.get('weight'))
            resoloution = int(request.form.get('resoloution'))
            ppi = int(request.form.get('ppi'))
            cpu_core = int(request.form.int('cpu_core'))
            cpu_freq = float(request.form.get('cpu_freq'))
            internal_mem = int(request.form.get('internal_mem'))
            ram = float(request.form.get('ram'))
            RearCam = float(request.form.get('RearCam'))
            Front_Cam = int(request.form.get('Front_Cam'))
            battery = int(request.form.get('battery'))
            thickness = float(request.form.get('thickness'))

            cell = CellPhone()
            charges = cell.get_predictions(Sale,weight,resoloution,ppi,cpu_core,cpu_freq,internal_mem,ram,RearCam,Front_Cam,battery,thickness)

            return 'Price of Cell is:', charges
        
    except:
        return 'Error!'




if __name__ == "__main__":
    app.run(host='0.0.0.0' , debug=True)       
