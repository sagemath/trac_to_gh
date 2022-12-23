# Issue 3027: [with patches; needs review] Debian lintian fixes

archive/issues_003027.json:
```json
{
    "body": "Assignee: tabbott\n\nI ran lintian (the Debian packaging error checking tool) on all my packages, and found a bunch of bugs.  I guess the Debian build system is too automated for me to notice these normally.  I've attached a bunch of patches to fix many of these bugs (some others I reported upstream).\n\nIssue created by migration from https://trac.sagemath.org/ticket/3027\n\n",
    "created_at": "2008-04-26T01:30:09Z",
    "labels": [
        "debian-package",
        "blocker",
        "bug"
    ],
    "title": "[with patches; needs review] Debian lintian fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3027",
    "user": "tabbott"
}
```
Assignee: tabbott

I ran lintian (the Debian packaging error checking tool) on all my packages, and found a bunch of bugs.  I guess the Debian build system is too automated for me to notice these normally.  I've attached a bunch of patches to fix many of these bugs (some others I reported upstream).

Issue created by migration from https://trac.sagemath.org/ticket/3027





---

archive/issue_comments_020811.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T01:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3027#issuecomment-20811",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020812.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T01:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3027#issuecomment-20812",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020813.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T01:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3027#issuecomment-20813",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020814.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T01:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3027#issuecomment-20814",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020815.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T01:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3027#issuecomment-20815",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020816.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T01:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3027#issuecomment-20816",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020817.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T01:31:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3027#issuecomment-20817",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020818.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T01:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3027#issuecomment-20818",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020819.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-26T01:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3027#issuecomment-20819",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_020820.json:
```json
{
    "body": "Patches look good to me. I have slipped them all into their respective spkg without bumping the patch level to avoid forces rebuilds on upgrade. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T02:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3027#issuecomment-20820",
    "user": "mabshoff"
}
```

Patches look good to me. I have slipped them all into their respective spkg without bumping the patch level to avoid forces rebuilds on upgrade. Positive review.

Cheers,

Michael



---

archive/issue_comments_020821.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-26T02:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3027#issuecomment-20821",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020822.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha0",
    "created_at": "2008-04-26T02:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3027#issuecomment-20822",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha0
