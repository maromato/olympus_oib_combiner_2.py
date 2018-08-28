import os
import re
import time
import pickle
from ij.gui import GenericDialog
from ij.io import DirectoryChooser, FileSaver
from ij import IJ, ImagePlus
from ij.plugin import ChannelSplitter, StackCombiner
from java.lang import Runtime, Runnable


def loadStacks():
 
  
  IJ.log(" "); 
  IJ.log("oib concatenator v0.5.1; 2012; tischer@embl.de; almf@embl.de; revised by maromato2012@gmail.com"); 
  IJ.log("tested with: ImageJ 1.47a; FIJI update on July 20th 2012"); 
   
  srcDir = DirectoryChooser("Choose directory").getDirectory()
  if not srcDir:
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
      imp.setTitle("st"+str(iStack))  # in order of the combining to work additive
      print filename, str(iStack)
      iStack +=1

    
    imp2=IJ.run("Merge Channels...", "c1=st1 c2=st0 c3=st3 c4=st2  create composite");
    IJ.save(imp2,os.path.join(srcDir,filename+"_merge"))
         
def run():
  loadStacks()
    
run()
