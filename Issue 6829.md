# Issue 6829: Implement Manin symbols over number fields

archive/issues_006829.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  mtaranes\n\nKeywords: modular manin symbols\n\nManin symbols over number fields (related to modular symbols) are used for computing modular forms over those fields.  An implementation valid for general number fields is in prepration by Maite Aranes.\n\nThis will be part of a larger project to implement modular forms over number fields in Sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6829\n\n",
    "created_at": "2009-08-26T21:47:59Z",
    "labels": [
        "component: modular forms"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Implement Manin symbols over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6829",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @craigcitro

CC:  mtaranes

Keywords: modular manin symbols

Manin symbols over number fields (related to modular symbols) are used for computing modular forms over those fields.  An implementation valid for general number fields is in prepration by Maite Aranes.

This will be part of a larger project to implement modular forms over number fields in Sage.

Issue created by migration from https://trac.sagemath.org/ticket/6829





---

archive/issue_comments_056222.json:
```json
{
    "body": "Attachment [p1list_nf.patch](tarball://root/attachments/some-uuid/ticket6829/p1list_nf.patch) by mtaranes created at 2009-08-27 10:15:17",
    "created_at": "2009-08-27T10:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6829#issuecomment-56222",
    "user": "https://trac.sagemath.org/admin/accounts/users/mtaranes"
}
```

Attachment [p1list_nf.patch](tarball://root/attachments/some-uuid/ticket6829/p1list_nf.patch) by mtaranes created at 2009-08-27 10:15:17



---

archive/issue_comments_056223.json:
```json
{
    "body": "The patch is based on 4.1.1",
    "created_at": "2009-08-27T12:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6829#issuecomment-56223",
    "user": "https://trac.sagemath.org/admin/accounts/users/mtaranes"
}
```

The patch is based on 4.1.1



---

archive/issue_comments_056224.json:
```json
{
    "body": "Just my two cents.\n\nMathematically: Both the normalization (lines 415 - 455) and the list creation (lines 993 - 1018) look good to me, forming the heart of the module. Index-looking up is done by list searching, well. The other internal functions lift_to_sl2_Ok, make_coprime, psi also look good.\n\nNon-mathematically: This is how more Sage library code should look like. If this applies cleanly to the newest Sage alpha, doctests all pass and have 100% coverage, and the ReST documentation compiles OK (I didn't check, but I'd be surprised if there was any issue), then I'd vote to let this in.",
    "created_at": "2009-09-21T22:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6829#issuecomment-56224",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Just my two cents.

Mathematically: Both the normalization (lines 415 - 455) and the list creation (lines 993 - 1018) look good to me, forming the heart of the module. Index-looking up is done by list searching, well. The other internal functions lift_to_sl2_Ok, make_coprime, psi also look good.

Non-mathematically: This is how more Sage library code should look like. If this applies cleanly to the newest Sage alpha, doctests all pass and have 100% coverage, and the ReST documentation compiles OK (I didn't check, but I'd be surprised if there was any issue), then I'd vote to let this in.



---

archive/issue_comments_056225.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-23T01:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6829#issuecomment-56225",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056226.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T09:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6829#issuecomment-56226",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
