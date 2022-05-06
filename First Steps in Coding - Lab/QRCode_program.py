Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcod


address = 'https://www.mobile.bg/pcgi/mobile.cgi?act=4&adv=11628238575156057&slink=n7kpmd'
url = pyqrcode.create(address)
url.png('audi.png' , scale=8)
