# Issue 1921: add random_element to groups

archive/issues_001921.json:
```json
{
    "body": "Assignee: joyner\n\nCurrently, at least some of the groups G in SAGE access a random\nelement using G.random(). (This was borrowed from GAP's syntax.) \nThe default for a ring R in SAGE seems to be R.random_element(). \nThe function call should be the same in both cases, \nso for now add G.random_element() and in the future maybe deprecate\nG.random().\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1921\n\n",
    "created_at": "2008-01-25T06:09:48Z",
    "labels": [
        "group theory",
        "minor",
        "bug"
    ],
    "title": "add random_element to groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1921",
    "user": "wdj"
}
```
Assignee: joyner

Currently, at least some of the groups G in SAGE access a random
element using G.random(). (This was borrowed from GAP's syntax.) 
The default for a ring R in SAGE seems to be R.random_element(). 
The function call should be the same in both cases, 
so for now add G.random_element() and in the future maybe deprecate
G.random().


Issue created by migration from https://trac.sagemath.org/ticket/1921





---

archive/issue_comments_012179.json:
```json
{
    "body": "I greatly prefer random_element to random.  I think random is unclear about what it does, and of course inconsistent.  random_element is crystal clear.  I also use to use random in various places, since in Magma the command is `Random`. \n\nThere are current 28 instances of the random function in Sage:\n\n```\nsage: search_src('def random(')\n```\n\n\nThere are 36 instances of random_element.\n\n```\nsage: search_src('def random_element(')\n```\n\n\nIt would make the most sense to remove all the random(...) methods and\nreplace them by random_element throughout.  If we make all the random(...)\nmethods do a \n\n```\n    raise Deprecated\n```\n\nthen I hope those really do disappear completely within 2 months (say). ??",
    "created_at": "2008-01-25T06:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1921#issuecomment-12179",
    "user": "was"
}
```

I greatly prefer random_element to random.  I think random is unclear about what it does, and of course inconsistent.  random_element is crystal clear.  I also use to use random in various places, since in Magma the command is `Random`. 

There are current 28 instances of the random function in Sage:

```
sage: search_src('def random(')
```


There are 36 instances of random_element.

```
sage: search_src('def random_element(')
```


It would make the most sense to remove all the random(...) methods and
replace them by random_element throughout.  If we make all the random(...)
methods do a 

```
    raise Deprecated
```

then I hope those really do disappear completely within 2 months (say). ??



---

archive/issue_comments_012180.json:
```json
{
    "body": "Attachment [1921-doc.patch](tarball://root/attachments/some-uuid/ticket1921/1921-doc.patch) by AlexGhitza created at 2008-04-17 02:36:01\n\ndoc patch",
    "created_at": "2008-04-17T02:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1921#issuecomment-12180",
    "user": "AlexGhitza"
}
```

Attachment [1921-doc.patch](tarball://root/attachments/some-uuid/ticket1921/1921-doc.patch) by AlexGhitza created at 2008-04-17 02:36:01

doc patch



---

archive/issue_comments_012181.json:
```json
{
    "body": "The attached patch renames all .random() methods to random_element() and adds a NotImplementedError deprecated message to .random().\n\nThis change messes up a doctest in the tutorial, so there is also a small doc patch for that.",
    "created_at": "2008-04-17T02:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1921#issuecomment-12181",
    "user": "AlexGhitza"
}
```

The attached patch renames all .random() methods to random_element() and adds a NotImplementedError deprecated message to .random().

This change messes up a doctest in the tutorial, so there is also a small doc patch for that.



---

archive/issue_comments_012182.json:
```json
{
    "body": "Attachment [1921-1.patch](tarball://root/attachments/some-uuid/ticket1921/1921-1.patch) by mhansen created at 2008-04-26 02:24:19",
    "created_at": "2008-04-26T02:24:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1921#issuecomment-12182",
    "user": "mhansen"
}
```

Attachment [1921-1.patch](tarball://root/attachments/some-uuid/ticket1921/1921-1.patch) by mhansen created at 2008-04-26 02:24:19



---

archive/issue_comments_012183.json:
```json
{
    "body": "I fixed a few things up in the combinat/ directory.\n\nOther than that, looks good to me.  Apply the last two patches.",
    "created_at": "2008-04-26T02:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1921#issuecomment-12183",
    "user": "mhansen"
}
```

I fixed a few things up in the combinat/ directory.

Other than that, looks good to me.  Apply the last two patches.



---

archive/issue_comments_012184.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-26T02:49:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1921#issuecomment-12184",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012185.json:
```json
{
    "body": "Merged 1921-doc.patch and 1921-1.patch in Sage 3.0.1.alpha0",
    "created_at": "2008-04-26T02:49:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1921#issuecomment-12185",
    "user": "mabshoff"
}
```

Merged 1921-doc.patch and 1921-1.patch in Sage 3.0.1.alpha0
