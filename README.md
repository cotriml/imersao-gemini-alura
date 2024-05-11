# Assistente de Entrevistas

## _Aumentando a produtividade e eficiência no feedback de entrevistas de emprego_


### Necessidade

Geralmente em entrevistas de emprego todo entrevistador realiza anotações de perguntas e respostas das entrevistas para posteriormente dar seu feedback.

### Problema:

Esse processo, em uma grande escala, principalmente para recrutadores, acaba consumindo bastante tempo e algo que possa ser discutido na entrevista, que tenha relevância, pode ser esquecido ou omitido sem querer.

### Solução

Para solucionar esse problema, esse assistente de entrevistas foi pensado para auxiliar o entrevistador na sumarização do que foi conversado na entrevista em formato resumido de perguntas e respostas trazendo também um feedback sugestivo sobre o bate-papo.

### Impacto

O impacto dessa solução seria o ganho de tempo que impacta diretamente a produtivade da pessoa entrevistadora e a qualidade e integridade do conteúdo discutido na entrevista que está bastante alinhado com a eficiência dessa pessoa também.


### Observações e detalhes do projeto

- Foi utilizado um arquivo original de transcrição de audio gerado pelo Google Meet;

- Esse arquivo foi convertido para .txt para facilitar essa prova de conceito de utilização do SDK do Google Gemini;

- Se faz necessário criar uma variável de ambiente para a API KEY com o nome GEMINI_API_KEY;

- As possilidade de integração pós resposta da API do Gemini são infinitas, e-mail, Slack, Integração com sistemas SaaS de recutamento, entre outros. Não criei esse passo a mais pois se tratar de uma prova de conceito e por falta de tempo também. 


### Executando a aplicação

Instalando as dependências
```sh
pip install -r requirements.txt
```

Executando arquivo Python
```sh
python src/main.py
```

