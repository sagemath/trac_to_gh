# Issue 9490: Doctest failure of sage/sage/libs/galrep/wrapper.pyx on t2.math (Solaris 10 SPARC)

Issue created by migration from https://trac.sagemath.org/ticket/9490

Original creator: drkirkby

Original creation time: 2010-07-13 14:18:12

Assignee: mvngu

CC:  jhpalmieri justin cremona rlm

## Hardware + software
 * Sun T5240 with two T2+ UltraSPARC processors
 * 2 CPUS = 16 cores = 128 hardware threads 
 * 1167 MHz
 * 32 GB RAM
 * Solaris 10 update 7 (5/09)
 * sage-4.5.rc0 with:
  * A library patch from #7379
  * An ECL patch from #9187
 * gcc 4.4.1 configured to use the Sun linker and Sun assembler. 

## The problem
John Palmieri built Sage and run the long doctests. After inspecting Joh's ptestlong.log, I find the following test fails, even if run from the command line, and with SAGE_TIMEOUT_LONG increased to 10,000 seconds, which ensures there are no timeouts (around 3600 seconds should be sufficient on 't2.math' for SAGE_TIMEOUT_LONG)


```
sage -t -long "devel/sage/sage/libs/galrep/wrapper.pyx"     


------------------------------------------------------------
Unhandled SIGBUS: A bus error occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------


	 [18.0 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage/sage/libs/galrep/wrapper.pyx"
Total time for all tests: 18.0 seconds
```



---

Comment by drkirkby created at 2010-07-13 15:00:01

See also #9445, where Justin reports a failure (though not a crash) of this test on OS X. 

Dave


---

Comment by jhpalmieri created at 2010-07-13 15:33:40

When I reran the test using "sage -t -long -verbose ...", I got this:

```
sage -t -long -verbose "devel/sage/sage/libs/galrep/wrapper.pyx"
Trying:
    set_random_seed(0L)
Expecting nothing
ok
Trying:
    change_warning_output(sys.stdout)
Expecting nothing
ok
Trying:
    set_random_seed(0L)
Expecting nothing
ok
Trying:
    change_warning_output(sys.stdout)
Expecting nothing
ok
Trying:
    set_random_seed(0L)
Expecting nothing
ok
Trying:
    change_warning_output(sys.stdout)
Expecting nothing
ok
Trying:
    galrep.GalRep()###line 50:_sage_    >>> galrep.GalRep()
Expecting:
    Andrew Sutherland's Probabilistic Image of Galois Algorithm
ok
Trying:
    galrep.GalRep(os.path.join(sage.misc.misc.SAGE_EXTCODE,'galrep','galrep_ecdata.dat'))###line 52:_sage_    >>> galrep.GalRep(os.path.join(sage.misc.misc.SAGE_EXTCODE,'galrep','galrep_ecdata.dat'))
Expecting:
    Andrew Sutherland's Probabilistic Image of Galois Algorithm
ok
Trying:
    set_random_seed(0L)
Expecting nothing
ok
Trying:
    change_warning_output(sys.stdout)
Expecting nothing
ok
Trying:
    galrep.GalRep().mod_ell_image(-Integer(432),Integer(8208),Integer(3))###line 84:_sage_    >>> galrep.GalRep().mod_ell_image(-432,8208,3)
Expecting:
    0


------------------------------------------------------------
Unhandled SIGBUS: A bus error occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------

         [15.8 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long -verbose "devel/sage/sage/libs/galrep/wrapper.pyx"

```



---

Comment by drkirkby created at 2010-07-21 12:54:53

Resolution: fixed


---

Comment by drkirkby created at 2010-07-21 12:54:53

This can be closed, it was a patch (#8617) new to the 4.5 series which caused this problem, and Robert removed it before releasing 4.5. So this fortunately never appeared in a Sage release. 

Using sage-4.5.1 on a Sun Blade 1000 (dual 900 MHz UltraSPARC III+, 2 GB RAM), I get:


```
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 24542.2 seconds

drkirkby@redstart:~/sage-4.5.1$ uname -a
SunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000
drkirkby@redstart:~/sage-4.5.1$ cat /etc/release
                         Solaris 10 3/05 s10_74L2a SPARC
           Copyright 2005 Sun Microsystems, Inc.  All Rights Reserved.
                        Use is subject to license terms.
                            Assembled 22 January 2005
drkirkby@redstart:~/sage-4.5.1$ 
```

