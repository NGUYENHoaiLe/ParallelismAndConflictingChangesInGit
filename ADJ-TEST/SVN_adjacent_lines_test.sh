# !/bin/bash

###
#svn need to be install on your local machine *Ubuntu 16.04*
###

TEST_NAME="TP1" # name of the working directory
rm -rf ${TEST_NAME} # cleaning working directory
mkdir -p ${TEST_NAME}
cd ${TEST_NAME}




svn mkdir trunk
svn mkdir -m "Making a new dir." http://127.0.0.1/svn/myrepo/trunk
svn mkdir branch
svn mkdir -m "Making a new dir." http://127.0.0.1/svn/myrepo/branch

mkdir trunk
cd trunk
svn co http://127.0.0.1/svn/myrepo/trunk --username admin
echo "1\n2\n3\n4\n5\n6\n" > file.txt

svn add file.txt
svn commit -m "ws1 | add 123456 to file.txt"

cd ..


# create a branch

svn copy http://127.0.0.1/svn/myrepo/trunk http://127.0.0.1/svn/myrepo/branch -m "Creating a private branch"


cd trunk
svn co http://127.0.0.1/svn/myrepo/trunk --username admin

echo  "2d\nw\nq\n" | ed file.txt
echo  "2i\nX\n.\nw\nq\n" | ed file.txt
echo  "4d\nw\nq\n" | ed file.txt
echo  "4i\nY\n.\nw\nq\n" | ed file.txt
echo  "5d\nw\nq\n" | ed file.txt
echo  "5i\nZ\n.\nw\nq\n" | ed file.txt
svn commit -m "ws2 | insert 12X34Y5Z"
cd ..

#
mkdir branch
cd branch
svn switch
svn co http://127.0.0.1/svn/myrepo/branch --username admin

echo  "3d\nw\nq\n" | ed file.txt
echo "3i\nW\n.\nw\nq\n" | ed  file.txt
svn commit -m "ws3 | insert 123W45"
cd ..

cd trunk
svn up	
svn merge  http://127.0.0.1/svn/myrepo/branch

