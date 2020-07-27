#!/bin/bash
echo "Enter a year : "
read year
if ((year%100==0))
then
if ((year%400==0))
then
echo "Leap year"
else
echo "Not a leap year"
fi
else
if ((year%4==0))
then
echo "Leap year"
else
echo "Not a leap year"
fi
fi