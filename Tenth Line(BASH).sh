count=0
while read 
do
    count=$((count+1))
    if [[ $count -eq 10 ]]
    then
        echo $REPLY
        break
    fi
done<file.txt
