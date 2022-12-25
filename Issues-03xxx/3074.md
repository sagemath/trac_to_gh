# Issue 3074: [with spkg, positive review] Cyton 0.9.6.14 released

archive/issues_003074.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis contains all the changes in the latest spkg, as well as better unicode handling (mostly irrelevant for Sage), optimized append method, and the ability to declare cdef variable as python builtin types (list, dict, etc.) \n\nSpkg up at http://sage.math.washington.edu/home/robertwb/cython/\n\nIssue created by migration from https://trac.sagemath.org/ticket/3074\n\n",
    "closed_at": "2008-05-02T16:16:23Z",
    "created_at": "2008-05-01T21:42:01Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "[with spkg, positive review] Cyton 0.9.6.14 released",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3074",
    "user": "https://github.com/robertwb"
}
```
Assignee: mabshoff

This contains all the changes in the latest spkg, as well as better unicode handling (mostly irrelevant for Sage), optimized append method, and the ability to declare cdef variable as python builtin types (list, dict, etc.) 

Spkg up at http://sage.math.washington.edu/home/robertwb/cython/

Issue created by migration from https://trac.sagemath.org/ticket/3074





---

archive/issue_comments_021169.json:
```json
{
    "body": "Hi Robert,\n\nI am curious about the supposed repo status. In the spkg we have an unclean state:\n\n```\n! .hgtags\n! Demos/callback/Makefile\n! Demos/callback/Makefile.nodistutils\n! Demos/callback/README.txt\n! Demos/callback/Setup.py\n! Demos/callback/cheesefinder.c\n! Demos/callback/cheesefinder.h\n! Demos/callback/run_cheese.py\n! Demos/embed/Makefile\n! Demos/embed/Makefile.msc\n! Demos/embed/Makefile.msc.static\n! Demos/embed/Makefile.unix\n! Demos/embed/README\n! Demos/embed/embedded.pyx\n! Demos/embed/main.c\n! Demos/pyprimes.py\n! Demos/run_numeric_demo.py\n! Demos/run_primes.py\n! Demos/run_spam.py\n! bin/update_references\n! tests/compile/altet1.pyx.BROKEN\n! tests/compile/belchenko2.pyx.BROKEN\n! tests/compile/burton1.pyx.BROKEN\n! tests/compile/getattr3ref.pyx.BROKEN\n! tests/compile/hinsen1.pyx.BROKEN\n? Cython/Compiler/Lexicon.pickle\n? Demos/api.pyx\n? Demos/api2.pxd\n? Demos/append.pyx\n? Demos/builtin_types.pyx\n? Demos/public_enums.pyx\n? Demos/repr.pyx\n? Demos/weakref.pxd\n? Demos/weakref.pyx\n? Demos/weakref2.pyx\n? PKG-INFO\n? tests/run/public_enums.pyx\n```\nSo: we can either nuke the .hg repo from the spkg or clean it up. It is your call :).\n\nProvided Sage builds and doctests fine I will merge this spkg even with the slightly dirty repo since going back to a clean upstream is more important than some odd repo state IMHO.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-02T15:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3074#issuecomment-21169",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Robert,

I am curious about the supposed repo status. In the spkg we have an unclean state:

```
! .hgtags
! Demos/callback/Makefile
! Demos/callback/Makefile.nodistutils
! Demos/callback/README.txt
! Demos/callback/Setup.py
! Demos/callback/cheesefinder.c
! Demos/callback/cheesefinder.h
! Demos/callback/run_cheese.py
! Demos/embed/Makefile
! Demos/embed/Makefile.msc
! Demos/embed/Makefile.msc.static
! Demos/embed/Makefile.unix
! Demos/embed/README
! Demos/embed/embedded.pyx
! Demos/embed/main.c
! Demos/pyprimes.py
! Demos/run_numeric_demo.py
! Demos/run_primes.py
! Demos/run_spam.py
! bin/update_references
! tests/compile/altet1.pyx.BROKEN
! tests/compile/belchenko2.pyx.BROKEN
! tests/compile/burton1.pyx.BROKEN
! tests/compile/getattr3ref.pyx.BROKEN
! tests/compile/hinsen1.pyx.BROKEN
? Cython/Compiler/Lexicon.pickle
? Demos/api.pyx
? Demos/api2.pxd
? Demos/append.pyx
? Demos/builtin_types.pyx
? Demos/public_enums.pyx
? Demos/repr.pyx
? Demos/weakref.pxd
? Demos/weakref.pyx
? Demos/weakref2.pyx
? PKG-INFO
? tests/run/public_enums.pyx
```
So: we can either nuke the .hg repo from the spkg or clean it up. It is your call :).

Provided Sage builds and doctests fine I will merge this spkg even with the slightly dirty repo since going back to a clean upstream is more important than some odd repo state IMHO.

Cheers,

Michael



---

archive/issue_events_006948.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-02T15:00:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3074",
    "milestone": "sage-3.0.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3074#event-6948"
}
```



---

archive/issue_comments_021170.json:
```json
{
    "body": "The spkg builds fine, Sage does rebuild and doctests fine. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-02T16:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3074#issuecomment-21170",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg builds fine, Sage does rebuild and doctests fine. Positive review.

Cheers,

Michael



---

archive/issue_events_006949.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-02T16:16:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3074",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3074#event-6949"
}
```



---

archive/issue_comments_021171.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-02T16:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3074#issuecomment-21171",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021172.json:
```json
{
    "body": "Merged in Sage 3.0.1.rc0",
    "created_at": "2008-05-02T16:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3074#issuecomment-21172",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.rc0



---

archive/issue_comments_021173.json:
```json
{
    "body": "I think this is due to a difference in the MANIFEST file vs. the files tracked by hg. (I did python setup.py sdist and then made the spkg from that). I'll be sure to clean it up before the next release, but it shouldn't affect anything. Thanks for pointing this out.",
    "created_at": "2008-05-02T20:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3074#issuecomment-21173",
    "user": "https://github.com/robertwb"
}
```

I think this is due to a difference in the MANIFEST file vs. the files tracked by hg. (I did python setup.py sdist and then made the spkg from that). I'll be sure to clean it up before the next release, but it shouldn't affect anything. Thanks for pointing this out.
