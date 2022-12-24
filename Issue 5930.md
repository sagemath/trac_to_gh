# Issue 5930: switch from maxima to pynac for core symbolic manipulation system

archive/issues_005930.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  burcin\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5930\n\n",
    "created_at": "2009-04-29T01:52:44Z",
    "labels": [
        "algebra",
        "blocker",
        "enhancement"
    ],
    "title": "switch from maxima to pynac for core symbolic manipulation system",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5930",
    "user": "was"
}
```
Assignee: tbd

CC:  burcin



Issue created by migration from https://trac.sagemath.org/ticket/5930





---

archive/issue_comments_046883.json:
```json
{
    "body": "Changing component from algebra to symbolics.",
    "created_at": "2009-05-05T09:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46883",
    "user": "burcin"
}
```

Changing component from algebra to symbolics.



---

archive/issue_comments_046884.json:
```json
{
    "body": "Bug/Issue:  Control-C doesn't work in some cases. \n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: var('x,y,z')\n(x, y, z)\nsage: time f = (x+y+z)^5\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\nsage: g = f*(f+1)\nsage: timeit('g.expand()')\n5 loops, best of 3: 53.2 ms per loop\nsage: %prun g.expand()\n         8890 function calls in 0.069 CPU seconds\n| Sage Version 3.4.2, Release Date: 2009-05-05                       |\n| Type notebook() for the GUI, and license() for information.        |\n   Ordered by: internal time\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n        1    0.065    0.065    0.069    0.069 {method 'expand' of 'sage.symbolic.expression.Expression' objects}\n     8863    0.003    0.000    0.003    0.000 functional.py:393(imag)\n        1    0.000    0.000    0.069    0.069 <string>:1(<module>)\n        4    0.000    0.000    0.000    0.000 arith.py:1140(gcd)\n        4    0.000    0.000    0.000    0.000 {method 'lcm' of 'sage.structure.element.PrincipalIdealDomainElement' objects}\n        4    0.000    0.000    0.000    0.000 arith.py:1256(lcm)\n        4    0.000    0.000    0.000    0.000 {method 'gcd' of 'sage.rings.integer.Integer' objects}\n        8    0.000    0.000    0.000    0.000 {hasattr}\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n\nsage: %prun v = [g.expand() for _ in range(1000)]\n^CException exceptions.KeyboardInterrupt: KeyboardInterrupt() in 'sage.symbolic.pynac.py_is_real' ignored\n^CException exceptions.KeyboardInterrupt: KeyboardInterrupt() in 'sage.symbolic.pynac.py_is_real' ignored\n^CException exceptions.KeyboardInterrupt: KeyboardInterrupt() in 'sage.symbolic.pynac.py_is_real' ignored\n```\n",
    "created_at": "2009-05-07T16:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46884",
    "user": "was"
}
```

Bug/Issue:  Control-C doesn't work in some cases. 

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: var('x,y,z')
(x, y, z)
sage: time f = (x+y+z)^5
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: g = f*(f+1)
sage: timeit('g.expand()')
5 loops, best of 3: 53.2 ms per loop
sage: %prun g.expand()
         8890 function calls in 0.069 CPU seconds
| Sage Version 3.4.2, Release Date: 2009-05-05                       |
| Type notebook() for the GUI, and license() for information.        |
   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.065    0.065    0.069    0.069 {method 'expand' of 'sage.symbolic.expression.Expression' objects}
     8863    0.003    0.000    0.003    0.000 functional.py:393(imag)
        1    0.000    0.000    0.069    0.069 <string>:1(<module>)
        4    0.000    0.000    0.000    0.000 arith.py:1140(gcd)
        4    0.000    0.000    0.000    0.000 {method 'lcm' of 'sage.structure.element.PrincipalIdealDomainElement' objects}
        4    0.000    0.000    0.000    0.000 arith.py:1256(lcm)
        4    0.000    0.000    0.000    0.000 {method 'gcd' of 'sage.rings.integer.Integer' objects}
        8    0.000    0.000    0.000    0.000 {hasattr}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

sage: %prun v = [g.expand() for _ in range(1000)]
^CException exceptions.KeyboardInterrupt: KeyboardInterrupt() in 'sage.symbolic.pynac.py_is_real' ignored
^CException exceptions.KeyboardInterrupt: KeyboardInterrupt() in 'sage.symbolic.pynac.py_is_real' ignored
^CException exceptions.KeyboardInterrupt: KeyboardInterrupt() in 'sage.symbolic.pynac.py_is_real' ignored
```




