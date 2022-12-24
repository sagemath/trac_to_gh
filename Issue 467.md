# Issue 467: asymptotically slow pari integer conversions

archive/issues_000467.json:
```json
{
    "body": "Assignee: somebody\n\nThe conversion function from PARI integers to python longs is asymptotically slow (apparantly quadratic time). This shows up when doing something like `int(some_pari_object)`. Similarly from SAGE integers to PARI integers.\n\nThere are also inconsistencies like (on my machine at home):\n\n\n```\nsage: x = 10^100000\n\nsage: time y = pari(x)\nCPU times: user 1.18 s, sys: 0.01 s, total: 1.19 s\nWall time: 1.26\n\nsage: time z = Integer(y)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.02\n\nsage: time u = int(y)\nCPU times: user 1.94 s, sys: 1.33 s, total: 3.27 s\nWall time: 3.58\n\nsage: time u = int(Integer(y))\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.03\n```\n\n\nnow see the quadratic time:\n\n\n```\nsage: x = 10^1000000\n\nsage: time y = pari(x)\nCPU times: user 105.12 s, sys: 1.26 s, total: 106.38 s\nWall time: 121.86\n\nsage: time z = Integer(y)\nCPU times: user 0.03 s, sys: 0.02 s, total: 0.05 s\nWall time: 0.09\n\nsage: time u = int(y)\nCPU times: user 188.17 s, sys: 145.12 s, total: 333.28 s\nWall time: 364.80\n\nsage: time u = int(Integer(y))\nCPU times: user 0.04 s, sys: 0.02 s, total: 0.06 s\nWall time: 0.07\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/467\n\n",
    "created_at": "2007-08-20T10:40:55Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "asymptotically slow pari integer conversions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/467",
    "user": "dmharvey"
}
```
Assignee: somebody

The conversion function from PARI integers to python longs is asymptotically slow (apparantly quadratic time). This shows up when doing something like `int(some_pari_object)`. Similarly from SAGE integers to PARI integers.

There are also inconsistencies like (on my machine at home):


```
sage: x = 10^100000

sage: time y = pari(x)
CPU times: user 1.18 s, sys: 0.01 s, total: 1.19 s
Wall time: 1.26

sage: time z = Integer(y)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.02

sage: time u = int(y)
CPU times: user 1.94 s, sys: 1.33 s, total: 3.27 s
Wall time: 3.58

sage: time u = int(Integer(y))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.03
```


now see the quadratic time:


```
sage: x = 10^1000000

sage: time y = pari(x)
CPU times: user 105.12 s, sys: 1.26 s, total: 106.38 s
Wall time: 121.86

sage: time z = Integer(y)
CPU times: user 0.03 s, sys: 0.02 s, total: 0.05 s
Wall time: 0.09

sage: time u = int(y)
CPU times: user 188.17 s, sys: 145.12 s, total: 333.28 s
Wall time: 364.80

sage: time u = int(Integer(y))
CPU times: user 0.04 s, sys: 0.02 s, total: 0.06 s
Wall time: 0.07
```



Issue created by migration from https://trac.sagemath.org/ticket/467





---

archive/issue_comments_002320.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-09-14T02:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/467#issuecomment-2320",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_002321.json:
```json
{
    "body": "Changing assignee from somebody to craigcitro.",
    "created_at": "2007-10-10T23:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/467#issuecomment-2321",
    "user": "craigcitro"
}
```

Changing assignee from somebody to craigcitro.



---

archive/issue_comments_002322.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-10T23:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/467#issuecomment-2322",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002323.json:
```json
{
    "body": "So I've fixed half of the above problems, namely the Pari <--> SAGE issues. I'm going to make a patch for the Pari <--> int issues, but since 2.8.7 is imminent, I thought it would be worth getting this posted first. Here's the state of affairs after the first patch:\n\n\n```\nsage: x = 10^100000\n\nsage: time y = pari(x)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n\nsage: time z = Integer(y)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n\nsage: time u = int(y)\nCPU times: user 1.64 s, sys: 1.09 s, total: 2.73 s\nWall time: 2.79\n\nsage: time u = int(Integer(y))\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n\nsage: x = 10^1000000\n\nsage: time y = pari(x)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01\n\nsage: time z = Integer(y)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n\nsage: time u = int(y)\nCPU times: user 220.90 s, sys: 137.34 s, total: 358.24 s\nWall time: 408.11\n\nsage: time u = int(Integer(y))\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01\n\n```\n\n\nThere is a small (20%) improvement on pari --> sage with this patch, and a much larger (at least 5X, up to 7-8X depending on the length of the number) improvement on sage --> pari with this patch. Running y._pari_() with y an element of ZZ is the fastest way to get the corresponding pari element, as pari(y) has just a bit more overhead (it ultimately calls y._pari_() after a few typechecks and whatnot).\n\nThe other ticket (with the pari <--> python long issue) is #864.",
    "created_at": "2007-10-12T19:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/467#issuecomment-2323",
    "user": "craigcitro"
}
```

So I've fixed half of the above problems, namely the Pari <--> SAGE issues. I'm going to make a patch for the Pari <--> int issues, but since 2.8.7 is imminent, I thought it would be worth getting this posted first. Here's the state of affairs after the first patch:


```
sage: x = 10^100000

