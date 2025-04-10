import requests
import json

text = """
A reforma da Previdência é uma das principais pautas do governo federal, com o objetivo de equilibrar as contas públicas e garantir a sustentabilidade do sistema previdenciário brasileiro. O projeto propõe mudanças significativas nas regras de aposentadoria tanto para trabalhadores urbanos quanto rurais, além de servidores públicos.

Atualmente, o Brasil gasta cerca de 13% do seu PIB com previdência social, um dos percentuais mais altos do mundo. Especialistas alertam que, sem reformas, o déficit do sistema pode chegar a R$ 1 trilhão nos próximos 10 anos. A proposta estabelece idade mínima de 65 anos para homens e 62 anos para mulheres, com tempo mínimo de contribuição de 20 anos.

Para os professores, há uma pequena diferenciação, com idade mínima reduzida em 5 anos. Já os policiais e agentes penitenciários terão regras específicas considerando a natureza perigosa de suas profissões. O texto também cria uma transição gradual para quem já está no mercado de trabalho, com regras progressivas que serão implementadas ao longo de 12 anos.

Uma das principais polêmicas é a mudança no cálculo do benefício. Pela nova regra, o valor da aposentadoria será calculado sobre a média de todas as contribuições do trabalhador, e não mais sobre os 80% maiores salários, como ocorre atualmente. Isso deve reduzir o valor médio dos benefícios em aproximadamente 30%.

O governo argumenta que essas mudanças são necessárias para conter o crescimento acelerado da despesa previdenciária, que hoje consome mais de 40% do orçamento federal. Por outro lado, sindicatos e movimentos sociais criticam a proposta, alegando que ela penaliza principalmente os trabalhadores de baixa renda, que começam a contribuir mais cedo e geralmente têm expectativa de vida menor.

Estudos do IBGE mostram que a população brasileira está envelhecendo rapidamente. Em 2060, teremos apenas dois trabalhadores ativos para cada aposentado, contra a razão atual de quatro para um. Esse cenário demográfico pressiona ainda mais a necessidade de reformas estruturais no sistema previdenciário.

Além das mudanças na aposentadoria por idade, o projeto também altera as regras para benefícios como auxílio-doença, pensão por morte e aposentadoria por invalidez. Para receber estes benefícios, será necessário cumprir prazos de carência mais longos e passar por avaliações médicas periódicas.

Economistas apontam que, se aprovada, a reforma pode gerar uma economia de R$ 1,2 trilhão em 10 anos, além de melhorar a classificação de risco do país perante os investidores internacionais. No entanto, o caminho para aprovação no Congresso é árduo, exigindo negociações complexas com diversos partidos e blocos parlamentares.

A última tentativa de reforma, em 2019, enfrentou forte resistência e precisou ser modificada diversas vezes antes de ser aprovada. Desta vez, o governo busca construir um consenso maior antes de enviar a proposta ao Legislativo, realizando reuniões com governadores, prefeitos e lideranças sindicais.

Especialistas em direito previdenciário alertam que muitas dúvidas só serão esclarecidas quando o texto for regulamentado. Questões como a situação dos trabalhadores intermitentes, aposentadorias especiais e o impacto nas pequenas empresas ainda precisam ser melhor detalhadas no projeto de lei.
"""

url = "http://localhost:5000/summarize"

data = {
    "text": text,
    "num_sentences": 4 
}

headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print("Sumário:")
        print(result['summary'])
    else:
        print(f"Error: {response.status_code}")
        print(response.json())

except requests.exceptions.RequestException as e:
    print(f"Falha de conexão com a API: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
