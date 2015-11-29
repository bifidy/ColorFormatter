# -*- coding: utf-8 -*-

from xmlhandle import xml_string, Item
import re

class Color(object):

    def __init__(self, query):
        self.query = query
        self.items = []
        self.color = None

    default_item = [Item(title=u'请输入格式为 "#xxxxxx" 的颜色值', 
                         subtitle=u'结果将直接复制至粘贴板',
                         argument='xxx')]

    def convert(self):
        if not self.query:
            return 

        match_funcs = dir(self)
        match_func = None
        for f in match_funcs:
            if f[:2] == 'm_' and getattr(self, f)():
                match_func = f[2:]
                break

        if not match_func:
            return

        for f in match_funcs:
            if f[:2] == 'c_' and not re.match(match_func, f):
                self.items.append(getattr(self, f)())


    def show(self):
        self.convert()
        print xml_string(items=self.items or self.default_item)

    # Every color must have at least one covert func (prefix '_m').
    # If needed, appending a match func (prefix '_c') is better~
    # Same color func name is needed, it can escape the inputed color format showing in the result.

    # HexColor "#xxxxxx"
    def m_hex_color(self):
        querys = re.findall(r'((?=\b)[0-9a-fA-F]{6})', self.query)
        if not querys:
            return False
        hexcolor = int('0x' + querys[0], 16)
        self.color = ((hexcolor >> 16) & 0xff, (hexcolor >> 8) & 0xff, hexcolor & 0xff, 1)
        return True

    def c_ui_color_oc(self):
        (r, g, b, a) = self.color
        _tuple = (float(r)/256, float(g)/256, float(b)/256, a)
        color_str = u'[UIColor colorWithRed:%.2f green:%.2f blue:%.2f alpha:%.2f]' % _tuple
        return Item(title = color_str, subtitle = u'UIColor·Objective-C', argument = color_str)

    def c_ui_color_swift(self):
        (r, g, b, a) = self.color
        _tuple = (float(r)/256, float(g)/256, float(b)/256, a)
        color_str = u'UIColor(red:%.2f, green:%.2f blue:%.2f alpha:%.2f)' % _tuple
        return Item(title = color_str, subtitle = u'UIColor·Swift', argument = color_str)