---

archive/issue_comments_046885.json:
```json
{
    "body": "There is a sequence of *serious* speed regressions that I think Burcin caused by changes to the pynac spkg:\n\nIN SAGE-3.2 we get OK timings for this benchmarks.  They aren't great, but I can live with them, since it is\"only\" 57 times slower than Singular:\n\n```\nsage: var('x,y,z', ns=1); f = (x+y+z)^6;\nsage: timeit('(f*(f+1)).expand()')\n125 loops, best of 3: 3.25 ms per loop\n```\n\n\nIn Singular:\n\n```\nsage: R.<x,y,z> = QQ[]\nsage: timeit('g=(x+y+z)^6*((x+y+z)^6+1)')\n625 loops, best of 3: 56.3 \u00b5s per loop\nsage: 3250/56.3\n57.7264653641208\n```\n\n\nIt's hard to tell, but Mathematica seems to take about 1.7ms, which is comparable to the above:\n\n```\nsage: timeit(\"s=mathematica('Expand[(x+y+z)^6*((x+y+z)^6+1)]')\")\n125 loops, best of 3: 1.81 ms per loop\nsage: timeit(\"s=mathematica('2+3')\")\n625 loops, best of 3: 125 \u00b5s per loop\n```\n\n\nMaxima via Sage takes about 61 ms, since I guess (c)lisp is slow, etc.:\n\n```\nsage: timeit(\"s=maxima('expand((x+y+z)^6*((x+y+z)^6+1))')\")\n5 loops, best of 3: 61.8 ms per loop\n```\n\n\nFirst there was a MAJOR unacceptable speed regression going to sage-3.3 (this is probably all caused by the pynac spkg).  The timing jumped all the way to 42ms, so now it's almost as bad as Maxima:\n\n```\nsage: var('x,y,z', ns=1); f = (x+y+z)^6\n(x, y, z)\nsage: timeit('(f*(f+1)).expand()')\n5 loops, best of 3: 42.1 ms per loop\n```\n\n\nIn fact, directly in sage-3.2 with old Maxima symbolics:\n\n```\nsage: var('x,y,z', ns=0); f = (x+y+z)^6\nsage: timeit('(f*(f+1)).expand()')\n5 loops, best of 3: 106 ms per loop\n```\n\n\n\nIN SAGE-3.4.2 with new symbolics:\n\n```\nsage: var('x,y,z', ns=1); f = (x+y+z)^6\n(x, y, z)\nsage: timeit('(f*(f+1)).expand()')\n5 loops, best of 3: 206 ms per loop\n```\n\n\nThis may be due to a change in the pynac layer, where it is calling out to Python for some reason, even though it shouldn't need to.   206ms is really unacceptable.  It's much slower than Maxima itself, it's 63 times slower than Pynac *was* just a few months ago, and it's 367 times slower than Singular.",
    "created_at": "2009-05-07T17:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46885",
    "user": "was"
}
```

There is a sequence of *serious* speed regressions that I think Burcin caused by changes to the pynac spkg:

IN SAGE-3.2 we get OK timings for this benchmarks.  They aren't great, but I can live with them, since it is"only" 57 times slower than Singular:

```
sage: var('x,y,z', ns=1); f = (x+y+z)^6;
sage: timeit('(f*(f+1)).expand()')
125 loops, best of 3: 3.25 ms per loop
```


In Singular:

```
sage: R.<x,y,z> = QQ[]
sage: timeit('g=(x+y+z)^6*((x+y+z)^6+1)')
625 loops, best of 3: 56.3 µs per loop
sage: 3250/56.3
57.7264653641208
```


It's hard to tell, but Mathematica seems to take about 1.7ms, which is comparable to the above:

```
sage: timeit("s=mathematica('Expand[(x+y+z)^6*((x+y+z)^6+1)]')")
125 loops, best of 3: 1.81 ms per loop
sage: timeit("s=mathematica('2+3')")
625 loops, best of 3: 125 µs per loop
```


Maxima via Sage takes about 61 ms, since I guess (c)lisp is slow, etc.:

```
sage: timeit("s=maxima('expand((x+y+z)^6*((x+y+z)^6+1))')")
5 loops, best of 3: 61.8 ms per loop
```


First there was a MAJOR unacceptable speed regression going to sage-3.3 (this is probably all caused by the pynac spkg).  The timing jumped all the way to 42ms, so now it's almost as bad as Maxima:

```
sage: var('x,y,z', ns=1); f = (x+y+z)^6
(x, y, z)
sage: timeit('(f*(f+1)).expand()')
5 loops, best of 3: 42.1 ms per loop
```


In fact, directly in sage-3.2 with old Maxima symbolics:

```
sage: var('x,y,z', ns=0); f = (x+y+z)^6
sage: timeit('(f*(f+1)).expand()')
5 loops, best of 3: 106 ms per loop
```



IN SAGE-3.4.2 with new symbolics:

```
sage: var('x,y,z', ns=1); f = (x+y+z)^6
(x, y, z)
sage: timeit('(f*(f+1)).expand()')
5 loops, best of 3: 206 ms per loop
```


This may be due to a change in the pynac layer, where it is calling out to Python for some reason, even though it shouldn't need to.   206ms is really unacceptable.  It's much slower than Maxima itself, it's 63 times slower than Pynac *was* just a few months ago, and it's 367 times slower than Singular.



---

archive/issue_comments_046886.json:
```json
{
    "body": "I've attached symbolics_final2.patch which applies on top of #5777.  This patch also requires the Pynac 0.1.7 spkg at http://sage.math.washington.edu/home/mhansen/pynac-0.1.7.spkg",
    "created_at": "2009-05-19T04:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46886",
    "user": "mhansen"
}
```

I've attached symbolics_final2.patch which applies on top of #5777.  This patch also requires the Pynac 0.1.7 spkg at http://sage.math.washington.edu/home/mhansen/pynac-0.1.7.spkg



---

archive/issue_comments_046887.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-19T04:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46887",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046888.json:
```json
{
    "body": "Changing assignee from tbd to mhansen.",
    "created_at": "2009-05-19T04:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46888",
    "user": "mhansen"
}
```

Changing assignee from tbd to mhansen.



---

archive/issue_comments_046889.json:
```json
{
    "body": "After applying the first patch, the second fails.  This is to clean 4.0.alpha0:\n\n\n```\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/5930/symbolics_final2.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5930/symbolics_final2.patch\nLoading: [..................................................]\ncd \"/Users/wstein/build/sage-4.0.alpha0/devel/sage\" && hg status\ncd \"/Users/wstein/build/sage-4.0.alpha0/devel/sage\" && hg status\ncd \"/Users/wstein/build/sage-4.0.alpha0/devel/sage\" && hg import   \"/Users/wstein/.sage/temp/teragon.local/1113/tmp_2.patch\"\napplying /Users/wstein/.sage/temp/teragon.local/1113/tmp_2.patch\npatching file doc/en/constructions/calculus.rst\nHunk #5 FAILED at 141\n1 out of 10 hunks FAILED -- saving rejects to file doc/en/constructions/calculus.rst.rej\npatching file sage/calculus/calculus.py\nHunk #15 FAILED at 291\n1 out of 25 hunks FAILED -- saving rejects to file sage/calculus/calculus.py.rej\npatching file sage/quadratic_forms/quadratic_form__mass__Conway_Sloane_masses.py\nHunk #1 succeeded at 4 with fuzz 2 (offset 0 lines).\npatching file sage/symbolic/function.pyx\nHunk #9 FAILED at 206\n1 out of 25 hunks FAILED -- saving rejects to file sage/symbolic/function.pyx.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2009-05-19T20:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46889",
    "user": "was"
}
```

After applying the first patch, the second fails.  This is to clean 4.0.alpha0:


```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/5930/symbolics_final2.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5930/symbolics_final2.patch
Loading: [..................................................]
cd "/Users/wstein/build/sage-4.0.alpha0/devel/sage" && hg status
cd "/Users/wstein/build/sage-4.0.alpha0/devel/sage" && hg status
cd "/Users/wstein/build/sage-4.0.alpha0/devel/sage" && hg import   "/Users/wstein/.sage/temp/teragon.local/1113/tmp_2.patch"
applying /Users/wstein/.sage/temp/teragon.local/1113/tmp_2.patch
patching file doc/en/constructions/calculus.rst
Hunk #5 FAILED at 141
1 out of 10 hunks FAILED -- saving rejects to file doc/en/constructions/calculus.rst.rej
patching file sage/calculus/calculus.py
Hunk #15 FAILED at 291
1 out of 25 hunks FAILED -- saving rejects to file sage/calculus/calculus.py.rej
patching file sage/quadratic_forms/quadratic_form__mass__Conway_Sloane_masses.py
Hunk #1 succeeded at 4 with fuzz 2 (offset 0 lines).
patching file sage/symbolic/function.pyx
Hunk #9 FAILED at 206
1 out of 25 hunks FAILED -- saving rejects to file sage/symbolic/function.pyx.rej
abort: patch failed to apply
```




---

archive/issue_comments_046890.json:
```json
{
    "body": "Replying to [comment:11 was]:\n> After applying the first patch, the second fails.  This is to clean 4.0.alpha0:\n\nThis patch set is on top of last night's 4.0.rc0 merge tree and will not work with 4.0.a0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T20:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46890",
    "user": "mabshoff"
}
```

Replying to [comment:11 was]:
> After applying the first patch, the second fails.  This is to clean 4.0.alpha0:

This patch set is on top of last night's 4.0.rc0 merge tree and will not work with 4.0.a0.

Cheers,

Michael



---

archive/issue_comments_046891.json:
```json
{
    "body": "symbolics_final2.patch does not import:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-4.0.rc0/devel/sage$ hg import symbolics_final1.patch\napplying symbolics_final1.patch\nmabshoff@sage:/scratch/mabshoff/sage-4.0.rc0/devel/sage$ hg import symbolics_final2.patch\napplying symbolics_final2.patch\npatching file sage/symbolic/function.pyx\nHunk #9 FAILED at 206\n1 out of 25 hunks FAILED -- saving rejects to file sage/symbolic/function.pyx.rej\nabort: patch failed to apply\nmabshoff@sage:/scratch/mabshoff/sage-4.0.rc0/devel/sage$ less sage/symbolic/function.pyx.rej\n```\n\nI have not touched the file that sees rejects since Mike pulled it last night, so please fix this :)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T20:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46891",
    "user": "mabshoff"
}
```

symbolics_final2.patch does not import:

```
mabshoff@sage:/scratch/mabshoff/sage-4.0.rc0/devel/sage$ hg import symbolics_final1.patch
applying symbolics_final1.patch
mabshoff@sage:/scratch/mabshoff/sage-4.0.rc0/devel/sage$ hg import symbolics_final2.patch
applying symbolics_final2.patch
patching file sage/symbolic/function.pyx
Hunk #9 FAILED at 206
1 out of 25 hunks FAILED -- saving rejects to file sage/symbolic/function.pyx.rej
abort: patch failed to apply
mabshoff@sage:/scratch/mabshoff/sage-4.0.rc0/devel/sage$ less sage/symbolic/function.pyx.rej
```

I have not touched the file that sees rejects since Mike pulled it last night, so please fix this :)

Cheers,

Michael



---

archive/issue_comments_046892.json:
```json
{
    "body": "Attachment [symbolics_final2.patch](tarball://root/attachments/some-uuid/ticket5930/symbolics_final2.patch) by mhansen created at 2009-05-19 23:02:16",
    "created_at": "2009-05-19T23:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46892",
    "user": "mhansen"
}
```

Attachment [symbolics_final2.patch](tarball://root/attachments/some-uuid/ticket5930/symbolics_final2.patch) by mhansen created at 2009-05-19 23:02:16



---

archive/issue_comments_046893.json:
```json
{
    "body": "Ok, the latest patch applies, but lacks a commit message.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T23:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46893",
    "user": "mabshoff"
}
```

Ok, the latest patch applies, but lacks a commit message.

Cheers,

Michael



---

archive/issue_comments_046894.json:
```json
{
    "body": "The spkg needs work:\n\n```\nconfigure: creating ./config.statusConfiguration of GiNaC 0.1.5 done. Now type \"make\".\n /bin/sh ./config.status\nconfig.status: creating Makefileconfig.status: creating pynac.spec\nconfig.status: creating pynac.pcconfig.status: creating ginac/Makefile\nconfig.status: creating ginac/version.h\nconfig.status: creating config.hconfig.status: config.h is unchanged\nconfig.status: executing depfiles commandscd . && /bin/sh /home/mabshoff/build-4.0.alpha0/sage-4.0.alpha0-cleo-system/spkg/build/pynac-0.1.7/src/missing --run autoheader\naclocal.m4:20: warning: this file was generated for autoconf 2.61.\nYou have another version of autoconf.  It may work, but is not guaranteed to.If you have problems, you may need to regenerate the build system entirely.\nTo do so, use the procedure documented by the package, typically `autoreconf'.configure.ac:26: error: Autoconf version 2.60 or higher is required\naclocal.m4:7127: AM_INIT_AUTOMAKE is expanded from...\nconfigure.ac:26: the top levelautom4te: /usr/bin/m4 failed with exit status: 63\nautoheader: /usr/bin/autom4te failed with exit status: 63\n```\n\nAll this autocrap should never be run in the spkg. The version number as well as the name of the library is also wrong.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T01:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46894",
    "user": "mabshoff"
}
```

The spkg needs work:

```
configure: creating ./config.statusConfiguration of GiNaC 0.1.5 done. Now type "make".
 /bin/sh ./config.status
