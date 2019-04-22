ping -i 3 -c 100 google.fr | grep time= | awk 'BEGIN {FS="[=]|[ ]"} {print $11}' > data/fr.txt
