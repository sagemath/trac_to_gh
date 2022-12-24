# Issue 4747: [with patch; needs review] add custom hash function for cusps.

archive/issues_004747.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis speeds up hash(c) for c a cusp by a lot.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4747\n\n",
    "created_at": "2008-12-09T21:59:30Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch; needs review] add custom hash function for cusps.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4747",
    "user": "@williamstein"
}
```
Assignee: @williamstein

This speeds up hash(c) for c a cusp by a lot.

Issue created by migration from https://trac.sagemath.org/ticket/4747





---

archive/issue_comments_035918.json:
```json
{
    "body": "Attachment [trac_4747.patch](tarball://root/attachments/some-uuid/ticket4747/trac_4747.patch) by @williamstein created at 2008-12-09 22:00:17",
    "created_at": "2008-12-09T22:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35918",
    "user": "@williamstein"
}
```

Attachment [trac_4747.patch](tarball://root/attachments/some-uuid/ticket4747/trac_4747.patch) by @williamstein created at 2008-12-09 22:00:17



---

archive/issue_comments_035919.json:
```json
{
    "body": "Patch applies fine and test ok on 32-bit but on 64-bit I get this:\n\n```\nsage -t  \"sage-3.2.1.rc0/devel/sage-hash/sage/modular/cusps.py\"**********************************************************************\nFile \"/home/jec/sage-3.2.1.rc0/devel/sage-hash/sage/modular/cusps.py\", line 319:\n    sage: hash(Cusp(1/3))\nExpected:\n    3713081631933328131    \nGot:\n    163512108431620420\n**********************************************************************\nFile \"/home/jec/sage-3.2.1.rc0/devel/sage-hash/sage/modular/cusps.py\", line 322:\n    sage: hash(Cusp(oo))\nExpected:\n    3713081631936575706    \nGot:\n    6982220252595711780\n**********************************************************************\n```\n\n\nI am amazed at the effect this has on the speed.  Hashing is not something I ever think about, but clearly I should!",
    "created_at": "2008-12-09T22:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35919",
    "user": "@JohnCremona"
}
```

Patch applies fine and test ok on 32-bit but on 64-bit I get this:

```
sage -t  "sage-3.2.1.rc0/devel/sage-hash/sage/modular/cusps.py"**********************************************************************
File "/home/jec/sage-3.2.1.rc0/devel/sage-hash/sage/modular/cusps.py", line 319:
    sage: hash(Cusp(1/3))
Expected:
    3713081631933328131    
Got:
    163512108431620420
**********************************************************************
File "/home/jec/sage-3.2.1.rc0/devel/sage-hash/sage/modular/cusps.py", line 322:
    sage: hash(Cusp(oo))
Expected:
    3713081631936575706    
Got:
    6982220252595711780
