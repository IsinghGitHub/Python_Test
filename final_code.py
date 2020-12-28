import pandas as pd
import xml.etree.ElementTree as ET
import io
import requests
import os, fnmatch
import os, fnmatch
import zipfile
from zipfile import ZipFile

# Checking all the xml files present in teh current dir
def xml_check():

    listOfFiles = os.listdir('.')
    pattern = "sample.xml"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            return entry

def iter_docs(name):
    name_attr = name.attrib
    for doc in name.iter('str'):
        doc_dict = name_attr.copy()
        doc_dict.update(doc.attrib)
        doc_dict['data'] = doc.text
        yield doc_dict
        
etree = ET.parse(xml_check())
doc_df = pd.DataFrame(list(iter_docs(etree.getroot())))
doc_df


url = doc_df.loc[:, "data"][7]
url



r = requests.get(url, allow_redirects=True)
print('Beginning file download with urllib2...')


# Checking all the zip files present in teh current dir
def file_check():

    listOfFiles = os.listdir('.')
    pattern = "*.zip"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            return entry

# Ensuring the zip file is valid


def main():
    try:
        with zipfile.ZipFile(file_check()) as file: # opening the zip file using 'zipfile.ZipFile' class
            print("Ok")
    except zipfile.BadZipFile: # if the zip file has any errors then it prints the error message which you wrote under the 'except' block
        print('Error: Zip file is corrupted')

if __name__ == '__main__': main()

## I used a badfile for the test




with ZipFile(file_check(), 'r') as zf:
       #display the files inside the zip
    zf.printdir()
       #Extracting the files from zip file
       # also generate the desired output name:
    zf.extractall()
    print('Zip Extraction Completed')



# Checking all the xml files present in teh current dir
def new_xml():
    
    listOfFiles = os.listdir('.')
    pattern = "DL*.xml"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            return entry


tree = ET.parse(new_xml())
xroot = tree.getroot()
xroot

for form in xroot.findall(".//"):
    print(form.attrib, form.text)


[elem.tag for elem in xroot.iter()][0:10]

Sorry I could have finished it but I started late. :)