import pyqrcode
from pyqrcode import QRCode
s="Hello world"

url= pyqrcode.create(s)
url.svg("testqrcode.svg",scale=8)

"""other external modules
1. Numpy
2. Pandas
3. 
look up more
"""