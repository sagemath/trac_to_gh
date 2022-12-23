# Issue 3730: Sage scripts ending with .py

archive/issues_003730.json:
```json
{
    "body": "Assignee: tba\n\nDebian's automated Python byte-compilation tool determines what's a python script based on whether it has extention .py (yeah, I know, pretty lame), and is apparently stupid enough to look in /usr/share/doc/sagemath/examples for things needing byte-compilation.\n\nUnfortunately, /usr/share/doc/sagemath/examples/example.py is a .py with a #!/usr/bin/sage and which apparently isn't entirely valid python (the last line causes the byte-compiler to fail):\n\n\n```\nCompiling /usr/share/sagemath/examples/example.py ...\n  File \"/usr/share/sagemath/examples/example.py\", line 62\n    time factor(Integer(2)**Integer(127)-Integer(1))\n              ^\nSyntaxError: invalid syntax\n```\n\n\nThe corresponding file example.sage seems to not exist, so I'm not sure what the story with that file is.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3730\n\n",
    "created_at": "2008-07-27T03:37:25Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "Sage scripts ending with .py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3730",
    "user": "tabbott"
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

archive/issue_comments_026484.json:
```json
{
    "body": "To be clear, I think this is the only instance of this problem in the distribution.",
    "created_at": "2008-07-27T04:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3730#issuecomment-26484",
    "user": "tabbott"
}
```

To be clear, I think this is the only instance of this problem in the distribution.



---

archive/issue_comments_026485.json:
```json
{
    "body": "Given that the examples/ directory is gone, this is no longer valid.",
    "created_at": "2012-06-01T18:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3730#issuecomment-26485",
    "user": "kcrisman"
}
```

Given that the examples/ directory is gone, this is no longer valid.



---

archive/issue_comments_026486.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-01T18:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3730#issuecomment-26486",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_026487.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-01T18:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3730#issuecomment-26487",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_026488.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-06-02T12:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3730#issuecomment-26488",
    "user": "jdemeyer"
}
```

Resolution: invalid
