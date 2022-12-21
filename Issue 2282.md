# Issue 2282: [with link to spkg, needs review] readline currently not building dynamic library on Mac

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-02-23 22:14:53

Assignee: craigcitro

Currently, readline fails to build a dynamic library on Mac, and the sage installer doesn't notice this at all. Once this happens, other things (notably Pari) can't find readline, and know not to build against the system-wide fake readline (Mac ships a pseudo-readline for licensing reasons). Pari then doesn't have readline support, and is annoying to use. Luckily, there was a fix on the [FAQ](http://www.ufr-mi.u-bordeaux.fr/~belabas/pari/doc/faq.html#mac10readline:Pari), which I've added to our spkg-install for readline when we're on a Mac. 

So there are really two things I've changed:

 * Add the fix for building readline (this involves changing `dynamic` to 
 `dynamiclib` in the generated Makefile)
 * Change `-o` to `-a` in `spkg-install`: this is why we weren't noticing that
 readline failed to build.

Of course, I don't know why it was `-o` instead of `-a` in the first place: if there was a good reason for that, someone should let me know and I'll change it back in the non-Mac case.




---

Comment by craigcitro created at 2008-02-23 22:20:05

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-02-23 22:20:05

Forgot to post a link to the spkg:

 . [http://sage.math.washington.edu/home/citro/patches/readline-5.2.p1.spkg](http://sage.math.washington.edu/home/citro/patches/readline-5.2.p1.spkg)

Also, I failed with entering a link to the Pari FAQ above, it should be to

 . [http://www.ufr-mi.u-bordeaux.fr/~belabas/pari/doc/faq.html#mac10readline](http://www.ufr-mi.u-bordeaux.fr/~belabas/pari/doc/faq.html#mac10readline)


---

Comment by was created at 2008-02-23 22:32:52

Awesome!  I'm so glad you tracked this down since it was driving me nuts. 

I've tested this spkg and it works perfectly.  The description of the fix
sounds reasonable to me, I guess.  So positive review.  I hope mabshoff will
look more closely at spkg-install and see if it makes sense to him. 

Thanks!!


---

Comment by cwitty created at 2008-02-23 22:38:33

The spkg works for me (install the spkg, force-install pari, check to make sure readline works for both gp and sage) on both bsd.math.washington.edu (OSX, where gp+readline was previously broken) and on my 32-bit x86 Linux box.


---

Comment by mabshoff created at 2008-02-24 19:18:50

Merged in Sage 2.10.3.alpha0


---

Comment by mabshoff created at 2008-02-24 19:18:50

Resolution: fixed
