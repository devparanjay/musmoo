from ytmusicapi import YTMusic
from collections import defaultdict
import json
import os
import glob

def get_conf(confpath):
    with open(confpath, 'r') as conff:
        conf = dict(json.load(conff))
    return conf

def get_recom():
    confpath = os.path.abspath('././data/config.json')
    conf = get_conf(confpath)

    usrconf = dict(conf['usr'])
    mooconf = dict(conf['moo'])
    musdict = dict(conf['moo']['musdict'])

    ytmusic = YTMusic()
    # yt_mood_cat = ytmusic.get_mood_categories()
    # print(yt_mood_cat)
    playlists = defaultdict(list)
    
    print('Getting recommendations for your current emotions and mood...\n')
    
    for mood in musdict['moods']:
        for genre in musdict['genres']:
            playlists[f'{mood}-{genre}'].append(ytmusic.search(f'{mood} {genre} songs {usrconf["usr_languages"].values()}', filter='songs', limit=2))
    playlists = dict(playlists)
    recommendations = dict.fromkeys(playlists.keys())
    for moodxgenre in playlists:
        if usrconf['usr_printpref'] == 1:
            print(moodxgenre, ': -')
        moodxgenre_recoms = []
        for i in range(len(playlists[moodxgenre][0])):
            song = playlists[moodxgenre][0][i]
            songurl = 'https://music.youtube.com/watch?v=' + song['videoId']
            moodxgenre_recoms.append(songurl)
            if usrconf['usr_printpref'] == 1:
                print(i, song['title'], sep=". ")
                print("URL: ", songurl)
        recommendations[moodxgenre] = moodxgenre_recoms
        if usrconf['usr_printpref'] == 1:
            print('\n')
        
    return recommendations

def rewrite_recom(recomdir, recoms:dict):
    oldrecomfiles = glob.glob(f'{os.path.abspath(recomdir)}*.txt')
    for files in oldrecomfiles:
        for file in files:
            os.remove(os.path.abspath(file))
    all_recom = []
    for mg in recoms:
        fname = str(mg) + '.txt'
        fpath = os.path.join(recomdir, fname)
        with open(fpath, 'w') as recomf:
            for songurl in recoms[mg]:
                all_recom.append(songurl+'\n')
                recomf.write(songurl+'\n')
    all_recom = list(set(all_recom))
    all_recom_path = os.path.join(recomdir, 'all-recommendations.txt')
    with open(all_recom_path, 'w') as allrecf:
        for i in all_recom:
            allrecf.write(i)

def promoo(recomdir):
    rewrite_recom(recomdir, get_recom())

if __name__ == '__main__':
    print('yoo')
    # yoo()