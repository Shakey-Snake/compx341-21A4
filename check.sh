echo $(python3 StaticCheck.py)
if [ $(python3 StaticCheck.py) = 0 ] 
then
    echo 'name and id not present'
    exit 1
fi
echo 'name check passed'
exit 0