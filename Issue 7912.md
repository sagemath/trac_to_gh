# Issue 7912: upgrade Python to 2.6.4

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-01-12 19:47:15

Assignee: tbd

I'm posting an spkg to update Python from 2.6.2 to 2.6.4.  The changes from the previous spkg: in spkg-install, I have removed the lines

```
# This tells Bash to exit the script if any statement returns a non-true
# value.
set -e
```

Reason: in this part of the script, we want to test the return values and print a helpful message if they're not true, rather than just exit silently.

I've also removed the patch for the file `src/Lib/ctypes/__init__.py`, because I think it only deals with Mac OS X, 10.3 or earlier, and we don't support that.  Does Sage even build on pre-10.4 systems?

I looked at the other patches, and I think we still need them, but I'm not an expert.  (I tried removing the pickle patches, for instance, and got lots of doctest failures.)

I've added a patch file for socket.py: what we're patching hasn't changed, but in the previous spkg, there wasn't a patch file recording it.

The spkg is here: [http://sage.math.washington.edu/home/palmieri/SPKG/python-2.6.4.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/python-2.6.4.p0.spkg).

With this spkg, I see one new doctest failure, but I don't know if it's significant.  If it's not significant, it's easy enough to fix the doctest.  It's for `sage/misc/explain_pickle.py` -- see the last line ("(cPickle raised an exception!)"):

```
File "/Applications/sage_builds/sage-4.3.1.alpha1-new-python/devel/sage/sage/misc/explain_pickle.py", line 2279:
    sage: test_pickle(pickle.dumps(v))
Expected:
        0: (    MARK
        1: (        MARK
        2: l            LIST       (MARK at 1)
        3: p        PUT        0
        6: (        MARK
        7: g            GET        0
       10: t            TUPLE      (MARK at 6)
       11: p        PUT        1
       14: a        APPEND
       15: 0        POP
       16: 0        POP        (MARK at 0)
       17: g    GET        1
       20: .    STOP
    highest protocol among opcodes = 0
    explain_pickle in_current_sage=True/False:
    si1 = []
    si2 = (si1,)
    list.append(si1, si2)
    si2
    result: ([(...)],) (cPickle raised an exception!)
Got:
        0: (    MARK
        1: (        MARK
        2: l            LIST       (MARK at 1)
        3: p        PUT        0
        6: (        MARK
        7: g            GET        0
       10: t            TUPLE      (MARK at 6)
       11: p        PUT        1
       14: a        APPEND
       15: 0        POP
       16: 0        POP        (MARK at 0)
       17: g    GET        1
       20: .    STOP
    highest protocol among opcodes = 0
    explain_pickle in_current_sage=True/False:
    si1 = []
    si2 = (si1,)
    list.append(si1, si2)
    si2
    result: ([(...)],)
```



---

Comment by jhpalmieri created at 2010-01-12 19:47:21

Changing status from new to needs_review.


---

Comment by craigcitro created at 2010-01-14 20:15:17

Changing status from needs_review to positive_review.


---

Comment by craigcitro created at 2010-01-14 20:15:17

I'm listing this as positive review -- I used this spkg as the base when I made a newer one for #7095. There were one or two tiny issues (removing the `wininst-*.exe` files, for instance), but I fixed those up. I think we should close this ticket, since this is now going to get merged as part of #7095. (John, if you agree, go ahead and close it.)


---

Comment by jhpalmieri created at 2010-01-14 21:08:13

Resolution: duplicate


---

Comment by jhpalmieri created at 2010-01-14 21:08:13

I'm closing this as "duplicate", since Craig has a revised version of the spkg at #7095, and we should use that one instead.
