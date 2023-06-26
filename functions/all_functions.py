import re
from weather.apis import *


# UTEÍS
def pula_linha():
    """
    Função que imprime uma linha vazia.
    :return: None.
    """
    print()


def tentar_novamente():
    """
    Função que imprime opção de retorno a fase anterior e retorna a escolha.
    :return: Escolha do menuzinho, String.
    """
    print("Tentar novamente?")
    print("[S] Sim")
    print("[V] Voltar")
    escolha = input("Escolha uma opção: ").upper().strip()
    while escolha != str(escolha) or escolha != "S" and escolha != "V":
        print("[ESCOLHA UMA OPÇÃO VÁLIDA]")
        escolha = input("Escolha uma opção: ").upper().strip()
    return escolha


def voltar():
    """
    Função que força o usuário a voltar para fase anterior.
    :return: Escolha forçada, String.
    """
    print("[V] Voltar")
    escolha = input("Escolha uma opção: ").upper().strip()
    while escolha != str(escolha) or escolha != "V":
        print("[ESCOLHA UMA OPÇÃO VÁLIDA]")
        escolha = input("Escolha uma opção: ").upper().strip()
    return escolha


# INÍCIO
def bem_vindo():
    """
    Função que printa mensagem de bem-vindo.
    :return: None.
    """
    print("[Bem-vindo(a) ao FarmingTech]")
    print("Impulsione sua colheita com as nossas soluções tecnológicas.")
    pula_linha()


# MENU DE LOGIN --------------------------------------------------------------------------------------------------------
def menu_login():
    """
    Função que imprime as opções de login, e retorna a escolha do usuário.
    :return: Item escolhido - String.
    """
    print("[INÍCIO]")
    print("Faça login ou inscreva-se agora!")
    print("[I] Inscreva-se")
    print("[L] Login")
    print("[S] Sair")
    escolha = input("Escolha uma opção: ").upper().strip()
    while escolha != str(escolha) or escolha != "L" and escolha != "I" and escolha != "S":
        print("[ESCOLHA INVÁLIDA]")
        escolha = input("Escolha uma opção válida: ").upper().strip()
    return escolha


# ÁREA DE INSCRIÇÃO ----------------------------------------------------------------------------------------------------
def inscrever(dic_usuarios):
    print("[NOVA CONTA]")
    print("Crie seu login preenchendo as informações abaixo.")
    print("A sua experiência será personalizada com base nas informações dadas.")
    pula_linha()
    refazer = "R"
    while refazer == "R":
        nome_login = checa_nome()
        pula_linha()
        email_login = checa_email()
        pula_linha()
        senha_login = checa_senha()
        pula_linha()
        localizacao_login = checa_localizacao()
        pula_linha()
        dic_usuarios[email_login] = {"Senha": senha_login, "Nome": nome_login, "Localização": localizacao_login}
        print("[CONFIRMAÇÃO]")
        print("ATENÇÃO: Informações erradas podem prejudicar o funcionamento deste software.")
        print("Certifique-se de que todos os dados fornecidos estão corretos.")
        print("[C] Continuar")
        print("[R] Refazer")
        refazer = input("Escolha uma opção: ").upper().strip()
        while refazer != str(refazer) or refazer != "C" and refazer != "R":
            print("[ESCOLHA UMA OPÇÃO VÁLIDA]")
            refazer = input("Escolha uma opção: ").upper().strip()
        if refazer == "C":
            pula_linha()
            print("[TUDO CERTO]")
            print("Acesse o menu fazendo login com seu e-mail e senha.")
            return dic_usuarios
        elif refazer == "R":
            print("Tudo bem! Tente novamente.")
            pula_linha()
            continue
    return dic_usuarios


def checa_nome():
    print("[NOME E SOBRENOME] Conta pra gente quem você é!")
    nome_login = input("Digite seu primeiro nome: ")
    while nome_login != str(nome_login) or not re.match(r"^[a-zA-ZÀ-ÿ\s-]+$", nome_login):
        print("[DIGITE UM NOME VÁLIDO]")
        nome_login = input("Digite seu nome: ")

    sobrenome_login = input("Digite seu sobrenome: ")
    while sobrenome_login != str(sobrenome_login) or not re.match(r"^[a-zA-ZÀ-ÿ\s-]+$", sobrenome_login):
        print("[DIGITE UM SOBRENOME VÁLIDO]")
        sobrenome_login = input("Digite seu sobrenome: ")
    return nome_login, sobrenome_login


