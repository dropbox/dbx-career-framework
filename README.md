# Dropbox Engineering Career Framework

This repo has two parts:

1. A public version of drl/eng-career, located in the `docs` directory
2. A `cleaner.py` script that converts drl/eng-career into the public version

# Setup

To run `cleaner.py`:

1. (One time) Create a virtual env. for the project: `python3 -m venv env`
2. Active the virtual env: `source env/bin/activate`
3. (One time) `python3 -m pip install beautifulsoup4`
3. Go to drl/eng-career and get your session cookie (using the browser's developer tools)
4. Download the binder: `wget --header "Cookie: sessionid=SESSION_ID" --mirror --convert-links
   --adjust-extension --page-requisites --no-parent -P raw --cut-dirs=3
   https://app.dropboxer.net/binder/eng-career/`
5. Run the "cleaner": `python3 clean.py raw/app.dropboxer.net ./docs --allow_file allow-list.txt`

Review any changes to the site made by the script and open a pull request.
