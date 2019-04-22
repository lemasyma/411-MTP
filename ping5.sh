ping -i 3 -c 100 google.lv | grep time= | awk 'BEGIN {FS="[=]|[ ]"} {print $11}' > lv.txt