config.status: creating Makefileconfig.status: creating pynac.spec
config.status: creating pynac.pcconfig.status: creating ginac/Makefile
config.status: creating ginac/version.h
config.status: creating config.hconfig.status: config.h is unchanged
config.status: executing depfiles commandscd . && /bin/sh /home/mabshoff/build-4.0.alpha0/sage-4.0.alpha0-cleo-system/spkg/build/pynac-0.1.7/src/missing --run autoheader
aclocal.m4:20: warning: this file was generated for autoconf 2.61.
You have another version of autoconf.  It may work, but is not guaranteed to.If you have problems, you may need to regenerate the build system entirely.
To do so, use the procedure documented by the package, typically `autoreconf'.configure.ac:26: error: Autoconf version 2.60 or higher is required
aclocal.m4:7127: AM_INIT_AUTOMAKE is expanded from...
configure.ac:26: the top levelautom4te: /usr/bin/m4 failed with exit status: 63
autoheader: /usr/bin/autom4te failed with exit status: 63
```

All this autocrap should never be run in the spkg. The version number as well as the name of the library is also wrong.

Cheers,

Michael



---

archive/issue_comments_046895.json:
```json
{
    "body": "I've been reading through the megabyte patch, and testing every function that's been touched.  I'd estimate my coverage of the file to be about 20%, and I made sure to bounce around a bunch (that is, I didn't just read the top or bottom 20%).  I didn't look at many corner cases, because I was trying to test as much as I could, and it often takes thought to come up with good corner cases.  In the end, I found some things that Maxima crashed on when it tried to simplify, like \n\n```\n exp(sum([log(x^(1/n)) for n in range(1,1000)]))\n```\n\nbut other than that, I found the entire system to be stable and useful.  In a lot of easy cases, it's *much* faster than before, which makes me happy.",
    "created_at": "2009-05-20T04:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46895",
    "user": "boothby"
}
```

