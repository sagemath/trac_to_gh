# Issue 7799: install_scripts should not install M2

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2009-12-31 01:50:51

Assignee: tbd

I have done


```
install_scripts("/usr/local/bin/")
```


on a Ubuntu machine with installed Macaulay2 and it stopped working. Apparently, M2 is one of the scripts that the above command has copied and it tries to use M2 shipped with Sage. However, Sage does not include Macaulay2, the package for it is broken and the recommended way to use them together is to install Macaulay2 separately. This works fine before installing scripts and after, if I remove M2 from /usr/local/bin manually.


---

Comment by jhpalmieri created at 2009-12-31 07:07:14

Here's a patch.  I think that the problem is, in the old version, the command 'which M2' was executed, and if it didn't return a system error (meaning that M2 didn't exist), then it installed the Sage script.  The patch changes it so it checks if 'which M2' returns an error, and if not, then whether 'which M2' starts with SAGE_ROOT.  If not, then M2 is already installed elsewhere, so don't install the Sage script.  (Of course it does this for all of the scripts, not just for M2.)

I've also added a doctest.

We could also worry about whether M2 should be included here at all, given its status.  I suggest that we keep it, since if my patch works the way I think, we should never install the script as long as we don't distribute a working version of M2, but if someone fixes the spkg for it, then we don't have to remember to reinstate it in 'install_scripts'.


---

Comment by jhpalmieri created at 2009-12-31 07:07:14

Changing status from new to needs_review.


---

Attachment

patch for main Sage repository


---

Comment by novoselt created at 2009-12-31 19:46:47

Changing status from needs_review to positive_review.


---

Comment by novoselt created at 2009-12-31 19:46:47

Works fine for me, install_scripts does not break Macaulay2 with this patch.


---

Comment by was created at 2009-12-31 19:50:15

Another positive review from me.


---

Comment by mhansen created at 2010-01-03 20:42:20

Resolution: fixed
