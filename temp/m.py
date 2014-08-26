import scipy.stats 
import numpy as np
import pdb

m = {'Terminator': {'Tom': 4.0,
  'Jack': 1.5,
  'Lisa': 3.0,
  'Sally': 2.0},
  
 'Terminator 2': {'Tom': 5.0,
  'Jack' : 1.0,
  'Lisa': 3.5,
  'Sally': 2.0},
  
 'It happened one night': {'Tom': 3.5,
  'Jack': 3.5,
  'Tiger': 4.0,
  'Lisa': 5.0,
  'Michele': 3.0,
  'Sally': 4.0,},
  
 '27 Dresses': {'Tom': 3.0,
  'Jack': 3.5,
  'Tiger': 3.0,
  'Lisa': 5.0,
  'Michele': 4.0,
  'Sally': 4.0},

  'Poirot': {'Tom': 4.0,
  'Jack': 3.0,
  'Tiger': 5.0,
  'Lisa': 4.0,
  'Michele': 3.5,
  'Sally': 3.0,
  },

 'Sherlock Holmes': {'Tom': 4.0,
  'Jack': 3.0,
  'Tiger': 3.5,
  'Lisa': 3.5,
  'Sally': 2.0,
  }}
  
  
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

my = {'Terminator': 5.0,
      'Sherlock Holmes' : 4.0,
      'Poirot' : 4.5
      }

for cnt in my.keys():
 if cnt in v.keys():
     #print my[cnt], v[cnt]
     for cnt2 in v[cnt]:
         print cnt, cnt2
         print v[cnt][cnt2]

total = {}         
# find all movies not reviewed         
for cnt in my.keys():
 if cnt in v.keys():
     #print my[cnt], v[cnt]
     for cnt2 in v[cnt]:
         if cnt2 not in  my.keys():
            print cnt2
            print v[cnt][cnt2]
            if cnt2 in total:
                total
            else:
                total.setdefault(cnt2, v[cnt][cnt2] )
print total            
         
      
'''
[a[key_b][ll] for ll in a[key_a] if ll in a[key_b]]
Out[44]: [4.0, 4.0, 3.5, 3.5, 3.5, 3.0]

[[ll] for ll in a[key_a] if ll in a[key_b]]
Out[45]: 
[['Tiger'],
 ['Sally'],
 ['Tom'],
 ['Lisa'],
 ['Jack'],
 ['Michele']]

[ll for ll in a[key_a] if ll in a[key_b]].sort()

[ll for ll in a[key_a] if ll in a[key_b]]

v={'27 Dresses': {'Poirot': -0.30434782608695654, 'Terminator 2': -0.12547286652195427, 'It happened one night': 0.5791405068790082, 'Sherlock Holmes': -0.27583864218368526, 'Terminator': -0.15404159684748153}, 'It happened one night': {'Terminator 2': 0.13468700594029476, '27 Dresses': 0.5791405068790082, 'Terminator': 0.10629880069054677, 'Sherlock Holmes': 0.0, 'Poirot': 0.2895702534395041}, 'Terminator 2': {'Poirot': 0.90726470872655474, '27 Dresses': -0.12547286652195427, 'It happened one night': 0.13468700594029476, 'Sherlock Holmes': 0.73889576951817515, 'Terminator': 0.99861543720375834}, 'Terminator': {'Terminator 2': 0.99861543720375834, '27 Dresses': -0.15404159684748153, 'It happened one night': 0.10629880069054677, 'Sherlock Holmes': 0.77020798423740755, 'Poirot': 0.91132237686576711}, 'Poirot': {'Terminator 2': 0.90726470872655474, '27 Dresses': -0.30434782608695654, 'It happened one night': 0.2895702534395041, 'Sherlock Holmes': 0.66989384530323559, 'Terminator': 0.91132237686576711}, 'Sherlock Holmes': {'Poirot': 0.6698938453032357, 'Terminator 2': 0.73889576951817515, '27 Dresses': -0.27583864218368526, 'It happened one night': 0.0, 'Terminator': 0.77020798423740755}}


for cnt in my.keys():
 if cnt in v.keys():
     #print my[cnt], v[cnt]
     for cnt2 in v.keys():
         print cnt, cnt2
         #print v[cnt][cnt2]
         
         

'''
