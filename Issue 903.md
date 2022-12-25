# Issue 903: charpoly of matrices over number fields is ridiculously slow right now (easy fixes exist)

archive/issues_000903.json:
```json
{
    "body": "Assignee: @williamstein\n\nSee the below examples that illustrate that charpoly(A), where A is over a number field, currently totally\nsucks.  This has very bad implications for modular forms computations.  Even switching to use PARI for\ncharpoly would give a significant speedup (which is a lot faster than Magma, interestingly). \n\n\n\n```\nK.<a> = NumberField(x^2 + 17)\na^2\n///\n-17\n```\n\n\n\n```\nn = 40\nm = matrix(K, n, [(a+1)^randint(0,3) for _ in xrange(n^2)])\nm\n///\n40 x 40 dense matrix over Number Field in a with defining polynomial x^2 + 17\n```\n\n\n\n```\nm[0] # first row\n///\n(2*a - 16, 1, -14*a - 50, a + 1, 2*a - 16, 2*a - 16, a + 1, -14*a - 50, 1, -14*a - 50, 2*a - 16, a + 1, 1, a + 1, a + 1, a + 1, a + 1, -14*a - 50, -14*a - 50, 2*a - 16, 1, a + 1, 1, a + 1, 2*a - 16, -14*a - 50, 1, 2*a - 16, 2*a - 16, 1, a + 1, a + 1, 1, 2*a - 16, -14*a - 50, 2*a - 16, 2*a - 16, -14*a - 50, 2*a - 16, -14*a - 50)\n```\n\n\n\n```\ntime k = m*m\n///\nCPU time: 0.14 s,  Wall time: 0.27 s\n```\n\n\n\n```\ntime f=m.charpoly()\n///\nCPU time: 23.93 s,  Wall time: 26.22 s\n```\n\n\n<b>NOTE:</b> Sage <i>should</i> use PARI for charpoly's over number\nfields, but currently it doesn't.  Notice how much faster PARI is at\nthe same computation!\n\n\n```\nm._clear_cache()\ng = pari(m)\ntime h = g.charpoly()\n///\nTime: CPU 2.52 s, Wall: 2.76 s\n```\n\n\nBut a <b>multimodular algorithm</b> should blow away all of them.  Student project?\nBasically, charpoly mod p is extremely fast in Sage, and one could reduce modulo\n<i>primes of a number field</i>, do the computation mod p, then lift, and get the\ncorrect result.  I know of no implementations of this.  A student project could be\nto implement this and tune it to be the fastest program in the world for charpoly\nover number fields. \n<br>\n\n\n```\ntime m.echelonize()\n///\nCPU time: 0.35 s,  Wall time: 0.35 s\n```\n\n\n\n```\n%magma\nR<x> := PolynomialRing(RationalField());\nK<a> := NumberField(x^2 + 17);\nn := 40;\nm := MatrixAlgebra(K, n)![(1+a)^Random(0, 3) : i in [1..n^2]];\ntime k := m*m;\ntime f := CharacteristicPolynomial(m);\ntime e := EchelonForm(m);\n///\nTime: 0.000\nTime: 15.220\nTime: 0.150\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/903\n\n",
    "created_at": "2007-10-15T21:01:58Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "charpoly of matrices over number fields is ridiculously slow right now (easy fixes exist)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/903",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

See the below examples that illustrate that charpoly(A), where A is over a number field, currently totally
sucks.  This has very bad implications for modular forms computations.  Even switching to use PARI for
charpoly would give a significant speedup (which is a lot faster than Magma, interestingly). 



```
K.<a> = NumberField(x^2 + 17)
a^2
///
-17
```



```
n = 40
m = matrix(K, n, [(a+1)^randint(0,3) for _ in xrange(n^2)])
m
///
40 x 40 dense matrix over Number Field in a with defining polynomial x^2 + 17
```



