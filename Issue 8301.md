# Issue 8301: segfault in m4ri

archive/issues_008301.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @malb boothby\n\nType in\n\n```\nsage: b = random_matrix(GF(2),4,200); b[3] = b[0]; b.rank()\n```\n\nand get an absolutely stupendous segfault!\n\nFor the first time ever I finally get to use GF(2) matrix algebra for some actually interesting number theory research.  So I wrote a program that creates some fairly simple GF(2) matrices (using modular symbols), and tried the first somewhat nontrivial thing (computing the rank of a 4xn matrix) and got segfaults.  This is on 64-bit Ubuntu Linux.  Yikes.   So:\n\n1. These need to get fixed, obviously.\n\n2. Is there an easy way to completely turn off m4ri?  Seeing how easily it fell over, I don't trust it, and though it is fast I definitely want to rerun all my calculations m4ri free once I have everything setup.  These are calculations for a published paper that will play a key role in a \"proof by computer\" of a potentially important result in number theory.  \n\nRegarding 2, here is a way that I seem to be able to get a matrix mod n dense, and I can then compute the rank, which in this case uses linbox, and is probably fast enough for my application:\n\n```\nsage: c = sage.matrix.matrix_modn_dense.Matrix_modn_dense(b.parent(),b.list(),False,True)\nsage: c.rank()\n3\nsage: timeit('c.rank()')\n625 loops, best of 3: 534 ns per loop\nsage: timeit('c._clear_cache(); c.rank()')\n625 loops, best of 3: 161 \u00b5s per loop\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8301\n\n",
    "created_at": "2010-02-19T02:21:08Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "segfault in m4ri",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8301",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @malb boothby

Type in

```
sage: b = random_matrix(GF(2),4,200); b[3] = b[0]; b.rank()
```

and get an absolutely stupendous segfault!

For the first time ever I finally get to use GF(2) matrix algebra for some actually interesting number theory research.  So I wrote a program that creates some fairly simple GF(2) matrices (using modular symbols), and tried the first somewhat nontrivial thing (computing the rank of a 4xn matrix) and got segfaults.  This is on 64-bit Ubuntu Linux.  Yikes.   So:

1. These need to get fixed, obviously.

2. Is there an easy way to completely turn off m4ri?  Seeing how easily it fell over, I don't trust it, and though it is fast I definitely want to rerun all my calculations m4ri free once I have everything setup.  These are calculations for a published paper that will play a key role in a "proof by computer" of a potentially important result in number theory.  

Regarding 2, here is a way that I seem to be able to get a matrix mod n dense, and I can then compute the rank, which in this case uses linbox, and is probably fast enough for my application:

```
sage: c = sage.matrix.matrix_modn_dense.Matrix_modn_dense(b.parent(),b.list(),False,True)
sage: c.rank()
3
sage: timeit('c.rank()')
625 loops, best of 3: 534 ns per loop
sage: timeit('c._clear_cache(); c.rank()')
625 loops, best of 3: 161 µs per loop
```



Issue created by migration from https://trac.sagemath.org/ticket/8301





---

archive/issue_comments_073404.json:
```json
{
    "body": "I will take a look ASAP.",
    "created_at": "2010-02-19T11:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73404",
    "user": "https://github.com/malb"
}
```

I will take a look ASAP.



---

archive/issue_comments_073405.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-02-19T15:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73405",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_073406.json:
```json
{
    "body": "I can confirm the bug. A fix is available:\n\n  http://bitbucket.org/malb/m4ri/changeset/dfdd4bce3eac/\n\nI will make a new SPKG tomorrow-ish.",
    "created_at": "2010-02-19T15:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73406",
    "user": "https://github.com/malb"
}
```

I can confirm the bug. A fix is available:

  http://bitbucket.org/malb/m4ri/changeset/dfdd4bce3eac/

I will make a new SPKG tomorrow-ish.



---

archive/issue_comments_073407.json:
```json
{
    "body": "A new SPKG is available at:\n\n   http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100221.spkg\n\nFWIW, I just ran\n\n```python\nsage: for i in range(10^4):\n    b = random_matrix(GF(2),4,200); b[3] = b[0]\n    c = sage.matrix.matrix_modn_dense.Matrix_modn_dense(b.parent(),b.list(),False,True)\n    assert(b.rank() == c.rank())\n....:\n```\n\nwithout errors.",
    "created_at": "2010-02-21T13:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73407",
    "user": "https://github.com/malb"
}
```

A new SPKG is available at:

   http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100221.spkg

FWIW, I just ran

```python
sage: for i in range(10^4):
    b = random_matrix(GF(2),4,200); b[3] = b[0]
    c = sage.matrix.matrix_modn_dense.Matrix_modn_dense(b.parent(),b.list(),False,True)
    assert(b.rank() == c.rank())
....:
```

