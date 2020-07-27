#!bin/sh
i=1
while(( i<1000 ))
do
t=$i
b=0
while(( t>0 ))
do
a=$((t%10))
b=$((b+(a*a*a)))
t=$((t/10))
done
if(( $b==$i ))
then
echo "$i "
fi
i=$((i+1))
done