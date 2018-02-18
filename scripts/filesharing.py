import os

# for f in os.listdir('smb://Patricks-MacBook-Pro'):
#     print f
folder = '/Users/patricktchankue/mnt/example'
if not os.path.exists(folder):
    os.makedirs(folder)
os.system('mount_smbfs //patricktchankue:@Patricks-MacBook-Pro.local/Books/ /Users/patricktchankue/mnt/example')

"""
smbclient -L //user@host

smbutil view

for f in os.listdir('smb://PMACBOOKPRO-1BA6'):
    print f

osascript -e 'tell application "Finder" to mount volume "smb://patricktchankue:@Patricks-MacBook-Pro.local/Books"'

smb://psielinou:@neptune/legalcollections$/titanic/Late\ Stage\ Collections

"""

os.access('//patricktchankue:@Patricks-MacBook-Pro.local/Books', os.W_OK)