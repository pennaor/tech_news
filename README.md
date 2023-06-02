# Tech News

Aplicação que provê meios para raspar dados do [blog da Trybe](https://blog.betrybe.com/).
Foi desenvolvida como projeto de aprendizado no curso de desenvolvimento Web da [Trybe](https://www.betrybe.com/).

<details>
<summary><strong>Ferramentas utilizadas</strong></summary>

- [Python](https://www.python.org)
- [Pytest](https://docs.pytest.org/en/7.3.x)
- [Parsel](https://parsel.readthedocs.io/en/latest)
- [Requests](https://requests.readthedocs.io/en/latest)
- [MongoDB](https://www.mongodb.com)

</details>

<details>
<summary><strong>Habilidades trabalhadass</strong></summary>

- Utilizar o terminal interativo do Python
- Escrever módulos e importá-los em outros códigos
- Aplicar técnicas de raspagem de dados
- Extrair dados de conteúdo HTML
- Armazenar os dados obtidos em um banco de dados

</details>

<details>
  <summary><strong>MongoDB</strong></summary>

  A aplicação usa um banco de dados denominado `tech_news` gerenciado pelo MongoDB rodando na porta `27017`.
  As funções que interagem com o banco de dados estão presentes no módulo `database.py`.
  As notícias são armazenadas em uma coleção chamada `news`.

  <strong>Docker</strong>

  É possível rodar o MongoDB pelo docker com o comando no terminal:

  <code>docker-compose up -d mongodb</code>

  Para mais detalhes acerca do mongo com o docker, olhe o arquivo `docker-compose.yml`

  Caso queira instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções no tutorial oficial:

  Ubuntu: <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/>

  MacOS:  <https://docs.mongodb.com/guides/server/install/>
</details>

<details>
<summary><strong>Instalação</strong></summary>

⚠️ Certifique-se de estar rodando o MongoDB na porta padrão `27017`

1. Clone o repositório e entre na pasta do repositório que você acabou de clonar

```bash
git clone git@github.com:pennaor/tech_news.git
cd ./tech_news
```

2. Crie o ambiente virtual para o projeto

```bash
python3 -m venv .venv && source .venv/bin/activate
```

3. Instale as dependências

```bash
python3 -m pip install -r dev-requirements.txt
```

</details>

<details>
<summary><strong>Utilização</strong></summary>

  1. Abra um terminal Python importando as funções do arquivo menu.py

```bash
python3 -i tech_news/menu.py
```

  2. Execute a função analyzer_menu e em seguida digite o número da opção desejada
```bash
analyser_menu()

Selecione uma das opções a seguir:
0 - Popular o banco com notícias;
1 - Buscar notícias por título;
2 - Buscar notícias por data;
3 - Buscar notícias por categoria;
4 - Listar top 5 categorias;
5 - Sair.
```

> 0 - Popula o banco de dados com a quantidade de notícias informada

> 1 - Busca `case insensitive` de nóticias por título que contenha o valor procurado. É retornada uma lista de tuplas contendo o título e URL da notícia

> 2 - Busca notícias pela data no formato YYYY-MM-DD. É retornada uma lista de tuplas contendo o título e URL da notícia

> 3 - Busca `case insensitive` de notícias por categoria, É retornada uma lista de tuplas contendo o título e URL da notícia

> 4 - Lista as 5 categorias mais encontradas

> 5 - Encerra o programa

</details>

<details>
<summary><strong>Teste da classe ReadingPlanService</strong></summary>

O teste `test_reading_plan_group_news`, presente em `tests/reading_plan/test_reading_plan.py`, deve garantir o funcionamento correto do método `group_news_for_available_time` da classe `ReadingPlanService`.

`ReadingPlanService`, implementado no arquivo `tech_news/analyzer/reading_plan.py`, coleta as notícias do banco de dados e as divide em 2 agrupamentos:

1. `readable`: notícias que podem ser lidas em até `X` minutos
2. `unreadable`: notícias que **não** podem ser lidas em até `X` minutos

Além disso, as notícias `readable` são organizadas em sub-grupos cuja soma dos tempos de leitura seja menor que `X`. Assim, a pessoa leitora pode ler mais do que 1 notícia sem ultrapassar o tempo disponível!

O valor de `X`, que é o tempo de leitura que uma pessoa tem disponível, é passado por parâmetro no método `group_news_for_available_time`.

Para executar o teste, digite em um terminal:
```bash
python3 -m pytest
```
⚠️ O ambiente virtual deve estar ativado!

</details>
