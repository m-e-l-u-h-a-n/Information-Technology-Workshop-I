#!/bin/bash
isprime()
{
i=2
while(( i<=$((a/2)) ))
do
if (( $((a%i))==0 ))
then
flag=1
breakfi
i=$((i+1))
done
}
echo "How many prime numbers"
read p
a=2
k=0
while(( k<p ))
do
flag=0
isprime a
if(( flag==0 ))
then
echo "$a"
k=$((k+1))
fi
a=$((a+1))
done