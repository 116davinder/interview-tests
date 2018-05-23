#1/bin/sh

if [ "$#" -eq 0 ];
then
    echo "No Argument passed"
    echo "Usage: "
    echo "./uncompress.sh *               for all types of files"
    echo "./uncompress.sh file6.xz        for specific file only"
    exit 1
fi

if [ "$1" = "*" ];
then
    echo "Unzipping all files"
    find ./ -type f -name '*.gz' ! -name "*.tar.gz" -exec gunzip -k {} \;
    find ./ -type f -name "*.tar.gz" -exec tar xzf {} \;
    find ./ -type f -name '*.bz2' ! -name "*.tar.bz2" -exec bzip2 -d {} \;
    find ./ -type f -name "*.tar.bz2" -exec tar xjf {} \;
    find ./ -type f -name '*.xz' ! -name "*.tar.xz" -exec unxz -k {} \;
    find ./ -type f -name "*.tar.xz" -exec tar -xf {} \;
    find ./ -type f -name '*.rar' -exec unrar e {} \;
    find ./ -type f -name '*.zip' -exec unzip {} \;
    echo "Unzipping Done"
else
    echo "Unzipping only " $1
    file_name=$1
    file_extension="${filename##*.}"
    if [ "$file_extension" = "gz"];
    then
        echo "gz"
        second_extension=$(echo $file_name | cut -d . -f2)
        if [ "$second_extension" = "tar"];
        then
            tar xzf $file_name
        else
            gunzip -k $file_name
    elif [ "$file_extension" = "bz2"];
    then
        echo "bz2"
        second_extension=$(echo $file_name | cut -d . -f2)
        if [ "$second_extension" = "tar"];
        then
            tar xjf $file_name
        else
            bzip2 -d $file_name
    elif [ "$file_extension" = "zip"];
    then
        unzip $file_name
    elif [ "$file_extension" = "rar"];
    then
        unrar -e $file_name
    elif [ "$file_extension" = "xz"];
    then
        second_extension=$(echo $file_name | cut -d . -f2)
        if [ "$second_extension" = "tar"];
        then
            tar -xf $file_name
        else
            unxz -k $file_name
    else
        echo "given file doesn't match any known compression format"
        exit 1
fi