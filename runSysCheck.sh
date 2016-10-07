xdpyinfo | grep dimensions | sed -e 's/dimensions://g' -e 's/([^()]*)//g' -e 's/pixels//g' | xargs \
	echo "Resolution    :"
lspci | grep VGA | sed -e 's/.*://' | xargs \
	echo "Graphics      :"
lscpu | grep 'Model name' | sed -e 's/.*://' -e 's/([^()]*)//g' | xargs \
	echo "CPU           :"
lscpu | grep 'per socket' | sed 's/.*:.*\([0-9]\)/\1/' | xargs \
	echo "CPU Cores     :"
python syscheck.py
