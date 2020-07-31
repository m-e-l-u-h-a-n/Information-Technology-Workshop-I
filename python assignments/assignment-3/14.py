import os
import shutil
print('My current working directory is: ',os.getcwd())
newdir=input('Enter the name of new directory to be created: ')
try:
    os.mkdir(os.getcwd()+'/'+newdir)
except OSError:
    print('directory creation failed')
#creating a file in the directory
else:
    print('directory creation successful, writing a new file to created directory')
    try:
        with open(os.getcwd() + '/' + newdir + '/myfile.txt', 'a') as file:
            file.write('This is a newly created file in this directory')
    except Exception:
        print('couldn\'t create new file in the new directory')
    else:
        print('a new file named myfile.txt has been created in the new directory')
        x=input('press q to delete the newly created directory: ')
# deleting the directory
        if x=='q':
            try:
                shutil.rmtree(os.getcwd() + '/' + newdir, ignore_errors=True)
            except Exception as e:
                print('new directory couldn\'t be deleted', e)
            else:
                print('successfully deleted the newly created directory')
        else:
            exit(1)

