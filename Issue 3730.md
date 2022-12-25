# Issue 3730: Sage scripts ending with .py

archive/issues_003730.json:
```json
{
    "body": "Assignee: tba\n\nDebian's automated Python byte-compilation tool determines what's a python script based on whether it has extention .py (yeah, I know, pretty lame), and is apparently stupid enough to look in /usr/share/doc/sagemath/examples for things needing byte-compilation.\n\nUnfortunately, /usr/share/doc/sagemath/examples/example.py is a .py with a #!/usr/bin/sage and which apparently isn't entirely valid python (the last line causes the byte-compiler to fail):\n\n```\nCompiling /usr/share/sagemath/examples/example.py ...\n  File \"/usr/share/sagemath/examples/example.py\", line 62\n    time factor(Integer(2)**Integer(127)-Integer(1))\n              ^\nSyntaxError: invalid syntax\n```\n\nThe corresponding file example.sage seems to not exist, so I'm not sure what the story with that file is.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3730\n\n",
    "created_at": "2008-07-27T03:37:25Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage scripts ending with .py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3730",
    "user": "https://github.com/timabbott"
}
```
Assignee: tba

Debian's automated Python byte-compilation tool determines what's a python script based on whether it has extention .py (yeah, I know, pretty lame), and is apparently stupid enough to look in /usr/share/doc/sagemath/examples for things needing byte-compilation.

Unfortunately, /usr/share/doc/sagemath/examples/example.py is a .py with a #!/usr/bin/sage and which apparently isn't entirely valid python (the last line causes the byte-compiler to fail):

```
Compiling /usr/share/sagemath/examples/example.py ...
  File "/usr/share/sagemath/examples/example.py", line 62
    time factor(Integer(2)**Integer(127)-Integer(1))
              ^
SyntaxError: invalid syntax
```

The corresponding file example.sage seems to not exist, so I'm not sure what the story with that file is.

Issue created by migration from https://trac.sagemath.org/ticket/3730





---

archive/issue_comments_026427.json:
```json
{
    "body": "To be clear, I think this is the only instance of this problem in the distribution.",
    "created_at": "2008-07-27T04:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3730#issuecomment-26427",
    "user": "https://github.com/timabbott"
}
```

To be clear, I think this is the only instance of this problem in the distribution.



---

archive/issue_events_008537.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-29T16:11:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3730",
    "milestone": "sage-3.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3730#event-8537"
}
```



---

archive/issue_events_008538.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2012-06-01T18:05:41Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3730",
    "milestone": "sage-3.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3730#event-8538"
}
```



---

archive/issue_events_008539.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2012-06-01T18:05:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3730",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3730#event-8539"
}
```



---

archive/issue_comments_026428.json:
```json
{
    "body": "Given that the examples/ directory is gone, this is no longer valid.",
    "created_at": "2012-06-01T18:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3730#issuecomment-26428",
    "user": "https://github.com/kcrisman"
}
```

Given that the examples/ directory is gone, this is no longer valid.



---

archive/issue_comments_026429.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-01T18:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3730#issuecomment-26429",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_026430.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-01T18:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3730#issuecomment-26430",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008540.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-06-02T12:35:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3730",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3730#event-8540"
}
```



---

archive/issue_comments_026431.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-06-02T12:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3730#issuecomment-26431",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid
