# Issue 7016: Bizarre results when taking the mod of a p-adic number

archive/issues_007016.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  wstein mabshoff @roed314\n\nKeywords: padic, mod, %\n\nThe operation x % n for p-adic numbers x and integers n currently depends on the creation method of the p-adic number (not just it's equality).  It also does not seem to return meaningful results!\n\nIssue created by migration from https://trac.sagemath.org/ticket/7016\n\n",
    "created_at": "2009-09-26T01:54:51Z",
    "labels": [
        "algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Bizarre results when taking the mod of a p-adic number",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7016",
    "user": "@jonhanke"
}
```
Assignee: tbd

CC:  wstein mabshoff @roed314

Keywords: padic, mod, %

The operation x % n for p-adic numbers x and integers n currently depends on the creation method of the p-adic number (not just it's equality).  It also does not seem to return meaningful results!

Issue created by migration from https://trac.sagemath.org/ticket/7016





---

archive/issue_comments_058064.json:
```json
{
    "body": "\n```\n## Create a p-adic number in two ways\nsage: e = 1 + O(2^20)  ## Explicit creation\nsage: e\n1 + O(2^20)\nsage: c = Qp(2)(1)     ## By coercion\nsage: c\n1 + O(2^20)\nsage: e == c\nTrue\n\n## Check their types\nsage: type(e)\n<type 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>\nsage: type(c)\n<type 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>\n\n## Use the mod operation, with inconsistent results: (I expected the integer 1 in both cases)\nsage: e % 8\n1 + O(2^20)\nsage: c % 8\n0\nsage: e % 8 == c % 8\nFalse\n\n## Check the mod types\nsage: type(e % 8)\n<type 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>\nsage: type(c % 8)\n<type 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>\n\n\n## Check their lifts\nsage: e.lift()\n1\nsage: c.lift()\n1\nsage: c.lift() == e.lift()\nTrue\nsage: c.lift() % 8 == e.lift() % 8\nTrue\n\n\n```\n\n\n\n\nSuggestions:\n\n\n1) x % M returns an integer when x is a p-adic number (in Qp) and M is\n   an integer or raises an error if either the modulus is not a power\n   of p or is larger than the known precision of the number allows.\n   This syntax will return an error for any (non-trivial) extensions\n   of Qp.\n\n2) Add a more general syntax x.reduce_mod_prime() returns an element\n   of FiniteField(q) whenever x is an element of an unramified\n   extension Qq of Qp.\n\n3) It might also be nice to have an x.reduce_mod_prime_power(n) which\n   would return an element in the associated finite quotient ring\n   Q_q/((pi)**n), but this may not be worth the effort right now.",
    "created_at": "2009-09-26T01:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58064",
    "user": "@jonhanke"
}
```


```
## Create a p-adic number in two ways
sage: e = 1 + O(2^20)  ## Explicit creation
sage: e
1 + O(2^20)
sage: c = Qp(2)(1)     ## By coercion
sage: c
1 + O(2^20)
sage: e == c
True

## Check their types
sage: type(e)
<type 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>
sage: type(c)
<type 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>

## Use the mod operation, with inconsistent results: (I expected the integer 1 in both cases)
sage: e % 8
1 + O(2^20)
sage: c % 8
0
sage: e % 8 == c % 8
False

## Check the mod types
sage: type(e % 8)
<type 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>
sage: type(c % 8)
<type 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>


## Check their lifts
sage: e.lift()
1
sage: c.lift()
1
sage: c.lift() == e.lift()
True
sage: c.lift() % 8 == e.lift() % 8
True


```




Suggestions:


1) x % M returns an integer when x is a p-adic number (in Qp) and M is
   an integer or raises an error if either the modulus is not a power
   of p or is larger than the known precision of the number allows.
   This syntax will return an error for any (non-trivial) extensions
   of Qp.

2) Add a more general syntax x.reduce_mod_prime() returns an element
   of FiniteField(q) whenever x is an element of an unramified
   extension Qq of Qp.

3) It might also be nice to have an x.reduce_mod_prime_power(n) which
   would return an element in the associated finite quotient ring
   Q_q/((pi)**n), but this may not be worth the effort right now.



---

archive/issue_comments_058065.json:
```json
{
    "body": "This is a consequence of the fact that those two elements have different parents: \n\n```\nsage: parent(1+O(2^20))\n2-adic Ring with capped relative precision 20\nsage: parent(Qp(2)(1))\n2-adic Field with capped relative precision 20\n```\n\n\nMost rings in sage return an element of the same ring when applying the operation %.  The function you want is residue.\n\n\n```\nsage: a = Zp(2)(1); b = Qp(2)(1)\nsage: a.residue(3), b.residue(3)\n(1, 1)\nsage: a.residue(3).parent(), b.residue(3).parent()\n(Ring of integers modulo 8, Ring of integers modulo 8)\nsage: c = Qp(2)(1/2)\nsage: c.residue(3)\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\nValueError: Element must have non-negative valuation in order to compute residue.\n```\n\n\nThere are some tricky questions for % and // and how they relate.  A similar issue bit William this past spring, so maybe we should have a design discussion about how to solve it.  I'm probably not going to be working on the p-adics this fall though: my advisor wants me to work on my thesis.  ;-)",
    "created_at": "2009-09-26T05:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58065",
    "user": "@roed314"
}
```

This is a consequence of the fact that those two elements have different parents: 

```
sage: parent(1+O(2^20))
2-adic Ring with capped relative precision 20
sage: parent(Qp(2)(1))
2-adic Field with capped relative precision 20
```


Most rings in sage return an element of the same ring when applying the operation %.  The function you want is residue.


```
sage: a = Zp(2)(1); b = Qp(2)(1)
sage: a.residue(3), b.residue(3)
(1, 1)
sage: a.residue(3).parent(), b.residue(3).parent()
(Ring of integers modulo 8, Ring of integers modulo 8)
sage: c = Qp(2)(1/2)
sage: c.residue(3)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

ValueError: Element must have non-negative valuation in order to compute residue.
```


There are some tricky questions for % and // and how they relate.  A similar issue bit William this past spring, so maybe we should have a design discussion about how to solve it.  I'm probably not going to be working on the p-adics this fall though: my advisor wants me to work on my thesis.  ;-)



---

archive/issue_comments_058066.json:
```json
{
    "body": "Changing priority from critical to major.",
    "created_at": "2010-12-26T21:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58066",
    "user": "@roed314"
}
```

Changing priority from critical to major.



---

archive/issue_comments_058067.json:
```json
{
    "body": "I was just glancing through tickets and found this one.  If anyone has suggestions for making % and // less confusing, please let me know.  There's documentation, but it's hidden in double underscore methods, so often doesn't get seen.",
    "created_at": "2010-12-26T21:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58067",
    "user": "@roed314"
}
```

I was just glancing through tickets and found this one.  If anyone has suggestions for making % and // less confusing, please let me know.  There's documentation, but it's hidden in double underscore methods, so often doesn't get seen.



---

archive/issue_comments_058068.json:
```json
{
    "body": "Changing component from algebra to padics.",
    "created_at": "2010-12-26T21:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58068",
    "user": "@roed314"
}
```

Changing component from algebra to padics.



---

archive/issue_comments_058069.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-03-21T17:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58069",
    "user": "rozenszt"
}
```

New commits:



---

archive/issue_comments_058070.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-03-21T17:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58070",
    "user": "rozenszt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058071.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-03-21T17:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58071",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_058072.json:
```json
{
    "body": "Personally, I don't think that the sentence \"This is different from the mod function `%` which returns an element with the same parent.\" really clarifies anything.",
    "created_at": "2016-03-21T17:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58072",
    "user": "@jdemeyer"
}
```

Personally, I don't think that the sentence "This is different from the mod function `%` which returns an element with the same parent." really clarifies anything.



---

archive/issue_comments_058073.json:
```json
{
    "body": "Replying to [comment:3 roed]:\n> This is a consequence of the fact that those two elements have different parents: \n> \n> Most rings in sage return an element of the same ring when applying the operation `%`.  The function you want is residue.\n> \n> There are some tricky questions for `%` and `//` and how they relate.\n\nThat may be, but it's still a poor excuse for having \"bizarre\" results for `%`. If `%` makes no sense, better disallow it completely.",
    "created_at": "2016-03-21T17:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58073",
    "user": "@jdemeyer"
}
```

Replying to [comment:3 roed]:
> This is a consequence of the fact that those two elements have different parents: 
> 
> Most rings in sage return an element of the same ring when applying the operation `%`.  The function you want is residue.
> 
> There are some tricky questions for `%` and `//` and how they relate.

