# Issue 5600: Cleanup of integer compositions

archive/issues_005600.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat jbandlow\n\nFix  some weirdness of http://wiki.sagemath.org/combinat/Weirdness:\nSee compositions-cleanup-....-nt.patch\n\nAccept any iterable as input\nAdds concatenation of compositions\n\nIssue created by migration from https://trac.sagemath.org/ticket/5600\n\n",
    "created_at": "2009-03-24T21:10:07Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Cleanup of integer compositions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5600",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat jbandlow

Fix  some weirdness of http://wiki.sagemath.org/combinat/Weirdness:
See compositions-cleanup-....-nt.patch

Accept any iterable as input
Adds concatenation of compositions

Issue created by migration from https://trac.sagemath.org/ticket/5600





---

archive/issue_comments_043658.json:
```json
{
    "body": "Changing keywords from \"\" to \"integer compositions\".",
    "created_at": "2009-05-03T02:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5600#issuecomment-43658",
    "user": "nthiery"
}
```

Changing keywords from "" to "integer compositions".



---

archive/issue_comments_043659.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-19T06:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5600#issuecomment-43659",
    "user": "nthiery"
}
```

Attachment



---

archive/issue_comments_043660.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-19T06:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5600#issuecomment-43660",
    "user": "nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043661.json:
```json
{
    "body": "I very much want this patch to get in, since I almost opened a ticket for one of the problems that it fixes. (`Composition()` doesn't take tuples as input.) One thing that needs to change, though, is with the docstring for Composition: right now, it tells the user to do `Composition_class?`, but that doesn't work since `Composition_class` is not in the default namespace. I think `Composition?` should simply display the correct docstring; there's no need to annoy the user by sending him or her bouncing from one docstring to the next.\n\nAnother issue is that the AUTHORS block is deleted from the head of the file. This should not be done. In fact, you should add yourself to it as the [developer's guide suggests](http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files): something like \"Nicolas M. Thiery (2009-05-25): several cleanups, new functions, and improvements (trac #5600)\". I like listing ticket numbers because interested developers can go see exactly what you changed.\n\nTiny grammar/spelling issues:\n\n* At the top of compositions.py, you write \"a compositions c of...\"; you should use the singular. \"A composition c of...\"\n* line 56: you say a composition is a list of *positive* integers, but it should be a list of *nonnegative* integers.\n\nFinally, I am seeing a doctest failure with this patch applied to vanilla 4.0.rc0:\n\n```\n**********************************************************************\nFile \"/var/tmp/sage-4.0.rc0/devel/sage/sage/combinat/ribbon_tableau.py\", line 875:\n    sage: SemistandardMultiSkewTableaux([sp[0], sp[-1]],[2,2,2]).list()\nExpected:\n    [[[[1], [2], [3]], [[1, 2, 3]]]]\nGot:\n    [[[[1, 1, 2]], [[None, None, 3], [None, 3], [2]]], [[[1, 2, 2]], [[None, None, 3], [None, 3], [1]]], [[[1, 1, 2]], [[None, None, 3], [None, 2], [3]]], [[[1, 2, 2]], [[None, None, 3], [None, 1], [3]]], [[[1, 1, 2]], [[None, None, 2], [None, 3], [3]]], [[[1, 2, 2]], [[None, None, 1], [None, 3], [3]]], [[[1, 1, 3]], [[None, None, 3], [None, 2], [2]]], [[[1, 2, 3]], [[None, None, 3], [None, 2], [1]]], [[[1, 2, 3]], [[None, None, 3], [None, 1], [2]]], [[[2, 2, 3]], [[None, None, 3], [None, 1], [1]]], [[[1, 1, 3]], [[None, None, 2], [None, 3], [2]]], [[[1, 2, 3]], [[None, None, 2], [None, 3], [1]]], [[[1, 2, 3]], [[None, None, 1], [None, 3], [2]]], [[[2, 2, 3]], [[None, None, 1], [None, 3], [1]]], [[[1, 1, 3]], [[None, None, 2], [None, 2], [3]]], [[[1, 2, 3]], [[None, None, 2], [None, 1], [3]]], [[[1, 2, 3]], [[None, None, 1], [None, 2], [3]]], [[[2, 2, 3]], [[None, None, 1], [None, 1], [3]]], [[[1, 3, 3]], [[None, None, 2], [None, 2], [1]]], [[[1, 3, 3]], [[None, None, 2], [None, 1], [2]]], [[[1, 3, 3]], [[None, None, 1], [None, 2], [2]]], [[[2, 3, 3]], [[None, None, 2], [None, 1], [1]]], [[[2, 3, 3]], [[None, None, 1], [None, 2], [1]]], [[[2, 3, 3]], [[None, None, 1], [None, 1], [2]]]]\n**********************************************************************\n```\n",
    "created_at": "2009-05-25T06:16:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5600#issuecomment-43661",
    "user": "ddrake"
}
```

I very much want this patch to get in, since I almost opened a ticket for one of the problems that it fixes. (`Composition()` doesn't take tuples as input.) One thing that needs to change, though, is with the docstring for Composition: right now, it tells the user to do `Composition_class?`, but that doesn't work since `Composition_class` is not in the default namespace. I think `Composition?` should simply display the correct docstring; there's no need to annoy the user by sending him or her bouncing from one docstring to the next.

Another issue is that the AUTHORS block is deleted from the head of the file. This should not be done. In fact, you should add yourself to it as the [developer's guide suggests](http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files): something like "Nicolas M. Thiery (2009-05-25): several cleanups, new functions, and improvements (trac #5600)". I like listing ticket numbers because interested developers can go see exactly what you changed.

Tiny grammar/spelling issues:

* At the top of compositions.py, you write "a compositions c of..."; you should use the singular. "A composition c of..."
* line 56: you say a composition is a list of *positive* integers, but it should be a list of *nonnegative* integers.

Finally, I am seeing a doctest failure with this patch applied to vanilla 4.0.rc0:

```
**********************************************************************
File "/var/tmp/sage-4.0.rc0/devel/sage/sage/combinat/ribbon_tableau.py", line 875:
    sage: SemistandardMultiSkewTableaux([sp[0], sp[-1]],[2,2,2]).list()
