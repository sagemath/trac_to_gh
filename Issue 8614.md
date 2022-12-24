# Issue 8614: Optimize creation of modular symbols spaces by speeding up quotienting out by 2-term relations

archive/issues_008614.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  alexghitza\n\n* The attached patch speeds up a creating ModularSymbols spaces a bunch by removing a bottleneck -- quotienting by 2-term relations -- by moving it to Cython. \n\n* Also the coverage for the modsym directory is improved to 100% by adding one trivial missing doctest.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8614\n\n",
    "created_at": "2010-03-27T03:29:42Z",
    "labels": [
        "modular forms",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "Optimize creation of modular symbols spaces by speeding up quotienting out by 2-term relations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8614",
    "user": "@williamstein"
}
```
Assignee: @craigcitro

CC:  alexghitza

* The attached patch speeds up a creating ModularSymbols spaces a bunch by removing a bottleneck -- quotienting by 2-term relations -- by moving it to Cython. 

* Also the coverage for the modsym directory is improved to 100% by adding one trivial missing doctest.

Issue created by migration from https://trac.sagemath.org/ticket/8614





---

archive/issue_comments_078053.json:
```json
{
    "body": "Attachment [trac_8614.patch](tarball://root/attachments/some-uuid/ticket8614/trac_8614.patch) by @williamstein created at 2010-03-27 03:44:06",
    "created_at": "2010-03-27T03:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78053",
    "user": "@williamstein"
}
```

Attachment [trac_8614.patch](tarball://root/attachments/some-uuid/ticket8614/trac_8614.patch) by @williamstein created at 2010-03-27 03:44:06



---

archive/issue_comments_078054.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-27T03:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78054",
    "user": "@williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078055.json:
```json
{
    "body": "Which cases do you expect to be most speeded up by this patch? I ran some tests and it actually seems to make things marginally *slower* in the cases I tried:\n\nBefore:\n\n```\nsage: time ModularSymbols(2002, 2)\nCPU times: user 1.52 s, sys: 0.41 s, total: 1.93 s\nWall time: 1.93 s\nModular Symbols space of dimension 673 for Gamma_0(2002) of weight 2 with sign 0 over Rational Field\nsage: time ModularSymbols(302, 4)\nCPU times: user 2.21 s, sys: 0.00 s, total: 2.21 s\nWall time: 2.21 s\nModular Symbols space of dimension 228 for Gamma_0(302) of weight 4 with sign 0 over Rational Field\nsage: time ModularSymbols(Gamma1(33), 4)\nCPU times: user 3.04 s, sys: 0.46 s, total: 3.49 s\nWall time: 3.49 s\nModular Symbols space of dimension 240 for Gamma_1(33) of weight 4 with sign 0 and over Rational Field\nsage: time ModularSymbols(DirichletGroup(308).0, 5)\nCPU times: user 5.94 s, sys: 0.65 s, total: 6.59 s\nWall time: 6.59 s\nModular Symbols space of dimension 384 and level 308, weight 5, character [-1, 1, 1], sign 0, over Rational Field\n```\n\n\nAfter:\n\n```\nsage: time ModularSymbols(2002, 2)\nCPU times: user 1.52 s, sys: 0.67 s, total: 2.19 s\nWall time: 2.19 s\nModular Symbols space of dimension 673 for Gamma_0(2002) of weight 2 with sign 0 over Rational Field\nsage: time ModularSymbols(302, 4)\nCPU times: user 2.12 s, sys: 0.18 s, total: 2.30 s\nWall time: 2.30 s\nModular Symbols space of dimension 228 for Gamma_0(302) of weight 4 with sign 0 over Rational Field\nsage: time ModularSymbols(Gamma1(33), 4)\nCPU times: user 2.66 s, sys: 0.90 s, total: 3.57 s\nWall time: 3.57 s\nModular Symbols space of dimension 240 for Gamma_1(33) of weight 4 with sign 0 and over Rational Field\nsage: time ModularSymbols(DirichletGroup(308).0, 5)\nCPU times: user 5.97 s, sys: 0.71 s, total: 6.68 s\nWall time: 6.68 s\nModular Symbols space of dimension 384 and level 308, weight 5, character [-1, 1, 1], sign 0, over Rational Field\n```\n",
    "created_at": "2010-03-27T13:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78055",
    "user": "@loefflerd"
}
```

Which cases do you expect to be most speeded up by this patch? I ran some tests and it actually seems to make things marginally *slower* in the cases I tried:

Before:

```
sage: time ModularSymbols(2002, 2)
CPU times: user 1.52 s, sys: 0.41 s, total: 1.93 s
Wall time: 1.93 s
Modular Symbols space of dimension 673 for Gamma_0(2002) of weight 2 with sign 0 over Rational Field
sage: time ModularSymbols(302, 4)
CPU times: user 2.21 s, sys: 0.00 s, total: 2.21 s
Wall time: 2.21 s
Modular Symbols space of dimension 228 for Gamma_0(302) of weight 4 with sign 0 over Rational Field
sage: time ModularSymbols(Gamma1(33), 4)
CPU times: user 3.04 s, sys: 0.46 s, total: 3.49 s
Wall time: 3.49 s
Modular Symbols space of dimension 240 for Gamma_1(33) of weight 4 with sign 0 and over Rational Field
sage: time ModularSymbols(DirichletGroup(308).0, 5)
CPU times: user 5.94 s, sys: 0.65 s, total: 6.59 s
Wall time: 6.59 s
Modular Symbols space of dimension 384 and level 308, weight 5, character [-1, 1, 1], sign 0, over Rational Field
```


After:

```
sage: time ModularSymbols(2002, 2)
CPU times: user 1.52 s, sys: 0.67 s, total: 2.19 s
Wall time: 2.19 s
Modular Symbols space of dimension 673 for Gamma_0(2002) of weight 2 with sign 0 over Rational Field
sage: time ModularSymbols(302, 4)
CPU times: user 2.12 s, sys: 0.18 s, total: 2.30 s
Wall time: 2.30 s
Modular Symbols space of dimension 228 for Gamma_0(302) of weight 4 with sign 0 over Rational Field
sage: time ModularSymbols(Gamma1(33), 4)
CPU times: user 2.66 s, sys: 0.90 s, total: 3.57 s
Wall time: 3.57 s
Modular Symbols space of dimension 240 for Gamma_1(33) of weight 4 with sign 0 and over Rational Field
sage: time ModularSymbols(DirichletGroup(308).0, 5)
CPU times: user 5.97 s, sys: 0.71 s, total: 6.68 s
Wall time: 6.68 s
Modular Symbols space of dimension 384 and level 308, weight 5, character [-1, 1, 1], sign 0, over Rational Field
```




---

archive/issue_comments_078056.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-04-03T06:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78056",
    "user": "@aghitza"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_078057.json:
```json
{
    "body": "It appears to be significantly better for high weights:\n\nOn sage-4.6.1, before the patch:\n\n\n```\nsage: time M = ModularSymbols(1, 810, 0, GF(809))\nCPU times: user 51.57 s, sys: 0.45 s, total: 52.02 s\nWall time: 52.03 s\n```\n\n\nAfter the patch:\n\n\n```\nsage: time M = ModularSymbols(1, 810, 0, GF(809))\nCPU times: user 16.40 s, sys: 0.17 s, total: 16.57 s\nWall time: 16.58 s\n```\n\n\nThis makes me *very* happy.",
    "created_at": "2011-01-18T00:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78057",
    "user": "@aghitza"
}
```

It appears to be significantly better for high weights:

On sage-4.6.1, before the patch:


```
sage: time M = ModularSymbols(1, 810, 0, GF(809))
CPU times: user 51.57 s, sys: 0.45 s, total: 52.02 s
Wall time: 52.03 s
```


After the patch:


```
sage: time M = ModularSymbols(1, 810, 0, GF(809))
CPU times: user 16.40 s, sys: 0.17 s, total: 16.57 s
Wall time: 16.58 s
```


This makes me *very* happy.



---

archive/issue_comments_078058.json:
```json
{
    "body": "According to the profiler, that difference seems to be coming almost entirely from the optimizations to `binomial`. The much larger chunk of new code in `relation_matrix.pyx` code only gets called when (among other conditions) the base ring is the rationals; and it doesn't seem to make much of an impact on the speed.\n\nI suggest we split this into two tickets: one for the changes to binomial and the other miscellaneous fixes, which I would be happy to give a positive review to on the spot, and the other for the cythonization of the 2-term relations stuff, which seems a bit less clear-cut to me.",
    "created_at": "2011-01-26T14:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78058",
    "user": "@loefflerd"
}
```

According to the profiler, that difference seems to be coming almost entirely from the optimizations to `binomial`. The much larger chunk of new code in `relation_matrix.pyx` code only gets called when (among other conditions) the base ring is the rationals; and it doesn't seem to make much of an impact on the speed.

I suggest we split this into two tickets: one for the changes to binomial and the other miscellaneous fixes, which I would be happy to give a positive review to on the spot, and the other for the cythonization of the 2-term relations stuff, which seems a bit less clear-cut to me.



---

archive/issue_comments_078059.json:
```json
{
    "body": "Replying to [comment:7 davidloeffler]:\n> According to the profiler, that difference seems to be coming almost entirely from the optimizations to `binomial`. The much larger chunk of new code in `relation_matrix.pyx` code only gets called when (among other conditions) the base ring is the rationals; and it doesn't seem to make much of an impact on the speed.\n> \n> I suggest we split this into two tickets: one for the changes to binomial and the other miscellaneous fixes, which I would be happy to give a positive review to on the spot, and the other for the cythonization of the 2-term relations stuff, which seems a bit less clear-cut to me.\n\nI agree, and I had noticed the point about `binomial` myself.  It's late (or really early) here, but I'll try to split off the easier bits tomorrow.",
    "created_at": "2011-01-26T14:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78059",
    "user": "@aghitza"
}
```

Replying to [comment:7 davidloeffler]:
> According to the profiler, that difference seems to be coming almost entirely from the optimizations to `binomial`. The much larger chunk of new code in `relation_matrix.pyx` code only gets called when (among other conditions) the base ring is the rationals; and it doesn't seem to make much of an impact on the speed.
> 
> I suggest we split this into two tickets: one for the changes to binomial and the other miscellaneous fixes, which I would be happy to give a positive review to on the spot, and the other for the cythonization of the 2-term relations stuff, which seems a bit less clear-cut to me.

I agree, and I had noticed the point about `binomial` myself.  It's late (or really early) here, but I'll try to split off the easier bits tomorrow.



---

archive/issue_comments_078060.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2011-01-26T14:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78060",
    "user": "@aghitza"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_078061.json:
```json
{
    "body": "OK, so I have split off the part not directly involved in the 2-term relations into two other tickets: #10709 for the binomial coefficients in the matrix actions on Manin symbols, and #10710 for the various docstring/doctest/comment fixes.\n\nI will soon update the patch on this ticket by removing those parts.",
    "created_at": "2011-01-29T06:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78061",
    "user": "@aghitza"
}
```

OK, so I have split off the part not directly involved in the 2-term relations into two other tickets: #10709 for the binomial coefficients in the matrix actions on Manin symbols, and #10710 for the various docstring/doctest/comment fixes.

I will soon update the patch on this ticket by removing those parts.



---

archive/issue_comments_078062.json:
```json
{
    "body": "Attachment [trac-8614-optimize-modular-symbol-relations-rebase.patch](tarball://root/attachments/some-uuid/ticket8614/trac-8614-optimize-modular-symbol-relations-rebase.patch) by mraum created at 2011-03-22 02:25:56\n\nI rebased the patch to 4.7alpha2 (with #10709 applied). Its not true that the new code is slower. I ran the following small tests:\n\n\n```\n%time M = ModularSymbols(1000,2,sign=1).new_subspace().cuspidal_subspace()\n%time t3 = M.hecke_matrix(3)\n%time time d = t3.decomposition(algorithm='multimodular', height_guess=1)\n\n%time ModularSymbols(2002, 2)\n%time ModularSymbols(302, 4)\n%time ModularSymbols(Gamma1(33), 4)\n%time ModularSymbols(DirichletGroup(308).0, 5)\n%time M = ModularSymbols(1, 810, 0, GF(809))\n```\n\n\nWithout the patch:\n\n```\nWall time: 2.92 s\nWall time: 0.19 s\nWall time: 0.09 s\n\nWall time: 1.34 s\nWall time: 4.08 s\nWall time: 2.20 s\nWall time: 10.97 s\nWall time: 16.23 s\n```\n\n\nWith the patch applied:\n\n```\nWall time: 2.77 s\nWall time: 0.13 s\nWall time: 0.09 s\n\nWall time: 1.22 s\nWall time: 4.38 s\nWall time: 2.10 s\nWall time: 11.12 s\nWall time: 15.33 s\n```\n\n\nNone of the differences is significant in the sense that %timeit could reproduce it. A profile\n\n```\n%prun M = ModularSymbols(Gamma1(52), 4)\n```\n\nshows that indeed the new code is three times as fast as the old one. But since the relevant function only needs 0.1s and 0.03s, respectively, this can be hardly tracked.\n\nMartin",
    "created_at": "2011-03-22T02:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78062",
    "user": "mraum"
}
```

Attachment [trac-8614-optimize-modular-symbol-relations-rebase.patch](tarball://root/attachments/some-uuid/ticket8614/trac-8614-optimize-modular-symbol-relations-rebase.patch) by mraum created at 2011-03-22 02:25:56

I rebased the patch to 4.7alpha2 (with #10709 applied). Its not true that the new code is slower. I ran the following small tests:


```
%time M = ModularSymbols(1000,2,sign=1).new_subspace().cuspidal_subspace()
%time t3 = M.hecke_matrix(3)
%time time d = t3.decomposition(algorithm='multimodular', height_guess=1)

