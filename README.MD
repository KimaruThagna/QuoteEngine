To use the application, you must first populate text_image_pair.txt with data in the followning
format STRICTLY
author*header*content message*#imagename.jpg
this gives the author of the quote, heading and content of message and lastly, name of image
you want to use
The program runs in a loop depending on how many lines youll have in the file
at every individual run, you will be prompted for a header and footer font and whether you will
want to blur the background image or not.
To use the font, install them first on local machine and change the path in FONTS variable to
point to appropriate path where your fonts are installed.
Required libraries is nider and PIL
Ive given some sample data with 5 lines and 5 images