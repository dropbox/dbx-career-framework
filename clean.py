import argparse
import os
from bs4 import BeautifulSoup

def dir_path(dir):
    if os.path.isdir(dir):
        return dir
    else:
        raise NotADirectoryError(dir)

def parse_args():
    parser = argparse.ArgumentParser(description='Massages Binder Output')
    parser.add_argument('in_dir', help='The directory containing files to clean', type=dir_path)
    parser.add_argument('out_dir', help='The directory to output to', type=dir_path)
    parser.add_argument('--allow_file', help='A file containing components to include, one per line')
    return parser.parse_args()

def read_allow_list(args):
    if args.allow_file:
        with open(args.allow_file) as f:
            allow_list = []

            for line in f:
                allow_list.append(line.strip())

            return allow_list
    else:
        return []

def clean(dir_entry, args, allow_list):
    with open(dir_entry.path) as fp:
        soup = BeautifulSoup(fp)

        # Remove search
        for el in soup.find_all(id='toc-search'):
            el.extract()

        # remove edit links
        for el in soup.find_all('a', 'edit'):
            el.extract()

        # remove unnecessary scripts
        for el in soup.find_all('script'):
            # Google analytics
            if el.string and 'GoogleAnalyticsObject' in el.string:
                el.extract()

            # Search
            if el.string and 'function search' in el.string:
                el.extract()

            # Feedback prompt
            if el.string and 'feedback-button' in el.string:
                el.extract()

            # Revision check
            if el.string and 'checkRevisions' in el.string:
                el.extract()

            # binder JS
            if 'src' in el.attrs and 'binder.js' in el['src']:
                el.extract()

            if el.string and 'enable_safeWindowOpen' in el.string:
                el.extract()

            if el.string and 'loadLocalLink' in el.string:
                el.extract()

        for el in soup.find_all('a'):
            # remove external links
            if el['href'].startswith('http'):
                el.unwrap()

            # remove links to things not in allow-list
            if len(allow_list) > 0 and el['href'] not in allow_list:
                el.extract()

        # Remove empty TOC entries
        for el in soup.find_all('div', 'ace-line selectable'):
            if len(el.contents) == 0:
                el.extract()

        for el in soup.find_all('div', 'child-container'):
            if len(el.contents) == 0:
                el.parent.extract()

        for el in soup.find_all('div', 'ace-line hidden'):
            el.extract()

        # remove original-href and data-doc-id attributes from anchors
        for el in soup.find_all('a'):
            del el['data-doc-id']
            del el['original-href']
            del el['prev-name']
            del el['prev-href']
            del el['next-name']
            del el['next-href']

        # Rewrite static link/script urls
        for el in soup.find_all('link'):
            if 'dropbox-appbox-static' in el['href']:
                el['href'] = 'static/' + el['href'].split('/')[-1]

        for el in soup.find_all('script'):
            if 'src' in el.attrs and 'dropbox-appbox-static' in el['src']:
                el['src'] = 'static/' + el['src'].split('/')[-1]

        # Output
        with open(os.path.join(args.out_dir, dir_entry.name), mode='w') as wp:
            print(str(soup), file=wp)


def main():
    args = parse_args()
    allow_list = read_allow_list(args)

    for file in os.scandir(args.in_dir):
        if len(allow_list) == 0 or file.name in allow_list:
            # FIXME parse and pass allow list
            clean(file, args, allow_list)


if __name__ == "__main__":
    main()
