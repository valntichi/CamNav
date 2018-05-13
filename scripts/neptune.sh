#!/bin/bash

if [ ! -f /etc/smb_credentials.txt ]; then
    echo "File not found!\n>>> Creating smb file"
    echo "username=ABCol_DEV" > randomtext.txt
    echo "password=xxx" >> randomtext.txt
    echo "domain=UNIZA" >> randomtext.txt
fi

#sudo mkdir /mnt/neptune

#sudo mount -v -t cifs //neptune/legalcollections$/TITANIC/Late\ Stage\ Collections /mnt/neptune -o credentials=/etc/smb_credentials.txt