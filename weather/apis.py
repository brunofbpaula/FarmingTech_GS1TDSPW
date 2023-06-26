import requests
import openai
import arrow
from geopy.geocoders import Nominatim


# OPEN WEATHER MAP -----------------------------------------------------------------------------------------------------
def open_weather(cidade_login):
    """
    Função que retorna o dicionário da API de Clima da Open Weather Map.
    :param cidade_login: Cidade da qual será requisitado o clima, String.
    :return: Dicionário da requisição.
    """
    api_key = "0952be387f90a00cf451a0396421f691"
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade_login}" \
           f"&appid={api_key}&units=metric&lang=pt_br"
    request = requests.get(link)
    dic_weather = request.json()
    return dic_weather


def forecast(lat, lon):
    """
    Função que faz uma requisição ao OpenWeatherMap e retorna um dicionário com previsão dos próximos cinco dias,
    com atualizações de previsão a cada três horas.
    :param lat: Latitude (da localização do usuário) parâmetro da requisição, String.
    :param lon: Longitude (da localização do usuário) parâmetro da requisição, String.
    :return:
    """
    api_key = "0952be387f90a00cf451a0396421f691"
    link = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}" \
           f"&appid={api_key}&units=metric&lang=pt_br"
    request = requests.get(link)
    dic_forecast = request.json()
    return dic_forecast


# CHATGPT --------------------------------------------------------------------------------------------------------------
def pergunta_estacoes(cidade_login):
    """
    Função que retorna uma pergunta sobre recomendação de vegetais para se plantar em determinada estação do ano de
    determinada cidade.
    :param cidade_login: Cidade em que a recomendação será baseada, String.
    :return: Pergunta que será enviada ao ChatGPT, em String.
    """
    pergunta = f"Explique como funciona o clima de {cidade_login} durante o ano. " \
               f"Depois, me diga quais são os melhores vegetais para se plantar em {cidade_login}, " \
               f"levando em consideração as condições gerais de clima da cidade" \
               ", em uma lista divida por estações do ano. Explique brevemente a escolha dos vegetais de cada estação."
    return pergunta


def chatgpt(pergunta):
    """
    Função que faz uma requisição a OpenIA, e retorna a resposta do ChatGPT.
    :param pergunta: Pergunta feita ao ChatGPT.
    :return: Resposta do ChatGPT, em String.
    """
    openai.api_key = "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"
    chat_gpt = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "system", "content": f"{pergunta}"}])
    retorno_chatgpt = chat_gpt.choices[0].message.content
    return retorno_chatgpt


# GEOPY ----------------------------------------------------------------------------------------------------------------
def latitude_longitude(endereco):
    """
    Função que recebe um endereço e retorna as suas coordenadas (latitude e longitude)
    :param endereco: Endereço ao qual as coordenadas serão retornadas.
    :return: Coordenadas do endereço, em String.
    """
    localizador = Nominatim(user_agent="FarmingTech")
    localizacao = localizador.geocode(endereco)
    latitude = localizacao.latitude
    longitude = localizacao.longitude
    return latitude, longitude


# STORM GLASS ----------------------------------------------------------------------------------------------------------
def storm_glass(latitude, longitude):
    """
    Função que retorna um dicionário com valores de temperatura e umidade do solo.
    :param latitude: Latitude, parâmetro da API da Storm Glass.
    :param longitude: Longitude, parâmetro da API da Storm Glass.
    :return: Dicionário com dado dos parâmetros da API (nesse caso, de dados do solo).
    """
    start = arrow.utcnow()
    end = arrow.utcnow()
    api_key = '7324f8bc-0248-11ee-a26f-0242ac130002-7324f948-0248-11ee-a26f-0242ac130002'
    # api_key_reserva = 'dd191924-0112-11ee-8b7f-0242ac130002-dd1919ec-0112-11ee-8b7f-0242ac130002'
    response = requests.get(
        'https://api.stormglass.io/v2/bio/point',
        params={
            'lat': latitude,
            'lng': longitude,
            'params': ','.join(
                ['soilTemperature', 'soilTemperature10cm', 'soilTemperature40cm', 'soilTemperature100cm',
                 'soilMoisture', 'soilMoisture10cm', 'soilMoisture40cm', 'soilMoisture100cm']),
            'start': start.to('UTC').timestamp(),
            'end': end.to('UTC').timestamp()
        },
        headers={
            'Authorization': api_key
        }
    )
    dic_solo = response.json()
    return dic_solo


