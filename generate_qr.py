import qrcode
data= "https://www.linkedin.com/in/debojyoti-chakraborty-057209274/"

#creating qr code
qr=qrcode.QRCode(version=1, box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)

#creating image
image=qr.make_image(fill="black",bg="white")

#image save
image.save("linkedin_qr.png")
image.show()