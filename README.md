simple_admin
============

使用jinja2模板功能,实现快速建立admin原型

初步计划
~~~~~~~~

1) 使用方式
simple_admin -d <template-directory> -c <config.json> -o <dist-directory>

simple_admin -f <template_file> -c <config.json> -o <dist_directory>

2) config.json格式
{
    context: {<模板变量>},
}
