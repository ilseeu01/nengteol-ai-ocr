# RAG 시스템 설정 파일
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def getenv_any(*keys, default=None):
    for k in keys:
        v = os.getenv(k)
        if v and str(v).strip():
            return v
    return default

CLOVA_CONFIG = {
    # 언더스코어 有/無 모두 허용
    "api_key": getenv_any("CLOVA_STUDIO_API_KEY", "CLOVA_STUDIO_API_KEY"),
    # request_id도 두 이름 모두 허용 (없으면 자동 생성 문자열)
    "request_id": getenv_any("CLOVASTUDIO_REQUEST_ID", "CLOVA_STUDIO_REQUEST_ID", default="food-classification-request"),
    "host": os.getenv("CLOVA_STUDIO_HOST", "https://clovastudio.stream.ntruss.com"),
    "endpoint_kind": os.getenv("CLOVA_ENDPOINT_KIND", "testapp"),   # "testapp" 또는 "serviceapp"
    "model": os.getenv("CLOVA_MODEL", "HCX-005"),
    "max_tokens": int(os.getenv("CLOVA_MAX_TOKENS", "1000")),
    "temperature": float(os.getenv("CLOVA_TEMPERATURE", "0.7")),
}

# 식약처 API 설정
FOOD_API_CONFIG = {
    "base_url": "http://apis.data.go.kr/1471000/FoodNtrCpntDbInfo02",
    "endpoint": "/getFoodNtrCpntDbInq02",
    "api_key_encoding": "%2F6rrnUampF4T33WBTsqvj5RvlKuyttK%2BmTQoi%2BiaVIa44%2FWI05MoCh94HBR5J71WRevIOA1dJRYlPdZ3ctO70g%3D%3D",
    "api_key_decoding": "/6rrnUampF4T33WBTsqvj5RvlKuyttK+mTQoi+iaVIa44/WI05MoCh94HBR5J71WRevIOA1dJRYlPdZ3ctO70g==",
    "data_format": "JSON"
}

# 캐시 설정
CACHE_CONFIG = {
    "cache_duration": 3600,  # 1시간
    "max_cache_size": 1000,  # 최대 1000개 캐시
    "cache_dir": "cache"
}

# RAG 설정
RAG_CONFIG = {
    "embedding_model": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    "similarity_threshold": 0.7,
    "max_results": 5,
    "embeddings_dir": "embeddings"
}