def checa_email():
    print("[EMAIL] O seu melhor e-mail é o recomendado.")
    email_login = input("Digite o e-mail: ")
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email_login):  # EXPRESSÃO REGULAR DE E-MAIL
        print("[DIGITE UM E-MAIL VÁLIDO]")
        email_login = input("Digite o e-mail: ")
    return email_login


def checa_senha():
    print("[SENHA] A sua senha deve conter no mínimo seis digitos.")
    senha_login = input("Digite a senha: ")
    while not re.match(r"^.{6,}$", senha_login):
        print("[DIGITE UMA SENHA VÁLIDA]")
        senha_login = input("Digite a senha: ")
    return senha_login


def checa_localizacao():
    print("[LOCALIZAÇÃO] Sua localização molda sua experiência no FarmingTech!")
    print("Siga os exemplos a risca. Essa etapa é determinante no funcionamento do software.")
    print("As informações fornecidas serão utilizadas única e exclusivamente para nutrir nossas ferramentas.")
    pais_login = input("Digite o país em que você mora (Exemplo: Brasil, Uruguai): ")
    estado_login = input("Digite o estado em que você mora (Exemplo: Santa Catarina, São Paulo): ")
    cidade_login = input("Digite a cidade em que você mora (Exemplo: São Paulo, Florianópolis): ")
    logradouro_login = input("Digite o logradouro de onde você mora "
                             "(Exemplo: Avenida Paulista 1106, Rua Oscar Freire 14): ")
    return pais_login, estado_login, cidade_login, logradouro_login


# LOGAR --------------------------------------------------------------------------------------------------------
def logar(dic_usuarios):
    while True:
        print("[ÁREA DE LOGIN]")
        email_login = input("Digite o seu e-mail: ")
        validacao_email = dic_usuarios.get(email_login)
        if validacao_email is None:
            print("[E-MAIL NÃO ENCONTRADO]")
            escolha = tentar_novamente()
            if escolha == "S":
                pula_linha()
                continue
            else:
                break
        else:
            senha_login = input("Digite a sua senha: ")
            valida_senha = dic_usuarios[email_login]["Senha"]
            if valida_senha == senha_login:
                print("Entrando...")
                return email_login
            else:
                print("[SENHA INCORRETA]")
                escolha = tentar_novamente()
                if escolha == "S":
                    logar(dic_usuarios)
                else:
                    break


# AREA LOGIN -------------------------------------------------------------------------------------------------------
def area_login(dic_usuarios):
    while True:
        escolha = menu_login()
        if escolha == "S":
            chave_vazia = None  # Chave sem valor, entra na condicional do menu que retorna (para) a função.
            return dic_usuarios, chave_vazia
        elif escolha == "I":
            pula_linha()
            inscrever(dic_usuarios)  # Dicionário atualizado
            pula_linha()
            continue
        elif escolha == "L":
            pula_linha()
            chave_dic = logar(dic_usuarios)  # Chave valorada, parâmetro da função menu
            pula_linha()
            if chave_dic is not None:
                return dic_usuarios, chave_dic
            else:
                continue
        else:
            print("Oops!")  # Nunca vai executar... eu acho.
            return


# MENU PRINCIPAL -------------------------------------------------------------------------------------------------------
def menu(dic_usuarios, email_login):
    """
    Função que imprime e controla o fluxo do menu, contém todos os itens.
    :param dic_usuarios: Dicionário do qual será extraído as
    informações relevante do usuário para funcionamento do menu e suas respectivas funções.
    :param email_login: E-mail do usuário, chave do dicionário. String.
    :return: None.
    """
    while True:
        if email_login is None:
            pula_linha()
            return
        nome = dic_usuarios[email_login]["Nome"][0]
        pais = dic_usuarios[email_login]["Localização"][0]
        estado = dic_usuarios[email_login]["Localização"][1]
        cidade = dic_usuarios[email_login]["Localização"][2]
        logradouro = dic_usuarios[email_login]["Localização"][3]
        endereco = f"{logradouro}, {cidade}, {estado} - {pais}"
        itens_menu(nome)
        escolha = escolha_item_menu()  # ITEM ESCOLHIDO PELO USUÁRIO
        pula_linha()
        if escolha == "B":
            biblioteca_verde()  # BIBLIOTECA VERDE
            continue
        elif escolha == "C":
            clima(cidade)  # CLIMA E PREVISÃO
            continue
        elif escolha == "V":
            dic_usuarios, email_login = area_login(dic_usuarios)  # VOLTAR AO LOGIN
            continue
        elif escolha == "R":
            recomendacao(cidade)  # RECOMENDAÇÃO DA IA
            continue
        elif escolha == "M":
            monitoramento_solo(endereco)  # INFORMAÇÕES DO SOLO
            continue
        else:
            break
    return


