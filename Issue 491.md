# Issue 491: gcc 4.3: fix givaro build due to ::memcpy failure

archive/issues_000491.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe givaro spkg released with Sage 2.8.2 doesn't compile with gcc 4.3:\n\n```\nMaking all in memory\nmake[4]: Entering directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src/src/kernel/memory'\n/bin/sh ../../../libtool --mode=compile g++ -DHAVE_CONFIG_H -I. -I. -I../../.. -I../../.. -I../../../src/kernel/system   -g -O2 -Wall -c givaromm.C\n g++ -DHAVE_CONFIG_H -I. -I. -I../../.. -I../../.. -I../../../src/kernel/system -g -O2 -Wall -c givaromm.C  -fPIC -DPIC -o .libs/givaromm.o\ngivaromm.C: In static member function 'static void* GivMMFreeList::reallocate(void*, size_t, size_t)':\ngivaromm.C:191: error: '::memcpy' has not been declared\ngivaromm.C: In static member function 'static void GivMMFreeList::memcpy(void*, const void*, size_t)':\ngivaromm.C:205: error: '::memcpy' has not been declared\ngivaromm.C: In static member function 'static void* GivMMRefCount::reallocate(void*, size_t, size_t)':\ngivaromm.C:246: error: '::memcpy' has not been declared\ngivaromm.C:247: error: '::memcpy' has not been declared\ngivaromm.C:245: warning: suggest explicit braces to avoid ambiguous 'else'\nmake[4]: *** [givaromm.lo] Error 1\nmake[4]: Leaving directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src/src/kernel/memory'\nmake[3]: *** [all-recursive] Error 1\nmake[3]: Leaving directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src/src/kernel'\nmake[2]: *** [all-recursive] Error 1\nmake[2]: Leaving directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src/src'\nmake[1]: *** [all-recursive] Error 1\nmake[1]: Leaving directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src'\nmake: *** [all-recursive-am] Error 2\n```\nIncluding string.h in givaromm.C fixes the problem. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/491\n\n",
    "closed_at": "2007-12-06T21:02:46Z",
    "created_at": "2007-08-25T23:16:18Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "gcc 4.3: fix givaro build due to ::memcpy failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/491",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The givaro spkg released with Sage 2.8.2 doesn't compile with gcc 4.3:

```
Making all in memory
make[4]: Entering directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src/src/kernel/memory'
/bin/sh ../../../libtool --mode=compile g++ -DHAVE_CONFIG_H -I. -I. -I../../.. -I../../.. -I../../../src/kernel/system   -g -O2 -Wall -c givaromm.C
 g++ -DHAVE_CONFIG_H -I. -I. -I../../.. -I../../.. -I../../../src/kernel/system -g -O2 -Wall -c givaromm.C  -fPIC -DPIC -o .libs/givaromm.o
givaromm.C: In static member function 'static void* GivMMFreeList::reallocate(void*, size_t, size_t)':
givaromm.C:191: error: '::memcpy' has not been declared
givaromm.C: In static member function 'static void GivMMFreeList::memcpy(void*, const void*, size_t)':
givaromm.C:205: error: '::memcpy' has not been declared
givaromm.C: In static member function 'static void* GivMMRefCount::reallocate(void*, size_t, size_t)':
givaromm.C:246: error: '::memcpy' has not been declared
givaromm.C:247: error: '::memcpy' has not been declared
givaromm.C:245: warning: suggest explicit braces to avoid ambiguous 'else'
make[4]: *** [givaromm.lo] Error 1
make[4]: Leaving directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src/src/kernel/memory'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src/src/kernel'
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src/src'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/spkg/build/givaro-3.2.6.p1/src'
make: *** [all-recursive-am] Error 2
```
Including string.h in givaromm.C fixes the problem. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/491





---

archive/issue_comments_002445.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2007-08-25T23:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/491#issuecomment-2445",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_002446.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-25T23:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/491#issuecomment-2446",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002447.json:
```json
{
    "body": "Another suggestion has been made by Patrick Pelissier:\n\n```\nFor checking of givaro inside the configure, as a work-around,\nI suggest including cstdio explicitly before gmp.h.\n```\nThis supposedly will not require workarounds for the gmp.h\n\nCheers,\n\nMichael",
    "created_at": "2007-08-26T12:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/491#issuecomment-2447",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Another suggestion has been made by Patrick Pelissier:

```
For checking of givaro inside the configure, as a work-around,
I suggest including cstdio explicitly before gmp.h.
```
This supposedly will not require workarounds for the gmp.h

Cheers,

Michael



---

archive/issue_comments_002448.json:
```json
{
    "body": "Fix in the new spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/givaro-3.2.6.p4.spkg\n\nCheers,\n\nMichael",
    "created_at": "2007-12-06T21:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/491#issuecomment-2448",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fix in the new spkg at

http://sage.math.washington.edu/home/mabshoff/givaro-3.2.6.p4.spkg

Cheers,

Michael



---

archive/issue_events_001254.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-06T21:02:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/491",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/491#event-1254"
}
```



---

archive/issue_comments_002449.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-06T21:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/491#issuecomment-2449",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002450.json:
```json
{
    "body": "Merged in 2.9.alpha1.",
    "created_at": "2007-12-06T21:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/491#issuecomment-2450",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.alpha1.



---

archive/issue_events_001255.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-06T21:02:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/491",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/491#event-1255"
}
```
