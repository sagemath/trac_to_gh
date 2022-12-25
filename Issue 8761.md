# Issue 8761: sage notebook: make a new interact control (like selector) that really works like a button

archive/issues_008761.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @kcrisman @jhpalmieri boothby\n\nFirst, see this screenshot:\n   http://sage.math.washington.edu/home/wstein/tmp/button.png\n\nNow imagine that when you push either of the buttons, the interact is triggered and the button comes back up (it does not get *stuck* down as a selector).  \n\nWhen the interact triggers calling of the function, if this is triggered by a button being clicked then the corresponding variable is set to the value of that button (usually the text label).  Otherwise, the variable is set to None.  Then interact applications can tell if a button being pushed triggered the function being called based on whether or not the variable is None.\n\n\n```\n@interact\ndef f(X = button(['Ok', 'Cancel', \"Continue\"])):\n    print X\n```\n\n\nNotice that button is much like selector with buttons=True...\n\nIssue created by migration from https://trac.sagemath.org/ticket/8761\n\n",
    "created_at": "2010-04-25T01:11:12Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage notebook: make a new interact control (like selector) that really works like a button",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8761",
    "user": "https://github.com/williamstein"
}
```
Assignee: jason, was

CC:  @kcrisman @jhpalmieri boothby

First, see this screenshot:
   http://sage.math.washington.edu/home/wstein/tmp/button.png

Now imagine that when you push either of the buttons, the interact is triggered and the button comes back up (it does not get *stuck* down as a selector).  

When the interact triggers calling of the function, if this is triggered by a button being clicked then the corresponding variable is set to the value of that button (usually the text label).  Otherwise, the variable is set to None.  Then interact applications can tell if a button being pushed triggered the function being called based on whether or not the variable is None.


```
@interact
def f(X = button(['Ok', 'Cancel', "Continue"])):
    print X
```


Notice that button is much like selector with buttons=True...

Issue created by migration from https://trac.sagemath.org/ticket/8761





---

archive/issue_comments_080027.json:
```json
{
    "body": "ancient ticket about deprecated sagenb, can we close ?",
    "created_at": "2020-04-04T06:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8761#issuecomment-80027",
    "user": "https://github.com/fchapoton"
}
```

ancient ticket about deprecated sagenb, can we close ?



---

archive/issue_comments_080028.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-04-04T06:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8761#issuecomment-80028",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080029.json:
```json
{
    "body": "Yes, I think so.",
    "created_at": "2020-04-04T21:44:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8761#issuecomment-80029",
    "user": "https://github.com/jhpalmieri"
}
```

Yes, I think so.



---

archive/issue_comments_080030.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-04-04T21:44:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8761#issuecomment-80030",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080031.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2020-04-05T06:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8761#issuecomment-80031",
    "user": "https://github.com/fchapoton"
}
```

Resolution: wontfix
