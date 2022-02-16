def centigrade(Fahrenheit):
    return (5.0 / 9.0) * (Fahrenheit - 32)

Fahrenheit = int(input())
Celsia = centigrade(Fahrenheit)

print(f"{Fahrenheit} fahrenheit is {Celsia} centigrade")
