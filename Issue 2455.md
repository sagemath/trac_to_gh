# Issue 2455: [with patch, needs review] improve documentation for multivariate polynomial ideals

archive/issues_002455.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @ncalexan\n\nAfter the patch was applied:\n\n\n```\nSCORE devel/sage-docday2/sage/rings/polynomial/multi_polynomial_ideal.py: 88% (40 of 45)\n\nMissing doctests:\n         * redSB(func)\n         * wrapper(*args, **kwds)\n         * _variety(T, V, v=None)\n         * _macaulay2_(self, macaulay2=None)\n         * groebner_fan(self, is_groebner_basis=False, symmetry=None, verbose=False)\n```\n\n\nI cannot write Macaulay2 doctests right now because the optional SPKG fails to install. Groebner fan also has issues.\n\nOld:\n\n```\n----------------------------------------------------------------------\ndevel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py\nSCORE devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py: 68% (32 of 47)\n\nMissing documentation:\n         * is_MPolynomialIdeal(x)\n         * __enter__(self)\n         * __exit__(self, type, value, tb)\n         * wrapper(*args, **kwds)\n         * f(x,y)\n         * _singular_groebner_basis(self)\n         * _variety(T, V, v=None)\n\n\nMissing doctests:\n         * __init__(self, singular=singular_default)\n         * redSB(func)\n         * dimension(self)\n         * genus(self)\n         * syzygy_module(self)\n         * reduced_basis(self)\n         * _macaulay2_(self, macaulay2=None)\n         * groebner_fan(self, is_groebner_basis=False, symmetry=None, verbose=False)\n\n\nPossibly wrong (function name doesn't occur in doctests):\n         * _magma_groebner_basis(self)\n         * _contains_(self, f)\n         * _macaulay2_groebner_basis(self)\n\n----------------------------------------------------------------------\n```\n\n\nThis patch does not increase the number of doctests very much but focuses on the quality of the doctests and documentation.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2455\n\n",
    "created_at": "2008-03-10T12:07:54Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, needs review] improve documentation for multivariate polynomial ideals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2455",
    "user": "https://github.com/malb"
}
```
Assignee: tba

CC:  @ncalexan

After the patch was applied:


```
SCORE devel/sage-docday2/sage/rings/polynomial/multi_polynomial_ideal.py: 88% (40 of 45)

Missing doctests:
         * redSB(func)
         * wrapper(*args, **kwds)
         * _variety(T, V, v=None)
         * _macaulay2_(self, macaulay2=None)
         * groebner_fan(self, is_groebner_basis=False, symmetry=None, verbose=False)
```


I cannot write Macaulay2 doctests right now because the optional SPKG fails to install. Groebner fan also has issues.

Old:

```
----------------------------------------------------------------------
devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py
SCORE devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py: 68% (32 of 47)

Missing documentation:
         * is_MPolynomialIdeal(x)
         * __enter__(self)
         * __exit__(self, type, value, tb)
         * wrapper(*args, **kwds)
         * f(x,y)
         * _singular_groebner_basis(self)
         * _variety(T, V, v=None)


Missing doctests:
         * __init__(self, singular=singular_default)
         * redSB(func)
         * dimension(self)
         * genus(self)
         * syzygy_module(self)
         * reduced_basis(self)
         * _macaulay2_(self, macaulay2=None)
         * groebner_fan(self, is_groebner_basis=False, symmetry=None, verbose=False)


