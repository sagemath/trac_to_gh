# Issue 388: bug in modular symbol projection function

archive/issues_000388.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nOn 6/21/07, Mak Trifkovic <mak@math.uvic.ca> wrote:\n> Hi William,\n>\n> I found an odd thing:\n> -----------------------\n> S=ModularSymbols(53,sign=1).cuspidal_subspace()[1];S\n>\n>         Modular Symbols subspace of dimension 3 of Modular Symbols space of\n>         dimension 5 for Gamma_0(53) of weight 2 with sign 1 over Rational Field\n>\n> p=S.projection()\n>\n>\n> S.basis()\n>\n>         ((1,33) - (1,37), (1,35), (1,49))\n>\n> for i in [0,1,2]: p(S.basis()[i])\n>\n>\n> (1,35)\n> (1,49)\n> 0\n> ------------------------------\n> Shouldn't the projection onto a subspace restricted to that subspace be\n> the identity?\n\nYes.  That's definitely a bug.  Thanks for finding it.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/388\n\n",
    "created_at": "2007-06-22T11:25:44Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "bug in modular symbol projection function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/388",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
On 6/21/07, Mak Trifkovic <mak@math.uvic.ca> wrote:
> Hi William,
>
> I found an odd thing:
> -----------------------
> S=ModularSymbols(53,sign=1).cuspidal_subspace()[1];S
>
>         Modular Symbols subspace of dimension 3 of Modular Symbols space of
>         dimension 5 for Gamma_0(53) of weight 2 with sign 1 over Rational Field
>
> p=S.projection()
>
>
> S.basis()
>
>         ((1,33) - (1,37), (1,35), (1,49))
>
> for i in [0,1,2]: p(S.basis()[i])
>
>
> (1,35)
> (1,49)
> 0
> ------------------------------
> Shouldn't the projection onto a subspace restricted to that subspace be
> the identity?

Yes.  That's definitely a bug.  Thanks for finding it.
```


Issue created by migration from https://trac.sagemath.org/ticket/388





---

archive/issue_comments_001895.json:
```json
{
    "body": "This is still an issue with Sage 2.8.2. Maybe it is something for the next bug day:\n\n```\n[mabshoff@m940 sage-2.8.2]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.2, Release Date: 2007-08-22                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: S=ModularSymbols(53,sign=1).cuspidal_subspace()[1];S\nModular Symbols subspace of dimension 3 of Modular Symbols space of dimension 5 for Gamma_0(53) of weight 2 with sign 1 over Rational Field\nsage: p=S.projection()\nsage: S.basis()\n((1,33) - (1,37), (1,35), (1,49))\nsage: for i in [0,1,2]: p(S.basis()[i])\n....:\n(1,35)\n(1,49)\n0\nsage:\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-08-28T11:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/388#issuecomment-1895",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is still an issue with Sage 2.8.2. Maybe it is something for the next bug day:

```
[mabshoff@m940 sage-2.8.2]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.2, Release Date: 2007-08-22                       |
| Type notebook() for the GUI, and license() for information.        |
sage: S=ModularSymbols(53,sign=1).cuspidal_subspace()[1];S
Modular Symbols subspace of dimension 3 of Modular Symbols space of dimension 5 for Gamma_0(53) of weight 2 with sign 1 over Rational Field
sage: p=S.projection()
sage: S.basis()
((1,33) - (1,37), (1,35), (1,49))
sage: for i in [0,1,2]: p(S.basis()[i])
....:
(1,35)
(1,49)
0
sage:
```

Cheers,

Michael



---

archive/issue_comments_001896.json:
```json
{
    "body": "This fixes the bug above. The problem was this: if M is the full space of modular symbols above, SS its cuspidal subspace, and S as above, then S is the 3rd component in the decomposition of M, but the second in the decomposition of SS. At some point, this led to an indexing problem, and the wrong rows of M.decomposition_matrix() were being used to create S.projection.\n\nI fixed this as follows: since M has already been decomposed to get S, I simply use (M.decomposition()).index(S) to find out what the appropriate index is. I could be convinced that there's a more elegant way to do this.\n\nI'm attaching the patch, but it's also available here:\n\nhttp://sage.math.washington.edu/home/citro/patches/ticket_388.hg\n\n-cc",
    "created_at": "2007-09-01T07:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/388#issuecomment-1896",
    "user": "https://github.com/craigcitro"
}
```

This fixes the bug above. The problem was this: if M is the full space of modular symbols above, SS its cuspidal subspace, and S as above, then S is the 3rd component in the decomposition of M, but the second in the decomposition of SS. At some point, this led to an indexing problem, and the wrong rows of M.decomposition_matrix() were being used to create S.projection.

I fixed this as follows: since M has already been decomposed to get S, I simply use (M.decomposition()).index(S) to find out what the appropriate index is. I could be convinced that there's a more elegant way to do this.

I'm attaching the patch, but it's also available here:

http://sage.math.washington.edu/home/citro/patches/ticket_388.hg

-cc



---

archive/issue_comments_001897.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2007-09-01T07:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/388#issuecomment-1897",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_001898.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-01T18:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/388#issuecomment-1898",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_001899.json:
```json
{
    "body": "Attachment [ticket_388.hg](tarball://root/attachments/some-uuid/ticket388/ticket_388.hg) by @williamstein created at 2007-09-01 18:12:07\n\nlooks good to me.",
    "created_at": "2007-09-01T18:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/388#issuecomment-1899",
    "user": "https://github.com/williamstein"
}
```

Attachment [ticket_388.hg](tarball://root/attachments/some-uuid/ticket388/ticket_388.hg) by @williamstein created at 2007-09-01 18:12:07

looks good to me.



---

archive/issue_events_000410.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-09-01T18:12:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/388",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/388#event-410"
}
```
