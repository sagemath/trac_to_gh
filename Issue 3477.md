# Issue 3477: clisp spkg-install has bad hard-coded error message

archive/issues_003477.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe following code from the clisp spkg-install is confusing:\n\n```\n    echo \"If you already have clisp, you can type touch spkg/installed/clisp-2.38\"\n    echo \"(or whatever the current version is) from SAGE_ROOT, and continue the\"\n    echo \"install.  This tells SAGE that you already have clisp-2.38 installed.\"\n```\n\nIt should either use the current version, or not give a version at all.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3477\n\n",
    "created_at": "2008-06-19T22:16:39Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "clisp spkg-install has bad hard-coded error message",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3477",
    "user": "cwitty"
}
```
Assignee: mabshoff

The following code from the clisp spkg-install is confusing:

```
    echo "If you already have clisp, you can type touch spkg/installed/clisp-2.38"
    echo "(or whatever the current version is) from SAGE_ROOT, and continue the"
    echo "install.  This tells SAGE that you already have clisp-2.38 installed."
```

It should either use the current version, or not give a version at all.

Issue created by migration from https://trac.sagemath.org/ticket/3477





---

archive/issue_comments_024509.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2008-06-27T04:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3477#issuecomment-24509",
    "user": "mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_024510.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T21:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3477#issuecomment-24510",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_024511.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc0",
    "created_at": "2008-07-07T22:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3477#issuecomment-24511",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.rc0
