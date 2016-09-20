xdpyinfo | grep dimensions | sed -e 's/dimensions://g' -e 's/([^()]*)//g' -e 's/pixels//g' | xargs echo "Resolution:"
lspci | grep VGA | sed -e 's/.*://' | xargs echo "Graphics:"
lscpu | grep 'Model name' | sed -e 's/.*://' | xargs echo "CPU:"
upower -e | grep battery | xargs upower -i | grep capacity | sed -e 's/.*://' | xargs echo "Battery Health:"
