import tarfile
import os

# build  package/dir list
projects = [{'package':item,'dir':item.split('.')[2:3][0]} 
                 for item in os.listdir('./') 
                 if item.startswith('web2py.app.')]

opener, mode = tarfile.open, 'r:gz' 

# iterate over each create directory then unpack into the target directory
startdir = os.getcwd()
os.mkdir('unpacked')
for project in projects:
    targetdir = 'unpacked/' + project['dir'].replace('-','_')
    # make the directory
    print 'making ', targetdir
    try: 
        os.mkdir(targetdir)
    except OSError:
        pass
    # enter the directory
    print 'entering ', targetdir
    os.chdir(targetdir)
    print "now in ", os.getcwd()

    # unpack the package
    path = startdir + '/'  + project['package']
    print 'unpacking ', path
    file = opener(path, mode)
    file.extractall()
    os.chdir(startdir)
