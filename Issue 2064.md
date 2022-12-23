# Issue 2064: foo?? doesn't know about cpdef from the command line

archive/issues_002064.json:
```json
{
    "body": "Assignee: ncalexan\n\nCC:  jhpalmieri robertwb\n\nIf you cpdef a function foo, and do foo?? from the command line, it displays both foo and the next function after it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2064\n\n",
    "created_at": "2008-02-05T21:38:25Z",
    "labels": [
        "algebraic geometry",
        "trivial",
        "bug"
    ],
    "title": "foo?? doesn't know about cpdef from the command line",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2064",
    "user": "craigcitro"
}
```
Assignee: ncalexan

CC:  jhpalmieri robertwb

If you cpdef a function foo, and do foo?? from the command line, it displays both foo and the next function after it.

Issue created by migration from https://trac.sagemath.org/ticket/2064





---

archive/issue_comments_013358.json:
```json
{
    "body": "Changing component from algebraic geometry to misc.",
    "created_at": "2008-02-16T17:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13358",
    "user": "AlexGhitza"
}
```

Changing component from algebraic geometry to misc.



---

archive/issue_comments_013359.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13359",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_013360.json:
```json
{
    "body": "Recognize Cython tokens in source-code introspection.  **sage** repository.",
    "created_at": "2010-02-02T04:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13360",
    "user": "mpatel"
}
```

Recognize Cython tokens in source-code introspection.  **sage** repository.



---

archive/issue_comments_013361.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-02T04:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13361",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_013362.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2010-02-02T04:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13362",
    "user": "mpatel"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_013363.json:
```json
{
    "body": "Attachment\n\nI've attached a patch uses a modified `inspect.BlockFinder` to recognize the `cdef` and `cpdef` tokens.  This appears to work for me, but I'm not a Cython expert.\n\nCurrently, the notebook has its own `sagenb.misc.sageinspect` and this has diverged in several places from `sage.misc.sageinspect`.  If the approach here is OK, I'll open a separate ticket to reconcile the files and fixes this problem in the notebook.",
    "created_at": "2010-02-02T04:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13363",
    "user": "mpatel"
}
```

Attachment

I've attached a patch uses a modified `inspect.BlockFinder` to recognize the `cdef` and `cpdef` tokens.  This appears to work for me, but I'm not a Cython expert.

Currently, the notebook has its own `sagenb.misc.sageinspect` and this has diverged in several places from `sage.misc.sageinspect`.  If the approach here is OK, I'll open a separate ticket to reconcile the files and fixes this problem in the notebook.



---

archive/issue_comments_013364.json:
```json
{
    "body": "Changing component from misc to documentation.",
    "created_at": "2010-02-06T03:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13364",
    "user": "mpatel"
}
```

Changing component from misc to documentation.



---

archive/issue_comments_013365.json:
```json
{
    "body": "This seems to fix the problem for me (I tried `sage.rings.integer.Integer._act_on??` before and after the patch), but I'm not a Cython expert either.  Robert: can you look at it or suggest some else?",
    "created_at": "2010-02-07T19:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13365",
    "user": "jhpalmieri"
}
```

This seems to fix the problem for me (I tried `sage.rings.integer.Integer._act_on??` before and after the patch), but I'm not a Cython expert either.  Robert: can you look at it or suggest some else?



---

archive/issue_comments_013366.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-09T20:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13366",
    "user": "roed"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_013367.json:
```json
{
    "body": "I looked at the Python inspect module, and this seems like a sane modification.  It works for all of us.  \n\nMy main suggestion would be to remove \"cdef\" from the list of keywords you're looking for.  Since this is introspection, you can't ever see cdef'd functions, and I'm slightly worried that there's some use case where the other uses of that keyword in Cython could trip you up.\n\nOther than that, I'm happy to give it a positive review.",
    "created_at": "2010-02-09T20:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13367",
    "user": "roed"
}
```

I looked at the Python inspect module, and this seems like a sane modification.  It works for all of us.  

My main suggestion would be to remove "cdef" from the list of keywords you're looking for.  Since this is introspection, you can't ever see cdef'd functions, and I'm slightly worried that there's some use case where the other uses of that keyword in Cython could trip you up.

Other than that, I'm happy to give it a positive review.



---

archive/issue_comments_013368.json:
```json
{
    "body": "Removes \"cdef\" from keyword list.  Apply only this patch.",
    "created_at": "2010-02-16T21:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13368",
    "user": "mpatel"
}
```

Removes "cdef" from keyword list.  Apply only this patch.



---

archive/issue_comments_013369.json:
```json
{
    "body": "Attachment\n\nV2 adds only \"cpdef\" to the token search (or search for tokens).",
    "created_at": "2010-02-16T21:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13369",
    "user": "mpatel"
}
```

Attachment

V2 adds only "cpdef" to the token search (or search for tokens).



---

archive/issue_comments_013370.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-16T21:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13370",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_013371.json:
```json
{
    "body": "Yep.  Looks fine to me now.",
    "created_at": "2010-02-16T21:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13371",
    "user": "roed"
}
```

Yep.  Looks fine to me now.



---

archive/issue_comments_013372.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-16T21:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13372",
    "user": "roed"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_013373.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-17T20:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13373",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_013374.json:
```json
{
    "body": "Merged [trac_2064-sage_cpdef_inspect.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/2064/trac_2064-sage_cpdef_inspect.2.patch).",
    "created_at": "2010-02-17T20:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2064#issuecomment-13374",
    "user": "mvngu"
}
```

Merged [trac_2064-sage_cpdef_inspect.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/2064/trac_2064-sage_cpdef_inspect.2.patch).