I've been reading through the megabyte patch, and testing every function that's been touched.  I'd estimate my coverage of the file to be about 20%, and I made sure to bounce around a bunch (that is, I didn't just read the top or bottom 20%).  I didn't look at many corner cases, because I was trying to test as much as I could, and it often takes thought to come up with good corner cases.  In the end, I found some things that Maxima crashed on when it tried to simplify, like 

```
 exp(sum([log(x^(1/n)) for n in range(1,1000)]))
```

but other than that, I found the entire system to be stable and useful.  In a lot of easy cases, it's *much* faster than before, which makes me happy.



---

archive/issue_comments_046896.json:
```json
{
    "body": "I am doing the following\n\n* install pynac-1.0.17\n* pull in latest changes \n* sage -ba\n* install dsage\n* update pickle jar\n* run testlong\n\non \n\n* Linux x86, x86-64 and Itanium\n* some of the above with gcc 4.4\n* Solaris Sparc (32 bit)\n* OSX 10.4 (PPC)\n\nI am currently running `testlong`, so we should know more in the morning (local time)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T10:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46896",
    "user": "mabshoff"
}
```

I am doing the following

* install pynac-1.0.17
* pull in latest changes 
* sage -ba
* install dsage
* update pickle jar
* run testlong

on 

* Linux x86, x86-64 and Itanium
* some of the above with gcc 4.4
* Solaris Sparc (32 bit)
* OSX 10.4 (PPC)

