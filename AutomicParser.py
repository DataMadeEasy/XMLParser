import xml.etree.ElementTree as ET



def ParseAutomic(xmlfile):
    
    #load tree into variable
    tree = ET.parse(xmlfile)

    root = tree.getroot()
    
    
    for item in root:
        print(item)


    print(root)




def ParseFolderStruct(xmlbranch):
    print('ParseFolder')

def ParseFolder(xmlbranch):
    print('ParseFolder')

def ParseJobsWindows(xmlbranch):
    print('ParseJobsWindows')

def ParseJobsUnix(xmlbranch):
    print('ParseJobsWindows')

def ParseJobP(xmlbranch):
    print('ParseJobsWindows')








ParseAutomic('Automic_DRM.xml')


