# Issue 875: further work needed on frast Sage --> PARI int conversion

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-13 06:22:51

Assignee: somebody


```
22:42 < cwitty_> I was looking at #467, and I just crashed SAGE with a PARI stack overflow.
22:43 < cwitty_> I thought the stack was supposed to resize automatically, or something?  (Or at least
                 not crash SAGE.)
22:44 < cwitty_> sage: n = 10^10000000
22:44 < cwitty_> sage: %time _ = pari(n)
22:44 < cwitty_>   ***   the PARI stack overflows !
22:44 < cwitty_>   current stack size: 8000000 (7.629 Mbytes)
22:44 < cwitty_>   [hint] you can increase GP stack with allocatemem()
22:44 < cwitty_> /home/cwitty/sage/local/bin/sage-sage: line 205: 25703 Aborted
                 sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$`@`"
22:44 < cwitty_> (This is after I applied the patch from #467.)
22:45 < williamstein> weird.
22:45 < williamstein> it should automatically double *if* the author correctly uses _sig_on/_sig_off
22:47 < cwitty_> This is the ZZ->Pari fast coercion patch, and I'm pretty sure (from skimming the patch)
                 that he never touches _sig_on/_sig_off.  So that's probably it.
```


*THE SOLUTION*

Need to move code for _pari_c to gen.pyx as a method off of the Pari object.
Then wrap the call to the function in convert.c in _sig_on / _sig_off.
The _sig_on / _sig_off macros are specially constructed *only* in gen.pyx 
to automatically double the pari stack if we run out of memory.


---

Comment by craigcitro created at 2007-10-13 15:20:00

Changing status from new to assigned.


---

Comment by craigcitro created at 2007-10-13 15:20:00

Changing assignee from somebody to craigcitro.


---

Comment by was created at 2007-10-20 22:15:17

Changing type from defect to enhancement.


---

Comment by craigcitro created at 2007-10-27 08:07:19

This patch fixes the problem above, and adds a doctest about it. It took a bit of fiddling to get this to work -- the point is that you need to load the Integer type in order to make this work in gen.pyx, but you can't do that at compile time (it would be a circular dependency). This is further compounded by the fact that the code in gen.pyx actually gets *used* in the process of loading other parts of the Sage library -- that is, you create and use Sage's PariInstance in the process of loading various modules, so things had to be touched up in a few places to get things to load.

Also, re: William's note above about "hacking the Python/C API" -- that's not for this patch, that's for the upcoming patch on ticket 864. That might have to wait until 2.9 at the rate our new versions are coming these days, though. ;)


---

Attachment


---

Comment by cwitty created at 2007-10-27 19:45:45

Resolution: fixed