I am currently running `testlong`, so we should know more in the morning (local time)

Cheers,

Michael



---

archive/issue_comments_046897.json:
```json
{
    "body": "Ok, no joy: On Solaris/Sparc this patchset causes a hang in maxima.py. Mike told me that William and him allegedly fixed the underlying issue (see the discussion about the semicolon at #6054), but it causes the hang. All Maxima related doctests pass on that machine (modulo two tiny numerical noise problems), so the patch on this ticket is to blame.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T13:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46897",
    "user": "mabshoff"
}
```

Ok, no joy: On Solaris/Sparc this patchset causes a hang in maxima.py. Mike told me that William and him allegedly fixed the underlying issue (see the discussion about the semicolon at #6054), but it causes the hang. All Maxima related doctests pass on that machine (modulo two tiny numerical noise problems), so the patch on this ticket is to blame.

Cheers,

Michael



---

archive/issue_comments_046898.json:
```json
{
    "body": "And the failing doctest is this one:\n\n```\nTrying:\n    maxima('2+2')###line 751:_sage_    >>> maxima('2+2')\nExpecting:\n    4\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T13:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46898",
    "user": "mabshoff"
}
```

And the failing doctest is this one:

```
Trying:
    maxima('2+2')###line 751:_sage_    >>> maxima('2+2')
