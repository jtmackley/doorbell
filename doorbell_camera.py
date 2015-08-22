import datetime
import os
    
def takepicture(cfg):
	ignore_camera=cfg["app_debug"]
	print "Taking picture..."
	# Build a filename from the timestamp
	d = datetime.datetime.now()
	imgYear = "%04d" % (d.year)
	imgMonth = "%02d" % (d.month)
	imgDate = "%02d" % (d.day)
	imgHour = "%02d" % (d.hour)
	imgMins = "%02d" % (d.minute)
	imgSecs = "%02d" % (d.second)
	filename = "doorbell_" +str(imgYear) + str(imgMonth) + str(imgDate) + str(imgHour) + str(imgMins)  + str(imgSecs) + ".jpg"
	# test the last char of path 
	if not ignore_camera:
		try:
			os.system("raspistill -t 1 -n -w 640 -h 320 -o " + cfg["camera_local_file_path"] + filename)
		except:
			print "There was a problem grabbing the image."
			filename=""
	else:
		os.system("touch " + cfg["camera_local_file_path"] + filename + " &")
	# return the filename
	return filename