# Issue 6359: update to Python 2.6.2

Issue created by migration from https://trac.sagemath.org/ticket/6359

Original creator: mhansen

Original creation time: 2009-06-18 23:44:09

Assignee: mabshoff

CC:  sage-combinat nthiery

This requires updating a few other spkgs as well as some fixes in the Sage library.


---

Attachment


---

Comment by mhansen created at 2009-06-19 20:09:56

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2009-06-19 20:09:56

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-19 20:13:16

Note:  In order to get things to work, I did the following:

1) Took at 4.0.2 source tarball.

2) Replaced the spkgs in the tarball with the ones above.

3) Extracted the sage-*.spkg tarball, applied trac_6359-1.patch, and re "sage -spkg"'d it.

4) It's not necessary to apply the other two patches to get things up and running.


---

Comment by mhansen created at 2009-06-20 01:17:56

Note to Nicolas: This changes some things in combinat/ and structure/.  Do you want to have a look at them to decide what to do?


---

Comment by nthiery created at 2009-06-20 05:45:09

Replying to [comment:4 mhansen]:
> Note to Nicolas: This changes some things in combinat/ and structure/.  Do you want to have a look at them to decide what to do?

Thanks for the notice! Will do, but probably not before Monday!


---

Comment by boothby created at 2009-06-20 21:45:46

er... can I ask you to upload the python-2.6.2.spkg somewhere?


---

Comment by nthiery created at 2009-06-22 19:05:02

Replying to [comment:4 mhansen]:
> Note to Nicolas: This changes some things in combinat/ and structure/.  Do you want to have a look at them to decide what to do?

This commutes with the sage-combinat patches, so it's all good for me.


---

Comment by mhansen created at 2009-06-22 20:51:06

Nicolas: That's good to hear.  The changes were pretty minimal.

I've updated the python-2.6.2.spkg to copy over site-packages from 2.5 to 2.6.  I think this should do okay on upgrades.  I also added the ipython spkg update which was needed.


---

Comment by rlm created at 2009-06-25 01:15:39

Replying to [comment:8 mhansen]:
> I've updated the python-2.6.2.spkg to copy over site-packages from 2.5 to 2.6.  I think this should do okay on upgrades.  I also added the ipython spkg update which was needed.

Won't some packages need to have Python 2.6 actually do the installing? I am dubious that just copying over will work (although, of course, I wouldn't know).

Well, on top of alpha0, trac_6359-1.patch fails to apply, although I can't tell why at all- when I went in to fix the rejects (which weren't produced in the working directory like hg said they were), everything looked exactly the same. So after fixing the rest of the patch by hand, I repackaged Sage and forced the above packages to build.

Telling Sage to build very quickly fails, as it cannot find Jinja. So I force setuptools and jinja to build. The next problem is numpy. 
Forcing numpy to build does not solve the problem, either:


```
Traceback (most recent call last):
  File "setup.py", line 704, in <module>
    queue = compile_command_list(ext_modules, deps)
  File "setup.py", line 664, in compile_command_list
    dep_file, dep_time = deps.newest_dep(f)
  File "setup.py", line 579, in newest_dep
    for f in self.all_deps(filename):
  File "setup.py", line 560, in all_deps
    for f in self.immediate_deps(filename):
  File "setup.py", line 542, in immediate_deps
    self._deps[filename] = self.parse_deps(filename)
  File "setup.py", line 532, in parse_deps
    raise IOError, "could not find dependency %s included in %s."%(path, filename)
IOError: could not find dependency sage/plot/numpy.pxd included in sage/plot/complex_plot.pyx.
sage: There was an error installing modified sage library code.
```


Do we need to bump the version numbers for all the packages that go into site-packages (I can do this by hand if necessary)? This would make upgrading work for sure.

Also, your step 4) above is a bit lacking. What did you have to do, exactly, to get things up and running?


---

Attachment


---

Attachment


---

Comment by rlm created at 2009-06-25 08:44:20

Changing type from defect to enhancement.


---

Comment by rlm created at 2009-06-25 08:44:42

Resolution: fixed


---

Comment by rlm created at 2009-06-25 09:58:05

Changing status from closed to reopened.


---

Comment by rlm created at 2009-06-25 09:58:05

With the new Python spkg installed, `import _ssl` fails.

This is relevant:

http://www.webtop.com.au/compiling-python-with-ssl-support

One problem is that `Modules/_ssl.c` uses a lot more of OpenSSL than it used to, and much of what is used is not provided by the gnutls compatibility layer.


---

Comment by rlm created at 2009-06-25 09:58:05

Resolution changed from fixed to 


---

Comment by rlm created at 2009-06-25 10:03:17

For example, `SSL_ERROR_WANT_X509_LOOKUP` is implemented by OpenSSL but not supported by gnutls. There are a ton of others, too.


---

Comment by rlm created at 2009-06-25 10:04:05

I meant to say, for example, ..., and is used by `Modules/_ssl.c` in Python 2.6.2.


---

Comment by rlm created at 2009-06-25 17:16:04

Resolution: fixed
