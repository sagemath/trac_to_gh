# Issue 8595: Fixed point of word morphism is broken on some tuple input

archive/issues_008595.json:
```json
{
    "body": "Assignee: slabbe\n\nCC:  vdelecroix\n\nFrom [sage-combinat-devel group](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/3d5e4db608049516?hl=en) :\n\n\n```\n\n2010/3/23 Vincent Delecroix\n> Hi,\n>\n> I tried the following and get an unexpected error\n>\n> {{{\n> sage: s = WordMorphism({'a1': ['a1','a2'], 'a2':['a1']})\n> sage: s.fixed_point('a1')\n> Traceback\n> ...\n> KeyError: 'a'\n> }}}\n>\n> and it does the same for tuples\n>\n> {{{\n> sage: s = WordMorphism({('a', 1) : [('a', 1), ('a', 2)], ('a', 2) : [('a', 1)]})\n> sage: s.fixed_point(('a', 1))\n> Traceback\n> ...\n> KeyError: 'a'\n> }}}\n>\n> Is it a bug or not the right way to do ?\n>\n> (On this example it looks strange but I really need product alphabet)\n>\n> Cheers,\n> Vincent\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8595\n\n",
    "created_at": "2010-03-24T14:29:12Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Fixed point of word morphism is broken on some tuple input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8595",
    "user": "slabbe"
}
```
Assignee: slabbe

CC:  vdelecroix

From [sage-combinat-devel group](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/3d5e4db608049516?hl=en) :


```

2010/3/23 Vincent Delecroix
> Hi,
>
> I tried the following and get an unexpected error
>
> {{{
> sage: s = WordMorphism({'a1': ['a1','a2'], 'a2':['a1']})
> sage: s.fixed_point('a1')
> Traceback
> ...
> KeyError: 'a'
> }}}
>
> and it does the same for tuples
>
> {{{
> sage: s = WordMorphism({('a', 1) : [('a', 1), ('a', 2)], ('a', 2) : [('a', 1)]})
> sage: s.fixed_point(('a', 1))
> Traceback
> ...
> KeyError: 'a'
> }}}
>
> Is it a bug or not the right way to do ?
>
> (On this example it looks strange but I really need product alphabet)
>
> Cheers,
> Vincent

```


Issue created by migration from https://trac.sagemath.org/ticket/8595





---

archive/issue_comments_077826.json:
```json
{
    "body": "Attachment [trac_8595_fixed_point-sl.patch](tarball://root/attachments/some-uuid/ticket8595/trac_8595_fixed_point-sl.patch) by slabbe created at 2010-03-25 10:34:39",
    "created_at": "2010-03-25T10:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8595#issuecomment-77826",
    "user": "slabbe"
}
```

Attachment [trac_8595_fixed_point-sl.patch](tarball://root/attachments/some-uuid/ticket8595/trac_8595_fixed_point-sl.patch) by slabbe created at 2010-03-25 10:34:39



---

archive/issue_comments_077827.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-25T10:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8595#issuecomment-77827",
    "user": "slabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077828.json:
```json
{
    "body": "The bug seems to be resolved by the patch! Great.",
    "created_at": "2010-03-25T10:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8595#issuecomment-77828",
    "user": "vdelecroix"
}
```

The bug seems to be resolved by the patch! Great.



---

archive/issue_comments_077829.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-25T10:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8595#issuecomment-77829",
    "user": "vdelecroix"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077830.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8595#issuecomment-77830",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_077831.json:
```json
{
    "body": "Merged \"trac_8595_fixed_point-sl.patch\" in 4.4.alpha0.",
    "created_at": "2010-04-16T18:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8595#issuecomment-77831",
    "user": "jhpalmieri"
}
```

Merged "trac_8595_fixed_point-sl.patch" in 4.4.alpha0.
