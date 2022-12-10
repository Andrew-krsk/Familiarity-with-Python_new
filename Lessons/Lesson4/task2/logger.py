from datetime import datetime as dt

def temperature_logger(data):
    with open('log.csv', 'a') as file:
        time = dt.now().strftime('%H:%M')
        file.write('{};temperature;{}\n'.format(time, data))

def preassure_logger(data):
    with open('log.csv', 'a') as file:
        time = dt.now().strftime('%H:%M')
        file.write('{};preassure;{}\n'.format(time, data))

def wind_speed_logger(data):
    with open('log.csv', 'a') as file:
        time = dt.now().strftime('%H:%M')
        file.write('{};wind_speed;{}\n'.format(time, data))
