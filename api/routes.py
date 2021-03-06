from api import api
from api.resources.anime import Animes, Anime
from api.resources.similar_anime import SimilarAnime

api.add_route('/api/animes', Animes())
api.add_route('/api/anime/{anime_id}', Anime())
api.add_route('/api/anime/similar', SimilarAnime())
