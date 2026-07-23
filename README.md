# Registros de Estudo: Desenvolvimento de APIs com FastAPI

Repositório dedicado ao estudo prático e documentação do desenvolvimento de APIs RESTful em Python utilizando o framework **FastAPI**.

Após consolidar os fundamentos em Python e banco de dados MySQL, o foco deste projeto é aplicar esses conceitos na criação de serviços web modernos, eficientes e escaláveis.

### 📌 Conteúdo do Repositório
* **Anotações de Estudo:** Conceitos-chave, arquitetura de rotas e boas práticas anotados durante o curso da Hashtag Programação.
* **Códigos Práticos:** Testes de endpoints, validação de dados com Pydantic e manipuladores de requisições (`GET`, `POST`, `PUT`, `DELETE`).
* **Integração:** Conexão com banco de dados e estruturação de operações CRUD.

---

 Após as instalaçoes das extensões necessarias no Python, criamos o arquivo MAIN e dentro dele importamos o FastAPI, depois criamos propriamente o APLICATIVO com uma variavel, comunalmente chamada de app:

from fastapi import FastAPI

app = FastAPI()

. temos as requisiçoes:

Get --> Leitura Post --> enviar/Criar Put/Patch --> Edição Delete --> Deletar

. Uma observação muito importante é que uma ROTA ou caminho, é tudo que vem depois do DOMINIO do link do site

. Uma boa pratica de codificação, é criar as rotas em arquivos diferentes, cada rota em seu arquivo diferente, levando em isso em conta, no arquivo MAIN a ordem de importação desses arquivos de rotas TEM UMA IMPORTANCIA EXTREMA, onde os arquivos de rotas devem ser importados após a linha de codigo onde criamos o APLICATIVO, ou seja após a linha de codigo: app = FastAPI()

. Nesse curso iremos trabalhar os arquivos de AUTH_ROUTES e ORDER_ROUTES, respectivamente ROTAS DE AUTENTICAÇÃO e ROTAS DE ORDENS

. Estruturando todo o arquivo MAIN ficaria:

from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router from order_routes import order_router

. As chamadas de AUTH_ROUTER e ORDER_ROUTER serão criadas em seus respectivos arquivos, lembrando que esse nome é de livre escolha, nao dependendo de nada especifico

PARTINDO PARA CRIAÇÃO DAS ROTAS DE CAMINHOS DOS LINKS

. Nos arquivos de rotas criados posteriormente, iremos criar os caminhos das rotas atraves de uma variavel que podemos dar o nome que quisermos, nesse curso iremos usar os nomes AUTH_ROUTER e ORDER_ROUTER, assim como eles foram chamados no exemplo logo acima

. Começamos nesses arquivos de rotas importando o APIRouter

from fastapi import APIRouter

. Criando essa variavel temos alguns requisitos a seguir como o PREFIXO de um link, como ele sempre sera chamado dentro do seu "setor", como por exemplo a rota de AUTENTICAÇÃO o AUTH_ROUTES / AUTH_ROUTER , depois seguimos com as TAGS, que são etiquetas para identificar a "seção" de cada rota, no caso desse curso as rotas de AUTENTICAÇÃO ou ORDENS, segue o exemplo da variavel que sera criada e modularizada posteriormente no arquivo MAIN:

auth_router = APIRouter(prefix="/auth" , tags=["auth"]) --> criando essa linha de codigo dentro do seu respectivo arquivo

order_router = APIRouter(prefix="/order" , tags=["order"]) --> criando essa linha de codigo dentro do seu respectivo arquivo

. Após criarmos os roteadores de caminhos, definirmos seus prefixos e tags, voltamos ao arquivo main e pedimos para que o aplicativo (variavel APP) inclua em si mesmo as rotas criadas ate entao, fazemos isso atraves do comando app.include_router() esse comando faz com que o aplicativo utilize essas rotas quando forem chamadas no site, veja o exemplo de como ficará o arquivo MAIN ate o momento:

from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router from order_routes import order_router

app.include_router(auth_router) app.include_router(order_router)

---------------------------------------------------------------------------------------------------------

INTEGRAÇÃO DE COMANDOS COM BANCO DE DADOS

. Uma boa pratica na programação é criar um aquivo separado com nome de MODELS.PY para definirmos os comandos de classes do banco de dados 

. Para as importações serão SQLALCHEMY com seu modulo CREATE_ENGINE, que é o modulo que permite a criação de um banco de dados

. Criamos um banco de dados novo atribuindo um comando a uma variavel, nesse caso utilizaremos DB = CREATE_ENGINE() dentro dos parenteses temos paramentros para incluir, sendo primeiro o prefixo     "sqlite:///    e o nome do banco que sera criado .(ponto) db:                            db = create_engine("sqlite:///banco.db)         

. Após criarmos o banco de dados, precisamos criar a BASE do banco de dados, para isso: importamos primeiramente um modulo do SQLALCHEMY.ORM chamado DECLARATIVE_BASE, depois criamos uma variavel e armazenamos a linha de codigo: DECLARATIVE_BASE() dentro da variavel criada, segue o exemplo da estrutra abaixo: 

