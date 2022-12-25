# Issue 7316: notebook: default values for variables are printed incorrectly in docstrings

archive/issues_007316.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein\n\nFrom [sage-notebook](http://groups.google.com/group/sage-notebook/browse_frm/thread/28a506759aac37ae):\n\n```\n> I notice that in Sage 4.2, the version of sageinspect in the notebook \n> doesn't match the one in sage.misc -- the one in sagenb/misc is \n> missing the fix from Trac #6848.  As a result, \n> {{{ \n> RDF.random_element? \n> }}} \n> produces incorrect output, as noted on the ticket.  Should this be \n> fixed, or was the fix intentionally omitted because it uses \"eval\"? \n```\n\nFor the fix, see the patch at #6848, especially the new lines 269-270 (and the associated doctest fixes).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7316\n\n",
    "created_at": "2009-10-26T23:31:35Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "notebook: default values for variables are printed incorrectly in docstrings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7316",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: boothby

CC:  @williamstein

From [sage-notebook](http://groups.google.com/group/sage-notebook/browse_frm/thread/28a506759aac37ae):

```
> I notice that in Sage 4.2, the version of sageinspect in the notebook 
> doesn't match the one in sage.misc -- the one in sagenb/misc is 
> missing the fix from Trac #6848.  As a result, 
> {{{ 
> RDF.random_element? 
> }}} 
> produces incorrect output, as noted on the ticket.  Should this be 
> fixed, or was the fix intentionally omitted because it uses "eval"? 
```

For the fix, see the patch at #6848, especially the new lines 269-270 (and the associated doctest fixes).


Issue created by migration from https://trac.sagemath.org/ticket/7316





---

archive/issue_comments_061020.json:
```json
{
    "body": "Attachment [trac_7316-sageinspect_defn.patch](tarball://root/attachments/some-uuid/ticket7316/trac_7316-sageinspect_defn.patch) by @qed777 created at 2009-10-27 02:48:40\n\nFix Cython docstring \"Definition\". Rebase of sageinspect part of #6848. Apply to sagenb repository.",
    "created_at": "2009-10-27T02:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7316#issuecomment-61020",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7316-sageinspect_defn.patch](tarball://root/attachments/some-uuid/ticket7316/trac_7316-sageinspect_defn.patch) by @qed777 created at 2009-10-27 02:48:40

Fix Cython docstring "Definition". Rebase of sageinspect part of #6848. Apply to sagenb repository.



---

archive/issue_comments_061021.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-27T02:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7316#issuecomment-61021",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061022.json:
```json
{
    "body": "All doctests pass, if I copy the patched `sagenb.misc.sageinspect.py` to `$SAGE_ROOT/devel/sage/sage`, say, and run `sage -t sageinspect.py` in that directory.\n\nTo the extent that it counts, my review is positive.",
    "created_at": "2009-10-27T02:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7316#issuecomment-61022",
    "user": "https://github.com/qed777"
}
```

All doctests pass, if I copy the patched `sagenb.misc.sageinspect.py` to `$SAGE_ROOT/devel/sage/sage`, say, and run `sage -t sageinspect.py` in that directory.

To the extent that it counts, my review is positive.



---

archive/issue_comments_061023.json:
```json
{
    "body": "Is this now a duplicate of #7349?",
    "created_at": "2009-10-29T17:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7316#issuecomment-61023",
    "user": "https://github.com/jhpalmieri"
}
```

Is this now a duplicate of #7349?



---

archive/issue_comments_061024.json:
```json
{
    "body": "Doctests count and the the bugs are fixed. Positive review.",
    "created_at": "2009-10-29T18:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7316#issuecomment-61024",
    "user": "https://github.com/TimDumol"
}
```

Doctests count and the the bugs are fixed. Positive review.



---

archive/issue_comments_061025.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-29T18:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7316#issuecomment-61025",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061026.json:
```json
{
    "body": "merged into sagenb-0.4.2 (sage-4.2.1)",
    "created_at": "2009-11-11T19:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7316#issuecomment-61026",
    "user": "https://github.com/williamstein"
}
```

merged into sagenb-0.4.2 (sage-4.2.1)



---

archive/issue_comments_061027.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-11T19:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7316#issuecomment-61027",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
