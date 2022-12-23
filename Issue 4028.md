# Issue 4028: doctest and improve sage/interfaces/axiom.py

archive/issues_004028.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4028\n\n",
    "created_at": "2008-09-01T02:40:26Z",
    "labels": [
        "interfaces",
        "minor",
        "enhancement"
    ],
    "title": "doctest and improve sage/interfaces/axiom.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4028",
    "user": "mhansen"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/4028





---

archive/issue_comments_029046.json:
```json
{
    "body": "Attachment\n\nOne spelling error: \"requires Axoim\" (which Mike corrected) - other than that is passes doctests with and without Axiom installed. Mike went with me over the patch and answered questions. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T03:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4028#issuecomment-29046",
    "user": "mabshoff"
}
```

Attachment

One spelling error: "requires Axoim" (which Mike corrected) - other than that is passes doctests with and without Axiom installed. Mike went with me over the patch and answered questions. Positive review.

Cheers,

Michael



---

archive/issue_comments_029047.json:
```json
{
    "body": "Oops, with the original axiom running the doctest with -optional results in a fork bomb :(\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T03:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4028#issuecomment-29047",
    "user": "mabshoff"
}
```

Oops, with the original axiom running the doctest with -optional results in a fork bomb :(

Cheers,

Michael



---

archive/issue_comments_029048.json:
```json
{
    "body": "Looks like somehow the following ends up getting called:\n\n```\nsage -axiom -nox -noclef\n```\n\nIf I run that from the command line it also starts a fork bomb.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T03:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4028#issuecomment-29048",
    "user": "mabshoff"
}
```

Looks like somehow the following ends up getting called:

```
sage -axiom -nox -noclef
```

If I run that from the command line it also starts a fork bomb.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_029049.json:
```json
{
    "body": "It is all William's fault:\n\n```\nmabshoff@sage:/usr/local/bin$ pwd\n/usr/local/bin\nmabshoff@sage:/usr/local/bin$ cat axiom \n#!/bin/sh\nsage -axiom $*\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T03:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4028#issuecomment-29049",
    "user": "mabshoff"
}
```

It is all William's fault:

```
mabshoff@sage:/usr/local/bin$ pwd
/usr/local/bin
mabshoff@sage:/usr/local/bin$ cat axiom 
#!/bin/sh
sage -axiom $*
```


Cheers,

Michael



---

archive/issue_comments_029050.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha4",
    "created_at": "2008-09-01T04:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4028#issuecomment-29050",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha4



---

archive/issue_comments_029051.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-01T04:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4028#issuecomment-29051",
    "user": "mabshoff"
}
```

Resolution: fixed
