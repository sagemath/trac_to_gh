# Issue 5574: taking symbolic powers should coerce objects to symbolic expressions

archive/issues_005574.json:
```json
{
    "body": "CC:  @videlec\n\nReported by Alex Raichev on sage-support:\n\n\n```\nsage: var('n',ns=1)\nn\nsage: (QQbar(2)^3)^n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n<...>\n<...>/sage/rings/qqbar.pyc in __pow__(self, e)\n   2808             1\n   2809         \"\"\"\n-> 2810         e = QQ._coerce_(e)\n   2811         n = e.numerator()\n   2812         d = e.denominator()\n\n<...>/sage/structure/parent_old.so in \nsage.structure.parent_old.Parent._coerce_ (sage/structure\n/parent_old.c:4031)()\n\n<...>/site-packages/sage/structure/parent.so in \nsage.structure.parent.Parent.coerce (sage/structure/parent.c:4185)()\n\nTypeError: no canonical coercion from New Symbolic Ring to Rational\nField\n```\n\n\nSince pynac supports using arbitrary Sage objects as numeric objects in symbolic expressions, we should return a symbolic expression as a result of the above commands.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5574\n\n",
    "created_at": "2009-03-20T10:09:12Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.2",
    "title": "taking symbolic powers should coerce objects to symbolic expressions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5574",
    "user": "https://github.com/burcin"
}
```
CC:  @videlec

Reported by Alex Raichev on sage-support:


```
sage: var('n',ns=1)
n
sage: (QQbar(2)^3)^n
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

