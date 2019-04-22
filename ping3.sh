ping -i 3 -c 100 google.pl | grep time= | awk 'BEGIN {FS="[=]|[ ]"} {print $11}' > pl.txt
