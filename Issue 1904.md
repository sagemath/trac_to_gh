# Issue 1904: elliptic curves -- many period lattice functions just don't work

archive/issues_001904.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @loefflerd\n\n\n```\nsage: E = EllipticCurve('37a1')\nsage: Lambda = E.period_lattice()\nsage: OE = Lambda.omega(); OE\n5.986917292463919259664019958905016355595167582740265970681046757126500713973\nsage: Lambda.matrix()\nTraceback (most recent call last):\n...\nTypeError: Unable to coerce 2.451389381986790060854224831866525225349617289144796614656471406129152899999*I (<type 'sage.rings.complex_number.ComplexNumber'>) to Rational\nsage: Lambda.gram_matrix()\nTraceback (most recent call last):\n...\nAttributeError: 'PeriodLattice_ell' object has no attribute 'ambient_vector_space'\nsage: Lambda.basis()\n(2.993458646231959629832009979452508177797583791370132985340523378563250356987, 2.451389381986790060854224831866525225349617289144796614656471406129152899999*I)\nsage: Lambda.basis_matrix()\nTraceback (most recent call last):\n...\nTypeError: Unable to coerce 2.451389381986790060854224831866525225349617289144796614656471406129152899999*I (<type 'sage.rings.complex_number.ComplexNumber'>) to Rational\ns\n```\n\n\nThe root cause of this is that Period lattices actually derive from the abstract free module type, but they don't implement all the functionality that type requires. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1904\n\n",
    "created_at": "2008-01-24T02:46:27Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "elliptic curves -- many period lattice functions just don't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1904",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @loefflerd


```
sage: E = EllipticCurve('37a1')
sage: Lambda = E.period_lattice()
sage: OE = Lambda.omega(); OE
5.986917292463919259664019958905016355595167582740265970681046757126500713973
sage: Lambda.matrix()
Traceback (most recent call last):
...
TypeError: Unable to coerce 2.451389381986790060854224831866525225349617289144796614656471406129152899999*I (<type 'sage.rings.complex_number.ComplexNumber'>) to Rational
sage: Lambda.gram_matrix()
Traceback (most recent call last):
...
AttributeError: 'PeriodLattice_ell' object has no attribute 'ambient_vector_space'
sage: Lambda.basis()
(2.993458646231959629832009979452508177797583791370132985340523378563250356987, 2.451389381986790060854224831866525225349617289144796614656471406129152899999*I)
sage: Lambda.basis_matrix()
Traceback (most recent call last):
...
TypeError: Unable to coerce 2.451389381986790060854224831866525225349617289144796614656471406129152899999*I (<type 'sage.rings.complex_number.ComplexNumber'>) to Rational
s
```


The root cause of this is that Period lattices actually derive from the abstract free module type, but they don't implement all the functionality that type requires. 

Issue created by migration from https://trac.sagemath.org/ticket/1904





---

archive/issue_comments_012021.json:
```json
{
    "body": "Just to confirm that none of this has changed yet despite a lot of (mainly precision-related) work on period lattices leading up to 3.1.2.\n\nI'm not sure what benefits, if any, the class PeriodLattice_ell gains from being derived from FreeModule_generic_pid (via class PeriodLattice), but it means that len(dir(L)) is 210 so there's a lot of work to do implementing possibly trivial and possibly irrelevant things.\n\nThe issue is that a FreeModule_generic_pid seems to think that it's a submodule of some concrete module like `ZZ^n`, rather than being an abstract module;  functions like basis_matrix() make no sense in general.\n\nIf anyone can point out a method of FreeModule_generic_pid which PeriodLattice_ell should implement but does not, I would be happy to implement it.",
    "created_at": "2008-09-09T14:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12021",
    "user": "https://github.com/JohnCremona"
}
```

Just to confirm that none of this has changed yet despite a lot of (mainly precision-related) work on period lattices leading up to 3.1.2.

I'm not sure what benefits, if any, the class PeriodLattice_ell gains from being derived from FreeModule_generic_pid (via class PeriodLattice), but it means that len(dir(L)) is 210 so there's a lot of work to do implementing possibly trivial and possibly irrelevant things.

The issue is that a FreeModule_generic_pid seems to think that it's a submodule of some concrete module like `ZZ^n`, rather than being an abstract module;  functions like basis_matrix() make no sense in general.

If anyone can point out a method of FreeModule_generic_pid which PeriodLattice_ell should implement but does not, I would be happy to implement it.



---

archive/issue_comments_012022.json:
```json
{
    "body": "Just for the record: ticket #4388 goes some way towards fixing this by providing a basis_matrix() method for period lattices. This fixes all of the problems reported by was above, but several issues remain: for example, I can't seem to create any nonzero element of a period lattice -- the return values of basis() are plain complex numbers, not elements of the lattice, and attempting to coerce them back into the lattice fails.",
    "created_at": "2008-11-04T11:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12022",
    "user": "https://github.com/loefflerd"
}
```

