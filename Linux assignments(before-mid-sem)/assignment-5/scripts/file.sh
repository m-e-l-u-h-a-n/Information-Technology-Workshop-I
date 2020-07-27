#!/bin/bash

if test $1 -eq 1
then
echo "			FILE AND DIRECRTORY CONTROL COMMANDS"
echo
echo "		1--Display the contents of a file"
echo "		2--Remove a file"
echo "		3--Copy a file"
echo "		4--List a File"
echo "		5--Size of a file"
echo "		6--Quit--Return to main Menu"
echo "		7--Help"
echo -e "		Enter Your Option: \c"
read op
flag=0
while test $flag -eq 0
do

if test $op -ge 1 -a $op -lt 8
then
flag=$((flag+1))
break
else
echo "Enter The Numerical Value For The Given Options"
read op
fi

done

if test $op -eq 1
then
echo "command used is cat"
cat testfile1.txt
sh file.sh 1
elif test $op -eq 2
then
echo "command used is rm"
rm testfile2.txt
touch testfile2.txt
sh file.sh 1
elif test $op -eq 3
then
echo "command used is cp"
cp testfile1.txt
sh file.sh 1
elif test $op -eq 4
then
echo "command used is ls -l"
ls -l testfile1.txt
sh file.sh 1
elif test $op -eq 5
then
echo "command used is du"
du  testfile1.txt
sh file.sh 1
elif test $op -eq 6
then
echo "command used is sh myhelp.sh"
sh myhelp.sh
elif test $op -eq 7
then
echo "command used is sh help.sh 1"
sh help.sh 1
fi
#expert mode programming
elif test $1 -eq 2
then
echo "			FILE AND DIRECRTORY CONTROL COMMANDS"
echo
echo "		1--Display the contents of a file"
echo "		2--Remove a file"
echo "		3--Copy a file"
echo "		4--List a File"
echo "		5--Size of a file"
echo "		6--Exit Program"
echo -e "		Enter Your Option: \c"
read op
flag=0
while test $flag -eq 0
do

if test $op -ge 1 -a $op -lt 7
then
flag=$(($flag+1))
else
echo "Enter The Numerical Value For The Given Options"
read op
fi

done

if test $op -eq 1
then
echo "command used is cat"
cat testfile1.txt
sh file.sh 2
elif test $op -eq 2
then
echo "command used is rm"
rm testfile2.txt
touch testfile2.txt
sh file.sh 2
elif test $op -eq 3
then
echo "command used is cp"
cp testfile1.txt
sh file.sh 2
elif test $op -eq 4
then
echo "command used is ls -l"
ls -l testfile1.txt
sh file.sh 2
elif test $op -eq 5
then
echo "command used is du"
du  testfile1.txt
sh file.sh 2
elif test $op -eq 6
then
echo "command used is sh Exit"
fi
fi
