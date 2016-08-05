Title: Configure VirtualEnv to run Python 2 and 3 Side by Side
Date: 2016-7-17 14:17
Category:Dev Environment
Tags:VirtualEnv, Python2, Python3, Configuration, Hacks
Slug: configure-virtualenv-to-run-python-2-and-3-side-by-side
Status: draft


Recently one of the tutorials that I have wanted to work on was actually explicitly for Python3. Since virtually everything else that I have worked on to this point is for Python2, I hadn't really given any thought to the problem of how to continue to use VirtualEnv with a different version of Python. The topic is covered some











```
python3 = which python3

alias mkvirtualenv3 = mkvirtualenv -p $python3


alias lls="ls \-al"
export PS1="\[\033[36m\]\u:\[\033[m\]\w\[\033[m\]$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

#nvm
export NVM_DIR=~/.nvm
. $(brew --prefix nvm)/nvm.sh

#move usr/local to front of path
export PATH=usr/local/bin:$PATH

WORKON_HOME = ~/Envs
source /usr/local/bin/virtualenvwrapper.sh

#ruby env mgr
if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi
```