```
m[0] # first row
///
(2*a - 16, 1, -14*a - 50, a + 1, 2*a - 16, 2*a - 16, a + 1, -14*a - 50, 1, -14*a - 50, 2*a - 16, a + 1, 1, a + 1, a + 1, a + 1, a + 1, -14*a - 50, -14*a - 50, 2*a - 16, 1, a + 1, 1, a + 1, 2*a - 16, -14*a - 50, 1, 2*a - 16, 2*a - 16, 1, a + 1, a + 1, 1, 2*a - 16, -14*a - 50, 2*a - 16, 2*a - 16, -14*a - 50, 2*a - 16, -14*a - 50)
```



```
time k = m*m
///
CPU time: 0.14 s,  Wall time: 0.27 s
```



```
time f=m.charpoly()
///
CPU time: 23.93 s,  Wall time: 26.22 s
```


<b>NOTE:</b> Sage <i>should</i> use PARI for charpoly's over number
fields, but currently it doesn't.  Notice how much faster PARI is at
the same computation!


```
m._clear_cache()
g = pari(m)
time h = g.charpoly()
///
Time: CPU 2.52 s, Wall: 2.76 s
```


But a <b>multimodular algorithm</b> should blow away all of them.  Student project?
Basically, charpoly mod p is extremely fast in Sage, and one could reduce modulo
<i>primes of a number field</i>, do the computation mod p, then lift, and get the
correct result.  I know of no implementations of this.  A student project could be
to implement this and tune it to be the fastest program in the world for charpoly
over number fields. 
<br>


```
time m.echelonize()
///
CPU time: 0.35 s,  Wall time: 0.35 s
```



```
%magma
R<x> := PolynomialRing(RationalField());
K<a> := NumberField(x^2 + 17);
n := 40;
m := MatrixAlgebra(K, n)![(1+a)^Random(0, 3) : i in [1..n^2]];
time k := m*m;
time f := CharacteristicPolynomial(m);
time e := EchelonForm(m);
///
Time: 0.000
Time: 15.220
Time: 0.150
```


Issue created by migration from https://trac.sagemath.org/ticket/903





---

