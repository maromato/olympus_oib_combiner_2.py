import os
import re
import time
import pickle
from ij.gui import GenericDialog
from ij.io import DirectoryChooser, FileSaver, OpenDialog
from ij import IJ, ImagePlus, ImageStack
from java.lang import Runtime, Runnable
from loci.plugins.util import BFVirtualStack
from loci.formats import ChannelSeparator

def extractChannel(imp, nChannel, nFrame):
 #""" Extract a stack for a specific color channel and time frame """
 stack = imp.getImageStack()
 ch = ImageStack(imp.width, imp.height)
 for i in range(1, imp.getNSlices() + 1):
   index = imp.getStackIndex(nChannel, i, nFrame)
   ch.addSlice(str(i), stack.getProcessor(index))
 return ImagePlus("Channel " + str(nChannel), ch)


def loadStacks():
 
  
  IJ.log(" "); 
  IJ.log("oib_tiff_converter_ver1.0; 08/24/2018; maromato2012@gmail.com"); 
  IJ.log("tested with: ImageJ 1.47a; FIJI update on July 20th 2012"); 
   
  srcDir = DirectoryChooser("Choose directory").getDirectory()
  if not srcDir:
    return
  
  targetDir = DirectoryChooser("Choose target directory").getDirectory()
  if targetDir is None:
    # User canceled the dialog
    return
  
  sId = ".tiff"  	
  iStack = 0
  
  for root, directories, filenames in os.walk(srcDir):
    for filename in filenames:
      path = os.path.join(root,filename)
      if not (sId in filename):
        continue

      IJ.log("opening "+filename)
      imp = IJ.openImage(path)
      imp.show()
      nChannels = imp.getNChannels()
      imp = IJ.getImage()
      for j in range(1,nChannels+1):
       imp2=extractChannel(imp, j, 1)
       imp2.show()
       fs=FileSaver(imp2)
       fs.saveAsTiff(os.path.join(targetDir+filename+"_c"+str(j)+".tiff"))
        
      iStack = iStack + 1
      print(iStack)
   
 
  IJ.log("if you got an error message from the hyperstack you probably ran out of memory and it did not load all files!")

loadStacks()
 
