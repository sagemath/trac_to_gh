# Issue 7194: extended singular functions interface, needs work

archive/issues_007194.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @malb @burcin hannes@mathematik.uni-kl.de\n\nKeywords: singular\n\nwrapped list, use intvec as input, wrapped ring (RingWrap for return)...\nThis can wrap a lot more of Singular functions now.\n\nThis needs the header file lists.h, which is not installed by default.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7194\n\n",
    "created_at": "2009-10-12T12:23:23Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "extended singular functions interface, needs work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7194",
    "user": "PolyBoRi"
}
```
Assignee: @malb

CC:  @malb @burcin hannes@mathematik.uni-kl.de

Keywords: singular

wrapped list, use intvec as input, wrapped ring (RingWrap for return)...
This can wrap a lot more of Singular functions now.

This needs the header file lists.h, which is not installed by default.

Issue created by migration from https://trac.sagemath.org/ticket/7194





---

archive/issue_comments_059652.json:
```json
{
    "body": "Attachment [singular_list.2.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.2.patch) by PolyBoRi created at 2009-10-13 09:08:55",
    "created_at": "2009-10-13T09:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59652",
    "user": "PolyBoRi"
}
```

Attachment [singular_list.2.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.2.patch) by PolyBoRi created at 2009-10-13 09:08:55



---

archive/issue_comments_059653.json:
```json
{
    "body": "I updated the patch. It now supports matrices as well :-).\nI also fixes some problem when returning polynomials.\nCheers,\nMichael\n\nP.S.: Next targets are intmat and letter place.",
    "created_at": "2009-10-13T09:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59653",
    "user": "PolyBoRi"
}
```

I updated the patch. It now supports matrices as well :-).
I also fixes some problem when returning polynomials.
Cheers,
Michael

P.S.: Next targets are intmat and letter place.



---

archive/issue_comments_059654.json:
```json
{
    "body": "Hi!\nA small demonstration of the copy and paste feature:\n\nSingular:\n\n```\nproc content(f)\n\"USAGE:   content(f); f polynomial/vector\nRETURN:  number, the content (greatest common factor of coefficients)\n         of the polynomial/vector f\nSEE ALSO: cleardenom\nEXAMPLE: example content; shows an example\n\"\n{\n  if (f==0) { return(number(1)); }\n  return(leadcoef(f)/leadcoef(cleardenom(f)));\n}\nexample\n{ \"EXAMPLE:\"; echo = 2;\n   ring r=0,(x,y,z),(c,lp);\n   content(3x2+18xy-27xyz);\n   vector v=[3x2+18xy-27xyz,15x2+12y4,3];\n   content(v);\n}\n```\n\n\nSage:\n\n```python\n\nfrom sage.libs.singular.function import singular_function, lib\nleadcoef =  singular_function(\"leadcoef\")\ncleardenom = singular_function(\"cleardenom\")\n\ndef content(f):\n    \"\"\"\n    Examples:\n    sage: P.<x,y,z>=PolynomialRing(QQ)\n    sage: content(3*x**2+18*x*y-27*x*y*z)\n    -3\n    \"\"\"\n    if f==0:\n        return 1\n    return leadcoef(f)/leadcoef(cleardenom(f))\n\n```\n",
    "created_at": "2009-10-13T11:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59654",
    "user": "PolyBoRi"
}
```

Hi!
A small demonstration of the copy and paste feature:

Singular:

```
proc content(f)
"USAGE:   content(f); f polynomial/vector
RETURN:  number, the content (greatest common factor of coefficients)
         of the polynomial/vector f
SEE ALSO: cleardenom
EXAMPLE: example content; shows an example
"
{
  if (f==0) { return(number(1)); }
  return(leadcoef(f)/leadcoef(cleardenom(f)));
}
example
{ "EXAMPLE:"; echo = 2;
   ring r=0,(x,y,z),(c,lp);
   content(3x2+18xy-27xyz);
   vector v=[3x2+18xy-27xyz,15x2+12y4,3];
   content(v);
}
```


Sage:

```python

from sage.libs.singular.function import singular_function, lib
leadcoef =  singular_function("leadcoef")
cleardenom = singular_function("cleardenom")

def content(f):
    """
    Examples:
    sage: P.<x,y,z>=PolynomialRing(QQ)
    sage: content(3*x**2+18*x*y-27*x*y*z)
    -3
    """
    if f==0:
        return 1
    return leadcoef(f)/leadcoef(cleardenom(f))

