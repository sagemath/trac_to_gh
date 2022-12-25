# Issue 5945: fastify factorization of inferior integers with flint

archive/issues_005945.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @zimmermann6\n\nFLINT can factor faster than PARI for integers smaller than 2^50 or so.  So by default, we should use FLINT for this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5945\n\n",
    "created_at": "2009-04-30T06:15:16Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "fastify factorization of inferior integers with flint",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5945",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: tbd

CC:  @zimmermann6

FLINT can factor faster than PARI for integers smaller than 2^50 or so.  So by default, we should use FLINT for this.

Issue created by migration from https://trac.sagemath.org/ticket/5945





---

archive/issue_comments_046912.json:
```json
{
    "body": "Note, we'll need an upgraded FLINT for this to work.  Among other things, FLINT exports a global variable named \"primes\".  And so does PARI.  And they don't play well with eachother.\n\nAlso, the attached code contains a bug.  And Factorization objects can be made with less overhead.",
    "created_at": "2009-04-30T06:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46912",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Note, we'll need an upgraded FLINT for this to work.  Among other things, FLINT exports a global variable named "primes".  And so does PARI.  And they don't play well with eachother.

Also, the attached code contains a bug.  And Factorization objects can be made with less overhead.



---

archive/issue_comments_046913.json:
```json
{
    "body": "The attached fixes aforementioned bug.  New spkg coming soon.",
    "created_at": "2009-04-30T07:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46913",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

The attached fixes aforementioned bug.  New spkg coming soon.



---

archive/issue_comments_046914.json:
```json
{
    "body": "Changing component from algebra to factorization.",
    "created_at": "2009-04-30T07:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46914",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from algebra to factorization.



---

archive/issue_comments_046915.json:
```json
{
    "body": "Replying to [comment:3 boothby]:\n> The attached fixes aforementioned bug.  New spkg coming soon.\n\nWhat is the plan here? Right now from my end I want to get the latest released upstream into 3.4.2, so it would be nice if you got your code into FLINT and then get Bill to release it. That way the Debian people won't complain ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T07:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46915",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:3 boothby]:
> The attached fixes aforementioned bug.  New spkg coming soon.

What is the plan here? Right now from my end I want to get the latest released upstream into 3.4.2, so it would be nice if you got your code into FLINT and then get Bill to release it. That way the Debian people won't complain ;)

Cheers,

Michael



---

archive/issue_comments_046916.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-10-06T19:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46916",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_046917.json:
```json
{
    "body": "I created a new ticket #10211 for changes in long_extras.pxd, to get this fixed faster.",
    "created_at": "2010-11-04T10:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46917",
    "user": "https://github.com/a-andre"
}
```

I created a new ticket #10211 for changes in long_extras.pxd, to get this fixed faster.



---

archive/issue_comments_046918.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-08T09:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46918",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_046919.json:
```json
{
    "body": "Attachment [5945_check_improvements.sage](tarball://root/attachments/some-uuid/ticket5945/5945_check_improvements.sage) by @a-andre created at 2010-11-08 09:29:12\n\nI decided to move `flint_factor` to `fast_arith.pyx`, so it can be used for `int`, too.\nTo check the improvements use attachment:5945_check_improvements.patch, attachment:5945_check_improvements.sage and\n\n```\n(line(values_p)+line(values_f,color='red')).plot()\n(line(values_med_p)+line(values_med_f,color='red')).plot()\n```\n",
    "created_at": "2010-11-08T09:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46919",
    "user": "https://github.com/a-andre"
}
```

Attachment [5945_check_improvements.sage](tarball://root/attachments/some-uuid/ticket5945/5945_check_improvements.sage) by @a-andre created at 2010-11-08 09:29:12

I decided to move `flint_factor` to `fast_arith.pyx`, so it can be used for `int`, too.
To check the improvements use attachment:5945_check_improvements.patch, attachment:5945_check_improvements.sage and

```
(line(values_p)+line(values_f,color='red')).plot()
(line(values_med_p)+line(values_med_f,color='red')).plot()
```




---

archive/issue_comments_046920.json:
```json
{
    "body": "Attachment [trac_5945_flintfactor.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945_flintfactor.patch) by @a-andre created at 2010-11-10 10:07:42\n\napply only this patch; apply after #10211",
    "created_at": "2010-11-10T10:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46920",
    "user": "https://github.com/a-andre"
}
```

Attachment [trac_5945_flintfactor.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945_flintfactor.patch) by @a-andre created at 2010-11-10 10:07:42

apply only this patch; apply after #10211



---

archive/issue_comments_046921.json:
```json
{
    "body": "Attachment [5945_check_improvements.patch](tarball://root/attachments/some-uuid/ticket5945/5945_check_improvements.patch) by @a-andre created at 2010-11-10 10:08:15\n\nonly to check improvements, not for release",
    "created_at": "2010-11-10T10:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46921",
    "user": "https://github.com/a-andre"
}
```

Attachment [5945_check_improvements.patch](tarball://root/attachments/some-uuid/ticket5945/5945_check_improvements.patch) by @a-andre created at 2010-11-10 10:08:15

only to check improvements, not for release



---

archive/issue_comments_046922.json:
```json
{
    "body": "patch updated to fix problem buildbot has\n\n```\n2010-12-03 10:18:03 -0800\nhg qpush trac_5945_factor_flint.patch\napplying trac_5945_factor_flint.patch\npatching file sage/rings/arith.py\nHunk #2 FAILED at 2076\n1 out of 2 hunks FAILED -- saving rejects to file sage/rings/arith.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_5945_factor_flint.patch\npatch queue now empty\nNone\n2010-12-03 10:18:04 -0800\n0 seconds\n```\n",
    "created_at": "2010-12-06T15:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46922",
    "user": "https://github.com/a-andre"
}
```

patch updated to fix problem buildbot has

```
2010-12-03 10:18:03 -0800
hg qpush trac_5945_factor_flint.patch
applying trac_5945_factor_flint.patch
patching file sage/rings/arith.py
Hunk #2 FAILED at 2076
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/arith.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_5945_factor_flint.patch
patch queue now empty
None
2010-12-03 10:18:04 -0800
0 seconds
```




---

archive/issue_comments_046923.json:
```json
{
    "body": "only apply this patch",
    "created_at": "2010-12-08T09:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46923",
    "user": "https://github.com/a-andre"
}
```

only apply this patch



---

archive/issue_comments_046924.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-08T06:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46924",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_046925.json:
```json
{
    "body": "Attachment [trac_5945_factor_flint.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945_factor_flint.patch) by spancratz created at 2011-01-08 06:49:32\n\nThanks for doing this!\n\nLooking at the source code, the line ``flint_bits = int(FLINT_BITS)`` seems wrong.  You can (and should, I think) simply use FLINT_BITS directly.  Of course, this comment is rather minor.\n\nSebastian",
    "created_at": "2011-01-08T06:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46925",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac_5945_factor_flint.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945_factor_flint.patch) by spancratz created at 2011-01-08 06:49:32

Thanks for doing this!

Looking at the source code, the line ``flint_bits = int(FLINT_BITS)`` seems wrong.  You can (and should, I think) simply use FLINT_BITS directly.  Of course, this comment is rather minor.

Sebastian



---

archive/issue_comments_046926.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-10T06:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46926",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_046927.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-10T07:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46927",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_046928.json:
```json
{
    "body": "segfault in arith.py",
    "created_at": "2011-01-10T07:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46928",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

segfault in arith.py



---

archive/issue_comments_046929.json:
```json
{
    "body": "I tried to apply your patch to 4.6.1 rc1\n\n```\napplying /scratch/sage-4.6.1rc1/trac_5945bp.patch\npatching file sage/rings/arith.py\nHunk #2 FAILED at 2290\n1 out of 2 hunks FAILED -- saving rejects to file sage/rings/arith.py.rej\npatching file sage/rings/integer.pyx\nHunk #1 FAILED at 3139\n1 out of 1 hunks FAILED -- saving rejects to file sage/rings/integer.pyx.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2011-01-10T14:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46929",
    "user": "https://github.com/a-andre"
}
```

I tried to apply your patch to 4.6.1 rc1

```
applying /scratch/sage-4.6.1rc1/trac_5945bp.patch
patching file sage/rings/arith.py
Hunk #2 FAILED at 2290
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/arith.py.rej
patching file sage/rings/integer.pyx
Hunk #1 FAILED at 3139
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/integer.pyx.rej
abort: patch failed to apply
```




---

archive/issue_comments_046930.json:
```json
{
    "body": "Hi Andre,\n\nYes, that was an unfortunate case of Tom and I uploading the patch last night before combining it with another patch it relied on.  I have now uploaded a file ``trac_5945.patch``, which should combine everything and is to be applied on top of #10211.\n\nSebastian",
    "created_at": "2011-01-10T18:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46930",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Hi Andre,

Yes, that was an unfortunate case of Tom and I uploading the patch last night before combining it with another patch it relied on.  I have now uploaded a file ``trac_5945.patch``, which should combine everything and is to be applied on top of #10211.

Sebastian



---

archive/issue_comments_046931.json:
```json
{
    "body": "Just in case this wasn't obvious, ``trac_5945.patch`` applies to 4.6 and ``trac_5945_461rc0.patch`` applies to 4.6.1.rc0.  Both of these depend on #10211.\n\nSebastian",
    "created_at": "2011-01-10T19:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46931",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Just in case this wasn't obvious, ``trac_5945.patch`` applies to 4.6 and ``trac_5945_461rc0.patch`` applies to 4.6.1.rc0.  Both of these depend on #10211.

Sebastian



---

archive/issue_comments_046932.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-11T00:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46932",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_046933.json:
```json
{
    "body": "After some cleaning up, there is now a single patch ``trac_5945.patch`` that can be applied against 4.6.1.rc0 with #10211.\n\nMorally speaking, this should be good to go.  However, sage.math.washington is currently under heavy use by Jeroen and I'll wait until tomorrow before running the complete test suite.\n\nBest wishes,\nSebastian",
    "created_at": "2011-01-11T07:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46933",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

After some cleaning up, there is now a single patch ``trac_5945.patch`` that can be applied against 4.6.1.rc0 with #10211.

Morally speaking, this should be good to go.  However, sage.math.washington is currently under heavy use by Jeroen and I'll wait until tomorrow before running the complete test suite.

Best wishes,
Sebastian



---

archive/issue_comments_046934.json:
```json
{
    "body": "You should use the variable `flint_depends` in **module_list.py** and\n\n```\nSAGE_LOCAL+'include/FLINT/'\n```\n\nor\n\n```\nSAGE_INC+'FLINT/'\n```\n\ninstead of\n\n```\nSAGE_ROOT+'/local/include/FLINT/'\n```\n\n\n**arith.py**:\nremove\n\n```\nif proof is None:\n    proof = True\n```\n\nand let `n.factor` handle `proof=None`.\n\n**integer.pyx**: I suggest using the global default for *proof* in factor()\n\nChange\n\n```\nF = [(Integer(f.p[i]), f.exp[i]) for i from 0 <= i < f.num]\n```\n\nto\n\n```\nF = [(Integer(f.p[i]), int(f.exp[i])) for i from 0 <= i < f.num]\n```\n\nthen only following doctests fail (otherwise even more would fail, e.g. arith.py):\n\n```\nsage/misc/sageinspect.py\nsage/structure/factorization.py\n```\n",
    "created_at": "2011-01-11T12:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46934",
    "user": "https://github.com/a-andre"
}
```

You should use the variable `flint_depends` in **module_list.py** and

```
SAGE_LOCAL+'include/FLINT/'
```

or

```
SAGE_INC+'FLINT/'
```

instead of

```
SAGE_ROOT+'/local/include/FLINT/'
```


**arith.py**:
remove

```
if proof is None:
    proof = True
```

and let `n.factor` handle `proof=None`.

**integer.pyx**: I suggest using the global default for *proof* in factor()

Change

```
F = [(Integer(f.p[i]), f.exp[i]) for i from 0 <= i < f.num]
```

to

```
F = [(Integer(f.p[i]), int(f.exp[i])) for i from 0 <= i < f.num]
```

then only following doctests fail (otherwise even more would fail, e.g. arith.py):

```
sage/misc/sageinspect.py
sage/structure/factorization.py
```




---

archive/issue_comments_046935.json:
```json
{
    "body": "Hi Andre,\n\nThank you for the quick comments.  All of these are very sensible!  The only one I am not quite sure about is the last, where I thought the underlying FLINT structure already had f.exp[i] of the right type to that calling int(-) on it would not be necessary, but I might be wrong.\n\n(I'm not quite sure which time zone you are working in right now, so this comment might be more for Tom.)  I'm off to the gym now, but I'll have fixed this in time for lunch,\n\nSebastian",
    "created_at": "2011-01-11T16:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46935",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Hi Andre,

Thank you for the quick comments.  All of these are very sensible!  The only one I am not quite sure about is the last, where I thought the underlying FLINT structure already had f.exp[i] of the right type to that calling int(-) on it would not be necessary, but I might be wrong.

(I'm not quite sure which time zone you are working in right now, so this comment might be more for Tom.)  I'm off to the gym now, but I'll have fixed this in time for lunch,

Sebastian



---

archive/issue_comments_046936.json:
```json
{
    "body": "Attachment [trac_5945.2.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945.2.patch) by spancratz created at 2011-01-12 04:15:17\n\nI'm sorry for adding the duplicate file ``trac_5945.2.patch``, this can be deleted from here.  The other file ``trac_5945.patch`` should now apply cleanly to 4.6.1.rc0 and pass all tests.\n\nSebastian",
    "created_at": "2011-01-12T04:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46936",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac_5945.2.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945.2.patch) by spancratz created at 2011-01-12 04:15:17

I'm sorry for adding the duplicate file ``trac_5945.2.patch``, this can be deleted from here.  The other file ``trac_5945.patch`` should now apply cleanly to 4.6.1.rc0 and pass all tests.

Sebastian



---

archive/issue_comments_046937.json:
```json
{
    "body": "trac_5945.patch seems to be incomplete, e.g. `class IntegerFactorization(Factorization)` and comment changes are missing, thus I couldn't finish review.\n\nAnyway.\n\n*arith.py*:\nMaybe you should also pass `**kwds` to n.factor() if n is Integer, int or long, so `limit` can be used: `factor(8*49,limit=5)`",
    "created_at": "2011-01-12T13:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46937",
    "user": "https://github.com/a-andre"
}
```

trac_5945.patch seems to be incomplete, e.g. `class IntegerFactorization(Factorization)` and comment changes are missing, thus I couldn't finish review.

Anyway.

*arith.py*:
Maybe you should also pass `**kwds` to n.factor() if n is Integer, int or long, so `limit` can be used: `factor(8*49,limit=5)`



---

archive/issue_comments_046938.json:
```json
{
    "body": "Can you also fix #10602 for Integer.factor(). I only mention this because it's fixed in none of the last two patches.",
    "created_at": "2011-01-12T17:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46938",
    "user": "https://github.com/a-andre"
}
```

Can you also fix #10602 for Integer.factor(). I only mention this because it's fixed in none of the last two patches.



---

archive/issue_comments_046939.json:
```json
{
    "body": "Attachment [trac_5945.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945.patch) by spancratz created at 2011-01-12 19:25:10\n\nVersion for 4.6.0",
    "created_at": "2011-01-12T19:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46939",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac_5945.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945.patch) by spancratz created at 2011-01-12 19:25:10

Version for 4.6.0



---

archive/issue_comments_046940.json:
```json
{
    "body": "Attachment [trac_5945-461rc0.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945-461rc0.patch) by spancratz created at 2011-01-12 19:57:28\n\nVersion for 4.6.1.rc0",
    "created_at": "2011-01-12T19:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46940",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac_5945-461rc0.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945-461rc0.patch) by spancratz created at 2011-01-12 19:57:28

Version for 4.6.1.rc0



---

archive/issue_comments_046941.json:
```json
{
    "body": "Fix for a remaining doctest failure in sageinspect.py",
    "created_at": "2011-01-12T20:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46941",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Fix for a remaining doctest failure in sageinspect.py



---

archive/issue_comments_046942.json:
```json
{
    "body": "Attachment [trac_5945_fix.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945_fix.patch) by spancratz created at 2011-01-12 20:24:35\n\nHi Andre,\n\nI'm sorry for the earlier patch not including the IntegerFactorization class, I don't know how that happened.  Now, there are three things to do:\n\n- Apply #10211\n- Apply either trac_5945.patch or trac_5945-461rc0.patch, depending on the Sage version\n- Apply trac_5945_fix.patch\n\nTom, could you perhaps clean up this ticket and remove all other files that I or we added?\n\nSebastian",
    "created_at": "2011-01-12T20:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46942",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac_5945_fix.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945_fix.patch) by spancratz created at 2011-01-12 20:24:35

Hi Andre,

I'm sorry for the earlier patch not including the IntegerFactorization class, I don't know how that happened.  Now, there are three things to do:

- Apply #10211
- Apply either trac_5945.patch or trac_5945-461rc0.patch, depending on the Sage version
- Apply trac_5945_fix.patch

Tom, could you perhaps clean up this ticket and remove all other files that I or we added?

Sebastian



---

archive/issue_comments_046943.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-13T11:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46943",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_046944.json:
```json
{
    "body": "Attachment [trac_5945_reviewer.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945_reviewer.patch) by @a-andre created at 2011-01-13 11:13:46\n\nApply trac_5945_reviewer.patch after trac_5945_fix.patch\n\nVersion rc0 reviewed.\n\nAttached trac_5945_reviewer.patch handles doctest failure in *factorization.py*. I only changed the expected result but actually it should be a new test with old result.\n\n*sage/libs/flint/long_extras.pxd* contained `ctypedef struct factor_t:`... twice so I removed one.\n\nEverything else is okay.",
    "created_at": "2011-01-13T11:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46944",
    "user": "https://github.com/a-andre"
}
```

Attachment [trac_5945_reviewer.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945_reviewer.patch) by @a-andre created at 2011-01-13 11:13:46

Apply trac_5945_reviewer.patch after trac_5945_fix.patch

Version rc0 reviewed.

Attached trac_5945_reviewer.patch handles doctest failure in *factorization.py*. I only changed the expected result but actually it should be a new test with old result.

*sage/libs/flint/long_extras.pxd* contained `ctypedef struct factor_t:`... twice so I removed one.

Everything else is okay.



---

archive/issue_comments_046945.json:
```json
{
    "body": "Hi Andre,\n\nGreat, thank you for doing this!\n\nSebastian",
    "created_at": "2011-01-13T18:58:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46945",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Hi Andre,

Great, thank you for doing this!

Sebastian



---

archive/issue_comments_046946.json:
```json
{
    "body": "Attachment [trac_5945-462a0.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945-462a0.patch) by @a-andre created at 2011-01-17 13:09:57",
    "created_at": "2011-01-17T13:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46946",
    "user": "https://github.com/a-andre"
}
```

Attachment [trac_5945-462a0.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945-462a0.patch) by @a-andre created at 2011-01-17 13:09:57



---

archive/issue_comments_046947.json:
```json
{
    "body": "Merged patches into trac_5945-462a0.patch. So you only need to apply this one. Based on 4.6.2.alpha0.",
    "created_at": "2011-01-17T13:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46947",
    "user": "https://github.com/a-andre"
}
```

Merged patches into trac_5945-462a0.patch. So you only need to apply this one. Based on 4.6.2.alpha0.



---

archive/issue_comments_046948.json:
```json
{
    "body": "There are a few doctest failures:\n\n```\nThe following tests failed:\n\n        sage -t  -force_lib devel/sagenb-main/sagenb/misc/sageinspect.py # 1 doctests failed\n        sage -t  -force_lib devel/sage/doc/en/tutorial/programming.rst # 1 doctests failed\n        sage -t  -force_lib devel/sage/doc/fr/tutorial/programming.rst # 1 doctests failed\n```\n",
    "created_at": "2011-01-17T20:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46948",
    "user": "https://github.com/jdemeyer"
}
```

There are a few doctest failures:

```
The following tests failed:

        sage -t  -force_lib devel/sagenb-main/sagenb/misc/sageinspect.py # 1 doctests failed
        sage -t  -force_lib devel/sage/doc/en/tutorial/programming.rst # 1 doctests failed
        sage -t  -force_lib devel/sage/doc/fr/tutorial/programming.rst # 1 doctests failed
```




---

archive/issue_comments_046949.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-17T20:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46949",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_046950.json:
```json
{
    "body": "Attachment [trac_5945_doc_fix.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945_doc_fix.patch) by @a-andre created at 2011-01-18 09:27:49",
    "created_at": "2011-01-18T09:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46950",
    "user": "https://github.com/a-andre"
}
```

Attachment [trac_5945_doc_fix.patch](tarball://root/attachments/some-uuid/ticket5945/trac_5945_doc_fix.patch) by @a-andre created at 2011-01-18 09:27:49



---

archive/issue_comments_046951.json:
```json
{
    "body": "Apply trac_5945_sagenb.patch and trac_5945_doc_fix.patch after trac_5945-462a0.patch",
    "created_at": "2011-01-18T09:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46951",
    "user": "https://github.com/a-andre"
}
```

Apply trac_5945_sagenb.patch and trac_5945_doc_fix.patch after trac_5945-462a0.patch



---

archive/issue_comments_046952.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-18T09:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46952",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_046953.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-19T01:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46953",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_046954.json:
```json
{
    "body": "Doctests are fixed.",
    "created_at": "2011-01-19T01:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46954",
    "user": "https://github.com/jdemeyer"
}
```

Doctests are fixed.



---

archive/issue_comments_046955.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5945#issuecomment-46955",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
