#Desafio 26
#Débora Janini

dia_ini = input().split(' ')

s_dia_i = str(dia_ini[0])
n_dia_i = int(dia_ini[1])

horarioi = input().split(" : ")

hi = int(horarioi[0])
mi = int(horarioi[1])
si = int(horarioi[2])

dia_fin = input().split(' ')

s_dia_f = str(dia_fin[0])
n_dia_f = int(dia_fin[1])

horariof = input().split(" : ")

hf = int(horariof[0])
mf = int(horariof[1])
sf = int(horariof[2])

seg_total_i = si + (mi*60) + (hi*3600) + (n_dia_i * 86400)
seg_total_f = sf + (mf*60) + (hf*3600) + (n_dia_f * 86400)


seg_final = seg_total_f - seg_total_i

#O final sempre será maior que o inicial, pois 
#está no mesmo mês, terminando em um dia de numeor maior
#mas por desencargo de conciência


if seg_final < 0:
    seg_final += 24*60*60


dias = seg_final//86400
seg_final -= dias*86400

horas =  seg_final//3600
seg_final -= horas*3600

minutos = seg_final //60 
segundos = seg_final%60

print(dias, "dia(s)")
print(horas, "hora(s)")
print(minutos, "minuto(s)")
print(segundos, "segundo(s)")