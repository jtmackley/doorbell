import datetime
import os
ignore_camera=False
try:
    import picamera
except ImportError:
    print "Requires python-picamera"
    ignore_camera=True
    
def takepicture(cfg):

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
	filepath=cfg["local_file_path"]
	if filepath[-1]!="/":
		# Add / if missing
		filepath=cfg["local_file_path"] + "/"
	if not ignore_camera:
		# Using the camera object
		camera = picamera.PiCamera()
		# Capture a pic
		camera.capture(filepath + filename)
	else:
		os.system("touch " + filepath + filename + " &")
	# return the filename
	return filename