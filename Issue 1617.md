# Issue 1617: speed problem when factoring polynoms

archive/issues_001617.json:
```json
{
    "body": "Assignee: @williamstein\n\nThere is a huge speed difference. Any special reasons? A novice user would possibly not understand why!\n\n\n\n\n```\nvar('x,y')\ntime p1=factor(x^99+y^99)\n\nTime: CPU 0.05 s, Wall: 58.43 s\n```\n\n\n\n\n\n```\nR.<x,y> = QQ[]\ntime p2=factor(x^99+y^99)\n\nTime: CPU 0.06 s, Wall: 0.06 s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1617\n\n",
    "created_at": "2007-12-28T22:01:50Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "speed problem when factoring polynoms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1617",
    "user": "@haraldschilly"
}
```
Assignee: @williamstein

There is a huge speed difference. Any special reasons? A novice user would possibly not understand why!




```
var('x,y')
time p1=factor(x^99+y^99)

Time: CPU 0.05 s, Wall: 58.43 s
```





```
R.<x,y> = QQ[]
time p2=factor(x^99+y^99)

Time: CPU 0.06 s, Wall: 0.06 s
```


Issue created by migration from https://trac.sagemath.org/ticket/1617





---

archive/issue_comments_010283.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2007-12-29T04:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1617#issuecomment-10283",
    "user": "mabshoff"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_010284.json:
```json
{
    "body": "This is likely caused by using Maxima's factoring vs. Singular's libfactor. In the first case x and y are symbolic. \n\nCheers,\n\nMichael",
    "created_at": "2007-12-29T04:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1617#issuecomment-10284",
    "user": "mabshoff"
}
```

This is likely caused by using Maxima's factoring vs. Singular's libfactor. In the first case x and y are symbolic. 

Cheers,

Michael



---

archive/issue_comments_010285.json:
```json
{
    "body": "Changing component from algebraic geometry to commutative algebra.",
    "created_at": "2007-12-29T04:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1617#issuecomment-10285",
    "user": "mabshoff"
}
```

Changing component from algebraic geometry to commutative algebra.



---

archive/issue_comments_010286.json:
```json
{
    "body": "I vote for `wontfix` because I see no way of fixing this, this is a Maxima speed issue. The only fix I could think of is to add something about this in some documentation.",
    "created_at": "2008-01-16T16:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1617#issuecomment-10286",
    "user": "@malb"
}
```

I vote for `wontfix` because I see no way of fixing this, this is a Maxima speed issue. The only fix I could think of is to add something about this in some documentation.



---

archive/issue_comments_010287.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-16T16:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1617#issuecomment-10287",
    "user": "@williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010288.json:
```json
{
    "body": "Changing assignee from @malb to @williamstein.",
    "created_at": "2008-01-16T16:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1617#issuecomment-10288",
    "user": "@williamstein"
}
```

Changing assignee from @malb to @williamstein.



---

archive/issue_comments_010289.json:
```json
{
    "body": "Attachment [trac-1617.patch](tarball://root/attachments/some-uuid/ticket1617/trac-1617.patch) by @williamstein created at 2008-01-16 16:58:31",
    "created_at": "2008-01-16T16:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1617#issuecomment-10289",
    "user": "@williamstein"
}
```

Attachment [trac-1617.patch](tarball://root/attachments/some-uuid/ticket1617/trac-1617.patch) by @williamstein created at 2008-01-16 16:58:31



---

archive/issue_comments_010290.json:
```json
{
    "body": "At least one comment is wrong in the patch since the \"-\" no longer shows up:\n\n```\n2288\t2288\t        Notice that the -1 factor is separated out: \n2289\t2289\t            sage: f.factor_list() \n2290\t \t            [(-1, 1), (y - x, 1), (y^2 + x*y + x^2, 1)] \n \t2290\t            [(x - y, 1), (y^2 + x*y + x^2, 1)] \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-01-16T17:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1617#issuecomment-10290",
    "user": "mabshoff"
}
```

At least one comment is wrong in the patch since the "-" no longer shows up:

```
2288	2288	        Notice that the -1 factor is separated out: 
2289	2289	            sage: f.factor_list() 
2290	 	            [(-1, 1), (y - x, 1), (y^2 + x*y + x^2, 1)] 
 	2290	            [(x - y, 1), (y^2 + x*y + x^2, 1)] 
```


Cheers,

Michael



---

archive/issue_comments_010291.json:
```json
{
    "body": "This patch could interact with #1391 (http://trac.sagemath.org/sage_trac/ticket/1391).  That one should be applied first, I think, and then this looked at again.",
    "created_at": "2008-01-19T22:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1617#issuecomment-10291",
    "user": "@ncalexan"
}
```

This patch could interact with #1391 (http://trac.sagemath.org/sage_trac/ticket/1391).  That one should be applied first, I think, and then this looked at again.



---

archive/issue_comments_010292.json:
```json
{
    "body": "The patch applies to 2.10.1.alpha1 (hunks, but success). Afterwards, only the `toy_buchberger.py` tests fail which is unrelated. Thus, I say: apply.",
    "created_at": "2008-01-25T17:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1617#issuecomment-10292",
    "user": "@malb"
}
```

The patch applies to 2.10.1.alpha1 (hunks, but success). Afterwards, only the `toy_buchberger.py` tests fail which is unrelated. Thus, I say: apply.



---

archive/issue_comments_010293.json:
```json
{
    "body": "The mabshoff comment above about \"At least one comment is wrong in the patch since the \"-\" no longer shows up\" was caused by ncalexan's patch related to factorization.py, which was after #1617.",
    "created_at": "2008-01-25T17:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1617#issuecomment-10293",
    "user": "@williamstein"
}
```

The mabshoff comment above about "At least one comment is wrong in the patch since the "-" no longer shows up" was caused by ncalexan's patch related to factorization.py, which was after #1617.



---

archive/issue_comments_010294.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-25T17:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1617#issuecomment-10294",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha2



---

archive/issue_comments_010295.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-25T17:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1617#issuecomment-10295",
    "user": "mabshoff"
}
```

Resolution: fixed
