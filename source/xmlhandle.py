# -*- coding: utf-8 -*-

from xml.dom import minidom

class Item(object):

    def __init__(self, title, subtitle, argument, 
            icon=None, autocomplete='autocompletex', uid=None):
        self.title = title    
        self.subtitle = subtitle
        self.uid = uid
        self.argument = argument
        self.icon = icon
        self.autocomplete = autocomplete    

def xml_string(items, first_uid=0):
    doc = minidom.Document()
    _items = doc.createElement('items')
    for (index,item) in enumerate(map(__itemAdapter,items)):
        item.setAttribute('uid', str(index+first_uid))
        _items.appendChild(item)
    doc.appendChild(_items)
    return doc.toprettyxml()

def __itemAdapter(item):
    doc = minidom.Document()
    _item = doc.createElement('item')
    _item.setAttribute('autocomplete', item.autocomplete)
    _item.setAttribute('arg', item.argument)
    title_attr = doc.createElement('title')
    title_content = doc.createTextNode(item.title)
    title_attr.appendChild(title_content)
    subtitle_attr = doc.createElement('subtitle')
    subtitle_content = doc.createTextNode(item.subtitle)
    subtitle_attr.appendChild(subtitle_content)
    _item.appendChild(title_attr)
    _item.appendChild(subtitle_attr) 
    return _item

