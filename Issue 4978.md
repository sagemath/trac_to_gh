# Issue 4978: fix NTL tuning issue on Linux/ppc64

Issue created by migration from https://trac.sagemath.org/ticket/4978

Original creator: mabshoff

Original creation time: 2009-01-14 22:55:53

Assignee: mabshoff

spkg-install has the following:

```
    # Do performance tuning steps.
    if [ `uname` = "Linux" -a `uname -m` = "ppc64" ]; then
        echo "NTL auto tuning is broken on Linux ppc64.  Please report this to Victor Shoup.  Thanks."
    else
        do_tune
    fi
```

I cannot imagine the tuning code being broken and even if it is the spkg should still at least build, so fix it.

Cheers,

Michael


---

Comment by was created at 2009-01-15 03:00:22

> I cannot imagine ... being broken ...

Famous last words :-)


---

Comment by mabshoff created at 2009-01-29 03:32:45

The issue is fixed via the spkg at #5040.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 03:32:45

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-29 04:05:46

Indirect positive review by Carl Witty via #5040.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 04:06:01

Resolution: fixed


---

Comment by mabshoff created at 2009-01-29 04:06:01

Merged in Sage 3.3.alpha3.

Cheers,

Michael
