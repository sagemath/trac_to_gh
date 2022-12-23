# Issue 7787: Use a javascript minifier instead of a packer for sagenb

archive/issues_007787.json:
```json
{
    "body": "Assignee: was\n\nCC:  chapoton\n\nA minifier is safer (less likely to cause errors), is faster (no need for client-side to unpack), and smaller (with gzip).\n\nGoogle has reimplemented Douglas Crockford's `jsmin.py` with a BSD License for its V8 engine. It is available here:\n\nhttp://code.google.com/p/v8/source/browse/branches/bleeding_edge/tools/jsmin.py\n\nIssue created by migration from https://trac.sagemath.org/ticket/7787\n\n",
    "created_at": "2009-12-29T10:20:28Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "title": "Use a javascript minifier instead of a packer for sagenb",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7787",
    "user": "timdumol"
}
```
Assignee: was

CC:  chapoton

A minifier is safer (less likely to cause errors), is faster (no need for client-side to unpack), and smaller (with gzip).

Google has reimplemented Douglas Crockford's `jsmin.py` with a BSD License for its V8 engine. It is available here:

http://code.google.com/p/v8/source/browse/branches/bleeding_edge/tools/jsmin.py

Issue created by migration from https://trac.sagemath.org/ticket/7787





---

archive/issue_comments_067204.json:
```json
{
    "body": "Attachment\n\nAdds Google's jsmin.py",
    "created_at": "2009-12-29T10:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67204",
    "user": "timdumol"
}
```

Attachment

Adds Google's jsmin.py



---

archive/issue_comments_067205.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-29T10:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67205",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067206.json:
```json
{
    "body": "Attachment\n\nReplaces JavaScriptCompressor with JavaScriptMinifier",
    "created_at": "2009-12-29T10:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67206",
    "user": "timdumol"
}
```

Attachment

Replaces JavaScriptCompressor with JavaScriptMinifier



---

archive/issue_comments_067207.json:
```json
{
    "body": "Attachment\n\nAdds Google's jsmin.py. Apply this patch alone.",
    "created_at": "2009-12-29T10:40:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67207",
    "user": "timdumol"
}
```

Attachment

Adds Google's jsmin.py. Apply this patch alone.



---

archive/issue_comments_067208.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-29T15:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67208",
    "user": "timdumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067209.json:
```json
{
    "body": "Google's `jsmin.py` causes failures (\"//\" in a string deletes the rest of the line), and does not remove unneeded lines.",
    "created_at": "2009-12-29T15:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67209",
    "user": "timdumol"
}
```

Google's `jsmin.py` causes failures ("//" in a string deletes the rest of the line), and does not remove unneeded lines.



---

archive/issue_comments_067210.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67210",
    "user": "mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_067211.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67211",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067212.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-19T08:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67212",
    "user": "chapoton"
}
```

Resolution: invalid
