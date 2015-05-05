import ftplib

def upload(cfg,img):
	session = ftplib.FTP(cfg["ftp_server"],cfg["ftp_user"],cfg["ftp_password"])
	filepath=cfg["local_file_path"]	
	if filepath[-1]!="/":							# Add / if missing
		filepath=cfg["local_file_path"] + "/"

	print "FTP Uploading: " + filepath + img + " to " + cfg["ftp_remote_path"]
	session.cwd(cfg["ftp_remote_path"])
	file = open(filepath + img,'rb')                # file to send
	session.storbinary("STOR " + img, file)     				# send the file
	file.close()                                    # close file and FTP
	session.quit()