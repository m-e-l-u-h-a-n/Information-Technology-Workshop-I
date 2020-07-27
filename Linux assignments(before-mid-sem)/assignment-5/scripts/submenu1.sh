#!/bin/bash
echo "					Enter The Mode"
echo "		1--Novice Mode"
echo "		2--Expert Mode"
echo "			Enter Your Choice: \c"
read mode
flag=0

while test $flag -eq 0
do
if test $mode -eq 1 -o $mode -eq 2
then
flag=$(($flag+1))
else
echo -e "Enter the numerical values for the above options: \c"
read mode
fi
done

if test "$1" -eq 1
then
sh file.sh $mode
elif test "$1" -eq 2
then 
sh text.sh $mode
elif test "$1" -eq 3
then 
sh status.sh $mode
fi
