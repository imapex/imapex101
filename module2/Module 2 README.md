[Class Contents](../README.md)

# Module 2: Advanced Git and GitHub

Basic Operations
-----------------------

For this module it is assumed that the reader has a basic working knowledge of basic git workflow including creating
repositories, cloning, and making commits to a simple repository.


The official tutorial for Github is a useful resource and can be find [Here](https://guides.github.com/activities/hello-world/)

Issues / Tags
-----------------------

Issues are the primary vehicle by which feature enhancements and bug fixes are tracked.

Labels are used to categorize the the issue. Examples of tags are enhancement, bug, question, help wanted.

 A detailed explanation of Issues, Labels, and Milestones can be found [Here](https://guides.github.com/features/issues/)

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
is important to consider what other developers are doing relative to the project. The fork based workflow is dominant in
opensource projects as contributors likely would not have access to push code to the main repository.

For more information see this [Stack Overflow Post](http://stackoverflow.com/questions/3611256/forking-vs-branching-in-github)

Stashing Changes
------------------------

Another useful workflow within Git is the ability to stash local changes prior to performing other operations on the
repository - a good example of this is that you've been working on some changes and want to pull the latest changes that
others have committed.

In it's simplest form, you can executre the stash/unstash workflow with the following commands

```
git stash

git stash apply
```

*NOTE* One important thing to remember is that git stash will not save files in the working directory unless they have been
added to the index (git add)

A detailed explanation of git stash can be found [Here](https://git-scm.com/book/en/v1/Git-Tools-Stashing)

Discussion Items for kickoff

* Production deployments will be done from the master branch
* All feature development should be done via the developers fork / branch
* All feature development should have an open issue tagged enhancement for tracking purposes
* All bug fixes should have an open issue for tracking purposes



README Standards and Expectations
----------------------------------

A good README file is important for outlining the motivation behind a particular project repository, as well
as providing the reader with an overview of how to effectively utilize the project repository.


[http://stackoverflow.com/questions/2304863/how-to-write-a-good-readme](http://stackoverflow.com/questions/2304863/how-to-write-a-good-readme)


* ASCII characters only, if the README is written in English
* write it in English if possible, and ship translated version with two-letter
  language code extension like README.ja
* 80 characters or less per line
* single empty line between paragraphs
* dashes under the headers
* indent using whitespace (0x20) not tab



Pull Requests
-----------------------

Pull requests are the way of notifying others about changes that you've checked in and you want incorporated into the
main project.  Pull requests can be issued from a forked repository, or from a branch within a single repository.

TODO
-----------------------
* Public vs Private Repos
* Git Skills
* Rebasing
* Fast Forward
* Forking and Syncing
* Managing Multiple Development Environments

Lab Exercise
=============================

For the lab exercise of this module we will be combining these steps into a real-world workflow.


# Instructions

1. Open an Issue against the imapex/101-github-lab referencing the fact that your email is missing from the CONTRIBUTORS.txt
file. As you are now going to be contributing to the project - this is obviously and enhancement, so label it as such!!!

2. Assign yourself to the issue

3. Create a fork of your /101-github-lab repository

	```
   git clone https://github.com/<your_git_id>/101-github-lab
   ```

4. Create and checkout a new branch for your enhancement

	```
   git branch -m adding-email-addr
    git checkout adding-email-addr
   ```

	* **_NOTE_ If your branch is going to exist for a longer period of time why you are developing your feature you could add the upstream repo as a remote for your repository as well.**

		```
	   git remote add --track master upstream git://github.com/upstreamname/projectname.git
	   ```

	* Now you can get updates from the main project as well by using:

		```
	   git fetch upstream
	   git merge upstream/master
	   ```

5. Make the appropriate changes to add your email address to the CONTRIBUTORS.txt file.

6. Commit your changes, be sure to indicate the issue number that you are working on in your commit message

	```
    git add CONTRIBUTORS.txt
   git commit -m "added email address - closes #XXX"
   ```
7. Push your changes from local to your forked repository
    ```
    git push -u origin adding-email-addr
    ```

5. From your web browser, go to the github page of your fork, and open a pull request.

6. Navigate to the upstream repository [IMAPEX/101-github-lab](https://github.com/imapex/101-github-lab) and
verify that the pull request was issued.  From here discussion can occur on the proposed changes, and the owner
of the repository can merge the changes in once completed.  
	* **_Note_ An opened PR is often a trigger for a something to
happen in the build pipeline, such as automated testing of the proposed changes.**


# Helpful Git CLI Workflows 

Here are some example git command structures for some common actions.  

* Create new branch and push to remote

	```
	git checkout -b BRANCH
	git push -u origin BRANCH
	```

* Pull down branch that is on remote repo locally

	```
	# view remote branched
	git branch -v -a
	
	# fetch all remote branches
	git fetch origin
	
	# create local branch and start working
	git checkout -b BRANCH origin/BRANCH
	```
	
* Sync your fork with master

	```
	# Link your local fork repo to the upstream and verify 
	git remote add upstream <https://github.com..>
	git remote -v

	# Pull your fork
	git pull

	# Pull upstream
	git pull upstream master

	# Push to your fork
	git push origin master
	```

* Merge Master (or another branch into a branch)

	```
	# Switch to destination
	git checkout master

	# Merge
	git merge <branch>

	# Push changes
	git push
	```

