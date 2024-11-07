from flask import Flask,render_template,request

from utils import AutoCarPrice

app = Flask(__name__)

@app.route('/')

def hello_flask():
    print('Car Price Prediction...')
    return render_template('index.html')

@app.route('/predict_prices',methods=['POST','GET'])

def get_car_prices():
    
    if request.method == 'GET':
        
        print('We are in GET Method...')
        
        # data = request.form
        # normalized_losses = eval(data[normalized_losses])
        # make = data[make]
        # fuel_type = data[fuel_type]
        # aspiration = data[aspiration]
        # num_of_doors = data[num_of_doors]
        # body_style = data[body_style]
        # drive_wheels = data[drive_wheels]
        # engine_location = data[engine_location]
        # width = data[width]
        # engine_type = data[engine_type]
        # num_of_cylinders = data[num_of_cylinders]
        # engine_size = eval(data[engine_size])
        # fuel_system = data[fuel_system]
        # stroke = eval(data[stroke])
        # compression_ratio = eval(data[compression_ratio])
        # horsepower = eval(data[horsepower])
        # peak_rpm = eval(data[peak_rpm])
        # city_mpg = eval(data[city_mpg])
        # highway_mpg = eval(data[highway_mpg])
        
        normalized_losses = eval(request.args.get('normalized_losses'))
        make = request.args.get('make')
        fuel_type = request.args.get('fuel_type')
        aspiration = request.args.get('aspiration')
        num_of_doors = request.args.get('num_of_doors')
        body_style = request.args.get('body_style')
        drive_wheels = request.args.get('drive_wheels')
        engine_location = request.args.get('engine_location')
        width = request.args.get('width')
        engine_type = request.args.get('engine_type')
        num_of_cylinders = request.args.get('num_of_cylinders')
        engine_size = eval(request.args.get('engine_size'))
        fuel_system = request.args.get('fuel_system')
        stroke = eval(request.args.get('stroke'))
        compression_ratio = eval(request.args.get('compression_ratio'))
        horsepower = eval(request.args.get('horsepower'))
        peak_rpm = eval(request.args.get('peak_rpm'))
        city_mpg = eval(request.args.get('city_mpg'))
        highway_mpg = eval(request.args.get('highway_mpg'))
        
        
        car_price = AutoCarPrice(normalized_losses,make,fuel_type,aspiration,
                 num_of_doors,body_style,drive_wheels,
                 engine_location,width,engine_type,
                 num_of_cylinders,engine_size,
                 fuel_system,stroke,compression_ratio,
                 horsepower,peak_rpm,city_mpg,highway_mpg)
        
        price = car_price.get_predicted_price()
        
        return render_template('index.html',prediction = round(price,2))
        
        # return f'Car Price is : $ {round(price,2)}'
    
print('__name__ :',__name__)

if __name__ == '__main__':
    app.run()