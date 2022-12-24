# Issue 8344: Factor constant polynomials over QQbar

archive/issues_008344.json:
```json
{
    "body": "Assignee: AlexGhitza\n\n\n```\nboothby@sage:~$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: f = QQbar['x'](1)\nsage: f.roots()\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n| Sage Version 4.3.2, Release Date: 2010-02-06                       |\n| Type notebook() for the GUI, and license() for information.        |\n/home/boothby/<ipython console> in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:29646)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/complex_roots.pyc in complex_roots(p, skip_squarefree, retval, min_prec)\n    339         factors = [(p, 1)]\n    340     else:\n--> 341         factors = p.squarefree_decomposition()\n    342 \n    343     prec = 53\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.squarefree_decomposition (sage/rings/polynomial/polynomial_element.c:10808)()\n\nIndexError: list index out of range\nsage: \n\n\n```\n\n\nThis one should be pretty easy.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8344\n\n",
    "created_at": "2010-02-24T04:15:55Z",
    "labels": [
        "basic arithmetic",
        "critical",
        "bug"
    ],
    "title": "Factor constant polynomials over QQbar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8344",
    "user": "boothby"
}
```
Assignee: AlexGhitza


```
boothby@sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: f = QQbar['x'](1)
sage: f.roots()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
| Sage Version 4.3.2, Release Date: 2010-02-06                       |
| Type notebook() for the GUI, and license() for information.        |
/home/boothby/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:29646)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/complex_roots.pyc in complex_roots(p, skip_squarefree, retval, min_prec)
    339         factors = [(p, 1)]
    340     else:
--> 341         factors = p.squarefree_decomposition()
    342 
    343     prec = 53

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.squarefree_decomposition (sage/rings/polynomial/polynomial_element.c:10808)()

IndexError: list index out of range
sage: 


```


This one should be pretty easy.

Issue created by migration from https://trac.sagemath.org/ticket/8344





---

archive/issue_comments_074476.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-02-24T07:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74476",
    "user": "dimpase"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_074477.json:
```json
{
    "body": "it's an easy to fix bug in squarefree_decomposition in sage/rings/ \npolynomial/polynomial_element.pyx, line 1142\nThe case of constant polynomials needs a special treatment.\n \nI can fix it if there are no takers...",
    "created_at": "2010-02-24T07:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74477",
    "user": "dimpase"
}
```

it's an easy to fix bug in squarefree_decomposition in sage/rings/ 
polynomial/polynomial_element.pyx, line 1142
The case of constant polynomials needs a special treatment.
 
I can fix it if there are no takers...



---

archive/issue_comments_074478.json:
```json
{
    "body": "Attachment [trac-8344.patch](tarball://root/attachments/some-uuid/ticket8344/trac-8344.patch) by dimpase created at 2010-02-26 07:44:28",
    "created_at": "2010-02-26T07:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74478",
    "user": "dimpase"
}
```

Attachment [trac-8344.patch](tarball://root/attachments/some-uuid/ticket8344/trac-8344.patch) by dimpase created at 2010-02-26 07:44:28



---

archive/issue_comments_074479.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-26T07:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74479",
    "user": "dimpase"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074480.json:
```json
{
    "body": "Replying to [comment:1 dimpase]:\n> it's an easy to fix bug in squarefree_decomposition in sage/rings/ \n> polynomial/polynomial_element.pyx, line 1142\n> The case of constant polynomials needs a special treatment.\n>  \n> I can fix it if there are no takers... \n\nthe patch is uploaded (also fixing a similar bug in factors()). Please test etc.",
    "created_at": "2010-02-26T07:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74480",
    "user": "dimpase"
}
```

Replying to [comment:1 dimpase]:
> it's an easy to fix bug in squarefree_decomposition in sage/rings/ 
> polynomial/polynomial_element.pyx, line 1142
> The case of constant polynomials needs a special treatment.
>  
> I can fix it if there are no takers... 

the patch is uploaded (also fixing a similar bug in factors()). Please test etc.



---

archive/issue_comments_074481.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-08T21:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74481",
    "user": "cremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074482.json:
```json
{
    "body": "I don't think this is right.\n\n```\n  if self.degree() == 0: \n \t return Factorization([(self,1)]) \n```\n\nIf R (the coefficient ring) is a field then we should return the factorization with no pairs (irreducible,exponent) but with unit=self.  But if (for example) R is ZZ then we do need to factor constants, so returning self(0).factor() is about right.",
    "created_at": "2010-03-08T21:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74482",
    "user": "cremona"
}
```

I don't think this is right.

```
  if self.degree() == 0: 
 	 return Factorization([(self,1)]) 
```

If R (the coefficient ring) is a field then we should return the factorization with no pairs (irreducible,exponent) but with unit=self.  But if (for example) R is ZZ then we do need to factor constants, so returning self(0).factor() is about right.



---

archive/issue_comments_074483.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-09T02:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74483",
    "user": "dimpase"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074484.json:
```json
{
    "body": "Replying to [comment:3 cremona]:\n> I don't think this is right.\n> {{{\n>   if self.degree() == 0: \n>  \t return Factorization([(self,1)]) \n> }}}\n> If R (the coefficient ring) is a field then we should return the factorization with no pairs (irreducible,exponent) but with unit=self.  But if (for example) R is ZZ then we do need to factor constants, so returning self(0).factor() is about right.\n\nI don't understand your remark.\nMy patch appears to be in accordance with the current design.\n\nsage: f = ZZ['x'](4*x)\nsage: f.squarefree_decomposition()\n(4) * x\nsage: f.factor()\n2^2 * x\n\nAnd it works:\n\nsage: f = ZZ['x'](4)\nsage: f.factor()\n2^2\nsage: f.squarefree_decomposition()\n4\n\nsage: f = QQbar['x'](4)\nsage: f.factor()\n4\nsage: f.squarefree_decomposition()\n4",
    "created_at": "2010-03-09T02:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74484",
    "user": "dimpase"
}
```

Replying to [comment:3 cremona]:
> I don't think this is right.
> {{{
>   if self.degree() == 0: 
>  	 return Factorization([(self,1)]) 
> }}}
> If R (the coefficient ring) is a field then we should return the factorization with no pairs (irreducible,exponent) but with unit=self.  But if (for example) R is ZZ then we do need to factor constants, so returning self(0).factor() is about right.

I don't understand your remark.
My patch appears to be in accordance with the current design.

sage: f = ZZ['x'](4*x)
sage: f.squarefree_decomposition()
(4) * x
sage: f.factor()
2^2 * x

And it works:

sage: f = ZZ['x'](4)
sage: f.factor()
2^2
sage: f.squarefree_decomposition()
4

sage: f = QQbar['x'](4)
sage: f.factor()
4
sage: f.squarefree_decomposition()
4



---

archive/issue_comments_074485.json:
```json
{
    "body": "Replying to [comment:4 dimpase]:\n\noops, sorry, wrong formatting in my previous comment (look OK in preview...). Fixed here.\n\n> Replying to [comment:3 cremona]:\n > I don't think this is right.\n > {{{\n >   if self.degree() == 0: \n >  \t return Factorization([(self,1)]) \n > }}}\n > If R (the coefficient ring) is a field then we should return the factorization with no pairs (irreducible,exponent) but with unit=self.  But if (for example) R is ZZ then we do need to factor constants, so returning self(0).factor() is about right.\n \n I don't understand your remark.\n My patch appears to be in accordance with the current design.\n\n``` \n sage: f = ZZ['x'](4*x)\n sage: f.squarefree_decomposition()\n (4) * x\n sage: f.factor()\n 2^2 * x\n```\n \nAnd it works:\n\n``` \n sage: f = ZZ['x'](4)\n sage: f.factor()\n 2^2\n sage: f.squarefree_decomposition()\n 4\n \n sage: f = QQbar['x'](4)\n sage: f.factor()\n 4\n sage: f.squarefree_decomposition()\n 4\n```\n",
    "created_at": "2010-03-09T02:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74485",
    "user": "dimpase"
}
```

Replying to [comment:4 dimpase]:

oops, sorry, wrong formatting in my previous comment (look OK in preview...). Fixed here.

> Replying to [comment:3 cremona]:
 > I don't think this is right.
 > {{{
 >   if self.degree() == 0: 
 >  	 return Factorization([(self,1)]) 
 > }}}
 > If R (the coefficient ring) is a field then we should return the factorization with no pairs (irreducible,exponent) but with unit=self.  But if (for example) R is ZZ then we do need to factor constants, so returning self(0).factor() is about right.
 
 I don't understand your remark.
 My patch appears to be in accordance with the current design.

``` 
 sage: f = ZZ['x'](4*x)
 sage: f.squarefree_decomposition()
 (4) * x
 sage: f.factor()
 2^2 * x
```
 
And it works:

``` 
 sage: f = ZZ['x'](4)
 sage: f.factor()
 2^2
 sage: f.squarefree_decomposition()
 4
 
 sage: f = QQbar['x'](4)
 sage: f.factor()
 4
 sage: f.squarefree_decomposition()
 4
```




---

archive/issue_comments_074486.json:
```json
{
    "body": "Sorry if I misunderstood -- I thought that was in the factor() function not the square-free decomposition.  Objection withdrawn (but no proper review yet, sorry).",
    "created_at": "2010-03-09T09:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74486",
    "user": "cremona"
}
```

Sorry if I misunderstood -- I thought that was in the factor() function not the square-free decomposition.  Objection withdrawn (but no proper review yet, sorry).



---

archive/issue_comments_074487.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-03-14T16:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74487",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_074488.json:
```json
{
    "body": "I tried to review that one, but I have some questions (maybe unrelated to that ticket):\n\n```\nsage: R = QQbar['x']\nsage: f = R(x)\n...\nNotImplementedError: symbol\n```\n\nThis works this way:\n\n```\nsage: R.<x> = PolynomialRing(QQbar)\nsage: f = R(x)\n```\n\nbut then:\n\n```\nsage: f = R(x^2)\nsage: f.factor()\n...\nNotImplementedError: \n```\n\nWhat is the point of being able to factor only constant polynomials over QQbar?",
    "created_at": "2010-03-14T16:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74488",
    "user": "zimmerma"
}
```

I tried to review that one, but I have some questions (maybe unrelated to that ticket):

```
sage: R = QQbar['x']
sage: f = R(x)
...
NotImplementedError: symbol
```

This works this way:

```
sage: R.<x> = PolynomialRing(QQbar)
sage: f = R(x)
```

but then:

```
sage: f = R(x^2)
sage: f.factor()
...
NotImplementedError: 
```

What is the point of being able to factor only constant polynomials over QQbar?



---

archive/issue_comments_074489.json:
```json
{
    "body": "Good point, Paul;  I had forgotten that no-one had done this yet, which is silly since it only takes one line:\n\n```\nsage: x = polygen(QQbar)\nsage: f = 3*x^2-2\nsage: Factorization([(x-r,e) for r,e in f.roots()],unit=f.leading_coefficient())\n(3) * (x - 0.8164965809277260?) * (x + 0.8164965809277260?)\n```\n\nBut doing this for QQbar would also mean doing it for AAbar, which is a little more complicated, which is probably why no-one has done it yet.\n\n```\nsage: f = x^4-2\nsage: x = polygen(AA)\nsage: f = x^4-2      \nsage: fr = f.roots(QQbar)\nsage: f1 = Factorization([(x-r,e) for r,e in f.roots() if f.imag().is_zero()],unit=f.leading_coefficient())\nsage: f2 = Factorization([(x^2-(r+r.conjugate()).real()*x+r.norm(),e) for r,e in fr if f.image()>0])\nsage: f1*f2\n(x - 1.189207115002722?) * (x + 1.189207115002722?) * (x^2 + 1.414213562373095?)\n```\n\n\nIt is very tempting to add this as a second patch to the ticket.  Can you see anything wrong in my worked examples here?",
    "created_at": "2010-03-14T17:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74489",
    "user": "cremona"
}
```

Good point, Paul;  I had forgotten that no-one had done this yet, which is silly since it only takes one line:

```
sage: x = polygen(QQbar)
sage: f = 3*x^2-2
sage: Factorization([(x-r,e) for r,e in f.roots()],unit=f.leading_coefficient())
(3) * (x - 0.8164965809277260?) * (x + 0.8164965809277260?)
```

But doing this for QQbar would also mean doing it for AAbar, which is a little more complicated, which is probably why no-one has done it yet.

```
sage: f = x^4-2
sage: x = polygen(AA)
sage: f = x^4-2      
sage: fr = f.roots(QQbar)
sage: f1 = Factorization([(x-r,e) for r,e in f.roots() if f.imag().is_zero()],unit=f.leading_coefficient())
sage: f2 = Factorization([(x^2-(r+r.conjugate()).real()*x+r.norm(),e) for r,e in fr if f.image()>0])
sage: f1*f2
(x - 1.189207115002722?) * (x + 1.189207115002722?) * (x^2 + 1.414213562373095?)
```


It is very tempting to add this as a second patch to the ticket.  Can you see anything wrong in my worked examples here?



---

archive/issue_comments_074490.json:
```json
{
    "body": "Dear John,\n\nyour method seems ok to me, however I can't reproduce your first example in Sage 4.3.3:\n\n```\nsage: x = polygen(QQbar)\nsage: f = 3*x^2-2\nsage: lc = f.leading_coefficient()\nsage: Factorization([(x-r,e) for r,e in f.roots()])\n(x - 0.8164965809277260?) * (x + 0.8164965809277260?)\nsage: Factorization([(x-r,e) for r,e in f.roots()],unit=1)\n(x - 0.8164965809277260?) * (x + 0.8164965809277260?)\nsage: Factorization([(x-r,e) for r,e in f.roots()],unit=lc)\n...\nTypeError: Illegal initializer for algebraic number\nsage: type(lc), parent(lc)\n(<class 'sage.rings.qqbar.AlgebraicNumber'>, Algebraic Field)\n```\n\nDoes it depend on another ticket?",
    "created_at": "2010-03-14T17:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74490",
    "user": "zimmerma"
}
```

Dear John,

your method seems ok to me, however I can't reproduce your first example in Sage 4.3.3:

```
sage: x = polygen(QQbar)
sage: f = 3*x^2-2
sage: lc = f.leading_coefficient()
sage: Factorization([(x-r,e) for r,e in f.roots()])
(x - 0.8164965809277260?) * (x + 0.8164965809277260?)
sage: Factorization([(x-r,e) for r,e in f.roots()],unit=1)
(x - 0.8164965809277260?) * (x + 0.8164965809277260?)
sage: Factorization([(x-r,e) for r,e in f.roots()],unit=lc)
...
TypeError: Illegal initializer for algebraic number
sage: type(lc), parent(lc)
(<class 'sage.rings.qqbar.AlgebraicNumber'>, Algebraic Field)
```

Does it depend on another ticket?



---

archive/issue_comments_074491.json:
```json
{
    "body": "Replying to [comment:9 zimmerma]:\n> Dear John,\n> \n> your method seems ok to me, however I can't reproduce your first example in Sage 4.3.3:\n\n> Does it depend on another ticket?\n\n#7984 I think, which was merged in 4.3.4.alpha0.  I was using 4.3.4.alpha1.  Keep up!",
    "created_at": "2010-03-14T18:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74491",
    "user": "cremona"
}
```

Replying to [comment:9 zimmerma]:
> Dear John,
> 
> your method seems ok to me, however I can't reproduce your first example in Sage 4.3.3:

> Does it depend on another ticket?

#7984 I think, which was merged in 4.3.4.alpha0.  I was using 4.3.4.alpha1.  Keep up!



---

archive/issue_comments_074492.json:
```json
{
    "body": "Replying to [comment:8 cremona]:\n> Good point, Paul;  I had forgotten that no-one had done this yet, which is silly since it only takes one line:\n> {{{\n> sage: x = polygen(QQbar)\n> sage: f = 3*x^2-2\n> sage: Factorization([(x-r,e) for r,e in f.roots()],unit=f.leading_coefficient())\n> (3) * (x - 0.8164965809277260?) * (x + 0.8164965809277260?)\n> }}}\n> But doing this for QQbar would also mean doing it for AAbar, which is a little more complicated, which is probably why no-one has done it yet.\n> {{{\n> sage: f = x^4-2\n> sage: x = polygen(AA)\n> sage: f = x^4-2      \n> sage: fr = f.roots(QQbar)\n> sage: f1 = Factorization([(x-r,e) for r,e in f.roots() if f.imag().is_zero()],unit=f.leading_coefficient())\n> sage: f2 = Factorization([(x^2-(r+r.conjugate()).real()*x+r.norm(),e) for r,e in fr if f.image()>0])\n> sage: f1*f2\n> (x - 1.189207115002722?) * (x + 1.189207115002722?) * (x^2 + 1.414213562373095?)\n> }}}\n> \n> It is very tempting to add this as a second patch to the ticket.  Can you see anything wrong in my worked examples here?\n\n\nShouldn't these roots be exact? (i.e. they should come with intervals isolating them, otherwise one can potentially get\nwrong results, mixing numerical noise with true multiplicities --- or is it built-in f.roots() already?)\n\n(same applies to QQbar---although I do not know anything\nabout isolating complex roots, excuse my ignorance...)\n\n\n>",
    "created_at": "2010-03-15T02:27:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74492",
    "user": "dimpase"
}
```

Replying to [comment:8 cremona]:
> Good point, Paul;  I had forgotten that no-one had done this yet, which is silly since it only takes one line:
> {{{
> sage: x = polygen(QQbar)
> sage: f = 3*x^2-2
> sage: Factorization([(x-r,e) for r,e in f.roots()],unit=f.leading_coefficient())
> (3) * (x - 0.8164965809277260?) * (x + 0.8164965809277260?)
> }}}
> But doing this for QQbar would also mean doing it for AAbar, which is a little more complicated, which is probably why no-one has done it yet.
> {{{
> sage: f = x^4-2
> sage: x = polygen(AA)
> sage: f = x^4-2      
> sage: fr = f.roots(QQbar)
> sage: f1 = Factorization([(x-r,e) for r,e in f.roots() if f.imag().is_zero()],unit=f.leading_coefficient())
> sage: f2 = Factorization([(x^2-(r+r.conjugate()).real()*x+r.norm(),e) for r,e in fr if f.image()>0])
> sage: f1*f2
> (x - 1.189207115002722?) * (x + 1.189207115002722?) * (x^2 + 1.414213562373095?)
> }}}
> 
> It is very tempting to add this as a second patch to the ticket.  Can you see anything wrong in my worked examples here?


Shouldn't these roots be exact? (i.e. they should come with intervals isolating them, otherwise one can potentially get
wrong results, mixing numerical noise with true multiplicities --- or is it built-in f.roots() already?)

