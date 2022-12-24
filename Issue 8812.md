# Issue 8812: notebook doctest failure in sage-4.4.1.alpha0

archive/issues_008812.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  acleone\n\n\n```\nwstein@sage:~/build/release/4.4.1/sage-4.4.1.alpha1$ ./sage -t  -long \"local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/twist.py\"\nsage -t -long \"local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/twist.py\"\n **********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/release/4.4.1/sage-4.4.1.alpha1/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/twist.py\", line 1696:\n    sage: E.render(ctx)\nExpected:\n    <RedirectResponse 301 Document moved to over there.>\nGot:\n    <sagenb.notebook.twist.RedirectResponse code=303, streamlen=None>\n**********************************************************************\n1 items had failures:\n   1 of  15 in __main__.example_30\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_twist.py\n         [4.0 s]\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/twist.py\"\nTotal time for all tests: 4.0 seconds\n```\n\n\nThis is a result of #8725.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8812\n\n",
    "created_at": "2010-04-29T00:30:55Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook doctest failure in sage-4.4.1.alpha0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8812",
    "user": "was"
}
```
Assignee: jason, was

CC:  acleone


```
wstein@sage:~/build/release/4.4.1/sage-4.4.1.alpha1$ ./sage -t  -long "local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/twist.py"
sage -t -long "local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/twist.py"
 **********************************************************************
File "/mnt/usb1/scratch/wstein/build/release/4.4.1/sage-4.4.1.alpha1/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/twist.py", line 1696:
    sage: E.render(ctx)
Expected:
    <RedirectResponse 301 Document moved to over there.>
Got:
    <sagenb.notebook.twist.RedirectResponse code=303, streamlen=None>
**********************************************************************
1 items had failures:
   1 of  15 in __main__.example_30
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_twist.py
         [4.0 s]

----------------------------------------------------------------------
The following tests failed:


        sage -t -long "local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/twist.py"
Total time for all tests: 4.0 seconds
```


This is a result of #8725.

Issue created by migration from https://trac.sagemath.org/ticket/8812





---

archive/issue_comments_080895.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-04-29T01:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8812#issuecomment-80895",
    "user": "acleone"
}
```

Resolution: duplicate



---

archive/issue_comments_080896.json:
```json
{
    "body": "Already a patch up at #8724",
    "created_at": "2010-04-29T01:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8812#issuecomment-80896",
    "user": "acleone"
}
```

Already a patch up at #8724