<...>
<...>/sage/rings/qqbar.pyc in __pow__(self, e)
   2808             1
   2809         """
-> 2810         e = QQ._coerce_(e)
   2811         n = e.numerator()
   2812         d = e.denominator()

<...>/sage/structure/parent_old.so in 
sage.structure.parent_old.Parent._coerce_ (sage/structure
/parent_old.c:4031)()

<...>/site-packages/sage/structure/parent.so in 
sage.structure.parent.Parent.coerce (sage/structure/parent.c:4185)()

TypeError: no canonical coercion from New Symbolic Ring to Rational
Field
```


Since pynac supports using arbitrary Sage objects as numeric objects in symbolic expressions, we should return a symbolic expression as a result of the above commands.

Issue created by migration from https://trac.sagemath.org/ticket/5574





---

archive/issue_comments_043363.json:
```json
{
    "body": "From sage-support `@`freenode today:\n\n\n```\n<base3___> raising a matrix to a variable power fails with \nNotImplementedError: non-integral exponents not supported,\neven if i do assume(n, 'integer')\n<base3___> am i missing something or should i file this as a bug?\n<burcin> base3___, it's a bug\n```\n",
    "created_at": "2009-04-09T13:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43363",
    "user": "https://github.com/burcin"
}
```

From sage-support `@`freenode today:


```
<base3___> raising a matrix to a variable power fails with 
NotImplementedError: non-integral exponents not supported,
even if i do assume(n, 'integer')
<base3___> am i missing something or should i file this as a bug?
<burcin> base3___, it's a bug
```




---

archive/issue_comments_043364.json:
```json
{
    "body": "This is a general shortcoming of `AlgebraicNumber.__pow__()`:\n\n```\nsage: (QQbar(2)^3)^1.\n...\nTypeError: no canonical coercion from Real Field with 53 bits of precision to Rational Field\n```\n",
    "created_at": "2015-10-19T13:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43364",
    "user": "https://github.com/rwst"
}
```

This is a general shortcoming of `AlgebraicNumber.__pow__()`:

```
sage: (QQbar(2)^3)^1.
...
TypeError: no canonical coercion from Real Field with 53 bits of precision to Rational Field
```




---

archive/issue_comments_043365.json:
```json
{
    "body": "Changing component from symbolics to algebra.",
    "created_at": "2015-10-19T13:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43365",
    "user": "https://github.com/rwst"
}
```

Changing component from symbolics to algebra.



---

archive/issue_comments_043366.json:
```json
{
    "body": "Note that this is not a group action (because of the choice of an n-th root)\n\n```\n((-1)^(1/3))^2 != ((-1)^2)^(1/3).\n```\n\nIsn't that a requirement that `g.(h.x) = (gh).x` for an action in Sage?",
    "created_at": "2018-01-08T11:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43366",
    "user": "https://github.com/videlec"
}
```

Note that this is not a group action (because of the choice of an n-th root)

```
((-1)^(1/3))^2 != ((-1)^2)^(1/3).
```

Isn't that a requirement that `g.(h.x) = (gh).x` for an action in Sage?



---

archive/issue_comments_043367.json:
```json
{
    "body": "Replying to [comment:10 vdelecroix]:\n> Note that this is not a group action (because of the choice of an n-th root)\n> {{{\n> ((-1)<sup>(1/3))</sup>2 != ((-1)<sup>2)</sup>(1/3).\n> }}}\n\nSo what? I don't plan to change any arithmetic, just the underlying implementation. Since we have an operation between 2 different parents (`QQbar` and `QQ`), an action is the right way to implement this.\n\n> Isn't that a requirement that `g.(h.x) = (gh).x` for an action in Sage?\n\nWhy should there be such a requirement? I see an action purely as a technical way to implement a certain operation.",
    "created_at": "2018-01-08T11:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43367",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:10 vdelecroix]:
> Note that this is not a group action (because of the choice of an n-th root)
> {{{
> ((-1)<sup>(1/3))</sup>2 != ((-1)<sup>2)</sup>(1/3).
> }}}

So what? I don't plan to change any arithmetic, just the underlying implementation. Since we have an operation between 2 different parents (`QQbar` and `QQ`), an action is the right way to implement this.

> Isn't that a requirement that `g.(h.x) = (gh).x` for an action in Sage?

Why should there be such a requirement? I see an action purely as a technical way to implement a certain operation.



---

archive/issue_comments_043368.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2018-01-08T13:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43368",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_043369.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-01-08T13:29:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43369",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_043370.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2018-01-09T09:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43370",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_043371.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2018-01-09T10:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43371",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_043372.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2018-01-09T10:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43372",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_043373.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2018-01-18T10:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43373",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_043374.json:
```json
{
    "body": "Rebased to 8.2.beta3",
    "created_at": "2018-01-18T10:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43374",
    "user": "https://github.com/jdemeyer"
}
```

Rebased to 8.2.beta3



---

archive/issue_comments_043375.json:
```json
{
    "body": "This is a dependency for both #24256 and #24500, so it would be good to get this ticket done.",
    "created_at": "2018-01-18T10:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43375",
    "user": "https://github.com/jdemeyer"
}
```

This is a dependency for both #24256 and #24500, so it would be good to get this ticket done.



---

archive/issue_comments_043376.json:
```json
{
    "body": "Is that complient with Sage documentation?\n\n```\nEXAMPLES in ``QQbar``::\n...\nEXAMPLES in ``AA``::\n...\n```\n\nWhy not\n\n```\nEXAMPLES:\n\npowering in ``QQbar``::\n...\npowering in ``AA``::\n...\n```\n",
    "created_at": "2018-01-25T14:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43376",
    "user": "https://github.com/videlec"
}
```

Is that complient with Sage documentation?

```
EXAMPLES in ``QQbar``::
...
EXAMPLES in ``AA``::
...
```

Why not

```
EXAMPLES:

powering in ``QQbar``::
...
powering in ``AA``::
...
```




---

archive/issue_comments_043377.json:
```json
{
    "body": "Timings look like it will be a bit slower. Before\n\n```\nsage: a = AA(5)\nsage: %timeit a^(1/3)\n1000 loops, best of 3: 327 \u00b5s per loop\nsage: a = AA(8)\nsage: %timeit a^(1/3)\n100000 loops, best of 3: 7.78 \u00b5s per loop\n```\n\nAfter\n\n```\nsage: a = AA(5)\nsage: %timeit a^(1/3)\n1000 loops, best of 3: 369 \u00b5s per loop\nsage: a = AA(8)\nsage: %timeit a^(1/3)\n100000 loops, best of 3: 9.64 \u00b5s per loop\n```\n",
    "created_at": "2018-01-25T14:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43377",
    "user": "https://github.com/videlec"
}
```

Timings look like it will be a bit slower. Before

```
sage: a = AA(5)
sage: %timeit a^(1/3)
1000 loops, best of 3: 327 µs per loop
sage: a = AA(8)
sage: %timeit a^(1/3)
100000 loops, best of 3: 7.78 µs per loop
```

After

```
sage: a = AA(5)
sage: %timeit a^(1/3)
1000 loops, best of 3: 369 µs per loop
sage: a = AA(8)
sage: %timeit a^(1/3)
100000 loops, best of 3: 9.64 µs per loop
```




---

archive/issue_comments_043378.json:
```json
{
    "body": "Timings should improve in #24500 but I obviously cannot promise that it will be as fast as before.",
    "created_at": "2018-01-25T16:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43378",
    "user": "https://github.com/jdemeyer"
}
```

Timings should improve in #24500 but I obviously cannot promise that it will be as fast as before.



---

archive/issue_comments_043379.json:
```json
{
    "body": "Replying to [comment:25 vdelecroix]:\n> Is that complient with Sage documentation?\n> {{{\n> EXAMPLES in ``QQbar``::\n> ...\n> EXAMPLES in ``AA``::\n> ...\n> }}}\n\nThere are some cases like that already in Sage. I don't see the problem, but if you insist, then I will change it.",
    "created_at": "2018-01-25T16:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43379",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:25 vdelecroix]:
> Is that complient with Sage documentation?
> {{{
> EXAMPLES in ``QQbar``::
> ...
> EXAMPLES in ``AA``::
> ...
> }}}

There are some cases like that already in Sage. I don't see the problem, but if you insist, then I will change it.



---

archive/issue_comments_043380.json:
```json
{
    "body": "Replying to [comment:28 jdemeyer]:\n> Replying to [comment:25 vdelecroix]:\n> > Is that complient with Sage documentation?\n> > {{{\n> > EXAMPLES in ``QQbar``::\n> > ...\n> > EXAMPLES in ``AA``::\n> > ...\n> > }}}\n> \n> There are some cases like that already in Sage. I don't see the problem, but if you insist, then I will change it.\n\nMy reference is http://doc.sagemath.org/html/en/developer/coding_basics.html#documentation-strings (and not the rest of Sage).",
    "created_at": "2018-01-25T16:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43380",
    "user": "https://github.com/videlec"
}
```

Replying to [comment:28 jdemeyer]:
> Replying to [comment:25 vdelecroix]:
> > Is that complient with Sage documentation?
> > {{{
> > EXAMPLES in ``QQbar``::
> > ...
> > EXAMPLES in ``AA``::
> > ...
> > }}}
> 
> There are some cases like that already in Sage. I don't see the problem, but if you insist, then I will change it.

My reference is http://doc.sagemath.org/html/en/developer/coding_basics.html#documentation-strings (and not the rest of Sage).



---

archive/issue_comments_043381.json:
```json
{
    "body": "I don't see anything in the docs saying that an `EXAMPLES` block should start exactly with the line `EXAMPLES::`",
    "created_at": "2018-01-25T17:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43381",
    "user": "https://github.com/jdemeyer"
}
```

I don't see anything in the docs saying that an `EXAMPLES` block should start exactly with the line `EXAMPLES::`



---

archive/issue_comments_043382.json:
```json
{
    "body": "This is different from Sphinx blocks like `.. WARNING::` because those are handled specially. But there is nothing special about `EXAMPLES`.",
    "created_at": "2018-01-25T17:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43382",
    "user": "https://github.com/jdemeyer"
}
```

This is different from Sphinx blocks like `.. WARNING::` because those are handled specially. But there is nothing special about `EXAMPLES`.



---

archive/issue_comments_043383.json:
```json
{
    "body": "Replying to [comment:31 jdemeyer]:\n> This is different from Sphinx blocks like `.. WARNING::` because those are handled specially. But there is nothing special about `EXAMPLES`.\n\n`TESTS` is also handled specially (hided in the doc). And `EXAMPLES` might in the future (e.g. interactive execution in Jupyter).",
    "created_at": "2018-01-25T23:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43383",
    "user": "https://github.com/videlec"
}
```

Replying to [comment:31 jdemeyer]:
> This is different from Sphinx blocks like `.. WARNING::` because those are handled specially. But there is nothing special about `EXAMPLES`.

`TESTS` is also handled specially (hided in the doc). And `EXAMPLES` might in the future (e.g. interactive execution in Jupyter).



---

archive/issue_comments_043384.json:
```json
{
    "body": "Replying to [comment:32 vdelecroix]:\n> And `EXAMPLES` might in the future (e.g. interactive execution in Jupyter).\n\nThat would be a bad idea. Executable commands should be limited to the `EXAMPLES` block.\n\nAnd if some software really wants to treat `EXAMPLES` blocks specially, it should still recognize `EXAMPLES in ``QQbar``` as `EXAMPLES` block.\n\nAnyway, if you really want me to change it, just say so.",
    "created_at": "2018-01-26T08:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43384",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:32 vdelecroix]:
> And `EXAMPLES` might in the future (e.g. interactive execution in Jupyter).

That would be a bad idea. Executable commands should be limited to the `EXAMPLES` block.

And if some software really wants to treat `EXAMPLES` blocks specially, it should still recognize `EXAMPLES in ``QQbar``` as `EXAMPLES` block.

Anyway, if you really want me to change it, just say so.



---

archive/issue_comments_043385.json:
```json
{
    "body": "Replying to [comment:33 jdemeyer]:\n> Replying to [comment:32 vdelecroix]:\n> > And `EXAMPLES` might in the future (e.g. interactive execution in Jupyter).\n> \n> That would be a bad idea. Executable commands should be limited to the `EXAMPLES` block.\n> \n> And if some software really wants to treat `EXAMPLES` blocks specially, it should still recognize `EXAMPLES in ``QQbar``` as `EXAMPLES` block.\n> \n> Anyway, if you really want me to change it, just say so.\n\nPlease do.",
    "created_at": "2018-01-26T09:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43385",
    "user": "https://github.com/videlec"
}
```

Replying to [comment:33 jdemeyer]:
> Replying to [comment:32 vdelecroix]:
> > And `EXAMPLES` might in the future (e.g. interactive execution in Jupyter).
> 
> That would be a bad idea. Executable commands should be limited to the `EXAMPLES` block.
> 
> And if some software really wants to treat `EXAMPLES` blocks specially, it should still recognize `EXAMPLES in ``QQbar``` as `EXAMPLES` block.
> 
> Anyway, if you really want me to change it, just say so.

Please do.



---

archive/issue_comments_043386.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-01-29T16:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43386",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_043387.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-01-29T22:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43387",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_005819.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2018-02-02T12:06:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5574#event-5819"
}
```



---

archive/issue_comments_043388.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2018-02-02T12:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5574#issuecomment-43388",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
