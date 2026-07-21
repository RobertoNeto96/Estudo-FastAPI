# Registros de Estudo: Desenvolvimento de APIs com FastAPI

Repositório dedicado ao estudo prático e documentação do desenvolvimento de APIs RESTful em Python utilizando o framework **FastAPI**.

Após consolidar os fundamentos em Python e banco de dados MySQL, o foco deste projeto é aplicar esses conceitos na criação de serviços web modernos, eficientes e escaláveis.

### 📌 Conteúdo do Repositório
* **Anotações de Estudo:** Conceitos-chave, arquitetura de rotas e boas práticas anotados durante o curso da Hashtag Programação.
* **Códigos Práticos:** Testes de endpoints, validação de dados com Pydantic e manipuladores de requisições (`GET`, `POST`, `PUT`, `DELETE`).
* **Integração:** Conexão com banco de dados e estruturação de operações CRUD.

---
. Após as instalaçoes das extensões necessarias no Python, criamos o arquivo MAIN e dentro dele importamos o FastAPI, depois criamos propriamente o APLICATIVO com uma variavel, comunalmente chamada de app:

from fastapi import FastAPI

app = FastAPI()


. temos as requisiçoes:

Get --> Leitura
Post --> enviar/Criar
Put/Patch --> Edição
Delete --> Deletar

. Uma observação muito importante é que uma ROTA ou caminho, é tudo que vem depois do DOMINIO do link do site

. Uma boa pratica de codificação, é criar as rotas em arquivos diferentes, cada rota em seu arquivo diferente, levando em isso em conta, no arquivo MAIN a ordem de importação desses arquivos de rotas TEM UMA IMPORTANCIA EXTREMA, onde os arquivos de rotas devem ser importados após a linha de codigo onde criamos o APLICATIVO, ou seja após a linha de codigo:   app = FastAPI()

. Nesse curso iremos trabalhar os arquivos de AUTH_ROUTES e ORDER_ROUTES, respectivamente ROTAS DE AUTENTICAÇÃO e ROTAS DE ORDENS

. Estruturando todo o arquivo MAIN ficaria:


from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router

. As chamadas de AUTH_ROUTER e ORDER_ROUTER serão criadas em seus respectivos arquivos, lembrando que esse nome é de livre escolha, nao dependendo de nada especifico


PARTINDO PARA CRIAÇÃO DAS ROTAS DE CAMINHOS DOS LINKS

. Nos arquivos de rotas criados posteriormente, iremos criar os caminhos das rotas atraves de uma variavel que podemos dar o nome que quisermos, nesse curso iremos usar os nomes AUTH_ROUTER e ORDER_ROUTER, assim como eles foram chamados no exemplo logo acima

. Começamos nesses arquivos de rotas importando o APIRouter

from fastapi import APIRouter


. Criando essa variavel temos alguns requisitos a seguir como o PREFIXO de um link, como ele sempre sera chamado dentro do seu "setor", como por exemplo a rota de AUTENTICAÇÃO o AUTH_ROUTES / AUTH_ROUTER , depois seguimos com as TAGS, que são etiquetas para identificar a "seção" de cada rota, no caso desse curso as rotas de AUTENTICAÇÃO ou ORDENS, segue o exemplo da variavel que sera criada e modularizada posteriormente no arquivo MAIN: 

auth_router = APIRouter(prefix="/auth" , tags=["auth"]) --> criando essa linha de codigo dentro do seu respectivo arquivo

order_router = APIRouter(prefix="/order" , tags=["order"]) --> criando essa linha de codigo dentro do seu respectivo arquivo

. Após criarmos os roteadores de caminhos, definirmos seus prefixos e tags, voltamos ao arquivo main e pedimos para que o aplicativo (variavel APP) inclua em si mesmo as rotas criadas ate entao, fazemos isso atraves do comando        app.include_router()        esse comando faz com que o aplicativo utilize essas rotas quando forem chamadas no site, veja o exemplo de como ficará o arquivo MAIN ate o momento:


from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)


