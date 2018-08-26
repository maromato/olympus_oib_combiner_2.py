# 2011-10-18 Albert Cardona for Nuno da Costa
# Choose a multi-slice image stack file in a virtual way
# and save each slice as an individual image file
# in a user-chosen directory.
import os
import re
import time
import pickle
from ij.gui import GenericDialog
from ij.io import DirectoryChooser, FileSaver,OpenDialog
from ij import IJ, ImagePlus
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
  targetDir = DirectoryChooser("Choose target directory").getDirectory()
  if targetDir is None:
    # User canceled the dialog
    return
  # Ready:
  cs = ChannelSeparator()
  cs.setId(path)
  print "cs" ,cs
  bf = BFVirtualStack(path, cs, False, False, False)
  for sliceIndex in xrange(1, bf.getSize() +1):
    print "Processing slice", sliceIndex
    ip = bf.getProcessor(sliceIndex)
    sliceFileName = os.path.join(targetDir, str(sliceIndex) + ".tif")
    FileSaver(ImagePlus(str(sliceIndex), ip)).saveAsTiff(sliceFileName)
 
run()
