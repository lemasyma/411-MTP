ping -i 3 -c 100 google.fi | grep time= | awk 'BEGIN {FS="[=]|[ ]"} {print $11}' > fi.txt
