import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
import glob
import os


pp = PdfPages('SkyImages.pdf')
mask_sum = np.zeros((720, 1280))
count = 0
for image_file in glob.glob(os.path.join(sys.argv[1], '*.jpg')):
	fig = plt.figure()
	img = cv2.imread(image_file)

	img_display = plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
	pp.savefig(fig)
	fig.clear()
	#plt.show(img_display)

	#color = ('g','b','r')
	#for i,col in enumerate(color):
	#    histr = cv2.calcHist([img],[i],None,[256],[0,256])
	#    plt.plot(histr,color = col)
	#    plt.xlim([0,256])
	#plt.show()

	blue_red_ratio = img[:,:,0]/img[:,:,1].astype('float')
	fig = plt.figure()
	ratio_display = plt.imshow(blue_red_ratio)
	pp.savefig(fig)
	fig.clear()
	#ratio_display.set_cmap('hot')  
	#plt.colorbar()
	#plt.show(ratio_display)

	mask_indices = np.where((blue_red_ratio>1.0) & (blue_red_ratio<1.2))
	mask = np.zeros_like(blue_red_ratio)
	mask[mask_indices] = 1
	mask_sum = mask_sum+mask
	fig = plt.figure()
	mask_dis = plt.imshow(mask)
	mask_dis.set_cmap('hot')  
	pp.savefig(fig)
	fig.clear()
	count+=1
	#plt.colorbar()
	#plt.show(mask_dis)

	#value_array = np.where((img[:,:,1]>215))
	#mask = np.zeros_like(img[:,:,0])
	#mask[value_array] = 1
	#value_array_display = plt.imshow(mask)
	#value_array_display.set_cmap('hot')  
	#plt.colorbar()
	#plt.show(value_array_display)

#fig.savefig('SkyImages.pdf', bbox_inches='tight')
pp.close()
plt.close()
mask_avg = mask_sum/count
mask_dis = plt.imshow(mask_avg)
mask_dis.set_cmap('hot') 
plt.show(mask_dis)
