# Issue 7796: prevent Sphinx from rebuilding full document

Issue created by migration from https://trac.sagemath.org/ticket/7796

Original creator: mvngu

Original creation time: 2009-12-30 15:26:07

Assignee: mvngu

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/64bcac2d0705570f):

```
I built the html documentation in a fresh 4.3 build using "sage
-docbuild reference html" as usual.  I made a clone, and it appeared
that all the docs were rebuilt (another 5 mins).  I made a change to a
docstring in one file (see #7780) and did "sage -b" and then "sage
-docbuild reference html" again, and again it appeared that all the
docs were built -- another 5 mins. 
```

Mitesh Patel suggests the following fix:

```
A possible workaround:  In

SAGE_LOCAL/lib/python2.6/site-packages/Sphinx-0.6.3-py2.6.egg/sphinx/environment.py

import inspect and insert, e.g.,

                if inspect.isfunction(config[key]):
                    continue

around line 474. 
```



---

Comment by mvngu created at 2009-12-30 15:37:54

An updated spkg is up at

http://boxen.math.washington.edu/home/mvngu/spkg/standard/sphinx/sphinx-0.6.3.p4.spkg


---

Comment by mvngu created at 2009-12-30 15:37:54

Changing status from new to needs_review.


---

Comment by cremona created at 2009-12-30 17:10:12

I installed the revised spkg (though I'm not qualified to judge the valifity of what was changed in its source code).  Then made a clone -- ok, no rebuilding of docs happened automatically.  In the clone, doing "sage -docbuild reference html" caused the docs to build: ok.   I then made a trivial change to a source file and re-did the docbuild:  ok, just that file was rebuilt.  I then switched back to the main brancha nd again did a docbuild, expecting nothing to happen -- but a complete docbuild started.

It would be good if someone else would try this too.  It looks as if we have made progress but not solved it yet.


---

Comment by mvngu created at 2009-12-30 20:21:33

I took the source tarball of Sage 4.3 and replaced the package  sphinx-0.6.3.p3.spkg` with `sphinx-0.6.3.p4.spkg`. I then built Sage 4.3 with the updated Sphinx package. On a newly compiled Sage 4.3 with the updated Sphinx spkg, I tested the updated Sphinx spkg as follows:

 1. The command "./sage -docbuild all html" didn't rebuild any of the documents in the standard documentation.
 1. I made a clone of the main branch and executed "./sage -docbuild all html", which build the doc. 
 1. I made a trivial change to a file in the cloned branch. Again, I ran "./sage -docbuild all html", which only rebuilt the portion of the document that has changed.
 1. Switching back to the main branch didn't rebuild any of the documents.

So the problem here is that the updated Sphinx spkg needs to also be built and installed during the build process of Sage. That is, you need to replace the previous version of the Sphinx package with the updated spkg before compiling Sage 4.3 from source. You would still experience the same problem of documents rebuilding if you force an installation of the updated Sphinx spkg on an already compiled Sage.


---

Comment by cremona created at 2009-12-30 20:29:53

I would be happy to trust you on this without going through all that myself!  But perhaps we need a third opinion before giving this a positive review?

I would think that making this spkg replacement part of the first alpha release of 4.3.1 would be the best way of testing it more thoroughly.


---

Comment by jhpalmieri created at 2009-12-30 23:26:33

Replying to [comment:2 cremona]:
> I then switched back to the main branch and again did a docbuild, expecting nothing to happen -- but a complete docbuild started.

The new spkg-install file deletes all of the documentation output (from all of the branches, not just the active one), so the docs for sage-main were deleted -- that's why they had to be rebuilt.

Anyway, the whole thing works as advertised for me.  Can we give it a positive review now?

Also, do we need to report anything upstream (in conjunction with the changes in #7683)?


---

Comment by jhpalmieri created at 2009-12-30 23:26:33

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 22:25:33

Resolution: fixed
