from PIL import Image
import pytesseract

def get_captcha_by_ocr(filename='captcha.jpg',threshold=110):
    '''ocr识图'''
    image=Image.open('captcha.jpg')
    #灰度处理
    gray=image.convert("L")
    #gray.show()
    #gray.save("captcha_gray.jpg")


    #二值化处理
    #threshold=110
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)

    ct=gray.point(table,'1')
    #ct.show()
    #ct.save('captcha_threshold.jpg')


    return pytesseract.image_to_string(ct)
