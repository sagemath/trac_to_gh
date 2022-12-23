# Issue 1742: [with spkg] Build ntl with debug info

archive/issues_001742.json:
```json
{
    "body": "Assignee: mabshoff\n\nNTL is currently build without debug symbols. This makes debugging or valgrinding harder and forces me to rebuild NTL manually. The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha1/ntl-5.4.1.p10.spkg\n\nadds debug flags to the appropriate CFLAGS and CXXFLAGS.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1742\n\n",
    "created_at": "2008-01-10T06:22:40Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "[with spkg] Build ntl with debug info",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1742",
    "user": "mabshoff"
}
```
Assignee: mabshoff

NTL is currently build without debug symbols. This makes debugging or valgrinding harder and forces me to rebuild NTL manually. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha1/ntl-5.4.1.p10.spkg

adds debug flags to the appropriate CFLAGS and CXXFLAGS.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1742





---

archive/issue_comments_011009.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-10T06:28:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1742#issuecomment-11009",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011010.json:
```json
{
    "body": "Merged in Sage 2.10.alpha1.",
    "created_at": "2008-01-10T06:28:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1742#issuecomment-11010",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.alpha1.
