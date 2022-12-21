# Issue 7230: [with spkg, needs review] Switch from setuptools to Distribute

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2009-10-16 00:05:56

Assignee: tbd

CC:  wstein mhansen leif

Distribute is a fork of setuptools that aims to be open and actively maintained. It's also run by a handful of core Python devs.

There's a new spkg file, as well as updates to `spkg/install` and `spkg/standard/deps`. All three are sitting in this directory:

  http://sage.math.washington.edu/home/craigcitro/distribute-spkg/

To test, delete the setuptools spkg, drop in the new `install` and `deps`, and then build sage. (Or, alternately, build the two spkgs that currently depend on setuptools -- Jinja and SQLAlchemy.)


---

Comment by craigcitro created at 2009-10-16 00:08:45

I should say -- I've currently got a build from scratch running on my machine; I'll report any trouble I run into.


---

Comment by craigcitro created at 2009-10-16 00:08:52

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2009-10-16 04:56:27

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2009-10-16 04:56:27

It worked fine for me on sage.math, but with a 64-bit build on Mac OS X 10.5, it didn't: when it tried to build Sphinx, it couldn't find Jinja.  (Then I very cleverly deleted the log file, so I can't reproduce the exact error message.  I'm building again, trying both 32- and 64-bit, and I'll post the error message assuming I get it again.)

Also, #6586 has just been merged in to 4.2.alpha0, and this includes jinja2 (in addition to jinja).  Do you need to modify deps and install to deal with jinja2?


---

Comment by craigcitro created at 2009-10-16 05:41:59

Yep, it failed on my Mac, too. I have no idea why: it's having trouble finding the Jinja egg, which is there in `site-packages`, and is listed in `easy_install.pth`! Here's the error message:


```
Installed /Users/craigcitro/Desktop/four-one-two/local/lib/python2.6/site-packages/Sphinx-0.5.1-py2.6.egg
Processing dependencies for Sphinx==0.5.1
Searching for Jinja>=1.1
Reading http://pypi.python.org/simple/Jinja/
Reading http://wsgiarea.pocoo.org/jinja/
Reading http://jinja.pocoo.org/
Best match: Jinja 1.2
Downloading http://pypi.python.org/packages/source/J/Jinja/Jinja-1.2.tar.gz#md5=1235a005ade00b213800ff1e798c0241
Processing Jinja-1.2.tar.gz
Running Jinja-1.2/setup.py -q bdist_egg --dist-dir /var/folders/L+/L+y6mfGYHtmJhXJSt0GpXE+++TI/-Tmp-/easy_install-3zfQSo/Jinja-1.2/egg-dist-tmp-lzQOap
No eggs found in /var/folders/L+/L+y6mfGYHtmJhXJSt0GpXE+++TI/-Tmp-/easy_install-3zfQSo/Jinja-1.2/egg-dist-tmp-lzQOap (setup script problem?)
error: Could not find required distribution Jinja>=1.1
```


It's clearly trying to go out and grab a dependency from the internet -- but I don't know why. In theory, that dependency should be provided already ... here's `easy_install.pth`:


```
import sys; sys.__plen = len(sys.path)
./distribute-0.6.6-py2.6.egg
./Jinja-1.2-py2.6-macosx-10.3-i386.egg
./Pygments-0.11.1-py2.6.egg
./Sphinx-0.5.1-py2.6.egg
import sys; new=sys.path[sys.__plen:]; del sys.path[sys.__plen:]; p=getattr(sys,'__egginsert',0); sys.path[p:p]=new; sys.__egginsert = p+len(new)
```


It's *identical* to the `easy_install.pth` installed via setuptools; I have no idea why it's failing.


---

Comment by jhpalmieri created at 2009-10-16 14:51:17

Well, I couldn't reproduce that error because I got one when trying to build jinja; it's still trying to use setuptools:

```

---------------------------------------------------------------------------
This script requires setuptools version 0.6c5 to run (even to display
help).  I will attempt to download it for you (from
http://cheeseshop.python.org/packages/2.6/s/setuptools/), but
you may need to enable firewall access for this script first.
I will start the download in 15 seconds.

(Note: if this machine does not have network access, please obtain the file

   http://cheeseshop.python.org/packages/2.6/s/setuptools/setuptools-0.6c5-py2.6.egg

and place it in this directory before rerunning this script.)
---------------------------------------------------------------------------
Downloading http://cheeseshop.python.org/packages/2.6/s/setuptools/setuptools-0.6c5-py2.6.egg
Traceback (most recent call last):
 
[snip]

urllib2.HTTPError: HTTP Error 404: Not Found
Error installing Jinja.
```

I get this with both 32-bit and 64-bit.

As I said earlier, I've also seen a different error -- it got a little farther and bombed when it reached Sphinx, and it was trying to download Jinja1.2.  In that case, there were files "setuptools.pth" and "setuptools-0.6....egg" in SAGE_ROOT/local/lib/python/site-packages by the time the build failed.


---

Comment by jhpalmieri created at 2011-06-20 18:22:12

Changing status from needs_work to positive_review.


---

Comment by jhpalmieri created at 2011-06-20 18:22:12

This can be closed: #11363 has made it redundant.


---

Comment by jdemeyer created at 2011-06-20 18:52:56

Resolution: duplicate
