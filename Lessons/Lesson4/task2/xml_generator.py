from user_interface import temperature_view
from user_interface import preassure_view
from user_interface import wind_speed_view

def create(device = 1):
    xml = '<xml>\n'
    xml += '   <temperature units = "c">{}</temperature>\n'\
        .format(temperature_view(device))
    xml += '   <preassure units = "mmHg">{}</preassure>\n'\
        .format(preassure_view(device))
    xml += '   <wind_speed units = "mmHg">{}</preassure>\n'\
        .format(wind_speed_view(device))
    
    with open('data.xml', 'w') as page:
        page.write(xml)

    return xml

def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n'
    xml += '   <temperature units = "f">{}</temperature>\n'\
        .format(t)
    xml += '   <preassure units = "mmHg">{}</preassure>\n'\
        .format(p)
    xml += '   <wind_speed units = "mmHg">{}</preassure>\n'\
        .format(w)
    
    with open('new_data.xml', 'w') as page:
        page.write(xml)

    return data