That may be, but it's still a poor excuse for having "bizarre" results for `%`. If `%` makes no sense, better disallow it completely.



---

archive/issue_comments_058074.json:
```json
{
    "body": "Replying to [comment:12 jdemeyer]:\n> Personally, I don't think that the sentence \"This is different from the mod function `%` which returns an element with the same parent.\" really clarifies anything.\n\nActually there is already a detailled explanation of how the mod function works in its documentation, so the point of the note is mostly to direct people to the approriate documentation.",
    "created_at": "2016-03-22T06:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58074",
    "user": "rozenszt"
}
```

Replying to [comment:12 jdemeyer]:
> Personally, I don't think that the sentence "This is different from the mod function `%` which returns an element with the same parent." really clarifies anything.

Actually there is already a detailled explanation of how the mod function works in its documentation, so the point of the note is mostly to direct people to the approriate documentation.



---

archive/issue_comments_058075.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-11-17T22:24:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58075",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_058076.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-11-17T22:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58076",
    "user": "@saraedum"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_058077.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-11-17T22:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58077",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_058078.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-11-17T23:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58078",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_058079.json:
```json
{
    "body": "Looks good.",
    "created_at": "2016-11-17T23:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58079",
    "user": "@roed314"
}
```

Looks good.



---

archive/issue_comments_058080.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-11-17T23:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58080",
    "user": "@roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058081.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-11-19T22:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7016#issuecomment-58081",
    "user": "@vbraun"
}
```

Resolution: fixed
