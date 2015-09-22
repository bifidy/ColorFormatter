# -*- coding: utf-8 -*-

from xmlhandle import xml_string, Item
import re
def format_color(query):
    default_item = Item(title=u'请输入格式为 "#xxxxxx" 的颜色值',
                        subtitle=u'结果将直接复制至粘贴板',
                        argument=query)
    if not validate(query):
        print xml_string(items=[default_item])

    rgb_tuple = rgb_color('0x' + query[1:7])
    ui_color_item = Item(title=ui_color(rgb_tuple),
                         subtitle='UIColor',
                         argument=ui_color(rgb_tuple))
    
    print xml_string(items=[ui_color_item])


def rgb_color(query):
    hexcolor = int(query,16)
    return ((hexcolor >> 16) & 0xff, 
            (hexcolor >> 8) & 0xff, 
            hexcolor & 0xff)

def validate(query):
    re_str = r'^#[0-9a-fA-F]{6}$'
    return re.match(re_str,query)

def ui_color(rgb_tuple):
    (red, green, blue) = rgb_tuple
    _tuple = (float(red)/256, float(green)/256, float(blue)/256)
    return '[UIColor colorWithRed:%.2f green:%.2f blue:%.2f alpha:1]' % _tuple

