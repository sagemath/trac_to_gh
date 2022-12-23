# Issue 2722: [with patch; needs trivial review] interact -- a doctest problem

archive/issues_002722.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n>  Fedora 7 32 bits:\n>  \n>  sage -t  devel/sage-main/sage/server/notebook/interact.py   **********************************************************************\n>  File \"interact.py\", line 1420:\n>      sage: slider([1, 'x', 'abc', 2/3], None, None, 3, 'alpha')\n>  Expected:\n>      Slider: alpha [abc--|1|---1]\n>  Got:\n>      Slider: alpha [2/3--|1|---x]\n>  **********************************************************************\n>  1 items had failures:\n>     1 of   3 in __main__.example_62\n>  ***Test Failed*** 1 failures.\n>  For whitespace errors, see the file .doctest_interact.py\n>           [2.4 s]\n\n\nGood catch.  The right fix is to change the input that causes\nthat failure to:\n   sage: slider([1, 'x', 'abc', 2/3], None, None, 'abc', 'alpha')\n\nThis was caused by a change in the definition of the slider\nfunction, which results in extreme cases in system-specific\nbehavior.  \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2722\n\n",
    "created_at": "2008-03-29T17:43:25Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "[with patch; needs trivial review] interact -- a doctest problem",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2722",
    "user": "was"
}
```
Assignee: boothby


```
>  Fedora 7 32 bits:
>  
>  sage -t  devel/sage-main/sage/server/notebook/interact.py   **********************************************************************
>  File "interact.py", line 1420:
>      sage: slider([1, 'x', 'abc', 2/3], None, None, 3, 'alpha')
>  Expected:
>      Slider: alpha [abc--|1|---1]
>  Got:
>      Slider: alpha [2/3--|1|---x]
>  **********************************************************************
>  1 items had failures:
>     1 of   3 in __main__.example_62
>  ***Test Failed*** 1 failures.
>  For whitespace errors, see the file .doctest_interact.py
>           [2.4 s]


Good catch.  The right fix is to change the input that causes
that failure to:
   sage: slider([1, 'x', 'abc', 2/3], None, None, 'abc', 'alpha')

This was caused by a change in the definition of the slider
function, which results in extreme cases in system-specific
behavior.  
```


Issue created by migration from https://trac.sagemath.org/ticket/2722





---

archive/issue_comments_018762.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-29T17:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2722#issuecomment-18762",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_018763.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-03-29T17:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2722#issuecomment-18763",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_018764.json:
```json
{
    "body": "This worked for me on Fedora 7 32 bits.\n\n\n\n```\n[jaap@paix sage-2.11.alpha2]$ ./sage -t  devel/sage-main/sage/server/notebook/interact.py\nsage -t  devel/sage-main/sage/server/notebook/interact.py   \n         [3.6 s]\n \n----------------------------------------------------------------------\nAll tests passed!\n\n```\n\n\n\nJaap",
    "created_at": "2008-03-29T18:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2722#issuecomment-18764",
    "user": "jsp"
}
```

This worked for me on Fedora 7 32 bits.



```
[jaap@paix sage-2.11.alpha2]$ ./sage -t  devel/sage-main/sage/server/notebook/interact.py
sage -t  devel/sage-main/sage/server/notebook/interact.py   
         [3.6 s]
 
----------------------------------------------------------------------
All tests passed!

```



Jaap



---

archive/issue_comments_018765.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T18:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2722#issuecomment-18765",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.rc0



---

archive/issue_comments_018766.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T18:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2722",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2722#issuecomment-18766",
    "user": "mabshoff"
}
```

Resolution: fixed
