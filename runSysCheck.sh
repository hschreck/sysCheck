xdpyinfo | grep dimensions
lspci | grep VGA
lscpu | grep 'Model name'
upower -e | grep battery | xargs upower -i | grep capacity