sage: time y = pari(x)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: time z = Integer(y)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: time u = int(y)
CPU times: user 1.64 s, sys: 1.09 s, total: 2.73 s
Wall time: 2.79

sage: time u = int(Integer(y))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: x = 10^1000000

sage: time y = pari(x)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01

sage: time z = Integer(y)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: time u = int(y)
CPU times: user 220.90 s, sys: 137.34 s, total: 358.24 s
Wall time: 408.11

sage: time u = int(Integer(y))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01

```


There is a small (20%) improvement on pari --> sage with this patch, and a much larger (at least 5X, up to 7-8X depending on the length of the number) improvement on sage --> pari with this patch. Running y._pari_() with y an element of ZZ is the fastest way to get the corresponding pari element, as pari(y) has just a bit more overhead (it ultimately calls y._pari_() after a few typechecks and whatnot).

The other ticket (with the pari <--> python long issue) is #864.



---

archive/issue_comments_002324.json:
```json
{
    "body": "Attachment [convert.hg](tarball://root/attachments/some-uuid/ticket467/convert.hg) by craigcitro created at 2007-10-12 19:49:47",
    "created_at": "2007-10-12T19:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/467#issuecomment-2324",
    "user": "craigcitro"
}
```

Attachment [convert.hg](tarball://root/attachments/some-uuid/ticket467/convert.hg) by craigcitro created at 2007-10-12 19:49:47



---

archive/issue_comments_002325.json:
```json
{
    "body": "This has a serious problem:\n\n```\n22:42 < cwitty_> I was looking at #467, and I just crashed SAGE with a PARI stack overflow.\n22:43 < cwitty_> I thought the stack was supposed to resize automatically, or something?  (Or at least\n                 not crash SAGE.)\n22:44 < cwitty_> sage: n = 10^10000000\n22:44 < cwitty_> sage: %time _ = pari(n)\n22:44 < cwitty_>   ***   the PARI stack overflows !\n22:44 < cwitty_>   current stack size: 8000000 (7.629 Mbytes)\n22:44 < cwitty_>   [hint] you can increase GP stack with allocatemem()\n22:44 < cwitty_> /home/cwitty/sage/local/bin/sage-sage: line 205: 25703 Aborted\n                 sage-ipython -c \"$SAGE_STARTUP_COMMAND;\" \"$@\"\n22:44 < cwitty_> (This is after I applied the patch from #467.)\n22:45 < williamstein> weird.\n22:45 < williamstein> it should automatically double *if* the author correctly uses _sig_on/_sig_off\n22:47 < cwitty_> This is the ZZ->Pari fast coercion patch, and I'm pretty sure (from skimming the patch)\n                 that he never touches _sig_on/_sig_off.  So that's probably it.\n\n```\n\n\nSee trac #",
    "created_at": "2007-10-13T06:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/467#issuecomment-2325",
    "user": "was"
}
```

This has a serious problem:

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
                 sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$@"
22:44 < cwitty_> (This is after I applied the patch from #467.)
22:45 < williamstein> weird.
22:45 < williamstein> it should automatically double *if* the author correctly uses _sig_on/_sig_off
22:47 < cwitty_> This is the ZZ->Pari fast coercion patch, and I'm pretty sure (from skimming the patch)
                 that he never touches _sig_on/_sig_off.  So that's probably it.

```


See trac #



---

archive/issue_comments_002326.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T06:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/467#issuecomment-2326",
    "user": "was"
}
```

Resolution: fixed