```




---

archive/issue_comments_059655.json:
```json
{
    "body": "Attachment [singular_list.3.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.3.patch) by PolyBoRi created at 2009-10-13 12:27:30",
    "created_at": "2009-10-13T12:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59655",
    "user": "PolyBoRi"
}
```

Attachment [singular_list.3.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.3.patch) by PolyBoRi created at 2009-10-13 12:27:30



---

archive/issue_comments_059656.json:
```json
{
    "body": "How to construct ring with parameters\n\n```python\nP.<x,y,z>=PolynomialRing(QQ)\ncharacteristic=0\nnumber_of_variables=1\nnumber_of_parameters=3\nl=[\n    [0, ['a','b','c'], [['dp', number_of_parameters*(1,)], ['C', (0,)]], P.ideal([0])]\n, ['x', 'y', 'z'], [['dp', number_of_parameters*(1,)], ['C', (0,)]], P.ideal([0])]\nring=singular_function(\"ring\")\nring(l, ring=P)\n```\n",
    "created_at": "2009-10-13T13:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59656",
    "user": "PolyBoRi"
}
```

How to construct ring with parameters

```python
P.<x,y,z>=PolynomialRing(QQ)
characteristic=0
number_of_variables=1
number_of_parameters=3
l=[
    [0, ['a','b','c'], [['dp', number_of_parameters*(1,)], ['C', (0,)]], P.ideal([0])]
, ['x', 'y', 'z'], [['dp', number_of_parameters*(1,)], ['C', (0,)]], P.ideal([0])]
ring=singular_function("ring")
ring(l, ring=P)
```




---

archive/issue_comments_059657.json:
```json
{
    "body": "how to make letter place\nsage: from sage.libs.singular.function import lib, singular_function\nsage: P.<x,y,z>=QQ[]\nsage: lib(\"freegb.lib\")\nsage: make_letter_place_ring = singular_function(\"makeLetterplaceRing\")\nsage: make_letter_place_ring(10, ring=P)\n<RingWrap>",
    "created_at": "2009-10-13T13:24:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59657",
    "user": "PolyBoRi"
}
```

how to make letter place
sage: from sage.libs.singular.function import lib, singular_function
sage: P.<x,y,z>=QQ[]
sage: lib("freegb.lib")
sage: make_letter_place_ring = singular_function("makeLetterplaceRing")
sage: make_letter_place_ring(10, ring=P)
<RingWrap>



---

archive/issue_comments_059658.json:
```json
{
    "body": "sorry:\n\n\n```python\n\nsage: from sage.libs.singular.function import lib, singular_function\nsage: P.<x,y,z>=QQ[]\nsage: lib(\"freegb.lib\")\nsage: \nsage: make_letter_place_ring = singular_function(\"makeLetterplaceRing\")\nsage: make_letter_place_ring(10, ring=P)\n<RingWrap>\n```\n",
    "created_at": "2009-10-13T13:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59658",
    "user": "PolyBoRi"
}
```

sorry:


```python

