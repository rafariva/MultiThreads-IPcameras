from threading import Thread
import cv2
import os
from datetime import datetime

class VideoShow:
	"""
	Class that continuously shows a frame using a dedicated thread.
	"""
	
	
	
	def __init__(self, frame=None, name="video"):
		self.frame = frame
		self.name = name
		self.stopped = False
		self.thermal_folder = "dataset"
		self.snap = False
		
		files = [img for img in os.listdir(self.thermal_folder+"/"+name) if img.endswith(".jpg")]
		if len(files) == 0: files = "000"
		self.count = int(files[-1][:3])+1

	def start(self):
		Thread(target=self.show, args=()).start()
		return self

	def show(self):
		x = int(self.name[0])
		if x==6: x=5
		cv2.namedWindow(self.name,cv2.WINDOW_NORMAL)
		cv2.resizeWindow(self.name,320,240)
		cv2.moveWindow(self.name,x*170,100)
		cv2.namedWindow(self.name+" - frame",cv2.WINDOW_NORMAL)
		cv2.resizeWindow(self.name+" - frame",320,240)
		cv2.moveWindow(self.name+" - frame",x*170,400)

		while not self.stopped:
			cv2.imshow(self.name, self.frame)
			
			key = cv2.waitKey(1)
			if key == ord("q"):
				self.stopped = True
			elif key==13: # enter
				self.snap = True

	def safe_snap(self):
		index = str(int(self.count)).zfill(3)
		
		cv2.imwrite(self.thermal_folder+"/"+self.name+"/"+index+".jpg",self.frame)
		self.count += 1
		cv2.imshow(self.name+" - frame",self.frame)
		
		if self.name == "160_domo":
			file = open(self.thermal_folder+"/logs.txt","a")
			dia_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			file.write(dia_hora+";"+index+";\n")
			file.close()
		
			print("taked")
		
		self.snap = False
				
	def stop(self):
		self.stopped = True