import glob
import os 

print('All files in the documents list')

downDir = "Users/alexaj/Downloads"

particleFiles = []
for prtPath in glob.glob(downDir + 'PRT*.pdf'):
  # print prtPath
  filename =  os.path.basename(prtPath)
  # print(filename)
  particleFiles.append(filename)
  
lessonFiles = []
for lsnPath in glob.glob(downDir + '*B_*.pdf'):
  # print lsnPath
  filename = os.path.basename(lsnPath)
  print(filename)
  # lessonFiles.append(filename)

docDir = "Users/alexaj/Documents/"
if not os.path.exists(docDir + "Particles")
  print("creating")
  os.makedirs(docDir + "Partciles")
if not os.path.exists(docDir + "Lessons)
  print("creating")
  os.makedirs(docDir + "Lessons")

parDir = "/Users/alexaj/Documents/Particles/"
lsnDir = "/Users/alexaj/Docuemnts/Lessons/"

if os.listdir(parDir) == []
  for particleFile in particleFiles:
    os.rename(downDir + particleFile, parDir + particleFile)
else:
  for particleFile in particleFiles:
    if not os.path.exists(parDir + particleFile):
      os.rename(downDir + particleFile, parDir + particleFile)
      particleFiles.remove(particleFile)
    else:
      lessonFiles.remove(lessonFile)

if os.listdir(lsnDir) == []
  for lessonFile in lessonFiles:
    os.rename(downDir + lessonFile, lsnDir + lessonFile) 
else:
  for lessonFile in lessonFiles:
    if not os.path.exists(lsnDir + lessonFile):
      os.rename(downDir + lessonFile, lsnDir + lessonFile)
      lessonFiles.remove(lessonFile)
    else:
      lessonFiles.remove(lessonFile)
