#!/bin/bash
echo -n "Enter digits : "
read a
while [ $a -gt 0 ]
do
num=$((a%10))
echo -n $num
a=$((a/10))
done
echo ''