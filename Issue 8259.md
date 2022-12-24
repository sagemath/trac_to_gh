# Issue 8259: Conversion from symmetric polynomials to basis of monomial symmetric functions

archive/issues_008259.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  @jbandlow sage-combinat\n\nKeywords: symmetric functions\n\nCurrently a function that converts a symmetric polynomial into the monomial basis is missing in sage. Jason Bandlow wrote a first version which should be integrated into sage:\n\ndef toSF(f):\n    \"\"\" Input is a symmetric polynomial in a polynomial ring in finitely\n    many variables.  Output is a symmetric function in the monomial\n    basis of the ring of symmetric functions over the same base ring.\n    \"\"\"\n    X = f.parent().gens()\n    n = f.parent().ngens()\n    SF = SymmetricFunctions(f.base_ring())\n    m = SF.monomial()\n    out = m(0)\n    while f != 0:\n        lt = f.lt()\n        c = lt.monomial_coefficient(lt)\n        p = Partition(lt.exponents()[0])\n        f += -c*m(p).expand(n,X)\n        out += c*m(p)\n    return out\n\nIssue created by migration from https://trac.sagemath.org/ticket/8259\n\n",
    "created_at": "2010-02-14T00:22:35Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Conversion from symmetric polynomials to basis of monomial symmetric functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8259",
    "user": "@anneschilling"
}
```
Assignee: sage-combinat

CC:  @jbandlow sage-combinat

Keywords: symmetric functions

Currently a function that converts a symmetric polynomial into the monomial basis is missing in sage. Jason Bandlow wrote a first version which should be integrated into sage:

def toSF(f):
    """ Input is a symmetric polynomial in a polynomial ring in finitely
    many variables.  Output is a symmetric function in the monomial
    basis of the ring of symmetric functions over the same base ring.
    """
    X = f.parent().gens()
    n = f.parent().ngens()
    SF = SymmetricFunctions(f.base_ring())
    m = SF.monomial()
    out = m(0)
    while f != 0:
        lt = f.lt()
        c = lt.monomial_coefficient(lt)
        p = Partition(lt.exponents()[0])
        f += -c*m(p).expand(n,X)
        out += c*m(p)
    return out

Issue created by migration from https://trac.sagemath.org/ticket/8259





---

archive/issue_comments_073090.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-20T05:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73090",
    "user": "@anneschilling"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073091.json:
```json
{
    "body": "Has this been checked on Solaris?\n\nThere's general information about building on Solaris at\n\n http://wiki.sagemath.org/solaris\n\nInformation specifically for 't2' at\n\n http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2\n\nBoth the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html\n\nDave",
    "created_at": "2010-02-21T23:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73091",
    "user": "drkirkby"
}
```

Has this been checked on Solaris?

There's general information about building on Solaris at

 http://wiki.sagemath.org/solaris

Information specifically for 't2' at

 http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave



---

archive/issue_comments_073092.json:
```json
{
    "body": "Dave,\n\nAre you sure you posted this comment to the correct ticket?\n\nIf so, could you please comment on the relevance of Solaris to \nthe code?\n\nThanks,\n\nAnne\n\nReplying to [comment:4 drkirkby]:\n> Has this been checked on Solaris?\n> \n> There's general information about building on Solaris at\n> \n>  http://wiki.sagemath.org/solaris\n> \n> Information specifically for 't2' at\n> \n>  http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2\n> \n> Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html\n> \n> Dave",
    "created_at": "2010-02-22T02:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73092",
    "user": "@anneschilling"
}
```

Dave,

Are you sure you posted this comment to the correct ticket?

If so, could you please comment on the relevance of Solaris to 
the code?

Thanks,

Anne

Replying to [comment:4 drkirkby]:
> Has this been checked on Solaris?
> 
> There's general information about building on Solaris at
> 
>  http://wiki.sagemath.org/solaris
> 
> Information specifically for 't2' at
> 
>  http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2
> 
> Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html
> 
> Dave



---

archive/issue_comments_073093.json:
```json
{
    "body": "Hi Anne,\n\nThe fix to crystals.py doesn't apply to either sage 4.3.2 or sage 4.3.3.  Can it be removed from this patch?\n\nThanks,\nJason",
    "created_at": "2010-02-22T20:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73093",
    "user": "@jbandlow"
}
```

Hi Anne,

The fix to crystals.py doesn't apply to either sage 4.3.2 or sage 4.3.3.  Can it be removed from this patch?

Thanks,
Jason



---

archive/issue_comments_073094.json:
```json
{
    "body": "One more thing.  I would really like to have an option to verify that the input actually is a symmetric function.  In fact I think this should be true by default.  So the key function would look something like this:\n\n\n```\ndef from_polynomial(self, f, check=True):        \n    assert(self.base_ring() == f.base_ring()\n    d = dict([(e,c) for e,c in f.dict().iteritems() if tuple(sorted(e)) == tuple(reversed(e))]) \n    if not check:\n        return self.sum(d[la]*self(Partition(la)) for la in d.keys())\n    out = self.sum(d[la]*self(Partition(la)) for la in d.keys())\n    assert( out.expand(f.parent().ngens(),f.parent().gens()) == f )\n    return out\n```\n",
    "created_at": "2010-02-22T21:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73094",
    "user": "@jbandlow"
}
```

One more thing.  I would really like to have an option to verify that the input actually is a symmetric function.  In fact I think this should be true by default.  So the key function would look something like this:


```
def from_polynomial(self, f, check=True):        
    assert(self.base_ring() == f.base_ring()
    d = dict([(e,c) for e,c in f.dict().iteritems() if tuple(sorted(e)) == tuple(reversed(e))]) 
    if not check:
        return self.sum(d[la]*self(Partition(la)) for la in d.keys())
    out = self.sum(d[la]*self(Partition(la)) for la in d.keys())
    assert( out.expand(f.parent().ngens(),f.parent().gens()) == f )
    return out
```




---

archive/issue_comments_073095.json:
```json
{
    "body": "Hi Jason,\n\nI attached a revised patch which includes your suggestion to add the option to test\nwhether the polynomial is symmetric.\n\nFor me the patch applied to sage-4.3.3. It depends on trac tickets #7978 and #8154\nwhich have been merged in sage-4.3.3. Hence it might not apply cleanly to sage-4.3.2.\n\nAnne",
    "created_at": "2010-02-23T02:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73095",
    "user": "@anneschilling"
}
```

Hi Jason,

I attached a revised patch which includes your suggestion to add the option to test
whether the polynomial is symmetric.

For me the patch applied to sage-4.3.3. It depends on trac tickets #7978 and #8154
which have been merged in sage-4.3.3. Hence it might not apply cleanly to sage-4.3.2.

Anne



---

archive/issue_comments_073096.json:
```json
{
    "body": "Attachment [trac_8259-from_poly_to_sym-as.patch](tarball://root/attachments/some-uuid/ticket8259/trac_8259-from_poly_to_sym-as.patch) by @anneschilling created at 2010-02-23 18:49:25",
    "created_at": "2010-02-23T18:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73096",
    "user": "@anneschilling"
}
```

Attachment [trac_8259-from_poly_to_sym-as.patch](tarball://root/attachments/some-uuid/ticket8259/trac_8259-from_poly_to_sym-as.patch) by @anneschilling created at 2010-02-23 18:49:25



---

archive/issue_comments_073097.json:
```json
{
    "body": "Hi Jason,\n\nAs we just discussed on the phone, I did revert the indentation of class Element\nin /combinat/sf/monomial.py back to the same level as\nclass SymmetricFunctionAlgebra_monomial\n\nHowever, I did change the indentation to be multiples of 4 rather than multiples \nof 3. I sent an e-mail to sage-combinat-devel to ask about the indentation issues\nin sf.\n\nAnne",
    "created_at": "2010-02-23T18:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73097",
    "user": "@anneschilling"
}
```

Hi Jason,

As we just discussed on the phone, I did revert the indentation of class Element
in /combinat/sf/monomial.py back to the same level as
class SymmetricFunctionAlgebra_monomial

However, I did change the indentation to be multiples of 4 rather than multiples 
of 3. I sent an e-mail to sage-combinat-devel to ask about the indentation issues
in sf.

Anne



---

archive/issue_comments_073098.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-23T21:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73098",
    "user": "@jbandlow"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073099.json:
```json
{
    "body": "Thanks Anne! This looks good to me.  Positive review.\n\n-Jason",
    "created_at": "2010-02-23T21:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73099",
    "user": "@jbandlow"
}
```

Thanks Anne! This looks good to me.  Positive review.

-Jason



---

archive/issue_comments_073100.json:
```json
{
    "body": "Just two tiny remarks:\n\n- One can write `assert a==b` instead of `assert(a==b)`\n- One could be a bit more specific:  `assert a==b, \"not a symmetric polynomial\"\n- Assertion are not *always* checked (see http://docs.python.org/reference/simple_stmts.html).\n  So I am not sure it is the appropriate idiom here.\n\nThat's minor, so I let you see if you want to add a quick review patch, or just leave things as is.\n\nThanks!",
    "created_at": "2010-02-25T08:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73100",
    "user": "@nthiery"
}
```

Just two tiny remarks:

- One can write `assert a==b` instead of `assert(a==b)`
- One could be a bit more specific:  `assert a==b, "not a symmetric polynomial"
- Assertion are not *always* checked (see http://docs.python.org/reference/simple_stmts.html).
  So I am not sure it is the appropriate idiom here.

That's minor, so I let you see if you want to add a quick review patch, or just leave things as is.

Thanks!



---

archive/issue_comments_073101.json:
```json
{
    "body": "Attachment [trac_8259-from_poly_to_sym-review-as.patch](tarball://root/attachments/some-uuid/ticket8259/trac_8259-from_poly_to_sym-review-as.patch) by @anneschilling created at 2010-02-25 18:00:10\n\nReplying to [comment:11 nthiery]:\n> Just two tiny remarks:\n> \n>  - One can write `assert a==b` instead of `assert(a==b)`\n>  - One could be a bit more specific:  `assert a==b, \"not a symmetric polynomial\"\n>  - Assertion are not *always* checked (see http://docs.python.org/reference/simple_stmts.html).\n>    So I am not sure it is the appropriate idiom here.\n> \n> That's minor, so I let you see if you want to add a quick review patch, or just leave things as is.\n> \n> Thanks!\n\nDone! Please review the review of the review of the review ... oops! Infinite loop!",
    "created_at": "2010-02-25T18:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73101",
    "user": "@anneschilling"
}
```

Attachment [trac_8259-from_poly_to_sym-review-as.patch](tarball://root/attachments/some-uuid/ticket8259/trac_8259-from_poly_to_sym-review-as.patch) by @anneschilling created at 2010-02-25 18:00:10

Replying to [comment:11 nthiery]:
> Just two tiny remarks:
> 
>  - One can write `assert a==b` instead of `assert(a==b)`
>  - One could be a bit more specific:  `assert a==b, "not a symmetric polynomial"
>  - Assertion are not *always* checked (see http://docs.python.org/reference/simple_stmts.html).
>    So I am not sure it is the appropriate idiom here.
> 
> That's minor, so I let you see if you want to add a quick review patch, or just leave things as is.
> 
> Thanks!

Done! Please review the review of the review of the review ... oops! Infinite loop!



---

archive/issue_comments_073102.json:
```json
{
    "body": "Replying to [comment:12 aschilling]:\n> Replying to [comment:11 nthiery]:\n> > Just two tiny remarks:\n> > \n> >  - One can write `assert a==b` instead of `assert(a==b)`\n> >  - One could be a bit more specific:  `assert a==b, \"not a symmetric polynomial\"\n> >  - Assertion are not *always* checked (see http://docs.python.org/reference/simple_stmts.html).\n> >    So I am not sure it is the appropriate idiom here.\n> > \n> > That's minor, so I let you see if you want to add a quick review patch, or just leave things as is.\n> > \n> > Thanks!\n> \n> Done! Please review the review of the review of the review ... oops! Infinite loop!\n\nThanks! I haven't rerun the tests, but the review patch looks good to me.",
    "created_at": "2010-02-25T18:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73102",
    "user": "@nthiery"
}
```

Replying to [comment:12 aschilling]:
> Replying to [comment:11 nthiery]:
> > Just two tiny remarks:
> > 
> >  - One can write `assert a==b` instead of `assert(a==b)`
> >  - One could be a bit more specific:  `assert a==b, "not a symmetric polynomial"
> >  - Assertion are not *always* checked (see http://docs.python.org/reference/simple_stmts.html).
> >    So I am not sure it is the appropriate idiom here.
> > 
> > That's minor, so I let you see if you want to add a quick review patch, or just leave things as is.
> > 
> > Thanks!
> 
> Done! Please review the review of the review of the review ... oops! Infinite loop!

Thanks! I haven't rerun the tests, but the review patch looks good to me.



---

archive/issue_comments_073103.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73103",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_073104.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8259-from_poly_to_sym-as.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8259/trac_8259-from_poly_to_sym-as.patch)\n2. [trac_8259-from_poly_to_sym-review-as.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8259/trac_8259-from_poly_to_sym-review-as.patch)",
    "created_at": "2010-03-02T21:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8259#issuecomment-73104",
    "user": "mvngu"
}
```

Merged in this order:

1. [trac_8259-from_poly_to_sym-as.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8259/trac_8259-from_poly_to_sym-as.patch)
2. [trac_8259-from_poly_to_sym-review-as.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8259/trac_8259-from_poly_to_sym-review-as.patch)
