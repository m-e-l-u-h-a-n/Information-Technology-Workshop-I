#!/bin/bash
if test $1 -eq 1
then
echo "				TEXT PROCESSING COMMANDS"
echo "			1--Search a file for a pattern"
echo "			2--Count lines,words,and charcters in specified files"
echo "			3--Display the diffrences between two files"
echo "			4--HELP"
echo "			5--Quit--return to main"
echo ""
echo -e "			Enter your choice: \c"
read op
flag=0
while test $flag -eq 0
do
if test $op -ge 1 -a $op -le 5
then
flag=$(($flag+1))
else
echo "enter numerical values for above options: "
read op
fi
done

if test $op -eq 1
then
echo "demonstrating grep command by searching 'linux' in linux.txt"
grep "linux" linux.txt
sh text.sh 1
elif test $op -eq 2
then
echo "demonstrating wc command in linux.txt"
wc linux.txt
sh text.sh 1
elif test $op -eq 3
then
echo "demonstrating diff command on file1.txt and file2.txt"
diff file1.txt file2.txt
sh text.sh 1
elif test $op -eq 4
then
echo "directing to help menu for novice mode"
sh help.sh
elif test $op -eq 5
then
sh myhelp.sh
fi

# expert mode programming 

elif test $1 -eq 2
then
echo "				TEXT PROCESSING COMMANDS"
echo "			1--Search a file for a pattern"
echo "			2--Count lines,words,and charcters in specified files"
echo "			3--Display the diffrences between two files"
echo "			4--Quit--return to main"
echo -e "			Enter your choice: \c"
read op
flag=0
while test $flag -eq 0
do
if test $op -ge 1 -a $op -le 5
then
flag=$(($flag+1))
else
echo "enter numerical values for above options: "
read op
fi
done

if test $op -eq 1
then
echo "demonstrating grep command by searching 'linux' in linux.txt"
grep "linux" linux.txt
sh text.sh 2
elif test $op -eq 2
then
echo "demonstrating wc command in linux.txt"
wc linux.txt
sh text.sh 2
elif test $op -eq 3
then
echo "demonstrating diff command on file1.txt and file2.txt"
diff file1.txt file2.txt
sh text.sh 2
elif test $op -eq 4
then
sh myhelp.sh
fi
fi
