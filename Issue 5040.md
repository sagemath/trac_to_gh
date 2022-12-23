# Issue 5040: Bug in NTL's ./configure

archive/issues_005040.json:
```json
{
    "body": "Assignee: mabshoff\n\nIf you build sage and the directory path contains a \"-h\" anywhere in it, then NTL's perl DoConfig script displays a help message and exists.  This totally breaks building sage.  The code at fault is:\n\n```\n\n   if ($arg =~ '-h|help|-help|--help') {\n      system(\"more ../doc/config.txt\");\n      exit;\n   }\n```\n\n\nIn particular, PREFIX will get passed in and if your directory were, e.g,. build-sage-help-me-foobar then Sage won't work.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5040\n\n",
    "created_at": "2009-01-20T22:37:46Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "Bug in NTL's ./configure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5040",
    "user": "was"
}
```
Assignee: mabshoff

If you build sage and the directory path contains a "-h" anywhere in it, then NTL's perl DoConfig script displays a help message and exists.  This totally breaks building sage.  The code at fault is:

```

   if ($arg =~ '-h|help|-help|--help') {
      system("more ../doc/config.txt");
      exit;
   }
```


In particular, PREFIX will get passed in and if your directory were, e.g,. build-sage-help-me-foobar then Sage won't work.



Issue created by migration from https://trac.sagemath.org/ticket/5040





---

archive/issue_comments_038389.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha3/ntl-5.4.2.p5.spkg\n\nfixes the problem by removing the help option for now. Note that this spkg also fixes #4978.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T03:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5040#issuecomment-38389",
    "user": "mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha3/ntl-5.4.2.p5.spkg

fixes the problem by removing the help option for now. Note that this spkg also fixes #4978.

Cheers,

Michael



---

archive/issue_comments_038390.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-29T03:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5040#issuecomment-38390",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038391.json:
```json
{
    "body": "Code looks good.  The new spkg does build, and relevant doctests still pass after rebuilding NTL-related .pyx files.\n\nPositive review.",
    "created_at": "2009-01-29T04:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5040#issuecomment-38391",
    "user": "cwitty"
}
```

Code looks good.  The new spkg does build, and relevant doctests still pass after rebuilding NTL-related .pyx files.

Positive review.



---

archive/issue_comments_038392.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T04:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5040#issuecomment-38392",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_038393.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-29T04:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5040#issuecomment-38393",
    "user": "mabshoff"
}
```

Resolution: fixed
