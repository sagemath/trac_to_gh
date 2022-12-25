# Issue 8460: doctest failure sagenb-0.7.5.1-py2.6.egg/sagenb/misc/sageinspect.py

archive/issues_008460.json:
```json
{
    "body": "Assignee: @williamstein\n\nI get this failure on Solaris 10, on SPARC using a modified version of the 4.3.4.alpha0 sources. (All modifications were necessary to get Sage to build). \n\n\n```\n**********************************************************************\nFile \"/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/misc/sageinspect.py\", line 562:\n    sage: sage_getsourcelines(matrix, True)[1]\nExpected:\n    33\nGot:\n    34\n**********************************************************************\n```\n\n\n\nI'm guessing a bit about the category for his. I'll this if I have chosen the wrong category. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8460\n\n",
    "created_at": "2010-03-06T22:13:05Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "doctest failure sagenb-0.7.5.1-py2.6.egg/sagenb/misc/sageinspect.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8460",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: @williamstein

I get this failure on Solaris 10, on SPARC using a modified version of the 4.3.4.alpha0 sources. (All modifications were necessary to get Sage to build). 


```
**********************************************************************
File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/misc/sageinspect.py", line 562:
    sage: sage_getsourcelines(matrix, True)[1]
Expected:
    33
Got:
    34
**********************************************************************
```



I'm guessing a bit about the category for his. I'll this if I have chosen the wrong category. 

Issue created by migration from https://trac.sagemath.org/ticket/8460





---

archive/issue_comments_076041.json:
```json
{
    "body": "This happens to be part of #8430 and the fix from #8324 is part of #8435.",
    "created_at": "2010-03-09T06:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8460#issuecomment-76041",
    "user": "https://github.com/qed777"
}
```

This happens to be part of #8430 and the fix from #8324 is part of #8435.



---

archive/issue_events_008644.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-03-09T06:41:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8460",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8460#event-8644"
}
```



---

archive/issue_comments_076042.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-09T06:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8460#issuecomment-76042",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