Expected:
    [[[[1], [2], [3]], [[1, 2, 3]]]]
Got:
    [[[[1, 1, 2]], [[None, None, 3], [None, 3], [2]]], [[[1, 2, 2]], [[None, None, 3], [None, 3], [1]]], [[[1, 1, 2]], [[None, None, 3], [None, 2], [3]]], [[[1, 2, 2]], [[None, None, 3], [None, 1], [3]]], [[[1, 1, 2]], [[None, None, 2], [None, 3], [3]]], [[[1, 2, 2]], [[None, None, 1], [None, 3], [3]]], [[[1, 1, 3]], [[None, None, 3], [None, 2], [2]]], [[[1, 2, 3]], [[None, None, 3], [None, 2], [1]]], [[[1, 2, 3]], [[None, None, 3], [None, 1], [2]]], [[[2, 2, 3]], [[None, None, 3], [None, 1], [1]]], [[[1, 1, 3]], [[None, None, 2], [None, 3], [2]]], [[[1, 2, 3]], [[None, None, 2], [None, 3], [1]]], [[[1, 2, 3]], [[None, None, 1], [None, 3], [2]]], [[[2, 2, 3]], [[None, None, 1], [None, 3], [1]]], [[[1, 1, 3]], [[None, None, 2], [None, 2], [3]]], [[[1, 2, 3]], [[None, None, 2], [None, 1], [3]]], [[[1, 2, 3]], [[None, None, 1], [None, 2], [3]]], [[[2, 2, 3]], [[None, None, 1], [None, 1], [3]]], [[[1, 3, 3]], [[None, None, 2], [None, 2], [1]]], [[[1, 3, 3]], [[None, None, 2], [None, 1], [2]]], [[[1, 3, 3]], [[None, None, 1], [None, 2], [2]]], [[[2, 3, 3]], [[None, None, 2], [None, 1], [1]]], [[[2, 3, 3]], [[None, None, 1], [None, 2], [1]]], [[[2, 3, 3]], [[None, None, 1], [None, 1], [2]]]]