# ITENS MENU PRINCIPAL -------------------------------------------------------------------------------------------------
def itens_menu(nome):
    """
    Função que imprime todos os itens do menu principal.
    :param nome: Primeiro nome do usuário, String.
    :return: None.
    """
    print("[MENU PRINCIPAL]")
    print(f"Como podemos te ajudar hoje, {nome.capitalize()}?")
    print("[B] Biblioteca Verde"
          "\n[C] Previsão e Clima"
          "\n[R] Recomendações de Plantio"
          "\n[M] Monitoramento de Solo"
          "\n[V] Voltar"
          "\n[S] Sair")


def escolha_item_menu():
    """
    Função para forçar escolha de item do menu.
    :return: Escolha do usuário, String.
    """
    escolha = input("Escolha uma opção: ").upper().strip()
    while escolha != str(escolha) or escolha != "B" and escolha != "V"\
            and escolha != "C" and escolha != "P" and escolha != "M" and escolha != "S" and escolha != "R":
        print("[ESCOLHA INVÁLIDA]")
        escolha = input("Escolha uma opção válida: ").upper().strip()
    return escolha


# BIBLIOTECA VERDE -----------------------------------------------------------------------------------------------------
def biblioteca_verde():
    """
    Função do item do menu 'Biblioteca Verde', onde há uma requisição ao chatgpt,
    que retorna a resposta da pergunta feita pelo usuário.
    :return: None.
    """
    print("[BIBLIOTECA VERDE]")
    print("Bem vindo a Biblioteca Verde! "
          "\nAqui você encontra respostas para suas dúvidas da agricultura.")
    escolha = perguntar_voltar()
    while True:
        if escolha == "V":
            pula_linha()
            return
        elif escolha == "P":
            print("O que você gostaria de saber?")
            pergunta = input("Eu gostaria de saber: ")
            pergunta = str(pergunta) + "(Responda apenas o que for relacionado a agricultura, " \
                                       "plantação, vegetais ou sobre o solo. Se não tiver relação " \
                                       "com o contexto, apenas diga que não pode ajudar.)"
            print("Gerando resposta... Isso talvez leve alguns segundos...")
            pula_linha()
            print("[RESPOSTA]")
            resposta = chatgpt(pergunta)
            print(resposta)
            print()
            print("[BIBLIOTECA VERDE]")
            print("Escolha uma ação.")
            escolha = perguntar_voltar()
            if escolha == "V":
                pula_linha()
            continue
        else:
            print("Ooops!")
            return


def perguntar_voltar():
    """
    Função do item 'Biblioteca Verde' do menu principal, que pergunta
    se o usuário quer perguntar novamente ou retornar ao menu.
    :return: Escolha do usuário, String.
    """
    print("[P] Perguntar"
          "\n[V] Voltar")
    escolha = input("Escolha uma opção: ").upper().strip()
    while escolha != str(escolha) or escolha != "P" and escolha != "V":
        print("[ESCOLHA INVÁLIDA]")
        escolha = input("Escolha uma opção válida: ").upper().strip()
    return escolha


# CLIMA ----------------------------------------------------------------------------------------------------------------
def clima(cidade):
    """
    Função que imprime informações do clima da cidade do usuário.
    :param cidade: Cidade em que o usuário se autodeclara residente, String.
    :return: None.
    """
    dic_clima = open_weather(cidade)
    descricao_clima = dic_clima["weather"][0]["description"]
    temp_max_clima = dic_clima["main"]["temp_max"]
    temp_min_clima = dic_clima["main"]["temp_min"]
    temperatura_clima = dic_clima["main"]["temp"]
    umidade_clima = dic_clima["main"]["humidity"]
    vento_clima = dic_clima["wind"]["speed"]
    print(f"[CLIMA - {cidade.upper()}]")
    print(f"Descrição do clima: {descricao_clima}.")
    print(f"A umidade é de {umidade_clima}%, com ventos de {vento_clima} km/h.")
    print("[TEMPERATURA]")
    print(f"Temperatura atual: {temperatura_clima}ºC"
          f"\nTemperatura mínima: {temp_min_clima}ºC"
          f"\nTemperatura máxima: {temp_max_clima}ºC")
    pula_linha()
    escolha = voltar()
    if escolha == "V":
        pula_linha()
    else:
        print("Oops!")


