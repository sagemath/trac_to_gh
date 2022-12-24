# Issue 6649: doctest failure in decorate.py (on OS X only)

archive/issues_006649.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nIt is a Python 2.6 issue:\n\n```\nsage -t -long \"devel/sage/sage/parallel/decorate.py\"\n**********************************************************************\nFile \"/Users/Shared/sage/sage-4.1.1.alpha1/devel/sage/sage/parallel/\ndecorate.py\", line 64:\n    sage: @parallel()\n    def f(N): return N**Integer(2)\nExpected nothing\nGot:\n    doctest:49: DeprecationWarning: os.popen2 is deprecated.  Use the\nsubprocess module.\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_3\n***Test Failed*** 1 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6649\n\n",
    "created_at": "2009-07-28T18:06:40Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "doctest failure in decorate.py (on OS X only)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6649",
    "user": "GeorgSWeber"
}
```
Assignee: GeorgSWeber

It is a Python 2.6 issue:

```
sage -t -long "devel/sage/sage/parallel/decorate.py"
**********************************************************************
File "/Users/Shared/sage/sage-4.1.1.alpha1/devel/sage/sage/parallel/
decorate.py", line 64:
    sage: @parallel()
    def f(N): return N**Integer(2)
Expected nothing
Got:
    doctest:49: DeprecationWarning: os.popen2 is deprecated.  Use the
subprocess module.
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_3
***Test Failed*** 1 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/6649





---

archive/issue_comments_054581.json:
```json
{
    "body": "Attachment [trac_6649_doctest.patch](tarball://root/attachments/some-uuid/ticket6649/trac_6649_doctest.patch) by GeorgSWeber created at 2009-07-28 18:11:31\n\ntested against 4.1.1.alpha1",
    "created_at": "2009-07-28T18:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6649#issuecomment-54581",
    "user": "GeorgSWeber"
}
```

Attachment [trac_6649_doctest.patch](tarball://root/attachments/some-uuid/ticket6649/trac_6649_doctest.patch) by GeorgSWeber created at 2009-07-28 18:11:31

tested against 4.1.1.alpha1



---

archive/issue_comments_054582.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-28T18:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6649#issuecomment-54582",
    "user": "GeorgSWeber"
}
```

Changing status from new to assigned.



---

archive/issue_comments_054583.json:
```json
{
    "body": "I can check this out on Tuesday.  Looks good just based on reading the patch.",
    "created_at": "2009-08-01T15:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6649#issuecomment-54583",
    "user": "mhampton"
}
```

I can check this out on Tuesday.  Looks good just based on reading the patch.



---

archive/issue_comments_054584.json:
```json
{
    "body": "The patch applies fine to 4.1.1.rc0. I tested this out on an intel macbook running 10.4.11. The only error (which may or may not be related) was the following.\n\n\n```\nsage -t  \"devel/sage/sage/symbolic/expression.pyx\"          \n**********************************************************************\nFile \"/Users/davidjoyner/sagefiles/sage-4.1.1.rc0/devel/sage/sage/symbolic/expression.pyx\", line 2503:\n    sage: ((x+y)^a).match(w0^w1)\nExpected:\n    {$1: a, $0: x + y}\nGot:\n    {$0: x + y, $1: a}\n**********************************************************************\nFile \"/Users/davidjoyner/sagefiles/sage-4.1.1.rc0/devel/sage/sage/symbolic/expression.pyx\", line 2509:\n    sage: ((a+b)*(a+c)).match((a+w0)*(a+w1))\nExpected:\n    {$1: c, $0: b}\nGot:\n    {$0: b, $1: c}\n**********************************************************************\nFile \"/Users/davidjoyner/sagefiles/sage-4.1.1.rc0/devel/sage/sage/symbolic/expression.pyx\", line 2515:\n    sage: (a*(x+y)+a*z+b).match(a*w0+w1)\nExpected:\n    {$1: a*z + b, $0: x + y}\nGot:\n    {$0: x + y, $1: a*z + b}\n**********************************************************************\n1 items had failures:\n   3 of  24 in __main__.example_62\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /Users/davidjoyner/sagefiles/sage-4.1.1.rc0/tmp/.doctest_expression.py\n         [38.4 s]\n```\n",
    "created_at": "2009-08-02T11:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6649#issuecomment-54584",
    "user": "wdj"
}
```

The patch applies fine to 4.1.1.rc0. I tested this out on an intel macbook running 10.4.11. The only error (which may or may not be related) was the following.


```
sage -t  "devel/sage/sage/symbolic/expression.pyx"          
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.rc0/devel/sage/sage/symbolic/expression.pyx", line 2503:
    sage: ((x+y)^a).match(w0^w1)
Expected:
    {$1: a, $0: x + y}
Got:
    {$0: x + y, $1: a}
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.rc0/devel/sage/sage/symbolic/expression.pyx", line 2509:
    sage: ((a+b)*(a+c)).match((a+w0)*(a+w1))
Expected:
    {$1: c, $0: b}
Got:
    {$0: b, $1: c}
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.rc0/devel/sage/sage/symbolic/expression.pyx", line 2515:
    sage: (a*(x+y)+a*z+b).match(a*w0+w1)
Expected:
    {$1: a*z + b, $0: x + y}
Got:
    {$0: x + y, $1: a*z + b}
**********************************************************************
1 items had failures:
   3 of  24 in __main__.example_62
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/davidjoyner/sagefiles/sage-4.1.1.rc0/tmp/.doctest_expression.py
         [38.4 s]
