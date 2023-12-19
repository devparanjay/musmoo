import os, json

from mmlib.moolib.preclass import preclass
from mmlib.moolib.proclass_onr import dafi_process
from mmlib.moolib.emopro import emopro

confpath = '././data/config.json'
confpath_abs = os.path.abspath(confpath)

def write_conf(emodict:dict, musdict:dict, vav):
    with open(confpath_abs, 'r') as conffr:
        conf = dict(json.load(conffr))
    with open(confpath_abs, 'w+') as conffw:
        conf['moo']['musdict'] = musdict
        conf['moo']['emodict'] = emodict
        conf['moo']['vav'] = vav
        json.dump(conf, conffw)

def moomoo():
    mopath = './infmod/roberta-base-go_emotions-quantized.onnx'
    tkpath = './infmod/tokenizer.json'
    dafi = '././data/emot.txt'
    qnrpath = '././data/qnr.txt'
    mopath_abs = os.path.join('moo', mopath)
    tkpath_abs = os.path.join('moo', tkpath)
    dafi_abs = os.path.abspath(dafi)
    qnrpath_abs = os.path.abspath(qnrpath)
    
    preclass(qnrpath=qnrpath_abs, confpath=confpath_abs, dafipath=dafi_abs)
    emoarr = dafi_process(dafi=dafi_abs, mopath=mopath_abs, tkpath=tkpath_abs)
    emodict, musdict, vav = emopro(emoarr=emoarr, emothresh=0.2)
    write_conf(emodict, musdict, vav)
    os.remove(dafi_abs)
    # print("emoarr - \n", emoarr)
    # emodict, musdict, vav = emopro(emoarr=emoarr, emothresh=0.2)
    # print("emodict - \n", emodict)
    # print("musdict - \n", musdict)
    # print("vav - \n", vav)
    
if __name__ == '__main__':
    print('moo')
    # moomoo()
    # print(confpath_abs)
    # write_conf(moomoo())