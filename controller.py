import subprocess
import os 

from pathlib import Path


# input txt 
input_txt =Path('input.txt').read_text(encoding="UTF-8")

# pass to crawler
output = open("./crawler/build/test.txt", "w")
output.write(input_txt)

#crawler 
print ("Working on some crawling ...")
command = "./crawler/build/main"
process = subprocess.Popen(command.split(),stdout=subprocess.PIPE)
process.wait()
print("Crawler is now done!!")

#now Translate

#first input file 
print ("Working on some translation ...")
command = "python3 ./vie-eng-Translate/vi2en.py -filename input" 
print ("executing: "+command)
process = subprocess.Popen(command.split(),stdout=subprocess.PIPE)
process.wait()

for i in range(10):
     command = "python3 ./vie-eng-Translate/vi2en.py -filename id_"+ str(i+1)  
     print ("executing: "+command)
     process = subprocess.Popen(command.split(),stdout=subprocess.PIPE)
     process.wait()

print ("translation is now done ...")

# manipulate and extraction 
print("Enter graph extraction and manipulation")
command = "python3 Text-to-entities/rebel.py -filename input_tl.txt"
process = subprocess.Popen(command.split(),stdout=subprocess.PIPE)
process.wait()
print ("graph extraction and manipulation is now done ...")


relation_txt = Path('relations-output.txt').read_text(encoding="UTF-8")
test_unseen = open("./plms-graph2text/webnlg/data/webnlg/test_unseen.source", "w")
test_unseen.write(relation_txt)
test_unseen.close()

print("Enter  Graph to text phrase")
os.chdir ("/home/thesunsavior/preprocess/Vietnamese-Fake-News-Generation/plms-graph2text")
command = "./decode_WEBNLG.sh t5-base webnlg-t5-base.ckpt 0"
process = subprocess.Popen(command.split(),stdout=subprocess.PIPE)
process.wait()
print ("Graph to text phrase is now done ...")

print("Enter final state")
os.chdir("/home/thesunsavior/preprocess/Vietnamese-Fake-News-Generation/")
relation_result = Path('/home/thesunsavior/preprocess/Vietnamese-Fake-News-Generation/plms-graph2text/webnlg/outputs/test_model/val_outputs/test_unseen_predictions.txt.debug').read_text(encoding="UTF-8")
eng_input = open("./en_input.txt", "w")
eng_input.write(relation_result)
eng_input.close ()

command = "python3 ./vie-eng-Translate/en2vi.py" 
process = subprocess.Popen(command.split(),stdout=subprocess.PIPE)
process.wait()

print ("Final state is now done !!!")
