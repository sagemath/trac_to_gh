# Issue 1951: reducation map modulo a number field prime ideal still not 100% done

archive/issues_001951.json:
```json
{
    "body": "Assignee: was\n\nThis should work:\n\n```\nsage: K.<i> = NumberField(x^2 + 1)\nsage: P = [g[0] for g in K.factor_integer(5)]; P\n[Fractional ideal (-i - 2), Fractional ideal (2*i + 1)]\nsage: a = 1/(1+2*i)\nsage: K = [g.residue_field() for g in P]; K\n[Residue field of Fractional ideal (-i - 2), Residue field of Fractional ideal (2*i + 1)]\nsage: F = K[0]\nsage: a.valuation(P[0])\n0\nsage: F(i/7)\n4\nsage: F(a)\nTraceback (most recent call last):\n...\nZeroDivisionError: Inverse does not exist.\n```\n\n\nThe problem is that a in terms of a basis for the maximal order still has\nsome 5's in the denominator, even though a is P[0]-integral.  To fix this\nin general, one could:\n  \n1. Find an element b of the ring of integers that is 1 modulo P[0] and is 0 modulo all the other P[i] (using the not-implemented-right now CRT),\n\n2. Multiply a through by some power of b.\n\n3. Reduce.  \n\n4. Divide back through by the reduction of b.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1951\n\n",
    "created_at": "2008-01-27T20:40:44Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "reducation map modulo a number field prime ideal still not 100% done",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1951",
    "user": "was"
}
```
Assignee: was

This should work:

```
sage: K.<i> = NumberField(x^2 + 1)
sage: P = [g[0] for g in K.factor_integer(5)]; P
[Fractional ideal (-i - 2), Fractional ideal (2*i + 1)]
sage: a = 1/(1+2*i)
sage: K = [g.residue_field() for g in P]; K
[Residue field of Fractional ideal (-i - 2), Residue field of Fractional ideal (2*i + 1)]
sage: F = K[0]
sage: a.valuation(P[0])
0
sage: F(i/7)
4
sage: F(a)
Traceback (most recent call last):
...
ZeroDivisionError: Inverse does not exist.
```


The problem is that a in terms of a basis for the maximal order still has
some 5's in the denominator, even though a is P[0]-integral.  To fix this
in general, one could:
  
1. Find an element b of the ring of integers that is 1 modulo P[0] and is 0 modulo all the other P[i] (using the not-implemented-right now CRT),

2. Multiply a through by some power of b.

3. Reduce.  

4. Divide back through by the reduction of b.



Issue created by migration from https://trac.sagemath.org/ticket/1951





---

archive/issue_comments_012416.json:
```json
{
    "body": "Attachment [1951-residues.patch](tarball://root/attachments/some-uuid/ticket1951/1951-residues.patch) by cremona created at 2008-09-10 09:32:38",
    "created_at": "2008-09-10T09:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1951#issuecomment-12416",
    "user": "cremona"
}
```

