# Issue 9320: Implement root numbers for elliptic curves over number fields

archive/issues_009320.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  @williamstein cturner beankao @pjbruin @JohnCremona\n\nKeywords: root number\n\nRoot numbers for elliptic curves are currently only implemented via Pari (pari(E).ellrootno()) and only over the rational numbers.\n\nWe (Tim Dokchitser's group at Sage Days 22) intend to add the possibility to compute local and global root numbers for elliptic curves over number fields.  A first patch may not fully implement the case of additive reduction over primes dividing 2 or 3.\n\nUpdate: Attached is a first implementation which allows for instance:\n\n```\nsage: K.<a>=NumberField(x^4+2)\nsage: E = EllipticCurve(K, [1, a, 0, 1+a, 0])\nsage: E.root_number()\n1\nsage: E.root_number(K.ideal(a+1))\n1\n```\n\nNote that the implementation needs the patches #9334 (Hilbert symbol) and #9684 (\"dirty model\") to be applied.\n\nTo prevent incorrect results in some cases as well as crashes, the tickets #9389 and #9417 need to be addressed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9320\n\n",
    "created_at": "2010-06-23T22:14:38Z",
    "labels": [
        "component: elliptic curves",
        "minor"
    ],
    "title": "Implement root numbers for elliptic curves over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9320",
    "user": "https://github.com/arminstraub"
}
```
Assignee: @JohnCremona

CC:  @williamstein cturner beankao @pjbruin @JohnCremona

Keywords: root number

Root numbers for elliptic curves are currently only implemented via Pari (pari(E).ellrootno()) and only over the rational numbers.

We (Tim Dokchitser's group at Sage Days 22) intend to add the possibility to compute local and global root numbers for elliptic curves over number fields.  A first patch may not fully implement the case of additive reduction over primes dividing 2 or 3.

Update: Attached is a first implementation which allows for instance:

```
sage: K.<a>=NumberField(x^4+2)
sage: E = EllipticCurve(K, [1, a, 0, 1+a, 0])
sage: E.root_number()
1
sage: E.root_number(K.ideal(a+1))
1
```

Note that the implementation needs the patches #9334 (Hilbert symbol) and #9684 ("dirty model") to be applied.

To prevent incorrect results in some cases as well as crashes, the tickets #9389 and #9417 need to be addressed.

Issue created by migration from https://trac.sagemath.org/ticket/9320





---

archive/issue_comments_087684.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-10T11:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87684",
    "user": "https://github.com/arminstraub"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087685.json:
```json
{
    "body": "I don't think it is possible to review this until the ticket it depends on (#9334) which needs work has been fixed.",
    "created_at": "2010-08-11T19:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87685",
    "user": "https://github.com/JohnCremona"
}
```

I don't think it is possible to review this until the ticket it depends on (#9334) which needs work has been fixed.



---

archive/issue_comments_087686.json:
```json
{
    "body": "Attachment [9320_root_numbers.patch](tarball://root/attachments/some-uuid/ticket9320/9320_root_numbers.patch) by @arminstraub created at 2010-08-13 00:32:26\n\nrequires #9334 and #9684",
    "created_at": "2010-08-13T00:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87686",
    "user": "https://github.com/arminstraub"
}
```

Attachment [9320_root_numbers.patch](tarball://root/attachments/some-uuid/ticket9320/9320_root_numbers.patch) by @arminstraub created at 2010-08-13 00:32:26

requires #9334 and #9684



---

archive/issue_comments_087687.json:
```json
{
    "body": "Adapted the patch to reflect the renaming of \"tidy\" to \"reduce\" following #9684.",
    "created_at": "2010-08-13T00:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87687",
    "user": "https://github.com/arminstraub"
}
```

Adapted the patch to reflect the renaming of "tidy" to "reduce" following #9684.



---

archive/issue_comments_087688.json:
```json
{
    "body": "Rebased to 4.8.alpha5",
    "created_at": "2011-12-30T17:59:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87688",
    "user": "https://github.com/loefflerd"
}
```

Rebased to 4.8.alpha5



---

archive/issue_comments_087689.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-12-30T18:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87689",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087690.json:
```json
{
    "body": "Attachment [9320_root_numbers-rebase.patch](tarball://root/attachments/some-uuid/ticket9320/9320_root_numbers-rebase.patch) by @loefflerd created at 2011-12-30 18:09:53\n\nTicket #9334 has been merged, so this is now ready for review. Sadly it fails to apply, due to a trivial conflict with #11749. I've uploaded a rebased patch, and checked that all doctests in sage/schemes/elliptic_curves pass with this applied. \n\nHowever, some (trivial but tedious) work is needed fixing the ReST formatting of the docstrings -- the indentation is all over the place, and :: should only be used to introduce example code blocks.",
    "created_at": "2011-12-30T18:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87690",
    "user": "https://github.com/loefflerd"
}
```

Attachment [9320_root_numbers-rebase.patch](tarball://root/attachments/some-uuid/ticket9320/9320_root_numbers-rebase.patch) by @loefflerd created at 2011-12-30 18:09:53

Ticket #9334 has been merged, so this is now ready for review. Sadly it fails to apply, due to a trivial conflict with #11749. I've uploaded a rebased patch, and checked that all doctests in sage/schemes/elliptic_curves pass with this applied. 

However, some (trivial but tedious) work is needed fixing the ReST formatting of the docstrings -- the indentation is all over the place, and :: should only be used to introduce example code blocks.



---

archive/issue_comments_087691.json:
```json
{
    "body": "Attachment [9320_root_numbers-rebase_docscleaned.patch](tarball://root/attachments/some-uuid/ticket9320/9320_root_numbers-rebase_docscleaned.patch) by cturner created at 2012-01-13 14:15:42\n\ndocstrings improved",
    "created_at": "2012-01-13T14:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87691",
    "user": "https://trac.sagemath.org/admin/accounts/users/cturner"
}
```

Attachment [9320_root_numbers-rebase_docscleaned.patch](tarball://root/attachments/some-uuid/ticket9320/9320_root_numbers-rebase_docscleaned.patch) by cturner created at 2012-01-13 14:15:42

docstrings improved



---

archive/issue_comments_087692.json:
```json
{
    "body": "I have tried to clean this up, but I'm not very experienced so I may have made some mistakes or missed something - could someone please have a look and help me to get it right?",
    "created_at": "2012-01-13T14:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87692",
    "user": "https://trac.sagemath.org/admin/accounts/users/cturner"
}
```

I have tried to clean this up, but I'm not very experienced so I may have made some mistakes or missed something - could someone please have a look and help me to get it right?



---

archive/issue_comments_087693.json:
```json
{
    "body": "apply only 9320_root_numbers-rebase_docscleaned.patch",
    "created_at": "2013-08-22T17:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87693",
    "user": "https://github.com/fchapoton"
}
```

apply only 9320_root_numbers-rebase_docscleaned.patch



---

archive/issue_comments_087694.json:
```json
{
    "body": "apply only 9320_root_numbers-rebase_docscleaned.patch",
    "created_at": "2013-08-22T17:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87694",
    "user": "https://github.com/fchapoton"
}
```

apply only 9320_root_numbers-rebase_docscleaned.patch



---

archive/issue_comments_087695.json:
```json
{
    "body": "seems to apply and pass all tests on 5.12.beta2\n\nneeds work to put coverage to 100%",
    "created_at": "2013-08-22T17:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87695",
    "user": "https://github.com/fchapoton"
}
```

seems to apply and pass all tests on 5.12.beta2

needs work to put coverage to 100%



---

archive/issue_comments_087696.json:
```json
{
    "body": "this one just needs a little more doc (three functions need doctests)",
    "created_at": "2013-12-06T20:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87696",
    "user": "https://github.com/fchapoton"
}
```

this one just needs a little more doc (three functions need doctests)



---

archive/issue_comments_087697.json:
```json
{
    "body": "Here is a git branch\n\n---\nNew commits:",
    "created_at": "2014-03-15T09:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87697",
    "user": "https://github.com/fchapoton"
}
```

Here is a git branch

---
New commits:



---

archive/issue_comments_087698.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-16T13:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87698",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087699.json:
```json
{
    "body": "It would be good if some expert of elliptic curve could provide correct doctests for the local root numbers at primes 2 and 3. Could you have a look, please ?",
    "created_at": "2014-03-16T13:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87699",
    "user": "https://github.com/fchapoton"
}
```

It would be good if some expert of elliptic curve could provide correct doctests for the local root numbers at primes 2 and 3. Could you have a look, please ?



---

archive/issue_comments_087700.json:
```json
{
    "body": "I suggest that a good source of examples would be elliptic curves over number fields where we know the associated modular form, since the root number at a bad prime should match the Atkin-Lehner eigenvalue.  (The alternative would be to compue a whole lot of examples with Magma, but that would make me uncomfortable;  nevertheless we should of course check that our results are compatible with Magma.)\n\nThere is no issue when the primes have multiplicative reduction, since then the root number is very easy being minus E.ap, i.e. depends only on whether the number of points on the reduction is p+1 or p-1 (of course \"p\" means Norm(p) in the number field case).  It's the case of additive reduction at primes dividing 2 or 3 which are harder.\n\nHere is one taken from my thesis (see http://www.numdam.org/numdam-bin/search?h=nc&id=CM_1984__51_3_275_0&format=complete):\n\n```\nK.<i>=QuadraticField(-1)\nE=EllipticCurve([1+i, 1+i, 0,i,0])\nP2=K.ideal(i+i)\nE.root_number(P2)\n-1\n```\nwhich I checked with Magma.  The conductor here is `P2^2 * P41`.\n\nIs this what you want?  How many examples do you need?\n\n\nTables of elliptic curves over number fields do exist, and were in fact one of the topics of last week's Curves and Automorphic Forms workshop in Arizona.",
    "created_at": "2014-03-18T09:58:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87700",
    "user": "https://github.com/JohnCremona"
}
```

I suggest that a good source of examples would be elliptic curves over number fields where we know the associated modular form, since the root number at a bad prime should match the Atkin-Lehner eigenvalue.  (The alternative would be to compue a whole lot of examples with Magma, but that would make me uncomfortable;  nevertheless we should of course check that our results are compatible with Magma.)

There is no issue when the primes have multiplicative reduction, since then the root number is very easy being minus E.ap, i.e. depends only on whether the number of points on the reduction is p+1 or p-1 (of course "p" means Norm(p) in the number field case).  It's the case of additive reduction at primes dividing 2 or 3 which are harder.

Here is one taken from my thesis (see http://www.numdam.org/numdam-bin/search?h=nc&id=CM_1984__51_3_275_0&format=complete):

```
K.<i>=QuadraticField(-1)
E=EllipticCurve([1+i, 1+i, 0,i,0])
P2=K.ideal(i+i)
E.root_number(P2)
-1
```
which I checked with Magma.  The conductor here is `P2^2 * P41`.

Is this what you want?  How many examples do you need?


Tables of elliptic curves over number fields do exist, and were in fact one of the topics of last week's Curves and Automorphic Forms workshop in Arizona.



---

archive/issue_comments_087701.json:
```json
{
    "body": "One example would be enough, I think if it is bad at both 2 and 3. Maybe one can just use the one above as \"indirect doctest\" ?\n\nDo you really mean `K.ideal(i+i)` ?",
    "created_at": "2014-03-18T11:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87701",
    "user": "https://github.com/fchapoton"
}
```

One example would be enough, I think if it is bad at both 2 and 3. Maybe one can just use the one above as "indirect doctest" ?

Do you really mean `K.ideal(i+i)` ?



---

archive/issue_comments_087702.json:
```json
{
    "body": "Replying to [comment:14 chapoton]:\n> One example would be enough, I think if it is bad at both 2 and 3. Maybe one can just use the one above as \"indirect doctest\" ?\n> \n\nI'll find another example at 3.  I don't know the code but I expect that it also depends on factors such as the ramification degree of the prime, so I'll give an example over Q(sqrt-3) with additive reduction at 3.  Wait for it...\n\n> Do you really mean `K.ideal(i+i)` ?\n\nYes",
    "created_at": "2014-03-18T13:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87702",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:14 chapoton]:
