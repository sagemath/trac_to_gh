# Issue 2204: Integrate Karim Belabas's HNF bug fix for pari

archive/issues_002204.json:
```json
{
    "body": "Assignee: mabshoff\n\nReported by William via the pari bug tracker:\n\n```\n---------- Forwarded message ----------\nFrom: Karim Belabas <Karim.Belabas@math.u-bordeaux1.fr>\nDate: Feb 18, 2008 2:49 AM\nSubject: Re: Bug#741: Fwd: bug in PARI's mathnf function\nTo: William Stein <wstein@gmail.com>, 741-close@pari.math.u-bordeaux.fr\n\n\n* William Stein [2008-02-16 23:47]:\n> > Package: pari\n> > Version: 2.3.3\n[...]\n> > PARI sometimes puts negative numbers in the *output* of mathnf(a, 1)[0],\n> > which is a bug.\n\nIndeed.\n\n> >   * I didn't use mathnf(b) directly (the default option), since\n> > already for a 20x18 matrix it\n> > is too slow to be useful.\n\nAs documented.\n\n[ Actually, I am going to change this: I don't see the point in defaulting\nto a slow routine; let mathnf choose depending on the matrix size.\nIt should either call matdetint + mathnfmod, or mathnf(,1) ]\n\n> >   * I'm guessing maybe mathnf(b, 1) uses the modular hnf modulo the\n> >   determinant.\n\nActually, no; mathnfmod does that.\n\n> > If not, maybe you just need to add mutliples of rows until everything\n> > is correctly normalized.\n\nWe do that, with one optimization too many which sometimes cancelled the\nnormalization step ( when the kernel is non trivial and we are \"lucky\":\na coefficient which we want to set to 0 is already 0 ).\n\nIt is fixed in both stable and unstable branches. I am attaching the\n(trivial) patch.\n\nThanks for your report !\n\n    K.B.\n--\nKarim Belabas                  Tel: (+33) (0)5 40 00 26 17\nIMB, Universite Bordeaux 1     Fax: (+33) (0)5 40 00 69 50\n351, cours de la Liberation    http://www.math.u-bordeaux.fr/~belabas/\nF-33405 Talence (France)       http://pari.math.u-bordeaux.fr/  [PARI/GP]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2204\n\n",
    "created_at": "2008-02-18T18:09:16Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "Integrate Karim Belabas's HNF bug fix for pari",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2204",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Reported by William via the pari bug tracker:

```
---------- Forwarded message ----------
From: Karim Belabas <Karim.Belabas@math.u-bordeaux1.fr>
Date: Feb 18, 2008 2:49 AM
Subject: Re: Bug#741: Fwd: bug in PARI's mathnf function
To: William Stein <wstein@gmail.com>, 741-close@pari.math.u-bordeaux.fr


* William Stein [2008-02-16 23:47]:
> > Package: pari
> > Version: 2.3.3
[...]
> > PARI sometimes puts negative numbers in the *output* of mathnf(a, 1)[0],
> > which is a bug.

Indeed.

> >   * I didn't use mathnf(b) directly (the default option), since
> > already for a 20x18 matrix it
> > is too slow to be useful.

As documented.

[ Actually, I am going to change this: I don't see the point in defaulting
to a slow routine; let mathnf choose depending on the matrix size.
It should either call matdetint + mathnfmod, or mathnf(,1) ]

> >   * I'm guessing maybe mathnf(b, 1) uses the modular hnf modulo the
> >   determinant.

Actually, no; mathnfmod does that.

> > If not, maybe you just need to add mutliples of rows until everything
> > is correctly normalized.

We do that, with one optimization too many which sometimes cancelled the
normalization step ( when the kernel is non trivial and we are "lucky":
a coefficient which we want to set to 0 is already 0 ).

It is fixed in both stable and unstable branches. I am attaching the
(trivial) patch.

Thanks for your report !

    K.B.
--
Karim Belabas                  Tel: (+33) (0)5 40 00 26 17
IMB, Universite Bordeaux 1     Fax: (+33) (0)5 40 00 69 50
351, cours de la Liberation    http://www.math.u-bordeaux.fr/~belabas/
F-33405 Talence (France)       http://pari.math.u-bordeaux.fr/  [PARI/GP]
```


Issue created by migration from https://trac.sagemath.org/ticket/2204





---

archive/issue_comments_014506.json:
```json
{
    "body": "Attachment [hnf.patch](tarball://root/attachments/some-uuid/ticket2204/hnf.patch) by mabshoff created at 2008-02-18 18:12:14\n\nThis patch needs to be applied to the pari.spkg",
    "created_at": "2008-02-18T18:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2204#issuecomment-14506",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [hnf.patch](tarball://root/attachments/some-uuid/ticket2204/hnf.patch) by mabshoff created at 2008-02-18 18:12:14

This patch needs to be applied to the pari.spkg



---

archive/issue_comments_014507.json:
```json
{
    "body": "The updated spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha1/pari-2.3.3.p0.spkg\n\ncontains the patch, adds support for 64 bit OSX. Builds fine on Linux and OSX.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-18T18:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2204#issuecomment-14507",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The updated spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha1/pari-2.3.3.p0.spkg

contains the patch, adds support for 64 bit OSX. Builds fine on Linux and OSX.

Cheers,

Michael



---

archive/issue_comments_014508.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-18T18:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2204#issuecomment-14508",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014509.json:
```json
{
    "body": "apply this patch to the sage hg repo; it adds a test to matrix/tests.py to ensure that the bug is (and stays) fixed.",
    "created_at": "2008-02-18T18:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2204#issuecomment-14509",
    "user": "https://github.com/williamstein"
}
```

apply this patch to the sage hg repo; it adds a test to matrix/tests.py to ensure that the bug is (and stays) fixed.



---

archive/issue_comments_014510.json:
```json
{
    "body": "Attachment [trac-2204.patch](tarball://root/attachments/some-uuid/ticket2204/trac-2204.patch) by mabshoff created at 2008-02-18 19:03:05\n\ntrac-2204.patch looks good to me. With it applied and the new pari.spkg doctests in `sage/matrix/tests.py` pass, so positive review (also from was for the spkg).\n\nCheers,\n\nMichael",
    "created_at": "2008-02-18T19:03:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2204#issuecomment-14510",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-2204.patch](tarball://root/attachments/some-uuid/ticket2204/trac-2204.patch) by mabshoff created at 2008-02-18 19:03:05

trac-2204.patch looks good to me. With it applied and the new pari.spkg doctests in `sage/matrix/tests.py` pass, so positive review (also from was for the spkg).

Cheers,

Michael



---

archive/issue_comments_014511.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-18T19:05:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2204#issuecomment-14511",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014512.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-18T19:05:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2204#issuecomment-14512",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1



---

archive/issue_events_002370.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-18T19:05:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2204",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2204#event-2370"
}
```
