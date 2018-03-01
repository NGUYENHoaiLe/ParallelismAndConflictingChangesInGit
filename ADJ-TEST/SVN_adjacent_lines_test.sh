# !/bin/bash


TEST_NAME="TP1" # name of the working directory
rm -rf ${TEST_NAME} # cleaning working directory
mkdir -p ${TEST_NAME}
cd ${TEST_NAME}

# initialising initial git workspace
mkdir ws1
cd ws1

# adding a file to ws1
# commit changes
echo "1\n2\n3\n4\n5\n6\n" > file.txt
svn import file.txt file:///home/svn/myproject


# create a branch
svn copy file:///home/svn/myproject file:///home/svn/myproject/branch1 -m "Creating a private branch"

#
svn co file:///home/svn/myproject
echo  "2d\nw\nq\n" | ed file.txt
echo  "2i\nX\n.\nw\nq\n" | ed file.txt
echo  "4d\nw\nq\n" | ed file.txt
echo  "4i\nY\n.\nw\nq\n" | ed file.txt
echo  "5d\nw\nq\n" | ed file.txt
echo  "5i\nZ\n.\nw\nq\n" | ed file.txt
svn commit

svn co file:///home/svn/myproject/branch1
echo  "3d\nw\nq\n" | ed file.txt
echo "3i\nW\n.\nw\nq\n" | ed  file.txt
svn commit


svn co file:///home/svn/myproject
svn merge  file:///home/svn/myproject/branch1

