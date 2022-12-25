# Issue 6206: move algebraic_closure method from RLF to LazyField

archive/issues_006206.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  craigcitro fwclarke robertwb\n\nKeywords: number field lazy field algebraic_closure\n\nTiny patch moves algebraic_closure method up the tree; I claim this is \"obviously\" the correct place for it to be, but you only hit this bug (missing method) when you are using strange embeddings of number fields and I don't have a good example at hand.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6206\n\n",
    "created_at": "2009-06-04T03:45:24Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "move algebraic_closure method from RLF to LazyField",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6206",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  craigcitro fwclarke robertwb

Keywords: number field lazy field algebraic_closure

Tiny patch moves algebraic_closure method up the tree; I claim this is "obviously" the correct place for it to be, but you only hit this bug (missing method) when you are using strange embeddings of number fields and I don't have a good example at hand.

Issue created by migration from https://trac.sagemath.org/ticket/6206





---

archive/issue_comments_049483.json:
```json
{
    "body": "Attachment [trac_6206-real_lazy-algebraic-closure.patch](tarball://root/attachments/some-uuid/ticket6206/trac_6206-real_lazy-algebraic-closure.patch) by @ncalexan created at 2009-06-04 03:45:56",
    "created_at": "2009-06-04T03:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6206#issuecomment-49483",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_6206-real_lazy-algebraic-closure.patch](tarball://root/attachments/some-uuid/ticket6206/trac_6206-real_lazy-algebraic-closure.patch) by @ncalexan created at 2009-06-04 03:45:56



---

archive/issue_comments_049484.json:
```json
{
    "body": "Yes, that makes sense.",
    "created_at": "2009-06-04T06:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6206#issuecomment-49484",
    "user": "https://github.com/robertwb"
}
```

Yes, that makes sense.



---

archive/issue_comments_049485.json:
```json
{
    "body": "Just a sec, while we're at it, I just noticed the docstring is wrong. It speaks of the \"Complex Double Field\" rather than \"Complex Lazy Field.\" This was probably originally my fault, but might as well fix it now.",
    "created_at": "2009-06-04T06:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6206#issuecomment-49485",
    "user": "https://github.com/robertwb"
}
```

Just a sec, while we're at it, I just noticed the docstring is wrong. It speaks of the "Complex Double Field" rather than "Complex Lazy Field." This was probably originally my fault, but might as well fix it now.



---

archive/issue_comments_049486.json:
```json
{
    "body": "Merged in 4.0.1.rc1 (and took care of the double -> lazy change.",
    "created_at": "2009-06-04T18:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6206#issuecomment-49486",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.1.rc1 (and took care of the double -> lazy change.



---

archive/issue_comments_049487.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T18:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6206#issuecomment-49487",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_014560.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-04T18:25:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6206",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6206#event-14560"
}
```
