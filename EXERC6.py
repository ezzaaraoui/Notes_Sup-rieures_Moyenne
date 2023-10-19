
T=[]

n=int(input("donner le nombre d'etudiant : "))
s=0
for i in range(0,n):
    T.append(int(input(f"donner la note de l'etudiant {i+1} : ")))
    s=s+T[i]

m=s/n
c=0
for i in range(0,n):
    if T[i]>m :
        c+=1

print(f" les notes supérieures à la moyenne est {c}")