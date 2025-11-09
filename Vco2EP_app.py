from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle

app = Flask(__name__)
model = pickle.load(open("Vehicle_CO2_Emission_Predictor_v1.1.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("WebApp.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        vehicle_brand = request.form['Vehicle Brand']
        if vehicle_brand == 'ACURA':
            vehicle_brand = 0
        elif vehicle_brand == 'ALFA ROMEO':
            vehicle_brand = 1
        elif vehicle_brand == 'ASTON MARTIN':
            vehicle_brand = 2
        elif vehicle_brand == 'AUDI':
            vehicle_brand = 3
        elif vehicle_brand == 'BENTLEY':
            vehicle_brand = 4
        elif vehicle_brand == 'BMW':
            vehicle_brand = 5
        elif vehicle_brand == 'BUGATTI':
            vehicle_brand = 6
        elif vehicle_brand == 'BUICK':
            vehicle_brand = 7
        elif vehicle_brand == 'CADILLAC':
            vehicle_brand = 8
        elif vehicle_brand == 'CHEVROLET':
            vehicle_brand = 9
        elif vehicle_brand == 'CHRYSLER':
            vehicle_brand = 10
        elif vehicle_brand == 'DODGE':
            vehicle_brand = 11
        elif vehicle_brand == 'FIAT':
            vehicle_brand = 12
        elif vehicle_brand == 'FORD':
            vehicle_brand = 13
        elif vehicle_brand == 'GENESIS':
            vehicle_brand = 14
        elif vehicle_brand == 'GMC':
            vehicle_brand = 15
        elif vehicle_brand == 'HONDA':
            vehicle_brand = 16
        elif vehicle_brand == 'HYUNDAI':
            vehicle_brand = 17
        elif vehicle_brand == 'INFINITI':
            vehicle_brand = 18
        elif vehicle_brand == 'JAGUAR':
            vehicle_brand = 19
        elif vehicle_brand == 'JEEP':
            vehicle_brand = 20
        elif vehicle_brand == 'KIA':
            vehicle_brand = 21
        elif vehicle_brand == 'LAMBORGHINI':
            vehicle_brand = 22
        elif vehicle_brand == 'LAND ROVER':
            vehicle_brand = 23
        elif vehicle_brand == 'LEXUS':
            vehicle_brand = 24
        elif vehicle_brand == 'LINCOLN':
            vehicle_brand = 25
        elif vehicle_brand == 'MASERATI':
            vehicle_brand = 26
        elif vehicle_brand == 'MAZDA':
            vehicle_brand = 27
        elif vehicle_brand == 'MERCEDES-BENZ':
            vehicle_brand = 28
        elif vehicle_brand == 'MINI':
            vehicle_brand = 29
        elif vehicle_brand == 'MITSUBISHI':
            vehicle_brand = 30
        elif vehicle_brand == 'NISSAN':
            vehicle_brand = 31
        elif vehicle_brand == 'PORSCHE':
            vehicle_brand = 32
        elif vehicle_brand == 'RAM':
            vehicle_brand = 33
        elif vehicle_brand == 'ROLLS-ROYCE':
            vehicle_brand = 34
        elif vehicle_brand == 'SCION':
            vehicle_brand = 35
        elif vehicle_brand == 'SMART':
            vehicle_brand = 36
        elif vehicle_brand == 'SRT':
            vehicle_brand = 37
        elif vehicle_brand == 'SUBARU':
            vehicle_brand = 38
        elif vehicle_brand == 'TOYOTA':
            vehicle_brand = 39
        elif vehicle_brand == 'VOLKSWAGEN':
            vehicle_brand = 40
        else:
            vehicle_brand = 41
            
            
        vehicle_class = request.form['Vehicle Class']
        if vehicle_class == 'COMPACT':
            vehicle_class = 0
        elif vehicle_class == 'FULL-SIZE':
            vehicle_class = 1
        elif vehicle_class == 'MID-SIZE':
            vehicle_class = 2
        elif vehicle_class == 'MINICOMPACT':
            vehicle_class = 3
        elif vehicle_class == 'MINIVAN':
            vehicle_class = 4
        elif vehicle_class == 'PICKUP TRUCK - SMALL':
            vehicle_class = 5
        elif vehicle_class == 'PICKUP TRUCK - STANDARD':
            vehicle_class = 6
        elif vehicle_class == 'SPECIAL PURPOSE VEHICLE':
            vehicle_class = 7
        elif vehicle_class == 'STATION WAGON - MID-SIZE':
            vehicle_class = 8
        elif vehicle_class == 'STATION WAGON - SMALL':
            vehicle_class = 9
        elif vehicle_class == 'SUBCOMPACT':
            vehicle_class = 10
        elif vehicle_class == 'SUV - SMALL':
            vehicle_class = 11
        elif vehicle_class == 'SUV - STANDARD':
            vehicle_class = 12
        elif vehicle_class == 'TWO-SEATER':
            vehicle_class = 13
        elif vehicle_class == 'VAN - CARGO':
            vehicle_class = 14
        else:
            vehicle_class = 15
            
            
        engine_size = float(request.form['Engine Size'])
        cylinders = int(request.form['Cylinders'])
        
        fuel_type = request.form['Fuel Type']
        if fuel_type == 'Diesel':
            fuel_type = 0
        elif fuel_type == 'Ethanol (E85)':
            fuel_type = 1
        elif fuel_type == 'Natural Gas':
            fuel_type = 2
        elif fuel_type == 'Regular Gasoline':
            fuel_type = 3
        else:
            fuel_type = 4
            
            
        fuel_consumption_city_roads = float(request.form['Fuel Consumption City Roads'])
        fuel_consumption_highways = float(request.form['Fuel Consumption Highways'])
        fuel_consumption_combined = (fuel_consumption_city_roads + fuel_consumption_highways) / 2
        fuel_consumption_combined_mpg = 282.481 / fuel_consumption_combined
        
        transmission_type = request.form['Transmission Type']
        if transmission_type == 'Automatic':
            transmission_type = 0
        elif transmission_type == 'Automated Manual':
            transmission_type = 1
        elif transmission_type == 'Automatic with Select Shift':
            transmission_type = 2
        elif transmission_type == 'Continuously Variable':
            transmission_type = 3
        else:
            transmission_type = 4
            
            
        no_of_gears = request.form['Number of Gears']
        if no_of_gears == '3':
            no_of_gears = 3
        elif no_of_gears == '4':
            no_of_gears = 4
        elif no_of_gears == '5':
            no_of_gears = 5
        elif no_of_gears == '6':
            no_of_gears = 6
        elif no_of_gears == '7':
            no_of_gears = 7
        elif no_of_gears == '8':
            no_of_gears = 8
        elif no_of_gears == '9':
            no_of_gears = 9
        else:
            no_of_gears = 10
        
        predicted_price = model.predict([[vehicle_brand, vehicle_class, engine_size, cylinders, fuel_type, fuel_consumption_city_roads, fuel_consumption_highways, fuel_consumption_combined, fuel_consumption_combined_mpg, transmission_type, no_of_gears]])

        return render_template('WebApp.html', prediction_text=f'{predicted_price[0]:.3f} g/km')

    return render_template("WebApp.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)