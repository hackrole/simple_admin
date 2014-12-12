#!/usr/bin/env python
# encoding: utf-8

import jinja2
import json
from tornado.options import options, define, parse_command_line


def simple_file(cfg_fp, tmp_fp, dist=None):
    text = open(tmp_fp).read()
    cfg = json.load(open(cfg_fp))

    template = jinja2.Template(text)

    print template.render(**cfg['context'])


if __name__ == "__main__":
    define("config", type=str, help="config file to use")
    define("file", type=str, help="template file to render")

    parse_command_line()
    simple_file(options.config, options.file)
