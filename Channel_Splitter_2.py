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

def run():
  # Choose a file to open
  od = OpenDialog("Choose multi-image file", None)
  srcDir = od.getDirectory()
  if srcDir is None:
    # User canceled the dialog
    return
  path = os.path.join(srcDir, od.getFileName())
  # Choose a directory to store each slice as a file
  #targetDir = DirectoryChooser("Choose target directory").getDirectory()
  #if targetDir is None:
    # User canceled the dialog
    #return
  # Ready:
  print path
  
  imp = IJ.openImage(path)
  imp.show()
  nSlices = imp.getNSlices()
  nChannels = imp.getNChannels()
  nTimeFrames = imp.getNFrames()
  imp = IJ.getImage()
  extractChannel(imp, 1, 1).show()
  
  stack = imp.getImageStack()
  ch = ImageStack(imp.width, imp.height)
  
  
  for i in range(1, imp.getNSlices() + 1):
   index = imp.getStackIndex(nChannels, i, nTimeFrames)
   ch.addSlice(str(i), stack.getProcessor(index))
   return ImagePlus("Channel " + str(nChannels), ch)
 
  print "nSlices :", nSlices, "nChannels :",  nChannels, "nTimeFrames :", nTimeFrames
  imp = IJ.getImage()
  extractChannel(imp, 1, 1).show()

run()
