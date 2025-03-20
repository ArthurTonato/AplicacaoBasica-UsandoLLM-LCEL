#IMPORTAÇÃO DAS BIBLIOTECAS
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os

#CARREGANDO AS VARIAVEIS DE AMBIENTE
load_dotenv(find_dotenv())

groq_api_key = os.getenv("GROQ_API_KEY")

#1 CRIAR O MODELO GROQ
llm = ChatGroq(
    model = "Gemma2-9b-It", #MODELO DE LLM UTILIZADO
    groq_api_key = groq_api_key, #CHAVE DE API DO GROQ
)

#CRIAR O PROMPT **** ESUDAR SOBRE PROMPTS ENGINEERING(FEW-SHOT, ZERO-SHOT, ONE-SHOT, CHAIN OF THOUGHTS)


#2 PARSER DE SAIDA : isso e necessario para que o sistema entenda a saida do modelo
parser = StrOutputParser()

#3 Prompt Template: Usando LCEL = Chain the Components
generic_template = "Translate the following sentence into {language}"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", generic_template),
        ("user", "{text})")
    ]
)

#O que é uma chain
#Uma cadeia é uma sequencia de componentes que sao executados em ordem

chain = prompt | llm | parser

#Executar a chain
print(chain.invoke({'language': 'Russian', 'text':'I am learning AI'})
)
