# Issue 8134: Escape $s in notebook keybindings docstring, config.py

archive/issues_008134.json:
```json
{
    "body": "Assignee: mvngu\n\nSphinx complains\n\n```\n[...]/sagenb/notebook/config.py:docstring of sagenb.notebook.config:26: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.\n```\n\nwhen building the reference manual.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8134\n\n",
    "created_at": "2010-01-31T02:28:33Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Escape $s in notebook keybindings docstring, config.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8134",
    "user": "mpatel"
}
```
Assignee: mvngu

Sphinx complains

```
[...]/sagenb/notebook/config.py:docstring of sagenb.notebook.config:26: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.
```

when building the reference manual.


Issue created by migration from https://trac.sagemath.org/ticket/8134





---

archive/issue_comments_071531.json:
```json
{
    "body": "Escape `$`s in `config.py`.  *sagenb* repo.",
    "created_at": "2010-01-31T02:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8134#issuecomment-71531",
    "user": "mpatel"
}
```

Escape `$`s in `config.py`.  *sagenb* repo.



---

archive/issue_comments_071532.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-31T02:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8134#issuecomment-71532",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071533.json:
```json
{
    "body": "Attachment [trac_8134-escape_dollars.patch](tarball://root/attachments/some-uuid/ticket8134/trac_8134-escape_dollars.patch) by mpatel created at 2010-01-31 02:36:47\n\nI'm not sure why `sagenb.notebook.config?` doesn't render nicely in the notebook.",
    "created_at": "2010-01-31T02:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8134#issuecomment-71533",
    "user": "mpatel"
}
```

Attachment [trac_8134-escape_dollars.patch](tarball://root/attachments/some-uuid/ticket8134/trac_8134-escape_dollars.patch) by mpatel created at 2010-01-31 02:36:47

I'm not sure why `sagenb.notebook.config?` doesn't render nicely in the notebook.



---

archive/issue_comments_071534.json:
```json
{
    "body": "The patch should apply cleanly to #8051's SageNB 0.7.2.",
    "created_at": "2010-01-31T02:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8134#issuecomment-71534",
    "user": "mpatel"
}
```

The patch should apply cleanly to #8051's SageNB 0.7.2.



---

archive/issue_comments_071535.json:
```json
{
    "body": "Changing component from documentation to notebook.",
    "created_at": "2010-02-05T07:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8134#issuecomment-71535",
    "user": "mpatel"
}
```

Changing component from documentation to notebook.



---

archive/issue_comments_071536.json:
```json
{
    "body": "It fixes the error messages and the output looks good.  Should there be an 'r' before the triple quotes at the top of the file?  I'll give it a positive review either way, so if you want to add that, go ahead.",
    "created_at": "2010-02-05T20:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8134#issuecomment-71536",
    "user": "jhpalmieri"
}
```

It fixes the error messages and the output looks good.  Should there be an 'r' before the triple quotes at the top of the file?  I'll give it a positive review either way, so if you want to add that, go ahead.



---

archive/issue_comments_071537.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-05T20:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8134#issuecomment-71537",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071538.json:
```json
{
    "body": "Make top docstring raw.  Replaces previous.",
    "created_at": "2010-02-06T16:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8134#issuecomment-71538",
    "user": "mpatel"
}
```

Make top docstring raw.  Replaces previous.



---

archive/issue_comments_071539.json:
```json
{
    "body": "Attachment [trac_8134-escape_dollars.2.patch](tarball://root/attachments/some-uuid/ticket8134/trac_8134-escape_dollars.2.patch) by mpatel created at 2010-02-06 16:26:52\n\nReplying to [comment:4 jhpalmieri]:\n> It fixes the error messages and the output looks good.  Should there be an 'r' before the triple quotes at the top of the file?  I'll give it a positive review either way, so if you want to add that, go ahead.\nDone!",
    "created_at": "2010-02-06T16:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8134#issuecomment-71539",
    "user": "mpatel"
}
```

Attachment [trac_8134-escape_dollars.2.patch](tarball://root/attachments/some-uuid/ticket8134/trac_8134-escape_dollars.2.patch) by mpatel created at 2010-02-06 16:26:52

Replying to [comment:4 jhpalmieri]:
> It fixes the error messages and the output looks good.  Should there be an 'r' before the triple quotes at the top of the file?  I'll give it a positive review either way, so if you want to add that, go ahead.
Done!



---

archive/issue_comments_071540.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-10T18:31:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8134#issuecomment-71540",
    "user": "mpatel"
}
```

Resolution: fixed
