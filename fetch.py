#!/usr/bin/env python
###
#
# fetch is a python script for batch fetching files from direct HTTP/FTP links
# created and maintained by Tuan Anh Tran <me@tuananh.us>
# using axel/wget to recursively download files. You can use wget though
# axel is highly recommended. You can install it via homebrew or MacPorts, Fink
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
###

import time, sys
import subprocess
import re
import os

def log(text):
    # print message with local time and date
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print "[%s] - %s" % (date, text)

# too few argvs
if (len(sys.argv)) < 2:
    print "Too few arguments. Type --help or -h for more info."
    exit()

# process argvs

# --help
if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print "fetch links.txt"
    print "     Download list of files from a file\n"
    
    print "fetch http://mydomain.com/myfile.zip"
    print "     Download one/several links\n"
    exit()

# initialize
isImportingFromFile = False
urls = []

# TODO: implement download a single/several links later

if os.path.exists(sys.argv[1]): # if from file
    isImportingFromFile = True
    myFile = sys.argv[1]
    log("Importing links from file %s" % myFile)
    print "\n"
    fileReader = file(myFile,"r")
    urls = fileReader.readlines()
    fileReader.close()
    # add links to urls
elif sys.argv[1].startswith("http://"): # if from URL(s)
    # append the URL(s) to urls
    for i in range(1, len(sys.argv)):
        urls.append(sys.argv[i])
else:
    print "%s is not a valid arguments" % sys.argv[1]
    print "please use valid URL(s). A valid URL should start with http:// or ftp://"
    print "if this is a file, please ensure that file exists"
    exit()

# download the files
current = urls
errors = ""
for url in urls:
    try:
        print url
            
        #using axel with alternative progress bar indicator
        process = subprocess.Popen(["axel", "-a", url])
        # using wget as alternative
        # process = subprocess.Popen(["wget", url])
        process.wait()
            
        # updating list of files
        if isImportingFromFile:
            current = current[1:]
            fileWriter = file(myFile, "w")
            fileWriter.writelines([errors] + current)
            fileWriter.close()
            log("list updated")
            
        print "\n\n"
        
    except KeyboardInterrupt:
        print "\n Bye"
        exit()
    except ValueError:
        log("ERR: This doesn't look like an URL. Unable to download.")
    except:
        log("ERR: Unexpected error.")
        raise
if errors:
    # print out error message here
    log("ERR: Unable to download the file(s).")

log("Finished.")

# def isValidLink(url):
#     return  (url.startswith("http://") or
#              url.startwith("ftp://"))