archive/issue_comments_005525.json:
```json
{
    "body": "The following IRC transcript is relevant.\n\n\n```\nncalexan-827: wstein-1606: is there a good way to find degree 1 primes in a number field.\nncalexan-827: ?\nwstein-1606: theoretically or in sage right now?\nncalexan-827: wstein-1606: right now, but also in theory.\nwstein-1606: for all but finitely many primes you factor the defining poly of the field and see if it splits completely.\ndmharvey left the chat room.\nwstein-1606: you can do that more quickly by taking the gcd mod p with x^p - x\nncalexan-827: Right.\nwstein-1606: or something like that.\nwstein-1606: I bet you get the idea.\nncalexan-827: Doesn't this only work if your ring of integers is generated by a single element?\nwstein-1606: nick -- that's why I said \"all but finitely many\".\nwstein-1606: For all but a couple primes the ring of integers is monogenic.\nwstein-1606: just avoid primes dividing the discriminant.\nwstein-1606: for those do the usual factorization algorithm.\nncalexan-827: wstein-1606: sure.  It sounds like a degree_one_primes() generator would be handy for multi modular algorithms, then.\nwstein-1606: yep!\nwstein-1606: But beware -- it is very very very hard to find any degree one primes if the field isn't cyclotomic.\nwstein-1606: For a galois S_n extension of degree n, only 1/n! of the primes split completely (by cebo.)\nncalexan-827: Hmm.  So it's not even worth it?\nwstein-1606: Well it's very worth it in the cyclotomic case.\nwstein-1606: more generally, in the abelian case.\nwstein-1606: E.g., for quadratic fields.\nwstein-1606: and even 1/n! isn't bad if n is small, which it often is.\n```\n",
    "created_at": "2008-01-19T22:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5525",
    "user": "https://github.com/ncalexan"
}
```

The following IRC transcript is relevant.


```
ncalexan-827: wstein-1606: is there a good way to find degree 1 primes in a number field.
ncalexan-827: ?
wstein-1606: theoretically or in sage right now?
ncalexan-827: wstein-1606: right now, but also in theory.
wstein-1606: for all but finitely many primes you factor the defining poly of the field and see if it splits completely.
dmharvey left the chat room.
wstein-1606: you can do that more quickly by taking the gcd mod p with x^p - x
ncalexan-827: Right.
wstein-1606: or something like that.
wstein-1606: I bet you get the idea.
ncalexan-827: Doesn't this only work if your ring of integers is generated by a single element?
wstein-1606: nick -- that's why I said "all but finitely many".
wstein-1606: For all but a couple primes the ring of integers is monogenic.
wstein-1606: just avoid primes dividing the discriminant.
wstein-1606: for those do the usual factorization algorithm.
ncalexan-827: wstein-1606: sure.  It sounds like a degree_one_primes() generator would be handy for multi modular algorithms, then.
wstein-1606: yep!
wstein-1606: But beware -- it is very very very hard to find any degree one primes if the field isn't cyclotomic.
wstein-1606: For a galois S_n extension of degree n, only 1/n! of the primes split completely (by cebo.)
ncalexan-827: Hmm.  So it's not even worth it?
wstein-1606: Well it's very worth it in the cyclotomic case.
wstein-1606: more generally, in the abelian case.
wstein-1606: E.g., for quadratic fields.
wstein-1606: and even 1/n! isn't bad if n is small, which it often is.
```




---

archive/issue_comments_005526.json:
```json
{
    "body": "I needed exactly this for my work on Unimodular Integer Circulants (To appear in: Mathematics of Computation) or see my web page.  At the time I used pari and have been meaning to try it in Sage too.  Rather than take gcd(f,x^p-x) -- all mof p of course -- , I took Mod(x,f*Mod(1,p))^p and that worked pretty well.  My worst example: deg(f) = 18, the first degree 1 prime was about 250 million and did not work for me so I sed the second one which was around 2 billion.  This poly has a Galois group of order only 2*(n/2)! ; if it been the generic n! I would probably still be waiting.\n\nThis suggests to me that for anything other than small degrees the implementation will need to use primes of higher degree.",
    "created_at": "2008-02-22T20:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5526",
    "user": "https://github.com/JohnCremona"
}
```

I needed exactly this for my work on Unimodular Integer Circulants (To appear in: Mathematics of Computation) or see my web page.  At the time I used pari and have been meaning to try it in Sage too.  Rather than take gcd(f,x^p-x) -- all mof p of course -- , I took Mod(x,f*Mod(1,p))^p and that worked pretty well.  My worst example: deg(f) = 18, the first degree 1 prime was about 250 million and did not work for me so I sed the second one which was around 2 billion.  This poly has a Galois group of order only 2*(n/2)! ; if it been the generic n! I would probably still be waiting.

This suggests to me that for anything other than small degrees the implementation will need to use primes of higher degree.



---

archive/issue_comments_005527.json:
```json
{
    "body": "Replying to [comment:3 cremona]:\n\nSorry about bad formatting.",
    "created_at": "2008-02-22T20:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5527",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:3 cremona]:

Sorry about bad formatting.



---

archive/issue_comments_005528.json:
```json
{
    "body": "See #2835 for a possible primes of degree one iterator implementation.",
    "created_at": "2008-04-06T22:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5528",
    "user": "https://github.com/ncalexan"
}
```

See #2835 for a possible primes of degree one iterator implementation.



---

archive/issue_comments_005529.json:
```json
{
    "body": "Attachment [903-charpoly_pari.patch](tarball://root/attachments/some-uuid/ticket903/903-charpoly_pari.patch) by @aghitza created at 2008-04-13 21:48:09",
    "created_at": "2008-04-13T21:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5529",
    "user": "https://github.com/aghitza"
}
```

