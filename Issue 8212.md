# Issue 8212: arithmetic on GF(2^n) might be improved

archive/issues_008212.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nThe default polynomials chosen by Sage to perform arithmetic over\nGF(2**n) have sometimes Hamming weight 7 or more, which is not optimal.\nConsider for example:\n\n```\nsage: T.<a> = GF(2^211)\nsage: T.modulus()\nx^211 + x^9 + x^6 + x^5 + x^3 + x + 1\n\ndef bar(n):\n   f = a\n   for i in range(n):\n      f = f^2\n   return f\n\nsage: %timeit bar(10000)\n5 loops, best of 3: 88.5 ms per loop\n```\n\nWith the following pentanomial, we get a nice speedup:\n\n```\nsage: R.<x> = PolynomialRing(GF(2))\nsage: T.<a> = GF(2^211,name='a',modulus=x^211 + x^11 + x^10 + x^8 + 1)\n\nsage: %timeit bar(10000)\n5 loops, best of 3: 57.3 ms per loop\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8212\n\n",
    "created_at": "2010-02-08T07:06:33Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "arithmetic on GF(2^n) might be improved",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8212",
    "user": "zimmerma"
}
```
Assignee: AlexGhitza

The default polynomials chosen by Sage to perform arithmetic over
GF(2**n) have sometimes Hamming weight 7 or more, which is not optimal.
Consider for example:

```
sage: T.<a> = GF(2^211)
sage: T.modulus()
x^211 + x^9 + x^6 + x^5 + x^3 + x + 1

def bar(n):
   f = a
   for i in range(n):
      f = f^2
   return f

sage: %timeit bar(10000)
5 loops, best of 3: 88.5 ms per loop
```

With the following pentanomial, we get a nice speedup:

```
sage: R.<x> = PolynomialRing(GF(2))
sage: T.<a> = GF(2^211,name='a',modulus=x^211 + x^11 + x^10 + x^8 + 1)

sage: %timeit bar(10000)
5 loops, best of 3: 57.3 ms per loop
```


Issue created by migration from https://trac.sagemath.org/ticket/8212





---

archive/issue_comments_072417.json:
```json
{
    "body": "The polynomials used are Conway's polynomials I guess, probably to stick with Magma's behaviour:\nhttp://magma.maths.usyd.edu.au/magma/htmlhelp/text287.htm#1625 .",
    "created_at": "2010-02-08T11:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8212#issuecomment-72417",
    "user": "ylchapuy"
}
```

The polynomials used are Conway's polynomials I guess, probably to stick with Magma's behaviour:
http://magma.maths.usyd.edu.au/magma/htmlhelp/text287.htm#1625 .



---

archive/issue_comments_072418.json:
```json
{
    "body": "> The polynomials used are Conway's polynomials[...]\n\nthanks for the explanation. Would it make sense to have an option GF(p<sup>n</sup>,minimalWeight=true)\nto produce a polynomial of minimal weight?\n\nPaul",
    "created_at": "2010-02-08T12:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8212#issuecomment-72418",
    "user": "zimmerma"
}
```

> The polynomials used are Conway's polynomials[...]

thanks for the explanation. Would it make sense to have an option GF(p<sup>n</sup>,minimalWeight=true)
to produce a polynomial of minimal weight?

Paul



---

archive/issue_comments_072419.json:
```json
{
    "body": "Here is a proposal. It does the job only for fields GF(2^n) implemented with NTL.\n\nYann",
    "created_at": "2010-02-08T15:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8212#issuecomment-72419",
    "user": "ylchapuy"
}
```

Here is a proposal. It does the job only for fields GF(2^n) implemented with NTL.

Yann



---

archive/issue_comments_072420.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-08T15:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8212#issuecomment-72420",
    "user": "ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072421.json:
```json
{
    "body": "> Here is a proposal.\n\ngreat! A few remarks before a complete review: (i) it would be best to write Conway instead of\nconway (maybe except for the option name, if small letters are mandatory); (ii) I get an error\nfor 2<sup>n</sup> for 2 <= n <= 15:\n\n```\nsage:    T.<a> = GF(2^2, modulus='conway')\n...\nTypeError: Cannot understand modulus\n```\n",
    "created_at": "2010-02-08T16:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8212#issuecomment-72421",
    "user": "zimmerma"
}
```

