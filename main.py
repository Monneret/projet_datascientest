import matplotlib.pyplot as plt
import glob
import pickle
from collections import Counter
from lstm import get_notes

test=get_notes(save=False,integer=False)
count=Counter(test)
count_best = dict((l[0],l[1]) for l in count.most_common(50))

plt.figure(figsize=(8,16))
pos=0
for k in count_best.keys():
    pos+=1
    plt.barh(pos,count[k],0.4)

plt.yticks(range(1,pos+1),count_best.keys())
plt.title("# notes Mario")
print(len(test))
print(len(set(test)))
plt.show()

#from music21 import *
#
#M=list()
#M.append(converter.parse('./data/Mario/1_SMB_OVERWORLD_115_BPM.mid'))
#M.append(converter.parse('./data/Mario/2_SMB3_OVERWORLD_140_BPM.mid'))
#M[0].plot('scatter', 'quarterLength', 'pitch', title='SMB Overworld')
#M[0].plot('histogram', 'octave', xHideUnused=False, yAxisLabel='Number of Pitches')
#M[0].plot('horizontalbar')
#M[0].plot('scatterweighted', 'pitch', 'quarterLength')
#M[0].plot('colorgrid')
#M[0].plot('horizontalbarweighted')
#M[0].plot('3dbars')