import xlrd
import csv
import sys
import os
from os import sys
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


#========================================================================
# excelToCsv is the function to convert to execel to csv file
#========================================================================
def excelToCsv(excel_file):

    wb = xlrd.open_workbook(excel_file)
    sh = wb.sheet_by_index(0)
    your_csv_file = open('your_csv_file.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
         wr.writerow(
             list(x.encode('utf-8').strip() if type(x) == type(u'') else x
                  for x in sh.row_values(rownum)))

#========================================================================
# read_csv uses the converted file to read company details and emails
#========================================================================
def read_csv():
        f = open("your_csv_file.csv")

        count = 0
        for row in csv.reader(f):
                #Condition to ignore first row
                if count != 0:
#                print row
                 row = filter(None, row)
                 rowlength = len(row)
                 send_mail(row[0], row[1:rowlength])
#                print len(row)
                count = count+1

#========================================================================
# send_mail sends emails to the company with attachment from the
# reports directrory
#========================================================================
def send_mail(company, listofmails):

 from_email = "do-not-reply@example.com"
 to_emails = listofmails
 cc_emails = ["email-sender@example.com"]
 fileToSend = "./reports/"+company + "-Report.xls"
 username = "username"
 password = "password"

 msg = MIMEMultipart()
 msg["From"] = from_email
 msg["To"] = ",".join(to_emails)
 msg["cc"] = ",".join(cc_emails)
 emails = to_emails + cc_emails
 msg["Subject"] = 'Monthly Usage Reports'
 message = 'Message to the customer'

 msg.attach(MIMEText(message))
 attachment = MIMEBase('application', 'octet-stream')

 try:
    with open (fileToSend, "rb") as fp:
        attachment.set_payload(fp.read())
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=company+"-Report.xls")
        msg.attach(attachment)
        fp.close()
 except IOError:
        msg = "Error opening attachment file %s" % fileToSend
        print msg
        sys.exit(1)

 server = smtplib.SMTP('example.jangosmtp.net',25)
 server.ehlo()
 server.ehlo()
 server.login(username,password)
 server.sendmail(from_email, emails, msg.as_string())
 server.quit()


#========================================================================
if __name__ == "__main__":
    excelToCsv(sys.argv[1])
    read_csv()
    os.remove("your_csv_file.csv")
    quit()
