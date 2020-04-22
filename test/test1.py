name= input("Hallo, bitte gib deinen Namen ein!")
alter= input("Bitte gib dein Alter ein!")

diff=100-int(alter)
jahr=2020+diff

print(name+", Du wirst "+str(jahr)+" 100 Jahre alt sein!")

zahl= input("Bitte gib noch eine weitere Zahl ein!")

for i in range(int(zahl)):
   print(name+", Du wirst "+str(jahr)+" 100 Jahre alt sein!")