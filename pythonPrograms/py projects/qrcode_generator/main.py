import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


# to create qrcode
img = qrcode.make('https://codeupon.wordpress.com')
img.save('codeupon.png')


# to read the qrcode
d = decode(Image.open('codeupon.png'))
print(d[0].data.decode('ascii'))