**********************************************************************
```


I am amazed at the effect this has on the speed.  Hashing is not something I ever think about, but clearly I should!



---

archive/issue_comments_035920.json:
```json
{
    "body": "John -- is there any chance you forgot to do a `sage -b` before testing this patch? I'm only suspicious because the incorrect values getting returned are exactly the values that `hash(Cusp(1/3))` and `hash(Cusp(oo))` returned **before** the patch ...",
    "created_at": "2008-12-14T08:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35920",
    "user": "@craigcitro"
}
```

John -- is there any chance you forgot to do a `sage -b` before testing this patch? I'm only suspicious because the incorrect values getting returned are exactly the values that `hash(Cusp(1/3))` and `hash(Cusp(oo))` returned **before** the patch ...



---

archive/issue_comments_035921.json:
```json
{
    "body": "Replying to [comment:2 craigcitro]:\n> John -- is there any chance you forgot to do a `sage -b` before testing this patch? I'm only suspicious because the incorrect values getting returned are exactly the values that `hash(Cusp(1/3))` and `hash(Cusp(oo))` returned **before** the patch ...\n\nMay be.  I'll try again.",
    "created_at": "2008-12-14T11:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35921",
    "user": "@JohnCremona"
}
```

Replying to [comment:2 craigcitro]:
> John -- is there any chance you forgot to do a `sage -b` before testing this patch? I'm only suspicious because the incorrect values getting returned are exactly the values that `hash(Cusp(1/3))` and `hash(Cusp(oo))` returned **before** the patch ...

May be.  I'll try again.



---

archive/issue_comments_035922.json:
```json
{
    "body": "William was right.  Sorry!",
    "created_at": "2008-12-14T14:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35922",
    "user": "@JohnCremona"
}
```

William was right.  Sorry!



---

archive/issue_comments_035923.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-14T17:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35923",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035924.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc0",
    "created_at": "2008-12-14T17:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35924",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.rc0



---

archive/issue_comments_035925.json:
```json
{
    "body": "This patch causes the following doctest failures:\n\n```\nsage -t -long \"devel/sage/sage/modular/congroup.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/modular/congroup.py\", line 540, in __main__.example_25\nFailed example:\n    Gamma0(Integer(36)).cusps()###line 514:_sage_    >>> Gamma0(36).cusps()\nExpected:\n    {1/6, 1/4, 1/3, 1/2, 1/9, 0, 1/18, 5/12, Infinity, 1/12, 2/3, 5/6}\nGot:\n    {1/2, 0, 1/3, 1/12, 5/6, 5/12, 1/4, 1/18, 1/6, 1/9, 2/3, Infinity}\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/modular/congroup.py\", line 1064, in __main__.example_48\nFailed example:\n    Gamma1(Integer(5))._find_cusps()###line 1283:_sage_    >>> Gamma1(5)._find_cusps()Expected:\n    {0, Infinity, 1/2, 2/5}\nGot:    {0, 1/2, Infinity, 2/5}\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/modular/congroup.py\", line 1066, in __main__.example_48\nFailed example:\n    Gamma1(Integer(35))._find_cusps()###line 1285:_sage_    >>> Gamma1(35)._find_cusps()\nExpected:\n    {3/35, 9/10, 9/14, 11/35, 3/14, 9/35, 3/10, 11/14, 8/35, 4/7, 8/15, Infinity, 13/14, 16/35, 13/35, 0, 4/15, 1/13, 2/35, 1/11, 1/10, 1/17, 1/1\n6, 1/15, 1/14, 1/7, 1/6, 1/5, 1/4, 1/3, 1/2, 6/35, 1/9, 1/8, 6/7, 3/5, 3/7, 7/10, 4/35, 2/5, 17/35, 2/7, 5/7, 1/12, 4/5, 5/14, 12/35, 2/15}\nGot:\n    {4/7, 1/3, 3/35, 16/35, 1/17, 1/15, 6/35, 1/6, 11/14, 3/7, 2/5, 1/11, 4/35, 3/14, 1/2, 6/7, 3/10, 1/14, 1/5, 2/35, 7/10, 5/7, 1/10, 8/15, 0, \n9/14, 13/35, 4/5, 1/13, 1/4, 11/35, 9/10, 1/9, 8/35, Infinity, 12/35, 3/5, 2/7, 1/12, 13/14, 4/15, 9/35, 5/14, 1/8, 17/35, 1/7, 2/15, 1/16}\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/modular/congroup.py\", line 1397, in __main__.example_65\nFailed example:\n    Gamma0(Integer(90))._find_cusps()###line 1681:_sage_    >>> Gamma0(90)._find_cusps()\nExpected:\n    {1/6, 1/5, 1/3, 1/2, 11/30, 1/9, 2/3, 1/30, Infinity, 5/6, 1/45, 0, 1/18, 1/10, 1/15, 2/15}\nGot:\n    {0, 1/3, 11/30, 5/6, 1/15, 1/10, 2/3, 1/9, Infinity, 1/2, 1/45, 1/18, 1/5, 2/15, 1/6, 1/30}\n**********************************************************************\n```\n\n\nThoughts? \n\nCheers,\n\nMichael",
    "created_at": "2008-12-14T18:14:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35925",
    "user": "mabshoff"
}
```

This patch causes the following doctest failures:

```
sage -t -long "devel/sage/sage/modular/congroup.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/modular/congroup.py", line 540, in __main__.example_25
Failed example:
    Gamma0(Integer(36)).cusps()###line 514:_sage_    >>> Gamma0(36).cusps()
Expected:
    {1/6, 1/4, 1/3, 1/2, 1/9, 0, 1/18, 5/12, Infinity, 1/12, 2/3, 5/6}
Got:
    {1/2, 0, 1/3, 1/12, 5/6, 5/12, 1/4, 1/18, 1/6, 1/9, 2/3, Infinity}
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/modular/congroup.py", line 1064, in __main__.example_48
Failed example:
    Gamma1(Integer(5))._find_cusps()###line 1283:_sage_    >>> Gamma1(5)._find_cusps()Expected:
    {0, Infinity, 1/2, 2/5}
