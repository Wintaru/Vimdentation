import sublime, sublime_plugin
import sys
import re

class VimTabPressCommand(sublime_plugin.TextCommand):
    """
    This is meant to be bound on the tab key like this:
    { "keys": ["tab"], "command": "vim_tab_press", "context":
        [
            { "key": "auto_complete_visible", "operator": "equal", "operand": false }
        ]
    }

    The context parameter ensures this doesn't break auto
    complete when "auto_complete_commit_on_tab": true is
    set.

    This lets you set a tab char width in spaces that
    is independent of the spaces advanced when the tab
    key is pressed. In my case, tabs are translated to
    spaces (8 of them), but below I have it set to insert
    4 spaces when tab is pressed.
    """
    def run(self, edit):
        spaces = "    "
        space_count = len(spaces)
        sel = self.view.sel()
        for region in sel:
            # If the region isn't empty it's selected text so
            # break out the lines in the selection and add the
            # spaces to the beginning of each line selected.
            if not region.empty():
                selectedLines = self.view.lines(region)
                i = 0
                for l in selectedLines:
                    self.view.insert(edit, l.begin() + i, spaces)
                    i += space_count
            else:
                # For those cases where nothing is selected, put the
                # spaces whereever the cursor is.
                self.view.insert(edit, region.begin(), spaces)

class VimShiftTabPressCommand(sublime_plugin.TextCommand):
    """
    This is meant to be bound on the tab key like this:
    { "keys": ["shift+tab"], "command": "vim_shift_tab_press"}

    Used in tandem with the above command, this allows you to use
    shift+tab in a way you might expect it to work. If you have
    your tab spaces set to 8, shift tab will move back 8 instead of
    4 without this.
    """
    def run(self, edit):
        spaces = "    "
        space_count = len(spaces)
        sel = self.view.sel()
        for region in sel:
            selectedLines = self.view.lines(region)
            for l in reversed(selectedLines):
                # Extract the string from the line region
                s = self.view.substr(l)

                # Only do this if there are enough spaces to start
                if s.find(spaces,0) == 0:
                    self.view.erase(edit, sublime.Region(l.begin(), l.begin() + space_count))
