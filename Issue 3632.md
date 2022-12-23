# Issue 3632: [with patch, needs review] small bug in p-adic heights

archive/issues_003632.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: E = EllipticCurve([37,0])\nsage: E.padic_regulator(5)\n```\n\n\ngives a Assertion Error.\n\nThe included patch corrects this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3632\n\n",
    "created_at": "2008-07-10T13:11:05Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] small bug in p-adic heights",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3632",
    "user": "wuthrich"
}
```
Assignee: was


```
sage: E = EllipticCurve([37,0])
sage: E.padic_regulator(5)
```


gives a Assertion Error.

The included patch corrects this.

Issue created by migration from https://trac.sagemath.org/ticket/3632





---

archive/issue_comments_025691.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-10T13:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3632#issuecomment-25691",
    "user": "wuthrich"
}
```

Attachment



---

archive/issue_comments_025692.json:
```json
{
    "body": "I hate to do this.... it's obviously a perfectly good patch.... but the documentation needs to be updated too, and the loop in the doctests needs to test the m = 1 case, and somewhere you need to add a doctest showing the correct behaviour for the example you gave in the ticket description!",
    "created_at": "2008-07-10T23:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3632#issuecomment-25692",
    "user": "dmharvey"
}
```

I hate to do this.... it's obviously a perfectly good patch.... but the documentation needs to be updated too, and the loop in the doctests needs to test the m = 1 case, and somewhere you need to add a doctest showing the correct behaviour for the example you gave in the ticket description!



---

archive/issue_comments_025693.json:
```json
{
    "body": "Attachment\n\nOk. I added an additional patch (applied after the first) with some docstring. I hope that it is enough.",
    "created_at": "2008-07-11T10:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3632#issuecomment-25693",
    "user": "wuthrich"
}
```

Attachment

Ok. I added an additional patch (applied after the first) with some docstring. I hope that it is enough.



---

archive/issue_comments_025694.json:
```json
{
    "body": "Attachment\n\nhi, I've added yet a third patch, with minor changes to your patch, plus cleaning up some existing nearby doctests which didn't make sense to me. Assuming you are happy with these changes, I think this patch is good to go.\n\n(all three patches should be applied)",
    "created_at": "2008-07-11T13:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3632#issuecomment-25694",
    "user": "dmharvey"
}
```

Attachment

hi, I've added yet a third patch, with minor changes to your patch, plus cleaning up some existing nearby doctests which didn't make sense to me. Assuming you are happy with these changes, I think this patch is good to go.

(all three patches should be applied)



---

archive/issue_comments_025695.json:
```json
{
    "body": "Yop, that is fine with me. I guess I am allowed to change the 'summary'.",
    "created_at": "2008-07-14T09:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3632#issuecomment-25695",
    "user": "wuthrich"
}
```

Yop, that is fine with me. I guess I am allowed to change the 'summary'.



---

archive/issue_comments_025696.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-16T01:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3632#issuecomment-25696",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025697.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-16T01:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3632#issuecomment-25697",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.6.alpha0
