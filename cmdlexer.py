from pygments.lexer import RegexLexer
from pygments.token import *


class CommandLexer(RegexLexer):
    name = 'cmd'
    aliases = ['cmd']
    filenames = ['*.sh']

    tokens = {
        'root': [
            (r'#.*$', Comment),				# A Comment
            (r'[\>\<=~\+\-]', Operator),
            (r'\".+\"', Literal),			# A String
            (r'\'.+\'', Literal),			# A String
            (r'^[ ]{0,}[A-Za-z0-9]+',Keyword),		# A Command
            (r'\|[ ]{0,}[A-Za-z0-9]+', Keyword),	# Piping in commands
            (r'\$[A-Za-z0-9_]+', Name.Variable),	# Variables like $USER
            (r'--?[^ \n]+', Generic.Inserted),		# Options in a command
            (r'[^ \n]+', Generic.Deleted),     		# Arguments
            (r'\s', Name),				# Ignore Whitespace
        ]
    }
