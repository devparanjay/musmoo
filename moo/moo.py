import os

from rw_modules.moolib.preclass import preclass
from rw_modules.moolib.proclass_onr import dafi_process
from rw_modules.moolib.postclass import *
from rw_modules.moolib.emopro import emopro
# from lib.proclass_onr import dafi_process
# from lib.postclass import *

def moomoo():
    mopath = './infmod/roberta-base-go_emotions-quantized.onnx'
    tkpath = './infmod/tokenizer.json'
    dafi = './data/emot.txt'
    qnrpath = './data/qnr.txt'
    confpath = './data/config.json'
    mopath_abs = os.path.join('moo', mopath)
    tkpath_abs = os.path.join('moo', tkpath)
    # dafi_abs = os.path.abspath(dafi)
    dafi_abs = os.path.join('moo', dafi)
    qnrpath_abs = os.path.join('moo', qnrpath)
    confpath_abs = os.path.join('moo', confpath)
    # qnrpath_abs = os.path.abspath(qnrpath)
    
    # emot = askq()
    preclass(qnrpath=qnrpath_abs, confpath=confpath_abs, dafipath=dafi_abs)
    emoarr = dafi_process(dafi=dafi_abs, mopath=mopath_abs, tkpath=tkpath_abs)
    print("emoarr - \n", emoarr)
    emodict, musdict, vav = emopro(emoarr=emoarr, emothresh=0.2)
    print("emodict - \n", emodict)
    print("musdict - \n", musdict)
    print("vav - \n", vav)
    
    return musdict
    
if __name__ == '__main__':
    print('moo')
    # moomoo()