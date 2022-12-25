# Issue 276: clisp/maxima dies with "invalid byte" on non-ASCII filename characters

archive/issues_000276.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: clisp maxima\n\nWhen clisp (and hence maxima) starts, it tries to load ~/.clisprc; this involves reading the names of all files in my home directory.  If I have no locale-related environment variables set, and I have a non-ASCII character in some filename in my home directory (in my case, an '\u00f1'), then clisp prints out the following error message:\n\n```\n*** - invalid byte #xF1 in CHARSET:ASCII conversion\nThe following restarts are available:\nABORT          :R1      ABORT\nABORT          :R2      ABORT\nBreak 1 [3]>\n```\n\n(If I abort from here, then clisp/maxima continues to start up, and apparently runs correctly.)\n\nEvidently, the clisp people don't consider this a bug; it is documented here:\nhttp://clisp.cons.org/impnotes/faq.html#faq-enc-err\n\nI suggest that SAGE should either set locale environment variables or use the -E flag to set encodings when it runs maxima (as suggested in the above-linked FAQ entry).  (For now, I have worked around the problem by moving this file out of my home directory.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/276\n\n",
    "created_at": "2007-02-22T20:06:21Z",
    "labels": [
        "component: interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "clisp/maxima dies with \"invalid byte\" on non-ASCII filename characters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/276",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

Keywords: clisp maxima

When clisp (and hence maxima) starts, it tries to load ~/.clisprc; this involves reading the names of all files in my home directory.  If I have no locale-related environment variables set, and I have a non-ASCII character in some filename in my home directory (in my case, an 'ñ'), then clisp prints out the following error message:

```
*** - invalid byte #xF1 in CHARSET:ASCII conversion
The following restarts are available:
ABORT          :R1      ABORT
ABORT          :R2      ABORT
Break 1 [3]>
```

(If I abort from here, then clisp/maxima continues to start up, and apparently runs correctly.)

Evidently, the clisp people don't consider this a bug; it is documented here:
http://clisp.cons.org/impnotes/faq.html#faq-enc-err

I suggest that SAGE should either set locale environment variables or use the -E flag to set encodings when it runs maxima (as suggested in the above-linked FAQ entry).  (For now, I have worked around the problem by moving this file out of my home directory.)

Issue created by migration from https://trac.sagemath.org/ticket/276





---

archive/issue_comments_001308.json:
```json
{
    "body": "Attachment [trac276.patch](tarball://root/attachments/some-uuid/ticket276/trac276.patch) by @williamstein created at 2007-10-21 02:17:36",
    "created_at": "2007-10-21T02:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/276#issuecomment-1308",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac276.patch](tarball://root/attachments/some-uuid/ticket276/trac276.patch) by @williamstein created at 2007-10-21 02:17:36



---

archive/issue_events_000293.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-21T02:17:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/276",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/276#event-293"
}
```



---

archive/issue_comments_001309.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T02:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/276#issuecomment-1309",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
