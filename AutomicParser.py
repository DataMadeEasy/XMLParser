import xml.etree.ElementTree as ET
import os


fileFolderStructure = open('M:\\temp\FolderStruct.txt', 'w')
fileJobs = open('M:\\temp\Jobs.txt', 'w')



def ParseAutomic(xmlfile):
    print('**********************************START*************************************')
    
    #load tree into variable
    tree = ET.parse(xmlfile)

    root = tree.getroot()

    fileFolderStructure.write('Child|Parent|Type')
    fileJobs.write('Name|Script')

    for child in root:
        childElement = child.tag
        #print('ParseAutomic :' + childElement)


        if (childElement == 'FolderStruct'):
            Parse_FolderStruct(child)
        elif (childElement== 'JOBS_WINDOWS'):
            Parse_JOBS_WINDOWS(child)
        else:
            print('not found')



    




def Parse_FolderStruct(xmlbranch):
    
    for item in xmlbranch:
        print ('In Parse Folder Struct: ' + item.tag )
        if (item.tag == 'FOLD'):
            fileFolderStructure.write('\n'+item.attrib['name']+'|root|' + item.tag)
            print ('In Parse Folder Struct:' + item.tag + item.attrib['name'])
            Parse_FOLD(item)
        else:
            print ('not a folder')


def Parse_FOLD(xmlbranch):
    print('Parse_Folder')

    for item in xmlbranch:
        print ('In Parse Folder : ' + item.tag)
        if (item.tag == 'FOLD'):
            fileFolderStructure.write('\n'+item.attrib['name']+'|' + xmlbranch.attrib['name'] + '|' + item.tag)
            Parse_FOLD(item)
        elif (item.tag == 'JOBS_WINDOWS'):
            fileFolderStructure.write('\n'+item.attrib['name']+'|' + xmlbranch.attrib['name'] + '|' + item.tag)
        elif (item.tag == 'JOBS_CIT'):
            fileFolderStructure.write('\n'+item.attrib['name']+'|' + xmlbranch.attrib['name'] + '|' + item.tag)
        elif (item.tag == 'JOBP'):
            fileFolderStructure.write('\n'+item.attrib['name']+'|' + xmlbranch.attrib['name'] + '|' + item.tag)
        elif (item.tag == 'JOBF_WINDOWS'):
            fileFolderStructure.write('\n'+item.attrib['name']+'|' + xmlbranch.attrib['name'] + '|' + item.tag)        
        elif (item.tag == 'EVENT'):
            fileFolderStructure.write('\n'+item.attrib['name']+'|' + xmlbranch.attrib['name'] + '|' + item.tag)        
        else:
            print('parse whats left')


def Parse_JOBS_WINDOWS(xmlbranch):
    print('JOBS_WINDOWS')
    for item in xmlbranch:
        fileJobs.write('\n'+xmlbranch.tag+'|' + item.tag)
    





ParseAutomic('Automic_DRM.xml')


