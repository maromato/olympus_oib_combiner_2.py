
# olympus_oib_tiff_converter.py
This python script is to import oib files from a specific folder, make a hyperstacked file with 2 channels (color and z-series), save them as tiff files.

# Channel_Splitter_MF.py
This python script is to import hyperstacked tiff files from a specific folder, split the color channels and save them into a user defined target folder.

# SliceStack_MF.py
This python script is to import multi-slice image stack files(tiff) from a specific folder and save each slice into a user defined target folder.  

# Merge_Channel_MF.py
This python script is to import a series of 4 separeted channle (4 channels) image files(tiff) from specific folders, merged them into composite files and save them to a user defined target folder.

# olympus_oib_combiner_2.py
This is a converter for olympus oib file to tiff file.
This python script is for importing oib files from a specific folder and save them as tiff files.
The tiff file will note be hyperstacked.

This scipt is for a converter for olympus oib file to tiff which was originally developed by EMBL as below.
https://www.embl.de/services/core_facilities/almf/services/downloads/oib-combiner/
A few bugs are fixed and the script is revised for the z-stack oib files from mulitile areas.

![dlaoultx4aevcbz](https://user-images.githubusercontent.com/17135389/44613872-99d62680-a7e8-11e8-9f15-84c870c67abd.jpg)

# Python and ImageJ or Fiji

Unfotunately, the latest Fiji (imageJ) at August, 2018 is still not compatible with jython-shaded-2.7.0.jar, even though the default jars in Fiji.app include this version of jython and python is not working in this setting! 
You probably see the error like "console: Failed to install '': java.nio.charset.UnsupportedCharsetException: cp0", when you try to run any of python code in Fiji.

if so, I would recommend you to change jython! You could download jython-shaded-2.5.3.jar as below.
https://mvnrepository.com/artifact/org.scijava/jython-shaded/2.5.3
It works at least in August, 2018!

You could also find the instruction.
https://stackoverflow.com/questions/49970418/how-can-use-iadf-iavff-1-0-fiji-plugins-java-phyton/51997948#51997948

Please let me know if there is any further question. maromato2012@gmail.com
