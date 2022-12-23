# Issue 8669: interrupting download in sage-spkg should delete the spkg file

Issue created by migration from https://trac.sagemath.org/ticket/8669

Original creator: jhpalmieri

Original creation time: 2010-04-10 18:56:51

Assignee: tbd

CC:  leif

If you run `sage-spkg PKG_NAME` and hit ctrl-c during downloading, you end up with a partial spkg file.  Then if you run `sage-spkg PKG_NAME` again, it just opens up that file and then crashes because the file is incomplete.

The attached patch attempts to fix this.  It seems to work, deleting the partially downloaded file, but for reasons I don't understand, it's not printing any of the accompanying messages.



---

Comment by jhpalmieri created at 2010-04-10 18:57:55

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-04-10 18:57:55

I'm marking this as "needs review", but if anyone can fix the printing problem mentioned in the summary, that would be great.


---

Comment by leif created at 2010-04-10 20:31:03

The reason for the "non-printing" is simple:

In `local/bin/sage-sage`, the output of `sage-spkg` is piped to `tee`, which is run from the same subshell and so gets the same signal.

(`sage-spkg` _does_ print the messages, but `tee` _does not_ "wait" for the _post-_`Ctrl-C` output.)


---

Comment by jhpalmieri created at 2010-04-10 22:44:49

Replying to [comment:2 leif]:
> The reason for the "non-printing" is simple:
> 
> In `local/bin/sage-sage`, the output of `sage-spkg` is piped to `tee`, which is run from the same subshell and so gets the same signal.

Any ideas how to fix this?  I tried using "pipestatus" from #8306, but it doesn't seem to help: when I hit ctrl-C, it prints 

```
[..^Cclose failed in file object destructor:
Error in sys.excepthook:

Original exception was:
```



---

Comment by jhpalmieri created at 2010-04-10 23:41:59

Okay, here's a new patch without any printing problems.


---

Comment by jhpalmieri created at 2010-04-10 23:42:12

scripts repo


---

Attachment

scripts repo


---

Attachment

scripts repo (same as other patch)


---

Attachment

To the release manager: please delete all but "trac_8669-download.patch".


---

Comment by timdumol created at 2010-04-18 08:28:02

Works as advertised. Positive review.


---

Comment by timdumol created at 2010-04-18 08:28:02

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-19 05:20:51

Merged "trac_8669-download.patch" into 4.4.alpha1.


---

Comment by jhpalmieri created at 2010-04-19 05:20:51

Resolution: fixed
