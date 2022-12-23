# Issue 947: Cython reload produces ln errors

archive/issues_000947.json:
```json
{
    "body": "Assignee: was\n\nIf you have a ./foo.spyx Cython file, and you \"load foo.spyx\" in SAGE, then touch foo.spyx and again \"load foo.spyx\", it gives messages of the sort:\n\nln: create symbolic link './d' to '/home/sage/d': File exists\n\nfor every directory d in ./\n\nEverything appears to compile correctly, but if you're working in a directory with 100 folders, this can be very annoying!\n\nIssue created by migration from https://trac.sagemath.org/ticket/947\n\n",
    "created_at": "2007-10-20T18:04:06Z",
    "labels": [
        "user interface",
        "minor",
        "bug"
    ],
    "title": "Cython reload produces ln errors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/947",
    "user": "jvoight"
}
```
Assignee: was

If you have a ./foo.spyx Cython file, and you "load foo.spyx" in SAGE, then touch foo.spyx and again "load foo.spyx", it gives messages of the sort:

ln: create symbolic link './d' to '/home/sage/d': File exists

for every directory d in ./

Everything appears to compile correctly, but if you're working in a directory with 100 folders, this can be very annoying!

Issue created by migration from https://trac.sagemath.org/ticket/947





---

archive/issue_comments_005785.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-10-20T22:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/947#issuecomment-5785",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_005786.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T22:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/947#issuecomment-5786",
    "user": "was"
}
```

Resolution: fixed
