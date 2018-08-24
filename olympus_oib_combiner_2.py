import os
import re
import time
import pickle
from ij.gui import GenericDialog
from ij.io import DirectoryChooser, FileSaver
from ij import IJ, ImagePlus
from java.lang import Runtime, Runnable


def loadStacks():
 
  
  IJ.log(" "); 
  IJ.log("oib concatenator v0.5; 2012; tischer@embl.de; almf@embl.de"); 
  IJ.log("tested with: ImageJ 1.47a; FIJI update on July 20th 2012"); 
   
  srcDir = DirectoryChooser("Choose directory").getDirectory()
  if not srcDir:
    return
  
  sId = ".oib"
  
  #stackType = getChoice("", ["normal stack", "virtual stack"])
  stackType = "normal stack"  # Concatenate seems not to work with virtual 
  #filepath = srcDir +"tiff"
  #print(filepath) 	
  iStack = 0
  for root, directories, filenames in os.walk(srcDir):
    for filename in filenames:
      path = os.path.join(root,filename)
      if not (sId in filename):
        continue

      IJ.log("opening "+filename)
      
      if stackType == "virtual stack":
        IJ.run("Bio-Formats Importer", "open="+path+" color_mode=Default view=[Standard ImageJ] stack_order=Default use_virtual_stack");
      else:
        IJ.run("Bio-Formats Importer", "open="+path+" color_mode=Default view=[Standard ImageJ] stack_order=Default"); 
    
      # first stack 
      if iStack == 0:
        imp = IJ.getImage()
        imp.setTitle(filename+".tiff")  # in order of the combining to work additive
        nSlices = imp.getNSlices()
        nChannels = imp.getNChannels()
        nTimeFrames = imp.getNFrames() 
        #IJ.run("Stack to Hyperstack...", "order=xyczt(default) channels="+str(nChannels)+" slices="+str(nSlices)+" frames="+str(nTimeFrames)+" display=Color");
        #IJ.log("convert back to normal stack: Image...Hyperstacks...Hyperstack to Stack")
        fs=FileSaver(imp)
        fs.saveAsTiff(srcDir+filename+".tiff")
      else:	
        imp = IJ.getImage()
        imp.setTitle(filename+".tiff")  # in order of the combining to work additive
        #IJ.run(imp,"Concatenate...", "image1=stack image2=st2 title=[stack]");
        #IJ.run("Stack to Hyperstack...", "order=xyczt(default) channels="+str(nChannels)+" slices="+str(nSlices)+" frames="+str(nTimeFrames)+" display=Color");
        #IJ.log("convert back to normal stack: Image...Hyperstacks...Hyperstack to Stack")
        fs=FileSaver(imp)
        fs.saveAsTiff(srcDir+filename+".tiff")
      iStack = iStack + 1
      print(iStack)
 
      
    IJ.log("nChannels = "+str(nChannels))
    IJ.log("nSlices = "+str(nSlices))
    IJ.log("nFrames = "+str(nTimeFrames*iStack))
    #IJ.run("Stack to Hyperstack...", "order=xyczt(default) channels="+str(nChannels)+" slices="+str(nSlices)+" frames="+str(nTimeFrames)+" display=Color");
    IJ.log("convert back to normal stack: Image...Hyperstacks...Hyperstack to Stack")
    IJ.log("if you got an error message from the hyperstack you probably ran out of memory and it did not load all files!")
    
def run():
  loadStacks()
    
run()
