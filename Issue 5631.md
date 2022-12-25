# Issue 5631: improve doctest coverage for schemes/generic/affine_space.py

archive/issues_005631.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: doctest affine space\n\nThe attached patch improves the doctest coverage of `affine_space.py` from 45% (9 of 20) to 80% (16 of 20) and fixes a few tiny bugs along the way.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5631\n\n",
    "created_at": "2009-03-29T07:59:52Z",
    "labels": [
        "component: algebraic geometry",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "improve doctest coverage for schemes/generic/affine_space.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5631",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

Keywords: doctest affine space

The attached patch improves the doctest coverage of `affine_space.py` from 45% (9 of 20) to 80% (16 of 20) and fixes a few tiny bugs along the way.


Issue created by migration from https://trac.sagemath.org/ticket/5631





---

archive/issue_comments_043887.json:
```json
{
    "body": "Changing assignee from @williamstein to @aghitza.",
    "created_at": "2009-03-29T08:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5631#issuecomment-43887",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @aghitza.



---

archive/issue_comments_043888.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-29T08:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5631#issuecomment-43888",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043889.json:
```json
{
    "body": "I don't understand why you deleted lines 415, 416 below:\n\n```\n414\t505\t    def subscheme_complement(self, X, Y): \n415\t \t        X = self.subscheme(X) \n416\t \t        Y = self.subscheme(Y) \n```\n\n\nThe way you have the code now, it subscheme_complement has nothing at all to do with self.  Why is it even a method of self as is now.  \n\nOtherwise this patch looks very good.",
    "created_at": "2009-03-29T17:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5631#issuecomment-43889",
    "user": "https://github.com/williamstein"
}
```

I don't understand why you deleted lines 415, 416 below:

```
414	505	    def subscheme_complement(self, X, Y): 
415	 	        X = self.subscheme(X) 
416	 	        Y = self.subscheme(Y) 
```


The way you have the code now, it subscheme_complement has nothing at all to do with self.  Why is it even a method of self as is now.  

Otherwise this patch looks very good.



---

archive/issue_comments_043890.json:
```json
{
    "body": "I had two problems with lines 415 and 416: (1) the doctest that I wrote wasn't working and (2) they aren't there in the corresponding method in `projective_space.py`.  If you look at the docstring that I wrote for `subscheme_complement` (and the doctest), you will notice that X and Y are already subschemes of self (so self is involved in a slightly hidden way).\n\nI guess that one could relax the syntax so that polynomial lists can be passed to `subscheme_complement`; in the example of the doctest this would be\n\n\n```\nsage: A.<x, y, z> = AffineSpace(3, ZZ)\nsage: A.subscheme_complement([x+y-z], [x-y+z])\n```\n\n\nIs this what you have in mind?",
    "created_at": "2009-03-29T21:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5631#issuecomment-43890",
    "user": "https://github.com/aghitza"
}
```

I had two problems with lines 415 and 416: (1) the doctest that I wrote wasn't working and (2) they aren't there in the corresponding method in `projective_space.py`.  If you look at the docstring that I wrote for `subscheme_complement` (and the doctest), you will notice that X and Y are already subschemes of self (so self is involved in a slightly hidden way).

I guess that one could relax the syntax so that polynomial lists can be passed to `subscheme_complement`; in the example of the doctest this would be


```
sage: A.<x, y, z> = AffineSpace(3, ZZ)
sage: A.subscheme_complement([x+y-z], [x-y+z])
```


Is this what you have in mind?



---

archive/issue_comments_043891.json:
```json
{
    "body": "> If you look at the docstring that I wrote for subscheme_complement \n> (and the doctest), you will notice that X and Y are already subschemes \n> of self (so self is involved in a slightly hidden way). \n\nCouldn't I do this:\n\n```\nsage: A.<x, y, z> = AffineSpace(3, ZZ)\nsage: [[make an X and a Y over GF(7) say that haven't nothing to do with A]]\nsage: A.subscheme_complement(X, Y)\n```\n\n\nEither subscheme_complement needs to check that X and Y are really subschemes of A, or it should just be a method of X, i.e.,\n\n```\nsage: X.complement(Y)\n```\n\nsay, which requires that X and Y live in a common ambient space.\n\n -- William",
    "created_at": "2009-03-30T00:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5631#issuecomment-43891",
    "user": "https://github.com/williamstein"
}
```

> If you look at the docstring that I wrote for subscheme_complement 
> (and the doctest), you will notice that X and Y are already subschemes 
> of self (so self is involved in a slightly hidden way). 

Couldn't I do this:

```
sage: A.<x, y, z> = AffineSpace(3, ZZ)
sage: [[make an X and a Y over GF(7) say that haven't nothing to do with A]]
sage: A.subscheme_complement(X, Y)
```


Either subscheme_complement needs to check that X and Y are really subschemes of A, or it should just be a method of X, i.e.,

```
sage: X.complement(Y)
```

say, which requires that X and Y live in a common ambient space.

 -- William



---

archive/issue_comments_043892.json:
```json
{
    "body": "So I looked at algebraic_scheme.py and noticed that there is a method `X.exclude(Y)` which seems to want to do what you're suggesting.  It's actually broken as it is, and I doubt that it ever worked (no doctests, not used anywhere in the Sage library, and the simplest tests that I thought of didn't work).  So I'm renaming it to `X.complement(Y)` and removing `subscheme_complement()` from both `affine_space.py` and `projective_space.py`.  They are also not used anywhere.",
    "created_at": "2009-03-30T21:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5631#issuecomment-43892",
    "user": "https://github.com/aghitza"
}
```

So I looked at algebraic_scheme.py and noticed that there is a method `X.exclude(Y)` which seems to want to do what you're suggesting.  It's actually broken as it is, and I doubt that it ever worked (no doctests, not used anywhere in the Sage library, and the simplest tests that I thought of didn't work).  So I'm renaming it to `X.complement(Y)` and removing `subscheme_complement()` from both `affine_space.py` and `projective_space.py`.  They are also not used anywhere.



---

archive/issue_comments_043893.json:
```json
{
    "body": "Attachment [trac_5631.patch](tarball://root/attachments/some-uuid/ticket5631/trac_5631.patch) by @aghitza created at 2009-04-03 10:09:26",
    "created_at": "2009-04-03T10:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5631#issuecomment-43893",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5631.patch](tarball://root/attachments/some-uuid/ticket5631/trac_5631.patch) by @aghitza created at 2009-04-03 10:09:26



---

archive/issue_comments_043894.json:
```json
{
    "body": "Can you rebase it?  Or does it depends on something?  I can't apply it:\n\n```\nteragon:build wstein$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nhg_sage.apply('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5631/trac_5631.patch')\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5631/trac_5631.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5631/trac_5631.patch\nLoading: [..]\ncd \"/Users/wstein/build/sage-3.4.1.rc1/devel/sage\" && hg status\ncd \"/Users/wstein/build/sage-3.4.1.rc1/devel/sage\" && hg status\ncd \"/Users/wstein/build/sage-3.4.1.rc1/devel/sage\" && hg import   \"/Users/wstein/.sage/temp/teragon.local/86960/tmp_1.patch\"\napplying /Users/wstein/.sage/temp/teragon.local/86960/tmp_1.patch\npatching file sage/schemes/generic/affine_space.py\nHunk #4 FAILED at 208\nHunk #5 succeeded at 243 with fuzz 2 (offset 0 lines).\nHunk #6 FAILED at 264\n2 out of 8 hunks FAILED -- saving rejects to file sage/schemes/generic/affine_space.py.rej\nabort: patch failed to apply\nsage: \n| Sage Version 3.4.1.rc1, Release Date: 2009-04-05                   |\n| Type notebook() for the GUI, and license() for information.        |\n```\n",
    "created_at": "2009-04-10T05:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5631#issuecomment-43894",
    "user": "https://github.com/williamstein"
}
```

Can you rebase it?  Or does it depends on something?  I can't apply it:

```
teragon:build wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
hg_sage.apply('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5631/trac_5631.patch')
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5631/trac_5631.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5631/trac_5631.patch
Loading: [..]
cd "/Users/wstein/build/sage-3.4.1.rc1/devel/sage" && hg status
cd "/Users/wstein/build/sage-3.4.1.rc1/devel/sage" && hg status
cd "/Users/wstein/build/sage-3.4.1.rc1/devel/sage" && hg import   "/Users/wstein/.sage/temp/teragon.local/86960/tmp_1.patch"
applying /Users/wstein/.sage/temp/teragon.local/86960/tmp_1.patch
patching file sage/schemes/generic/affine_space.py
Hunk #4 FAILED at 208
Hunk #5 succeeded at 243 with fuzz 2 (offset 0 lines).
Hunk #6 FAILED at 264
2 out of 8 hunks FAILED -- saving rejects to file sage/schemes/generic/affine_space.py.rej
abort: patch failed to apply
sage: 
| Sage Version 3.4.1.rc1, Release Date: 2009-04-05                   |
| Type notebook() for the GUI, and license() for information.        |
```




---

archive/issue_comments_043895.json:
```json
{
    "body": "Attachment [trac_5631_rebased.patch](tarball://root/attachments/some-uuid/ticket5631/trac_5631_rebased.patch) by @aghitza created at 2009-04-10 08:23:40\n\napply instead of the previous patch",
    "created_at": "2009-04-10T08:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5631#issuecomment-43895",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5631_rebased.patch](tarball://root/attachments/some-uuid/ticket5631/trac_5631_rebased.patch) by @aghitza created at 2009-04-10 08:23:40

apply instead of the previous patch



---

archive/issue_comments_043896.json:
```json
{
    "body": "Yes, there was some interaction with the ticket that fixed dimension issues.\n\nThe new patch applies to 3.4.1.rc1.",
    "created_at": "2009-04-10T08:24:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5631#issuecomment-43896",
    "user": "https://github.com/aghitza"
}
```

Yes, there was some interaction with the ticket that fixed dimension issues.

The new patch applies to 3.4.1.rc1.



---

archive/issue_comments_043897.json:
```json
{
    "body": "Merged trac_5631_rebased.patch in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-12T21:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5631#issuecomment-43897",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_5631_rebased.patch in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_043898.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-12T21:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5631#issuecomment-43898",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005872.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-04-12T21:33:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5631",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5631#event-5872"
}
```
