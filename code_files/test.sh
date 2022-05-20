if [[ $(file --mime-type -b "$1") = application/* ]]; then

    # Get the full path, the name and directory name of submited application file.
    myFile=$(realpath "$1")
    echo $myFile
    myBaseName=$(basename "$myFile")
    echo $myBaseName
    myPath=$(dirname "$myFile")
    echo $myPath

    # Function to verify if required program is installed.
    VerInst () {
	if [ $? -eq 127 ]; then
	    echo "$1 package is not installed."
	    echo "Install it before running this script."
	    echo "Aborting."
	    exit 1
	fi
    }

    # Extract icon and convert it to several png files of diferent quality, 
    wrestool -x -t 14 "$myFile" > "/tmp/$myBaseName.ico" 2> /dev/null
    VerInst icoutils
    convert -alpha on "/tmp/$myBaseName.ico" "/tmp/$myBaseName.png" 2> /dev/null
    VerInst imagemagick
    # Select the best png image file.
    cp "$(ls -S -1 "/tmp/$myBaseName"*".png"  | head -n 1)" "$HOME/Games4Linux/code_files/img_icon/$myBaseName.png"
fi
