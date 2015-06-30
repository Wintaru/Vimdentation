# Vimdentation
Sublime Text 3 Plugin For Vim-Like Indentation Abilities

## Synopsis
I wrote this plugin to give me the ability to look at old code and have it display correctly in Sublime Text. The codebase I support has indentation requirements that are unusual by today's standards, meaning they require Tab characters to be 8 spaces, but indentations to be 4 spaces.

This creates a problem with Sublime Text because while I can set the "tab_size" parameter to 8, it then causes all tab key presses to use 8 spaces as well. This is my attempt at resolving this issue. I decided to put this out there because from reading the forums and the userecho site for Sublime Text, there are at least a few other people out there in my shoes.

The name is corny, but I couldn't think of anything else to call it, and Vim (as well as emacs) is able to handle this type of indentation setting already.

## Installation

Until I decide if this deserves to go on the Package Manager for Sublime Text, you will have to do things the old fashioned way. Vimdentation.py should go inside a folder in your Packages folder (I named mine Vimdentation as well). You will then need these keymaps in your Key Bindings - User file:

```
{ "keys": ["tab"], "command": "vim_tab_press", "context":
    [
        { "key": "auto_complete_visible", "operator": "equal", "operand": false }
    ]
},
{ "keys": ["shift+tab"], "command": "vim_shift_tab_press" }
```

## Improvements
Please feel free to let me know if you find issues with this plugin. I'm not a python developer, this was cobbled together as a way for me to get my feet wet. I'm sure there are things that could be done better, and I'm also sure there are bugs to uncover. Thanks!