def recomendacao(cidade):
    """
    Função que imprime a recomendação de plantio personalizada ao usuário, gerada pelo ChatGPT por uma requisição.
    :param cidade: Cidade onde será baseada a recomendação.
    :return: None.
    """
    pergunta = pergunta_estacoes(cidade)
    print("[RECOMENDAÇÃO DE PLANTIO]")
    print("Vamos recomendar com base na sua localização e época do ano.")
    print("Isso pode levar alguns segundos...")
    pula_linha()
    print(f"[RECOMENDAÇÃO POR ESTAÇÃO DO ANO - {cidade.upper()}]")
    retorno = chatgpt(pergunta)
    print(retorno)
    pula_linha()
    escolha = voltar()
    if escolha == "V":
        pula_linha()
    else:
        print("Oops!")


# MONITORAMENTO DO SOLO ------------------------------------------------------------------------------------------------
def monitoramento_solo(endereco):
    """
    Função que imprime informações da temperatura e umidade do solo em determinada profundidade,
    por uma requisição a API da Storm Glass.
    :param endereco: Parâmetro da API Geopy, que retornará a
    latitude e longitude do endereço, que será parâmetro da API da Storm Glass, String.
    :return: None.
    """
    print("[MONITORAMENTO DE SOLO]")
    print("Utilizamos sua localização como ponto do monitoramento.")
    print(f"Calculando coordenadas de {endereco}...")
    lat, long = latitude_longitude(endereco)
    print(f"LATITUDE: {lat}")
    print(f"LONGITUDE: {long}")
    dic_solo = storm_glass(lat, long)
    temp_superficie = dic_solo['hours'][0]['soilTemperature']['noaa']
    temp_10 = dic_solo['hours'][0]['soilTemperature10cm']['noaa']
    temp_40 = dic_solo['hours'][0]['soilTemperature40cm']['noaa']
    temp_100 = dic_solo['hours'][0]['soilTemperature100cm']['noaa']
    umi_superficie = dic_solo['hours'][0]['soilMoisture']['noaa']
    umi_10 = dic_solo['hours'][0]['soilMoisture10cm']['noaa']
    umi_40 = dic_solo['hours'][0]['soilMoisture40cm']['noaa']
    umi_100 = dic_solo['hours'][0]['soilMoisture100cm']['noaa']
    pula_linha()
    print(f"[TEMPERATURA DO SOLO]")
    print("Dados da temperatura em cada profundidade do solo.")
    print(f"De zero a dez centímetros: {temp_superficie}ºC.")
    print(f"De dez a quarenta centímetros: {temp_10}ºC.")
    print(f"De quarenta a cem centímetros: {temp_40}ºC.")
    print(f"De cem a duzentos centímetros: {temp_100}ºC.")
    pula_linha()
    print("[UMIDADE DO SOLO]")
    print("Dados da umidade em cada profundidade do solo.")
    print(f"De zero a dez centímetros: {umi_superficie}%.")
    print(f"De dez a quarenta centímetros: {umi_10}%.")
    print(f"De quarenta a cem centímetros: {umi_40}%.")
    print(f"De cem a duzentos centímetros: {umi_100}%.")
    pula_linha()
    escolha = voltar()
    if escolha == "V":
        pula_linha()
    else:
        print("Oops!")


# VOLTE SEMPRE ---------------------------------------------------------------------------------------------------------
def volte_sempre():
    """
    Função que imprime uma mensagem de despedida.
    :return: None.
    """
    print("[VOLTE SEMPRE]")
    print("Até mais!")


if __name__ == '__main__':
    usuarios = {}
    dic_teste = {}
    chave_teste = "Teste"
    senha_teste = "051299"
    nome_teste = ["Ronqui", "Rafael"]
    localizacao_teste = ["Brasil", "SP", "São Paulo", "Avenida Paulista 1106"]
    dic_teste[chave_teste] = {"Senha": senha_teste, "Nome": nome_teste, "Localização": localizacao_teste}
    menu(dic_teste, chave_teste)
    volte_sempre()
