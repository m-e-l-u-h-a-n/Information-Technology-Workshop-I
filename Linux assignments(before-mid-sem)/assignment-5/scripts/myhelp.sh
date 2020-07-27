#!/bin/bash
clear
echo "				UNIX HELP MAIN MENU"
echo "1--File and Directory Management Commands"
echo "2--Text Processing Commands"
echo "3--System Status Commands"
echo "4--Exit"
echo
echo -e "			Enter Your Choice:\c"
read x
flag=0
while test $flag -eq 0
do

if test $x -ge 1 -a $x -lt 5
then
flag=$(($flag+1))
else
echo -e "Enter the numerical value to the corresponding to above options: \c"
read x
fi

done

if test $x -ge 1 -a $x -lt 4
then
sh submenu1.sh $x
else
echo "You selected to exit"
fi
