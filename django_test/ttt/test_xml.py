import xml.sax
import xml.sax.handler


class XMLHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.buffer = ""
        self.mapping = {}

    def startElement(self, name, attributes):
        self.buffer = ""

    def characters(self, data):
        self.buffer += data

    def endElement(self, name):
        self.mapping[name] = self.buffer

    def getDict(self):
        return self.mapping


data = '<xml><return_code><![CDATA[SUCCESS]]></return_code><return_msg><![CDATA[OK]]></return_msg></xml>'

xh = XMLHandler()
xml.sax.parseString(data, xh)
ret = xh.getDict()
print(type(ret))
print(ret)
print(ret['return_code'])

# 结果
# <class 'dict'>
# {'return_code': 'SUCCESS', 'return_msg': 'OK', 'xml': 'OK'}
# SUCCESS
