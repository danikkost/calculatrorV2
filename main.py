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

def kombinatorika():


    print(math.factorial(a))