sage: from sage.libs.singular.function import lib, singular_function
sage: P.<x,y,z>=QQ[]
sage: lib("freegb.lib")
sage: 
sage: make_letter_place_ring = singular_function("makeLetterplaceRing")
sage: make_letter_place_ring(10, ring=P)
<RingWrap>
```




---

archive/issue_comments_059659.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-10-15T11:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59659",
    "user": "PolyBoRi"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_059660.json:
```json
{
    "body": "the latest patch supports intvec/intmat\nCheers,\nMichael",
    "created_at": "2009-10-15T11:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59660",
    "user": "PolyBoRi"
}
```

the latest patch supports intvec/intmat
Cheers,
Michael



---

archive/issue_comments_059661.json:
```json
{
    "body": "Attachment [singular_list.4.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.4.patch) by PolyBoRi created at 2009-10-15 11:19:31",
    "created_at": "2009-10-15T11:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59661",
    "user": "PolyBoRi"
}
```

Attachment [singular_list.4.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.4.patch) by PolyBoRi created at 2009-10-15 11:19:31



---

archive/issue_comments_059662.json:
```json
{
    "body": "Attachment [singular_list.5.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.5.patch) by PolyBoRi created at 2009-10-15 15:08:13\n\nthe recent version wraps vectors over P**n in both direction.\nNow, I am about hunting the modules.",
    "created_at": "2009-10-15T15:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59662",
    "user": "PolyBoRi"
}
```

Attachment [singular_list.5.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.5.patch) by PolyBoRi created at 2009-10-15 15:08:13

the recent version wraps vectors over P**n in both direction.
Now, I am about hunting the modules.



---

archive/issue_comments_059663.json:
```json
{
    "body": "Attachment [singular_list.7.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.7.patch) by PolyBoRi created at 2009-10-16 13:01:50",
    "created_at": "2009-10-16T13:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59663",
    "user": "PolyBoRi"
}
```

Attachment [singular_list.7.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.7.patch) by PolyBoRi created at 2009-10-16 13:01:50



---

archive/issue_comments_059664.json:
```json
{
    "body": "The latest version supports also modules and free resolution objects.\n\nFree resolution objects form some lazy blackbox in Singular, so I just did some basic blackbox. The rest can be accessed via singular functions using this interface.\nSo, we might extend Resolution object interface at some time, when it is needed.\nCheers,\nMichael",
    "created_at": "2009-10-16T13:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59664",
    "user": "PolyBoRi"
}
```

The latest version supports also modules and free resolution objects.

Free resolution objects form some lazy blackbox in Singular, so I just did some basic blackbox. The rest can be accessed via singular functions using this interface.
So, we might extend Resolution object interface at some time, when it is needed.
Cheers,
Michael



---

archive/issue_comments_059665.json:
```json
{
    "body": "Attachment [singular_list.8.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.8.patch) by PolyBoRi created at 2009-10-16 14:15:40",
    "created_at": "2009-10-16T14:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59665",
    "user": "PolyBoRi"
}
```

Attachment [singular_list.8.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.8.patch) by PolyBoRi created at 2009-10-16 14:15:40



---

archive/issue_comments_059666.json:
```json
{
    "body": "Attachment [singular_list.9.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.9.patch) by @malb created at 2009-11-18 17:10:23\n\nA new SPKG installing `Singular/lists.h` is available here\n\n   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.p2.spkg",
    "created_at": "2009-11-18T17:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59666",
    "user": "@malb"
}
```

Attachment [singular_list.9.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.9.patch) by @malb created at 2009-11-18 17:10:23

A new SPKG installing `Singular/lists.h` is available here

   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.p2.spkg



---

archive/issue_comments_059667.json:
```json
{
    "body": "Attachment [singular_lists_referee.patch](tarball://root/attachments/some-uuid/ticket7194/singular_lists_referee.patch) by @malb created at 2009-11-18 17:45:30\n\nI give Michael's patch a positive review. However, somebody needs to review my documentation/cleanup patch and the SPKG.\n\nHow to apply:\n* install http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.p2.spkg\n* apply singular_list.10.patch\n* apply singular_lists_referee.patch",
    "created_at": "2009-11-18T17:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59667",
    "user": "@malb"
}
```

Attachment [singular_lists_referee.patch](tarball://root/attachments/some-uuid/ticket7194/singular_lists_referee.patch) by @malb created at 2009-11-18 17:45:30

I give Michael's patch a positive review. However, somebody needs to review my documentation/cleanup patch and the SPKG.

How to apply:
* install http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.p2.spkg
* apply singular_list.10.patch
* apply singular_lists_referee.patch



---

archive/issue_comments_059668.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-18T17:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59668",
    "user": "@malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059669.json:
```json
{
    "body": "Michael, Burcin, any takers for looking at my referee patch?",
    "created_at": "2009-12-01T16:39:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59669",
    "user": "@malb"
}
```

Michael, Burcin, any takers for looking at my referee patch?



---

archive/issue_comments_059670.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-01T18:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59670",
    "user": "@burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059671.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-12-01T18:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59671",
    "user": "@burcin"
}
```

Looks good to me.



---

archive/issue_comments_059672.json:
```json
{
    "body": "I get all sorts of Cython errors in function.pyx about cdef functions not being declared.\n\nDid you try this on 4.3.alpha0?",
    "created_at": "2009-12-02T08:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59672",
    "user": "@mwhansen"
}
```

I get all sorts of Cython errors in function.pyx about cdef functions not being declared.

Did you try this on 4.3.alpha0?



---

archive/issue_comments_059673.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-12-02T08:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59673",
    "user": "@mwhansen"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_059674.json:
```json
{
    "body": "Attachment [singular_list.10.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.10.patch) by @malb created at 2009-12-02 11:12:03\n\nfixed to work with 4.3",
    "created_at": "2009-12-02T11:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59674",
    "user": "@malb"
}
```

Attachment [singular_list.10.patch](tarball://root/attachments/some-uuid/ticket7194/singular_list.10.patch) by @malb created at 2009-12-02 11:12:03

fixed to work with 4.3



---

archive/issue_comments_059675.json:
```json
{
    "body": "I fixed the compilation failures under 4.3, strange that it compiled with 4.2. The instructions remain the same:\n\n* install  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.p2.spkg \n* apply `singular_list.10.patch` (fixed)\n* apply `singular_lists_referee.patch`",
    "created_at": "2009-12-02T11:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59675",
    "user": "@malb"
}
```

I fixed the compilation failures under 4.3, strange that it compiled with 4.2. The instructions remain the same:

* install  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.p2.spkg 
* apply `singular_list.10.patch` (fixed)
* apply `singular_lists_referee.patch`



---

archive/issue_comments_059676.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-02T11:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59676",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_059677.json:
```json
{
    "body": "Thanks to all, who helped to get that code into Sage (while I was in holidays).\nYou made me really happy :-).\n\nCheers,\nMichael",
    "created_at": "2009-12-07T13:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7194#issuecomment-59677",
    "user": "PolyBoRi"
}
```

Thanks to all, who helped to get that code into Sage (while I was in holidays).
You made me really happy :-).

Cheers,
Michael
