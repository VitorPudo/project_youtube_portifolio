from typing import Union, Dict

GenericSchema = Dict[str, Union[str, float, int]]

YoutubeSchema: GenericSchema = {
    "channelId": str,
    "title": str,
    "publishedAt": str,
    "channelTitle": str,
    "categoryId": str,
    "defaultLanguage": str,
    "defaultAudioLanguage": str,
    "viewCount": str,
    "likeCount": str,
    "favoriteCount": str,
    "commentCount": str,
}