Attachment [903-charpoly_pari.patch](tarball://root/attachments/some-uuid/ticket903/903-charpoly_pari.patch) by @aghitza created at 2008-04-13 21:48:09



---

archive/issue_comments_005530.json:
```json
{
    "body": "I suggest that we implement the easy fix and get that merged, and open an enhancement ticket along the lines \"implement multimodular algorithm for charpoly over number fields\".\n\nI'm attaching a patch with the easy fix.  On my machine, William's example runs 15 times faster after the patch than before.",
    "created_at": "2008-04-13T21:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5530",
    "user": "https://github.com/aghitza"
}
```

I suggest that we implement the easy fix and get that merged, and open an enhancement ticket along the lines "implement multimodular algorithm for charpoly over number fields".

I'm attaching a patch with the easy fix.  On my machine, William's example runs 15 times faster after the patch than before.



---

archive/issue_comments_005531.json:
```json
{
    "body": "I am not happy with this patch.  I want to see an explicit doctest (not random) that has a polynomial defined over the number field, not over QQ.\n\nI also want to see doctests for stacked relative fields -- I.e.\n\n```\nx = QQ['x'].gen()\nK.<a> = NumberField(x^2 - 2)\nL.<b> = K.extension(x^3 - a)\nM.<c> = L.extension(x^2 - a*x + b)\n```\n\n\nand see it work for matrices over all those fields.\n\nThis is hard -- we need polynomials over arbitrary pari number fields, and it doesn't work for #2329 yet, so it shouldn't work here yet.",
    "created_at": "2008-04-13T22:33:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5531",
    "user": "https://github.com/ncalexan"
}
```

I am not happy with this patch.  I want to see an explicit doctest (not random) that has a polynomial defined over the number field, not over QQ.

I also want to see doctests for stacked relative fields -- I.e.

```
x = QQ['x'].gen()
K.<a> = NumberField(x^2 - 2)
L.<b> = K.extension(x^3 - a)
M.<c> = L.extension(x^2 - a*x + b)
```


and see it work for matrices over all those fields.

This is hard -- we need polynomials over arbitrary pari number fields, and it doesn't work for #2329 yet, so it shouldn't work here yet.



---

archive/issue_comments_005532.json:
```json
{
    "body": "Attachment [903-charpoly_pari_doctests.patch](tarball://root/attachments/some-uuid/ticket903/903-charpoly_pari_doctests.patch) by @aghitza created at 2008-04-14 23:39:57\n\napply after 903-charpoly_pari.patch",
    "created_at": "2008-04-14T23:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5532",
    "user": "https://github.com/aghitza"
}
```

Attachment [903-charpoly_pari_doctests.patch](tarball://root/attachments/some-uuid/ticket903/903-charpoly_pari_doctests.patch) by @aghitza created at 2008-04-14 23:39:57

apply after 903-charpoly_pari.patch



---

archive/issue_comments_005533.json:
```json
{
    "body": "The point about the doctests is correct.  I put up a new patch that adds the appropriate doctests and fixes a small bug (due to some unrelated weirdness that I don't want to deal with right now).\n\nThe doctests pass and I checked the results.  It looks to me like it's working, so I'm not sure I agree with the last part of the last comment.",
    "created_at": "2008-04-14T23:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5533",
    "user": "https://github.com/aghitza"
}
```

The point about the doctests is correct.  I put up a new patch that adds the appropriate doctests and fixes a small bug (due to some unrelated weirdness that I don't want to deal with right now).

The doctests pass and I checked the results.  It looks to me like it's working, so I'm not sure I agree with the last part of the last comment.



---

archive/issue_comments_005534.json:
```json
{
    "body": "The patches apply and pass tests for me.  Nick, what are your thoughts?",
    "created_at": "2008-04-15T00:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5534",
    "user": "https://github.com/mwhansen"
}
```

The patches apply and pass tests for me.  Nick, what are your thoughts?



---

archive/issue_comments_005535.json:
```json
{
    "body": "Attachment [903-ncalexan-charpoly-over-number-field-1.patch](tarball://root/attachments/some-uuid/ticket903/903-ncalexan-charpoly-over-number-field-1.patch) by @ncalexan created at 2008-04-15 06:17:38",
    "created_at": "2008-04-15T06:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5535",
    "user": "https://github.com/ncalexan"
}
```

Attachment [903-ncalexan-charpoly-over-number-field-1.patch](tarball://root/attachments/some-uuid/ticket903/903-ncalexan-charpoly-over-number-field-1.patch) by @ncalexan created at 2008-04-15 06:17:38



---

archive/issue_comments_005536.json:
```json
{
    "body": "I prefer the attached patch because it does not require string parsing, at least not in the code.  It will be more robust to changes to PARI and uses the Sage library.  It's shorter, too, and I prefer the factored-out function.",
    "created_at": "2008-04-15T06:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5536",
    "user": "https://github.com/ncalexan"
}
```

I prefer the attached patch because it does not require string parsing, at least not in the code.  It will be more robust to changes to PARI and uses the Sage library.  It's shorter, too, and I prefer the factored-out function.



---

archive/issue_comments_005537.json:
```json
{
    "body": "Nick's patch applies and passes the tests.  I think it is preferable since it avoids string parsing.  I'm going to give it a positive review.  Alex, if you disagree, feel free to comment and change it.",
    "created_at": "2008-04-15T06:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5537",
    "user": "https://github.com/mwhansen"
}
```

Nick's patch applies and passes the tests.  I think it is preferable since it avoids string parsing.  I'm going to give it a positive review.  Alex, if you disagree, feel free to comment and change it.



---

archive/issue_comments_005538.json:
```json
{
    "body": "Yes, I much prefer Nick's code over mine.  I was struggling to get things from Pari into Sage and the way I was doing things was obscure and rather fragile.\n\nThere is one problem I run into with this: 2 doctests in number_field_element.pyx fail.  Probably an easy fix?",
    "created_at": "2008-04-15T13:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5538",
    "user": "https://github.com/aghitza"
}
```

Yes, I much prefer Nick's code over mine.  I was struggling to get things from Pari into Sage and the way I was doing things was obscure and rather fragile.

There is one problem I run into with this: 2 doctests in number_field_element.pyx fail.  Probably an easy fix?



---

archive/issue_comments_005539.json:
```json
{
    "body": "Attachment [903-small_fix.patch](tarball://root/attachments/some-uuid/ticket903/903-small_fix.patch) by @aghitza created at 2008-04-15 14:53:01\n\napply after Nick's patch",
    "created_at": "2008-04-15T14:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5539",
    "user": "https://github.com/aghitza"
}
```

Attachment [903-small_fix.patch](tarball://root/attachments/some-uuid/ticket903/903-small_fix.patch) by @aghitza created at 2008-04-15 14:53:01

apply after Nick's patch



---

archive/issue_comments_005540.json:
```json
{
    "body": "It was indeed an easy fix.  Pari treats the t_POLMOD 0 in a different way than the others, so the code chocked on that.  I've put up a patch that fixes this and adds a direct doctest for this behavior.\n\nWe should apply 903-ncalexan-charpoly-over-number-field-1.patch and 903-small_fix.patch.  When this ticket gets closed we should make a new enhancement ticket containing the above discussion of a multimodular algorithm.\n\nBTW, in 3.0.alpha5, before the patches:\n\n\n```\nsage: K.<a> = NumberField(x^2 + 17)\nsage: n = 40\nsage: m = matrix(K, n, [(a+1)^randint(0,3) for _ in xrange(n^2)])\nsage: time f = m.charpoly('Z')\nCPU times: user 59.69 s, sys: 0.01 s, total: 59.70 s\nWall time: 59.70\n```\n\n\nand after the patches:\n\n\n```\nsage: K.<a> = NumberField(x^2 + 17)\nsage: n = 40\nsage: m = matrix(K, n, [(a+1)^randint(0,3) for _ in xrange(n^2)])\nsage: time f = m.charpoly('Z')\nCPU times: user 3.96 s, sys: 0.02 s, total: 3.98 s\nWall time: 3.98\n```\n",
    "created_at": "2008-04-15T14:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5540",
    "user": "https://github.com/aghitza"
}
```

It was indeed an easy fix.  Pari treats the t_POLMOD 0 in a different way than the others, so the code chocked on that.  I've put up a patch that fixes this and adds a direct doctest for this behavior.

We should apply 903-ncalexan-charpoly-over-number-field-1.patch and 903-small_fix.patch.  When this ticket gets closed we should make a new enhancement ticket containing the above discussion of a multimodular algorithm.

BTW, in 3.0.alpha5, before the patches:


```
sage: K.<a> = NumberField(x^2 + 17)
sage: n = 40
sage: m = matrix(K, n, [(a+1)^randint(0,3) for _ in xrange(n^2)])
sage: time f = m.charpoly('Z')
CPU times: user 59.69 s, sys: 0.01 s, total: 59.70 s
Wall time: 59.70
```


and after the patches:


```
sage: K.<a> = NumberField(x^2 + 17)
sage: n = 40
sage: m = matrix(K, n, [(a+1)^randint(0,3) for _ in xrange(n^2)])
sage: time f = m.charpoly('Z')
CPU times: user 3.96 s, sys: 0.02 s, total: 3.98 s
Wall time: 3.98
```




---

archive/issue_comments_005541.json:
```json
{
    "body": "Attachment [903-ncalexan-charpoly-over-number-field-2.patch](tarball://root/attachments/some-uuid/ticket903/903-ncalexan-charpoly-over-number-field-2.patch) by @ncalexan created at 2008-04-15 16:03:52",
    "created_at": "2008-04-15T16:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5541",
    "user": "https://github.com/ncalexan"
}
```

Attachment [903-ncalexan-charpoly-over-number-field-2.patch](tarball://root/attachments/some-uuid/ticket903/903-ncalexan-charpoly-over-number-field-2.patch) by @ncalexan created at 2008-04-15 16:03:52



---

archive/issue_comments_005542.json:
```json
{
    "body": "`903-ncalexan-charpoly-over-number-field-2.patch` stands alone, and doesn't muck about with PARI at all: it turns out that polynomials over number fields work to the extent that special parsing is not necessary.\n\nBTW, great team effort guys!",
    "created_at": "2008-04-15T16:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5542",
    "user": "https://github.com/ncalexan"
}
```

`903-ncalexan-charpoly-over-number-field-2.patch` stands alone, and doesn't muck about with PARI at all: it turns out that polynomials over number fields work to the extent that special parsing is not necessary.

BTW, great team effort guys!



---

archive/issue_comments_005543.json:
```json
{
    "body": "I *love* the end result, it's so clean and simple (I wish there was a way to delete my old patches from this ticket, I'm somewhat embarrassed :)\n\nAnyway, it works great and fast and it should be merged.",
    "created_at": "2008-04-15T18:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5543",
    "user": "https://github.com/aghitza"
}
```

I *love* the end result, it's so clean and simple (I wish there was a way to delete my old patches from this ticket, I'm somewhat embarrassed :)

Anyway, it works great and fast and it should be merged.



---

archive/issue_comments_005544.json:
```json
{
    "body": "Nick, Alex,\n\nam I correct to understand that I must only apply 903-ncalexan-charpoly-over-number-field-2.patch?\n\nit applies by itself and does build, and doctests fine. \n\nCheers,\n\nMichael",
    "created_at": "2008-04-15T20:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5544",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nick, Alex,

am I correct to understand that I must only apply 903-ncalexan-charpoly-over-number-field-2.patch?

it applies by itself and does build, and doctests fine. 

Cheers,

Michael



---

archive/issue_comments_005545.json:
```json
{
    "body": "Merged 903-ncalexan-charpoly-over-number-field-2.patch in Sage 3.0.alpha6 only. In case that is not what is intended please comment here and I will merge those patches.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-15T20:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5545",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 903-ncalexan-charpoly-over-number-field-2.patch in Sage 3.0.alpha6 only. In case that is not what is intended please comment here and I will merge those patches.

Cheers,

Michael



---

archive/issue_events_001019.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-15T20:30:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/903#event-1019"
}
```



---

archive/issue_comments_005546.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T20:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5546",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_005547.json:
```json
{
    "body": "Yes, that patch was the only one that needed merging.",
    "created_at": "2008-04-15T20:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/903#issuecomment-5547",
    "user": "https://github.com/aghitza"
}
```

Yes, that patch was the only one that needed merging.
