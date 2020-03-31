import mistune
import sys

import inspect
import pprint


class CustomRenderer(object):

    NAME = 'custom'
    IS_TREE = False

    def __init__(self):
        self._methods = {}

    def register(self, name, method):
        self._methods[name] = method

    def text(self, text):
        return text

    def link(self, link, children=None, title=None):
        return ''

    def image(self, src, alt="", title=None):
        return ''

    def emphasis(self, text):
        return ''

    def strong(self, text):
        return text

    def codespan(self, text):
        return text

    def linebreak(self):
        return '<br />\n'

    def inline_html(self, html):
        return html

    def paragraph(self, text):
        return f"{text}\n"

    def heading(self, text, level):
        return ''

    def newline(self):
        return ''

    def thematic_break(self):
        return ''

    def block_text(self, text):
        return text

    def block_code(self, code, info=None):
        return f"```\n{code}```\n"

    def block_quote(self, text):
        return f"```\n{text}```"

    def block_html(self, html):
        return f"```\n{html}```"

    def block_error(self, html):
        return f"```\n{html}```"

    def list(self, text, ordered, level, start=None):
        # if ordered:
        #     html = '<ol'
        #     if start is not None:
        #         html += ' start="' + str(start) + '"'
        #     return html + '>\n' + text + '</ol>\n'
        return f"{text}\n"

    def list_item(self, text, level):
        return f"{text}\n"

    def _get_method(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            method = self._methods.get(name)
            if not method:
                raise AttributeError('No renderer "{!r}"'.format(name))
            return method

def parse_mdfile(input_filename):
    try:
        with open(input_filename, 'r') as input_file:
            m = mistune.Markdown(renderer=CustomRenderer())
            md = m(input_file.read())
            return md

    except Exception as e:
        print("File read error")
        print(e)
        exit()


if __name__ == "__main__":

    args_count = len(sys.argv)
    if args_count == 2:
        print(f"input_file: {sys.argv[1]}")
        md = parse_mdfile(sys.argv[1])
    else:
        print(f"arguments count not match.")
        print("usage:")
        print("python main.py [input_markdown_file]")
        exit()

    md = '\n'.join(filter(lambda x: x.strip(), map(lambda x: x.strip(), md.split('\n'))))

    print(md)

