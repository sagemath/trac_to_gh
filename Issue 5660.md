# Issue 5660: count_points(1) for elliptic curves over finite fields is stupid

archive/issues_005660.json:
```json
{
    "body": "Assignee: was\n\nCC:  jcooley\n\nThere is one special case of count_points that could be massively faster.  This should definitely be optimized!\n\n\n```\nsage: E = EllipticCurve(GF(97),[1,2])\nsage: time E.count_points(1)\n[104]\nTime: CPU 1.91 s, Wall: 1.93 s\nsage: time E.cardinality()\n104\nTime: CPU 0.00 s, Wall: 0.18 s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5660\n\n",
    "created_at": "2009-04-01T17:27:14Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "count_points(1) for elliptic curves over finite fields is stupid",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5660",
    "user": "was"
}
```
Assignee: was

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

archive/issue_comments_044246.json:
```json
{
    "body": "I think that count_points is some general scheme thing.  All that needs doing is overriding that for elliptic curves I think.",
    "created_at": "2009-04-16T20:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44246",
    "user": "cremona"
}
```

I think that count_points is some general scheme thing.  All that needs doing is overriding that for elliptic curves I think.



---

archive/issue_comments_044247.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-21T08:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44247",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_044248.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-21T08:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44248",
    "user": "davidloeffler"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_044249.json:
```json
{
    "body": "All that is needed is to add a count_points(n) method for elliptic curves over finite fields which returns self.cardinality(extension_degree=n).  An easy job for someone!",
    "created_at": "2009-07-21T08:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44249",
    "user": "cremona"
}
```

All that is needed is to add a count_points(n) method for elliptic curves over finite fields which returns self.cardinality(extension_degree=n).  An easy job for someone!



---

archive/issue_comments_044250.json:
```json
{
    "body": "Applies to 4.1.1",
    "created_at": "2009-08-18T10:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44250",
    "user": "cremona"
}
```

Applies to 4.1.1



---

archive/issue_comments_044251.json:
```json
{
    "body": "Attachment [trac_5660-count_points.patch](tarball://root/attachments/some-uuid/ticket5660/trac_5660-count_points.patch) by cremona created at 2009-08-18 10:39:05\n\nThe patch follows the above suggestion, and also overwrites the rational_points() function for elliptic curves over finite fields to be synonymous to points().",
    "created_at": "2009-08-18T10:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44251",
    "user": "cremona"
}
```

Attachment [trac_5660-count_points.patch](tarball://root/attachments/some-uuid/ticket5660/trac_5660-count_points.patch) by cremona created at 2009-08-18 10:39:05

The patch follows the above suggestion, and also overwrites the rational_points() function for elliptic curves over finite fields to be synonymous to points().



---

archive/issue_comments_044252.json:
```json
{
    "body": "Apply after previous",
    "created_at": "2009-08-19T09:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44252",
    "user": "cremona"
}
```

Apply after previous



---

archive/issue_comments_044253.json:
```json
{
    "body": "Attachment [trac_5660-doc_fixes.patch](tarball://root/attachments/some-uuid/ticket5660/trac_5660-doc_fixes.patch) by AlexGhitza created at 2009-08-19 10:11:54\n\nLooks good and passes tests.",
    "created_at": "2009-08-19T10:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44253",
    "user": "AlexGhitza"
}
```

Attachment [trac_5660-doc_fixes.patch](tarball://root/attachments/some-uuid/ticket5660/trac_5660-doc_fixes.patch) by AlexGhitza created at 2009-08-19 10:11:54

Looks good and passes tests.



---

archive/issue_comments_044254.json:
```json
{
    "body": "I'm getting the following doctest failure with the above two patches applied to Sage 4.1.1:\n\n```\nsage -t -long devel/sage-main/sage/schemes/generic/algebraic_scheme.py\n**********************************************************************\nFile \"/scratch/mvngu/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/devel/sage-main/sage/schemes/generic/algebraic_scheme.py\", line 794:\n    sage: Etilde.rational_points()\nExpected:\n    [(0 : 0 : 1), (1 : 0 : 1), (2 : 0 : 1), (0 : 2 : 1), (1 : 2 : 1), (2 : 2 : 1), (0 : 1 : 0)]\nGot:\n    [(0 : 0 : 1), (0 : 1 : 0), (0 : 2 : 1), (1 : 0 : 1), (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_28\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/tmp/.doctest_algebraic_scheme.py\n\t [4.4 s]\n```\n",
    "created_at": "2009-08-23T00:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44254",
    "user": "mvngu"
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

archive/issue_comments_044255.json:
```json
{
    "body": "This is because the generic code for schemes is behaving badly and doesn't sort the list of points before returning it.\n\nI will fix this in #6810, but for now the above doctest should just be changed to `[(0 : 0 : 1), (0 : 1 : 0), (0 : 2 : 1), (1 : 0 : 1), (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]`, which is the correct behaviour.  I've added a trivial patch that does this.",
    "created_at": "2009-08-23T02:00:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44255",
    "user": "AlexGhitza"
}
```

This is because the generic code for schemes is behaving badly and doesn't sort the list of points before returning it.

I will fix this in #6810, but for now the above doctest should just be changed to `[(0 : 0 : 1), (0 : 1 : 0), (0 : 2 : 1), (1 : 0 : 1), (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]`, which is the correct behaviour.  I've added a trivial patch that does this.



---

archive/issue_comments_044256.json:
```json
{
    "body": "add after previous two",
    "created_at": "2009-08-23T02:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44256",
    "user": "AlexGhitza"
}
```

add after previous two



---

archive/issue_comments_044257.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-23T10:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44257",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_044258.json:
```json
{
    "body": "Attachment [trac_5660_fix.patch](tarball://root/attachments/some-uuid/ticket5660/trac_5660_fix.patch) by mvngu created at 2009-08-23 10:09:56",
    "created_at": "2009-08-23T10:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44258",
    "user": "mvngu"
}
```

Attachment [trac_5660_fix.patch](tarball://root/attachments/some-uuid/ticket5660/trac_5660_fix.patch) by mvngu created at 2009-08-23 10:09:56



---

archive/issue_comments_044259.json:
```json
{
    "body": "Replying to [comment:7 AlexGhitza]:\n> This is because the generic code for schemes is behaving badly and doesn't sort the list of points before returning it.\n> \n> I will fix this in #6810, but for now the above doctest should just be changed to `[(0 : 0 : 1), (0 : 1 : 0), (0 : 2 : 1), (1 : 0 : 1), (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]`, which is the correct behaviour.  I've added a trivial patch that does this.\n> \n\nThanks, Alex, you are quite right -- and it is my fault for not testing more before posting the patch.",
    "created_at": "2009-08-23T11:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5660#issuecomment-44259",
    "user": "cremona"
}
```

Replying to [comment:7 AlexGhitza]:
> This is because the generic code for schemes is behaving badly and doesn't sort the list of points before returning it.
> 
> I will fix this in #6810, but for now the above doctest should just be changed to `[(0 : 0 : 1), (0 : 1 : 0), (0 : 2 : 1), (1 : 0 : 1), (1 : 2 : 1), (2 : 0 : 1), (2 : 2 : 1)]`, which is the correct behaviour.  I've added a trivial patch that does this.
> 

Thanks, Alex, you are quite right -- and it is my fault for not testing more before posting the patch.
