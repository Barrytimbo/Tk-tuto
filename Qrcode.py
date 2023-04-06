import pyqrcode

url = "creation de qrcode"
img = pyqrcode.create(url)
img.png("qrcode",scale=100)