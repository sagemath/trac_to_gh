# Issue 3873: Doctest should test for warnings

Issue created by migration from https://trac.sagemath.org/ticket/3873

Original creator: jason

Original creation time: 2008-08-15 11:05:50

Assignee: mabshoff

This patch makes it so that warnings are output to stdout and are compared in the doctest framework.  To doctest a warning, do something like:


```
def mytest():
    r"""
    EXAMPLES:
        sage: warnings.warn("hi")
        /...:1: UserWarning: hi
        #...
        """
    pass
```


This patch will probably break a few doctests (that gave warnings before, but the warnings were ignored).


---

Attachment


---

Comment by jason created at 2008-08-16 16:58:36

This patch should be applied to whatever repository includes $SAGE_LOCAL/bin/


---

Comment by jason created at 2008-08-24 00:14:09

This depends on #3940 (which imports the warnings module on sage startup).


---

Attachment


---

Attachment


---

Comment by cwitty created at 2008-08-24 00:52:48

Positive review for Jason's patch; my two patches need to be reviewed.  The first patch (to be applied to sage_scripts after Jason's patch) fixes Jason's patch to not depend on #3940 any more, and to get rid of useless filenames (that would have to be elided from every doctest).

The second patch fixes the two places in the Sage library that generate warnings in doctests.


---

Comment by mabshoff created at 2008-08-25 00:19:38

Nice patches, but how does #3940 relate here?

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-25 00:25:13

Positive review for Carl's patches.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-25 01:13:06

Merged all three patches in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-25 01:13:06

Resolution: fixed
