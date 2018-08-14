import glob
import os 

print('All files in the documents list')

particleFiles = []
for prtPath in glob.glob('/Users/alexaj/Documents/PRT*.tiff'):
  # print prtPath
  filename =  os.path.basename(prtPath)
  print(filename)
  # lessonFiles.append(filename)
  

lessonFiles = []
for lsnPath in glob.glob('/Users/alexaj/Documents/*B*.tiff'):
  # print lsnPath
  filename = os.path.basename(lsnPath)
  print(filename)
  # lessonFiles.append(filename)

