# Issue 1178: flint in 2.8.12 fails on Solaris 10: u_int16_t undefined

archive/issues_001178.json:
```json
{
    "body": "Assignee: Bill Hart\n\nHello,\n\nthe problem was reported by Klas Heggemann. See\n\nhttp://groups.google.com/group/sage-devel/t/b35f8758cd98fad6\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1178\n\n",
    "created_at": "2007-11-15T15:51:45Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "flint in 2.8.12 fails on Solaris 10: u_int16_t undefined",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1178",
    "user": "mabshoff"
}
```
Assignee: Bill Hart

Hello,

the problem was reported by Klas Heggemann. See

http://groups.google.com/group/sage-devel/t/b35f8758cd98fad6

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1178





---

archive/issue_comments_007277.json:
```json
{
    "body": "FLINT 1.0 works on Solaris 9 when I define\n\n```\ntypedef unsigned int            uint32_t;\ntypedef unsigned long long      u_int64_t;\n```\n\nin `stdint.h`\n\nCheers,\n\nMichael",
    "created_at": "2007-12-06T20:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1178#issuecomment-7277",
    "user": "mabshoff"
}
```

FLINT 1.0 works on Solaris 9 when I define

```
typedef unsigned int            uint32_t;
typedef unsigned long long      u_int64_t;
```

in `stdint.h`

Cheers,

Michael



---

archive/issue_comments_007278.json:
```json
{
    "body": "This has been fixed a while ago. So close it.",
    "created_at": "2008-01-28T05:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1178#issuecomment-7278",
    "user": "mabshoff"
}
```

This has been fixed a while ago. So close it.



---

archive/issue_comments_007279.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-28T05:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1178#issuecomment-7279",
    "user": "mabshoff"
}
```

Resolution: fixed