# TESTE ----------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print("TESTES")
    # lat, lon = latitude_longitude("Rua Americano 179, Castanhal - Pará, Brasil")
    # dic_previsao = forecast(lat, lon)
    # print(dic_previsao['list'][0])
    # previsoes = []
    # for x in dic_previsao['list']:
    #     for i in range(9):
    #         print(dic_previsao['list'][i]['pop'])
    #         previsoes.append(dic_previsao['list'][i]['pop'])
    # print(previsoes)
    # print(len(previsoes))
    #
    # print("DIA")
    # data = dic_previsao['list'][8]['dt_txt']
    # dia_data = pandas.Timestamp(data)
    # dia_semana = dia_data.day_name()
    #
    # print(dia_semana)
    # print(f"00:00 - {previsoes[0]*100}%")
    # print()
    # print("FUNÇÕES")
    # def previsao(endereco): ------------------------------------------------------------------------------------------
    #     lat, lon = latitude_longitude(endereco)
    #     dic_previsao = forecast(lat, lon)
    #     previsoes = []
    #     for i in range(40):
    #         previsoes.append(dic_previsao['list'][i]['pop'])  # TODAS PREVISÕES (8 POR DIA)
    #     dia_um = dic_previsao['list'][0]['dt_txt']
    #     dia_um = pandas.Timestamp(dia_um)
    #     dia_um_semana = dia_um.day_name()  # ////////////// DIA DA SEMANA
    #     dia_dois = dic_previsao['list'][10]['dt_txt']
    #     dia_dois = pandas.Timestamp(dia_dois)
    #     dia_dois_semana = dia_dois.day_name()  # /////////
    #     dia_tres = dic_previsao['list'][18]['dt_txt']
    #     dia_tres = pandas.Timestamp(dia_tres)
    #     dia_tres_semana = dia_tres.day_name()  # /////////
    #     dia_quatro = dic_previsao['list'][28]['dt_txt']
    #     dia_quatro = pandas.Timestamp(dia_quatro)
    #     dia_quatro_semana = dia_quatro.day_name()  # /////
    #     dia_cinco = dic_previsao['list'][38]['dt_txt']
    #     dia_cinco = pandas.Timestamp(dia_cinco)
    #     dia_cinco_semana = dia_cinco.day_name()  # //////
    #     escolha = semana(dia_um_semana, dia_dois_semana, dia_tres_semana, dia_quatro_semana, dia_cinco_semana)
    #     if escolha == f"{dia_um_semana[0:3].upper()}":
    #         print(previsoes[0:8])
    #         print(len(previsoes[0:8]))
    #     elif escolha == f"{dia_dois_semana[0:3].upper()}":
    #         print(previsoes[9:17])
    #         print(len(previsoes[9:17]))
    #     elif escolha == f"{dia_tres_semana[0:3].upper()}":
    #         print(previsoes[18:26])
    #         print(len(previsoes[18:26]))
    #     elif escolha == f"{dia_quatro_semana[0:3].upper()}":
    #         print(previsoes[27:34])
    #         print(len(previsoes[27:35]))
    #     elif escolha == f"{dia_cinco_semana[0:3].upper()}":
    #         print(previsoes[35:40])
    #         print(len(previsoes[32:40]))
    #
    # def semana(um, dois, tres, quatro, cinco):
    #     print("[PREVISÃO DO TEMPO]")
    #     print("Escolha um dia da semana.")
    #     print(f"[{um[0:3].upper()}] {um.upper()}")
    #     print(f"[{dois[0:3].upper()}] {dois.upper()}")
    #     print(f"[{tres[0:3].upper()}] {tres.upper()}")
    #     print(f"[{quatro[0:3].upper()}] {quatro.upper()}")
    #     print(f"[{cinco[0:3].upper()}] {cinco.upper()}")
    #     escolha = input("Dia da semana escolhido: ")
    #     return escolha
    # previsao("Rua Americano 179, Castanhal - Pará, Brasil") ----------------------------------------------------------
    # for i in dic_previsao['list'][0:9]:
    #     print(i)

    # endereco_teste = "Avenida Paulista 1106, São Paulo - SP"
    # latitude_teste, longitude_teste = latitude_longitude(endereco_teste)
    #
    # print(endereco_teste.upper())
    # print(f"Temperatura do solo até 10cm: {json_data['hours'][0]['soilTemperature']['noaa']}ºC")
    # print(f"Temperatura 10cm-40cm: {json_data['hours'][0]['soilTemperature10cm']['noaa']}ºC")
    # print(f"Temperatura 40cm-100cm: {json_data['hours'][0]['soilTemperature40cm']['noaa']}ºC")
    # print(f"Temperatura 100-200cm: {json_data['hours'][0]['soilTemperature100cm']['noaa']}ºC")
    # print()
    # print("DICIONÁRIO")
    # print(json_data)
    # dic_open_weather = open_weather("São Paulo")
    # descricao = dic_open_weather["weather"][0]["description"]
    # temp_max = dic_open_weather["main"]["temp_max"]
    # temp_min = dic_open_weather["main"]["temp_min"]
    # temperatura = dic_open_weather["main"]["temp"]
    # sensacao_termica = dic_open_weather["main"]["feels_like"]
    # umidade = dic_open_weather["main"]["humidity"]
    # vento = dic_open_weather["wind"]["speed"]
    #
    # print(f"[CLIMA EM SÃO PAULO]")
    # print(f"DESCRIÇÃO: {descricao.capitalize()}"
    #       f"\nTEMPERATURA MÁXIMA: {temp_max}ºC"
    #       f"\nTEMPERATURA MÍNIMA: {temp_min}ºC"
    #       f"\nTEMPERATURA ATUAL: {temperatura}ºC"
    #       f"\nSENSAÇÃO TÉRMICA: {sensacao_termica}ºC"
    #       f"\nUMIDADE DO AR: {umidade}%"
    #       f"\nVENTO: {vento} km/h")
    # print()
    # print(f"[O QUE PLANTAR EM {cidade.upper()}]")
    # print(chatgpt(pergunta_estacoes(cidade)))
