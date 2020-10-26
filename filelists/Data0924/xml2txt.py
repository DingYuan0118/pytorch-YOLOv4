import os
import sys
import xml.etree.ElementTree as ET
import glob

image_class_dict = {
    "background":'0',
    "tar":'1'
}

def xml_to_txt(indir,outdir):

    os.chdir(indir)
    annotations = os.listdir('.')
    annotations = glob.glob(str(annotations)+'*.xml')

    for i, file in enumerate(annotations):

        file_save = file.split('.')[0]+'.txt'
        file_txt=os.path.join(outdir,file_save)
        f_w = open(file_txt,'w')

        # actual parsing
        in_file = open(file, encoding = 'utf-8')
        tree=ET.parse(in_file)
        root = tree.getroot()

        for obj in root.iter('object'):
                current = list()
                name = obj.find('name').text

                xmlbox = obj.find('bndbox')
                xn = xmlbox.find('xmin').text
                xx = xmlbox.find('xmax').text
                yn = xmlbox.find('ymin').text
                yx = xmlbox.find('ymax').text
                #print xn
                f_w.write(xn+','+yn+','+xx+','+yx+',')
                f_w.write(image_class_dict[name] +'\n')

indir='./xml'   #xml目录
outdir='../txt'  #txt目录

xml_to_txt(indir,outdir)