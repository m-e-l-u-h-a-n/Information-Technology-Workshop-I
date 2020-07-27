#!bin/sh
echo "Enter a string"read s
if [[ $(rev <<< "$s") == "$s" ]]
then
echo "Palindrome"
else
echo "Not a Palindrome"
fi