# Issue 7468: SageNB - Include `zope.testbrowser` and its dependencies in the SageNB package

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-11-15 07:26:48

Assignee: boothby

CC:  mpatel

This package will be used for future testing. Adding another package to a package was also done with the Trac package.


---

Comment by timdumol created at 2009-11-15 07:30:44

Adds `zope.testbrowser` to the package's dependencies and makes `spkg-dist` automatically download the dependencies. Depends on #7467


---

Attachment

This should do the trick.


---

Comment by timdumol created at 2009-11-15 07:31:10

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-11-26 14:30:06

Is zope.testbrowser (or does it appear to be) sufficiently powerful to implement a [nearly] complete Sage Remote Access API (cf. [comment:24:ticket:7343 this comment] at #7343)?  

Programmatic possibilities: login/out; create, archive, delete, rename, share, up/download, publish worksheets; add/remove data files.


---

Comment by was created at 2009-12-08 21:12:33

This patch is *totally unacceptable* as is.  The problem is this:

(1) Turn off your internet connection, then

(2) Try doing "sage -python setup.py install", and you get

```
...
Reading http://pypi.python.org/simple/zope.testbrowser/
Download error: [Errno 8] nodename nor servname provided, or not known -- Some packages may not be found!
Reading http://pypi.python.org/simple/zope.testbrowser/
Download error: [Errno 8] nodename nor servname provided, or not known -- Some packages may not be found!
Couldn't find index page for 'zope.testbrowser' (maybe misspelled?)
Scanning index of all packages (this may take a while)
Reading http://pypi.python.org/simple/
Download error: [Errno 8] nodename nor servname provided, or not known -- Some packages may not be found!
No local packages or download links found for zope.testbrowser>=3.7.0a1
error: Could not find suitable distribution for Requirement.parse('zope.testbrowser>=3.7.0a1')
```


Now imagine that you're building Sage from source on an airplane, or while camping, or working at a job which for security reasons doesn't allow outside network connections.

Options:

(1) Get zope.testbrowser included as a standard sage package. 

(2) Make the dependency on zope.testbrowser optional.  

 -- william


---

Comment by was created at 2009-12-08 21:12:33

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2009-12-09 11:59:41

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2009-12-09 11:59:41

I have edited the `spkg-dist` file, which I believe is used for creating the sagenb spkg, in this patch to automatically download zope.testbrowser and its dependencies, and include it in the spkg. Thus, installing through `sage -i sagenb` or `spkg-install` should not require internet access. Inclusion of package dependencies is also done in the Twisted package (zope.interface) and in the Trac package (Genshi).

Please correct me if I am mistaken, though.


---

Comment by was created at 2009-12-09 14:17:50

> Please correct me if I am mistaken, though. 

No, that should be fine, and is probably a good idea.     Can you post your edited spkg-dist file?


---

Comment by was created at 2009-12-09 14:19:53

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-09 14:19:53

Oops, I stupidly missed that you had already done that 3 weeks ago!  Thanks for teaching me setuptools. :-)  This indeed looks fine.


---

Comment by was created at 2010-01-04 06:59:11

Resolution: fixed


---

Comment by was created at 2010-01-04 06:59:11

Merged into sagenb-0.4.8.