> Here is a proposal.

great! A few remarks before a complete review: (i) it would be best to write Conway instead of
conway (maybe except for the option name, if small letters are mandatory); (ii) I get an error
for 2<sup>n</sup> for 2 <= n <= 15:

```
sage:    T.<a> = GF(2^2, modulus='conway')
...
TypeError: Cannot understand modulus
```




---

archive/issue_comments_072422.json:
```json
{
    "body": "Changing assignee from AlexGhitza to zimmerma.",
    "created_at": "2010-02-08T16:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8212#issuecomment-72422",
    "user": "zimmerma"
}
```

Changing assignee from AlexGhitza to zimmerma.



---

archive/issue_comments_072423.json:
```json
{
    "body": "sage -t * did pass (more precisely it did not exhibit more failures with respect to #7773), which\nshows that the case p<sup>n</sup> for n <= 15 should be exercised in the tests, especially with the new\nmodulus=... options.",
    "created_at": "2010-02-08T16:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8212#issuecomment-72423",
    "user": "zimmerma"
}
```

sage -t * did pass (more precisely it did not exhibit more failures with respect to #7773), which
shows that the case p<sup>n</sup> for n <= 15 should be exercised in the tests, especially with the new
modulus=... options.



---

archive/issue_comments_072424.json:
```json
{
    "body": "Attachment [trac_8212-minimal_weight_poly_defining_GF2n.patch](tarball://root/attachments/some-uuid/ticket8212/trac_8212-minimal_weight_poly_defining_GF2n.patch) by ylchapuy created at 2010-02-08 16:35:01\n\nReplying to [comment:4 zimmerma]:\n> great! A few remarks before a complete review: (i) it would be best to write Conway instead of\n> conway (maybe except for the option name, if small letters are mandatory); \n\nAgreed. I modified the docstring, but didn't touch the conway_polynomial functions (and therefore the RuntimeError).\n\n(ii) I get an error\n> for 2<sup>n</sup> for 2 <= n <= 15:\n\nThis is expected, that's why I specified implemented with NTL.\nFor smaller fields, Sage uses Givaro.\nThe options available for creating fields with Givaro, NTL and Pari are different. Another ticket should probably be opened to add some consistency.\n\nYann",
    "created_at": "2010-02-08T16:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8212#issuecomment-72424",
    "user": "ylchapuy"
}
```

Attachment [trac_8212-minimal_weight_poly_defining_GF2n.patch](tarball://root/attachments/some-uuid/ticket8212/trac_8212-minimal_weight_poly_defining_GF2n.patch) by ylchapuy created at 2010-02-08 16:35:01

Replying to [comment:4 zimmerma]:
> great! A few remarks before a complete review: (i) it would be best to write Conway instead of
> conway (maybe except for the option name, if small letters are mandatory); 

Agreed. I modified the docstring, but didn't touch the conway_polynomial functions (and therefore the RuntimeError).

(ii) I get an error
> for 2<sup>n</sup> for 2 <= n <= 15:

This is expected, that's why I specified implemented with NTL.
For smaller fields, Sage uses Givaro.
The options available for creating fields with Givaro, NTL and Pari are different. Another ticket should probably be opened to add some consistency.

Yann



---

archive/issue_comments_072425.json:
```json
{
    "body": "> Another ticket should probably be opened to add some consistency.\n\nI'm not sure we can let this patch in, which might break some code doing\n`T.<a> = GF(q, modulus='conway')`. If the limit for smaller fields is\ndocumented somewhere, I suggest you disable the new options in that case,\nand document it in GF?.",
    "created_at": "2010-02-09T07:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8212#issuecomment-72425",
    "user": "zimmerma"
}
```

> Another ticket should probably be opened to add some consistency.

I'm not sure we can let this patch in, which might break some code doing
`T.<a> = GF(q, modulus='conway')`. If the limit for smaller fields is
documented somewhere, I suggest you disable the new options in that case,
and document it in GF?.



---

archive/issue_comments_072426.json:
```json
{
    "body": "Replying to [comment:7 zimmerma]:\n> > Another ticket should probably be opened to add some consistency.\n> \n> I'm not sure we can let this patch in, which might break some code doing\n> `T.<a> = GF(q, modulus='conway')`. If the limit for smaller fields is\n> documented somewhere, I suggest you disable the new options in that case,\n> and document it in GF?.\n\nThis won't break anything because the option modulus='conway' is new as well.\n\nThe limit for the different implementations is documented at the begining of the file finite_field.py\n(see http://www.sagemath.org/doc/reference/sage/rings/finite_field.html )\n\nFinally, I opened another ticket (#8220) you might review after this one:\n\n* it cleans the code and the documentation for finite field creation;\n* modulus = 'conway' and modulus = 'random' are available for all implementations;\n* modulus = 'minimal_weight' is available for all binary fields;\n* it adds modulus = 'first_lexicographic' for all binary fields.",
    "created_at": "2010-02-09T15:43:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8212#issuecomment-72426",
    "user": "ylchapuy"
}
```

Replying to [comment:7 zimmerma]:
> > Another ticket should probably be opened to add some consistency.
> 
> I'm not sure we can let this patch in, which might break some code doing
> `T.<a> = GF(q, modulus='conway')`. If the limit for smaller fields is
> documented somewhere, I suggest you disable the new options in that case,
> and document it in GF?.

This won't break anything because the option modulus='conway' is new as well.

The limit for the different implementations is documented at the begining of the file finite_field.py
(see http://www.sagemath.org/doc/reference/sage/rings/finite_field.html )

Finally, I opened another ticket (#8220) you might review after this one:

* it cleans the code and the documentation for finite field creation;
* modulus = 'conway' and modulus = 'random' are available for all implementations;
* modulus = 'minimal_weight' is available for all binary fields;
* it adds modulus = 'first_lexicographic' for all binary fields.



---

archive/issue_comments_072427.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-10T11:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8212#issuecomment-72427",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072428.json:
```json
{
    "body": "ok, I give a positive review for that ticket, and will review #8220 afterwards. Great work!\n\nPaul\n\nPS: a related question is the following over GF(2): when no irreducible trinomial exists for a \ngiven degree n, instead of using a pentanomial, one can use an \"almost irreducible\" trinomial,\ni.e., a trinomial x<sup>n+d</sup>+x<sup>s</sup>+1 which has an irreducible factor of degree n. For example for\nn=211, x<sup>214</sup>+x<sup>103</sup>+1 works. I tried this with QuotientRing, but it is much slower:\n\n```\nR.<x> = PolynomialRing(GF(2),x)\nT.<x> = QuotientRing(R, x^214 + x^103 + 1)\n\ndef bar(n):\n   f = x\n   for i in range(n):\n      f = f^2\n   return f\nsage: %timeit bar(10000)\n10 loops, best of 3: 191 ms per loop\n```\n",
    "created_at": "2010-02-10T11:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8212#issuecomment-72428",
    "user": "zimmerma"
}
```

ok, I give a positive review for that ticket, and will review #8220 afterwards. Great work!

Paul

PS: a related question is the following over GF(2): when no irreducible trinomial exists for a 
given degree n, instead of using a pentanomial, one can use an "almost irreducible" trinomial,
i.e., a trinomial x<sup>n+d</sup>+x<sup>s</sup>+1 which has an irreducible factor of degree n. For example for
n=211, x<sup>214</sup>+x<sup>103</sup>+1 works. I tried this with QuotientRing, but it is much slower:

```
R.<x> = PolynomialRing(GF(2),x)
T.<x> = QuotientRing(R, x^214 + x^103 + 1)

def bar(n):
   f = x
   for i in range(n):
      f = f^2
   return f
sage: %timeit bar(10000)
10 loops, best of 3: 191 ms per loop
```




---

archive/issue_comments_072429.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8212#issuecomment-72429",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_072430.json:
```json
{
    "body": "Please remember to update the relevant ticket fields --- the release\nmanagers use an automated script to generate lists of merged tickets.",
    "created_at": "2010-02-11T14:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8212#issuecomment-72430",
    "user": "mpatel"
}
```

Please remember to update the relevant ticket fields --- the release
managers use an automated script to generate lists of merged tickets.
