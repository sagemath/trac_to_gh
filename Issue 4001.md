# Issue 4001: [with patch, needs review] ZZ['x'].gen()^(2^20) should work but doesn't

archive/issues_004001.json:
```json
{
    "body": "Assignee: somebody\n\nOn [sage-devel] Bill Hart wrote:\n\n> I don't seem to be able to create large polynomials in SAGE currently.\n> If I try to create a polynomial f(x)=x<sup>2**20</sup> where I am working in a\n>  genuine univariate polynomial ring over ZZ, it just tells me it is out\n> of memory.\n\n> It looks like a message from the memory manager from FLINT, but FLINT\n> really has no problem creating polynomials of this size. So I'm a bit\n> puzzled as to what is going on there.\n\n> Magma, by the way, can create polynomials up to length about 2<sup>28</sup> and\n> can store polynomials (as a result of a computation) up to about\n> length 2<sup>30</sup>.\n\n> I was interested in seeing if SAGE could do better than that. However,\n> not being able to create a polynomial of length 1 million seems really\n> limiting to me. Does someone know why this is?\n\nIssue created by migration from https://trac.sagemath.org/ticket/4001\n\n",
    "created_at": "2008-08-30T12:36:40Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] ZZ['x'].gen()^(2^20) should work but doesn't",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4001",
    "user": "malb"
}
```
Assignee: somebody

On [sage-devel] Bill Hart wrote:

> I don't seem to be able to create large polynomials in SAGE currently.
> If I try to create a polynomial f(x)=x<sup>2**20</sup> where I am working in a
>  genuine univariate polynomial ring over ZZ, it just tells me it is out
> of memory.

> It looks like a message from the memory manager from FLINT, but FLINT
> really has no problem creating polynomials of this size. So I'm a bit
> puzzled as to what is going on there.

> Magma, by the way, can create polynomials up to length about 2<sup>28</sup> and
> can store polynomials (as a result of a computation) up to about
> length 2<sup>30</sup>.

> I was interested in seeing if SAGE could do better than that. However,
> not being able to create a polynomial of length 1 million seems really
> limiting to me. Does someone know why this is?

Issue created by migration from https://trac.sagemath.org/ticket/4001





---

archive/issue_comments_028894.json:
```json
{
    "body": "Attachment [4001_flint_gen_power.patch](tarball://root/attachments/some-uuid/ticket4001/4001_flint_gen_power.patch) by malb created at 2008-08-30 12:37:52",
    "created_at": "2008-08-30T12:37:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4001#issuecomment-28894",
    "user": "malb"
}
```

Attachment [4001_flint_gen_power.patch](tarball://root/attachments/some-uuid/ticket4001/4001_flint_gen_power.patch) by malb created at 2008-08-30 12:37:52



---

archive/issue_comments_028895.json:
```json
{
    "body": "\n```\nsage: x^(2^20) \n1048576 \n```\n\n\nI think you have set the 1st coefficient to exp instead of the other way round!",
    "created_at": "2008-08-30T16:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4001#issuecomment-28895",
    "user": "cremona"
}
```


```
sage: x^(2^20) 
1048576 
```


I think you have set the 1st coefficient to exp instead of the other way round!



---

archive/issue_comments_028896.json:
```json
{
    "body": "Wow, I even doctested the wrong behavior. No clue, how I managed to miss that. Sorry. New patch coming up.",
    "created_at": "2008-08-30T16:18:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4001#issuecomment-28896",
    "user": "malb"
}
```

Wow, I even doctested the wrong behavior. No clue, how I managed to miss that. Sorry. New patch coming up.



---

archive/issue_comments_028897.json:
```json
{
    "body": "Attachment [4001_flint_gen_power.2.patch](tarball://root/attachments/some-uuid/ticket4001/4001_flint_gen_power.2.patch) by malb created at 2008-08-30 16:22:09\n\nActually, It was only a copy'n'paste error in the doctest, the actual implementation was fine. I was just too lazy to run the doctest afterwards, that should teach me.",
    "created_at": "2008-08-30T16:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4001#issuecomment-28897",
    "user": "malb"
}
```

Attachment [4001_flint_gen_power.2.patch](tarball://root/attachments/some-uuid/ticket4001/4001_flint_gen_power.2.patch) by malb created at 2008-08-30 16:22:09

Actually, It was only a copy'n'paste error in the doctest, the actual implementation was fine. I was just too lazy to run the doctest afterwards, that should teach me.



---

archive/issue_comments_028898.json:
```json
{
    "body": "... and to be honest I had not applied the patch, just read it!\n\nPatch applies ok to 3.1.2.alpha2, doctests in sage.rings.polynomial all pass.\n\nBy the way, `x<sup>(2</sup>25)` works ok too, but `x<sup>(2</sup>30)` causes Sage to crash:\n\n```\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\nDoes that mean that your new special code should have _sig_on, _sig_off?",
    "created_at": "2008-08-30T16:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4001#issuecomment-28898",
    "user": "cremona"
}
```

... and to be honest I had not applied the patch, just read it!

Patch applies ok to 3.1.2.alpha2, doctests in sage.rings.polynomial all pass.

By the way, `x<sup>(2</sup>25)` works ok too, but `x<sup>(2</sup>30)` causes Sage to crash:

```
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

Does that mean that your new special code should have _sig_on, _sig_off?



---

archive/issue_comments_028899.json:
```json
{
    "body": "Attachment [4001_flint_gen_power.3.patch](tarball://root/attachments/some-uuid/ticket4001/4001_flint_gen_power.3.patch) by malb created at 2008-08-30 16:49:50\n\nReplying to [comment:4 cremona]:\n> Does that mean that your new special code should have _sig_on, _sig_off?\n\nYes, I've just updated the patch. I'm not going to write a doctest for this, since it unnecessarily slows down the user's computer by filling up his/her RAM ... on a related note: Incredible in how many ways I can screw up such a short patch.",
    "created_at": "2008-08-30T16:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4001#issuecomment-28899",
    "user": "malb"
}
```

Attachment [4001_flint_gen_power.3.patch](tarball://root/attachments/some-uuid/ticket4001/4001_flint_gen_power.3.patch) by malb created at 2008-08-30 16:49:50

Replying to [comment:4 cremona]:
> Does that mean that your new special code should have _sig_on, _sig_off?

Yes, I've just updated the patch. I'm not going to write a doctest for this, since it unnecessarily slows down the user's computer by filling up his/her RAM ... on a related note: Incredible in how many ways I can screw up such a short patch.



---

archive/issue_comments_028900.json:
```json
{
    "body": "Looks good to me.  Note for mabshoff: apply *only* the last of the three patches.",
    "created_at": "2008-08-30T17:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4001#issuecomment-28900",
    "user": "cremona"
}
```

Looks good to me.  Note for mabshoff: apply *only* the last of the three patches.



---

archive/issue_comments_028901.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-30T18:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4001#issuecomment-28901",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028902.json:
```json
{
    "body": "Merged 4001_flint_gen_power.3.patch in Sage 3.1.2.alpha3",
    "created_at": "2008-08-30T18:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4001#issuecomment-28902",
    "user": "mabshoff"
}
```

Merged 4001_flint_gen_power.3.patch in Sage 3.1.2.alpha3
