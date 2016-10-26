import os
workaround = 0

health_low=50
health_mid=80

designcap = os.popen("sudo dmidecode --type 22 | grep 'Design Capacity' | sed 's/[^0-9]*//g' ").read()

designvolt = os.popen("sudo dmidecode --type 22 | grep 'Design Voltage' | sed 's/[^0-9]*//g' ").read()

currentcap = os.popen("upower -e | grep battery | xargs upower -i | grep energy-full: | sed -e 's/ Wh//' -e 's/.* //' ").read()

modelName = os.popen("sudo dmidecode --type 1 | grep 'Product Name' | sed -e 's/.*: //g' ").read()
modelName = modelName.rstrip("\n")
print("Model         : " + modelName)
designcap = float(designcap) / 1000

currentcap=float(currentcap)
#print(designcap)
#print(currentcap)
#modified workaround based on battery percentage being reported incorrectly instead of on model

#Allows up to 110% of capacity before using workaround
if (currentcap/designcap) > 1.1:
    designcap = designcap * designvolt / 1000
    workaround = 1
health = round((currentcap/designcap) * 100, 2)

if health < health_low :
    print("Battery       : " + str(health) + "% (Dispose)")
elif health < health_mid :
    print("Battery       : " + str(health) + "% (Grade B)")
elif health > health_mid :
    print("Battery       : " + str(health) + "% (Grade A)")
else:
    print("Battery not detected or is dead.")

if workaround == 1:
    print("This was calculated using a workaround for improperly-reported levels; if this reads 100% or just seems wrong, contact harold.schreckengost@er2.com")
