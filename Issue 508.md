# Issue 508: problem with "sage -c"

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-29 08:19:22

Assignee: was

Create any script, say test.sage.  The following should work but doesn't:

```
  # sage -c "load test.sage"
Traceback (most recent call last):
  File "/home/was/s/local/bin/sage-eval", line 10, in <module>
    eval(compile(s,tmp_filename(),'exec'))
  File "/home/was/.sage//temp/sage/25215//tmp_0", line 1
    load test.sage
            ^
SyntaxError: invalid syntax
```



---

Comment by craigcitro created at 2007-09-07 05:28:29

Changing component from algebraic geometry to user interface.


---

Comment by anakha created at 2008-10-23 23:02:00

Why is this supposed to work?

Anyway I did some investigation, and the problem comes from the fact that preparse() doesn't take care of "load test.sage" since that is done by ipython magic usually.  

There is very complicated logic in sage-preparse to deal with those that would be inappropriate to reproduce in sage-eval.

Also there is a very simple workaround: sage test.sage

So I vote for 'wontfix' for this bug.


---

Comment by was created at 2008-10-23 23:37:25

> So I vote for 'wontfix' for this bug.

Just because you couldn't fix it and there is a workaround doesn't mean it isn't a bug.

And this is still a bug in sage-3.2:

```
teragon:tmp wstein$ more a.sage
print 2^3
teragon:tmp wstein$ sage -c "load a.sage"
Traceback (most recent call last):
  File "/Users/wstein/sage/local/bin/sage-eval", line 10, in <module>
    eval(compile(s,tmp_filename(),'exec'))
  File "/Users/wstein/.sage//temp/teragon.local/98089//tmp_0", line 1
    load a.sage
         ^
SyntaxError: invalid syntax

```



---

Attachment

Fixes the problem by emulating load and attach.

It won't work with files that have spaces in their name because sage, sage-sage, sage-run, and various other are not ready to deal with that, yet.


---

Comment by was created at 2008-11-27 07:49:26

This doesn't work because when sage-eval gets run the working directory is local/bin/, so the file test.sage isn't found.  I bet you tested this patch with test.sage in SAGE_ROOT/local/bin/, which is the only case when this will work:

```
teragon-2:sage-3.2 wstein$ more test.sage
print "Hi"
teragon-2:sage-3.2 wstein$ ./sage -c "load test.sage"
/Users/wstein/sage/build/sage-3.2/local/bin/sage-preparse: File test.sage is missing
python: can't open file 'test.py': [Errno 2] No such file or directory
teragon-2:sage-3.2 wstein$ cp test.sage local/bin/
teragon-2:sage-3.2 wstein$ ./sage -c "load test.sage"
Hi
```



---

Attachment


---

Comment by abergeron created at 2008-12-24 04:57:07

Changing assignee from was to abergeron.


---

Comment by abergeron created at 2008-12-24 04:57:07

It did work with 3.1.4 in other directories.  But it doesn't with 3.2 and up as you pointed out.

Last patch fixes this.


---

Comment by GeorgSWeber created at 2008-12-29 21:15:08

Target time for the review: January 12th


---

Comment by GeorgSWeber created at 2009-01-15 21:40:14

Rescheduled for January 18th


---

Comment by GeorgSWeber created at 2009-01-18 23:52:55

Works fine, and looks good to me. (Apply the v2 patch only; tested with Sage 3.2.3)

I adjusted the milestone because this patch does not interfere with the sphinxification.


---

Comment by mabshoff created at 2009-01-19 06:14:38

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 06:14:38

Merged in Sage 3.3.alpha0
