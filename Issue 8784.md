# Issue 8784: remove quit_sage() command from all.py top level

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-27 20:47:41

Assignee: jason

It is stupid that it is this easy to accidentally destabilize and segfault Sage.    Also, having a function "quit_sage()" available at the sage: prompt by default that does not quit sage, is dumb. 

```
wstein`@`boxen:~/build/sage-4.4$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: quit_sage()
Exiting Sage (CPU time 0m0.04s, Wall time 0m3.16s).
sage: quit
Exiting Sage (CPU time 0m0.07s, Wall time 0m4.80s).
/virtual/scratch/wstein/build/sage-4.4/local/bin/sage-sage: line 206: 11559 Segmentation fault      sage-ipython "$`@`" -i
wstein`@`boxen:~/build/sage-4.4$            
```

| Sage Version 4.4, Release Date: 2010-04-24                         |
| Type notebook() for the GUI, and license() for information.        |
The fix is to rename quit_sage() somehow and change *all* code that calls it. 


---

Comment by jason created at 2010-04-28 02:30:02

Maybe rename it to "sage_library_cleanup"?


---

Comment by mjo created at 2022-01-25 22:50:54

Now all of the cleanup happens automatically and `quit_sage()` is a no-op:


```
sage: quit_sage()
<ipython-input-1-ce1781e96a1f>:1: DeprecationWarning: quit_sage is deprecated and now does nothing; please simply delete it
See http://trac.sagemath.org/8784 for details.
  quit_sage()
sage:
```

----
New commits:


---

Comment by mjo created at 2022-01-25 22:50:54

Changing status from new to needs_review.


---

Comment by dimpase created at 2022-01-31 13:30:02

Does this mean that `sage-cleaner` may go, too?


---

Comment by mjo created at 2022-01-31 14:48:23

Replying to [comment:8 dimpase]:
> Does this mean that `sage-cleaner` may go, too?

Not yet, although that's another long-term goal of mine. sage-cleaner also cleans up "temporary" files, which it wouldn't have to do if we used the OS's built-in tempfile functions instead of our home-grown `SAGE_TMP`. The first and easiest part of that cleanup is #33213.


---

Comment by mjo created at 2022-02-18 00:31:41

Replying to [comment:8 dimpase]:
> Does this mean that `sage-cleaner` may go, too?

Ok, I actually did this in #33213, which now depends on this ticket.


---

Comment by dimpase created at 2022-03-11 12:41:41

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2022-03-11 12:41:41

OK, looks and tests good.


---

Comment by dimpase created at 2022-03-11 12:42:15

perhaps you want to rebase on the latest beta


---

Comment by git created at 2022-03-11 13:48:11

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. This was a forced push. New commits:


---

Comment by git created at 2022-03-11 13:48:11

Changing status from positive_review to needs_review.


---

Comment by dimpase created at 2022-03-29 10:28:37

oops, overlooked this, sorry. Looks good.


---

Comment by dimpase created at 2022-03-29 10:28:37

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2022-04-02 10:53:24

Resolution: fixed


---

Comment by mkoeppe created at 2022-04-17 19:43:47

Follow up in #33706.


---

Comment by dimpase created at 2022-07-17 16:44:44

We have a complaint about ipython processes staying alive in a patchbot.
https://groups.google.com/d/msgid/sage-devel/20220717160807.GA13671%40metelu.net

Could it be due to this ticket, perhaps the change for `src/sage/repl/ipython_extension.py`
was an overkill?