Possibly wrong (function name doesn't occur in doctests):
         * _magma_groebner_basis(self)
         * _contains_(self, f)
         * _macaulay2_groebner_basis(self)

----------------------------------------------------------------------
```


This patch does not increase the number of doctests very much but focuses on the quality of the doctests and documentation.


Issue created by migration from https://trac.sagemath.org/ticket/2455





---

archive/issue_comments_016582.json:
```json
{
    "body": "Attachment [mpoly-ideal-docday.patch](tarball://root/attachments/some-uuid/ticket2455/mpoly-ideal-docday.patch) by @malb created at 2008-03-10 12:08:11\n\napply against code repository",
    "created_at": "2008-03-10T12:08:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2455#issuecomment-16582",
    "user": "https://github.com/malb"
}
```

Attachment [mpoly-ideal-docday.patch](tarball://root/attachments/some-uuid/ticket2455/mpoly-ideal-docday.patch) by @malb created at 2008-03-10 12:08:11

apply against code repository



---

archive/issue_comments_016583.json:
```json
{
    "body": "this patch adds a doctest for the groebner_fan method",
    "created_at": "2008-03-12T16:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2455#issuecomment-16583",
    "user": "https://github.com/malb"
}
```

this patch adds a doctest for the groebner_fan method



---

archive/issue_comments_016584.json:
```json
{
    "body": "Changing assignee from tba to @malb.",
    "created_at": "2008-03-12T16:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2455#issuecomment-16584",
    "user": "https://github.com/malb"
}
```

Changing assignee from tba to @malb.



---

archive/issue_comments_016585.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-12T16:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2455#issuecomment-16585",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016586.json:
```json
{
    "body": "Attachment [mpoly-ideal-gfan.patch](tarball://root/attachments/some-uuid/ticket2455/mpoly-ideal-gfan.patch) by @malb created at 2008-03-12 16:53:03",
    "created_at": "2008-03-12T16:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2455#issuecomment-16586",
    "user": "https://github.com/malb"
}
```

Attachment [mpoly-ideal-gfan.patch](tarball://root/attachments/some-uuid/ticket2455/mpoly-ideal-gfan.patch) by @malb created at 2008-03-12 16:53:03



---

archive/issue_comments_016587.json:
```json
{
    "body": "This looks good to me, with one major exception: all the Groebner's were changed to \"Gr\u00c3\u00b6bner\" and it doesn't display correctly for me.  I think we should stick to standard transliteration or latex.\n\nI say apply after fixing that Groebner business.",
    "created_at": "2008-03-12T17:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2455#issuecomment-16587",
    "user": "https://github.com/ncalexan"
}
```

This looks good to me, with one major exception: all the Groebner's were changed to "GrÃ¶bner" and it doesn't display correctly for me.  I think we should stick to standard transliteration or latex.

I say apply after fixing that Groebner business.



---

archive/issue_comments_016588.json:
```json
{
    "body": "Replying to [comment:3 ncalexan]:\n> This looks good to me, with one major exception: all the Groebner's were changed to \"Gr\u00c3\u00b6bner\" and it doesn't display correctly for me.  I think we should stick to standard transliteration or latex.\n\nThis is a Trac issue. It prints correctly (as \"Gr\u00f6bner\") in my shell, in the reference manual PDF and in the Sage notebook.",
    "created_at": "2008-03-12T18:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2455#issuecomment-16588",
    "user": "https://github.com/malb"
}
```

Replying to [comment:3 ncalexan]:
> This looks good to me, with one major exception: all the Groebner's were changed to "GrÃ¶bner" and it doesn't display correctly for me.  I think we should stick to standard transliteration or latex.

This is a Trac issue. It prints correctly (as "Gröbner") in my shell, in the reference manual PDF and in the Sage notebook.



---

archive/issue_comments_016589.json:
```json
{
    "body": "I downloaded the patch and it displays wrong in my emacs and in my shell.",
    "created_at": "2008-03-12T18:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2455#issuecomment-16589",
    "user": "https://github.com/ncalexan"
}
```

I downloaded the patch and it displays wrong in my emacs and in my shell.



---

archive/issue_comments_016590.json:
```json
{
    "body": "this is the UTF-8 free version of the earlier patch",
    "created_at": "2008-03-12T18:40:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2455#issuecomment-16590",
    "user": "https://github.com/malb"
}
```

this is the UTF-8 free version of the earlier patch



---

archive/issue_comments_016591.json:
```json
{
    "body": "Attachment [mpoly-ideal-docday-wo-utf8.patch](tarball://root/attachments/some-uuid/ticket2455/mpoly-ideal-docday-wo-utf8.patch) by @malb created at 2008-03-12 18:42:36\n\nI've uploaded an UTF-8 free version of the patch. Unfortunately, the time doesn't seem right for Umlauts in Python yet. \"Umlauts \u00fcber alles\" postponed, I reckon.",
    "created_at": "2008-03-12T18:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2455#issuecomment-16591",
    "user": "https://github.com/malb"
}
```

Attachment [mpoly-ideal-docday-wo-utf8.patch](tarball://root/attachments/some-uuid/ticket2455/mpoly-ideal-docday-wo-utf8.patch) by @malb created at 2008-03-12 18:42:36

I've uploaded an UTF-8 free version of the patch. Unfortunately, the time doesn't seem right for Umlauts in Python yet. "Umlauts über alles" postponed, I reckon.



---

archive/issue_comments_016592.json:
```json
{
    "body": "Good stuff.  I applied mpoly-ideal-docday-wo-utf8.patch against sage-2.10.3, everything seems fine.  Then I applied \nmpoly-ideal-gfan.patch, and it's also good.  All doctests in sage/rings pass.",
    "created_at": "2008-03-15T18:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2455#issuecomment-16592",
    "user": "https://github.com/aghitza"
}
```

Good stuff.  I applied mpoly-ideal-docday-wo-utf8.patch against sage-2.10.3, everything seems fine.  Then I applied 
mpoly-ideal-gfan.patch, and it's also good.  All doctests in sage/rings pass.



---

archive/issue_comments_016593.json:
```json
{
    "body": "Merged mpoly-ideal-docday-wo-utf8.patch and mpoly-ideal-gfan.patch in Sage 2.10.4.rc0",
    "created_at": "2008-03-15T19:23:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2455#issuecomment-16593",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged mpoly-ideal-docday-wo-utf8.patch and mpoly-ideal-gfan.patch in Sage 2.10.4.rc0



---

archive/issue_comments_016594.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-15T19:23:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2455#issuecomment-16594",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
