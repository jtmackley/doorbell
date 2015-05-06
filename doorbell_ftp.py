import ftplib

def upload(cfg,img):
	session = ftplib.FTP(cfg["ftp_server"],cfg["ftp_user"],cfg["ftp_password"])
	print "FTP Uploading: " + cfg["camera_local_file_path"] + img + " to " + cfg["ftp_remote_path"]
	session.cwd(cfg["ftp_remote_path"])
	file = open(cfg["camera_local_file_path"] + img,'rb')                # file to send
	session.storbinary("STOR " + img, file)     				# send the file
	file.close()                                    # close file and FTP
	session.quit()