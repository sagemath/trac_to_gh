# Issue 2229: sage-2.10.2.alpha1 -- breakage in new totally_rel.py

archive/issues_002229.json:
```json
{
    "body": "Assignee: was\n\nI don't know about this code at all, but something is messed up:\n\n```\n         [2.8 s]\nsage -t  devel/sage-main/sage/rings/number_field/totallyreal_rel.py**********************************************************************\nFile \"totallyreal_rel.py\", line 654:\n    sage: [NumberField(ZZx(_[i][1]), 't').is_galois() for i in range(len(_))]\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[7]>\", line 1, in <module>\n        [NumberField(ZZx(_[i][Integer(1)]), 't').is_galois() for i in range(len(_))]###line 654:\n    sage: [NumberField(ZZx(_[i][1]), 't').is_galois() for i in range(len(_))]\n    TypeError: 'int' object is unsubscriptable\n**********************************************************************\n1 items had failures:\n   1 of  11 in __main__.example_6\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_totallyreal_rel.py\n         [50.8 s]\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2229\n\n",
    "created_at": "2008-02-20T07:03:35Z",
    "labels": [
        "number theory",
        "blocker",
        "bug"
    ],
    "title": "sage-2.10.2.alpha1 -- breakage in new totally_rel.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2229",
    "user": "was"
}
```
Assignee: was

I don't know about this code at all, but something is messed up:

```
         [2.8 s]
sage -t  devel/sage-main/sage/rings/number_field/totallyreal_rel.py**********************************************************************
File "totallyreal_rel.py", line 654:
    sage: [NumberField(ZZx(_[i][1]), 't').is_galois() for i in range(len(_))]
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[7]>", line 1, in <module>
        [NumberField(ZZx(_[i][Integer(1)]), 't').is_galois() for i in range(len(_))]###line 654:
    sage: [NumberField(ZZx(_[i][1]), 't').is_galois() for i in range(len(_))]
    TypeError: 'int' object is unsubscriptable
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_totallyreal_rel.py
         [50.8 s]

```


Issue created by migration from https://trac.sagemath.org/ticket/2229





---

archive/issue_comments_014765.json:
```json
{
    "body": "Changing assignee from was to craigcitro.",
    "created_at": "2008-02-20T20:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2229#issuecomment-14765",
    "user": "craigcitro"
}
```

Changing assignee from was to craigcitro.



---

archive/issue_comments_014766.json:
```json
{
    "body": "So I don't see this doctest failure on my machine, but looking at the doctests, they're clearly nonsense (i.e. the above error *should* be showing up on my machine). I'm very curious why it doesn't.\n\nIn any event, the attached patch *should* fix it.",
    "created_at": "2008-02-20T20:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2229#issuecomment-14766",
    "user": "craigcitro"
}
```

So I don't see this doctest failure on my machine, but looking at the doctests, they're clearly nonsense (i.e. the above error *should* be showing up on my machine). I'm very curious why it doesn't.

In any event, the attached patch *should* fix it.



---

archive/issue_comments_014767.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-20T20:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2229#issuecomment-14767",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014768.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-20T20:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2229#issuecomment-14768",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_014769.json:
```json
{
    "body": "The patch fixes the doctest failure, positive review.",
    "created_at": "2008-02-20T20:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2229#issuecomment-14769",
    "user": "mabshoff"
}
```

The patch fixes the doctest failure, positive review.



---

archive/issue_comments_014770.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-20T20:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2229#issuecomment-14770",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014771.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha2",
    "created_at": "2008-02-20T20:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2229#issuecomment-14771",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha2
