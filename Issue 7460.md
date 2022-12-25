# Issue 7460: numerical noise on itanium (iras)

archive/issues_007460.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nwstein@iras:~/screen/iras/build/sage-4.2.1.rc0> ./sage -t -long \"devel/sage/doc/en/numerical_sage/cvxopt.rst\"\nsage -t -long \"devel/sage/doc/en/numerical_sage/cvxopt.rst\"\n**********************************************************************\nFile \"/home/wstein/screen/iras/build/sage-4.2.1.rc0/devel/sage/doc/en/numerical_sage/cvxopt.rst\", line 137:\n    sage: print sol['x']\nExpected:\n       1.0000e+00\n       1.0000e+00\nGot:   \n       1.0000e-00\n       1.0000e+00\n    <BLANKLINE>\n**********************************************************************\n1 items had failures:\n   1 of  11 in __main__.example_2\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_cvxopt.py\n         [3.8 s]\nexit code: 1024\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7460\n\n",
    "created_at": "2009-11-14T18:08:08Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "numerical noise on itanium (iras)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7460",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
wstein@iras:~/screen/iras/build/sage-4.2.1.rc0> ./sage -t -long "devel/sage/doc/en/numerical_sage/cvxopt.rst"
sage -t -long "devel/sage/doc/en/numerical_sage/cvxopt.rst"
**********************************************************************
File "/home/wstein/screen/iras/build/sage-4.2.1.rc0/devel/sage/doc/en/numerical_sage/cvxopt.rst", line 137:
    sage: print sol['x']
Expected:
       1.0000e+00
       1.0000e+00
Got:   
       1.0000e-00
       1.0000e+00
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_cvxopt.py
         [3.8 s]
exit code: 1024

```


Issue created by migration from https://trac.sagemath.org/ticket/7460





---

archive/issue_comments_062720.json:
```json
{
    "body": "With the attached patch:\n\n```\nwstein@iras:~/screen/iras/build/sage-4.2.1.rc0> ./sage -t -long \"devel/sage/doc/en/numerical_sage/cvxopt.rst\"\nsage -t -long \"devel/sage/doc/en/numerical_sage/cvxopt.rst\" \n         [3.7 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 3.7 seconds\n```\n",
    "created_at": "2009-11-14T18:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7460#issuecomment-62720",
    "user": "https://github.com/williamstein"
}
```

With the attached patch:

```
wstein@iras:~/screen/iras/build/sage-4.2.1.rc0> ./sage -t -long "devel/sage/doc/en/numerical_sage/cvxopt.rst"
sage -t -long "devel/sage/doc/en/numerical_sage/cvxopt.rst" 
         [3.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3.7 seconds
```




---

archive/issue_comments_062721.json:
```json
{
    "body": "Attachment [trac_7460.patch](tarball://root/attachments/some-uuid/ticket7460/trac_7460.patch) by @williamstein created at 2009-11-14 18:13:24",
    "created_at": "2009-11-14T18:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7460#issuecomment-62721",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7460.patch](tarball://root/attachments/some-uuid/ticket7460/trac_7460.patch) by @williamstein created at 2009-11-14 18:13:24



---

archive/issue_comments_062722.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-14T18:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7460#issuecomment-62722",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062723.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-15T14:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7460#issuecomment-62723",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_062724.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-15T14:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7460#issuecomment-62724",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_017690.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-17T05:55:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7460",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7460#event-17690"
}
```



---

archive/issue_comments_062725.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T05:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7460#issuecomment-62725",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
