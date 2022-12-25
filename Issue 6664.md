# Issue 6664: [with patch, needs review] Skip nested classes in docs by Sphinx v0.6.x

archive/issues_006664.json:
```json
{
    "body": "Assignee: tba\n\nSphinx complains about nested classes when building the reference manual.\n\nThis just tweaks #6419 so that it works with Sphinx v0.6.x's `autodoc` extension.  See [comment:#6586:10 this comment] at #6586 for more.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6664\n\n",
    "created_at": "2009-08-02T09:39:43Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] Skip nested classes in docs by Sphinx v0.6.x",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6664",
    "user": "https://github.com/qed777"
}
```
Assignee: tba

Sphinx complains about nested classes when building the reference manual.

This just tweaks #6419 so that it works with Sphinx v0.6.x's `autodoc` extension.  See [comment:#6586:10 this comment] at #6586 for more.

Issue created by migration from https://trac.sagemath.org/ticket/6664





---

archive/issue_comments_054596.json:
```json
{
    "body": "Attachment [trac_6664-skip_nested.patch](tarball://root/attachments/some-uuid/ticket6664/trac_6664-skip_nested.patch) by @qed777 created at 2009-08-02 10:37:54\n\n\"Depends\" on #6586.",
    "created_at": "2009-08-02T10:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6664#issuecomment-54596",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6664-skip_nested.patch](tarball://root/attachments/some-uuid/ticket6664/trac_6664-skip_nested.patch) by @qed777 created at 2009-08-02 10:37:54

"Depends" on #6586.



---

archive/issue_comments_054597.json:
```json
{
    "body": "This suppresses the private methods (`__init__`, etc.).  I'm not sure this is a good idea.  Before the transition to Sphinx, these were included in the reference manual, and then they weren't post-Sphinx, I think mainly because the default was to not include them.  I think they should be included.",
    "created_at": "2009-08-23T18:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6664#issuecomment-54597",
    "user": "https://github.com/jhpalmieri"
}
```

This suppresses the private methods (`__init__`, etc.).  I'm not sure this is a good idea.  Before the transition to Sphinx, these were included in the reference manual, and then they weren't post-Sphinx, I think mainly because the default was to not include them.  I think they should be included.



---

archive/issue_comments_054598.json:
```json
{
    "body": "Sounds good.  I should have understood and [remembered](http://groups.google.com/group/sage-devel/browse_thread/thread/80a99dc2c2836a7b/ad3407f7714349bf).  How about a docbuild option to select between \"developer\" and \"user\" documentation?  Or is this not a meaningful distinction?  Are there any private methods we should always suppress?   Of course, we can just close this ticket (or mark it as invalid).",
    "created_at": "2009-08-23T18:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6664#issuecomment-54598",
    "user": "https://github.com/qed777"
}
```

Sounds good.  I should have understood and [remembered](http://groups.google.com/group/sage-devel/browse_thread/thread/80a99dc2c2836a7b/ad3407f7714349bf).  How about a docbuild option to select between "developer" and "user" documentation?  Or is this not a meaningful distinction?  Are there any private methods we should always suppress?   Of course, we can just close this ticket (or mark it as invalid).



---

archive/issue_comments_054599.json:
```json
{
    "body": "I think that having different versions of the reference manual was discussed at some point, but without definite outcomes or guidelines.  Maybe it should be discussed on sage-devel?\n\nAt the moment, though, including private methods is a bit problematic.  First, `__weakref__` appears sort of at random, and then some classes get all sorts of weird extra methods, maybe inherited from another class?  See the `Matrix` class in `SAGE_ROOT/devel/sage/doc/output/html/en/reference/sage/matrix/matrix0.html`, for example; there is an entry for `__delitem__`, and the entry for `__init__` is wrong: it looks generic rather than the one which is actually in the file.  Maybe this has to do with it being Cython rather than Python.\n\nIs it better to exclude all private methods, or to include them at the price of having all sorts of extra crap in addition?  I say we continue to exclude them until we can figure out how to fix this.  So let's keep this patch for now.  I'll give it a positive review.\n\nDoes this really depend on #6586, or can it be merged now?",
    "created_at": "2009-08-23T21:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6664#issuecomment-54599",
    "user": "https://github.com/jhpalmieri"
}
```

I think that having different versions of the reference manual was discussed at some point, but without definite outcomes or guidelines.  Maybe it should be discussed on sage-devel?

At the moment, though, including private methods is a bit problematic.  First, `__weakref__` appears sort of at random, and then some classes get all sorts of weird extra methods, maybe inherited from another class?  See the `Matrix` class in `SAGE_ROOT/devel/sage/doc/output/html/en/reference/sage/matrix/matrix0.html`, for example; there is an entry for `__delitem__`, and the entry for `__init__` is wrong: it looks generic rather than the one which is actually in the file.  Maybe this has to do with it being Cython rather than Python.

Is it better to exclude all private methods, or to include them at the price of having all sorts of extra crap in addition?  I say we continue to exclude them until we can figure out how to fix this.  So let's keep this patch for now.  I'll give it a positive review.

Does this really depend on #6586, or can it be merged now?



---

archive/issue_events_015723.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2009-08-23T21:22:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6664",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6664#event-15723"
}
```



---

archive/issue_comments_054600.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n> Does this really depend on #6586, or can it be merged now?\n\nIt's not dependent, according to `du -s`.  I tested this with and without the patch, with Sphinx 0.5.1.",
    "created_at": "2009-08-24T04:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6664#issuecomment-54600",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:4 jhpalmieri]:
> Does this really depend on #6586, or can it be merged now?

It's not dependent, according to `du -s`.  I tested this with and without the patch, with Sphinx 0.5.1.



---

archive/issue_events_015724.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-29T11:40:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6664",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6664#event-15724"
}
```



---

archive/issue_comments_054601.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-29T11:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6664#issuecomment-54601",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
