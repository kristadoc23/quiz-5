def thermostat(temp):
    if temp <= 52:
        print("The heater is on")
    elif 52< temp < 71:
        print("Heater and AC are off")
    else:
        print("AC is on")

thermostat(50)
thermostat(55)
thermostat(75)
