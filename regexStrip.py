#! /usr/bin/env python3
# regexStrip.py - Does the same thing as the strip() string method.

import re

text = input("Original text:")
new = input("Strip this:")

def strip(text,new):
    newstring = ''
    SspaceRegex = re.compile(r'^\s*')
    EspaceRegex = re.compile(r'\s*$')
    if new == '':
        newstring = SspaceRegex.sub(r'', text)
        return EspaceRegex.sub(r'', newstring)
    else:
        SspecRegex = re.compile(r'^[%s]+' % new)
        EspecRegex = re.compile(r'[%s]+$' % new)
        newstring = SspecRegex.sub(r'', text)
        return EspecRegex.sub(r'', newstring)
    

print(strip(text,new))
