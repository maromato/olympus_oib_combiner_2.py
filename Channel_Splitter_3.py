import os
import re
import time
import pickle
from ij.gui import GenericDialog
from ij.io import DirectoryChooser, FileSaver, OpenDialog
from ij import IJ, ImagePlus, ImageStack
from java.lang import Runtime, Runnable
import os
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

 
def run():
  # Choose a file to open
  od = OpenDialog("Choose multi-image file", None)
  srcDir = od.getDirectory()
  if srcDir is None:
    # User canceled the dialog
    return
  path = os.path.join(srcDir, od.getFileName())
  filename=od.getFileName()
  # Choose a directory to store each slice as a file
  targetDir = DirectoryChooser("Choose target directory").getDirectory()
  if targetDir is None:
    # User canceled the dialog
    return
    #Ready:#print path
  
  imp = IJ.openImage(path)
  imp.show()
  nChannels = imp.getNChannels()
  imp = IJ.getImage()
  for j in range(1,nChannels+1):
   imp2=extractChannel(imp, j, 1)
   imp2.show()
   
   fs=FileSaver(imp2)
   fs.saveAsTiff(os.path.join(targetDir+filename+"_c"+str(j)+".tiff"))
   
run()
