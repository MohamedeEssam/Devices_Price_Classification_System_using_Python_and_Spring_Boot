from django.shortcuts import render, get_object_or_404
from .models import Device
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import models
from .apps import ResbaseConfig as r
from sklearn.preprocessing import MinMaxScaler
import pickle
from numpy import array
import pandas as pd 
import numpy as np



# Create your views here.

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'  # Include all fields


@api_view(['GET'])
def get_all_devices(request):
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_device_by_id(request, id):
    device = get_object_or_404(Device, pk=id)
    serializer = DeviceSerializer(device)
    return Response(serializer.data)

@api_view(['GET'])
def pred_by_id(request, id):
    device = get_object_or_404(Device, pk=id)  # Fetch device data
    device_data = device.__dict__  # Convert to dictionary
    del device_data['id']
    del device_data['_state']
    data = pd.DataFrame([device_data])
    # preprocessed_data = r.pre_proc.transform(data)
    
    return Response(r.svm.predict(data))
        
@api_view(['POST'])
def create_device(request):
    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Save the device data
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def predict(request):
    if request.method == 'POST':
        with open("model_svm.pkl", "rb") as f:
            model = pickle.load(f)
        # passenger_count = int(request.POST['passenger_count'])
        battery_power=int(request.POST['battery_power'])
        blue=int(request.POST['blue'])
        clock_speed=float(request.POST['clock_speed'])
        dual_sim=int(request.POST['dual_sim'])
        fc=int(request.POST['fc'])
        four_g=int(request.POST['four_g'])
        int_memory=int(request.POST['int_memory'])
        m_dep=float(request.POST['m_dep'])
        mobile_wt=int(request.POST['mobile_wt'])
        n_cores=int(request.POST['n_cores'])
        pc=int(request.POST['pc'])
        px_height=int(request.POST['px_height'])
        px_width=int(request.POST['px_width'])
        ram=int(request.POST['ram'])
        sc_h=int(request.POST['sc_h'])
        sc_w=int(request.POST['sc_w'])
        talk_time=int(request.POST['talk_time'])
        three_g=int(request.POST['three_g'])
        touch_screen=int(request.POST['touch_screen'])
        wifi=int(request.POST['wifi'])
        # Construct an instance of MinMaxScaler
        scaler = MinMaxScaler(feature_range=(1, 5))
        # # Normalization of selected columns
        

        scaler.fit_transform([[battery_power, clock_speed, fc, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time]])

        y_pred = model.predict([[battery_power, blue, clock_speed, dual_sim, fc,
       four_g, int_memory, m_dep, mobile_wt, n_cores, pc,
       px_height, px_width, ram, sc_h, sc_w, talk_time, three_g,
       touch_screen, wifi]])
        res=""
        if (y_pred==0):res="Low"
        elif(y_pred==1):res="Medium "
        elif(y_pred==2):res="Height "
        else: res="Very hight"
        return render(request, 'main.html', {'result':res})
    return render(request, 'main.html')


'''[[battery_power, blue, clock_speed, dual_sim, fc,
       four_g, int_memory, m_dep, mobile_wt, n_cores, pc,
       px_height, px_width, ram, sc_h, sc_w, talk_time, three_g,
       touch_screen, wifi]]'''