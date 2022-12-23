# Issue 4791: [with patch, needs review] purge nodoctest.py from the Sage library tree

archive/issues_004791.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe should doctest every possible file and not put up with any nodoctest.py crap. This keeps certain files from getting doctested, i.e.\n\n```\nsage -t -long devel/sage/sage/dsage/server/stats.py\n         [2.3 s]\nsage -t -long devel/sage/sage/dsage/server/tests/test_server.py\n         [2.6 s]\nsage -t -long devel/sage/sage/dsage/twisted/tests/test_pubkeyauth.py\n         [2.4 s]\nsage -t -long devel/sage/sage/dsage/twisted/tests/test_remote.py\n         [2.5 s]\nsage -t -long devel/sage/sage/dsage/twisted/pubkeyauth.py\n         [2.6 s]\nsage -t -long devel/sage/sage/dsage/twisted/pb.py\n         [2.7 s]\nsage -t -long devel/sage/sage/server/notebook/sage_email.py\n         [2.5 s]\nsage -t -long devel/sage/sage/quadratic_forms/genera/genus.py\n         [2.7 s]\n```\n\nThe following files are removed by this patch:\n\n```\nsage/dsage/database/tests/nodoctest.py\nsage/dsage/database/nodoctest.py\nsage/dsage/errors/nodoctest.py\nsage/dsage/misc/nodoctest.py\nsage/dsage/scripts/nodoctest.py\nsage/dsage/server/tests/nodoctest.py\nsage/dsage/server/nodoctest.py\nsage/dsage/twisted/tests/nodoctest.py\nsage/dsage/twisted/nodoctest.py\nsage/dsage/nodoctest.py\nsage/quadratic_forms/genera/nodoctest.py\nsage/server/notebook/compress/nodoctest.py\n```\n\nWith my current merge tree -t -long passes.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4791\n\n",
    "created_at": "2008-12-14T07:22:12Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] purge nodoctest.py from the Sage library tree",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4791",
    "user": "mabshoff"
}
```
Assignee: mabshoff

We should doctest every possible file and not put up with any nodoctest.py crap. This keeps certain files from getting doctested, i.e.

```
sage -t -long devel/sage/sage/dsage/server/stats.py
         [2.3 s]
sage -t -long devel/sage/sage/dsage/server/tests/test_server.py
         [2.6 s]
sage -t -long devel/sage/sage/dsage/twisted/tests/test_pubkeyauth.py
         [2.4 s]
sage -t -long devel/sage/sage/dsage/twisted/tests/test_remote.py
         [2.5 s]
sage -t -long devel/sage/sage/dsage/twisted/pubkeyauth.py
         [2.6 s]
sage -t -long devel/sage/sage/dsage/twisted/pb.py
         [2.7 s]
sage -t -long devel/sage/sage/server/notebook/sage_email.py
         [2.5 s]
sage -t -long devel/sage/sage/quadratic_forms/genera/genus.py
         [2.7 s]
```

The following files are removed by this patch:

```
sage/dsage/database/tests/nodoctest.py
sage/dsage/database/nodoctest.py
sage/dsage/errors/nodoctest.py
sage/dsage/misc/nodoctest.py
sage/dsage/scripts/nodoctest.py
sage/dsage/server/tests/nodoctest.py
sage/dsage/server/nodoctest.py
sage/dsage/twisted/tests/nodoctest.py
sage/dsage/twisted/nodoctest.py
sage/dsage/nodoctest.py
sage/quadratic_forms/genera/nodoctest.py
sage/server/notebook/compress/nodoctest.py
```

With my current merge tree -t -long passes.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4791





---

archive/issue_comments_036314.json:
```json
{
    "body": "Attachment\n\nThis is a git style patch",
    "created_at": "2008-12-14T07:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4791#issuecomment-36314",
    "user": "mabshoff"
}
```

Attachment

This is a git style patch



---

archive/issue_comments_036315.json:
```json
{
    "body": "Yep, I agree that we should remove all these `nodoctest.py` files. Anything that pops up should get turned up by the next alpha/rc ...",
    "created_at": "2008-12-14T08:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4791#issuecomment-36315",
    "user": "craigcitro"
}
```

Yep, I agree that we should remove all these `nodoctest.py` files. Anything that pops up should get turned up by the next alpha/rc ...



---

archive/issue_comments_036316.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc0",
    "created_at": "2008-12-14T08:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4791#issuecomment-36316",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.rc0



---

archive/issue_comments_036317.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-14T08:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4791#issuecomment-36317",
    "user": "mabshoff"
}
```

Resolution: fixed
