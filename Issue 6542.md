# Issue 6542: tachyon ouput seems broken in sage-4.1

Issue created by migration from https://trac.sagemath.org/ticket/6542

Original creator: mhampton

Original creation time: 2009-07-16 11:49:09

Assignee: was

CC:  kcrisman wstein boothby mvngu

Keywords: graphics, tachyon, raytracer

As part of tracking this down, I am planning on adding doctests to more of the tachyon related files, which currently have low coverage.


---

Comment by mvngu created at 2009-07-16 11:52:15

This problem was raised in this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/12104b9aec94c758) thread.


---

Comment by mhampton created at 2009-07-16 14:38:47

This might have been broken by 6269 or 6372.  At any rate, the tostr function in tachyon.py is now missing a crucial piece.  I am working on a patch.


---

Comment by mhampton created at 2009-07-16 18:19:55

fixes a mistaken deletion of critical functionality in tachyon's tostr function


---

Attachment

The patch fixes a mistaken deletion of critical functionality in tachyon's tostr function.  Looks like a piece of this function was sliced off by mistake during the colorsys refactoring.

I will open a seperate ticket to improve the tachyon doctests; I think this patch should go in ASAP since tachyon is totally broken without it.


---

Comment by mhampton created at 2009-07-16 18:22:09

Changing priority from major to blocker.


---

Comment by kcrisman created at 2009-07-16 18:37:08

This happened during the rebasing of #6372, moving the tachyon stuff.  Perhaps this is a warning against restoring positive reviews immediately upon rebase, or perhaps not.  In any case, the current patch needs a doctest to catch this - currently the function returns None every time this is called on a non-string, and that is probably why things didn't get caught before.


---

Comment by mhampton created at 2009-07-16 19:13:30

Well, yeah - the whole damn file needs doctests, which will take a while.  But I really think this should be fixed as soon as possible.

I made ticket #6543 to fix the lack of doctests; that can build on this patch.


---

Comment by kcrisman created at 2009-07-16 19:22:33

Replying to [comment:5 mhampton]:
> Well, yeah - the whole damn file needs doctests, which will take a while.  But I really think this should be fixed as soon as possible.
True; I just meant to add a string with doctest that 

```
tostr([5,4,3])
' 5.0 4.0 3.0 '
```

as per Sage convention to check that it was fixed; that shouldn't be too bad.  I'd do it myself but do not have a current Sage build available.
> I made ticket #6543 to fix the lack of doctests; that can build on this patch.
Yes, I've been thinking about doing this for a while too.


---

Attachment

new version with doctest


---

Comment by mhampton created at 2009-07-16 20:07:18

OK, I added a doctest to the tostr function.


---

Comment by kcrisman created at 2009-07-17 13:07:06

The function itself (obviously, since just replaces from before) works fine for me as is, and the documentation works fine in testing.  Unfortunately, I can't currently merge it in a Sage build and do a test run, so needs further review to ensure that.  This should be REALLY EASY to do for anyone who has a current Sage 4.1.


---

Comment by mhampton created at 2009-07-23 03:21:23

Changing assignee from was to mhampton.


---

Comment by timdumol created at 2009-07-27 09:22:28

Works perfectly for me -- Sage 4.1.


---

Comment by mvngu created at 2009-07-27 13:19:34

Typo in the word "seperated" on line 990:

```
-Converts vector information to a space-seperated string.
+Converts vector information to a space-separated string.
```



---

Comment by mvngu created at 2009-07-29 11:12:52

Resolution: fixed