without errors.



---

archive/issue_comments_073408.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-21T13:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73408",
    "user": "https://github.com/malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073409.json:
```json
{
    "body": "Time comparisons:\n\n\n```python\nsage: timeit('c._clear_cache(); c.rank()')\n625 loops, best of 3: 181 \u00b5s per loop\n\nsage: timeit('b._clear_cache(); b.rank()')\n625 loops, best of 3: 8 \u00b5s per loop\n```\n",
    "created_at": "2010-02-21T13:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73409",
    "user": "https://github.com/malb"
}
```

Time comparisons:


```python
sage: timeit('c._clear_cache(); c.rank()')
625 loops, best of 3: 181 µs per loop

sage: timeit('b._clear_cache(); b.rank()')
625 loops, best of 3: 8 µs per loop
```




---

archive/issue_comments_073410.json:
```json
{
    "body": "Tom Boothby will referee this...",
    "created_at": "2010-02-23T18:41:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73410",
    "user": "https://github.com/williamstein"
}
```

Tom Boothby will referee this...



---

archive/issue_comments_073411.json:
```json
{
    "body": "Tom, do think you can referee this for the next release? I've linked to the *only* changeset above for this new SPKG everything else is identical to the current one. So it should be an easy review",
    "created_at": "2010-03-20T12:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73411",
    "user": "https://github.com/malb"
}
```

Tom, do think you can referee this for the next release? I've linked to the *only* changeset above for this new SPKG everything else is identical to the current one. So it should be an easy review



---

archive/issue_comments_073412.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-21T15:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73412",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073413.json:
```json
{
    "body": "Sorry this took so long.  Works for me.",
    "created_at": "2010-03-21T15:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73413",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Sorry this took so long.  Works for me.



---

archive/issue_comments_073414.json:
```json
{
    "body": "I can't build this on one of the skynet machines:\n\n```\niras     ia64-Linux-suse\n\n$ uname -a\nLinux iras 2.6.16.46-0.12-default #1 SMP Thu May 17 14:00:09 UTC 2007 ia64 ia64 ia64 GNU/Linux\n```\n\nI get this:\n\n```\nmake[2]: Entering directory `/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/li\\\nbm4ri-20100221/src'\nCDPATH=\"${ZSH_VERSION+.}:\" && cd . && /bin/sh /home/palmieri/iras/sage-4.4.alph\\\na1x/spkg/build/libm4ri-20100221/src/missing --run aclocal-1.11\n/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/libm4ri-20100221/src/missing: l\\\nine 54: aclocal-1.11: command not found\nWARNING: `aclocal-1.11' is missing on your system.  You should only need it if\n         you modified `acinclude.m4' or `configure.ac'.  You might want\n         to install the `Automake' and `Perl' packages.  Grab them from\n         any GNU archive site.\n cd . && /bin/sh /home/palmieri/iras/sage-4.4.alpha1x/spkg/build/libm4ri-201002\\\n21/src/missing --run automake-1.11 --gnu\n/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/libm4ri-20100221/src/missing: l\\\nine 54: automake-1.11: command not found\nWARNING: `automake-1.11' is missing on your system.  You should only need it if\n         you modified `Makefile.am', `acinclude.m4' or `configure.ac'.\n         You might want to install the `Automake' and `Perl' packages.\n         Grab them from any GNU archive site.\nCDPATH=\"${ZSH_VERSION+.}:\" && cd . && /bin/sh /home/palmieri/iras/sage-4.4.alph\\\na1x/spkg/build/libm4ri-20100221/src/missing --run autoconf\n/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/libm4ri-20100221/src/missing: l\\\nine 54: autoconf: command not found\nWARNING: `autoconf' is missing on your system.  You should only need it if\n         you modified `configure.ac'.  You might want to install the\n         `Autoconf' and `GNU m4' packages.  Grab them from any GNU\n         archive site.\n/bin/sh ./config.status --recheck\nrunning CONFIG_SHELL=/bin/sh /bin/sh ./configure --prefix=/home/palmieri/iras/s\\\nage-4.4.alpha1x/local --includedir=/home/palmieri/iras/sage-4.4.alpha1x/local/i\\\nnclude/ CC=gcc CFLAGS= -I/home/palmieri/iras/sage-4.4.alpha1x/local/include/ -L\\\n/home/palmieri/iras/sage-4.4.alpha1x/local/lib -g -fPIC -Wall -pedantic  -O2 LD\\\nFLAGS= CPPFLAGS=-I/home/palmieri/iras/sage-4.4.alpha1x/local/include/ --no-crea\\\nte --no-recursion\nchecking build system type... ia64-unknown-linux-gnu\nchecking host system type... ia64-unknown-linux-gnu\nchecking for a BSD-compatible install... /usr/bin/install -c\nchecking whether build environment is sane... configure: error: newly created f\\\nile is older than distributed files!\nCheck your system clock\nmake[2]: *** [config.status] Error 1\nmake[2]: Leaving directory `/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/lib\\\nm4ri-20100221/src'\nError building libm4ri\n```\n\nI haven't seen this on any other platform.",
    "created_at": "2010-04-20T20:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73414",
    "user": "https://github.com/jhpalmieri"
}
```

I can't build this on one of the skynet machines:

```
iras     ia64-Linux-suse