```




---

archive/issue_comments_054585.json:
```json
{
    "body": "David: The doctest failures you got are, I think, harmless. By definition, a non-empty dictionary is made up of a number of key-value pairs, which are stored in an arbitrary but non-random order. You can think of a non-empty Python dictionary as a set of unordered key-value pairs. From your report, I see that there are 3 failures. If you compare\n\n```\nExpected:\n    {$1: a, $0: x + y}\n```\n\nwith\n\n```\nGot:\n    {$0: x + y, $1: a}\n```\n\nyou see that these two dictionaries are essentially the same. Again by comparison, the dictionaries\n\n```\nExpected:\n    {$1: c, $0: b}\n```\n\nand\n\n```\nGot:\n    {$0: b, $1: c}\n```\n\nare equivalent, and likewise for\n\n```\nExpected:\n    {$1: a*z + b, $0: x + y}\n```\n\nand\n\n```\nGot:\n    {$0: x + y, $1: a*z + b}\n```\n\nI would say that you can ignore these 3 failures.",
    "created_at": "2009-08-02T23:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6649#issuecomment-54585",
    "user": "mvngu"
}
```

David: The doctest failures you got are, I think, harmless. By definition, a non-empty dictionary is made up of a number of key-value pairs, which are stored in an arbitrary but non-random order. You can think of a non-empty Python dictionary as a set of unordered key-value pairs. From your report, I see that there are 3 failures. If you compare

```
Expected:
    {$1: a, $0: x + y}
```

with

```
Got:
    {$0: x + y, $1: a}
```

you see that these two dictionaries are essentially the same. Again by comparison, the dictionaries

```
Expected:
    {$1: c, $0: b}
```

and

```
Got:
    {$0: b, $1: c}
```

are equivalent, and likewise for

```
Expected:
    {$1: a*z + b, $0: x + y}
```

and

```
Got:
    {$0: x + y, $1: a*z + b}
```

I would say that you can ignore these 3 failures.



---

archive/issue_comments_054586.json:
```json
{
    "body": "Okay, I would then give this a positive review. Is there more testing needed?",
    "created_at": "2009-08-02T23:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6649#issuecomment-54586",
    "user": "wdj"
}
```

Okay, I would then give this a positive review. Is there more testing needed?



---

archive/issue_comments_054587.json:
```json
{
    "body": "To be extra safe, apply the patch `trac_6649_doctest.patch` to a fresh clone of the main repository, rebuild the clone and run it. Then execute the following from the Sage command line:\n\n```\nsage: @parallel()\n....: def f(N): return N^2\n....: \nsage: v = list(f([1,2,4])); v.sort(); v\n[(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]\nsage: @parallel('reference')\n....: def f(N): return N^2\n....: \nsage: v = list(f([1,2,4])); v.sort(); v\n[(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]\nsage: sage.parallel.ncpus.ncpus()\n24\n```\n\nThe command `sage.parallel.ncpus.ncpus()` would return different answers depending on the number of CPU's on your system. In the case of the machine sage.math it returns 24, which is the number of cores on that machine. For an Intel Mac with dual core, I would expect `sage.parallel.ncpus.ncpus()` to return 2. But in any case, testing that command on a Mac should not result in a deprecation warning. The idea of Georg's patch is to prevent the deprecation warning when using a Mac.",
    "created_at": "2009-08-02T23:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6649#issuecomment-54587",
    "user": "mvngu"
}
```

To be extra safe, apply the patch `trac_6649_doctest.patch` to a fresh clone of the main repository, rebuild the clone and run it. Then execute the following from the Sage command line:

```
sage: @parallel()
....: def f(N): return N^2
....: 
sage: v = list(f([1,2,4])); v.sort(); v
[(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]
sage: @parallel('reference')
....: def f(N): return N^2
....: 
sage: v = list(f([1,2,4])); v.sort(); v
[(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]
sage: sage.parallel.ncpus.ncpus()
24
```

The command `sage.parallel.ncpus.ncpus()` would return different answers depending on the number of CPU's on your system. In the case of the machine sage.math it returns 24, which is the number of cores on that machine. For an Intel Mac with dual core, I would expect `sage.parallel.ncpus.ncpus()` to return 2. But in any case, testing that command on a Mac should not result in a deprecation warning. The idea of Georg's patch is to prevent the deprecation warning when using a Mac.



---

archive/issue_comments_054588.json:
```json
{
    "body": "What I got agrees with what you said should happen:\n\n\n```\nLoading Sage library. Current Mercurial branch is: 6649\nsage: @parallel()\n....: def f(N): return N^2\n....: \nsage: v = list(f([1,2,4])); v.sort(); v\n[(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]\nsage: @parallel('reference')\n....: def f(N): return N^2\n....: \nsage: v = list(f([1,2,4])); v.sort(); v\n[(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]\nsage: sage.parallel.ncpus.ncpus()\n2\nsage: \n```\n\nSo changing this from \"needs review\" to \"positive review\".",
    "created_at": "2009-08-02T23:57:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6649#issuecomment-54588",
    "user": "wdj"
}
```

What I got agrees with what you said should happen:


```
Loading Sage library. Current Mercurial branch is: 6649
sage: @parallel()
....: def f(N): return N^2
....: 
sage: v = list(f([1,2,4])); v.sort(); v
[(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]
sage: @parallel('reference')
....: def f(N): return N^2
....: 
sage: v = list(f([1,2,4])); v.sort(); v
[(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]
sage: sage.parallel.ncpus.ncpus()
2
sage: 
```

So changing this from "needs review" to "positive review".



---

archive/issue_comments_054589.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-03T06:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6649#issuecomment-54589",
    "user": "mvngu"
}
```

Resolution: fixed
