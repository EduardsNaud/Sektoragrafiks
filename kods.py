import matplotlib.pyplot as plt
dalas=[69,100,150,21,20]
nosauk=['Āboli',"Bumbieri","Banāni", "Zemenes","Brūklenes"]
krasas=["maroon","darkkhaki","teal","rebeccapurple","forestgreen"]
izcelums=[0.02,0.02,0.02,0.02,0.02]
plt.pie(dalas,labels=nosauk,explode=izcelums,autopct="%.2f",colors=krasas)
plt.show()