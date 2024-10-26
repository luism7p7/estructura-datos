invertir=float(input(('cuanto deseas invertir')))

anual=int(input('cuantos años deseas invertir'))
interez=float(input('cuantos  deseas dar el interez'))

plan= invertir*(1+interez/100)**anual##formula interes porcentual
plant=round(plan,2)

print(plan)


