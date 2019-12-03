from pygments.lexer import RegexLexer
from pygments.token import *


class CommandLexer(RegexLexer):
    name = 'cmd'
    aliases = ['cmd']
    filenames = ['*.sh']

    tokens = {
        'root': [
            (r'#.*$', Comment.Multiline),
            (r'\".+\"', Text),
            (r'^[ ]{0,}[A-Za-z0-9]+\s+',Keyword),
            (r'--?[^ \n]+\s+', Generic.Inserted),
            (r'[^ \n]+\s+', Generic.Deleted),
        ]
    }
