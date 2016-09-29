import os

workaroundModels= [
        'HP EliteBook 2540p',
        ]

health_low=50
health_mid=80

designcap = os.popen("sudo dmidecode --type 22 | grep 'Design Capacity' | sed 's/[^0-9]*//g' ").read()

designvolt = os.popen("sudo dmidecode --type 22 | grep 'Design Voltage' | sed 's/[^0-9]*//g' ").read()

currentcap = os.popen("upower -e | grep battery | xargs upower -i | grep energy-full: | sed -e 's/ Wh//' -e 's/.* //' ").read()

modelName = os.popen("sudo dmidecode --type 1 | grep 'Product Name' | sed 's/.*: //g' ").read()

if modelName in workaroundModels:
    designcap = float(designcap)/1000 * float(designvolt)/1000 
else:
    designcap = float(designcap) / 1000

currentcap=float(currentcap)
#print(designcap)
#print(currentcap)
health = round((currentcap/designcap) * 100, 2)

if health < health_low :
    print("Battery       : " + str(health) + "% (Dispose)")
elif health < health_mid :
    print("Battery       : " + str(health) + "% (Grade B)")
elif health > health_mid :
    print("Battery       : " + str(health) + "% (Grade A)")
else:
    print("Battery not detected or is dead.")

