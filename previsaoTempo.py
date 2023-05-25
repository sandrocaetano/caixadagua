import urequests 
import ujson as json
from time import sleep
import network
import machine

def prevchuva():   
    if station.isconnected() == True:
        print("CONECTADO")
        print(station.ifconfig())
    else:
        station.connect(ssdi, password)

    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = "535c1a0c6c7fb6e742c2d9564df25b82"
    city_name = "curitiba"
    url = base_url + "q="+ city_name + "&appid=" + api_key


    requisicao = urequests.get(url)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['main']
    temperatura = requisicao_dic['main']['temp'] - 273.15
    chuva = ""

    if requisicao_dic['weather'][0]['main'] == 'Rain' or requisicao_dic['weather'][0]['main'] == "Thunderstorm": #Rain ou Clouds
        chuva = requisicao_dic['rain']['1h']
        if chuva >= 5:
            print("Vai chover, Retorna True")
            return True
        else: 
            print("vai chover, volume de água baixo?, Retorna False")
            return False
        
    else:
        print("Sem chuva, Retorna False")
        return False

    return False
    print(descricao, f"{temperatura}°C", chuva) 
