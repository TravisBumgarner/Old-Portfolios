# Run from /blog dir

if test -z "$2" 
then
      echo "Making new post" $1

    filename=$(echo "$1" | tr '[:upper:]' '[:lower:]')
    filename=$( echo "$filename" | tr ' ' '-')

    mkdir "./static/image/$filename"
    /opt/homebrew/bin/hugo new "post/$filename.md"
else
      echo "Add quotes around article title"
fi

