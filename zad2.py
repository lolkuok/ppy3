import random


plan: str = "Panie, panowie jedziemy do"
miasta = {" Radom", " Sosnowiec",
          " Bydgoszcz", " Torun",
          " Ohio", " Chicago",
          " Dublin", " Lodz",
          " Jaworzno", " Kielce"}
lm = list(miasta)
for i in range(0, 9):
    print (i,':')
    a = random.randint(0, 9-i)
    print(a,lm[a],"Idzie do gułagu")
    plan = plan + lm[a]
    del lm[a]

print(plan)
