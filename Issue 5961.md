# Issue 5961: Document potential interference issues with ~/.pydistutils.cfg

Issue created by migration from https://trac.sagemath.org/ticket/5961

Original creator: mabshoff

Original creation time: 2009-05-02 06:39:51

Assignee: tba

See https://groups.google.com/group/sage-devel/browse_thread/thread/2cee11b068180497

```
Dear Sage developers,

I tried to build Sage-3.4 on my intel macbook (Mac OS X 10.4.11).  I
have Xcode 2.5 installed and gcc-4.0.1. I downloaded the sage-3.4.tar,
untarred it and ran make. I have macports installed so changed the PATH
to remove anything from /opt.  I also renamed /opt to something else in
one attempt but both failed with the same error:

-------------
[...]
Sleeping for three seconds before testing python
Traceback (most recent call last):
   File "<string>", line 1, in <module>
   File "/Users/prabhu/src/build/sage-3.4/local/lib/python2.5/md5.py",
line 6, in <module>
     from hashlib import md5
   File
"/Users/prabhu/src/build/sage-3.4/local/lib/python2.5/hashlib.py", line
133, in <module>
     md5 = __get_builtin_constructor('md5')
   File
"/Users/prabhu/src/build/sage-3.4/local/lib/python2.5/hashlib.py", line
60, in __get_builtin_constructor
     import _md5
ImportError: No module named _md5
md5 module failed to import
[...]
sage: An error occurred while installing python-2.5.2.p9
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/prabhu/src/build/sage-3.4/install.log.  Describe your
computer, operating system, etc.

-----------------

Searching the lists for this gave me this:

http://groups.google.com/group/sage-devel/browse_thread/thread/e2fcb3...

which isn't very helpful.

After spending a little while figuring out what is wrong I realize that
I've done something a little non-standard that broke things.  I have
a default ~/.pydistutils.cfg which reads like so:

[install]
install_lib = ~/Library/Python/$py_version_short/site-packages
install_scripts = ~/usr/bin

I completely forgot about this and my install logs indicated a large
number of files being installed in the `install_lib` directory. So
moving this .pydistutils.cfg out of the way helped resolve the problem
and the build went well.

I think this should be documented somewhere so others don't fall into
the same trap.  Thanks.

cheers,
prabhu 
```



---

Comment by kcrisman created at 2015-01-05 16:13:20

This is a dup of #9536.


---

Comment by kcrisman created at 2015-01-05 16:13:20

Changing status from new to needs_review.


---

Comment by kcrisman created at 2015-01-05 16:13:41

Not that that one has had much activity lately either, but it has an actual patch and some conversation.


---

Comment by kcrisman created at 2015-01-05 16:13:41

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-01-13 01:14:12

Resolution: duplicate
