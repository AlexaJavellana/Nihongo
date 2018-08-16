import glob
import os 

print('All files in the documents list')

downDir = "/Users/AlexaJ/Downloads/"

particleFiles = []
for prtPath in glob.glob(downDir + 'PRT*.pdf'):
  # print prtPath
  filename =  os.path.basename(prtPath)
  # print(filename)
  particleFiles.append(filename)
  

lessonFiles = []
for lsnPath in glob.glob('/Users/AlexaJ/Downloads/*B*.pdf'):
  # print lsnPath
  filename = os.path.basename(lsnPath)
  # print(filename)
  lessonFiles.append(filename)
'''
for particleFile in particleFiles:
  print(particleFile)
'''

docDir = "/Users/AlexaJ/Documents/"
if not os.path.exists(docDir + "Particle_Lessons"):
  print("creating")
  os.makedirs(docDir + "Particle_Lessons")
if not os.path.exists(docDir + "B_Lessons"):
  print("creating")
  os.makedirs(docDir + "B_Lessons")

parDir = "/Users/AlexaJ/Documents/Particle_Lessons/"
lsnDir = "/Users/AlexaJ/Documents/B_Lessons/"

#lessonFiles
#particleFiles

if os.listdir(parDir) == []:
  for particleFile in particleFiles:
    os.rename(downDir + particleFile, parDir + particleFile)
else:
  for particleFile in particleFiles: 
    if not os.path.exists(parDir + particleFile):
      os.rename(downDir + particleFile, parDir + particleFile)
      particleFiles.remove(particleFile)
    else:
      particleFiles.remove(particleFile)

if os.listdir(lsnDir) == []:
  for lessonFile in lessonFiles:
    os.rename(downDir + lessonFile, lsnDir + lessonFile)
else:
  for lessonFile in lessonFiles:
    if not os.path.exists(lsnDir + lessonFile):
      os.rename(downDir + lessonFile, lsnDir + lessonFile)
      lessonFiles.remove(lessonFile)
    else:
      lessonFiles.remove(lessonFile)

