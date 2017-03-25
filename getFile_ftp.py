import gzip
import sys
import ftplib
import os
from ftplib import FTP


def extract_gzip(gzip_file):
        ## Open the gzip file
        a = gzip.open(gzip_file)

        ## Print the content in the file
        mystring = a.read().encode('utf-8')

        ## replace the string pipe with comma
        mystring = mystring.replace(', ', "; ").encode('utf-8')

        mystring = mystring.replace("|", ",").encode('utf-8')

        ## create a csv file
        gzip_file = gzip_file.replace('.dat.gz', "")

        csv_file = open(gzip_file+".csv", "w")

        csv_file.write(mystring)

        csv_file.close()

        ## remove gz file from the system
        os.remove(gzip_file+".dat.gz")

#========================================================================
def grabFTP_file(ftpfile):

        ## ftp details hostname, username, password and current working directory
        ftp = FTP('example.com')
        ftp.login(user='example', passwd='pass123')
        
        ## FTP Path directory
        ftp.cwd('/Daily_Reports/')

        try:
         localfile = open(ftpfile, 'wb')
         ftp.retrbinary('RETR ' + ftpfile, localfile.write, 1024)
         ftp.quit()
         localfile.close()
        except ftplib.all_errors:
         os.remove(ftpfile)
         print "ERROR : File " + ftpfile +" doesn't exists in FTP Server"
         sys.exit()

#========================================================================
if __name__ == "__main__":
        grabFTP_file(sys.argv[1])
        extract_gzip(sys.argv[1])

        print "Done..!"