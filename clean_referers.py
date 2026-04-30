import os, glob

for f in glob.glob('viu_media/libs/provider/anime/allanime/extractors/*.py'):
    if f.endswith('__init__.py') or f.endswith('extractor.py') or f.endswith('base.py'):
        continue
        
    basename = os.path.basename(f)
    with open(f, 'r') as file:
        content = file.read()
    
    # We only want to keep Referer for yt_mp4.py (Yt server)
    # Actually, Wixmp might need it too but let's see.
    # ani-cli says Yt needs it.
    if basename != 'yt_mp4.py':
        # Remove Referer from headers
        # It looks like: headers={"Referer": f"{API_GRAPHQL_REFERER}"}
        content = content.replace(', headers={"Referer": f"{API_GRAPHQL_REFERER}"}', '')
        content = content.replace('headers={"Referer": f"{API_GRAPHQL_REFERER}"},', '')
        content = content.replace('headers={"Referer": f"{API_GRAPHQL_REFERER}"}', '')
        
    with open(f, 'w') as file:
        file.write(content)
    print("Cleaned Referer from", f)
