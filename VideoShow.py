from threading import Thread
import cv2
import os

class VideoShow:
	"""
	Class that continuously shows a frame using a dedicated thread.
	"""
	
	def __init__(self, frame=None, name="video",dataset_folder="dataset"):
		self.frame = frame
		self.name = name
		self.stopped = False
		self.dataset_folder = dataset_folder
		self.snap = False
		
		files = [img for img in os.listdir(self.dataset_folder+"/"+name) if img.endswith(".jpg")]
		if len(files) == 0: files = "000"
		self.count = int(files[-1][:3])+1

	def start(self):
		Thread(target=self.show, args=()).start()
		return self

	global posX; posX = 0
	
	def show(self,width=380,height=240):
		global posX
		
		cv2.namedWindow(self.name,cv2.WINDOW_NORMAL)
		cv2.resizeWindow(self.name,width,height)
		cv2.moveWindow(self.name,(width+30)*posX+60,50)
		
		cv2.namedWindow(self.name+" - frame",cv2.WINDOW_NORMAL)
		cv2.resizeWindow(self.name+" - frame",width,height)
		cv2.moveWindow(self.name+" - frame",(width+30)*posX+60,height+100)
		
		posX += 1

		while not self.stopped:
			cv2.imshow(self.name, self.frame)
			
			key = cv2.waitKey(1)
			if key == ord("q"):
				self.stopped = True
			elif key==13: # enter
				self.snap = True
				print("taked")

	def safe_snap(self):
		index = str(int(self.count)).zfill(4)
		cv2.imwrite(self.dataset_folder+"/"+self.name+"/"+index+".jpg",self.frame)
		cv2.imshow(self.name+" - frame",self.frame)
		
		# You can add a save file log of every snap here
		
		self.count += 1
		self.snap = False
				
	def stop(self):
		self.stopped = True
