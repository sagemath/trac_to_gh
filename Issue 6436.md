# Issue 6436: ideal([]) gives unhelpful error message

archive/issues_006436.json:
```json
{
    "body": "Assignee: tbd\n\nWhen I type \"ideal([])\" in Sage 4.0.1 I get an error message intended for a different case:\n\n\n```\nsage: ideal([])\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n...\nTypeError: unable to find common ring into which all ideal generators map\n```\n\n\nThis error message is incorrect since, trivially, the empty set of generators will map into any ring at all. The attached patch changes this to\n\n\n```\nsage: ideal([])\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n...\nValueError: unable to determine which ring to embed the ideal in\n```\n\n\nBy the way, the function ideal in ideal.py has a documentation section named TESTS with doctests in it. As far as I can determine, these doctests do not get run.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6436\n\n",
    "created_at": "2009-06-27T22:55:50Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "ideal([]) gives unhelpful error message",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6436",
    "user": "broune"
}
```
Assignee: tbd

When I type "ideal([])" in Sage 4.0.1 I get an error message intended for a different case:


```
sage: ideal([])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: unable to find common ring into which all ideal generators map
```


This error message is incorrect since, trivially, the empty set of generators will map into any ring at all. The attached patch changes this to


```
sage: ideal([])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: unable to determine which ring to embed the ideal in
```


By the way, the function ideal in ideal.py has a documentation section named TESTS with doctests in it. As far as I can determine, these doctests do not get run.

Issue created by migration from https://trac.sagemath.org/ticket/6436





---

archive/issue_comments_051665.json:
```json
{
    "body": "Attachment [ideal_empty_list.patch](tarball://root/attachments/some-uuid/ticket6436/ideal_empty_list.patch) by jhpalmieri created at 2009-06-28 01:41:17\n\n> By the way, the function ideal in ideal.py has a documentation section named TESTS with doctests in it. As far as I can determine, these doctests do not get run.\n\nI'm not sure why you say this.  If you add lines like\n\n```\nsage: 3+5\n9\n```\n\nto that section, you get a doctest failure.  At least, I do.  I think that your addition to that section doesn't produce an error because it starts with `Sage:`, not `sage:`.  Since you already test this failure earlier, I'm adding a referee's patch deleting this non-doctest from the TESTS section, and also fixing a small reST issue.",
    "created_at": "2009-06-28T01:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6436#issuecomment-51665",
    "user": "jhpalmieri"
}
```

Attachment [ideal_empty_list.patch](tarball://root/attachments/some-uuid/ticket6436/ideal_empty_list.patch) by jhpalmieri created at 2009-06-28 01:41:17

> By the way, the function ideal in ideal.py has a documentation section named TESTS with doctests in it. As far as I can determine, these doctests do not get run.

I'm not sure why you say this.  If you add lines like

```
sage: 3+5
9
```

to that section, you get a doctest failure.  At least, I do.  I think that your addition to that section doesn't produce an error because it starts with `Sage:`, not `sage:`.  Since you already test this failure earlier, I'm adding a referee's patch deleting this non-doctest from the TESTS section, and also fixing a small reST issue.



---

archive/issue_comments_051666.json:
```json
{
    "body": "Attachment [ref_6436.patch](tarball://root/attachments/some-uuid/ticket6436/ref_6436.patch) by jhpalmieri created at 2009-06-28 01:41:49",
    "created_at": "2009-06-28T01:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6436#issuecomment-51666",
    "user": "jhpalmieri"
}
```

Attachment [ref_6436.patch](tarball://root/attachments/some-uuid/ticket6436/ref_6436.patch) by jhpalmieri created at 2009-06-28 01:41:49



---

archive/issue_comments_051667.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-04T01:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6436#issuecomment-51667",
    "user": "rlm"
}
```

Resolution: fixed
