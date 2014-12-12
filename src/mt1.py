#!/usr/bin/env python
# encoding: utf-8

class User(Document):
    
    mobile = StringField(required=True, max_length=10)
    
    nickname = StringField(required=True)
    
    pwd = StringField(required=True)
    
