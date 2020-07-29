# lcc-tree
Make a LCC Treemap with a bunch of MARC files

view here: https://thisismattmiller.github.io/lcc-tree/


To make your own. You need python3 installed.

1. Put all your MARC files into one directry.
2. Edit build_data.py to reflect that location and make sure you install the need libraries `pip3 install pymarc tqdm`
3. Run `python3 build_data.py`
4. Run `python3 build_json_tree.py`
5. Fork https://observablehq.com/@thisismattmiller/harvard-lcc-treemap into your own workbook.
6. Find the line that says `data = FileAttachment("listhierarchy@1.json").json()` click the paperclip and replace the json file with your own `listhierarchy.json` that was created by the scripts.
7. 🌲🤷‍♂️🌲
