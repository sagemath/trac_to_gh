# Issue 9325: Bugs concerning coding comments and docstrings in sage-preparse

archive/issues_009325.json:
```json
{
    "body": "Assignee: ncalexan\n\nKeywords: preparse docstring\n\nI found (and fixed) a few Bugs in the file local/bin/sage-preparse.\n\nThese are the things I fixed:\n\n* The module docstrings disappeared when preparsing because the\npreparse_file function inserted those numeric_literals definitions before\nthe docstrings.\n\n* Now also unicode-docstrings (e.g. u\"\"\"foo\"\"\") are recognized as\ndocstrings. Also raw docstrings may now use an upper case R as string\nmodifier (R\"\"\"foo\"\"\" would work now) which is allowed in Python.\n\n* Now all coding-comments as specified by Python are found and excluded\nfrom preparsing.\n\n* I did not fix a bug that occurs when a statement is on the same line\nwhere the docstring ends (e.g. \"\"\"foo\"\"\"; print 2^5). It will not be\npreparsed! I added a TODO-comment on the according line. \n\ngreetings,\nDavid Poetzsch-Heffter\n\nIssue created by migration from https://trac.sagemath.org/ticket/9325\n\n",
    "created_at": "2010-06-24T10:02:02Z",
    "labels": [
        "sage-mode",
        "major",
        "bug"
    ],
    "title": "Bugs concerning coding comments and docstrings in sage-preparse",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9325",
    "user": "dpoetzsch"
}
```
Assignee: ncalexan

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
where the docstring ends (e.g. """foo"""; print 2^5). It will not be
preparsed! I added a TODO-comment on the according line. 

greetings,
David Poetzsch-Heffter

Issue created by migration from https://trac.sagemath.org/ticket/9325





---

archive/issue_comments_087939.json:
```json
{
    "body": "Changing assignee from ncalexan to jason.",
    "created_at": "2010-06-24T10:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9325#issuecomment-87939",
    "user": "dpoetzsch"
}
```

Changing assignee from ncalexan to jason.



---

archive/issue_comments_087940.json:
```json
{
    "body": "Changing component from sage-mode to misc.",
    "created_at": "2010-06-24T10:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9325#issuecomment-87940",
    "user": "dpoetzsch"
}
```

Changing component from sage-mode to misc.



---

archive/issue_comments_087941.json:
```json
{
    "body": "Bugfixes",
    "created_at": "2010-06-24T10:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9325#issuecomment-87941",
    "user": "dpoetzsch"
}
```

Bugfixes



---

archive/issue_comments_087942.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-06-24T12:32:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9325#issuecomment-87942",
    "user": "dpoetzsch"
}
```

Attachment



---

archive/issue_comments_087943.json:
```json
{
    "body": "Thanks for creating this ticket and working on it! I was about just to create one to suggest that the encoding lines \"# -*- coding: utf-8 -*-\" would not be stripped away.",
    "created_at": "2010-07-01T09:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9325#issuecomment-87943",
    "user": "nthiery"
}
```

Thanks for creating this ticket and working on it! I was about just to create one to suggest that the encoding lines "# -*- coding: utf-8 -*-" would not be stripped away.



---

archive/issue_comments_087944.json:
```json
{
    "body": "Replying to [comment:3 nthiery]:\n> Thanks for creating this ticket and working on it! I was about just to create one to suggest that the encoding lines \"# -*- coding: utf-8 -*-\" would not be stripped away.\n\nOops, never mind. This line is already propagated properly. Mine had a double # at the beginning.",
    "created_at": "2010-07-01T09:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9325#issuecomment-87944",
    "user": "nthiery"
}
```

Replying to [comment:3 nthiery]:
> Thanks for creating this ticket and working on it! I was about just to create one to suggest that the encoding lines "# -*- coding: utf-8 -*-" would not be stripped away.

Oops, never mind. This line is already propagated properly. Mine had a double # at the beginning.
