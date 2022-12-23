# Issue 9309: Add an spkg-check file for the IML library

Issue created by migration from https://trac.sagemath.org/ticket/9309

Original creator: drkirkby

Original creation time: 2010-06-22 14:41:47

Assignee: tbd

CC:  leif jhpalmieri pjeremy

The IML library is one of the many standard packages in Sage (see #9281 for a list), which do not have a spkg-check file. This means that if one builds Sage with the environment variable SAGE_CHECK set to "yes", no self-tests of the package will be run. This is silly, as the IML library has a test suite, though it only consists of two tests. 

After adding the required file, the test suite is run. 


```
creating test-largeentry
PASS: test-smallentry
PASS: test-largeentry
==================
All 2 tests passed
==================
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src/tests'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src/tests'
Making check in examples
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src/examples'
make[1]: Nothing to be done for `check'.
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src/examples'
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src'
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing iml-1.0.1.p13.spkg
```



---

Attachment

Mercurial patch to add an spkg-check file to enable self-tests


---

Comment by drkirkby created at 2010-06-22 14:59:46

The package can be found here

http://boxen.math.washington.edu/home/kirkby/patches/iml-1.0.1.p13.spkg


---

Comment by drkirkby created at 2010-06-22 14:59:46

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-07-16 15:07:22

Since you three tend to take quality quite seriously, I'll cc you!

Dave


---

Comment by malb created at 2010-07-21 16:08:53

Changing status from needs_review to positive_review.


---

Comment by malb created at 2010-07-21 16:08:53

The patch looks okay. I also tested in on sage.math.


---

Comment by leif created at 2010-07-21 16:33:32

(Dave:) Shouldn't we improve this spkg like we did with the new GSL one (at #9533)? (I must admit I haven't yet looked at its `spkg-install`. If you don't want to spend further time on it, I could do it, say, until this weekend. Then you'd have to review it - or Martin again...)

I would at least add a message reporting that the test suite passed, and append to `CFLAGS` et al. rather than overwrite them (if `SAGE64=yes`).


---

Comment by leif created at 2010-07-21 16:54:18

Replying to [comment:4 leif]:
> (Dave:) Shouldn't we improve this spkg like we did with the new GSL one (at #9533)? [...]

Obviously this would be out of the ticket's current scope, so we could equally well open a new one for that purpose instead.


---

Comment by leif created at 2010-07-21 17:07:32

At least [IML's home page](http://www.cs.uwaterloo.ca/~astorjoh/iml.html) has moved (the one in `SPKG.txt` gives a 404). From there:

  What is New?

  * 2008-07-28 The current release is 1.0.3. This version incorporates a new function nullspaceMP into the library interface which computes the right nullspace of an integer matrix filled with GMP bignums.
 
  * 2007-09-14 The current release is 1.0.2. This version corrects several bugs.

  * 2006-11-26 The current release is 1.0.1. This version corrects several bugs as well as incorporates a new function nullspaceLong into the library interface which computes the right nullspace of an integer matrix with type long.

  [...]

So perhaps really worth a follow-up ticket... (But we should update the address in `SPKG.txt` _here_ I think.)

Martin, what do _you_ think?


---

Comment by malb created at 2010-07-21 17:23:50

Sure, let's do both: update SPKG.txt here and then update to the newest upstream release in a different package.


---

Comment by leif created at 2010-07-21 17:49:02

Only updates upstream info in SPKG.txt


---

Attachment

Dave, can you merge my patch to `SPKG.txt`?


---

Comment by drkirkby created at 2010-07-21 22:22:49

Replying to [comment:8 leif]:
> Dave, can you merge my patch to `SPKG.txt`?

Leif, 

I copied your changes to SPKG.txt to the package at: 

http://boxen.math.washington.edu/home/kirkby/patches/iml-1.0.1.p13.spkg

I also created #9568 to update the IML library, and improve spkg-install. We should also consider whether that can be built in parallel. Anyway, leave any comments on #9568. 

 == Note to the release managers == 

No patches need to be applied to any other Sage repositories - all changes are merged into the repository. Just replace the current IML package with this one.

http://boxen.math.washington.edu/home/kirkby/patches/iml-1.0.1.p13.spkg

Dave


---

Comment by mpatel created at 2010-08-09 09:35:14

Resolution: fixed
