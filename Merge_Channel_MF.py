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

  IJ.log("Channel_Splitter_ver1.0; 08/24/2018; maromato2012@gmail.com"); 

  IJ.log("tested with: ImageJ2 with jython-shaded-2.5.3.jar, Fiji updated 8/24/2018"); 

   

  srcDir = DirectoryChooser("Choose directory").getDirectory()

  if srcDir is None:

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


      imp.setTitle("st"+str(iStack))  # in order of the combining to work additive

      print filename, str(iStack)

      iStack +=1
      if (iStack)%4 == 0:
        imp2=IJ.run("Merge Channels...", "c1=st1 c2=st2 c3=st3 c4=st0  create composite");
        IJ.save(imp2,os.path.join(targetDir,filename+"_merge"))
        iStack=0
      

         

def run():

  loadStacks()

run()

    

