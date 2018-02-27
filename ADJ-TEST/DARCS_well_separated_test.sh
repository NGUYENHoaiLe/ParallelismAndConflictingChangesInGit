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
echo "1\n2\n3\n4\n5\n6\n7" > file.txt

#git add file.txt
#git commit -m "ws1 | add 1234567 to file.txt"
darcs add file.txt
darcs record -am "ws1 | add 1234567 to file.txt"
cd ..

# cloning three times ws1 (as ws2, ws3)
#git clone ws1 ws2
#git clone ws1 ws3
darcs clone ws1 ws2
darcs clone ws1 ws3



# updating file.txt in ws2 (insert X at line 3, then write and quit 'ed')
# commit changes
cd ws2
echo  "1d\nw\nq\n" | ed file.txt
echo  "1i\n7\n.\nw\nq\n" | ed file.txt
echo  "1i\n6\n.\nw\nq\n" | ed file.txt
echo  "1i\n5 \n.\nw\nq\n" | ed file.txt
echo  "9d\nw\nq\n" | ed file.txt
echo  "8d\nw\nq\n" | ed file.txt
echo  "7d\nw\nq\n" | ed file.txt 
#git add file.txt
#git commit -m "ws2 |  567234"

darcs record -am "ws2 |  567234"
cd ..

# updating file.txt in ws3 (insert Y at line 3, then write and quit 'ed')
# commit changes
cd ws3
echo  "3d\nw\nq\n" | ed file.txt
# git add file.txt
# git commit -m "ws3 |  124567"
darcs record -am  "ws3 |  124567"
cd ..



cd ws1
darcs pull ../ws2
darcs pull ../ws3
cd ..
