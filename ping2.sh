ping -i 3 -c 100 google.es | grep time= | awk 'BEGIN {FS="[=]|[ ]"} {print $11}' > data/es.txt
