import os, glob

for f in glob.glob('viu_media/libs/provider/anime/allanime/extractors/*.py'):
    if f.endswith('__init__.py') or f.endswith('extractor.py') or f.endswith('base.py'):
        continue
        
    with open(f, 'r') as file:
        content = file.read()
    
    # Fix the f-string bug introduced earlier
    content = content.replace('API_BASE_URL, API_GRAPHQL_REFERER', 'API_BASE_URL')
    
    # Ensure Referer is updated correctly
    # Check for the old pattern without the slash
    if 'f"https://{API_BASE_URL}{url.replace' in content and 'headers={"Referer": API_GRAPHQL_REFERER' not in content:
         content = content.replace('headers={"Referer": f"https://{API_BASE_URL}/"}', 'headers={"Referer": f"{API_GRAPHQL_REFERER}"}')
         if 'API_GRAPHQL_REFERER' not in content:
             content = content.replace('from ..constants import API_BASE_URL', 'from ..constants import API_BASE_URL, API_GRAPHQL_REFERER')
             
    with open(f, 'w') as file:
        file.write(content)
    print("Fixed", f)