Expecting:
    4
```


Cheers,

Michael



---

archive/issue_comments_046899.json:
```json
{
    "body": "Hmm, this looks suspicious, but reverting it does not fix the problem:\n\n```\n@@ -755,7 +755,7 @@\n         if self._expect is None: return\n         r = randrange(2147483647)\n         s = marker + str(r+1)\n-        cmd = ''';sconcat(\"%s\",(%s+1));\\n'''%(marker,r)\n+        cmd = '''0;sconcat(\"%s\",(%s+1));\\n'''%(marker,r)\n         self._sendstr(cmd)\n         try:\n             self._expect_expr(timeout=0.5)\n```\n\nRunning `maxima('2+2')` in a loop does work, so I am not sure what the problem is yet.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T13:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46899",
    "user": "mabshoff"
}
```

Hmm, this looks suspicious, but reverting it does not fix the problem:

```
@@ -755,7 +755,7 @@
         if self._expect is None: return
         r = randrange(2147483647)
         s = marker + str(r+1)
-        cmd = ''';sconcat("%s",(%s+1));\n'''%(marker,r)
+        cmd = '''0;sconcat("%s",(%s+1));\n'''%(marker,r)
         self._sendstr(cmd)
         try:
             self._expect_expr(timeout=0.5)
```

Running `maxima('2+2')` in a loop does work, so I am not sure what the problem is yet.

Cheers,

Michael



---

archive/issue_comments_046900.json:
```json
{
    "body": "Hmm, another thing:\n\n```\n cdef class Matrix_symbolic_dense(matrix_dense.Matrix_dense):\n     r\"\"\"\n@@ -162,7 +161,7 @@\n             sage: cmp(m,m)\n             0\n             sage: cmp(m,3)\n-            -1\n+            1\n         \"\"\"\n         return self._richcmp(right, op)\n \n```\n\nis cmp() in this case deterministic? \n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T14:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46900",
    "user": "mabshoff"
}
```

Hmm, another thing:

```
 cdef class Matrix_symbolic_dense(matrix_dense.Matrix_dense):
     r"""
@@ -162,7 +161,7 @@
             sage: cmp(m,m)
             0
             sage: cmp(m,3)
-            -1
+            1
         """
         return self._richcmp(right, op)
 
