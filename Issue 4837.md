# Issue 4837: implement random_element for number fields

archive/issues_004837.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nKeywords: random element number field\n\nAt the moment, if K is a number field then K.random_element() uses a generic implementation that simply returns a random *integer* coerced into K.  It would be useful to have a real implementation that returns an actual random element of K.\n\nA simple idea would be to find a primitive element j that generates K as a field extension over QQ, and to return a random polynomial of degree at most [K:QQ].  This should be easy since random polynomials in one variable are already implemented.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4837\n\n",
    "created_at": "2008-12-20T15:37:20Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "implement random_element for number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4837",
    "user": "AlexGhitza"
}
```
Assignee: AlexGhitza

Keywords: random element number field

At the moment, if K is a number field then K.random_element() uses a generic implementation that simply returns a random *integer* coerced into K.  It would be useful to have a real implementation that returns an actual random element of K.

A simple idea would be to find a primitive element j that generates K as a field extension over QQ, and to return a random polynomial of degree at most [K:QQ].  This should be easy since random polynomials in one variable are already implemented.


Issue created by migration from https://trac.sagemath.org/ticket/4837





---

archive/issue_comments_036668.json:
```json
{
    "body": "OK, the attached patch implements the simple idea given above.  More precisely: let a be a primitive element of K, then every element of K can be written as a polynomial of degree (at most) [K:QQ]-1 in the variable a, with rational coefficients.  Therefore the function returns a random polynomial of this type.",
    "created_at": "2008-12-20T16:40:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4837#issuecomment-36668",
    "user": "AlexGhitza"
}
```

OK, the attached patch implements the simple idea given above.  More precisely: let a be a primitive element of K, then every element of K can be written as a polynomial of degree (at most) [K:QQ]-1 in the variable a, with rational coefficients.  Therefore the function returns a random polynomial of this type.



---

archive/issue_comments_036669.json:
```json
{
    "body": "There are two obvious ways to implement this:  the one in the patch (random polynomial), or a random QQ_vector applied to the QQ_basis for the field.  I think I prefer the latter, though I am not sure why.  It would almost certainly be useful to have a random_integer() function too, implemented via a random ZZ-linear combination of the ZZ-basis.  The current patch could also be adapted, but with more difficulty (especially if the ring of integers is not of the form ZZ[a]).\n\nI don't know how easy the alternative approach would be to apply to relative extensions.  The current patch does fine, as long as computing a primitive element is not too time-consuming.\n\nThis patch applies cleanly to 3.2.2 and all tests in sage/rings/number_field pass, so I am happy to give it a positive review, while inviting comments on my comments!",
    "created_at": "2008-12-21T17:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4837#issuecomment-36669",
    "user": "cremona"
}
```

There are two obvious ways to implement this:  the one in the patch (random polynomial), or a random QQ_vector applied to the QQ_basis for the field.  I think I prefer the latter, though I am not sure why.  It would almost certainly be useful to have a random_integer() function too, implemented via a random ZZ-linear combination of the ZZ-basis.  The current patch could also be adapted, but with more difficulty (especially if the ring of integers is not of the form ZZ[a]).

I don't know how easy the alternative approach would be to apply to relative extensions.  The current patch does fine, as long as computing a primitive element is not too time-consuming.

This patch applies cleanly to 3.2.2 and all tests in sage/rings/number_field pass, so I am happy to give it a positive review, while inviting comments on my comments!



---

archive/issue_comments_036670.json:
```json
{
    "body": "Hi John,\n\nHere's a third possibility: any field extension L/K is really a quotient K[x]/(f(x)), so we can start with a random element of K[x] and reduce it mod f(x).  Getting a random element of K[x] is easy if we can get random elements of K itself.  If L is an absolute number field, then K=QQ and we're in business; if L/K is a relative number field, then this will \"descend\" to K and so on until it hits QQ.\n\nThe advantage of this approach is that it is very transparent and easy to code.  Also in the relative situation there is no need to compute a primitive element, all we need are the splitting polynomials for each step in the tower, and those are just part of the given data.\n\nI agree with the suggestion that we should be able to produce random algebraic integers as well.  But I think this should be implemented as a method random_element() of an order in a number field, rather than as a method of the number field itself.  And then your idea of using the ZZ-basis is really the only option I can think of.",
    "created_at": "2008-12-22T06:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4837#issuecomment-36670",
    "user": "AlexGhitza"
}
```

Hi John,

Here's a third possibility: any field extension L/K is really a quotient K[x]/(f(x)), so we can start with a random element of K[x] and reduce it mod f(x).  Getting a random element of K[x] is easy if we can get random elements of K itself.  If L is an absolute number field, then K=QQ and we're in business; if L/K is a relative number field, then this will "descend" to K and so on until it hits QQ.

The advantage of this approach is that it is very transparent and easy to code.  Also in the relative situation there is no need to compute a primitive element, all we need are the splitting polynomials for each step in the tower, and those are just part of the given data.

I agree with the suggestion that we should be able to produce random algebraic integers as well.  But I think this should be implemented as a method random_element() of an order in a number field, rather than as a method of the number field itself.  And then your idea of using the ZZ-basis is really the only option I can think of.



---

archive/issue_comments_036671.json:
```json
{
    "body": "I fully agree:  use the existing method for absolute fields (where there's essentially no need to find a primitive element), use the recursive method for relative extensions, and make a new ticket for random elements of orders (and fractional ideals while we're at it) which will use Z-bases.\n\nWill you be adapting the current patch accordingly?",
    "created_at": "2008-12-22T09:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4837#issuecomment-36671",
    "user": "cremona"
}
```

I fully agree:  use the existing method for absolute fields (where there's essentially no need to find a primitive element), use the recursive method for relative extensions, and make a new ticket for random elements of orders (and fractional ideals while we're at it) which will use Z-bases.

Will you be adapting the current patch accordingly?



---

archive/issue_comments_036672.json:
```json
{
    "body": "Good.  I will modify the patch to use this strategy and resubmit it.",
    "created_at": "2008-12-22T10:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4837#issuecomment-36672",
    "user": "AlexGhitza"
}
```

Good.  I will modify the patch to use this strategy and resubmit it.



---

archive/issue_comments_036673.json:
```json
{
    "body": "Alex, I just noticed that you can do this in one line with \n\nK(K.polynomial_ring().random_element(degree=K.degree()-1))\n\nsince K.polynomial_ring is *not* K[x] but is the polynomial ring over K's base field, whatever that is.  So this will automatically work ok recursively, given that the random_element() method for polynomial rings uses the random_element() method for the coefficient ring.\n\nJohn",
    "created_at": "2008-12-22T16:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4837#issuecomment-36673",
    "user": "cremona"
}
```

Alex, I just noticed that you can do this in one line with 

K(K.polynomial_ring().random_element(degree=K.degree()-1))

since K.polynomial_ring is *not* K[x] but is the polynomial ring over K's base field, whatever that is.  So this will automatically work ok recursively, given that the random_element() method for polynomial rings uses the random_element() method for the coefficient ring.

John



---

archive/issue_comments_036674.json:
```json
{
    "body": "Attachment [trac_4837.patch](tarball://root/attachments/some-uuid/ticket4837/trac_4837.patch) by AlexGhitza created at 2008-12-23 11:12:15\n\ndepends on the patch at #4218",
    "created_at": "2008-12-23T11:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4837#issuecomment-36674",
    "user": "AlexGhitza"
}
```

Attachment [trac_4837.patch](tarball://root/attachments/some-uuid/ticket4837/trac_4837.patch) by AlexGhitza created at 2008-12-23 11:12:15

depends on the patch at #4218



---

archive/issue_comments_036675.json:
```json
{
    "body": "Following the discussion at\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/67b40b64970bbf19\nI implemented coercion of elements from the isomorphic polynomial quotient ring to the number field.  As a consequence of this and the code for random elements of quotient rings at #4218, random_element() for number fields became a fairly trivial one-liner.\n\nSee the attached patch.  It is advisable to first merge the patch at #4218.",
    "created_at": "2008-12-23T11:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4837#issuecomment-36675",
    "user": "AlexGhitza"
}
```

Following the discussion at
http://groups.google.com/group/sage-devel/browse_thread/thread/67b40b64970bbf19
I implemented coercion of elements from the isomorphic polynomial quotient ring to the number field.  As a consequence of this and the code for random elements of quotient rings at #4218, random_element() for number fields became a fairly trivial one-liner.

See the attached patch.  It is advisable to first merge the patch at #4218.



---

archive/issue_comments_036676.json:
```json
{
    "body": "The patch applies fine (over 3.2.2 + #4218).  Just one thing:  for an absolute extension we can create an element from a polynomial over the base field, but not for a relative extension:\n\n```\nsage: K.<z>=CyclotomicField(7)\nsage: Ky.<y>=PolynomialRing(K)\nsage: L.<a>=K.extension(y^2+1)\nsage: K(K.polynomial_ring().random_element())\nz + 1\nsage: L(L.polynomial_ring().random_element())\n---------------------------------------------------------------------------\nTypeError           \n...\nTypeError: Unable to coerce 7/2*z^5 + 1/2*z^4 + z^3 - 37/2*z to a rational\n```\n\nI'm sure this will cause complaints before long, so can we make the new constructor slightly more flexible?  Of course if your replace `polynomial_ring()` with `polynomial_quotient_ring()` it works fine thanks to the new code.",
    "created_at": "2008-12-23T12:44:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4837#issuecomment-36676",
    "user": "cremona"
}
```

The patch applies fine (over 3.2.2 + #4218).  Just one thing:  for an absolute extension we can create an element from a polynomial over the base field, but not for a relative extension:

```
sage: K.<z>=CyclotomicField(7)
sage: Ky.<y>=PolynomialRing(K)
sage: L.<a>=K.extension(y^2+1)
sage: K(K.polynomial_ring().random_element())
z + 1
sage: L(L.polynomial_ring().random_element())
---------------------------------------------------------------------------
TypeError           
...
TypeError: Unable to coerce 7/2*z^5 + 1/2*z^4 + z^3 - 37/2*z to a rational
```

I'm sure this will cause complaints before long, so can we make the new constructor slightly more flexible?  Of course if your replace `polynomial_ring()` with `polynomial_quotient_ring()` it works fine thanks to the new code.



---

archive/issue_comments_036677.json:
```json
{
    "body": "I was hoping to be able to take care of this quickly, but I keep running into brick walls.  I agree that it should be fixed though, and I've opened a new ticket for it, see #4869.",
    "created_at": "2008-12-24T12:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4837#issuecomment-36677",
    "user": "AlexGhitza"
}
```

I was hoping to be able to take care of this quickly, but I keep running into brick walls.  I agree that it should be fixed though, and I've opened a new ticket for it, see #4869.



---

archive/issue_comments_036678.json:
```json
{
    "body": "OK, given the new ticket I'm happy to give this the positive review it has been waiting for.  Sorry to be fussy, Alex!",
    "created_at": "2008-12-24T14:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4837#issuecomment-36678",
    "user": "cremona"
}
```

OK, given the new ticket I'm happy to give this the positive review it has been waiting for.  Sorry to be fussy, Alex!



---

archive/issue_comments_036679.json:
```json
{
    "body": "Replying to [comment:11 cremona]:\n> Sorry to be fussy, Alex!\n\nNo need to apologise, I quite appreciate a careful reviewing; in this instance, I had noticed the problem with polynomial rings earlier in the process, but since it wasn't the main point I put it aside, then forgot about it.  This way we have it properly reported.",
    "created_at": "2008-12-25T08:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4837#issuecomment-36679",
    "user": "AlexGhitza"
}
```

Replying to [comment:11 cremona]:
> Sorry to be fussy, Alex!

No need to apologise, I quite appreciate a careful reviewing; in this instance, I had noticed the problem with polynomial rings earlier in the process, but since it wasn't the main point I put it aside, then forgot about it.  This way we have it properly reported.



---

archive/issue_comments_036680.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-12T01:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4837#issuecomment-36680",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_comments_036681.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-12T01:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4837#issuecomment-36681",
    "user": "mabshoff"
}
```

Resolution: fixed
