import os, glob

for f in glob.glob('viu_media/libs/provider/anime/allanime/extractors/*.py'):
    if f.endswith('__init__.py') or f.endswith('extractor.py') or f.endswith('base.py') or f.endswith('yt_mp4.py'):
        continue
        
    with open(f, 'r') as file:
        content = file.read()
    
    if "response.json()" in content and 'return Server(' in content:
        # Check if referer is already handled
        if 'referer = response.json().get("Referer")' not in content:
            content = content.replace('streams: AllAnimeEpisodeStreams = response.json()', 'streams: AllAnimeEpisodeStreams = response.json()\n        referer = response.json().get("Referer")')
            content = content.replace('episode_title=episode["notes"],', 'episode_title=episode["notes"],\n            headers={"Referer": referer} if referer else {},')
            
    with open(f, 'w') as file:
        file.write(content)
    print("Updated dynamic Referer for", f)
