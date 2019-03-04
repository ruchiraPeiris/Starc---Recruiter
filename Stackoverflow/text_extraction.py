from PIL import Image
import PIL.Image

# from pytesseract import image_to_string
# import pytesseract
#
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
# TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'
# output = pytesseract.image_to_string(PIL.Image.open('C:/Users/pc/Desktop/images for FYP/job add.png').convert("RGB"), lang='eng')
# print(output)

# text='Ensures that code artifacts produced are of the highest quali, conforming to set or agreed upon standard.'
# text+='Follows the processes, agile practices and motivates his/her team members to do So'
# text+='Escalates and communicates issues, risks and concerns to leads or managers.'
# text+='Provides input on estimates and achieve on-time Delivery,'
# text+='Aligns self to organizational goals.'
# text+='Acoepis project delivery responsibilities and demonstrate accountability to leadership.'
# text+='Maintains a sense of individuality in thinking and decision making'
#
# print(text)

import PIL.Image


def text_extraction(filepath_to_image):
    global TESSDATA_PREFIX, output
    from pytesseract import image_to_string
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
    TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'
    output = pytesseract.image_to_string(PIL.Image.open(filepath_to_image).convert("RGB"), lang='eng')
    print(output)
    return output

# text_extraction()