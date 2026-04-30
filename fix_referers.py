import os, glob
for f in glob.glob('viu_media/libs/provider/anime/allanime/extractors/*.py'):
    content = open(f).read()
    if 'headers={"Referer":' in content:
        content = content.replace('https://{API_BASE_URL}/', '{API_GRAPHQL_REFERER}')
        content = content.replace('API_BASE_URL', 'API_BASE_URL, API_GRAPHQL_REFERER')
        open(f, 'w').write(content)
        print("Fixed", f)
