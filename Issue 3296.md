# Issue 3296: polymake spkg needs "CDDLIB_VERSION='094b.p2" in spkg-install

archive/issues_003296.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: polymake, cddlib\n\nThe short summary describes both the problem and solution.  I could post a new spkg but its almost easier to change that one line.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3296\n\n",
    "created_at": "2008-05-25T02:34:07Z",
    "labels": [
        "packages: optional",
        "minor",
        "bug"
    ],
    "title": "polymake spkg needs \"CDDLIB_VERSION='094b.p2\" in spkg-install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3296",
    "user": "mhampton"
}
```
Assignee: mabshoff

Keywords: polymake, cddlib

The short summary describes both the problem and solution.  I could post a new spkg but its almost easier to change that one line.

Issue created by migration from https://trac.sagemath.org/ticket/3296





---

archive/issue_comments_022798.json:
```json
{
    "body": "Instead of patching polymake each time cddlib changes you should use the following construct:\n\n```\nspkg/standard$ ./newest_version cddlib\ncddlib-094b.p2\n```\n\nThat way it keeps working ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-05-25T02:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3296#issuecomment-22798",
    "user": "mabshoff"
}
```

Instead of patching polymake each time cddlib changes you should use the following construct:

```
spkg/standard$ ./newest_version cddlib
cddlib-094b.p2
```

That way it keeps working ;)

Cheers,

Michael



---

archive/issue_comments_022799.json:
```json
{
    "body": "The same applies to the gmp, too. Either way, the polymake spkg-install is a mess. In fact the polymake.spkg violates a copious amount of other rules. So while I am at it I might as well update the the polymake 2.3 release.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-05-25T02:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3296#issuecomment-22799",
    "user": "mabshoff"
}
```

The same applies to the gmp, too. Either way, the polymake spkg-install is a mess. In fact the polymake.spkg violates a copious amount of other rules. So while I am at it I might as well update the the polymake 2.3 release.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_022800.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-25T02:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3296#issuecomment-22800",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022801.json:
```json
{
    "body": "#3640 will shortly have a working polymake.spkg, so I am closing this as a duplicate.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-31T01:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3296#issuecomment-22801",
    "user": "mabshoff"
}
```

#3640 will shortly have a working polymake.spkg, so I am closing this as a duplicate.

Cheers,

Michael



---

archive/issue_comments_022802.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-07-31T01:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3296",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3296#issuecomment-22802",
    "user": "mabshoff"
}
```

Resolution: duplicate
