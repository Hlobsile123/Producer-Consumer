import xml.etree.ElementTree as ET
import random
import re
import socket
import tqdm
import os


data = ET.Element('metadata')
element1 = ET.SubElement(data, 'student')    
ET.indent(data, '  ')

class ITStudent:
    def __init__(self, name, id, program, courses, marks):
        self.name = name
        self.id = id
        self.program = program
        self.courses = courses
        self.marks = marks

    def writeStudent(self):        
        s_elem1 = ET.SubElement(element1, 'name')
        s_elem2 = ET.SubElement(element1, 'id')
        s_elem3 = ET.SubElement(element1, 'program')
        s_elem4 = ET.SubElement(element1, 'courses')
        s_elem5 = ET.SubElement(element1, 'marks')
        
        s_elem1.text = self.name
        s_elem2.text = self.id
        s_elem3.text = self.program
        s_elem4.text = self.courses
        s_elem5.text = self.marks
        
        


marks = [[50, 69], [78, 51], [95, 46], [76, 89], [95, 46], [65, 72], [78, 45]]
names = ["Nombuso Ngwenya", "Nongcebo Mkhonta", "Sive Gulwako", "Mandla Sibiya", "Mfaniseni Nhlabatsi", "Nokuthula Maziya", "Noxolo Siphepho", "Phephile Ndzimandze", "Fezile Phakathi", "Siboniso Dlamini"]
ids = [95494878, 91654645, 96532142, 96924516, 95423164, 95641235, 94613254, 94924613, 93645164, 99461531]
programs = ["Faculty of Management", "Information Technology", "Computer Science", "Faculty of Networking"]
courses = [["Intro to Computers", "Intro To Networking"], ["Information Systems", "Media Management"], ["Languages and Speaking", "Public Speaking"], ["Cyber Security", "The internet of technology"]]

def getRandom(lst):
     return random.choice(lst)

stud = ITStudent(getRandom(names), f'{getRandom(ids)}', getRandom(programs), f'{getRandom(courses)}', f'{getRandom(marks)}')
stud.writeStudent()
#
b_xml = ET.tostring(data, encoding="utf-8", xml_declaration=True)

with open("ITStudent.xml", "wb") as f:
	f.write(b_xml)
        


#Calculations and output
def calculateStudentAverage(marks):
    
    total = (76 +65)   
    
    average = (total / 2)
    return average;





SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step
# the ip address or hostname of the server, the receiver
host = socket.gethostbyname(socket.gethostname())
# the port, let's use 5001
port = 5001
# the name of file we want to send, make sure it exists
filename = "ITStudent.xml"
# get the file size
filesize = os.path.getsize(filename)
# create the client socket
s = socket.socket()
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")
# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())
# start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket
s.close()








print (f'This student average mark is {calculateStudentAverage(marks)}')
print(f'Student courses were {stud.courses}')
print(f'Marks were {stud.marks}')
print(f'Student has passed the exam!')