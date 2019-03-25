import cv2
import os
from datetime import datetime

sub_folders = ["cam1","cam2","cam3"]
dataset_folder = "dataset"

min = 999
max = 0

for i in range(len(sub_folders)):
	if os.path.exists(dataset_folder+"/"+sub_folders[i]):
		files = [img for img in os.listdir(dataset_folder+"/"+sub_folders[i]) if img.endswith(".jpg")]
		if int(files[0][:3])<min: 
			min = int(files[0][:3])
		if int(files[-1][:3])>max: 
			max = int(files[-1][:3])
  else:
    print("folders no detected")
    exit()
	
  
rango = range(min,max+1)
ind = rango[0]

while ind in rango:
	index = str(ind).zfill(3)
	for i in range(len(sub_folders)):
		file = dataset_folder+"/"+sub_folders[i]+"/"+index+".jpg"
		if os.path.isfile(file):
			img = cv2.imread(file)
			cv2.imshow(sub_folders[i],img)
	
	key = cv2.waitKey()
	#print(key)
	if key == 27 or key == 113:
		break
	elif key == 103: #(g)ood
		pass
	elif key == 98: #(b)ad
		pass
	elif key == 32: #(b)ack
		ind -= 1
	else: #any or enter
		ind += 1
    
	if ind<rango[0]: ind=rango[-1]
	if ind>rango[-1]: ind=rango[0]
