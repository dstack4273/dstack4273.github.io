Title: Use Python to Save a Web Page
Date: 2016-9-24 14:20
Category: Using Python
Tags: how-to, Python2, Python3, tools
Slug: use-python-to-save-a-web-page
Status: published

I wrote most of this a couple of months ago, but I forgot to post it...because well, I'm not great at this blogging thing yet. I'll try to get better about that.

I finally finished up a post to a car forum that I follow to provide a little DIY about something that I added to my car for the other users to reference. I also figured it might help encourage anyone that might have been on the fence whether they were going to buy the product or not. One of the regular contributors to that forum asked if I could provide a PDF of the thread, or if they could. I took a quick look around and checked out what the output of print saved to PDF by way of the OS X built-in utility would look like, and thought that there might be a web based offering that might provide slightly nicer results. I found one that worked fairly well, but it watermarked all of the pages unless you bought a premium (monthly fee) user license. Another almost identical utility (probably the same underlying code even) had an almost identical set up.

Next I turned to Google to see if there was perhaps an open source Python package that could do something like what I was looking for: Enter pdfkit [github](https://github.com/JazzCore/python-pdfkit), [pypi](https://pypi.python.org/pypi/pdfkit/0.4.1).

This [post on stackoverflow](http://stackoverflow.com/questions/23359083/how-to-convert-webpage-into-pdf-by-using-python), showed that I could accomplish this task with a crisp two lines of code: sign. me. up! I went ahead and pip installed my newfound open source savior, only to find out that it had a dependency: wkhtmltopdf. Okay no sweat I'll just grab that , install it real quick, and be on my way.

>**/Sidebar/**
>
After learning the hard learned lesson about dependencies getting tangled up, and the difficulty of updating and managing software installs on OS X, I switched over to homebrew, which I try to always use now if at all possible. If you haven't used it, I *highly* encourage you to check it out. Homebrew is invoked via the command line using `brew {some operator command} <software that you want you want to do something with>`

>**/End Sidebar/**

I tried using `brew info wkhtmltopdf` but instead of the short details I expected to see back instead homebrew returned `Error: No available formula with the name "wkhtmltopdf"`. Grrr, so I go to the wkhtmltopdf homepage (http://wkhtmltopdf.org/) and saw that they have a nice set of installers to get everything up and running. But, first I wanted to see if I could figure out why wkhtmltopdf wasn't available in brew so I searched around a bit and eventually came across a note in the pdfkit Github repository wiki (https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf) that said I could use `brew install Caskroom/cask/wkhtmltopdf`. I ran that in my terminal and everything installed great! Now I moved back to my editor and put together my short script:

``` python
import os
from pdfkit import from_url as converter

my_desktop = os.path.expanduser('~/Desktop')

converter('http://forums.vwvortex.com/showthread.php?7825737-INA-HPFP-Cam-Follower-to-TSI-Roller-Install-DIY-lite', my_desktop + '/post.pdf' )
```
</br>
From that little script (which could probably be shortened with some clever one-liner syntax, and a URL shortener), I now had a PDF on my desktop named "post".

The script throws out an error `Exit with code 1 due to network error: ContentNotFoundError`, but everything still works like I needed it to. As an added benefit, this should work in both Python 2 and Python 3 - yay!