Got:    {0, 1/2, Infinity, 2/5}
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/modular/congroup.py", line 1066, in __main__.example_48
Failed example:
    Gamma1(Integer(35))._find_cusps()###line 1285:_sage_    >>> Gamma1(35)._find_cusps()
Expected:
    {3/35, 9/10, 9/14, 11/35, 3/14, 9/35, 3/10, 11/14, 8/35, 4/7, 8/15, Infinity, 13/14, 16/35, 13/35, 0, 4/15, 1/13, 2/35, 1/11, 1/10, 1/17, 1/1
6, 1/15, 1/14, 1/7, 1/6, 1/5, 1/4, 1/3, 1/2, 6/35, 1/9, 1/8, 6/7, 3/5, 3/7, 7/10, 4/35, 2/5, 17/35, 2/7, 5/7, 1/12, 4/5, 5/14, 12/35, 2/15}
Got:
    {4/7, 1/3, 3/35, 16/35, 1/17, 1/15, 6/35, 1/6, 11/14, 3/7, 2/5, 1/11, 4/35, 3/14, 1/2, 6/7, 3/10, 1/14, 1/5, 2/35, 7/10, 5/7, 1/10, 8/15, 0, 
9/14, 13/35, 4/5, 1/13, 1/4, 11/35, 9/10, 1/9, 8/35, Infinity, 12/35, 3/5, 2/7, 1/12, 13/14, 4/15, 9/35, 5/14, 1/8, 17/35, 1/7, 2/15, 1/16}
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/modular/congroup.py", line 1397, in __main__.example_65
Failed example:
    Gamma0(Integer(90))._find_cusps()###line 1681:_sage_    >>> Gamma0(90)._find_cusps()
Expected:
    {1/6, 1/5, 1/3, 1/2, 11/30, 1/9, 2/3, 1/30, Infinity, 5/6, 1/45, 0, 1/18, 1/10, 1/15, 2/15}
Got:
    {0, 1/3, 11/30, 5/6, 1/15, 1/10, 2/3, 1/9, Infinity, 1/2, 1/45, 1/18, 1/5, 2/15, 1/6, 1/30}
**********************************************************************
```


Thoughts? 

Cheers,

Michael



---

archive/issue_comments_035926.json:
```json
{
    "body": "Reopened for now due to non-trivial doctest failure.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-14T18:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35926",
    "user": "mabshoff"
}
```

Reopened for now due to non-trivial doctest failure.

Cheers,

Michael



---

archive/issue_comments_035927.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-12-14T18:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35927",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_035928.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-12-14T18:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35928",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_035929.json:
```json
{
    "body": "Replying to [comment:8 mabshoff]:\nThe change in hash function means that sets of cusps will be ordered differently.  I'll check visually that the sets have not changed;  assuming that is the case I'll just adjust the doctests to agree with the new output order.",
    "created_at": "2008-12-14T18:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35929",
    "user": "@JohnCremona"
}
```

Replying to [comment:8 mabshoff]:
The change in hash function means that sets of cusps will be ordered differently.  I'll check visually that the sets have not changed;  assuming that is the case I'll just adjust the doctests to agree with the new output order.



---

archive/issue_comments_035930.json:
```json
{
    "body": "Attachment [trac-4747-doctest.patch](tarball://root/attachments/some-uuid/ticket4747/trac-4747-doctest.patch) by @JohnCremona created at 2008-12-14 19:10:14",
    "created_at": "2008-12-14T19:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35930",
    "user": "@JohnCremona"
}
```

Attachment [trac-4747-doctest.patch](tarball://root/attachments/some-uuid/ticket4747/trac-4747-doctest.patch) by @JohnCremona created at 2008-12-14 19:10:14



---

archive/issue_comments_035931.json:
```json
{
    "body": "New patch fixes the problem.",
    "created_at": "2008-12-14T19:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35931",
    "user": "@JohnCremona"
}
```

New patch fixes the problem.



---

archive/issue_comments_035932.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-12-14T19:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35932",
    "user": "@craigcitro"
}
```

Looks good.



---

archive/issue_comments_035933.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-14T20:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35933",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035934.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc0",
    "created_at": "2008-12-14T20:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4747#issuecomment-35934",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.rc0