%time ModularSymbols(2002, 2)
%time ModularSymbols(302, 4)
%time ModularSymbols(Gamma1(33), 4)
%time ModularSymbols(DirichletGroup(308).0, 5)
%time M = ModularSymbols(1, 810, 0, GF(809))
```


Without the patch:

```
Wall time: 2.92 s
Wall time: 0.19 s
Wall time: 0.09 s

Wall time: 1.34 s
Wall time: 4.08 s
Wall time: 2.20 s
Wall time: 10.97 s
Wall time: 16.23 s
```


With the patch applied:

```
Wall time: 2.77 s
Wall time: 0.13 s
Wall time: 0.09 s

Wall time: 1.22 s
Wall time: 4.38 s
Wall time: 2.10 s
Wall time: 11.12 s
Wall time: 15.33 s
```


None of the differences is significant in the sense that %timeit could reproduce it. A profile

```
%prun M = ModularSymbols(Gamma1(52), 4)
```

shows that indeed the new code is three times as fast as the old one. But since the relevant function only needs 0.1s and 0.03s, respectively, this can be hardly tracked.

Martin



---

archive/issue_comments_078063.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-22T02:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78063",
    "user": "mraum"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078064.json:
```json
{
    "body": "The patch looks good to me (applied to 4.7.alpha2) and I am testing now, by testing whether ModularSymbols(N) and CremonaModularSymbols(N) have the same dimension for N up to `10^4`.  And some more.",
    "created_at": "2011-03-25T19:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78064",
    "user": "@JohnCremona"
}
```

The patch looks good to me (applied to 4.7.alpha2) and I am testing now, by testing whether ModularSymbols(N) and CremonaModularSymbols(N) have the same dimension for N up to `10^4`.  And some more.



---

archive/issue_comments_078065.json:
```json
{
    "body": "Replying to [comment:11 cremona]:\n> The patch looks good to me (applied to 4.7.alpha2) and I am testing now, by testing whether ModularSymbols(N) and CremonaModularSymbols(N) have the same dimension for N up to `10^4`.  And some more.\n\n\n```\nsage: time a=[CremonaModularSymbols(N).dimension() for N in [1000..2000]]\nCPU times: user 31.12 s, sys: 0.52 s, total: 31.64 s\nWall time: 31.68 s\nsage: time b=[ModularSymbols(N).dimension() for N in [1000..2000]]       \nCPU times: user 636.90 s, sys: 0.14 s, total: 637.04 s\nWall time: 637.91 s\nsage: a==b\nTrue\n```\n\n\nThis is enough to convince me that the implementation is ok.  I tested the complete library too.",
    "created_at": "2011-03-25T22:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78065",
    "user": "@JohnCremona"
}
```

Replying to [comment:11 cremona]:
> The patch looks good to me (applied to 4.7.alpha2) and I am testing now, by testing whether ModularSymbols(N) and CremonaModularSymbols(N) have the same dimension for N up to `10^4`.  And some more.


```
sage: time a=[CremonaModularSymbols(N).dimension() for N in [1000..2000]]
CPU times: user 31.12 s, sys: 0.52 s, total: 31.64 s
Wall time: 31.68 s
sage: time b=[ModularSymbols(N).dimension() for N in [1000..2000]]       
CPU times: user 636.90 s, sys: 0.14 s, total: 637.04 s
Wall time: 637.91 s
sage: a==b
True
```


This is enough to convince me that the implementation is ok.  I tested the complete library too.



---

archive/issue_comments_078066.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-25T22:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78066",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078067.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-13T07:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8614#issuecomment-78067",
    "user": "@jdemeyer"
}
```

Resolution: fixed
