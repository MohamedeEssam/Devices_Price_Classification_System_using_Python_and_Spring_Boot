# Devices-Price-Classification-System-using-Python-and-Django
Devices Price Classification System (AI System) using Python and linked with Django
Mainly the system include two small projects:
* Python project: will allow you to predict the prices, allowing the sellers to classify the device's prices according to their characteristics
* Django project: Will contain a simple entity, and a few endpoints, to call the service from the Python project for a bunch of test cases, and store them.
  EndPoints: 
* POST /api/devices/: Retrieve a list of all devices
* GET /api/devices/{id}: Retrieve details of a specific device by ID.
* POST /api/devices: Add a new device.
* POST /api/predict/{deviceId}

## The recorded video

Please check the folder of recorded video to see the run of my project

# How to run : 
Go to django side and type the following command 

1. install requirements

```CMD
pip install -r requirements.txt
```

2.  migrate the project

```CMD
python manage.py migrate
or 
python manage.py makemigrate
```

3. runserver

``` CMD
python manage.py runserver
```

Then four endpoints can be accessed : 
1. Adding a new device
2. Getting a list of all the devices
3. Getting a device from id
4. Predict the device price range based on the id
5. Predict the device price range based on the data

"# Devices_Price_Classification_System_using_Python_and_Spring_Boot" 
