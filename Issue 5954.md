# Issue 5954: Added documentation/doctests for all quadratic form genus symbol routines

archive/issues_005954.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  tornaria mabshoff wstein cremona\n\nKeywords: QuadraticForm\n\nThis patch documents and brings doctest coverage to 100% for all routines in:\n\n```\nquadratic_forms/quadratic_form__genus.py\nquadratic_forms/genera/genus.py\n```\n\n\nIt also rewrote a few signature routines and the rational_diagonal_form() routine which was causing the bug reported in Ticket #5837:\n\n```\nsage: Q2=QuadraticForm(ZZ,3,[ -3,2,0 , 3,-2 , 5 ])\nsage: Q2.rational_diagonal_form()\n\nQuadratic form in 3 variables over Rational Field with coefficients: \n[ -3 0 0 ]\n[ * 10/3 0 ]\n[ * * 47/10 ]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5954\n\n",
    "created_at": "2009-05-01T05:59:31Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Added documentation/doctests for all quadratic form genus symbol routines",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5954",
    "user": "jonhanke"
}
```
Assignee: tbd

CC:  tornaria mabshoff wstein cremona

Keywords: QuadraticForm

This patch documents and brings doctest coverage to 100% for all routines in:

```
quadratic_forms/quadratic_form__genus.py
quadratic_forms/genera/genus.py
```


It also rewrote a few signature routines and the rational_diagonal_form() routine which was causing the bug reported in Ticket #5837:

```
sage: Q2=QuadraticForm(ZZ,3,[ -3,2,0 , 3,-2 , 5 ])
sage: Q2.rational_diagonal_form()

Quadratic form in 3 variables over Rational Field with coefficients: 
[ -3 0 0 ]
[ * 10/3 0 ]
[ * * 47/10 ]
```


Issue created by migration from https://trac.sagemath.org/ticket/5954





---

archive/issue_comments_047095.json:
```json
{
    "body": "Attachment [patch-1__QF_genus_symbols__3.4.1.patch](tarball://root/attachments/some-uuid/ticket5954/patch-1__QF_genus_symbols__3.4.1.patch) by jonhanke created at 2009-05-01 05:59:55",
    "created_at": "2009-05-01T05:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5954#issuecomment-47095",
    "user": "jonhanke"
}
```

Attachment [patch-1__QF_genus_symbols__3.4.1.patch](tarball://root/attachments/some-uuid/ticket5954/patch-1__QF_genus_symbols__3.4.1.patch) by jonhanke created at 2009-05-01 05:59:55



---

archive/issue_comments_047096.json:
```json
{
    "body": "I just skimmed through patch-1__QF_genus_symbols__3.4.1.patch and I'm very happy with what I'm seeing!  I did order the Repo Man movie, in case I needed lessons in how to rip out all the quadratic forms code.  It looks like I won't :-)\n\n -- William",
    "created_at": "2009-05-01T06:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5954#issuecomment-47096",
    "user": "was"
}
```

I just skimmed through patch-1__QF_genus_symbols__3.4.1.patch and I'm very happy with what I'm seeing!  I did order the Repo Man movie, in case I needed lessons in how to rip out all the quadratic forms code.  It looks like I won't :-)

 -- William



---

archive/issue_comments_047097.json:
```json
{
    "body": "Hehe, nice comment William. There is at least one typo in the docstring:\n\n```\n        doubling conventions strraight throughout!  This is especially \n```\n\nI have skimmed the rest and did not see anything obvious. The renaming could introduce some trouble, so adding deprecation messages for the old names might be a good idea. We will see what the real reviewer will say.\n\nI am CCing John also to see if he can slip it into their review schedule. John: in case you are busy feel free to ignore this. :)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-01T06:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5954#issuecomment-47097",
    "user": "mabshoff"
}
```

Hehe, nice comment William. There is at least one typo in the docstring:

```
        doubling conventions strraight throughout!  This is especially 
```

I have skimmed the rest and did not see anything obvious. The renaming could introduce some trouble, so adding deprecation messages for the old names might be a good idea. We will see what the real reviewer will say.

I am CCing John also to see if he can slip it into their review schedule. John: in case you are busy feel free to ignore this. :)

Cheers,

Michael



---

archive/issue_comments_047098.json:
```json
{
    "body": "Looks good to me. The renamings mentioned by mabshoff are:\n- `signature_of_matrix` renamed to `signature_pair_of_matrix`\n- `is_even` renamed to `is_even_matrix`\n- `trace_diag` renamed to `trace_diag_mod_8`\n- `is_trivial_symbol` removed\nOf these the first three are internal, not exported in {{{sage.quadratic_forms.all}}. The renaming aids to readability. The fourth one was actually exported, but apparently it was not clear what it does (the comment reads \"Removed because it was unused and undocumented!\"). Jon may want to add a comment about it here.\n\nOther than that, I will be giving positive review together with the whole series of QF doctest patches summarized in #6040, since coverage goes up to 100% and all doctest pass after a few trivial bugfixes.\n\nIncidentally, this patch fixes the issue in #5837, so that one should be closed as this patch gets merged.",
    "created_at": "2009-05-18T23:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5954#issuecomment-47098",
    "user": "tornaria"
}
```

Looks good to me. The renamings mentioned by mabshoff are:
- `signature_of_matrix` renamed to `signature_pair_of_matrix`
- `is_even` renamed to `is_even_matrix`
- `trace_diag` renamed to `trace_diag_mod_8`
- `is_trivial_symbol` removed
Of these the first three are internal, not exported in {{{sage.quadratic_forms.all}}. The renaming aids to readability. The fourth one was actually exported, but apparently it was not clear what it does (the comment reads "Removed because it was unused and undocumented!"). Jon may want to add a comment about it here.

Other than that, I will be giving positive review together with the whole series of QF doctest patches summarized in #6040, since coverage goes up to 100% and all doctest pass after a few trivial bugfixes.

Incidentally, this patch fixes the issue in #5837, so that one should be closed as this patch gets merged.



---

archive/issue_comments_047099.json:
```json
{
    "body": "Mark the ticket properly as Gonzalo reviewed it.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-18T23:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5954#issuecomment-47099",
    "user": "mabshoff"
}
```

Mark the ticket properly as Gonzalo reviewed it.

Cheers,

Michael



---

archive/issue_comments_047100.json:
```json
{
    "body": "I'm ok with the positive review.",
    "created_at": "2009-05-19T00:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5954#issuecomment-47100",
    "user": "tornaria"
}
```

I'm ok with the positive review.



---

archive/issue_comments_047101.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T00:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5954#issuecomment-47101",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_047102.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T00:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5954#issuecomment-47102",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_047103.json:
```json
{
    "body": "Changing component from algebra to quadratic forms.",
    "created_at": "2009-06-07T14:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5954#issuecomment-47103",
    "user": "davidloeffler"
}
```

Changing component from algebra to quadratic forms.
