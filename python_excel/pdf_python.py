from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import re


# Successfully installed pdfminer3k-1.3.4 ply-3.11


def read_from_pdf(file_path):
    """
    读取pdf文件
    """
    try:
        with open(file_path, 'rb') as file:
            resource_manager = PDFResourceManager()
            return_str = StringIO()
            lap_params = LAParams()
            device = TextConverter(resource_manager, return_str, laparams=lap_params)
            process_pdf(resource_manager, device, file)
            device.close()
            content = return_str.getvalue()
            return_str.close()
            return re.sub(r'\s+', ' ', content)
    except Exception as e:
        return '123'


content = read_from_pdf('知了课堂爬虫VIP课件.pdf')
print(content)
