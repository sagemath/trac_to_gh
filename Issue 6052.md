# Issue 6052: partial_fraction_decomposition is broken for irreducible denominators

archive/issues_006052.json:
```json
{
    "body": "Assignee: @tornaria\n\n\n```\n19:34 < rickhg12hs> having some issues with partial fraction decomposition\n19:37 < rickhg12hs> sage: R.<x> = GF(2)[];((x+1)/(x^3+x+1)).partial_fraction_decomposition()\n19:37 < rickhg12hs> ... generates type errors\n19:39 < rickhg12hs> sage: P.<y>=ZZ[];((y+1)/(y^2+y+1)).partial_fraction_decomposition()\n19:39 < rickhg12hs> ... generates type errors also\n19:41 < rickhg12hs> sage: ((y+1)/(y^2+y+1) + (y+1)/(y^2+1)).partial_fraction_decomposition()\n19:41 < rickhg12hs> ... the line above works\n19:43 < rickhg12hs> sage: ((x+1)/(x^3+x+1) + (x+1)/(x^3+x^2+1)).partial_fraction_decomposition()\n19:43 < rickhg12hs> ... the line above works\n19:46 < rickhg12hs> FYI:\n19:46 < rickhg12hs> sage: version()\n19:46 < rickhg12hs> 'Sage Version 3.4.2, Release Date: 2009-05-05'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6052\n\n",
    "created_at": "2009-05-17T02:43:00Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "partial_fraction_decomposition is broken for irreducible denominators",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6052",
    "user": "@tornaria"
}
```
Assignee: @tornaria


```
19:34 < rickhg12hs> having some issues with partial fraction decomposition
19:37 < rickhg12hs> sage: R.<x> = GF(2)[];((x+1)/(x^3+x+1)).partial_fraction_decomposition()
19:37 < rickhg12hs> ... generates type errors
19:39 < rickhg12hs> sage: P.<y>=ZZ[];((y+1)/(y^2+y+1)).partial_fraction_decomposition()
19:39 < rickhg12hs> ... generates type errors also
19:41 < rickhg12hs> sage: ((y+1)/(y^2+y+1) + (y+1)/(y^2+1)).partial_fraction_decomposition()
19:41 < rickhg12hs> ... the line above works
19:43 < rickhg12hs> sage: ((x+1)/(x^3+x+1) + (x+1)/(x^3+x^2+1)).partial_fraction_decomposition()
19:43 < rickhg12hs> ... the line above works
19:46 < rickhg12hs> FYI:
19:46 < rickhg12hs> sage: version()
19:46 < rickhg12hs> 'Sage Version 3.4.2, Release Date: 2009-05-05'
```


Issue created by migration from https://trac.sagemath.org/ticket/6052





---

archive/issue_comments_048213.json:
```json
{
    "body": "Attachment [trac_6052.patch](tarball://root/attachments/some-uuid/ticket6052/trac_6052.patch) by @mwhansen created at 2009-05-19 04:59:21\n\nLooks good to me.  I just updated some minor Sphinx formatting issues in the patch.\n\nOther than that, all tests pass and things look good to me.",
    "created_at": "2009-05-19T04:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6052#issuecomment-48213",
    "user": "@mwhansen"
}
```

Attachment [trac_6052.patch](tarball://root/attachments/some-uuid/ticket6052/trac_6052.patch) by @mwhansen created at 2009-05-19 04:59:21

Looks good to me.  I just updated some minor Sphinx formatting issues in the patch.

Other than that, all tests pass and things look good to me.



---

archive/issue_comments_048214.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T18:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6052#issuecomment-48214",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_048215.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T18:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6052#issuecomment-48215",
    "user": "mabshoff"
}
```

Resolution: fixed
