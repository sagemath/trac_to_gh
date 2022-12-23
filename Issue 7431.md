# Issue 7431: @interact and %hide don't play nice together

archive/issues_007431.json:
```json
{
    "body": "Assignee: itolkov\n\nCC:  jason\n\n\n```\n%hide \n@interact \ndef _(n=2): \n    f(x,y)=x^n \n    show(plot(f,(x,0,1))) \n```\n\ndoesn't work well, especially if you update the interact. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7431\n\n",
    "created_at": "2009-11-11T19:47:36Z",
    "labels": [
        "interact",
        "major",
        "bug"
    ],
    "title": "@interact and %hide don't play nice together",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7431",
    "user": "kcrisman"
}
```
Assignee: itolkov

CC:  jason


```
%hide 
@interact 
def _(n=2): 
    f(x,y)=x^n 
    show(plot(f,(x,0,1))) 
```

doesn't work well, especially if you update the interact. 

Issue created by migration from https://trac.sagemath.org/ticket/7431





---

archive/issue_comments_062527.json:
```json
{
    "body": "Update on this:  Interact does work with hide, but for some reason only after you save, quit, and restart.  Why???",
    "created_at": "2010-01-04T20:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7431#issuecomment-62527",
    "user": "kcrisman"
}
```

Update on this:  Interact does work with hide, but for some reason only after you save, quit, and restart.  Why???



---

archive/issue_comments_062528.json:
```json
{
    "body": "Another update:  Lately, it's been working, but only if I remove the focus from that cell, then use the interact.  Anyway, it's confusing.  Perhaps someone else will have input.  Changing priority since no one else has touched this, though.",
    "created_at": "2010-04-22T01:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7431#issuecomment-62528",
    "user": "kcrisman"
}
```

Another update:  Lately, it's been working, but only if I remove the focus from that cell, then use the interact.  Anyway, it's confusing.  Perhaps someone else will have input.  Changing priority since no one else has touched this, though.



---

archive/issue_comments_062529.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-04-22T01:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7431#issuecomment-62529",
    "user": "kcrisman"
}
```

Changing priority from major to minor.
