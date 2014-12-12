#!/usr/bin/env python
# encoding: utf-8

class {{ model_class_name }}({{ base_class }}):
    {% for field in model_fields %}
    {{ field.name }} = {{ field.class }}
    {% endfor %}
