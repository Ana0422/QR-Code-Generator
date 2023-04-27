import qrcode as qr
img= qr.make("https://paytm.com/")
img.save("upi_paytm.png")
