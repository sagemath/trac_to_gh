# Issue 389: bug in mpfi C library

archive/issues_000389.json:
```json
{
    "body": "Assignee: somebody\n\nThere is a bug in the mpfi C library for interval arithmetic, which leads to an infinite loop in SAGE:\n\n\n```\nwonder if there is something wrong with the interval cosine\ncalculation?  cos seems to loop forever on [-1 .. +1].  Try this:\n\nsage: x = RealInterval(-1.1,1.1)\nsage: x.cos()\n[0.453596121425577307 .. 1.00000000000000000]\nsage: x = RealInterval(-1.0,1.0)\nsage: x.cos()\n---------------------------------------------------------------------------\n<type 'exceptions.KeyboardInterrupt'>     Traceback (most recent call\nlast)\n\n/files/home/nholtz/<ipython console> in <module>()\n\n------\n\n\n\nJust as a followup, in case anyone cares ...\n\nThe problem is definitely in libmpfi, as I can duplicate\nthe infinite loop problem in computing mpfi_cos([-1.0,1.0]) in C.\n\nI have notified the maintainers of libmpfi, and we'll see what\nhappens.\n\nneal\n\nOn Jun 19, 11:16 am, neal <nho...@docuweb.ca> wrote:\n> I wonder if there is something wrong with the interval cosine\n> calculation?  cos seems to loop forever on [-1 .. +1].  Try this:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/389\n\n",
    "created_at": "2007-06-22T11:30:37Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "bug in mpfi C library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/389",
    "user": "was"
}
```
Assignee: somebody

There is a bug in the mpfi C library for interval arithmetic, which leads to an infinite loop in SAGE:


```
wonder if there is something wrong with the interval cosine
calculation?  cos seems to loop forever on [-1 .. +1].  Try this:

sage: x = RealInterval(-1.1,1.1)
sage: x.cos()
[0.453596121425577307 .. 1.00000000000000000]
sage: x = RealInterval(-1.0,1.0)
sage: x.cos()
---------------------------------------------------------------------------
<type 'exceptions.KeyboardInterrupt'>     Traceback (most recent call
last)

/files/home/nholtz/<ipython console> in <module>()

------



Just as a followup, in case anyone cares ...

The problem is definitely in libmpfi, as I can duplicate
the infinite loop problem in computing mpfi_cos([-1.0,1.0]) in C.

I have notified the maintainers of libmpfi, and we'll see what
happens.

neal

On Jun 19, 11:16 am, neal <nho...@docuweb.ca> wrote:
> I wonder if there is something wrong with the interval cosine
> calculation?  cos seems to loop forever on [-1 .. +1].  Try this:
```


Issue created by migration from https://trac.sagemath.org/ticket/389





---

archive/issue_comments_001908.json:
```json
{
    "body": "The following code reproduces the problem:\n\n```\n#include \"mpfi.h\"\n\nint main()\n{\n    mpfi_t SinX,X;\n    mpfi_init(X);\n    mpfi_init(SinX);\n    mpfr_set_si (&(X->left), -1, GMP_RNDN);\n    mpfr_set_ui (&(X->right), 1, GMP_RNDN);\n    mpfi_cos (SinX, X);\n\n}\n```\n\nA bug has been open since 2007-01-17 09:22 at the mpfi bug tracker. See \nhttp://gforge.inria.fr/tracker/index.php?func=detail&aid=1868&group_id=157&atid=709\n\nTo quote the bug report:\n> [this bug was mentioned to me by Sylvain Chevillard]\n>\n> The internal mpfi_cmp_sym_pi function loops when z=0 and y=-x\n> in mpfi-1.3.4-RC3.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-19T06:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/389#issuecomment-1908",
    "user": "mabshoff"
}
```

The following code reproduces the problem:

```
#include "mpfi.h"

int main()
{
    mpfi_t SinX,X;
    mpfi_init(X);
    mpfi_init(SinX);
    mpfr_set_si (&(X->left), -1, GMP_RNDN);
    mpfr_set_ui (&(X->right), 1, GMP_RNDN);
    mpfi_cos (SinX, X);

}
```

A bug has been open since 2007-01-17 09:22 at the mpfi bug tracker. See 
http://gforge.inria.fr/tracker/index.php?func=detail&aid=1868&group_id=157&atid=709

To quote the bug report:
> [this bug was mentioned to me by Sylvain Chevillard]
>
> The internal mpfi_cmp_sym_pi function loops when z=0 and y=-x
> in mpfi-1.3.4-RC3.

Cheers,

Michael



---

archive/issue_comments_001909.json:
```json
{
    "body": "Attachment [389.patch](tarball://root/attachments/some-uuid/ticket389/389.patch) by cwitty created at 2007-11-02 06:02:33\n\nThere is a new MPFI spkg at http://sage.math.washington.edu/home/cwitty/mpfi-1.3.4-rc3.p9.spkg that fixes this (it also includes a minor fix from Paul Zimmerman, for mpfi_ui_sub()).\n\nThe attached patch adds a doctest for the new package.  With the old spkg, the doctest will loop forever; with the new spkg, it works.",
    "created_at": "2007-11-02T06:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/389#issuecomment-1909",
    "user": "cwitty"
}
```

Attachment [389.patch](tarball://root/attachments/some-uuid/ticket389/389.patch) by cwitty created at 2007-11-02 06:02:33

There is a new MPFI spkg at http://sage.math.washington.edu/home/cwitty/mpfi-1.3.4-rc3.p9.spkg that fixes this (it also includes a minor fix from Paul Zimmerman, for mpfi_ui_sub()).

The attached patch adds a doctest for the new package.  With the old spkg, the doctest will loop forever; with the new spkg, it works.



---

archive/issue_comments_001910.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-02T19:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/389#issuecomment-1910",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_001911.json:
```json
{
    "body": "applied to 2.8.11.rc2, spkg updated.",
    "created_at": "2007-11-02T19:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/389#issuecomment-1911",
    "user": "mabshoff"
}
```

applied to 2.8.11.rc2, spkg updated.
