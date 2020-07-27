echo "Welcome to the help window for the novice mode"
printf "\n\n"
echo "> For navigating through the main menu enter the numerical value corresponding to the provided options"
printf "\n"
echo "> Ater you enter a valid option in the main menu you are to select the mode of operation novice or expert in the submenu that appears by selecting the numerical values corresponding to the option"
printf "\n"
echo "This help menu is for novice mode only"
printf "\n\n"
echo "FILE AND DIRECTORY MANAGEMENT COMMAND HELP"
printf "\n"
echo "> Enter the numerical value corresponding to the provided options"
echo "> If 1 is Selected contents of a file named testfile1.txt is displayed using cat command"
echo "> If 2 is selected a file named testfile2.txt is removed using rm command"
echo "> If 3 is selected contents of a file named testfile1.txt are copied to file3.txt using cp command"
echo "> If 4 is selected long format listing of a file  named testfile1.txt is done using ls -l command"
echo "> If 5 is selected this help window is opened"
echo "> If 6 is selected you are directed to the main menu again"
printf "\n\n"
echo "TEXT PROCESSING COMMAND HELP"
printf "\n"
echo "> Enter the numerical value corresponding to the provided options"
echo "> If 1 is selected a pattern linux is searched in file linux.txt using grep command "
echo "> If 2 is selected wc command is run on a file named linux.txt to count lines, words and characters"
echo "> If 3 is diffrences between two files are displayed using diff command"
echo "> If 4 is selected this help window is opened"
echo "> If 5 is selected you are directed to main menu again"
printf "\n\n"
echo "SYSTEM STATUS COMMAND HELP"
printf "\n"
echo "> Enter the numerical value corresponding to the provided options"
echo "> If 1 is selected date and time are displayed using date command"
echo "> If 2 is selected current disk usage is displayed using du command"
echo "> If 3 is selected environment variable corresponding to the PWD is printed using printenv command"
echo "> If 4 is selected top command is run to display the status of currently running processes"
echo "> If 5 is selected this help window is opened"
echo "> If 6 is selected you are directed to the main menu again"
printf "\n"
echo -e "Enter q to go main menu again: \c"
read v
flag=0
while test $flag -eq 0
do
if test "$v" = "q"
then
sh myhelp.sh 
flag=$(($flag+1))
else
echo -e "Enter q to go the main menu again: \c"
read v
fi
done
