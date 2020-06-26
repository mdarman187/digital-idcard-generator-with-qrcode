from PIL import Image, ImageDraw,ImageFont
import qrcode
from pymongo import *
import os

image = Image.new('RGB', (500,300), (255, 255, 255))
d= ImageDraw.Draw(image)
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', 15)
font1 = ImageFont.truetype('Roboto-Bold.ttf', 25)
q='UGC Autonomous College | Accreditation by NAAC (Grade A)'
w='12 K.M. Stone,Amritsar-jalandhar G.T. Road,Amritsar'
r='Tel:0183-5069530,5069532,5069534'
a=input('\nEnter Name: ')
font2= ImageFont.truetype("arial.ttf", 10)

#a='Md Arman'
d.text((83, 35), q, fill=color,font=font2)
d.text((83, 45), w, fill=color,font=font2)
d.text((120, 55), r, fill=color,font=font2)
d.text((110, 90), a, fill=color,font=font1)


g=input('\nEnter Father Name:')
d.text((19, 130), 'F_Name    '+str(g), fill=color,font=font)


g=input('\nEnter Roll number:')

d.text((19, 150), 'Roll No    '+str(g), fill=color,font=font)

b=input('\nEnter age: ')

d.text((19, 170), 'Age         '+str(b), fill=color,font=font)

c=input('\nEnter DOB:')
#c='18/07/1998'
d.text((19, 190), 'DOB        '+c, fill=color,font=font)

g=input('\nEnter Mob No:')
#g='8539856333'
d.text((19, 210), 'Mobile      '+g, fill=color,font=font)

f=input('\nEnter Gmail:')
#f='muhammadarman187@gmail.com'
d.text((19, 230), 'Gmail       '+f, fill=color,font=font)

e=input('\nEnter Address:')
#e='kurji'
d.text((19, 250), 'Address   '+e, fill=color,font=font)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
qr.make(fit=True)
img = qr.make_image()
qr.add_data('a')


img1=Image.open('0.png')
img2 = img1.resize((70,70), Image.ANTIALIAS)
d.text((80, 10), 'AMRITSAR GROUP OF COLLEGES', fill='blue',font=font1)
img3=Image.open('IMG_20190301_192221_517.jpg')

img4 = img3.resize((105,105), Image.ANTIALIAS)

#img = qrcode.make(str(a) + str(g))
image.paste(img2, (10, 10))
image.paste(img, (350, 163))
image.paste(img4, (369, 70))


#image.paste(img1, (300, 50))
image.save(str(a) + '.png')

image.show()

#connection=MongoClient("mongodb+srv://*************.mongodb.net/test?retryWrites=true")
#db = connection.test()