Just for the record: ticket #4388 goes some way towards fixing this by providing a basis_matrix() method for period lattices. This fixes all of the problems reported by was above, but several issues remain: for example, I can't seem to create any nonzero element of a period lattice -- the return values of basis() are plain complex numbers, not elements of the lattice, and attempting to coerce them back into the lattice fails.



---

archive/issue_comments_012023.json:
```json
{
    "body": "You are right, David.  For me this class is just a sort of place-holder to hold the data needed for when you ask an elliptic curve about its periods and related things.  I never thought about it as a lattice in any precise sense.  (I did not create the class, by the way, but I have added to it -- for example, support for real embeddings of number fields, not just Q).\n\nFeel free to let it behave more sensibly for what you need by adding stuff!  John",
    "created_at": "2008-11-04T12:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12023",
    "user": "https://github.com/JohnCremona"
}
```

You are right, David.  For me this class is just a sort of place-holder to hold the data needed for when you ask an elliptic curve about its periods and related things.  I never thought about it as a lattice in any precise sense.  (I did not create the class, by the way, but I have added to it -- for example, support for real embeddings of number fields, not just Q).

Feel free to let it behave more sensibly for what you need by adding stuff!  John



---

archive/issue_comments_012024.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:06:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12024",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_012025.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T19:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12025",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_012026.json:
```json
{
    "body": "Assigned to new \"elliptic curves\" component.",
    "created_at": "2009-07-20T19:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12026",
    "user": "https://github.com/loefflerd"
}
```

Assigned to new "elliptic curves" component.



---

archive/issue_comments_012027.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T19:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12027",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_012028.json:
```json
{
    "body": "Remove assignee @loefflerd.",
    "created_at": "2009-10-09T09:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12028",
    "user": "https://github.com/loefflerd"
}
```

Remove assignee @loefflerd.



---

archive/issue_comments_012029.json:
```json
{
    "body": "Changing keywords from \"\" to \"ecc2011\".",
    "created_at": "2011-09-16T13:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12029",
    "user": "https://github.com/zimmermann6"
}
```

Changing keywords from "" to "ecc2011".



---

archive/issue_comments_012030.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2011-09-16T13:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12030",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_012031.json:
```json
{
    "body": "the examples in the description work with Sage 4.7.1:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: 9322\nsage: E = EllipticCurve('37a1')\nsage: Lambda = E.period_lattice()\nsage: OE = Lambda.omega(); OE\n5.98691729246392\nsage: Lambda.matrix()\n[ 2.99345864623196 0.000000000000000]\n[0.000000000000000  2.45138938198679]\nsage: Lambda.gram_matrix()\n[ 8.96079466670088 0.000000000000000]\n[0.000000000000000  6.00930990211758]\nsage: Lambda.basis()\n(2.99345864623196, 2.45138938198679*I)\nsage: Lambda.basis_matrix()\n[ 2.99345864623196 0.000000000000000]\n[0.000000000000000  2.45138938198679]\n```\n\nShould this ticket be closed?\n| Sage Version 4.7.1, Release Date: 2011-08-11                       |\n| Type notebook() for the GUI, and license() for information.        |\nPaul",
    "created_at": "2011-09-16T13:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12031",
    "user": "https://github.com/zimmermann6"
}
```

the examples in the description work with Sage 4.7.1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 9322
sage: E = EllipticCurve('37a1')
sage: Lambda = E.period_lattice()
sage: OE = Lambda.omega(); OE
5.98691729246392
sage: Lambda.matrix()
[ 2.99345864623196 0.000000000000000]
[0.000000000000000  2.45138938198679]
sage: Lambda.gram_matrix()
[ 8.96079466670088 0.000000000000000]
[0.000000000000000  6.00930990211758]
sage: Lambda.basis()
(2.99345864623196, 2.45138938198679*I)
sage: Lambda.basis_matrix()
[ 2.99345864623196 0.000000000000000]
[0.000000000000000  2.45138938198679]
```

Should this ticket be closed?
| Sage Version 4.7.1, Release Date: 2011-08-11                       |
| Type notebook() for the GUI, and license() for information.        |
Paul



---

archive/issue_comments_012032.json:
```json
{
    "body": "Replying to [comment:7 zimmerma]:\n\n> Should this ticket be closed?\n> \n> Paul\n\nIn my opinion, yes, but see the comments above by David Loeffler.",
    "created_at": "2011-09-16T13:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12032",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:7 zimmerma]:

> Should this ticket be closed?
> 
> Paul

In my opinion, yes, but see the comments above by David Loeffler.



---

archive/issue_comments_012033.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-09-16T13:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12033",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_012034.json:
```json
{
    "body": "I concur with the vote to close. Setting this to \"positive review\" to bring it to the notice of someone who has the authority to do so. -- David",
    "created_at": "2011-09-16T13:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12034",
    "user": "https://github.com/loefflerd"
}
```

I concur with the vote to close. Setting this to "positive review" to bring it to the notice of someone who has the authority to do so. -- David



---

archive/issue_comments_012035.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-09-16T13:48:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12035",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_012036.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-17T05:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1904#issuecomment-12036",
    "user": "https://github.com/nexttime"
}
```

Resolution: fixed
