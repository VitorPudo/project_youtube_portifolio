Projeto ETL com FastAPI para Dados do YouTube

Este projeto utiliza FastAPI para criar uma rota que executa um processo ETL para dados do YouTube.

Funcionalidades:

Extração de Dados:

Utiliza a rota /get_data do FastAPI para extrair dados populares do YouTube.
Transformação de Dados:

Extrai os dados recebidos e os transforma em um formato adequado para análise.
Salva os dados transformados em um arquivo CSV chamado "popular_videos.csv".
Carga de Dados:

Converte os dados transformados em formato Parquet.
Envia os dados em formato Parquet para o Amazon S3.
Integração Futura:

Os dados serão enviados para um banco de dados PostgreSQL (ainda não implementado).
Utiliza o Streamlit para visualização, consumindo os dados da última semana.
Tecnologias Utilizadas:

FastAPI: Framework para construir APIs rápidas em Python.
Requests: Biblioteca para fazer requisições HTTP em Python.
Pandas: Biblioteca para análise e manipulação de dados em Python.
PyArrow: Biblioteca para processamento eficiente de dados em formato de coluna.
Amazon S3: Serviço de armazenamento de objetos da Amazon Web Services.
PostgreSQL: Sistema de gerenciamento de banco de dados relacional.
Streamlit: Framework para criação de aplicativos web para análise de dados em Python.
Este projeto visa automatizar a obtenção e processamento de dados do YouTube, fornecendo uma estrutura para análise e visualização contínuas dos vídeos populares.
