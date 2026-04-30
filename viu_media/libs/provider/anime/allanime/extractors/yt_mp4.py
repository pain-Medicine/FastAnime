from ...types import EpisodeStream, Server
from ..constants import API_BASE_URL, API_GRAPHQL_REFERER
from ..types import AllAnimeEpisode, AllAnimeSource
from .base import BaseExtractor


class YtExtractor(BaseExtractor):
    @classmethod
    def extract(
        cls,
        url,
        client,
        episode_number: str,
        episode: AllAnimeEpisode,
        source: AllAnimeSource,
    ) -> Server:
        return Server(
            name="Yt",
            links=[EpisodeStream(link=url, quality="1080")],
            episode_title=episode["notes"],
            headers={"Referer": f"{API_GRAPHQL_REFERER}"},
        )
