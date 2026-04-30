import os, glob

for f in glob.glob('viu_media/libs/provider/anime/allanime/extractors/*.py'):
    if f.endswith('__init__.py') or f.endswith('extractor.py') or f.endswith('base.py'):
        continue
        
    with open(f, 'r') as file:
        content = file.read()
    
    # Fix the f-string bug: replace the tuple with just API_BASE_URL
    # We look for the tuple inside curly braces
    content = content.replace('{API_BASE_URL, API_GRAPHQL_REFERER}', '{API_BASE_URL}')
    
    # Ensure Referer header uses API_GRAPHQL_REFERER
    # Pattern 1: headers={"Referer": f"https://{API_BASE_URL}/"}
    # Pattern 2: headers={"Referer": f"{API_GRAPHQL_REFERER}"} (already might be fixed)
    content = content.replace('headers={"Referer": f"https://{API_BASE_URL}/"}', 'headers={"Referer": f"{API_GRAPHQL_REFERER}"}')
    
    # Ensure import is correct
    if 'API_GRAPHQL_REFERER' not in content:
        content = content.replace('from ..constants import API_BASE_URL', 'from ..constants import API_BASE_URL, API_GRAPHQL_REFERER')

    with open(f, 'w') as file:
        file.write(content)
    print("Fixed", f)
