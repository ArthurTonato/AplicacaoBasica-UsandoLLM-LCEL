# Projeto de Tradução com LangChain e Groq

## Índice
1. [Introdução](#introducao)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Instalação](#instalacao)
4. [Explicação do Código](#explicacao-do-codigo)
   - [Importação das Bibliotecas](#importacao-das-bibliotecas)
   - [Carregamento das Variáveis de Ambiente](#carregamento-das-variaveis-de-ambiente)
   - [Criação do Modelo LLM](#criacao-do-modelo-llm)
   - [Parser de Saída](#parser-de-saida)
   - [Criação do Prompt Template](#criacao-do-prompt-template)
   - [Criação e Execução da Chain](#criacao-e-execucao-da-chain)
5. [Glossário](#glossario)
6. [Como Clonar e Executar o Projeto](#como-clonar-e-executar-o-projeto)

## Introdução <a id="introducao"></a>
Este projeto utiliza a biblioteca LangChain junto com a API do Groq para realizar traduções automáticas de sentenças para diferentes idiomas.

## Tecnologias Utilizadas <a id="tecnologias-utilizadas"></a>
- Python
- LangChain
- Groq API
- dotenv

## Instalação <a id="instalacao"></a>
Antes de rodar o projeto, é necessário instalar as dependências listadas no arquivo `requirements.txt`. Use o seguinte comando:
```bash
pip install -r requirements.txt
```

## Explicação do Código <a id="explicacao-do-codigo"></a>

### Importação das Bibliotecas <a id="importacao-das-bibliotecas"></a>
As bibliotecas necessárias para o projeto são importadas:
```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os
```

### Carregamento das Variáveis de Ambiente <a id="carregamento-das-variaveis-de-ambiente"></a>
Carregamos as variáveis de ambiente do arquivo `.env`.
```python
load_dotenv(find_dotenv())
groq_api_key = os.getenv("GROQ_API_KEY")
```

### Criação do Modelo LLM <a id="criacao-do-modelo-llm"></a>
Criamos uma instância do modelo `Gemma2-9b-It` da API Groq.
```python
llm = ChatGroq(
    model = "Gemma2-9b-It",
    groq_api_key = groq_api_key,
)
```

### Parser de Saída <a id="parser-de-saida"></a>
Usamos um parser para processar a saída do modelo.
```python
parser = StrOutputParser()
```

### Criação do Prompt Template <a id="criacao-do-prompt-template"></a>
Criamos um template genérico para o prompt.
```python
generic_template = "Translate the following sentence into {language}"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", generic_template),
        ("user", "{text})")
    ]
)
```

### Criação e Execução da Chain <a id="criacao-e-execucao-da-chain"></a>
Definimos e executamos a cadeia de componentes:
```python
chain = prompt | llm | parser

print(chain.invoke({'language': 'Russian', 'text':'I am learning AI'}))
```

## Glossário <a id="glossario"></a>
- **LLM (Large Language Model)**: Modelos de inteligência artificial treinados em grandes quantidades de texto.
- **Prompt Engineering**: Prática de criar prompts eficazes para modelos de IA.
- **Few-shot, Zero-shot, One-shot Learning**: Diferentes abordagens para ensinar um modelo a responder corretamente.
- **Chain of Thought**: Estratégia para melhorar a capacidade de raciocínio de modelos de IA.

## Como Clonar e Executar o Projeto <a id="como-clonar-e-executar-o-projeto"></a>
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Execute o script:
```bash
python seu_script.py
```

Agora, seu projeto estará pronto para uso!

