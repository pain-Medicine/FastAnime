import os, glob
from viu_media.libs.provider.anime.allanime.constants import API_BASE_URL, API_GRAPHQL_REFERER

for f in glob.glob('viu_media/libs/provider/anime/allanime/extractors/*.py'):
    with open(f, 'r') as file:
        content = file.read()
    
    if 'headers={"Referer":' in content:
        # Import API_GRAPHQL_REFERER if not present
        if 'API_GRAPHQL_REFERER' not in content:
            content = content.replace('from ..constants import API_BASE_URL', 'from ..constants import API_BASE_URL, API_GRAPHQL_REFERER')
        
        # Replace the referer header value
        content = content.replace('f"https://{API_BASE_URL}/"', 'f"{API_GRAPHQL_REFERER}"')
        
        with open(f, 'w') as file:
            file.write(content)
        print("Fixed", f)
