##itw1 asignment 1##
#1.
ls -p|grep -v|grep "lib"|wc -l>count.txt u
#2.
ls -au > list.txt
#3.
ps -U root-u root u>processes.txt
#  or
ps -ef |grep "^root" > processes.txt
#4.
tr ' ' '\12' filename | sort|uniq -c |sort -nr
#5.
who -q
#6.
	#(i)
		df -h
  	#(ii)
		history
#7.
	#(i) 
		cap sourcefile destination file
  	#(ii)
		cat file1 file2 > file3
#8.
##system control commands:
	#mkdir,cd,pwd,rmdir,ls,touch,mv,cp,ln,cat,less,fined
##process control commands:
     	#bg,fg
##utilities control commands:
     	#which,man,find,su
#9.
grep a filname |grep e | grep i | grep o | grep u
#10.
sort -u file1 file2
# or:
sort file1|uniq > file2
#11.
ls -S |grep ".conf" |head -5
#12.
grep LINUX* | grep -vc "unix"
#13.
grep -iv unix*
#14.
	#(i)
		date "+%d-%m-%y"
   	#(ii) 
		grep -o "linux" filename | wc
