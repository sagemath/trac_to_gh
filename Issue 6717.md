# Issue 6717: Sage 4.1.1.rc2: doctest failures in sage/symbolic/expression.pyx

archive/issues_006717.json:
```json
{
    "body": "Assignee: tbd\n\nGeorg S. Weber reported the following doctest failures at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/5f23ec4032f5e91b) thread:\n\n```\non Mac(Intel) OS X 10.4.11 (XCode 2.5 / gcc 4.0.1 build \"5370\"), Sage\n4.1.1.rc2 builds fine.\nHowever, there are two (reproducible) doctest failures, one known one\nand one I never saw before. The known one is:\n\nsage -t -long \"devel/sage/sage/symbolic/expression.pyx\"\n**********************************************************************\nFile \"/Users/Shared/sage/sage-4.1.1.rc2/devel/sage/sage/symbolic/\nexpression.pyx\", line 2515:\n    sage: ((x+y)^a).match(w0^w1)\nExpected:\n    {$1: a, $0: x + y}\nGot:\n    {$0: x + y, $1: a}\n**********************************************************************\nFile \"/Users/Shared/sage/sage-4.1.1.rc2/devel/sage/sage/symbolic/\nexpression.pyx\", line 2521:\n    sage: ((a+b)*(a+c)).match((a+w0)*(a+w1))\nExpected:\n    {$1: c, $0: b}\nGot:\n    {$0: b, $1: c}\n**********************************************************************\nFile \"/Users/Shared/sage/sage-4.1.1.rc2/devel/sage/sage/symbolic/\nexpression.pyx\", line 2527:\n    sage: (a*(x+y)+a*z+b).match(a*w0+w1)\nExpected:\n    {$1: a*z + b, $0: x + y}\nGot:\n    {$0: x + y, $1: a*z + b}\n**********************************************************************\n1 items had failures:\n   3 of  24 in __main__.example_62\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /Users/Shared/sage/sage-4.1.1.rc2/\ntmp/.doctest_expression.py\n         [73.6 s] \n```\n\nHere is William Stein's suggestion for fixing the above doctest failures:\n\n```\nThe above doctest should be changed so they don't depend on random hashing,\ne.g., change the dicts to lists of sorted tuples. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6717\n\n",
    "created_at": "2009-08-09T18:06:33Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "Sage 4.1.1.rc2: doctest failures in sage/symbolic/expression.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6717",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tbd

Georg S. Weber reported the following doctest failures at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/5f23ec4032f5e91b) thread:

```
on Mac(Intel) OS X 10.4.11 (XCode 2.5 / gcc 4.0.1 build "5370"), Sage
4.1.1.rc2 builds fine.
However, there are two (reproducible) doctest failures, one known one
and one I never saw before. The known one is:

sage -t -long "devel/sage/sage/symbolic/expression.pyx"
**********************************************************************
File "/Users/Shared/sage/sage-4.1.1.rc2/devel/sage/sage/symbolic/
expression.pyx", line 2515:
    sage: ((x+y)^a).match(w0^w1)
Expected:
    {$1: a, $0: x + y}
Got:
    {$0: x + y, $1: a}
**********************************************************************
File "/Users/Shared/sage/sage-4.1.1.rc2/devel/sage/sage/symbolic/
expression.pyx", line 2521:
    sage: ((a+b)*(a+c)).match((a+w0)*(a+w1))
Expected:
    {$1: c, $0: b}
Got:
    {$0: b, $1: c}
**********************************************************************
File "/Users/Shared/sage/sage-4.1.1.rc2/devel/sage/sage/symbolic/
expression.pyx", line 2527:
    sage: (a*(x+y)+a*z+b).match(a*w0+w1)
Expected:
    {$1: a*z + b, $0: x + y}
Got:
    {$0: x + y, $1: a*z + b}
**********************************************************************
1 items had failures:
   3 of  24 in __main__.example_62
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/Shared/sage/sage-4.1.1.rc2/
tmp/.doctest_expression.py
         [73.6 s] 
```

Here is William Stein's suggestion for fixing the above doctest failures:

```
The above doctest should be changed so they don't depend on random hashing,
e.g., change the dicts to lists of sorted tuples. 
```


Issue created by migration from https://trac.sagemath.org/ticket/6717





---

archive/issue_comments_055026.json:
```json
{
    "body": "Attachment [trac_6717.patch](tarball://root/attachments/some-uuid/ticket6717/trac_6717.patch) by @burcin created at 2009-08-09 19:45:27\n\nfix random printing problems in doctests",
    "created_at": "2009-08-09T19:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6717#issuecomment-55026",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6717.patch](tarball://root/attachments/some-uuid/ticket6717/trac_6717.patch) by @burcin created at 2009-08-09 19:45:27

fix random printing problems in doctests



---

archive/issue_comments_055027.json:
```json
{
    "body": "Changing assignee from tbd to @burcin.",
    "created_at": "2009-08-09T19:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6717#issuecomment-55027",
    "user": "https://github.com/burcin"
}
```

Changing assignee from tbd to @burcin.



---

archive/issue_comments_055028.json:
```json
{
    "body": "attachment:trac_6717.patch fixes the reported problems, and one more. :)",
    "created_at": "2009-08-09T19:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6717#issuecomment-55028",
    "user": "https://github.com/burcin"
}
```

attachment:trac_6717.patch fixes the reported problems, and one more. :)



---

archive/issue_comments_055029.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-08-09T19:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6717#issuecomment-55029",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_055030.json:
```json
{
    "body": "Yep, this patch does the job, now the doctest does not fail anymore for me.\nAlthough I didn't test on a system, where the test already went fine before the patch, from the nature of the changes, I'm confident, that it will still work.",
    "created_at": "2009-08-09T21:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6717#issuecomment-55030",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Yep, this patch does the job, now the doctest does not fail anymore for me.
Although I didn't test on a system, where the test already went fine before the patch, from the nature of the changes, I'm confident, that it will still work.



---

archive/issue_events_015861.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-12T00:03:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6717",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6717#event-15861"
}
```



---

archive/issue_comments_055031.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-12T00:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6717#issuecomment-55031",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
