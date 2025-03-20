Projeto de Tradução com LangChain e Groq

Índice

Introdução

Tecnologias Utilizadas

Instalação

Explicação do Código

Importação das Bibliotecas

Carregamento das Variáveis de Ambiente

Criação do Modelo LLM

Parser de Saída

Criação do Prompt Template

Criação e Execução da Chain

Glossário

Como Clonar e Executar o Projeto

Introdução 

Este projeto utiliza a biblioteca LangChain junto com a API do Groq para realizar traduções automáticas de sentenças para diferentes idiomas.

Tecnologias Utilizadas 

Python

LangChain

Groq API

dotenv

Instalação 

Antes de rodar o projeto, é necessário instalar as dependências listadas no arquivo requirements.txt. Use o seguinte comando:

Explicação do Código 

Importação das Bibliotecas 

As bibliotecas necessárias para o projeto são importadas:

Carregamento das Variáveis de Ambiente 

Carregamos as variáveis de ambiente do arquivo .env.

Criação do Modelo LLM 

Criamos uma instância do modelo Gemma2-9b-It da API Groq.

Parser de Saída 

Usamos um parser para processar a saída do modelo.

Criação do Prompt Template 

Criamos um template genérico para o prompt.

Criação e Execução da Chain 

Definimos e executamos a cadeia de componentes:

Glossário 

LLM (Large Language Model): Modelos de inteligência artificial treinados em grandes quantidades de texto.

Prompt Engineering: Prática de criar prompts eficazes para modelos de IA.

Few-shot, Zero-shot, One-shot Learning: Diferentes abordagens para ensinar um modelo a responder corretamente.

Chain of Thought: Estratégia para melhorar a capacidade de raciocínio de modelos de IA.