$ uname -a
Linux iras 2.6.16.46-0.12-default #1 SMP Thu May 17 14:00:09 UTC 2007 ia64 ia64 ia64 GNU/Linux
```

I get this:

```
make[2]: Entering directory `/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/li\
bm4ri-20100221/src'
CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/sh /home/palmieri/iras/sage-4.4.alph\
a1x/spkg/build/libm4ri-20100221/src/missing --run aclocal-1.11
/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/libm4ri-20100221/src/missing: l\
ine 54: aclocal-1.11: command not found
WARNING: `aclocal-1.11' is missing on your system.  You should only need it if
         you modified `acinclude.m4' or `configure.ac'.  You might want
         to install the `Automake' and `Perl' packages.  Grab them from
         any GNU archive site.
 cd . && /bin/sh /home/palmieri/iras/sage-4.4.alpha1x/spkg/build/libm4ri-201002\
21/src/missing --run automake-1.11 --gnu
/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/libm4ri-20100221/src/missing: l\
ine 54: automake-1.11: command not found
WARNING: `automake-1.11' is missing on your system.  You should only need it if
         you modified `Makefile.am', `acinclude.m4' or `configure.ac'.
         You might want to install the `Automake' and `Perl' packages.
         Grab them from any GNU archive site.
CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/sh /home/palmieri/iras/sage-4.4.alph\
a1x/spkg/build/libm4ri-20100221/src/missing --run autoconf
/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/libm4ri-20100221/src/missing: l\
ine 54: autoconf: command not found
WARNING: `autoconf' is missing on your system.  You should only need it if
         you modified `configure.ac'.  You might want to install the
         `Autoconf' and `GNU m4' packages.  Grab them from any GNU
         archive site.
/bin/sh ./config.status --recheck
running CONFIG_SHELL=/bin/sh /bin/sh ./configure --prefix=/home/palmieri/iras/s\
age-4.4.alpha1x/local --includedir=/home/palmieri/iras/sage-4.4.alpha1x/local/i\
nclude/ CC=gcc CFLAGS= -I/home/palmieri/iras/sage-4.4.alpha1x/local/include/ -L\
/home/palmieri/iras/sage-4.4.alpha1x/local/lib -g -fPIC -Wall -pedantic  -O2 LD\
FLAGS= CPPFLAGS=-I/home/palmieri/iras/sage-4.4.alpha1x/local/include/ --no-crea\
te --no-recursion
checking build system type... ia64-unknown-linux-gnu
checking host system type... ia64-unknown-linux-gnu
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... configure: error: newly created f\
ile is older than distributed files!
Check your system clock
make[2]: *** [config.status] Error 1
make[2]: Leaving directory `/home/palmieri/iras/sage-4.4.alpha1x/spkg/build/lib\
m4ri-20100221/src'
Error building libm4ri
```

I haven't seen this on any other platform.



---

archive/issue_comments_073415.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-20T20:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73415",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_073416.json:
```json
{
    "body": "I fixed the issue, tested it on iras and provided a new SPKG (replacing the old one), at:\n\n http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100221.spkg",
    "created_at": "2010-04-20T20:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73416",
    "user": "https://github.com/malb"
}
```

I fixed the issue, tested it on iras and provided a new SPKG (replacing the old one), at:

 http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100221.spkg



---

archive/issue_comments_073417.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-20T20:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73417",
    "user": "https://github.com/malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073418.json:
```json
{
    "body": "All I did was to run 'make' and 'make distclean' on a different machine to fix the timestamps etc.",
    "created_at": "2010-04-20T20:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73418",
    "user": "https://github.com/malb"
}
```

All I did was to run 'make' and 'make distclean' on a different machine to fix the timestamps etc.



---

archive/issue_comments_073419.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-07T23:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73419",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008498.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-08T22:02:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8301#event-8498"
}
```



---

archive/issue_comments_073420.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T22:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73420",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_073421.json:
```json
{
    "body": "Merged [libm4ri-20100221.spkg](http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100221.spkg) in the standard spkg repository.",
    "created_at": "2010-05-08T22:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8301#issuecomment-73421",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [libm4ri-20100221.spkg](http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100221.spkg) in the standard spkg repository.
