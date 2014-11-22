#-*-coding:utf8-*-
import socket
from xml.dom.minidom import parseString

def seg(input):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('140.109.19.104',1501))
    s.send(('<?xml version="1.0" ?><wordsegmentation version="0.1"><option showcategory="1" /><authentication username="corpustag" password="ntucorpus" /><text>'+input.decode('utf-8').encode('cp950')+'</text></wordsegmentation>'))
    xml=s.recv(2048).decode('cp950').encode('utf-8')
    s.close()
    result=parseString(xml).getElementsByTagName('sentence')[0].childNodes[0].data.encode('utf-8')
    return [word_tag.split('(')[0] for word_tag in result.split('　')][1:]