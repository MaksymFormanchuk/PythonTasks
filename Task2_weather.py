from pyowm import OWM

with open('key.txt') as file:                     # read API key from file
    key = str(file.read())

owm = OWM(key)                                     # Valid API key

place = input("Enter your city: ")

mgr = owm.weather_manager()                        # call weather manager
observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]             # getting weather details
wind = w.wind('meters_sec')['speed']
humid = w.humidity
detail_st = w.detailed_status

print("It's " + detail_st + " in " + place + " and the temperature is " + str(temp) + " degrees Celsius")
print("The humidity in " + place + " is " + str(humid) + "% and the wind is " + str(wind) + "m/s" )