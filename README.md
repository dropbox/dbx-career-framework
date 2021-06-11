## Prerequisites
* Git 
* Ruby version 2.4.0 or higher (on Mac, `ruby --version` to check)
* RubyGems
* GCC and Make
* Jekyll (https://jekyllrb.com/docs/)
* [Access to Dropbox Github Repo] (https://paper.dropbox.com/doc/GitHub--BMWOq92bnKbETW~CWqqNqNUUAg-peghfrxGGazfpTVp7o15n)
## Setup
* Install bundler and jekyll
  `gem install --user-install  jekyll bundler`
* Check out Dropbox/dbx-career-framework
* Build the site
`cd <your-project-directory>` 
`bundle install`
* Run locally to make it available on a local server
`bundle exec jekyll serve`
* Browse to http://localhost:4000

## Content Management
* This repo uses ["Just the Docs"](https://pmarsceill.github.io/just-the-docs/). View the quick [start guide](https://jekyllrb.com/docs/) for more information. Just the Docs requires no special plugins and can run on GitHub Pages’ standard Jekyll compiler.
* Steps to add content to this repo
** export paper docs as Markdown
** add the document to specific directory under `docs` 
** Run `bundle exec jekyll serve` locally to verify the changes
** push changes to the repo
* To customize content or navigation, see the [docs here](https://pmarsceill.github.io/just-the-docs/docs/configuration/#document-collections)
