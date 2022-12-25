# Issue 8174: maxima_methods wrapper for symbolic expressions

archive/issues_008174.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @kcrisman @jasongrout @robert-marik\n\nAttached patch provides a `.maxima_methods()` function in symbolic expressions to give access to various methods of simplification, etc. available in Maxima. The return values of functions called through this interface are Sage expressions. Tab completion and docstrings work as expected.\n\nThis was proposed on sage-devel:\n\nhttp://groups.google.com/group/sage-devel/t/3899a578da747009\n\nIssue created by migration from https://trac.sagemath.org/ticket/8174\n\n",
    "created_at": "2010-02-03T14:56:36Z",
    "labels": [
        "component: symbolics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "maxima_methods wrapper for symbolic expressions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8174",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

CC:  @kcrisman @jasongrout @robert-marik

Attached patch provides a `.maxima_methods()` function in symbolic expressions to give access to various methods of simplification, etc. available in Maxima. The return values of functions called through this interface are Sage expressions. Tab completion and docstrings work as expected.

This was proposed on sage-devel:

http://groups.google.com/group/sage-devel/t/3899a578da747009

Issue created by migration from https://trac.sagemath.org/ticket/8174





---

archive/issue_comments_071897.json:
```json
{
    "body": "Attachment [trac_8174-maxima_methods.patch](tarball://root/attachments/some-uuid/ticket8174/trac_8174-maxima_methods.patch) by @burcin created at 2010-02-03 14:58:05",
    "created_at": "2010-02-03T14:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8174#issuecomment-71897",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8174-maxima_methods.patch](tarball://root/attachments/some-uuid/ticket8174/trac_8174-maxima_methods.patch) by @burcin created at 2010-02-03 14:58:05



---

archive/issue_comments_071898.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-03T14:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8174#issuecomment-71898",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071899.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-04T18:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8174#issuecomment-71899",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071900.json:
```json
{
    "body": "Overall this is very nice.  I have two questions.\n\n1. If I do type(u) (for instance), I just get 'instance' as the type, whereas for something like t._maxima_() I get type giving a Maxima interface element or something.  Is there any way to make type(u) give something more useful (perhaps inheriting from another class?  I don't know.).\n\n2. Tab-completion works great, and just like as with other Maxima things (which means getting functions which don't actually apply, such as triangularize, but whatever, since it's the same behavior).  But one of the doctests for it doesn't seem to work - I get [] instead of the appropriate list.  Do you have some extra initialization in your Maxima that allows u.trigs to complete to the appropriate thing, but not u.simplify (this is the one that returns [] for me)?  I should point out that u.simplify[tab] doesn't work either for me, so the doctest is behaving 'correctly in that sense.",
    "created_at": "2010-02-04T18:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8174#issuecomment-71900",
    "user": "https://github.com/kcrisman"
}
```

Overall this is very nice.  I have two questions.

1. If I do type(u) (for instance), I just get 'instance' as the type, whereas for something like t._maxima_() I get type giving a Maxima interface element or something.  Is there any way to make type(u) give something more useful (perhaps inheriting from another class?  I don't know.).

2. Tab-completion works great, and just like as with other Maxima things (which means getting functions which don't actually apply, such as triangularize, but whatever, since it's the same behavior).  But one of the doctests for it doesn't seem to work - I get [] instead of the appropriate list.  Do you have some extra initialization in your Maxima that allows u.trigs to complete to the appropriate thing, but not u.simplify (this is the one that returns [] for me)?  I should point out that u.simplify[tab] doesn't work either for me, so the doctest is behaving 'correctly in that sense.



---

archive/issue_comments_071901.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> 1. If I do type(u) (for instance), I just get 'instance' as the type, whereas for something like t._maxima_() I get type giving a Maxima interface element or something.  Is there any way to make type(u) give something more useful (perhaps inheriting from another class?  I don't know.).\n\nInheriting from `SageObject` fixed this. I also added `_repr_` and `__reduce__` methods.\n\n> 2. Tab-completion works great, and just like as with other Maxima things (which means getting functions which don't actually apply, such as triangularize, but whatever, since it's the same behavior).  But one of the doctests for it doesn't seem to work - I get [] instead of the appropriate list.  Do you have some extra initialization in your Maxima that allows u.trigs to complete to the appropriate thing, but not u.simplify (this is the one that returns [] for me)?  I should point out that u.simplify[tab] doesn't work either for me, so the doctest is behaving 'correctly in that sense.\n\nOn 4.3.3.alpha1, `u.trigs` was triggering different completions for me too. I changed the doctest to look for completions to `airy_` and `elliptic_`. The output of these is less likely to change between maxima versions. I don't know why tab completion with `simplify` doesn't work for you, perhaps this was related to #8223.",
    "created_at": "2010-02-20T12:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8174#issuecomment-71901",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:2 kcrisman]:
> 1. If I do type(u) (for instance), I just get 'instance' as the type, whereas for something like t._maxima_() I get type giving a Maxima interface element or something.  Is there any way to make type(u) give something more useful (perhaps inheriting from another class?  I don't know.).

Inheriting from `SageObject` fixed this. I also added `_repr_` and `__reduce__` methods.

> 2. Tab-completion works great, and just like as with other Maxima things (which means getting functions which don't actually apply, such as triangularize, but whatever, since it's the same behavior).  But one of the doctests for it doesn't seem to work - I get [] instead of the appropriate list.  Do you have some extra initialization in your Maxima that allows u.trigs to complete to the appropriate thing, but not u.simplify (this is the one that returns [] for me)?  I should point out that u.simplify[tab] doesn't work either for me, so the doctest is behaving 'correctly in that sense.

On 4.3.3.alpha1, `u.trigs` was triggering different completions for me too. I changed the doctest to look for completions to `airy_` and `elliptic_`. The output of these is less likely to change between maxima versions. I don't know why tab completion with `simplify` doesn't work for you, perhaps this was related to #8223.



---

archive/issue_comments_071902.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-20T12:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8174#issuecomment-71902",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071903.json:
```json
{
    "body": "Attachment [trac_8174-maxima_methods.take2.patch](tarball://root/attachments/some-uuid/ticket8174/trac_8174-maxima_methods.take2.patch) by @burcin created at 2010-02-20 12:29:18\n\napply only this patch",
    "created_at": "2010-02-20T12:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8174#issuecomment-71903",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8174-maxima_methods.take2.patch](tarball://root/attachments/some-uuid/ticket8174/trac_8174-maxima_methods.take2.patch) by @burcin created at 2010-02-20 12:29:18

apply only this patch



---

archive/issue_comments_071904.json:
```json
{
    "body": "Very useful patch, thanks. Long tests passed on 4.4.rc0.\n\nPositive review. Apply only trac_8174-maxima_methods.take2.patch",
    "created_at": "2010-04-29T05:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8174#issuecomment-71904",
    "user": "https://github.com/robert-marik"
}
```

Very useful patch, thanks. Long tests passed on 4.4.rc0.

Positive review. Apply only trac_8174-maxima_methods.take2.patch



---

archive/issue_comments_071905.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-29T05:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8174#issuecomment-71905",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071906.json:
```json
{
    "body": "Merged [trac_8174-maxima_methods.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8174/trac_8174-maxima_methods.take2.patch).",
    "created_at": "2010-05-08T22:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8174#issuecomment-71906",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_8174-maxima_methods.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8174/trac_8174-maxima_methods.take2.patch).



---

archive/issue_comments_071907.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T22:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8174#issuecomment-71907",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_019575.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-08T22:08:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8174",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8174#event-19575"
}
```
