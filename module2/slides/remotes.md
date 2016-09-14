## Remotes

A git repo may have many copies in various locations called remotes:

* URL reference to other copies of the repository
* most commonly github
* `origin` - automatically created remote when a repo is cloned
* `cat .git/config` - see configured remotes
* `git add remote <name> <url>` add additional remote
* `git remote --help` - add'l remote operations