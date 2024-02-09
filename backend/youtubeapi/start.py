from fastapi import FastAPI, Query
from typing import List
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

api_key = os.environ.get("api_key")
# Crie uma instância da API do YouTube
youtube = build("youtube", "v3", developerKey=api_key)

@app.get("/get_data")
async def get_popular_videos(query: str = Query(None)):
    # Calcule a data de sete dias atrás
    sete_dias_atras = (datetime.now() - timedelta(days=7)).isoformat() + "Z"

    # Parâmetros da solicitação de pesquisa inicial
    search_request_params = {
        "part": "snippet",
        "q": query if query else "",  # Sua consulta de pesquisa aqui
        "publishedAfter": sete_dias_atras,  # Apenas vídeos publicados após esta data
        "type": "video",  # Apenas vídeos
        "maxResults": 5,  # Número máximo de resultados por página
        "regionCode": "BR",# Restringe os resultados ao Brasil
        "order": "rating",

    }   

    # Lista para armazenar todos os vídeos
    all_videos = []

    # Variável para armazenar o token da próxima página
    next_page_token = None

    # Loop para buscar todas as páginas de resultados até alcançar 1000 vídeos ou o final dos resultados
    while len(all_videos) < 100:
        # Atualize o token da próxima página na solicitação de pesquisa
        if next_page_token:
            search_request_params["pageToken"] = next_page_token

        # Faça a solicitação de pesquisa para a página atual
        search_request = youtube.search().list(**search_request_params)
        search_response = search_request.execute()

        # Obtenha uma lista de IDs de vídeo dos resultados da pesquisa
        video_ids = [item["id"]["videoId"] for item in search_response["items"]]

        # Parâmetros da solicitação de vídeo para obter detalhes, incluindo likes
        videos_request_params = {
            "part": "snippet,statistics",
            "id": ",".join(video_ids),  # IDs de vídeo separados por vírgula
        }

        # Faça a solicitação de vídeo para obter detalhes dos vídeos, incluindo likes
        videos_request = youtube.videos().list(**videos_request_params)
        videos_response = videos_request.execute()

        # Adicione os vídeos obtidos à lista geral
        all_videos.extend(videos_response["items"])

        # Atualize o token da próxima página
        next_page_token = search_response.get("nextPageToken")

        # Saia do loop se não houver mais páginas de resultados
        if not next_page_token:
            break

    # Retorna a lista completa de vídeos
    return all_videos