from sqlachemy import create_engine
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///banco.db") --> nessa linha de codigo criamos a "forma" para criarmos de fato o banco de dados posteriormente
base = declarative_base() --> aqui criamos a base do banco de dados, para efeito de um entendimento melhor, esse comando é como um tradutor, que conhece comandos em SQL e comandos em PYTHON

. Após termos definidos a criação do banco de dados acima, vamos criar uma CLASSE com as tabelas que farão parte do banco de dados, e respectivamente as colunas de cada tabela, para isso utilizamos CLASS (nome da tabela que sera criado) (base(variavel definida nos exemplos acima)):

class usuario(base):
    __tablename__ = "usuarios"
    id = 
    nome =
    email = 
    senha =

. A estrutura acima é composta por algumas linhas, sendo elas, a primeira onde definimos a classe no python com o nome de usuarios e logo em seguida chamamos o variavel/"tradutor" BASE, com o codigo que faz o python e o sql conversarem entre si

. Na segunda linha temos um comando que faz com que a tabela seja criada exatamente com o nome que esta entre as aspas, logo apos o sinal de atribuição, ou seja a tabela criada tera o nome de USUARIOS

. E nas respectivas linhas ID , NOME, EMAIL, serao as colunas que serao criadas dentro da tabela USUARIOS

. Agora para defirnimos os valores de cada coluna que sera criada, precisamos IMPORTAR no arquivo os tipos primitivos do banco de dados, sendo eles BOOLEANOS, INTEIROS, FLUTUANTES, TEXTOS e outros, para isso importamos column, segue o exemplo da estrutura do codigo:

from sqlalchemy import create_engine, column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

. Explicando os valores importados: 
 String = TEXTO
 Integer = NUMEROS INTEIROS
 Boolean = VALORES VERDADEIROS OU FALSOS
 Float = NUMEROS COM VIRGULA/PONTO
 ForeignKey = CHAVES PRIMARIAS QUE CONVERSAM ENTRE TABELAS

. Importando esses tipos primitivos, podemos atribuir os valores nas colunas dentro da tabela que foi criada, seguindo um parametro especifico: 

class usuario(base):
    __tablename__ = "usuarios"
    id = column("id" , integer , primary_key=True, autoincrement=True)
    nome = column("nome" , String , nullable=False)
    email = column("email" , String ,)
    senha = column("senha" , Integer , nullable=False)

. Explicando o bloco de codigo acima, após definimros o nome da VARIAVEL que sera chamada no PYTHON, nos definimos o nome da COLUNA que sera DENTRO DO BANCO DE DADOS, como boas praticas da programação, utilizamos os mesmos nomes em ambos lugares, PYTHON e BANCO DE DADOS, sempre utilizando aspas duplas para definir o nome da coluna que sera criada, apos definirmos o nome, colocamos o tipo primitivo que essa coluna terá, seja tipo booleano, numero inteiro ou com virgula.

               id                    =        column                                    ("id"                   ,     Integer)
(nome da variavel dentro do python)    (modulo que foi importado)   (nome que a coluna dentro do banco receberá)  (tipo primitivo)

. Além dos tipos primitivos temos mais alguns parametros que ajudam a criar regras em colunas especificas, como é o caso do NULLABLE, ele faz com que o campo que ele faz parte seja obrigatorio ter a informação que é pedido, como nome, senha, ou E-mail, assim como é utilizado no exemplo acima, no caso o usuario só sera cadastrado se ele colcoar a informação pedida nos 3 campos, NOME e SENHA

. Assim como na criação de tabelas direto no Banco de dados, temos as regras de autoincrement, que o proprio codigo integra em sequencia um numero ao usuario cadastrado, e temos PRIMARY_KEY que é onde ocorre a incrementação de uma chave primaria ao id do usuario, onde posteriormente faremos a foreignKey para ligaçoes entre tabelas

. Temos tambem a regra DEFAULT, que é o mesmo estudado em banco de dados, sempre que o usuario nao inserir nenhum ainformação em algum campo, o sistema automaticamente preenche com alguma informação pre definida, exemplo: nacionalidade = column("nacionalidade" , default='Brasil') --> nesse exemplo quando o usuario nao inserir nenhuma informação no campo nacionalidade, autoamaticamente o sistema preenche com 'Brasil'

. Após criarmos toda a estrutura com as colunas definidas com seus tipos primitivos, e suas respectivas regras, utilizamos o INIT que em linguagem mais comum, ele é como um "empacotador" de usuarios cadastrados nessa ocasião, a partir da estrutra do codigo toda montada, vamos explicar sua função:

from sqlalchemy import create_engine , Column, String , Integer , Boolean , Float , ForeignKey 
from sqlalchemy.orm import declarative_base


db = create_engine("sqlite:///banco.db")

base = declarative_base()

class Usuario(base):
    __tablename__ = "usuarios"
    id = Column("id" , Integer , primary_key=True, autoincrement=True)
    nome = Column("nome" , String , nullable=False)
    email = Column("email" , String ,)
    senha = Column("senha" , String , nullable=False)

    def __init__(self, nome, email, senha):
    self.nome = nome
    self.email = email
    self.senha = senha

. def__init__(self , nome, email, senha): é a função que "empacotará" o usuario cadastrado em uma unica variavel, como por exemplo 'usuario1', 'usuario2' e assim por diante, sem precisar fazer isso manualmente

