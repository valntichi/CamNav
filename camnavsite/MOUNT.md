> mount

osxfs on /downloads type fuse.osxfs (rw,nosuid,nodev,relatime,user_id=0,group_id=0,allow_other,max_read=1048576)

- - -- --- -- -- --
| Hello
|
- - - - - - - - - -


umount /mnt/neptune

mount -

psielinou@MtrlOSwarm3:~$ sudo mount -v -t cifs //neptune/legalcollections$/TITANIC/Late\ Stage\ Collections /mnt/neptune -o credentials=/etc/smb_credentials.txt
domain=UNIZA
mount.cifs kernel mount options: ip=10.30.122.151,unc=\\neptune\legalcollections$,user=ABCol_DEV,,domain=UNIZA,prefixpath=TITANIC/Late Stage Collections,pass=********
psielinou@MtrlOSwarm3:~$ sudo mount -v -t cifs //neptune/thunderhead$/AB\ Collections/OUT /mnt/thunderhead -o credentials=/etc/smb_credentials.txt
domain=UNIZA
