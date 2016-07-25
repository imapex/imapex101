[Class Contents](../README.md)

# Module 2: Advanced Git and GitHub

Prerequisites
-----------------------

For this module it is assumed that the reader has a basic working knowledge of basic git workflow including creating
repositories, cloning, and making commits to a simple repository.

Issues / Tags
-----------------------

Issues will be the primary vehicle by which feature enhancements and bug fixes will be tracked.

*TIP:* To close an issue in the same repository, use one of the keywords in the list below followed by a
reference to the issue number in the commit message. For example, a commit message with Fixes #45 will close issue 45
in that repository once the commit is merged into the default branch.

If the commit is in a non-default branch, the issue will remain open and the issue will be referenced with a tooltip.

For more information and similar tips see [https://help.github.com/articles/closing-issues-via-commit-messages/]

Forking vs Branching
-----------------------

Forking and Branching are mechanisms used by Git to diverge from the main code line for feature development, or bug
fixes. Branches are seperate trains within the same repository, whereas a fork, creates a copy of the entire repository in
a different location (user account). From the perspective of a single developer the two are very similar, however, it
is important to consider what other developers are doing relative to the project.


Discussion Items for kickoff

* Production deployments will be done from the master branch
* All feature development should be done via the developers fork / branch
* All feature development should have an open issue tagged enhancement for tracking purposes
* All bug fixes should have an open issue for tracking purposes




README Standards and Expectations
----------------------------------

A good README file is important for outlining the motivation behind a particular project repository, as well
as providing the reader with an overview of how to effectively utilize the project repository.


[http://stackoverflow.com/questions/2304863/how-to-write-a-good-readme]


* ASCII characters only, if the README is written in English
* write it in English if possible, and ship translated version with two-letter
  language code extension like README.ja
* 80 characters or less per line
* single empty line between paragraphs
* dashes under the headers
* indent using whitespace (0x20) not tab



Pull Requests
-----------------------

Pull requests should be issues against the main repositories 'development' branch


Public vs Private Repos
-----------------------

TODO
-----------------------
* Git Skills
* Rebasing
* Fast Forward
* Forking and Syncing
* Managing Multiple Development Environments