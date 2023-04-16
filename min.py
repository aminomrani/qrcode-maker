import os 
import qrcode 
print('this is only a traning project') ;
print('welcome to Qrcode project !'); 
print('you can send any link for me and i make qrcode for you !!') ;
url = input('send your link : ');


img = qrcode.make(url) ;
img.save('{}.png'.format(url));
filename = '{}.png'.format(url)
if os.path.exists(filename) : 
    os.remove(filename)
    img.save('{}.png'.format(url));