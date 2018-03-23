from class_SAM import SAM

file = SAM()
filepath = 'C:\\Users\\hpatterton\\Downloads\\test_sam2.sam'
number = file.ReadSAMFile(filepath)
print(file.entries)
print(file.GetField(0,'QNAME'))
print(file.GetOPTValue(0,'AS'))
print(file.GetCIGARvalues(0))