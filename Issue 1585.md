# Issue 1585: fix file permissions in guava

archive/issues_001585.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nrm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/guavapage/guava_light.jpg'? y\nrm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/guavapage/guava.jpg'? y\nrm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/guavapage/guava.ps'? y\nrm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/src/leon/doc/leon_guava_manual.pdf'? y\nrm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/src/leon/doc/README'? y\nrm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/src/leon/doc/manual.tex'? y\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1585\n\n",
    "created_at": "2007-12-22T01:26:31Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "fix file permissions in guava",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1585",
    "user": "@rlmill"
}
```
Assignee: @williamstein


```
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/guavapage/guava_light.jpg'? y
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/guavapage/guava.jpg'? y
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/guavapage/guava.ps'? y
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/src/leon/doc/leon_guava_manual.pdf'? y
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/src/leon/doc/README'? y
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/gap-4.4.10/pkg/guava3.1/src/leon/doc/manual.tex'? y
```


Issue created by migration from https://trac.sagemath.org/ticket/1585





---

archive/issue_comments_010089.json:
```json
{
    "body": "also\n\n```\nrm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/libreadline.so.5.2'? y\nrm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/libhistory.so.5.2'? y\n```\n",
    "created_at": "2007-12-22T01:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1585#issuecomment-10089",
    "user": "@rlmill"
}
```

also

```
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/libreadline.so.5.2'? y
rm: remove write-protected regular file `sage-2.9.1.alpha3/local/lib/libhistory.so.5.2'? y
```




---

archive/issue_comments_010090.json:
```json
{
    "body": "I've fixed the files in guava",
    "created_at": "2007-12-22T20:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1585#issuecomment-10090",
    "user": "@rlmill"
}
```

I've fixed the files in guava



---

archive/issue_comments_010091.json:
```json
{
    "body": "After #1752 the permission issues with `libreadline` and `libhistory` are also gone:\n\n```\nsage-2.10.alpha3$ ls -al local/lib/libreadline.* local/lib/libhistory.*\n-rwxr-xr-x 1 mabshoff 1090  157594 2008-01-11 12:20 local/lib/libhistory.a\nlrwxrwxrwx 1 mabshoff 1090      15 2008-01-11 12:21 local/lib/libhistory.so -> libhistory.so.5\nlrwxrwxrwx 1 mabshoff 1090      17 2008-01-11 12:21 local/lib/libhistory.so.5 -> libhistory.so.5.2\n-rwxr-xr-x 1 mabshoff 1090   97893 2008-01-11 12:21 local/lib/libhistory.so.5.2\n-rwxr-xr-x 1 mabshoff 1090 1084724 2008-01-11 12:20 local/lib/libreadline.a\nlrwxrwxrwx 1 mabshoff 1090      16 2008-01-11 12:21 local/lib/libreadline.so -> libreadline.so.5\nlrwxrwxrwx 1 mabshoff 1090      18 2008-01-11 12:21 local/lib/libreadline.so.5 -> libreadline.so.5.2\n-rwxr-xr-x 1 mabshoff 1090  626992 2008-01-11 12:21 local/lib/libreadline.so.5.2\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-01-13T19:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1585#issuecomment-10091",
    "user": "mabshoff"
}
```

After #1752 the permission issues with `libreadline` and `libhistory` are also gone:

```
sage-2.10.alpha3$ ls -al local/lib/libreadline.* local/lib/libhistory.*
-rwxr-xr-x 1 mabshoff 1090  157594 2008-01-11 12:20 local/lib/libhistory.a
lrwxrwxrwx 1 mabshoff 1090      15 2008-01-11 12:21 local/lib/libhistory.so -> libhistory.so.5
lrwxrwxrwx 1 mabshoff 1090      17 2008-01-11 12:21 local/lib/libhistory.so.5 -> libhistory.so.5.2
-rwxr-xr-x 1 mabshoff 1090   97893 2008-01-11 12:21 local/lib/libhistory.so.5.2
-rwxr-xr-x 1 mabshoff 1090 1084724 2008-01-11 12:20 local/lib/libreadline.a
lrwxrwxrwx 1 mabshoff 1090      16 2008-01-11 12:21 local/lib/libreadline.so -> libreadline.so.5
lrwxrwxrwx 1 mabshoff 1090      18 2008-01-11 12:21 local/lib/libreadline.so.5 -> libreadline.so.5.2
-rwxr-xr-x 1 mabshoff 1090  626992 2008-01-11 12:21 local/lib/libreadline.so.5.2
```


Cheers,

Michael



---

archive/issue_comments_010092.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-13T19:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1585#issuecomment-10092",
    "user": "mabshoff"
}
```

Resolution: fixed