> One example would be enough, I think if it is bad at both 2 and 3. Maybe one can just use the one above as "indirect doctest" ?
> 

I'll find another example at 3.  I don't know the code but I expect that it also depends on factors such as the ramification degree of the prime, so I'll give an example over Q(sqrt-3) with additive reduction at 3.  Wait for it...

> Do you really mean `K.ideal(i+i)` ?

Yes



---

archive/issue_comments_087703.json:
```json
{
    "body": "An example which is additive at 3:\n\n```\nsage: K.<r> = NumberField(x^2-x+1)\nsage: E = EllipticCurve([r-1,r,1,r-1,-1])\nsage: P3 = K.ideal(2*r-1)\nsage: assert P3.is_prime() and P3.norm()==3\nsage: assert E.has_additive_reduction(P3)\nsage: assert P.root_number(P3)==1 ## not implemented\n```\nHere the value is taken from page 115 of my thesis, and agrees with Magma's value.\n\nFor additional testing we could put in an 'algorithm' parameter which could be 'magma' and then (of course) only work when Magma is installed, so you could have optional doctests conditional on Magma of the form\n\n```\nassert E.root_number(P) == E.root_number(P, algorithm='magma')\n```",
    "created_at": "2014-03-18T13:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87703",
    "user": "https://github.com/JohnCremona"
}
```

An example which is additive at 3:

```
sage: K.<r> = NumberField(x^2-x+1)
sage: E = EllipticCurve([r-1,r,1,r-1,-1])
sage: P3 = K.ideal(2*r-1)
sage: assert P3.is_prime() and P3.norm()==3
sage: assert E.has_additive_reduction(P3)
sage: assert P.root_number(P3)==1 ## not implemented
```
Here the value is taken from page 115 of my thesis, and agrees with Magma's value.

For additional testing we could put in an 'algorithm' parameter which could be 'magma' and then (of course) only work when Magma is installed, so you could have optional doctests conditional on Magma of the form

```
assert E.root_number(P) == E.root_number(P, algorithm='magma')
```



---

archive/issue_comments_087704.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-18T15:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87704",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087705.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-18T15:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87705",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087706.json:
```json
{
    "body": "Thanks a lot for the examples. I have done what I could for this code, but there is now a failing doctest for the example you provided which has additive reduction at 2.\n\nAnd I had to replace `K.ideal(i+i)` by `K.ideal(1+i)` ...\n\nNot being in my field of expertise, I will now leave this ticket in more able hands.",
    "created_at": "2014-03-18T15:58:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87706",
    "user": "https://github.com/fchapoton"
}
```

Thanks a lot for the examples. I have done what I could for this code, but there is now a failing doctest for the example you provided which has additive reduction at 2.

And I had to replace `K.ideal(i+i)` by `K.ideal(1+i)` ...

Not being in my field of expertise, I will now leave this ticket in more able hands.



---

archive/issue_comments_087707.json:
```json
{
    "body": "I had a quick look at this and there are indeed major issues with the local root number at places above 2 when the reduction is additive, potentially good. That is in the function `_root_number_local_2` in `ell_number_field.py`.\n\nWith the current commit above we get an error for\n\n```\nsage: K.<i> = QuadraticField(-1)\nsage: E = EllipticCurve([1+i, 1+i, 0, i, 0])\nsage: P2 = K.ideal(1+i)\nsage: E.root_number(P2)\n```\n\nbecause line 1966 tries to create and extension with a reducible polynomial `K2 = K.extension(t**2+E.a2()*t+E.a4(), 'a2')`. I guess - but it would take me some time to read the sources - that K2 should just be K in this case.\n\nHowever there are other issues. For instance\n  \n```\nsage: E = EllipticCurve([1+i,0,0,0,i])\nsage: E._root_number_local_2(P2)\n```\n\ngoes \"bang\".\n\nI would think the code without the very bad case at places above 2 is ok and that could already go in. So I see two possible futures for this ticket:\n\n1. Someone fixes these issues above 2 or\n\n2. We raise an `NotImplementedError` if the reduction is additive and potentially good at a place above 2 and open a new ticket for fixing the problem.\n\nI can help with 2), but I won't have time to do 1). But maybe there is someone out there who would.",
    "created_at": "2014-03-31T13:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87707",
    "user": "https://github.com/categorie"
}
```

I had a quick look at this and there are indeed major issues with the local root number at places above 2 when the reduction is additive, potentially good. That is in the function `_root_number_local_2` in `ell_number_field.py`.

With the current commit above we get an error for

```
sage: K.<i> = QuadraticField(-1)
sage: E = EllipticCurve([1+i, 1+i, 0, i, 0])
sage: P2 = K.ideal(1+i)
sage: E.root_number(P2)
```

because line 1966 tries to create and extension with a reducible polynomial `K2 = K.extension(t**2+E.a2()*t+E.a4(), 'a2')`. I guess - but it would take me some time to read the sources - that K2 should just be K in this case.

However there are other issues. For instance
  
```
sage: E = EllipticCurve([1+i,0,0,0,i])
sage: E._root_number_local_2(P2)
```

goes "bang".

I would think the code without the very bad case at places above 2 is ok and that could already go in. So I see two possible futures for this ticket:

1. Someone fixes these issues above 2 or

2. We raise an `NotImplementedError` if the reduction is additive and potentially good at a place above 2 and open a new ticket for fixing the problem.

I can help with 2), but I won't have time to do 1). But maybe there is someone out there who would.



---

archive/issue_comments_087708.json:
```json
{
    "body": "It all started a long time ago, at the Sage Days & summer school at MSRI.  Perhaps we good get Tim Dokchitser, who led the original project (and who developed the background theory, I think) involved?  He works mainly in Magma, but back in 2010 he certainly was involved with this.",
    "created_at": "2014-03-31T13:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87708",
    "user": "https://github.com/JohnCremona"
}
```

It all started a long time ago, at the Sage Days & summer school at MSRI.  Perhaps we good get Tim Dokchitser, who led the original project (and who developed the background theory, I think) involved?  He works mainly in Magma, but back in 2010 he certainly was involved with this.



---

archive/issue_comments_087709.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-07-09T12:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87709",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087710.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-07-09T13:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87710",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087711.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-10-28T20:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87711",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087712.json:
```json
{
    "body": "Sorry, I reverted that. Tim did not touch much of the code himself as far as I can remember that long long time ago in Berkley. I doubt he would want to vouch for this code by himself...",
    "created_at": "2015-10-29T09:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87712",
    "user": "https://github.com/categorie"
}
```

Sorry, I reverted that. Tim did not touch much of the code himself as far as I can remember that long long time ago in Berkley. I doubt he would want to vouch for this code by himself...



---

archive/issue_comments_087713.json:
```json
{
    "body": "Instead of reverting, at least fix it.",
    "created_at": "2015-10-29T09:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87713",
    "user": "https://github.com/jdemeyer"
}
```

Instead of reverting, at least fix it.



---

archive/issue_comments_087714.json:
```json
{
    "body": "What is the issue ? Why can't you leave the original string in there ?",
    "created_at": "2015-10-29T09:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87714",
    "user": "https://github.com/categorie"
}
```

What is the issue ? Why can't you leave the original string in there ?



---

archive/issue_comments_087715.json:
```json
{
    "body": "Because \"Tim Dokchitser and group (Sage Days 22)\" isn't an actual person.",
    "created_at": "2015-10-29T10:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87715",
    "user": "https://github.com/jdemeyer"
}
```

Because "Tim Dokchitser and group (Sage Days 22)" isn't an actual person.



---

archive/issue_comments_087716.json:
```json
{
    "body": "But it was a collaborative effort. The wiki for the sage days lists the participants in this group as \"Armin, Charlie, Hatice, Christ, Lola, Robert Miller, Thilina, M. Tip, Robert Bradshaw \" I am not sure who actually did the coding and I don't remember all full names. So the original string was probably the closest to who the author was. Otherwise set it to Armin Straub, who did the original uploading onto this trac ticket.",
    "created_at": "2015-10-29T10:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87716",
    "user": "https://github.com/categorie"
}
```

But it was a collaborative effort. The wiki for the sage days lists the participants in this group as "Armin, Charlie, Hatice, Christ, Lola, Robert Miller, Thilina, M. Tip, Robert Bradshaw " I am not sure who actually did the coding and I don't remember all full names. So the original string was probably the closest to who the author was. Otherwise set it to Armin Straub, who did the original uploading onto this trac ticket.



---

archive/issue_comments_087717.json:
```json
{
    "body": "there are some failing doctests..",
    "created_at": "2015-10-29T20:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87717",
    "user": "https://github.com/fchapoton"
}
```

there are some failing doctests..



---

archive/issue_comments_087718.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-01T11:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87718",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087719.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-05T17:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87719",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087720.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-05T18:14:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87720",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087721.json:
```json
{
    "body": "Could some expert in elliptic curves have a look at the last failing doctest, please ?",
    "created_at": "2016-03-06T13:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87721",
    "user": "https://github.com/fchapoton"
}
```

Could some expert in elliptic curves have a look at the last failing doctest, please ?



---

archive/issue_comments_087722.json:
```json
{
    "body": "I can simply repeat my comment:20 above. This is a genuine bug. \n\nMy favourite solution is still to raise non implemented warnings for the cases this code does not do currently.\n\nBefore accepting this ticket, the reviewer will have to do lots of comparison with magma. The code in magma will have plenty less bugs than this one as the Dokchitsers have worked a lot on that code.",
    "created_at": "2016-03-07T16:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87722",
    "user": "https://github.com/categorie"
}
```

I can simply repeat my comment:20 above. This is a genuine bug. 

My favourite solution is still to raise non implemented warnings for the cases this code does not do currently.

Before accepting this ticket, the reviewer will have to do lots of comparison with magma. The code in magma will have plenty less bugs than this one as the Dokchitsers have worked a lot on that code.



---

archive/issue_comments_087723.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-10T20:53:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87723",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087724.json:
```json
{
    "body": "I tried to fix the problem, but only with partial success. It seems that at some point\nthe code assumes vanishing of coeff a1 in long Weierstrass equation, and I cannot see why.",
    "created_at": "2016-03-10T20:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87724",
    "user": "https://github.com/fchapoton"
}
```

I tried to fix the problem, but only with partial success. It seems that at some point
the code assumes vanishing of coeff a1 in long Weierstrass equation, and I cannot see why.



---

archive/issue_comments_087725.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-29T18:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87725",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087726.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-09-14T12:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87726",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087727.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-01-04T15:58:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87727",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087728.json:
```json
{
    "body": "Merged with 8.6.beta1\n\n---\nNew commits:",
    "created_at": "2019-01-05T09:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87728",
    "user": "https://github.com/JohnCremona"
}
```

Merged with 8.6.beta1

---
New commits:



---

archive/issue_comments_087729.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2019-01-09T09:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87729",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087730.json:
```json
{
    "body": "After merging with 8.6.beta1 I ran the tests, and there is one failure in line 2294 of ell_number_field where a local root number at a ramified prime above 2 where there is additive reduction is computed incorrectly.\n\nI checked with Magma that -1 is the correct value.  This curve is http://beta.lmfdb.org/EllipticCurve/2.0.4.1/164.2/a/2 and has associated Bianchi newform http://beta.lmfdb.org/ModularForm/GL2/ImaginaryQuadratic/2.0.4.1/164.2/a/ where you can see that the Atkin-Lehner eigenvalue at 1+i is -1, giving a second independent evaluation.",
    "created_at": "2019-01-09T09:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9320#issuecomment-87730",
    "user": "https://github.com/JohnCremona"
}
```

After merging with 8.6.beta1 I ran the tests, and there is one failure in line 2294 of ell_number_field where a local root number at a ramified prime above 2 where there is additive reduction is computed incorrectly.

I checked with Magma that -1 is the correct value.  This curve is http://beta.lmfdb.org/EllipticCurve/2.0.4.1/164.2/a/2 and has associated Bianchi newform http://beta.lmfdb.org/ModularForm/GL2/ImaginaryQuadratic/2.0.4.1/164.2/a/ where you can see that the Atkin-Lehner eigenvalue at 1+i is -1, giving a second independent evaluation.