(same applies to QQbar---although I do not know anything
about isolating complex roots, excuse my ignorance...)


>



---

archive/issue_comments_074493.json:
```json
{
    "body": "QQbar elements have infinite precision, in effect:  the ? in the output is normal for elements of RIF.  The QQbar implementation automatically increases the precision as necessary.  Each element also comes with a polynomial (over QQ) of which it is a root.\n\nI suggest that you read some of the documentation of QQbar, which is an amazing piece of code!",
    "created_at": "2010-03-15T09:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74493",
    "user": "cremona"
}
```

QQbar elements have infinite precision, in effect:  the ? in the output is normal for elements of RIF.  The QQbar implementation automatically increases the precision as necessary.  Each element also comes with a polynomial (over QQ) of which it is a root.

I suggest that you read some of the documentation of QQbar, which is an amazing piece of code!



---

archive/issue_comments_074494.json:
```json
{
    "body": "John,\n\nafter applying #7984 on vanilla 4.3.3, your first example works, but the second one still fails:\n\n```\nsage: f1 = Factorization([(x-r,e) for r,e in f.roots() if f.imag().is_zero()],unit=f.leading_coefficient())\n...\nAttributeError: 'Polynomial_generic_dense_field' object has no attribute 'imag'\n```\n\nAny other ticket to apply? (Sorry I have no time to install an alpha version.)",
    "created_at": "2010-03-15T10:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74494",
    "user": "zimmerma"
}
```

