# Issue 8686: gettext related bug in _ (history)

archive/issues_008686.json:
```json
{
    "body": "Assignee: itolkov, jason\n\nCC:  was timdumol\n\nKeywords: gettext history documentation\n\nIn versions of Sage up to 4.3.2, the following worked as expected:\n\n\n```\n>./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: _?\n[...]\nsage: _\n''\nsage: _\n''\n```\n\n| Sage Version 4.3.2, Release Date: 2010-02-06                       |\n| Type notebook() for the GUI, and license() for information.        |\nHowever, with Sage 4.3.3, it has stopped working:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: _?\n[...]\nsage: _\n''\nsage: _\n<bound method NullTranslations.ugettext of <gettext.NullTranslations instance at 0x4b1a680>>\n```\n\n| Sage Version 4.3.3, Release Date: 2010-02-21                       |\n| Type notebook() for the GUI, and license() for information.        |\nFor some things, the history works as expected, but for others it does not.  To me it appears that it is \"simple\" things, e.g. above, the empty expression, or simple expressions like \"3+4\" where it does not work anymore, but for more complex things (e.g. if you call a function that returns something), \"_\" still does what you would expect it to do.\n\nThis bug still exists in Sage 4.3.5.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8686\n\n",
    "created_at": "2010-04-14T13:01:16Z",
    "labels": [
        "interact",
        "minor",
        "bug"
    ],
    "title": "gettext related bug in _ (history)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8686",
    "user": "logix"
}
```
Assignee: itolkov, jason

CC:  was timdumol

Keywords: gettext history documentation

In versions of Sage up to 4.3.2, the following worked as expected:


```
>./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: _?
[...]
sage: _
''
sage: _
''
```

| Sage Version 4.3.2, Release Date: 2010-02-06                       |
| Type notebook() for the GUI, and license() for information.        |
However, with Sage 4.3.3, it has stopped working:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: _?
[...]
sage: _
''
sage: _
<bound method NullTranslations.ugettext of <gettext.NullTranslations instance at 0x4b1a680>>
```

| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
For some things, the history works as expected, but for others it does not.  To me it appears that it is "simple" things, e.g. above, the empty expression, or simple expressions like "3+4" where it does not work anymore, but for more complex things (e.g. if you call a function that returns something), "_" still does what you would expect it to do.

This bug still exists in Sage 4.3.5.

Issue created by migration from https://trac.sagemath.org/ticket/8686





---

archive/issue_comments_079149.json:
```json
{
    "body": "Changing assignee from itolkov, jason to was.",
    "created_at": "2010-04-14T13:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8686#issuecomment-79149",
    "user": "logix"
}
```

Changing assignee from itolkov, jason to was.



---

archive/issue_comments_079150.json:
```json
{
    "body": "Changing component from interact to user interface.",
    "created_at": "2010-04-14T13:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8686#issuecomment-79150",
    "user": "logix"
}
```

Changing component from interact to user interface.



---

archive/issue_comments_079151.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-03T22:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8686#issuecomment-79151",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079152.json:
```json
{
    "body": "Attachment [trac_8686.patch](tarball://root/attachments/some-uuid/ticket8686/trac_8686.patch) by mhansen created at 2010-05-03 22:01:35",
    "created_at": "2010-05-03T22:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8686#issuecomment-79152",
    "user": "mhansen"
}
```

Attachment [trac_8686.patch](tarball://root/attachments/some-uuid/ticket8686/trac_8686.patch) by mhansen created at 2010-05-03 22:01:35



---

archive/issue_comments_079153.json:
```json
{
    "body": "Changing component from user interface to notebook.",
    "created_at": "2010-05-03T22:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8686#issuecomment-79153",
    "user": "mhansen"
}
```

Changing component from user interface to notebook.



---

archive/issue_comments_079154.json:
```json
{
    "body": "Nice debugging. Works as advertised.",
    "created_at": "2010-05-04T04:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8686#issuecomment-79154",
    "user": "timdumol"
}
```

Nice debugging. Works as advertised.



---

archive/issue_comments_079155.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-04T04:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8686#issuecomment-79155",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079156.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-11T06:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8686#issuecomment-79156",
    "user": "timdumol"
}
```

Resolution: fixed
