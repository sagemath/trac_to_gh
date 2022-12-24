# Issue 8102: Simplify Sphinxify

archive/issues_008102.json:
```json
{
    "body": "Assignee: was\n\nCC:  timdumol\n\nSimplifying `sagenb.misc.sphinxify` and importing `sphinx.application.Sphinx` on demand should make docstrings render faster and reduce Sage startup time.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8102\n\n",
    "created_at": "2010-01-28T02:23:43Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Simplify Sphinxify",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8102",
    "user": "mpatel"
}
```
Assignee: was

CC:  timdumol

Simplifying `sagenb.misc.sphinxify` and importing `sphinx.application.Sphinx` on demand should make docstrings render faster and reduce Sage startup time.

Issue created by migration from https://trac.sagemath.org/ticket/8102





---

archive/issue_comments_071086.json:
```json
{
    "body": "Attachment [trac_8102-simplify_sphinxify.patch](tarball://root/attachments/some-uuid/ticket8102/trac_8102-simplify_sphinxify.patch) by mpatel created at 2010-01-28 02:33:56\n\nSimplify `sphinxify.py`.  Some pep8 tweaks.  sagenb repo.",
    "created_at": "2010-01-28T02:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8102#issuecomment-71086",
    "user": "mpatel"
}
```

Attachment [trac_8102-simplify_sphinxify.patch](tarball://root/attachments/some-uuid/ticket8102/trac_8102-simplify_sphinxify.patch) by mpatel created at 2010-01-28 02:33:56

Simplify `sphinxify.py`.  Some pep8 tweaks.  sagenb repo.



---

archive/issue_comments_071087.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-28T02:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8102#issuecomment-71087",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071088.json:
```json
{
    "body": "The patch also includes some [pep8](http://pypi.python.org/pypi/pep8/) tweaks.",
    "created_at": "2010-01-28T02:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8102#issuecomment-71088",
    "user": "mpatel"
}
```

The patch also includes some [pep8](http://pypi.python.org/pypi/pep8/) tweaks.



---

archive/issue_comments_071089.json:
```json
{
    "body": "Specifically,\n\n```sh\n/usr/bin/pep8 --repeat --show-source --ignore=E251,E301,E302,E501 sphinxify.py\n```\n\n\nAnd to test the startup imports / time:  `sage -startuptime`",
    "created_at": "2010-02-03T05:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8102#issuecomment-71089",
    "user": "mpatel"
}
```

Specifically,

```sh
/usr/bin/pep8 --repeat --show-source --ignore=E251,E301,E302,E501 sphinxify.py
```


And to test the startup imports / time:  `sage -startuptime`



---

archive/issue_comments_071090.json:
```json
{
    "body": "In line 89\n\n```\nconfdir = os.path.join(SAGE_DOC, 'en', 'introspect') \n```\n\nwon't there be problems if SAGE_DOC is None?  I guess earlier in the file, you could change the last line in the following:\n\n```\ntry:\n    from sage.misc.misc import SAGE_DOC\nexcept ImportError:\n    SAGE_DOC = \"\"  # used to be None\n```\n\nOtherwise it looks good.",
    "created_at": "2010-02-03T05:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8102#issuecomment-71090",
    "user": "jhpalmieri"
}
```

In line 89

```
confdir = os.path.join(SAGE_DOC, 'en', 'introspect') 
```

won't there be problems if SAGE_DOC is None?  I guess earlier in the file, you could change the last line in the following:

```
try:
    from sage.misc.misc import SAGE_DOC
except ImportError:
    SAGE_DOC = ""  # used to be None
```

Otherwise it looks good.



---

archive/issue_comments_071091.json:
```json
{
    "body": "Attachment [trac_8102-simplify_sphinxify.2.patch](tarball://root/attachments/some-uuid/ticket8102/trac_8102-simplify_sphinxify.2.patch) by mpatel created at 2010-02-03 05:56:04\n\nReplace `SAGE_DOC = None` with `SAGE_DOC = ''`.  Replaces previous.",
    "created_at": "2010-02-03T05:56:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8102#issuecomment-71091",
    "user": "mpatel"
}
```

Attachment [trac_8102-simplify_sphinxify.2.patch](tarball://root/attachments/some-uuid/ticket8102/trac_8102-simplify_sphinxify.2.patch) by mpatel created at 2010-02-03 05:56:04

Replace `SAGE_DOC = None` with `SAGE_DOC = ''`.  Replaces previous.



---

archive/issue_comments_071092.json:
```json
{
    "body": "Thanks for catching that exception.  V2 includes the change.",
    "created_at": "2010-02-03T05:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8102#issuecomment-71092",
    "user": "mpatel"
}
```

Thanks for catching that exception.  V2 includes the change.



---

archive/issue_comments_071093.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-03T16:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8102#issuecomment-71093",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071094.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-05T00:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8102#issuecomment-71094",
    "user": "mpatel"
}
```

Resolution: fixed
