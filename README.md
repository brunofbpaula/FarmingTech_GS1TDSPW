# FarmingTech_GS1TDSPW
Projeto do grupo FIVETECH para a Global Solution do primeiro semestre do curso de Análise e Desenvolvimento de sistemas.

# FUNCIONAMENTO DO SISTEMA
Neste projeto, serão utilizadas APIs do OpenWeatherMap, OpenAI, Storm Glass e Geopy. O sistema, através dos dados inseridos pelo usuário, será capaz de imprimir informações sobre o solo (como temperatura e umidade), clima (temperatura, descrição, umidade e velocidade do vento), e localizar as coordenadas da localização declarada pelo usuário. Ao mesmo tempo, integrar respostas da inteligência artificial generativa mais famosa do mundo, o ChatGPT, visando recomendar plantio personalizado de acordo com clima local e estação do ano.

# Proposta Global Solution Fome Zero
A fome é um problema global que afeta milhões de pessoas em todo o mundo. Segundo a Organização das Nações Unidas para a Alimentação e Agricultura (FAO), cerca de 828 milhões de pessoas foram afetadas pela fome em 2021, enquanto 2,3 bilhões de pessoas sofrem de insegurança alimentar moderada ou grave em 2021.
Tomada por esses fatos, a FiveTech se engajou no combate a fome mundial e a escassez de alimentos, utilizando tecnologia e inovação em sua contribuição.
Com foco em pequenos agricultores, a plataforma ‘Farming Tech’ promove uma dinâmica transmissão de informação, além do uso de inteligências artificiais generativas, a fim de aumentar a produtividade, eficiência e sustentabilidade no processo da cadeia agrícola de pequenos produtores oferecendo recursos e orientações valiosas.

# CONCLUSÃO
O sistema requer um cadastro simples, requisitando nome e endereço do usuário para a personalização do sistema para eles. 
Os dados são essenciais para a tomada de decisões relacionadas ao plantio, colheita e manejo das plantações, garantindo que 
os agricultores estejam preparados para enfrentar diferentes cenários climáticos e situações de solo específicas.

# INSTRUÇÕES DE USO
Ao testar o programa, utilize uma localização real. Siga os exemplos a risca, a fim de não ter problemas com o software.
O programa forçará, sempre que necessário, a resposta correta do usuário. Entretanto, ele não pode evitar localizações não verdadeiras.
A opção "Monitoramento de Solo" faz requisição a Storm Glass. Por não termos um assinatura, estamos limitados a dez requisições por dia. Há uma API key reserva na função, que pode substituir a utilizada, tornando possível fazer mais dez requisições.
Caso for utilizar um endereço de um país que não tenha a divisão em estados, mas em regiões, informe o nome da cidade como estado (Exemplo: Pais: Inglaterra, Estado: Londres, Cidade: Londres, Logradouro: Londres SW1A 1AA).

# DEPENDÊNCIAS
Serviços da OpenWeatherMap, OpenAI, Geopy e Storm Glass.
