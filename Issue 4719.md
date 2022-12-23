# Issue 4719: Doctests report mysterious errors instead of ordinary failures

Issue created by migration from https://trac.sagemath.org/ticket/4719

Original creator: davidloeffler

Original creation time: 2008-12-05 21:00:20

Assignee: mabshoff

CC:  gfurnish

Keywords: doctests

The doctest module in 3.2.2.alpha0 seems to report *all* failed doctests as "A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest." This occurs even when the failure is a very simple one:


```
def bad_docstring():
        r""" A function with a bogus docstring.

        EXAMPLES:
                sage: 2
                1
        """
        pass
```


Running "sage -t" on a file containing only the above code returns a "mysterious error", both on 32-bit SuSE (upgraded from 3.2.1) and on the sage.math binary. 


---

Comment by mabshoff created at 2008-12-05 21:03:29

The issue has been more than likely introduced by #717. My guess is that the output from the doctest run is not passed back and the logic "no output -> mysterious error" kicks in. 

Cheers,

Michael


---

Attachment

Failing doctests should now fail correctly.


---

Comment by gfurnish created at 2008-12-06 03:23:09

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-12-06 03:23:09

Changing assignee from mabshoff to gfurnish.


---

Comment by mabshoff created at 2008-12-06 05:08:01

Nice work. The problem cases now pass correctly. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-06 05:08:23

Merged in Sage 3.2.2.alpha1


---

Comment by mabshoff created at 2008-12-06 05:08:23

Resolution: fixed
