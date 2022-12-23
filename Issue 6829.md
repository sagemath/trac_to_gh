# Issue 6829: Implement Manin symbols over number fields

archive/issues_006829.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  mtaranes\n\nKeywords: modular manin symbols\n\nManin symbols over number fields (related to modular symbols) are used for computing modular forms over those fields.  An implementation valid for general number fields is in prepration by Maite Aranes.\n\nThis will be part of a larger project to implement modular forms over number fields in Sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6829\n\n",
    "created_at": "2009-08-26T21:47:59Z",
    "labels": [
        "modular forms",
        "major",
        "enhancement"
    ],
    "title": "Implement Manin symbols over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6829",
    "user": "cremona"
}
```
Assignee: craigcitro

CC:  mtaranes

Keywords: modular manin symbols

Manin symbols over number fields (related to modular symbols) are used for computing modular forms over those fields.  An implementation valid for general number fields is in prepration by Maite Aranes.

This will be part of a larger project to implement modular forms over number fields in Sage.

Issue created by migration from https://trac.sagemath.org/ticket/6829





---

archive/issue_comments_056324.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-08-27T10:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6829#issuecomment-56324",
    "user": "mtaranes"
}
```

Attachment



---

archive/issue_comments_056325.json:
```json
{
    "body": "The patch is based on 4.1.1",
    "created_at": "2009-08-27T12:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6829#issuecomment-56325",
    "user": "mtaranes"
}
```

The patch is based on 4.1.1



---

archive/issue_comments_056326.json:
```json
{
    "body": "Just my two cents.\n\nMathematically: Both the normalization (lines 415 - 455) and the list creation (lines 993 - 1018) look good to me, forming the heart of the module. Index-looking up is done by list searching, well. The other internal functions lift_to_sl2_Ok, make_coprime, psi also look good.\n\nNon-mathematically: This is how more Sage library code should look like. If this applies cleanly to the newest Sage alpha, doctests all pass and have 100% coverage, and the ReST documentation compiles OK (I didn't check, but I'd be surprised if there was any issue), then I'd vote to let this in.",
    "created_at": "2009-09-21T22:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6829#issuecomment-56326",
    "user": "GeorgSWeber"
}
```

Just my two cents.

Mathematically: Both the normalization (lines 415 - 455) and the list creation (lines 993 - 1018) look good to me, forming the heart of the module. Index-looking up is done by list searching, well. The other internal functions lift_to_sl2_Ok, make_coprime, psi also look good.

Non-mathematically: This is how more Sage library code should look like. If this applies cleanly to the newest Sage alpha, doctests all pass and have 100% coverage, and the ReST documentation compiles OK (I didn't check, but I'd be surprised if there was any issue), then I'd vote to let this in.



---

archive/issue_comments_056327.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-23T01:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6829#issuecomment-56327",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056328.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T09:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6829#issuecomment-56328",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
