import math

a = int(input('Ieraksti Pirmas loterejas visus skaitļus : '))
b = int(input('Ieraksti cik ir pozitivi no viņiem : '))
c = int(input('Ieraksti Otras loterejas visus skaitļus : '))
d = int(input('Ieraksti cik ir pozitivi no viņiem : '))

def varbutiba():

    first = b/a*100
    second = d/c*100

    if first > second:
        print("Pirmas loterejas uzvaras procents ir lielaks un viņš ir", first, "%")

    elif first < second:
        print("Otras loterejas uzvaras procents ir lielaks un viņš ir", second, "%")
    elif first == second:
        print("Pirmas un otras loterejas uzvaras procents ir vienads un viņš ir", first, "%")
        
varbutiba()

def kombinatorika():

    first = b / a
    second = d / c

    if first > second:
        print("Tas ir iespējamais kombinācijas skaits: ", (math.factoriab(b)))
    elif first < second:
        print("Tas ir iespējamais kombinācijas skaits: ", (math.factorial(d)))
    elif first == second:
        print("Tas ir iespējamais kombinācijas skaitss(Pirma loterijai): ", (math.factorial(b)))
        print("Tas ir iespējamais kombinācijas skaitss(Otra loterijai): ", (math.factorial(d)))
