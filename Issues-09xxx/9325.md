# Issue 9325: Bugs concerning coding comments and docstrings in sage-preparse

archive/issues_009325.json:
```json
{
    "body": "Assignee: @jasongrout\n\nKeywords: preparse docstring\n\nI found (and fixed) a few Bugs in the file local/bin/sage-preparse.\n\nThese are the things I fixed:\n\n* The module docstrings disappeared when preparsing because the\npreparse_file function inserted those numeric_literals definitions before\nthe docstrings.\n\n* Now also unicode-docstrings (e.g. u\"\"\"foo\"\"\") are recognized as\ndocstrings. Also raw docstrings may now use an upper case R as string\nmodifier (R\"\"\"foo\"\"\" would work now) which is allowed in Python.\n\n* Now all coding-comments as specified by Python are found and excluded\nfrom preparsing.\n\n* I did not fix a bug that occurs when a statement is on the same line\nwhere the docstring ends, e.g.\n\n```\n\"\"\"foo\"\"\"; print 2^5\n```\nIt will not be preparsed! I added a TODO-comment on the according line. \n\ngreetings,\nDavid Poetzsch-Heffter\n\nIssue created by migration from https://trac.sagemath.org/ticket/9325\n\n",
    "created_at": "2010-06-24T10:02:02Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "title": "Bugs concerning coding comments and docstrings in sage-preparse",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9325",
    "user": "https://trac.sagemath.org/admin/accounts/users/dpoetzsch"
}
```
Assignee: @jasongrout

Keywords: preparse docstring

I found (and fixed) a few Bugs in the file local/bin/sage-preparse.

These are the things I fixed:

* The module docstrings disappeared when preparsing because the
preparse_file function inserted those numeric_literals definitions before
the docstrings.

* Now also unicode-docstrings (e.g. u"""foo""") are recognized as
docstrings. Also raw docstrings may now use an upper case R as string
modifier (R"""foo""" would work now) which is allowed in Python.

* Now all coding-comments as specified by Python are found and excluded
from preparsing.

* I did not fix a bug that occurs when a statement is on the same line
where the docstring ends, e.g.

```
"""foo"""; print 2^5
```
It will not be preparsed! I added a TODO-comment on the according line. 

greetings,
David Poetzsch-Heffter

Issue created by migration from https://trac.sagemath.org/ticket/9325





---

archive/issue_comments_087800.json:
```json
{
    "body": "Changing assignee from @ncalexan to @jasongrout.",
    "created_at": "2010-06-24T10:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9325#issuecomment-87800",
    "user": "https://trac.sagemath.org/admin/accounts/users/dpoetzsch"
}
```

Changing assignee from @ncalexan to @jasongrout.



---

archive/issue_comments_087801.json:
```json
{
    "body": "Changing component from sage-mode to misc.",
    "created_at": "2010-06-24T10:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9325#issuecomment-87801",
    "user": "https://trac.sagemath.org/admin/accounts/users/dpoetzsch"
}
```

Changing component from sage-mode to misc.



---

archive/issue_comments_087802.json:
```json
{
    "body": "Bugfixes",
    "created_at": "2010-06-24T10:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9325#issuecomment-87802",
    "user": "https://trac.sagemath.org/admin/accounts/users/dpoetzsch"
}
```

Bugfixes



---

archive/issue_comments_087803.json:
```json
{
    "body": "Attachment [1474.patch](tarball://root/attachments/some-uuid/ticket9325/1474.patch) by dpoetzsch created at 2010-06-24 12:32:37",
    "created_at": "2010-06-24T12:32:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9325#issuecomment-87803",
    "user": "https://trac.sagemath.org/admin/accounts/users/dpoetzsch"
}
```

Attachment [1474.patch](tarball://root/attachments/some-uuid/ticket9325/1474.patch) by dpoetzsch created at 2010-06-24 12:32:37



---

archive/issue_comments_087804.json:
```json
{
    "body": "Thanks for creating this ticket and working on it! I was about just to create one to suggest that the encoding lines \"# -*- coding: utf-8 -*-\" would not be stripped away.",
    "created_at": "2010-07-01T09:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9325#issuecomment-87804",
    "user": "https://github.com/nthiery"
}
```

Thanks for creating this ticket and working on it! I was about just to create one to suggest that the encoding lines "# -*- coding: utf-8 -*-" would not be stripped away.



---

archive/issue_comments_087805.json:
```json
{
    "body": "Replying to [comment:3 nthiery]:\n> Thanks for creating this ticket and working on it! I was about just to create one to suggest that the encoding lines \"# -*- coding: utf-8 -*-\" would not be stripped away.\n\n\nOops, never mind. This line is already propagated properly. Mine had a double # at the beginning.",
    "created_at": "2010-07-01T09:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9325#issuecomment-87805",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:3 nthiery]:
> Thanks for creating this ticket and working on it! I was about just to create one to suggest that the encoding lines "# -*- coding: utf-8 -*-" would not be stripped away.


Oops, never mind. This line is already propagated properly. Mine had a double # at the beginning.
