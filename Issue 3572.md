# Issue 3572: optimize sage startup time by not importing any modules that import linbox by default.

archive/issues_003572.json:
```json
{
    "body": "Assignee: cwitty\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3572\n\n",
    "created_at": "2008-07-06T21:28:10Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "optimize sage startup time by not importing any modules that import linbox by default.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3572",
    "user": "was"
}
```
Assignee: cwitty



Issue created by migration from https://trac.sagemath.org/ticket/3572





---

archive/issue_comments_025229.json:
```json
{
    "body": "Attachment [sage-3572.patch](tarball://root/attachments/some-uuid/ticket3572/sage-3572.patch) by was created at 2008-07-06 22:43:20",
    "created_at": "2008-07-06T22:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3572#issuecomment-25229",
    "user": "was"
}
```

Attachment [sage-3572.patch](tarball://root/attachments/some-uuid/ticket3572/sage-3572.patch) by was created at 2008-07-06 22:43:20



---

archive/issue_comments_025230.json:
```json
{
    "body": "on osx, BEFORE:\n\n```\nteragon-2:matrix was$ sage -startuptime |grep linbox\n            sage.libs.linbox.linbox: 0.270 (matrix_modn_dense)\n0.270 sage.libs.linbox.linbox (matrix_modn_dense)\n```\n\n\nAFTER\n\n```\nteragon-2:matrix was$ sage -startuptime |grep linbox\nteragon-2:matrix was$ \n```\n\n\nOf course now,\n\n\n```\nsage: time a = matrix(ZZ,2)\nCPU times: user 0.34 s, sys: 0.01 s, total: 0.35 s\nWall time: 0.36 s\nsage: time a = matrix(ZZ,3)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\n```\n\n\nbut that makes a lot of sense.  Only make people pay if they use the goods.\n\nWilliam",
    "created_at": "2008-07-06T22:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3572#issuecomment-25230",
    "user": "was"
}
```

on osx, BEFORE:

```
teragon-2:matrix was$ sage -startuptime |grep linbox
            sage.libs.linbox.linbox: 0.270 (matrix_modn_dense)
0.270 sage.libs.linbox.linbox (matrix_modn_dense)
```


AFTER

```
teragon-2:matrix was$ sage -startuptime |grep linbox
teragon-2:matrix was$ 
```


Of course now,


```
sage: time a = matrix(ZZ,2)
CPU times: user 0.34 s, sys: 0.01 s, total: 0.35 s
Wall time: 0.36 s
sage: time a = matrix(ZZ,3)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
```


but that makes a lot of sense.  Only make people pay if they use the goods.

William



---

archive/issue_comments_025231.json:
```json
{
    "body": "With this patch applied against 3.0.4.alpha2 I get one doctest failure:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2$ ./sage -t -long devel/sage/sage/misc/session.pyx\nsage -t -long devel/sage/sage/misc/session.pyx              \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/session.py\", line 212:\n    sage: save_session('session', verbose=True)\nExpected:\n    Not saving ...\nGot:\n    Saving doctest\n    Saving a\n    Not saving example_2: example_2 is a function\n    Not saving example_3: example_3 is a function\n    Not saving example_0: example_0 is a function\n    Not saving example_1: example_1 is a function\n    Not saving example_4: example_4 is a function\n    Not saving example_5: example_5 is a function\n    Saving __file__\n    Not saving f: f is a function\n    Saving __doc__\n    Saving __builtins__\n    Saving __name__\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_4\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/.doctest_session.py\n\t [2.0 s]\nexit code: 1024\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T04:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3572#issuecomment-25231",
    "user": "mabshoff"
}
```

With this patch applied against 3.0.4.alpha2 I get one doctest failure:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2$ ./sage -t -long devel/sage/sage/misc/session.pyx
sage -t -long devel/sage/sage/misc/session.pyx              
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/session.py", line 212:
    sage: save_session('session', verbose=True)
Expected:
    Not saving ...
Got:
    Saving doctest
    Saving a
    Not saving example_2: example_2 is a function
    Not saving example_3: example_3 is a function
    Not saving example_0: example_0 is a function
    Not saving example_1: example_1 is a function
    Not saving example_4: example_4 is a function
    Not saving example_5: example_5 is a function
    Saving __file__
    Not saving f: f is a function
    Saving __doc__
    Saving __builtins__
    Saving __name__
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_4
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/.doctest_session.py
	 [2.0 s]
exit code: 1024
```


Cheers,

Michael



---

archive/issue_comments_025232.json:
```json
{
    "body": "The patch doesn't apply cleanly any more, as you might expect.  I only got one doctest failure, from the following issue (not the one mabshoff reported, perhaps because that doctest in the patch didn't apply): \n\n```\nsage: os.system('sage -startuptime | grep linbox')\n           sage.libs.linbox.linbox: 0.006 (sage.matrix.matrix_modn_dense)\n0\n```\n\nSo there's another import which needs to be removed...",
    "created_at": "2009-05-10T23:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3572#issuecomment-25232",
    "user": "jhpalmieri"
}
```

The patch doesn't apply cleanly any more, as you might expect.  I only got one doctest failure, from the following issue (not the one mabshoff reported, perhaps because that doctest in the patch didn't apply): 

```
sage: os.system('sage -startuptime | grep linbox')
           sage.libs.linbox.linbox: 0.006 (sage.matrix.matrix_modn_dense)
0
```

So there's another import which needs to be removed...
