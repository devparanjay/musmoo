import numpy as np
from operator import itemgetter

def get_emodict(emoarr, emothresh, labels_list:list):
    # csvlabels = 'admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise, neutral'
    emodict = dict.fromkeys(labels_list)
    for cid in range(len(labels_list)):
        emodict[labels_list[cid]] = 0
        for rid in range(len(emoarr)):
            emodict[labels_list[cid]] = emodict[labels_list[cid]] + emoarr[rid, cid]
            # emodict[labels_list[cid]] = (emodict[labels_list[cid]] + emoarr[rid, cid])/2
        emodict[labels_list[cid]] = emodict[labels_list[cid]]/len(emoarr)
        # if emodict[labels[cid]] < emothresh:
            # emodict.pop(labels[cid], 'Label to be popped not found in emodict!')
            
    emodict = dict(sorted(emodict.items(), key=itemgetter(1), reverse=True))
    return emodict

def get_vav(emodict:dict, labels_list:list):
    # song_feats = 'danceability, acousticness, energy, instrumentalness, liveness, valence, loudness, speechiness, tempo, key'
    labels_str = [8, 6, 9, 7 ,5, 4, 3, 2, 8, 6, 5, 9, 8, 9, 10, 7, 6, 10, 10, 7, 8, 9, 5, 7, 8, 6, 8, 4]    
    emo_str = dict(zip(labels_list, labels_str))
    labels_pos = ['admiration', 'amusement', 'approval', 'caring', 'curiosity', 'desire', 'excitement', 'gratitude', 'joy', 'love', 'optimism', 'pride', 'realization', 'relief', 'surprise', 'neutral']
    labels_neg = ['anger', 'annoyance', 'confusion', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'fear', 'grief', 'nervousness', 'remorse', 'sadness']
    emo_pos_wa = 0
    emo_neg_wa = 0
    for label in labels_pos:
        emo_pos_wa = emo_pos_wa + calc_wa(label, emodict, emo_str)
    for label in labels_neg:
        emo_neg_wa = emo_neg_wa + calc_wa(label, emodict, emo_str)
    valence_arousal_val = emo_pos_wa - emo_neg_wa
    return valence_arousal_val

def calc_wa(emo:str, emodict:dict, emo_str:dict):
    return emodict.get(emo)*emo_str.get(emo)

def get_musdict(vav):
    music_keys = ['moods', 'genres']
    # music_val_moods = []
    # music_val_genres = []
    if vav <= -7:
        music_val_moods = ['eerie', 'haunting', 'unsettling']
        music_val_genres = ['Dark Ambient', 'Funeral',  'Doom Metal', 'Harsh Noise', 'Depressive Black Metal']
    elif -3 >= vav and vav >= -6:
        music_val_moods = ['sad', 'melancholic', 'reflective']
        music_val_genres = ['Blues', 'Grunge', 'Industrial', 'Gothic Rock']
    elif 2 >= vav and vav >= -2:
        music_val_moods = ['calm', 'soothing', 'nostalgic']
        music_val_genres = ['Pop', 'Folk', 'Jazz', 'Ambient']
    elif 6 >= vav and vav >= 3:
        music_val_moods = ['uplifting', 'energetic', 'joyful']
        music_val_genres = ['Reggae', 'Funk', 'Salsa', 'Indie Pop']
    elif vav >= 7:
        music_val_moods = ['euphoric', 'vibrant', 'ecstatic']
        music_val_genres = ['Disco', 'Tropical House', 'Happy Hardcore', 'Power Metal']
    musdict = dict.fromkeys(music_keys)
    musdict[music_keys[0]] = music_val_moods
    musdict[music_keys[1]] = music_val_genres
    return musdict
    
def emopro(emoarr, emothresh):
    labels = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']
    emodict = get_emodict(emoarr, emothresh, labels)
    vav = get_vav(emodict, labels)
    musdict = get_musdict(vav)
    return emodict, musdict, vav


def numarr():
    arr = np.array([['a', 'b', 'c', 'd'], [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    for idx, x in np.ndenumerate(arr):
        #print(idx, arr[idx])
        #print(len(arr))
        nid = (idx[0]+1,idx[1])
        if idx[0]+1 >= len(arr):
            break
        else:
            print(nid, arr[nid])
    
    karr = np.array([[3, 2, 4], [5, 0, 1]])
    print(karr)
    print(karr>3)
    print(np.where(karr>3))
    sarr = np.sort(karr)
    print(sarr)
    print(sarr>3)
    print(np.where(sarr>3))

    
if __name__ == '__main__':
    print('emopro')