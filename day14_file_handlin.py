#file creation
'''a=open("C:\\Users\\Live wire\\Desktop\\file2.pdf",'x')
print("file created successfully")'''

'''with open("C:\\Users\\Live wire\\Downloads\\Python Programming_Livewire Course_questions_9_6_2026_12_30_00_PM.pdf", "r", encoding="utf-8",errors="ignore") as p:
    print(p.read())'''
from pypdf import PdfReader

# Open the file in binary mode ("rb")
with open(, "rb") as p:
    reader = PdfReader(p)
    
    # Loop through and read text from all pages
    for page in reader.pages:
        print(page.extract_text())


'''
#file data insert
a=open("C:\\Users\\Live wire\\Desktop\\file2.txt",'w')
a.write("lets go for writing mode")
a.close()
print("done")


#appending
a=open("C:\\Users\\Live wire\\Desktop\\file2.txt",'a')
a.write("lets go for writing mode")
a.close()


b=open("C:\\Users\\Live wire\\Desktop\\tk.txt",'r')
#print(b.read())
print(b.readline(5))

import os
os.remove("C:\\Users\\Live wire\\Desktop\\file2.txt")
print("deleted")
'''
