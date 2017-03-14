# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 10:53:31 2017

@author: AB053658
"""

from PIL import Image,ImageDraw,ImageFont

def addnum(image,num):
    draw=ImageDraw.Draw(image,'RGB')
    myfont=ImageFont.truetype('C:/windows/fonts/ITCEDSCR.TTF',size=int(image.size[0]/10))
    fillcolor="#ff0000"
    width,height=image.size
    print(draw.getfont())
    draw.text((width/5,height/5),str(num),font=myfont,fill=fillcolor)
    x,y=image.size
    eX,eY=300,600
    bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
    draw.ellipse(bbox,fill=255,outline=50)
    image.save('result.jpg','jpeg')
    
    return 0

if __name__=='__main__':

  image=Image.open('image.jpg');
  addnum(image,'wangyanwu')
    