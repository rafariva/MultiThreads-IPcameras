# based on https://github.com/nrsyed/computer-vision/tree/master/multithread

import cv2
import os
from datetime import datetime

from VideoGet import VideoGet
from VideoShow import VideoShow

lst_video_getter = []
lst_video_shower = []

# list the ip cams you want to access, and assign a name for each one
lst_ip_cam = [0, # webcam
	      "http://root:root@192.168.0.10/mjpg/video.mjpg",
	      "rtsp://192.168.0.13:554/ch0"]
lst_cam_name = ["cam1","cam2","cam3"]
dataset_folder = "dataset"

if not os.path.exists(dataset_folder):
	os.makedirs(dataset_folder)
		  
for i in range(len(lst_ip_cam)):
	if not os.path.exists(dataset_folder+"/"+lst_cam_name[i]):
		os.makedirs(dataset_folder+"/"+lst_cam_name[i])
		
	video_getter = VideoGet(lst_ip_cam[i]).start()
	lst_video_getter.append(video_getter)
	lst_video_shower.append(VideoShow(video_getter.frame,lst_cam_name[i]).start())


stop = False
snap = False
while True:
	for i in range(len(lst_video_getter)):
		if lst_video_getter[i].stopped or lst_video_shower[i].stopped:
			lst_video_shower[i].stop()
			lst_video_getter[i].stop()
			
			stop=True
		
		if lst_video_shower[i].snap: 
			snap = True

		frame = lst_video_getter[i].frame
		lst_video_shower[i].frame = frame
	
	if snap: 
		for i in range(len(lst_video_getter)): 
			lst_video_shower[i].safe_snap()
			lst_video_shower[i].snap=False
		snap=False
	
	
	if stop:
		for i in range(len(lst_video_getter)):
			lst_video_shower[i].stop()
			lst_video_getter[i].stop()
			
		break
