"""jinjaxelatex - Python script to create templated XeLaTeX documents"""

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
    if os.path.exists(path):
        if os.path.isdir(path):
            return True
        else:
            raise e
    else:
        os.makedirs(path)
        return True

def render_template(j2env, template, context):
    pass

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

def fname(arg):
    pass

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
        with open()

def run_command(*args):
    """CLI wrapper"""
    opts = [i for i in args]
    cmd = [] + opts
    process = Popen(cmd, stdout=PIPE)
    process.communicate()[0]
    return process
