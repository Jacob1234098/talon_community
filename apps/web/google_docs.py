# """
# line numbers: https://chrome.google.com/webstore/detail/line-numbers-for-google-d/mblodabbcapnkgcfnddfpfaamjckjlik?hl=en
# go to line number
# snipline [#]
# cellrang
# wordneck/wordprev
# crew/trail
# cell crew/cell trail
# cursor center/top/bottom
# `menu share`
# """

# import time

# from talon.voice import Context, Key, press
# from talon import ctrl

# from . import browser


# ctx = Context(
#     "google_docs", func=browser.url_matches_func("https://docs.google.com/.*")
# )
# ctx.keymap(
#     {
#         "copy": Key("cmd+c"),
#         "cut": Key("cmd+x"),
#         "paste": Key("cmd+v"),
#         "paste without formatting": Key("cmd+shift+v"),
#         "undo": Key("cmd+z"),
#         "redo": Key("cmd+shift+z"),
#         "(insert | edit) link": Key("cmd+k"),
#         "open link": Key("alt+enter"),
#         "[show] [common] keyboard shortcuts": Key("cmd+/"),
#         "save": Key("cmd+s"),
#         "print": Key("cmd+p"),
#         "open": Key("cmd+o"),
#         # "find": Key("cmd+f"),
#         "find and replace": Key("cmd+shift+h"),
#         "find again": Key("cmd+g"),
#         "find (previous | prev)": Key("cmd+shift+g"),
#         "hide [the] menus ": Key("ctrl+shift+f"),
#         "[insert] page break": Key("cmd+enter"),
#         "(search [the] menus | command pallet)": Key("cmd+/"),
#         "bold": Key("cmd+b"),
#         "italicize": Key("cmd+i"),
#         "underline": Key("cmd+u"),
#         "strikethrough": Key("cmd+shift+x"),
#         "superscript": Key("cmd+."),
#         "subscript": Key("cmd+,"),
#         "copy [text] formatting": Key("cmd+alt+c"),
#         "paste [text] formatting": Key("cmd+alt+v"),
#         "(clear | remove) [text] formatting": Key("cmd+\\"),
#         "increase font size": Key("cmd+shift+>"),
#         "decrease font size": Key("cmd+shift+<"),
#         "increase [paragraph] indentation": Key("cmd+]"),
#         "decrease [paragraph] indentation": Key("cmd+["),
#         "[apply] normal (text | style)": Key("cmd+alt+0"),
#         "[apply] heading [style] 1": Key("cmd+alt+1"),
#         "[apply] heading [style] 2": Key("cmd+alt+2"),
#         "[apply] heading [style] 3": Key("cmd+alt+3"),
#         "[apply] heading [style] 4": Key("cmd+alt+4"),
#         "[apply] heading [style] 5": Key("cmd+alt+5"),
#         "[apply] heading [style] 6": Key("cmd+alt+6"),
#         "left align": Key("cmd+shift+l"),
#         "center align": Key("cmd+shift+e"),
#         "right align": Key("cmd+shift+r"),
#         "justify": Key("cmd+shift+j"),
#         "numbered list": Key("cmd+shift+7"),
#         "(bullet | bulleted) [list]": Key("cmd+shift+8"),
#         "resize larger": Key("cmd+ctrl+k"),
#         "resize larger horizontally": Key("cmd+ctrl+b"),
#         "resize larger vertically": Key("cmd+ctrl+i"),
#         "resize smaller": Key("cmd+ctrl+j"),
#         "resize smaller horizontally": Key("cmd+ctrl+w"),
#         "resize smaller vertically": Key("cmd+ctrl+q"),
#         "rotate clockwise by 15 degree": Key("alt+right"),
#         "rotate counterclockwise by 15 degree": Key("alt+left"),
#         "rotate counterclockwise by 1 degree": Key("alt+shift+left"),
#         "rotate clockwise by 1 degree": Key("alt+shift+right"),
#         "close drawing [editor]": Key("cmd+esc"),
#         "(insert | add) comment": Key("cmd+alt+m"),
#         "open discussion thread": Key("cmd+alt+shift+a"),
#         "enter [current] comment": Key("ctrl+enter"),
#         "insert footnote": Key("cmd+alt+f"),
#         "move to current footnote": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("e"),
#             press("f"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to next footnote": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("f"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to (previous | prev) footnote": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("f"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "context menu": Key("cmd+shift+\\"),
#         "file menu": Key("ctrl+alt+f"),
#         "new (file | document | doc)": [
#             Key("ctrl-alt-f"),
#             Key("down"),
#             Key("down"),
#             Key("right"),
#             Key("enter"),
#         ],
#         "rename": [
#             Key("ctrl-`"),
#             lambda m: time.sleep(1),
#             "rename",
#             lambda m: time.sleep(1),
#             Key("enter"),
#         ],
#         "edit menu": Key("ctrl+alt+e"),
#         "view menu": Key("ctrl+alt+v"),
#         "insert menu": Key("ctrl+alt+i"),
#         "format menu": Key("ctrl+alt+o"),
#         "tools menu": Key("ctrl+alt+t"),
#         "table menu": Key("ctrl+alt+b"),
#         "help menu": Key("ctrl+alt+h"),
#         "accessibility menu": Key("ctrl+alt+a"),
#         "input tools menu": Key("cmd+alt+shift+k"),
#         "toggle input controls": Key("cmd+shift+k"),
#         "select all": Key("cmd+a"),
#         "select line": [Key("cmd-left"), Key("shift-end")],
#         "extend selection [one] character left": Key("shift+left"),
#         "extend selection [one] character right": Key("shift+right"),
#         "extend selection [one] line up": Key("shift+up"),
#         "extend selection [one] line down": Key("shift+down"),
#         "extend selection to the beginning of the line": Key("shift+home"),
#         "extend selection [one] paragraph up": Key("alt+shift+up"),
#         "extend selection [one] paragraph down": Key("alt+shift+down"),
#         "extend selection to the end of the line": Key("shift+end"),
#         "extend selection to the beginning of the document": Key("cmd+shift+up"),
#         "extend selection to the end of the document": Key("cmd+shift+down"),
#         "select current list item": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("e"),
#             press("i"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "select all list items at current level": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("e"),
#             press("o"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "enable screen reader supportlearn more about using google docs with a screen reader": Key(
#             "alt+cmd+z"
#         ),
#         "speak selection": Key("ctrl+cmd+x"),
#         "speak from cursor location": Key("ctrl+cmd+r"),
#         "announce cursor location": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("a"),
#             press("l"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "announce formatting at cursor location": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("a"),
#             press("f"),
#             ctrl.ke8y_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "speak the table column and row header": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("h"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "speak the table cell location": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("n"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "speak the table row header": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("r"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "speak the table column header": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("c"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "[move to] next heading": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("h"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "[[move] to] (previous | prev) heading": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("h"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "[[move] to] next heading 1": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("1"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "[move to] next heading 2": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("2"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "[move to] next heading 3": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("3"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "[move to] next heading 4": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("4"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "[move to] next heading 5": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("5"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "[move to] next heading 6": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("6"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "[move to] (previous | prev) heading 1": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("1"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "[move to] (previous | prev) heading 2": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("2"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "[move to] (previous | prev) heading 3": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("3"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "[move to] (previous | prev) heading 4": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("4"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "[move to] (previous | prev) heading 5": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("5"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "[move to] (previous | prev) heading 6": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("6"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to next media": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("g"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to (previous | prev) media": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("g"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to next list": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("o"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to (previous | prev) list": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("o"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to next item in the current list": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("i"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to (previous | prev) item in the current list": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("i"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to next link": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("l"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to (previous | prev) link": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("l"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to next bookmark": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("b"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to (previous | prev) bookmark": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("b"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "(move to | spring) (next | neck) (formatting | format) [change]": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("w"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "(move to | spring) (previous | prev) (formatting | format) [change]": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("w"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to the next edit": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("n"),
#             press("r"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to the (previous | prev) edit": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("p"),
#             press("r"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move to the start of the table": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("s"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "move to the end of the table": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("d"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "move to the start of the table column": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("i"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "move to the end of the table column": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("k"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "move to the next table column": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("b"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "move to the (previous | prev) table column": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("v"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "move to the start of the table row": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("j"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "move to the end of the table row": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("l"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "move to the next table row": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("m"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "move to the (previous | prev) table row": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("g"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "exit table": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("t"),
#             press("e"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "move to the next table": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("n"),
#             press("t"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "move to the (previous | prev) table": lambda m: (
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, down=True),
#             press("p"),
#             press("t"),
#             ctrl.key_press("shift", ctrl=True, cmd=True, shift=True, up=True),
#         ),
#         "open revision history": Key("cmd+alt+shift+h"),
#         "open explore tool": Key("cmd+alt+shift+i"),
#         "open dictionary": Key("cmd+shift+y"),
#         "word count": Key("cmd+shift+c"),
#         "start voice typing": Key("cmd+shift+s"),
#         "page up": Key("pageup"),
#         "page down": Key("pagedown"),
#         "move to next misspelling": Key("cmd+'"),
#         "move to (previous | prev) misspelling": Key("cmd+;"),
#         "insert or move to header": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("o"),
#             press("h"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "insert or move to footer": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("o"),
#             press("f"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move focus to popup": lambda m: (
#             ctrl.key_press("cmd", ctrl=True, cmd=True, down=True),
#             press("e"),
#             press("p"),
#             ctrl.key_press("cmd", ctrl=True, cmd=True, up=True),
#         ),
#         "move focus out of document text": Key("cmd+alt+shift+m"),
#         "return focus to document text": Key("esc"),
#         "focus containing webpage": Key("ctrl+shift+esc"),
#         "(show | view | toggle) outline [view]": [Key("ctrl-cmd-a"), Key("ctrl-cmd-h")],
#         # "(search menus | command pallet)": Key('cmd-/'),
#         "snipline": [Key("cmd-left"), Key("cmd-shift-right"), Key("backspace")],
#         "snip bullet": [
#             Key("cmd-left"),
#             Key("cmd-shift-right"),
#             Key("backspace"),
#             Key("backspace"),
#             Key("backspace"),
#             Key("backspace"),
#         ],
#     }
# )
