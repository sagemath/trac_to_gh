# Issue 9683: pretty_print clobbers _ (history)

Issue created by migration from Trac.

Original creator: mguaypaq

Original creation time: 2010-08-04 05:05:14

Assignee: was

CC:  mhansen

Keywords: pretty_print, history

After using `pretty_print`, the first history variable (`_`) no longer updates.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: combinat
sage: 17
17
sage: _
17
sage: 23
23
sage: _
23
sage: pretty_print(17)
<html><span class="math">\newcommand{\Bold}[1]{\mathbf{#1}}17</span></html>
sage: _
17
sage: 23
23
sage: _
17
```

| Sage Version 4.5.1, Release Date: 2010-07-19                       |
| Type notebook() for the GUI, and license() for information.        |
The relevant function seems to be `pretty_print` in `/sage/misc/latex.py`, but I don't know the right way to fix it. The function and `pretty_print_default` in same file, and the functions `displayhook` and `install` in `/sage/misc/displayhook.py` may also be relevant.



---

Comment by iandrus created at 2012-11-25 21:34:43

In the  ipython `displayhook` it checks to see if underscore was set explicitly and if so, it stops tracking.  We are setting it explicitly in `pretty_print`.  Maybe if we just stop doing this it will work.  Also we probably need to fix `pretty_print_default` to set it to the ipython `displayhook` instead of the default one.


```
    def check_for_underscore(self):
        """Check if the user has set the '_' variable by hand."""
        # If something injected a '_' variable in __builtin__, delete
        # ipython's automatic one so we don't clobber that.  gettext() in
        # particular uses _, so we need to stay away from it.
        if '_' in __builtin__.__dict__:
            try:
                del self.shell.user_ns['_']
            except KeyError:
                pass
```



---

Attachment

I've posted a patch.  It doesn't have a test for this problem. I could make one, but it's slightly annoying since you have to do everything indirectly through an IPython shell object.


---

Comment by mhansen created at 2013-07-24 16:09:34

Changing status from new to needs_review.


---

Comment by vbraun created at 2014-04-10 21:21:32

New commits:


---

Comment by vbraun created at 2014-04-10 21:21:32

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-04-10 21:21:32

Changing keywords from "pretty_print, history" to "pretty_print, history, days57".


---

Comment by vbraun created at 2014-04-13 19:33:28

Resolution: fixed