```

is cmp() in this case deterministic? 

Cheers,

Michael



---

archive/issue_comments_046901.json:
```json
{
    "body": "Formal positive review by various other people not me. Followup should be directed to new tickets for 4.0 as long as it is open.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T02:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46901",
    "user": "mabshoff"
}
```

Formal positive review by various other people not me. Followup should be directed to new tickets for 4.0 as long as it is open.

Cheers,

Michael



---

archive/issue_comments_046902.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-21T02:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46902",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_046903.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T02:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46903",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_046904.json:
```json
{
    "body": "See #6111 for refereeing of symbolics.",
    "created_at": "2009-05-21T09:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46904",
    "user": "was"
}
```

See #6111 for refereeing of symbolics.



---

archive/issue_comments_046905.json:
```json
{
    "body": "Does anybody happen to remember why there is this strange condition involving `inspect.ismethod`?\n\n```python\n            import inspect\n            if not hasattr(_the_element,'_fast_callable_') or not inspect.ismethod(_the_element._fast_callable_):\n                # only warn if _the_element is not dynamic\n                from sage.misc.superseded import deprecation\n                deprecation(5930, \"Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you ca\n```\n",
    "created_at": "2017-06-07T12:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46905",
    "user": "jdemeyer"
}
```

Does anybody happen to remember why there is this strange condition involving `inspect.ismethod`?

```python
            import inspect
            if not hasattr(_the_element,'_fast_callable_') or not inspect.ismethod(_the_element._fast_callable_):
                # only warn if _the_element is not dynamic
                from sage.misc.superseded import deprecation
                deprecation(5930, "Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you ca
```




---

archive/issue_comments_046906.json:
```json
{
    "body": "Never mind, that condition was actually added in #2516.",
    "created_at": "2017-06-07T13:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5930",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5930#issuecomment-46906",
    "user": "jdemeyer"
}
```

Never mind, that condition was actually added in #2516.
