# Issue 1062: gp interface help should use extended help text (from "??")

archive/issues_001062.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @videlec @jdemeyer @slel\n\n\n```\n<wstein> \n The new ?? help looks quite nice. It would\n be good for gp.foo? to use it.\n```\n\n\nThe idea is that\n\n```\nsage: foo = gp(x)\nsage: foo.polroots?\n```\n\n\nshould use the help text from the gp command `??polroots`.\n\nThe obvious approach is to change '?%s' to '??%s' in gp.py's help() method.  This doesn't quite work, for two reasons:\n\n1) gphelp carefully formats the text to fit in the current line width, and then Sage displays this text indented; so almost every line wraps.\n\n2) gphelp uses control characters to make words bold, underlined, etc.; when the help is viewed from the notebook, these control codes are visible in the output, and look very ugly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1062\n\n",
    "created_at": "2007-11-02T01:31:09Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "gp interface help should use extended help text (from \"??\")",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1062",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

CC:  @videlec @jdemeyer @slel


```
<wstein> 
 The new ?? help looks quite nice. It would
 be good for gp.foo? to use it.
```


The idea is that

```
sage: foo = gp(x)
sage: foo.polroots?
```


should use the help text from the gp command `??polroots`.

The obvious approach is to change '?%s' to '??%s' in gp.py's help() method.  This doesn't quite work, for two reasons:

1) gphelp carefully formats the text to fit in the current line width, and then Sage displays this text indented; so almost every line wraps.

2) gphelp uses control characters to make words bold, underlined, etc.; when the help is viewed from the notebook, these control codes are visible in the output, and look very ugly.

Issue created by migration from https://trac.sagemath.org/ticket/1062





---

archive/issue_comments_006429.json:
```json
{
    "body": "See #17860 for a possible strategy.",
    "created_at": "2015-04-13T13:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1062#issuecomment-6429",
    "user": "https://github.com/mezzarobba"
}
```

See #17860 for a possible strategy.



---

archive/issue_comments_006430.json:
```json
{
    "body": "Changing keywords from \"\" to \"pari/gp, help\".",
    "created_at": "2018-11-23T08:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1062#issuecomment-6430",
    "user": "https://github.com/slel"
}
```

Changing keywords from "" to "pari/gp, help".



---

archive/issue_comments_006431.json:
```json
{
    "body": "This works in `cypari2` which is de facto the way to use PARI in Sage\n\n```\nsage: x.polroots?\nSignature:      x.polroots(precision)\nDocstring:     \n   Complex roots of the given polynomial using Schonhage's method, as\n   modified by Gourdon.\n```\n",
    "created_at": "2020-02-17T13:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1062#issuecomment-6431",
    "user": "https://github.com/videlec"
}
```

This works in `cypari2` which is de facto the way to use PARI in Sage

```
sage: x.polroots?
Signature:      x.polroots(precision)
Docstring:     
   Complex roots of the given polynomial using Schonhage's method, as
   modified by Gourdon.
```




---

archive/issue_comments_006432.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-02-17T13:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1062#issuecomment-6432",
    "user": "https://github.com/videlec"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_006433.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-04-04T22:30:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1062#issuecomment-6433",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_006434.json:
```json
{
    "body": "I do not agree that this works. We currently display only the short documentation, for pari() objects as well as for gp() objects.\n\nThe complete doc is much longer.",
    "created_at": "2020-06-20T06:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1062#issuecomment-6434",
    "user": "https://github.com/fchapoton"
}
```

I do not agree that this works. We currently display only the short documentation, for pari() objects as well as for gp() objects.

The complete doc is much longer.



---

archive/issue_comments_006435.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2020-06-20T06:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1062#issuecomment-6435",
    "user": "https://github.com/fchapoton"
}
```

Changing status from positive_review to needs_info.
