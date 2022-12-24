# Issue 8758: Add a top-level /data with static.File(DATA) that serves files from the data directory

archive/issues_008758.json:
```json
{
    "body": "Assignee: acleone\n\nCC:  acleone @williamstein @TimDumol\n\nInstead of having /js, /css, etc, we should serve all static data files out of /data.  For now this patch just adds /data using `child_data = static.File(DATA)`, where `static.File(path)` is defined in twisted.  It will serve files with the correct MIME type based on extension.\n\nEventually we should find all the /js and /css paths and change them to /data\n\nAt some point in the future we could even implement caching of all the static files easily by subclassing static.File(path), and making everything in /data cached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8758\n\n",
    "created_at": "2010-04-24T22:58:06Z",
    "labels": [
        "notebook",
        "trivial",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Add a top-level /data with static.File(DATA) that serves files from the data directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8758",
    "user": "acleone"
}
```
Assignee: acleone

CC:  acleone @williamstein @TimDumol

Instead of having /js, /css, etc, we should serve all static data files out of /data.  For now this patch just adds /data using `child_data = static.File(DATA)`, where `static.File(path)` is defined in twisted.  It will serve files with the correct MIME type based on extension.

Eventually we should find all the /js and /css paths and change them to /data

At some point in the future we could even implement caching of all the static files easily by subclassing static.File(path), and making everything in /data cached.

Issue created by migration from https://trac.sagemath.org/ticket/8758





---

archive/issue_comments_080134.json:
```json
{
    "body": "Adds the two static.File(DATA) calls to twist.py",
    "created_at": "2010-04-24T23:01:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8758#issuecomment-80134",
    "user": "acleone"
}
```

Adds the two static.File(DATA) calls to twist.py



---

archive/issue_comments_080135.json:
```json
{
    "body": "Attachment [trac_8758-data-toplevel-with-static-file.patch](tarball://root/attachments/some-uuid/ticket8758/trac_8758-data-toplevel-with-static-file.patch) by acleone created at 2010-04-24 23:02:01",
    "created_at": "2010-04-24T23:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8758#issuecomment-80135",
    "user": "acleone"
}
```

Attachment [trac_8758-data-toplevel-with-static-file.patch](tarball://root/attachments/some-uuid/ticket8758/trac_8758-data-toplevel-with-static-file.patch) by acleone created at 2010-04-24 23:02:01



---

archive/issue_comments_080136.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-24T23:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8758#issuecomment-80136",
    "user": "acleone"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080137.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-25T00:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8758#issuecomment-80137",
    "user": "@williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080138.json:
```json
{
    "body": "Not a patch bomb.",
    "created_at": "2010-04-25T00:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8758#issuecomment-80138",
    "user": "@williamstein"
}
```

Not a patch bomb.



---

archive/issue_comments_080139.json:
```json
{
    "body": "Changes the url to /static/.  Replaces previous.",
    "created_at": "2010-05-29T22:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8758#issuecomment-80139",
    "user": "acleone"
}
```

Changes the url to /static/.  Replaces previous.



---

archive/issue_comments_080140.json:
```json
{
    "body": "Attachment [trac_8758-toplevel-static-url.patch](tarball://root/attachments/some-uuid/ticket8758/trac_8758-toplevel-static-url.patch) by acleone created at 2010-05-29 22:43:37\n\nThe latest patch changes the url to /static/.\n\nI think we should also rename the \"data\" directory in the sagenb source to \"static\", and rename the global DATA to STATIC.\n\nDATA is slightly confusing because uploading files to a worksheet also uses a DATA global, eg DATA+'mydatafile.txt'.",
    "created_at": "2010-05-29T22:43:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8758#issuecomment-80140",
    "user": "acleone"
}
```

Attachment [trac_8758-toplevel-static-url.patch](tarball://root/attachments/some-uuid/ticket8758/trac_8758-toplevel-static-url.patch) by acleone created at 2010-05-29 22:43:37

The latest patch changes the url to /static/.

I think we should also rename the "data" directory in the sagenb source to "static", and rename the global DATA to STATIC.

DATA is slightly confusing because uploading files to a worksheet also uses a DATA global, eg DATA+'mydatafile.txt'.



---

archive/issue_comments_080141.json:
```json
{
    "body": "Ok - ignore the new patch.  Let's leave the url as /data.",
    "created_at": "2010-06-02T23:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8758#issuecomment-80141",
    "user": "acleone"
}
```

Ok - ignore the new patch.  Let's leave the url as /data.



---

archive/issue_comments_080142.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-11T05:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8758#issuecomment-80142",
    "user": "@TimDumol"
}
```

Resolution: fixed
