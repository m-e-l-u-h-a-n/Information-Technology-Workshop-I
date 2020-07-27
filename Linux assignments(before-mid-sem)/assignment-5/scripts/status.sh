#!/bin/bash
if test $1 -eq 1
then
echo "					SYSTEM STATUS COMMANDS"
echo "				1--Display the current date and time"
echo "				2--Current disk usage"
echo "				3--List current and environmental"
echo "				4--Display process status information"
echo "				5--HELP"
echo "				6--QUIT--Return to main menu"
echo -e "		Enter Your Option: \c"
read op
flag=0
while test $flag -eq 0
do

if test $op -ge 1 -a $op -lt 7
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
echo "command used is date"
date +%d/%m/%y
sh status.sh 1
elif test $op -eq 2
then
echo "command used is du"
du
sh status.sh 1
elif test $op -eq 3
then
echo "command used is printenv"
printenv PWD
sh status.sh 1
elif test $op -eq 4
then
echo "command used is top"
top 
sh status.sh 1
elif test $op -eq 5
then
echo "command used is sh help.sh"
sh help.sh
elif test $op -eq 6
then
echo "command used is sh myhelp.sh"
sh myhelp.sh
fi
#expert mode programming
elif test $1 -eq 2
then
echo "					SYSTEM STATUS COMMANDS"
echo "				1--Display the current date and time"
echo "				2--Current disk usage"
echo "				3--List current and environmental"
echo "				4--Display process status information"
echo "				5--QUIT--Return to main menu"
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
echo "command used is date"
date +%d/%m/%y
sh status.sh 2
elif test $op -eq 2
then
echo "command used is du"
du
sh status.sh 2
elif test $op -eq 3
then
echo "command used is printenv"
printenv PWD
sh status.sh 2
elif test $op -eq 4
then
echo "command used is top"
top 
sh status.sh 2
elif test $op -eq 5
then
echo "command used is sh myhelp.sh"
sh myhelp.sh
fi
fi
