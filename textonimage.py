from nider.core import Font
from nider.core import Outline

from nider.models import Header,Paragraph,Linkback,Content,Image

from PIL import ImageEnhance
from PIL import ImageFilter
from tkinter.filedialog import askopenfilename
import sys,os
#img root folder
IMG='images/'
#fonts root folder
FONTS='/home/kimaru/.local/share/fonts/'
#resultant image location after combining text and image
TOI='textOnImage/'
# read data from file...data will be separated by \n
# on each line, text will be separated from image by # format is text#image
# on each text, the format will be author*heading*content
# program loops according to number of lines in text file.
# font can be chosen by user
raw_data=open('text_image_pair.txt','r').read()
ti_pair=raw_data.split('\n')
if raw_data==None:
    print('Source file is empty\n populate text_image_pair.txt')
    sys.exit(-1)
checker=1
for ti_item in ti_pair:
    ti=ti_item.split('#') # get text and image name seperately
    text=ti[0].split('*') # get author, header and content
    author=text[0]
    head=text[1]
    body=text[2]
    checker=2
    print('Chose header font')
    header_font=askopenfilename() # selected font
    header_font=header_font.split('/')
    header_font=header_font[-1]
    print('Selected header font'+str(header_font))
    print('Chose content font')
    content_font=askopenfilename() # selected font
    content_font=content_font.split('/')
    content_font=content_font[-1]
    print( 'Selected content font'+str(content_font))
    outline = Outline(2, '#121212')

    header = Header(text=head,
                    font=Font(FONTS + header_font, 60),
                    text_width=40,
                    align='left',
                    color='#ededed',
                    outline=outline
                    )

    para = Paragraph(text=body,
                     font=Font(FONTS + content_font, 48),
                     text_width=65,
                     align='left',
                     color='#ededed',
                     outline=outline
                     )

    linkback = Linkback(text='myQuoteSite.com |'+author,
                        font=Font(FONTS + header_font, 18),
                        color='#ededed',
                        outline=outline
                        )

    content = Content(para, header, linkback)

    img = Image(content,
                fullpath=TOI+'resultant_'+ti[1],
                width=1024,
                height=640
                )

    choice=input('Do you wish to blur background image? y/n \n')
    if choice=='y':

        img.draw_on_image(IMG+ti[1],
                          image_enhancements=((ImageEnhance.Contrast, 0.75),
                                              (ImageEnhance.Brightness, 0.5)),
                          image_filters=((ImageFilter.BLUR),)
                          )
    else:
        img.draw_on_image(IMG + ti[1],
                          image_enhancements=((ImageEnhance.Contrast, 0.75),
                                              (ImageEnhance.Brightness, 0.5))
                          )

if checker!=1:
    print('Task completed \n Check '+str(TOI)+ 'folder for results')