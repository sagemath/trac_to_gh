# Issue 5660: count_points(1) for elliptic curves over finite fields is stupid

archive/issues_005660.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  jcooley\n\nThere is one special case of count_points that could be massively faster.  This should definitely be optimized!\n\n\n```\nsage: E = EllipticCurve(GF(97),[1,2])\nsage: time E.count_points(1)\n[104]\nTime: CPU 1.91 s, Wall: 1.93 s\nsage: time E.cardinality()\n104\nTime: CPU 0.00 s, Wall: 0.18 s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5660\n\n",
    "created_at": "2009-04-01T17:27:14Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "count_points(1) for elliptic curves over finite fields is stupid",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5660",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  jcooley

There is one special case of count_points that could be massively faster.  This should definitely be optimized!


```
sage: E = EllipticCurve(GF(97),[1,2])
sage: time E.count_points(1)
[104]
Time: CPU 1.91 s, Wall: 1.93 s
sage: time E.cardinality()
104
Time: CPU 0.00 s, Wall: 0.18 s
```


Issue created by migration from https://trac.sagemath.org/ticket/5660





---

archive/issue_comments_044161.json:
```json
{
    "body": "I think that count_points is some general scheme thing.  All that needs doing is overriding that for elliptic curves I think.",
    "created_at": "2009-04-16T20:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44161",
    "user": "https://github.com/JohnCremona"
}
```

I think that count_points is some general scheme thing.  All that needs doing is overriding that for elliptic curves I think.



---

archive/issue_comments_044162.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-21T08:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44162",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_044163.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-21T08:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44163",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_044164.json:
```json
{
    "body": "All that is needed is to add a count_points(n) method for elliptic curves over finite fields which returns self.cardinality(extension_degree=n).  An easy job for someone!",
    "created_at": "2009-07-21T08:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44164",
    "user": "https://github.com/JohnCremona"
}
```

All that is needed is to add a count_points(n) method for elliptic curves over finite fields which returns self.cardinality(extension_degree=n).  An easy job for someone!



---

archive/issue_comments_044165.json:
```json
{
    "body": "Applies to 4.1.1",
    "created_at": "2009-08-18T10:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44165",
    "user": "https://github.com/JohnCremona"
}
```

Applies to 4.1.1



---

archive/issue_comments_044166.json:
```json
{
    "body": "Attachment [trac_5660-count_points.patch](tarball://root/attachments/some-uuid/ticket5660/trac_5660-count_points.patch) by @JohnCremona created at 2009-08-18 10:39:05\n\nThe patch follows the above suggestion, and also overwrites the rational_points() function for elliptic curves over finite fields to be synonymous to points().",
    "created_at": "2009-08-18T10:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44166",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_5660-count_points.patch](tarball://root/attachments/some-uuid/ticket5660/trac_5660-count_points.patch) by @JohnCremona created at 2009-08-18 10:39:05

The patch follows the above suggestion, and also overwrites the rational_points() function for elliptic curves over finite fields to be synonymous to points().



---

archive/issue_comments_044167.json:
```json
{
    "body": "Apply after previous",
    "created_at": "2009-08-19T09:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44167",
    "user": "https://github.com/JohnCremona"
}
```

Apply after previous



---

archive/issue_comments_044168.json:
```json
{
    "body": "Attachment [trac_5660-doc_fixes.patch](tarball://root/attachments/some-uuid/ticket5660/trac_5660-doc_fixes.patch) by @aghitza created at 2009-08-19 10:11:54\n\nLooks good and passes tests.",
    "created_at": "2009-08-19T10:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44168",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5660-doc_fixes.patch](tarball://root/attachments/some-uuid/ticket5660/trac_5660-doc_fixes.patch) by @aghitza created at 2009-08-19 10:11:54

Looks good and passes tests.



---

archive/issue_comments_044169.json:
```json
{
    "body": "I'm getting the following doctest failure with the above two patches applied to Sage 4.1.1:\n\n```\nsage -t -long devel/sage-main/sage/schemes/generic/algebraic_scheme.py\n**********************************************************************\nFile \"/scratch/mvngu/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/devel/sage-main/sage/schemes/generic/algebraic_scheme.py\", line 794:\n    sage: Etilde.rational_points()\nExpected:\n    [(0 : 0 : 1), (1 : 0 : 1), (2 : 0 : 1), (0 : 2 : 1), (1 : 2 : 1), (2 : 2 : 1), (0 : 1 : 0)]\nGot:\n    [(0 : 0 : 1), (0 : 1 : 0), (0 : 2 : 1), (1 : 0 : 1), (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_28\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/tmp/.doctest_algebraic_scheme.py\n\t [4.4 s]\n```\n",
    "created_at": "2009-08-23T00:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44169",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I'm getting the following doctest failure with the above two patches applied to Sage 4.1.1:

```
sage -t -long devel/sage-main/sage/schemes/generic/algebraic_scheme.py
**********************************************************************
File "/scratch/mvngu/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/devel/sage-main/sage/schemes/generic/algebraic_scheme.py", line 794:
    sage: Etilde.rational_points()
Expected:
    [(0 : 0 : 1), (1 : 0 : 1), (2 : 0 : 1), (0 : 2 : 1), (1 : 2 : 1), (2 : 2 : 1), (0 : 1 : 0)]
Got:
    [(0 : 0 : 1), (0 : 1 : 0), (0 : 2 : 1), (1 : 0 : 1), (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_28
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/tmp/.doctest_algebraic_scheme.py
	 [4.4 s]
```




---

archive/issue_comments_044170.json:
```json
{
    "body": "This is because the generic code for schemes is behaving badly and doesn't sort the list of points before returning it.\n\nI will fix this in #6810, but for now the above doctest should just be changed to `[(0 : 0 : 1), (0 : 1 : 0), (0 : 2 : 1), (1 : 0 : 1), (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]`, which is the correct behaviour.  I've added a trivial patch that does this.",
    "created_at": "2009-08-23T02:00:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44170",
    "user": "https://github.com/aghitza"
}
```

This is because the generic code for schemes is behaving badly and doesn't sort the list of points before returning it.

I will fix this in #6810, but for now the above doctest should just be changed to `[(0 : 0 : 1), (0 : 1 : 0), (0 : 2 : 1), (1 : 0 : 1), (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]`, which is the correct behaviour.  I've added a trivial patch that does this.



---

archive/issue_comments_044171.json:
```json
{
    "body": "add after previous two",
    "created_at": "2009-08-23T02:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44171",
    "user": "https://github.com/aghitza"
}
```

add after previous two



---

archive/issue_comments_044172.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-23T10:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44172",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_013299.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-23T10:09:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5660#event-13299"
}
```



---

archive/issue_comments_044173.json:
```json
{
    "body": "Attachment [trac_5660_fix.patch](tarball://root/attachments/some-uuid/ticket5660/trac_5660_fix.patch) by mvngu created at 2009-08-23 10:09:56",
    "created_at": "2009-08-23T10:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44173",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_5660_fix.patch](tarball://root/attachments/some-uuid/ticket5660/trac_5660_fix.patch) by mvngu created at 2009-08-23 10:09:56



---

archive/issue_comments_044174.json:
```json
{
    "body": "Replying to [comment:7 AlexGhitza]:\n> This is because the generic code for schemes is behaving badly and doesn't sort the list of points before returning it.\n> \n> I will fix this in #6810, but for now the above doctest should just be changed to `[(0 : 0 : 1), (0 : 1 : 0), (0 : 2 : 1), (1 : 0 : 1), (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]`, which is the correct behaviour.  I've added a trivial patch that does this.\n> \n\nThanks, Alex, you are quite right -- and it is my fault for not testing more before posting the patch.",
    "created_at": "2009-08-23T11:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44174",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:7 AlexGhitza]:
> This is because the generic code for schemes is behaving badly and doesn't sort the list of points before returning it.
> 
> I will fix this in #6810, but for now the above doctest should just be changed to `[(0 : 0 : 1), (0 : 1 : 0), (0 : 2 : 1), (1 : 0 : 1), (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]`, which is the correct behaviour.  I've added a trivial patch that does this.
> 

Thanks, Alex, you are quite right -- and it is my fault for not testing more before posting the patch.
