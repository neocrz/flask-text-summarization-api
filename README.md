# flask-text-summarization-api

## Descrição

Esta é uma API REST simples construída com Flask que fornece funcionalidade de sumarização de texto. Você envia um texto para a API e ela retorna um resumo conciso do texto original, utilizando técnicas de Processamento de Linguagem Natural (PLN) com a biblioteca NLTK.

## Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.
*   **Flask**: Microframework web para Python utilizado para construir a API.
*   **Flask-RESTful**: Extensão do Flask para construir APIs RESTful de forma mais fácil.
*   **NLTK (Natural Language Toolkit)**: Biblioteca Python para trabalhar com linguagem humana, utilizada para tokenização, remoção de stopwords e cálculo de frequência de palavras para a sumarização.
*   **Nix (Opcional)**: Gerenciador de pacotes para um ambiente de desenvolvimento consistente e reproduzível.

## Pré-requisitos

*   **Python 3.11 ou superior**
*   **pip** (gerenciador de pacotes Python)
*   **Nix (Opcional)**: Se você deseja utilizar o ambiente de desenvolvimento Nix. [Instalação do Nix](https://nixos.org/download.html)

## Configuração e Execução

Existem duas maneiras de configurar e executar a API: utilizando o ambiente Nix (recomendado para consistência) ou diretamente com Python e pip.

### Utilizando Nix (Recomendado)

1.  **Certifique-se de ter o Nix instalado (com Flakes ativado).** [Instalação do Nix](https://nixos.org/download.html)
2.  **Navegue até o diretório do projeto** no seu terminal.
3.  **Inicie o shell de desenvolvimento Nix:**

    ```bash
    nix develop
    ```

    Este comando irá criar um ambiente virtual Python isolado com todas as dependências necessárias instaladas. A primeira vez que você executar este comando, pode demorar um pouco para baixar todas as dependências.
4.  **Execute a API Flask:**

    ```bash
    python app.py
    ```

    A API Flask será iniciada em `http://localhost:5000`. 

### Sem utilizar Nix (Configuração manual)

1.  **Certifique-se de ter o Python 3.11 ou superior instalado.**
2.  **Navegue até o diretório do projeto** no seu terminal.
3.  **Crie um ambiente virtual Python (opcional, mas recomendado):**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Linux/macOS
    .venv\Scripts\activate  # No Windows
    ```
4.  **Instale as dependências Python utilizando pip:**

    ```bash
    pip install -r requirements.txt
    ```
5.  **Execute a API Flask:**

    ```bash
    python app.py
    ```

    A API Flask será iniciada em `http://localhost:5000`.

## Como Utilizar a API

A API possui um único endpoint `/summarize` que aceita requisições HTTP POST com um texto para sumarizar.

### Requisição POST

*   **Endpoint:** `http://localhost:5000/summarize`
*   **Método:** `POST`
*   **Headers:** `Content-Type: application/json`
*   **Body (JSON):**

    ```json
    {
        "text": "Seu texto longo aqui para ser resumido.",
        "num_sentences": 4
    }
    ```

    *   `text`: (Obrigatório) O texto que você deseja resumir.
    *   `num_sentences`: (Opcional) O número desejado de sentenças no resumo. Se não fornecido, o padrão é 4 sentenças.

### Exemplo de Requisição utilizando `test.py`

O arquivo `test.py` no repositório fornece um exemplo de como enviar uma requisição para a API utilizando a biblioteca `requests` em Python. Para executar o script de teste:

1.  Certifique-se de que a API Flask está rodando (`python app.py`).
2.  Execute o script `test.py` no seu terminal:

    ```bash
    python test.py
    ```

    Este script irá enviar uma requisição POST para a API com um texto de exemplo e imprimir o resumo retornado.

### Resposta

A API retornará uma resposta JSON com o seguinte formato:

**Sucesso (Status Code 200 OK):**

```json
{
    "summary": "Um resumo do texto fornecido, contendo o número de sentenças solicitado."
}
```

**Erro (Status Code 400 Bad Request):**

Se o campo `text` não for fornecido no corpo da requisição, a API retornará um erro:

```json
{
    "error": "Nenhum texto em 'text' foi provido"
}
```

**Erro Interno do Servidor (Status Code 500 Internal Server Error):**

Se ocorrer algum erro inesperado durante o processamento do texto, a API retornará um erro 500 com uma mensagem descrevendo o erro.

```json
{
    "error": "Mensagem de erro detalhando o problema ocorrido."
}
```

## Arquivo `flake.nix`

O arquivo `flake.nix` é utilizado para fornecer um ambiente de desenvolvimento Nix reproduzível. Ele define as dependências do projeto (Python e bibliotecas Python) e garante que todos os desenvolvedores trabalhando no projeto utilizem o mesmo ambiente, evitando problemas de "funciona na minha máquina".

Ao utilizar `nix develop`, você entra em um shell com todas as dependências configuradas, conforme especificado no `flake.nix`. Isso simplifica a configuração do ambiente de desenvolvimento e garante a consistência.


