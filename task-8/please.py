from PIL import Image #Pillow==6.1.0 
import pytesseract #pytesseract==0.2.7

captcha = pytesseract.image_to_string(Image.open('captcha.png'), config='--psm 7')
print(captcha)
print(eval(captcha))