John,

after applying #7984 on vanilla 4.3.3, your first example works, but the second one still fails:

```
sage: f1 = Factorization([(x-r,e) for r,e in f.roots() if f.imag().is_zero()],unit=f.leading_coefficient())
...
AttributeError: 'Polynomial_generic_dense_field' object has no attribute 'imag'
```

Any other ticket to apply? (Sorry I have no time to install an alpha version.)



---

archive/issue_comments_074495.json:
```json
{
    "body": "Very sorry, it was a cut-and-paste error.  The lines defining f1 and f2 should read\n\n```\nsage: f1 = Factorization([(x-r,e) for r,e in f.roots() if r.imag().is_zero()],unit=f.leading_coefficient())\nsage: f2 = Factorization([(x^2-(r+r.conjugate()).real()*x+r.norm(),e) for r,e in fr if r.imag()>0])\n```\n\n(there was a typo in the second one too).\n\nThe trick of testing r.imag()>0 was just a way of picking exactly one conjugate of each pair of non-real conjugate roots.  I think that is quite cheap.  But a better way would be, for each element of AA or QQbar to have a function returning its minpoly over RR (currently the minpoly() function returns its minpoly over QQ).  And we have the norm of an element of QQbar which is the product of it with its CC/RR-conjugate (and not its norm down to QQ), but we do not have a trace:  another function I would like to add!",
    "created_at": "2010-03-15T10:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74495",
    "user": "cremona"
}
```