**********************************************************************
```




---

archive/issue_comments_043662.json:
```json
{
    "body": "The updated patch fixes the (the failure was actually actually a trivial thing in the doctest; thanks to Jason for spotting this!)",
    "created_at": "2009-07-29T11:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5600#issuecomment-43662",
    "user": "nthiery"
}
```

The updated patch fixes the (the failure was actually actually a trivial thing in the doctest; thanks to Jason for spotting this!)



---

archive/issue_comments_043663.json:
```json
{
    "body": "Attachment\n\nApply only this one, yes, this one!",
    "created_at": "2009-07-29T12:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5600#issuecomment-43663",
    "user": "nthiery"
}
```

Attachment

Apply only this one, yes, this one!



---

archive/issue_comments_043664.json:
```json
{
    "body": "Doctests pass, and it looks like Dan's issues have been resolved.  Positive review from me.",
    "created_at": "2009-07-29T16:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5600#issuecomment-43664",
    "user": "jbandlow"
}
```

Doctests pass, and it looks like Dan's issues have been resolved.  Positive review from me.



---

archive/issue_comments_043665.json:
```json
{
    "body": "Attachment\n\nreviewer patch",
    "created_at": "2009-08-22T23:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5600#issuecomment-43665",
    "user": "mvngu"
}
```

Attachment

reviewer patch



---

archive/issue_comments_043666.json:
```json
{
    "body": "I'm attaching the reviewer patch `trac_5600-reviewer.patch`. It fixes a number of typos introduced by `trac_5600-compositions_cleanup-nt.patch`, and edits some docstrings so they look a bit nicer when one views the corresponding pages in the reference manual. If people are happy with my reviewer patch `trac_5600-reviewer.patch`, then patches should be merged in this order:\n\n1. `trac_5600-compositions_cleanup-nt.patch`\n2. `trac_5600-reviewer.patch`",
    "created_at": "2009-08-22T23:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5600#issuecomment-43666",
    "user": "mvngu"
}
```

I'm attaching the reviewer patch `trac_5600-reviewer.patch`. It fixes a number of typos introduced by `trac_5600-compositions_cleanup-nt.patch`, and edits some docstrings so they look a bit nicer when one views the corresponding pages in the reference manual. If people are happy with my reviewer patch `trac_5600-reviewer.patch`, then patches should be merged in this order:

1. `trac_5600-compositions_cleanup-nt.patch`
2. `trac_5600-reviewer.patch`



---

archive/issue_comments_043667.json:
```json
{
    "body": "Replying to [comment:10 mvngu]:\n> I'm attaching the reviewer patch `trac_5600-reviewer.patch`. It fixes a number of typos introduced by `trac_5600-compositions_cleanup-nt.patch`, and edits some docstrings so they look a bit nicer when one views the corresponding pages in the reference manual. If people are happy with my reviewer patch `trac_5600-reviewer.patch`, then patches should be merged in this order:\n> \n>  1. `trac_5600-compositions_cleanup-nt.patch`\n>  1. `trac_5600-reviewer.patch`\n\nThanks much for fixing all those typos! positive review on your reviewer's patch.",
    "created_at": "2009-08-22T23:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5600#issuecomment-43667",
    "user": "nthiery"
}
```

Replying to [comment:10 mvngu]:
> I'm attaching the reviewer patch `trac_5600-reviewer.patch`. It fixes a number of typos introduced by `trac_5600-compositions_cleanup-nt.patch`, and edits some docstrings so they look a bit nicer when one views the corresponding pages in the reference manual. If people are happy with my reviewer patch `trac_5600-reviewer.patch`, then patches should be merged in this order:
> 
>  1. `trac_5600-compositions_cleanup-nt.patch`
>  1. `trac_5600-reviewer.patch`

Thanks much for fixing all those typos! positive review on your reviewer's patch.



---

archive/issue_comments_043668.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_5600-compositions_cleanup-nt.patch`\n2. `trac_5600-reviewer.patch`",
    "created_at": "2009-08-23T01:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5600#issuecomment-43668",
    "user": "mvngu"
}
```

Merged patches in this order:

1. `trac_5600-compositions_cleanup-nt.patch`
2. `trac_5600-reviewer.patch`



---

archive/issue_comments_043669.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-23T01:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5600#issuecomment-43669",
    "user": "mvngu"
}
```

Resolution: fixed
