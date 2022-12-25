# Issue 8023: doctest in combinat/words/morphism.py creates a file "test.sobj" not in a temporary directory

archive/issues_008023.json:
```json
{
    "body": "Assignee: sage-combinat\n\nDoctests in Sage should only create files in temporary directories, like SAGE_TMP.  The attached patch fixes a doctest in sage/combinat/words/morphism.py.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8023\n\n",
    "created_at": "2010-01-21T06:34:37Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "doctest in combinat/words/morphism.py creates a file \"test.sobj\" not in a temporary directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8023",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: sage-combinat

Doctests in Sage should only create files in temporary directories, like SAGE_TMP.  The attached patch fixes a doctest in sage/combinat/words/morphism.py.

Issue created by migration from https://trac.sagemath.org/ticket/8023





---

archive/issue_comments_069977.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-21T06:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8023#issuecomment-69977",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069978.json:
```json
{
    "body": "Attachment [trac_8023-sagetmp.patch](tarball://root/attachments/some-uuid/ticket8023/trac_8023-sagetmp.patch) by @jhpalmieri created at 2010-01-21 06:35:52",
    "created_at": "2010-01-21T06:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8023#issuecomment-69978",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8023-sagetmp.patch](tarball://root/attachments/some-uuid/ticket8023/trac_8023-sagetmp.patch) by @jhpalmieri created at 2010-01-21 06:35:52



---

archive/issue_comments_069979.json:
```json
{
    "body": "#5155 has a similar fix along with other stuff for preventing stuff to be written to $SAGE_ROOT",
    "created_at": "2010-01-21T18:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8023#issuecomment-69979",
    "user": "https://github.com/mwhansen"
}
```

#5155 has a similar fix along with other stuff for preventing stuff to be written to $SAGE_ROOT



---

archive/issue_comments_069980.json:
```json
{
    "body": "Replying to [comment:2 mhansen]:\n> #5155 has a similar fix along with other stuff for preventing stuff to be written to $SAGE_ROOT\n\nOkay, I'll mark this as a duplicate.",
    "created_at": "2010-01-21T21:04:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8023#issuecomment-69980",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:2 mhansen]:
> #5155 has a similar fix along with other stuff for preventing stuff to be written to $SAGE_ROOT

Okay, I'll mark this as a duplicate.



---

archive/issue_comments_069981.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-21T21:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8023#issuecomment-69981",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: duplicate



---

archive/issue_events_008234.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-01-21T21:54:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8023",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8023#event-8234"
}
```
