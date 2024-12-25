# Overview

Pick your AMD P-State EPP power preference with this redundant and very simple tool!

# Requirements

Ensure that you:

- Installed the latest version of python on your linux distribution,
- Gave executable permissions to the main.py file,
- Are using AMD P-State EPP compatible hardware, with a compatible linux kernel.

# Notes

This program is now considered obsolete as most power management tools for linux support AMD P-State EPP.

Check main.py for a quick showcase of how this software works. It's extremely simple, and probably not ideal.

It may be ideal to place main.py in your ~/Scripts/ directory, or an equivalent, and alias its execution accordingly in your ~/.bash_aliases file via:

> alias='sudo python ./path/to/script/main.py'

The latter will allow the script to conveniently function in your terminal of choice.
