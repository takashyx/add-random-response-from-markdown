import mistune
import sys

import inspect
import pprint

target_heading = [
    'マネージャについて',
    'キャリア開発',
    '会話のきっかけ',
    '働きがい',
    'その他',
    'チームと会社',
    'ワーク・ライフ',
]


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
        if text in target_heading:
            return '====================\n' + text + '\n====================\n'
        else:
            return '----------\n' + text + '\n----------\n'

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

    if args_count == 3:
        target_heading = sys.argv[2]

    elif args_count != 2:
        print(f"arguments count not match.")
        print("usage:")
        print("python main.py [input_markdown_file]")
        exit()

    print(f"input_file: {sys.argv[1]}, target_heading: {target_heading}")
    md = parse_mdfile(sys.argv[1])

    # remove empty lines
    md = '\n'.join(
        filter(
            lambda x: x.strip(), map(
                lambda x: x.strip(), md.split('\n'))))

    print(md)

    if len(md) > 4000:
        print("[WARN] Char count > 4000: beyond the limit of Slack custom response")
