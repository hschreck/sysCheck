xdpyinfo | grep dimensions | sed -e 's/dimensions://g' -e 's/([^()]*)//g' -e 's/pixels//g' | xargs \
	echo "Resolution    :"
lspci | grep VGA | sed -e 's/.*://' | xargs \
	echo "Graphics      :"
lscpu | grep 'Model name' | sed -e 's/.*://' -e 's/([^()]*)//g' | xargs \
	echo "CPU           :"
BATTERY=`upower -e | grep battery | xargs upower -i | grep capacity | sed -e 's/.*://' -e 's/%//' ` 
if [ $BATTERY -le 50 ]
then
	echo "Battery Health: Poor (Dispose)"
	exit 1;
elif [ $BATTERY -le 80 ]
then
	echo "Battery Health: Moderate (Grade B)"
	exit 1;
elif [ $BATTERY -gt 80 ]
then
	echo "Battery Health: Good (Grade A)"
	exit 1;
else
	echo "There was an error, battery health is at " $BATTERY
	exit 1;
fi
