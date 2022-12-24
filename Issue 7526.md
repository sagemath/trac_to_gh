# Issue 7526: polynomial_template should avoid unnecessary coercions

archive/issues_007526.json:
```json
{
    "body": "Assignee: tbd\n\ne.g. in __mod__, we should coerce other only if needed.\nThis gives great speed up, e.g:\n\n```\nsage: R.<x> = GF(3)[]\nsage: p=x^100 + x^81 + x^67 + x^33 + 1\nsage: q=x^10 + x^8 + x^6 + x^3 + 1\nsage: timeit('p%q')\n625 loops, best of 3: 677 \u00b5s per loop  #Before\n625 loops, best of 3: 60.3 \u00b5s per loop #After\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7526\n\n",
    "created_at": "2009-11-24T21:57:05Z",
    "labels": [
        "performance",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "polynomial_template should avoid unnecessary coercions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7526",
    "user": "ylchapuy"
}
```
Assignee: tbd

e.g. in __mod__, we should coerce other only if needed.
This gives great speed up, e.g:

```
sage: R.<x> = GF(3)[]
sage: p=x^100 + x^81 + x^67 + x^33 + 1
sage: q=x^10 + x^8 + x^6 + x^3 + 1
sage: timeit('p%q')
625 loops, best of 3: 677 µs per loop  #Before
625 loops, best of 3: 60.3 µs per loop #After
```



Issue created by migration from https://trac.sagemath.org/ticket/7526





---

archive/issue_comments_063793.json:
```json
{
    "body": "Attachment [trac_7256-polynomial_template_coercion.patch](tarball://root/attachments/some-uuid/ticket7526/trac_7256-polynomial_template_coercion.patch) by ylchapuy created at 2009-11-24 22:16:05\n\nbased on 4.3.alpha0",
    "created_at": "2009-11-24T22:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7526#issuecomment-63793",
    "user": "ylchapuy"
}
```

Attachment [trac_7256-polynomial_template_coercion.patch](tarball://root/attachments/some-uuid/ticket7526/trac_7256-polynomial_template_coercion.patch) by ylchapuy created at 2009-11-24 22:16:05

based on 4.3.alpha0



---

archive/issue_comments_063794.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-24T22:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7526#issuecomment-63794",
    "user": "ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063795.json:
```json
{
    "body": "I'm not totally sure of how this should be done as I don't know the details of coercions, neither the details of the polynomial templating used.\n\nAt least, my patch doesn't break any doctest for me.\n\nIt touch for methods, the ones using _coerce_.\n\nIt test for parent equality before applying coercion. I also introduce a variable\n\n`parent = (<Polynomial_template>self)._parent`\n\nfor readability.",
    "created_at": "2009-11-24T22:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7526#issuecomment-63795",
    "user": "ylchapuy"
}
```

I'm not totally sure of how this should be done as I don't know the details of coercions, neither the details of the polynomial templating used.

At least, my patch doesn't break any doctest for me.

It touch for methods, the ones using _coerce_.

It test for parent equality before applying coercion. I also introduce a variable

`parent = (<Polynomial_template>self)._parent`

for readability.



---

archive/issue_comments_063796.json:
```json
{
    "body": "The patch looks good and applies & doctests cleanly for me. However, we can do a little better. \n\nOn my machine I get the following:\n\n**Before**\n\n```\nsage: R.<x> = GF(3)[]\nsage: p=x^100 + x^81 + x^67 + x^33 + 1\nsage: q=x^10 + x^8 + x^6 + x^3 + 1\nsage: timeit('p%q')\n625 loops, best of 3: 193 \u00b5s per loop\n```\n\n\n**Patch**\n\n```\nsage: R.<x> = GF(3)[]\nsage: p=x^100 + x^81 + x^67 + x^33 + 1\nsage: q=x^10 + x^8 + x^6 + x^3 + 1\nsage: timeit('p%q')\n625 loops, best of 3: 26.6 \u00b5s per loop\n```\n\n\nWith my incremental reviewer patch I get:\n\n\n```\nsage: R.<x> = GF(3)[]\nsage: p=x^100 + x^81 + x^67 + x^33 + 1\nsage: q=x^10 + x^8 + x^6 + x^3 + 1\nsage: timeit('p%q')\n625 loops, best of 3: 18.2 \u00b5s per loop\n```\n\n\nSo, this is a positive review if someone reviews my reviewer patch.",
    "created_at": "2009-11-25T20:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7526#issuecomment-63796",
    "user": "malb"
}
```

The patch looks good and applies & doctests cleanly for me. However, we can do a little better. 

On my machine I get the following:

**Before**

```
sage: R.<x> = GF(3)[]
sage: p=x^100 + x^81 + x^67 + x^33 + 1
sage: q=x^10 + x^8 + x^6 + x^3 + 1
sage: timeit('p%q')
625 loops, best of 3: 193 µs per loop
```


**Patch**

```
sage: R.<x> = GF(3)[]
sage: p=x^100 + x^81 + x^67 + x^33 + 1
sage: q=x^10 + x^8 + x^6 + x^3 + 1
sage: timeit('p%q')
625 loops, best of 3: 26.6 µs per loop
```


With my incremental reviewer patch I get:


```
sage: R.<x> = GF(3)[]
sage: p=x^100 + x^81 + x^67 + x^33 + 1
sage: q=x^10 + x^8 + x^6 + x^3 + 1
sage: timeit('p%q')
625 loops, best of 3: 18.2 µs per loop
```


So, this is a positive review if someone reviews my reviewer patch.



---

archive/issue_comments_063797.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> So, this is a positive review if someone reviews my reviewer patch.\n\nI think you attached the patch for #7531.",
    "created_at": "2009-11-25T22:37:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7526#issuecomment-63797",
    "user": "ylchapuy"
}
```

Replying to [comment:2 malb]:
> So, this is a positive review if someone reviews my reviewer patch.

I think you attached the patch for #7531.



---

archive/issue_comments_063798.json:
```json
{
    "body": "Attachment [trac_7256-polynomial_template_coercion_faster.patch](tarball://root/attachments/some-uuid/ticket7526/trac_7256-polynomial_template_coercion_faster.patch) by malb created at 2009-11-25 22:47:20\n\nWoops, fixed.",
    "created_at": "2009-11-25T22:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7526#issuecomment-63798",
    "user": "malb"
}
```

Attachment [trac_7256-polynomial_template_coercion_faster.patch](tarball://root/attachments/some-uuid/ticket7526/trac_7256-polynomial_template_coercion_faster.patch) by malb created at 2009-11-25 22:47:20

Woops, fixed.



---

archive/issue_comments_063799.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-25T23:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7526#issuecomment-63799",
    "user": "ylchapuy"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063800.json:
```json
{
    "body": "Great thanks. Still applies fine and doctests ok.\nAnd here is the positive review!",
    "created_at": "2009-11-25T23:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7526#issuecomment-63800",
    "user": "ylchapuy"
}
```

Great thanks. Still applies fine and doctests ok.
And here is the positive review!



---

archive/issue_comments_063801.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T05:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7526#issuecomment-63801",
    "user": "mhansen"
}
```

Resolution: fixed
