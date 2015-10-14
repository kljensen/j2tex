#!/usr/bin/env python

import logging
logging.basicConfig(format='%(filename)s %(levelname)s ' \
        + 'line %(lineno)d --- %(message)s',)
logging.root.setLevel(logging.INFO)
import argparse

from j2tex import load_context_files, get_jinja_env, render_tex

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
        required=True,
        help="output directory",
        metavar='OUTPUT_DIRECTORY'
    )
    args = parser.parse_args()
    return args

def main(context_files, template_directory, output_directory):
    j2env = get_jinja_env(template_directory)
    context = load_context_files(context_files)
    render_tex(j2env, context, output_directory)
    print template_directory



if __name__ == '__main__':
    args = parse_args()
    main(args.context, args.template_directory, args.output)
