import scipy.stats 
import numpy as np
import pdb

m = {'Just My Luck': {'Claudia Puig': 3.0,
  'Gene Seymour': 1.5,
  'Lisa Rose': 3.0,
  'Mick LaSalle': 2.0},
  
 'Lady in the Water': {'Gene Seymour': 3.0,
  'Jack Matthews': 3.0,
  'Lisa Rose': 2.5,
  'Michael Phillips': 2.5,
  'Mick LaSalle': 3.0},
  
 'Snakes on a Plane': {'Claudia Puig': 3.5,
  'Gene Seymour': 3.5,
  'Jack Matthews': 4.0,
  'Lisa Rose': 3.5,
  'Michael Phillips': 3.0,
  'Mick LaSalle': 4.0,
  'Toby': 4.5},
  
 'The Night Listener': {'Claudia Puig': 4.5,
  'Gene Seymour': 3.0,
  'Jack Matthews': 3.0,
  'Lisa Rose': 3.0,
  'Michael Phillips': 4.0,
  'Mick LaSalle': 3.0},

  'Superman Returns': {'Claudia Puig': 4.0,
  'Gene Seymour': 5.0,
  'Jack Matthews': 5.0,
  'Lisa Rose': 3.5,
  'Michael Phillips': 3.5,
  'Mick LaSalle': 3.0,
  'Toby': 4.0},

 'You, Me and Dupree': {'Claudia Puig': 2.5,
  'Gene Seymour': 3.5,
  'Jack Matthews': 3.5,
  'Lisa Rose': 2.5,
  'Mick LaSalle': 2.0,
  'Toby': 1.0}}
  
  
#key_a = 'The Night Listener'
#key_b = 'Snakes on a Plane'

def foo(m, key_a):
    dic_bhai = {}
    for key in m:
        if key != key_a:
            key_b = key
            #print "key_a = {} key_b = {}".format(key_a, key_b)
    
            #s1 = [m[key_b][ll] for ll in m[key_a] if ll in m[key_b]]
            s1=[]
            s2=[]
            for ll in m[key_a]:
                if ll in m[key_b]:
                    #print ll, m[key_a][ll],  m[key_b][ll]
                    s1.append(m[key_a][ll])
                    s2.append(m[key_b][ll])
            '''    
            s2 = []
            print "\n"
            for dd in m[key_b]:
                print dd, m[key_b][dd]
                s2.append(m[key_b][dd])
            '''    
            #print s1, s2
                        
            #print scipy.stats.pearsonr(s1, s2)[0]
            #print  np.corrcoef(s1,s2)[1][0]
            dic_bhai[key] = np.corrcoef(s1,s2)[1][0]
            #break
    return dic_bhai

    
a = {}
#pdb.set_trace()
for dudes in m:
    a[dudes] =  foo(m, dudes)
        

print a
'''
[a[key_b][ll] for ll in a[key_a] if ll in a[key_b]]
Out[44]: [4.0, 4.0, 3.5, 3.5, 3.5, 3.0]

[[ll] for ll in a[key_a] if ll in a[key_b]]
Out[45]: 
[['Jack Matthews'],
 ['Mick LaSalle'],
 ['Claudia Puig'],
 ['Lisa Rose'],
 ['Gene Seymour'],
 ['Michael Phillips']]

[ll for ll in a[key_a] if ll in a[key_b]].sort()

[ll for ll in a[key_a] if ll in a[key_b]]
'''