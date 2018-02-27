# !/bin/bash


TEST_NAME="TP1" # name of the working directory
rm -rf ${TEST_NAME} # cleaning working directory
mkdir -p ${TEST_NAME}
cd ${TEST_NAME}

# initialising initial git workspace
mkdir ws1
cd ws1
#git init 
darcs initialize

# adding a file to ws1
# commit changes
echo "1\n2\n3\n4\n5\n6\n" > file.txt
#git add file.txt
#git commit -m "ws1 | add 123456 to file.txt"
darcs add file.txt
darcs record -m "ws1 add 123456 to file.txt"
cd ..

# cloning three times ws1 (as ws2, ws3)
#git clone ws1 ws2
#git clone ws1 ws3
darcs clone ws1 ws2
darcs clone ws1 ws3



# updating file.txt in ws2 (insert X at line 3, then write and quit 'ed')
# commit changes
cd ws2
echo  "2d\nw\nq\n" | ed file.txt
echo  "2i\nX\n.\nw\nq\n" | ed file.txt
echo  "4d\nw\nq\n" | ed file.txt
echo  "4i\nY\n.\nw\nq\n" | ed file.txt
echo  "5d\nw\nq\n" | ed file.txt
echo  "5i\nZ\n.\nw\nq\n" | ed file.txt

#git add file.txt
#git commit -m "ws2 | insert 12X34Y5Z"

darcs record -am "ws2 insert 12X34Y5Z"
cd ..

# updating file.txt in ws3 (insert Y at line 3, then write and quit 'ed')
# commit changes
cd ws3
echo  "3d\nw\nq\n" | ed file.txt
echo "3i\nW\n.\nw\nq\n" | ed  file.txt

#git add file.txt
#git commit -m "ws3 | insert 123W45"

darcs record -am "ws3 insert 123W45"

cd ..



cd ws1
darcs pull ../ws2
darcs pull ../ws3

cd ..