Attachment [1951-residues.patch](tarball://root/attachments/some-uuid/ticket1951/1951-residues.patch) by cremona created at 2008-09-10 09:32:38



---

archive/issue_comments_012417.json:
```json
{
    "body": "The patch fixes this, so that any element which is P-integral can be reduced modulo P (non-P-integral elements will raise a ZeroDivisionError with an explanation).\n\nIt took a long time to find out where to put the new code, since the structure of the residue fields and reduction maps code is so byzantine!  In the end the solution was not hard, though I used a different method from what was suggested (see comments in the patch).\n\nThe new code is in sage.rings.residue_field.pyx;  I also put a doctest into number_field.number_field_ideal.py.\n\nBy the way, it is not really necessary to use recursion since when the function calls itself it always bottoms out right away.  So it would be easy to rewrite it without any;  I just found it easier to write `self(nx)` than `self.__F(self.__to_vs(nx) * self.__PBinv)` and similar.",
    "created_at": "2008-09-10T09:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1951#issuecomment-12417",
    "user": "cremona"
}
```

The patch fixes this, so that any element which is P-integral can be reduced modulo P (non-P-integral elements will raise a ZeroDivisionError with an explanation).

It took a long time to find out where to put the new code, since the structure of the residue fields and reduction maps code is so byzantine!  In the end the solution was not hard, though I used a different method from what was suggested (see comments in the patch).

The new code is in sage.rings.residue_field.pyx;  I also put a doctest into number_field.number_field_ideal.py.

By the way, it is not really necessary to use recursion since when the function calls itself it always bottoms out right away.  So it would be easy to rewrite it without any;  I just found it easier to write `self(nx)` than `self.__F(self.__to_vs(nx) * self.__PBinv)` and similar.



---

archive/issue_comments_012418.json:
```json
{
    "body": "Changing keywords from \"\" to \"number field residue field reduction\".",
    "created_at": "2008-09-10T09:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1951#issuecomment-12418",
    "user": "cremona"
}
```

Changing keywords from "" to "number field residue field reduction".



---

archive/issue_comments_012419.json:
```json
{
    "body": "Attachment [1951-residues-1.patch](tarball://root/attachments/some-uuid/ticket1951/1951-residues-1.patch) by cremona created at 2008-09-10 10:36:32",
    "created_at": "2008-09-10T10:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1951#issuecomment-12419",
    "user": "cremona"
}
```

Attachment [1951-residues-1.patch](tarball://root/attachments/some-uuid/ticket1951/1951-residues-1.patch) by cremona created at 2008-09-10 10:36:32



---

archive/issue_comments_012420.json:
```json
{
    "body": "It's a small thing but I just noticed that the number field function residue_field() has this definition:\n\n```\n    def residue_field(self, prime, names = None, check = False):\n```\n\nwhere the \"check\" parameter claims to control whether  \"prime\" really is prime, but this is ignored.  It should be passed down through the call to  `sage.rings.residue_field.ResidueField(prime, names = names)`\nwhich does honour the check parameter.\n\nExample:\n\n```\nsage: K.<i> = NumberField(x^2 + 1)\nsage: Q = K.ideal(5)\nsage: Q.is_prime()\nFalse\nsage: K.residue_field(Q, check=False)\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/home/john/sage-3.1.2.rc1/devel/<ipython console> in <module>()\n\n/home/john/sage-3.1.2.rc1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in residue_field(self, prime, names, check)\n   3000             raise ValueError, \"prime must be a prime ideal of self\"\n   3001         import sage.rings.residue_field\n-> 3002         return sage.rings.residue_field.ResidueField(prime, names = names)\n   3003 \n   3004     def signature(self):\n\n/home/john/sage-3.1.2.rc1/devel/residue_field.pyx in sage.rings.residue_field.ResidueField (sage/rings/residue_field.c:2778)()\n\nValueError: p must be prime\n```\n\n\nThe second patch fixes this.  Note that the default was \"check=False\", while the called function ResidueField() has its default as \"check=True\".  I thought it safer to change the deafult to \"check=True\" since this makes the new default behaviour like the old behaviour.  (If you use check=False and the ideal is not prime, the first error which arises is a bit obscure:\n\n```\n    AttributeError: 'NumberFieldFractionalIdeal' object has no attribute '_NumberFieldIdeal__smallest_integer'\n```\n\nsince smallest_integer() is defined only for prime ideals.  But something has to go wrong at some point in this situation, and at least now it will only happen when the user has deliberately turned off checking.",
    "created_at": "2008-09-10T10:37:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1951#issuecomment-12420",
    "user": "cremona"
}
```

It's a small thing but I just noticed that the number field function residue_field() has this definition:

```
    def residue_field(self, prime, names = None, check = False):
```

where the "check" parameter claims to control whether  "prime" really is prime, but this is ignored.  It should be passed down through the call to  `sage.rings.residue_field.ResidueField(prime, names = names)`
which does honour the check parameter.

Example:

```
sage: K.<i> = NumberField(x^2 + 1)
sage: Q = K.ideal(5)
sage: Q.is_prime()
False
sage: K.residue_field(Q, check=False)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/john/sage-3.1.2.rc1/devel/<ipython console> in <module>()

/home/john/sage-3.1.2.rc1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in residue_field(self, prime, names, check)
   3000             raise ValueError, "prime must be a prime ideal of self"
   3001         import sage.rings.residue_field
-> 3002         return sage.rings.residue_field.ResidueField(prime, names = names)
   3003 
   3004     def signature(self):

/home/john/sage-3.1.2.rc1/devel/residue_field.pyx in sage.rings.residue_field.ResidueField (sage/rings/residue_field.c:2778)()

ValueError: p must be prime
```


The second patch fixes this.  Note that the default was "check=False", while the called function ResidueField() has its default as "check=True".  I thought it safer to change the deafult to "check=True" since this makes the new default behaviour like the old behaviour.  (If you use check=False and the ideal is not prime, the first error which arises is a bit obscure:

```
    AttributeError: 'NumberFieldFractionalIdeal' object has no attribute '_NumberFieldIdeal__smallest_integer'
```

since smallest_integer() is defined only for prime ideals.  But something has to go wrong at some point in this situation, and at least now it will only happen when the user has deliberately turned off checking.



---

archive/issue_comments_012421.json:
```json
{
    "body": "Looks good, applies cleanly against 3.1.2, and passes relevant doctests (checked sage/rings, sage/schemes, and sage/modular).",
    "created_at": "2008-09-20T04:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1951#issuecomment-12421",
    "user": "AlexGhitza"
}
```

Looks good, applies cleanly against 3.1.2, and passes relevant doctests (checked sage/rings, sage/schemes, and sage/modular).



---

archive/issue_comments_012422.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-20T22:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1951#issuecomment-12422",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012423.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha1",
    "created_at": "2008-09-20T22:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1951#issuecomment-12423",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha1
