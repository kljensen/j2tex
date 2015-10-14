#!/usr/bin/env python

import logging
logging.basicConfig(format='%(filename)s %(levelname)s ' \
        + 'line %(lineno)d --- %(message)s',)
logging.root.setLevel(logging.INFO)
import argparse


__version__ = '0.1.0'
__author__ = 'Kyle Jensen <kljensen@gmail.com>'
__all__ = []

import re
import yaml
import jinja2
import codecs
import os

LATEX_SUBS = (
    (re.compile(r'\\'), r'\\textbackslash'),
    (re.compile(r'([{}_#%&$])'), r'\\\1'),
    (re.compile(r'~'), r'\~{}'),
    (re.compile(r'\^'), r'\^{}'),
    (re.compile(r'"'), r"''"),
    (re.compile(r'\.\.\.+'), r'\\ldots'),
)

def escape_tex(value):
    newval = value
    for pattern, replacement in LATEX_SUBS:
        newval = pattern.sub(replacement, newval)
    return newval


def get_jinja_env(template_directory):
    params = {
        'block_start_string': '((*',
        'block_end_string': '*))',
        'variable_start_string': '(((',
        'variable_end_string': ')))',
        'comment_start_string': '((=',
        'comment_end_string': '=))',
        'loader': jinja2.FileSystemLoader(os.path.abspath(template_directory))
    }
    letter_renderer = jinja2.Environment(**params)
    letter_renderer.filters['escape_tex'] = escape_tex
    return letter_renderer

def load_yaml_file(file_path, encoding="utf-8"):
    """ Load a YAML file with a particular encoding and returns the data.
    """
    data = None
    with codecs.open(file_path, mode="r", encoding=encoding) as fh:
        data = yaml.load(fh)
    return data

def load_context_files(paths):
    """ Load a series of context files, each of which
        updates a single dictionary
    """
    data = {}
    for path in paths:
        data.update(load_yaml_file(path))
    return data

def mkdir(path):
    abspath = os.path.abspath(path)
    if os.path.exists(abspath):
        if os.path.isdir(abspath):
            return True
        else:
            raise e
    else:
        os.makedirs(abspath)
        return True

def validate_context(context):
    output = context.get('output', [])
    if len(output) == 0:
        raise Error('Your YAML context files need an `output` section')
    for o in output:
        if not context.get('template'):
            if not o.get('template'):
                raise Exception('Each output in your YAML context file requires a `template`')
        if not o.get('key'):
            raise Exception('Each output in your YAML context file requires a `key`')

def get_subcontext(default_context, overrides):
    subcontext = {}
    subcontext.update(default_context)
    subcontext.update(overrides)
    return subcontext

def get_output_file_path(output_directory, template, key, extension=None):
    """ Get the absolute file path for an output file
    """
    path = os.path.join(output_directory, template)
    if extension and path.endswith(extension):
        path = path[:-len(extension)]
    path = "{0}-{1}.tex".format(path, key)
    return path


def render_tex(j2env, context, output_directory):
    validate_context(context)
    mkdir(output_directory)
    default_context = {k: v for (k,v )in context.iteritems() if k != 'output'}
    for overrides in context['output']:
        subcontext = get_subcontext(default_context, overrides)
        tex_content = j2env.get_template(subcontext['template']).render(subcontext)
        output_file = get_output_file_path(
            output_directory,
            subcontext['template'],
            subcontext['key']
        )
        with codecs.open(output_file, mode="w", encoding="utf-8") as fh:
            fh.write(tex_content)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--context',
        action='append',
        required=True,
        help="YAML file with context data",
        metavar='CONTEXT_DATA_FILE'
    )
    parser.add_argument(
        '--template_directory',
        default='.',
        help="template file with context data",
        metavar='TEMPLATE_FILE'
    )
    parser.add_argument(
        '--output',
        default='.',
        help="output directory",
        metavar='OUTPUT_DIRECTORY'
    )
    args = parser.parse_args()
    return args


def main(context_files, template_directory, output_directory):
    j2env = get_jinja_env(template_directory)
    context = load_context_files(context_files)
    render_tex(j2env, context, output_directory)

if __name__ == '__main__':
    args = parse_args()
    main(args.context, args.template_directory, args.output)