Very sorry, it was a cut-and-paste error.  The lines defining f1 and f2 should read

```
sage: f1 = Factorization([(x-r,e) for r,e in f.roots() if r.imag().is_zero()],unit=f.leading_coefficient())
sage: f2 = Factorization([(x^2-(r+r.conjugate()).real()*x+r.norm(),e) for r,e in fr if r.imag()>0])
```

(there was a typo in the second one too).

The trick of testing r.imag()>0 was just a way of picking exactly one conjugate of each pair of non-real conjugate roots.  I think that is quite cheap.  But a better way would be, for each element of AA or QQbar to have a function returning its minpoly over RR (currently the minpoly() function returns its minpoly over QQ).  And we have the norm of an element of QQbar which is the product of it with its CC/RR-conjugate (and not its norm down to QQ), but we do not have a trace:  another function I would like to add!



---

archive/issue_comments_074496.json:
```json
{
    "body": "John, now I can reproduce your two examples. Just waiting for a patch to review, if you still believe we should add that to that ticket...\n\nPaul",
    "created_at": "2010-03-15T12:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74496",
    "user": "zimmerma"
}
```

John, now I can reproduce your two examples. Just waiting for a patch to review, if you still believe we should add that to that ticket...

Paul



---

archive/issue_comments_074497.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-03-15T12:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74497",
    "user": "zimmerma"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_074498.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-15T20:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74498",
    "user": "cremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074499.json:
```json
{
    "body": "I think we should use a different ticket for the general factorization of polynomials over QQbar (and AA).  So I will give this a positive review, and open a new ticket which refers to the discussion at this one.",
    "created_at": "2010-03-15T20:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74499",
    "user": "cremona"
}
```

I think we should use a different ticket for the general factorization of polynomials over QQbar (and AA).  So I will give this a positive review, and open a new ticket which refers to the discussion at this one.



---

archive/issue_comments_074500.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-15T20:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74500",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074501.json:
```json
{
    "body": "See #8644 for factoring general polynomials over QQbar and AA.",
    "created_at": "2010-03-15T20:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74501",
    "user": "cremona"
}
```

See #8644 for factoring general polynomials over QQbar and AA.



---

archive/issue_comments_074502.json:
```json
{
    "body": "Merged trac-8344.patch in 4.4.alpha0",
    "created_at": "2010-04-15T20:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74502",
    "user": "jhpalmieri"
}
```

Merged trac-8344.patch in 4.4.alpha0



---

archive/issue_comments_074503.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T20:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74503",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_074504.json:
```json
{
    "body": "Replying to [comment:19 cremona]:\n> See #8644 for factoring general polynomials over QQbar and AA.\n\nThat should read #8544.  A patch is now there.",
    "created_at": "2010-05-26T20:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8344#issuecomment-74504",
    "user": "cremona"
}
```

Replying to [comment:19 cremona]:
> See #8644 for factoring general polynomials over QQbar and AA.

That should read #8544.  A patch is now there.
