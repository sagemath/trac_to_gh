# Issue 9490: Doctest failure of sage/sage/libs/galrep/wrapper.pyx on t2.math (Solaris 10 SPARC)

archive/issues_009490.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  jhpalmieri justin cremona rlm\n\n## Hardware + software\n* Sun T5240 with two T2+ UltraSPARC processors\n* 2 CPUS = 16 cores = 128 hardware threads \n* 1167 MHz\n* 32 GB RAM\n* Solaris 10 update 7 (5/09)\n* sage-4.5.rc0 with:\n  * A library patch from #7379\n  * An ECL patch from #9187\n* gcc 4.4.1 configured to use the Sun linker and Sun assembler. \n\n## The problem\nJohn Palmieri built Sage and run the long doctests. After inspecting Joh's ptestlong.log, I find the following test fails, even if run from the command line, and with SAGE_TIMEOUT_LONG increased to 10,000 seconds, which ensures there are no timeouts (around 3600 seconds should be sufficient on 't2.math' for SAGE_TIMEOUT_LONG)\n\n\n```\nsage -t -long \"devel/sage/sage/libs/galrep/wrapper.pyx\"     \n\n\n------------------------------------------------------------\nUnhandled SIGBUS: A bus error occurred in Sage.\nThis probably occurred because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n\n\n\t [18.0 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long \"devel/sage/sage/libs/galrep/wrapper.pyx\"\nTotal time for all tests: 18.0 seconds\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9490\n\n",
    "created_at": "2010-07-13T14:18:12Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Doctest failure of sage/sage/libs/galrep/wrapper.pyx on t2.math (Solaris 10 SPARC)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9490",
    "user": "drkirkby"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/9490





---

archive/issue_comments_091108.json:
```json
{
    "body": "See also #9445, where Justin reports a failure (though not a crash) of this test on OS X. \n\nDave",
    "created_at": "2010-07-13T15:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9490#issuecomment-91108",
    "user": "drkirkby"
}
```

See also #9445, where Justin reports a failure (though not a crash) of this test on OS X. 

Dave



---

archive/issue_comments_091109.json:
```json
{
    "body": "When I reran the test using \"sage -t -long -verbose ...\", I got this:\n\n```\nsage -t -long -verbose \"devel/sage/sage/libs/galrep/wrapper.pyx\"\nTrying:\n    set_random_seed(0L)\nExpecting nothing\nok\nTrying:\n    change_warning_output(sys.stdout)\nExpecting nothing\nok\nTrying:\n    set_random_seed(0L)\nExpecting nothing\nok\nTrying:\n    change_warning_output(sys.stdout)\nExpecting nothing\nok\nTrying:\n    set_random_seed(0L)\nExpecting nothing\nok\nTrying:\n    change_warning_output(sys.stdout)\nExpecting nothing\nok\nTrying:\n    galrep.GalRep()###line 50:_sage_    >>> galrep.GalRep()\nExpecting:\n    Andrew Sutherland's Probabilistic Image of Galois Algorithm\nok\nTrying:\n    galrep.GalRep(os.path.join(sage.misc.misc.SAGE_EXTCODE,'galrep','galrep_ecdata.dat'))###line 52:_sage_    >>> galrep.GalRep(os.path.join(sage.misc.misc.SAGE_EXTCODE,'galrep','galrep_ecdata.dat'))\nExpecting:\n    Andrew Sutherland's Probabilistic Image of Galois Algorithm\nok\nTrying:\n    set_random_seed(0L)\nExpecting nothing\nok\nTrying:\n    change_warning_output(sys.stdout)\nExpecting nothing\nok\nTrying:\n    galrep.GalRep().mod_ell_image(-Integer(432),Integer(8208),Integer(3))###line 84:_sage_    >>> galrep.GalRep().mod_ell_image(-432,8208,3)\nExpecting:\n    0\n\n\n------------------------------------------------------------\nUnhandled SIGBUS: A bus error occurred in Sage.\nThis probably occurred because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n\n         [15.8 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long -verbose \"devel/sage/sage/libs/galrep/wrapper.pyx\"\n\n```\n",
    "created_at": "2010-07-13T15:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9490#issuecomment-91109",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_091110.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T12:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9490#issuecomment-91110",
    "user": "drkirkby"
}
```

Resolution: fixed



---

archive/issue_comments_091111.json:
```json
{
    "body": "This can be closed, it was a patch (#8617) new to the 4.5 series which caused this problem, and Robert removed it before releasing 4.5. So this fortunately never appeared in a Sage release. \n\nUsing sage-4.5.1 on a Sun Blade 1000 (dual 900 MHz UltraSPARC III+, 2 GB RAM), I get:\n\n\n```\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 24542.2 seconds\n\ndrkirkby@redstart:~/sage-4.5.1$ uname -a\nSunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000\ndrkirkby@redstart:~/sage-4.5.1$ cat /etc/release\n                         Solaris 10 3/05 s10_74L2a SPARC\n           Copyright 2005 Sun Microsystems, Inc.  All Rights Reserved.\n                        Use is subject to license terms.\n                            Assembled 22 January 2005\ndrkirkby@redstart:~/sage-4.5.1$ \n```\n",
    "created_at": "2010-07-21T12:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9490#issuecomment-91111",
    "user": "drkirkby"
}
```

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

