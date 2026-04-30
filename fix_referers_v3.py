import os, glob

for f in glob.glob('viu_media/libs/provider/anime/allanime/extractors/*.py'):
    if f.endswith('__init__.py') or f.endswith('extractor.py') or f.endswith('base.py'):
        continue
        
    with open(f, 'r') as file:
        content = file.read()
    
    if 'headers={"Referer":' in content:
        # Import API_GRAPHQL_REFERER if not present
        if 'API_GRAPHQL_REFERER' not in content:
            content = content.replace('from ..constants import API_BASE_URL', 'from ..constants import API_BASE_URL, API_GRAPHQL_REFERER')
        
        # Replace the referer header value
        # Old: headers={"Referer": f"https://{API_BASE_URL}/"}
        # New: headers={"Referer": f"{API_GRAPHQL_REFERER}"}
        content = content.replace('f"https://{API_BASE_URL}/"', 'f"{API_GRAPHQL_REFERER}"')
        
        with open(f, 'w') as file:
            file.write(content)
        print("Fixed", f)
