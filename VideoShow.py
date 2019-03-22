from threading import Thread
import cv2
import os

class VideoShow:
	"""
	Class that continuously shows a frame using a dedicated thread.
	"""
	
	def __init__(self, frame=None, name="video"):
		self.frame = frame
		self.name = name
		self.stopped = False
		self.dataset_folder = "dataset"
		self.snap = False
		
		files = [img for img in os.listdir(self.dataset_folder+"/"+name) if img.endswith(".jpg")]
		if len(files) == 0: files = "000"
		self.count = int(files[-1][:3])+1

	def start(self):
		Thread(target=self.show, args=()).start()
		return self

	def show(self):
		cv2.namedWindow(self.name,cv2.WINDOW_NORMAL)
		cv2.resizeWindow(self.name,320,240)
		#cv2.moveWindow(self.name,x*170,100)
		cv2.namedWindow(self.name+" - frame",cv2.WINDOW_NORMAL)
		cv2.resizeWindow(self.name+" - frame",320,240)
		#cv2.moveWindow(self.name+" - frame",x*170,400)

		while not self.stopped:
			cv2.imshow(self.name, self.frame)
			
			key = cv2.waitKey(1)
			if key == ord("q"):
				self.stopped = True
			elif key==13: # enter
				self.snap = True
				print("taked")

	def safe_snap(self):
		index = str(int(self.count)).zfill(3)
		cv2.imwrite(self.dataset_folder+"/"+self.name+"/"+index+".jpg",self.frame)
		cv2.imshow(self.name+" - frame",self.frame)
		
		self.count += 1
		self.snap = False
				
	def stop(self):
		self.stopped = True
