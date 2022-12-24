# Issue 7687: Remove leonconv binary from gap spkg (guava pkg).

archive/issues_007687.json:
```json
{
    "body": "Assignee: tbd\n\nWe ship a Linux *binary* `leonconv` with every copy of Sage.  This is bad and a potential security issue.  Delete this.  \n\n\n```\nwstein@sage:~/build/sage-4.3.rc0/spkg/standard/gap-4.4.10.p12/src/pkg/guava3.4/src$ ls -lh\ntotal 36K\ndrwxr-xr-x 2 wstein wstein 4.0K 2008-03-31 03:55 ctjhai\n-rw-r--r-- 1 wstein wstein  147 2008-03-17 14:40 defs.h\ndrwxr-xr-x 4 wstein wstein 4.0K 2008-03-31 03:55 leon\n-rwxr-xr-x 1 wstein wstein  15K 2008-03-17 14:40 leonconv\n-rw-r--r-- 1 wstein wstein 4.0K 2008-03-17 14:40 leonconv.c\n-rwxr-xr-x 1 wstein wstein  262 2008-03-17 14:44 Makefile\nwstein@sage:~/build/sage-4.3.rc0/spkg/standard/gap-4.4.10.p12/src/pkg/guava3.4/src$ ./leonconv\nError, usage: leonconv <switch> <inputfile> <outputfile>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7687\n\n",
    "created_at": "2009-12-15T19:24:16Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Remove leonconv binary from gap spkg (guava pkg).",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7687",
    "user": "was"
}
```
Assignee: tbd

We ship a Linux *binary* `leonconv` with every copy of Sage.  This is bad and a potential security issue.  Delete this.  


```
wstein@sage:~/build/sage-4.3.rc0/spkg/standard/gap-4.4.10.p12/src/pkg/guava3.4/src$ ls -lh
total 36K
drwxr-xr-x 2 wstein wstein 4.0K 2008-03-31 03:55 ctjhai
-rw-r--r-- 1 wstein wstein  147 2008-03-17 14:40 defs.h
drwxr-xr-x 4 wstein wstein 4.0K 2008-03-31 03:55 leon
-rwxr-xr-x 1 wstein wstein  15K 2008-03-17 14:40 leonconv
-rw-r--r-- 1 wstein wstein 4.0K 2008-03-17 14:40 leonconv.c
-rwxr-xr-x 1 wstein wstein  262 2008-03-17 14:44 Makefile
wstein@sage:~/build/sage-4.3.rc0/spkg/standard/gap-4.4.10.p12/src/pkg/guava3.4/src$ ./leonconv
Error, usage: leonconv <switch> <inputfile> <outputfile>
```


Issue created by migration from https://trac.sagemath.org/ticket/7687





---

archive/issue_comments_065964.json:
```json
{
    "body": "Since guava was supposed to be removed a long time ago (http://trac.sagemath.org/sage_trac/ticket/5701), I don't see why this trac ticket is necessary.",
    "created_at": "2009-12-15T20:24:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7687#issuecomment-65964",
    "user": "wdj"
}
```

Since guava was supposed to be removed a long time ago (http://trac.sagemath.org/sage_trac/ticket/5701), I don't see why this trac ticket is necessary.



---

archive/issue_comments_065965.json:
```json
{
    "body": "`leonconv` is not shipped anymore.",
    "created_at": "2014-06-22T14:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7687#issuecomment-65965",
    "user": "aapitzsch"
}
```

`leonconv` is not shipped anymore.



---

archive/issue_comments_065966.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-06-22T14:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7687#issuecomment-65966",
    "user": "aapitzsch"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065967.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-10-25T21:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7687#issuecomment-65967",
    "user": "vbraun"
}
```

Resolution: fixed
