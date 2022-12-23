# Issue 9921: Add release notes to SAGE_ROOT

Issue created by migration from https://trac.sagemath.org/ticket/9922

Original creator: jhpalmieri

Original creation time: 2010-09-16 19:57:55

Assignee: tbd

CC:  leif mvngu kcrisman

leif suggested at #9433 that we add release notes to SAGE_ROOT.  Perhaps they could be produced using mvngu's [rnotes script](http://sage.math.washington.edu/home/mvngu/apps/rnotes/) (also available at [http://bitbucket.org/mvngu/rnotes/](http://bitbucket.org/mvngu/rnotes/).  We could in fact (with his permission) include that script with Sage, and then run it as part of the sage-sdist script.


---

Comment by leif created at 2010-09-17 01:33:36

W.r.t. `VERSION.txt`: I think a single line containing the current version (perhaps also including _"[last] upgraded from ..."_) in plain format should be sufficient; cf. also #9434 and `local/bin/sage-banner`.


---

Comment by jhpalmieri created at 2011-09-08 19:03:39

In sage-sdist, should we write VERSION.txt to `SAGE_ROOT`, or should we create a symlink to `spkg/standard/VERSION.txt`?


---

Comment by kcrisman created at 2016-04-11 14:27:15

At the very least we could probably add the sum total changelog to `SAGE_ROOT`.  Which I notice is no longer on the website, only the individual changelogs...
