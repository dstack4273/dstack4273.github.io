Title: Configure VirtualEnv to run Python 2 and 3 Side by Side
Date: 2016-7-17 14:17
Category:Dev Environment
Tags:VirtualEnv, Python2, Python3, Configuration, Hacks
Slug: configure-virtualenv-to-run-python-2-and-3-side-by-side
Status: published


Recently one of the tutorials that I have wanted to work on was actually explicitly for Python3. Since virtually everything else that I have worked on to this point is for Python2, I hadn't really given any thought to the problem of how to continue to use VirtualEnv with a different version of Python. The topic is covered some in bits and pieces here and there, but no one really comes out and explains how to get it working. I do all of my work on OS X, so my configuration settings are from my .bash_profile dotfile. I have an existing Python 3 and Python 2 install through Homebrew. I had initially set up my VituralEnv Wrapper from the instructions listed in [this tutorial](http://newcoder.io/begin/setup-your-machine/). After that is working for you, all you should have to do is set up something like what I have in my .bash_profile:

</br>

```
python3 = which python3

alias mkvirtualenv3 = mkvirtualenv -p $python3
```
</br>

What this does is sets an environment variable that reads the location of your python3 install, and uses it along with the `mkvirtualenv` command's -p flag to define the version of python that you want to create your virtual environment with. You could just hard code in the path of your python3 install, but I thought that maybe using the actual `python3` shell path might make it a little more robust to any changes I might make absentmindedly.


###Use
Using this is super easy because of how I went about building it to work. Essentially those two lines allow me to have an alias that looks similar to the format of the `python` vs `python3` commands. For a Python 2 project you can type `mkvirtualenv <project name>` and for a Python 3 project `mkvirtualenv3 <project name>` where `<project name>` is the name of your project...(without the pointy brackets) and you'll have a new shiny virtual environment to start working in.


---

Here are all of the things that I currently have in my .bash_profile if you are curious in what other witchcraft I've got gathered together:

```
alias lls="ls \-al"
alias mkvirtualenv3="mkvirtualenv -p $py3"

export PS1="\[\033[36m\]\u:\[\033[m\]\w\[\033[m\]$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

#nvm
export NVM_DIR=~/.nvm
. $(brew --prefix nvm)/nvm.sh

#move usr/local to front of path
export PATH=usr/local/bin:$PATH

WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh

#ruby env mgr
if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi

py3=$(which python3)

#adroid sdk
export PATH=~/Library/Android/sdk/tools:$PATH
export PATH=~/Library/Android/sdk/platform-tools:$PATH
```

</br>

If you have any tips on how you work with both versions of Python in your environment please comment below. If you have any questions post them up and I'll do my best to answer them.


</br>
