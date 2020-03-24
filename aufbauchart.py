"""
A Python3 program to print the Aufbau Chart

This is a topic of Atomic Structure (Chemistry)
Specifically, the Quantum Model of Atoms

"""

l='spdf'+#'ghijklmnopqrstuvwxyz'        #remove the first hashtag in this line to print upto the Z-orbital
#l=l.upper()                            #remove the first hashtag in this line to print the orbital letters in UPPERCASE
n=[None]
for z in range(1,len(l)+1):
    n.append(str(z))
for a in range(1,len(l)+len(n)+1):
    for i in range(len(n)):
        for j in range(i):
            if i+j==a:
                print(n[i]+l[j])
                break
            else:
                continue
            break