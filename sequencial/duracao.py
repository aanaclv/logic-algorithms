#1 min = 60 segundos
# 1 hora = 60 min
#1 hora = 3600 segundos

duracao = int(input("digite a duração em segundos: "))
horas = duracao/3600
resto = duracao%3600
minutos = resto/60
segundos = resto%60

print(f"{horas:.0f}:{minutos:.0f}:{segundos:.0f}")