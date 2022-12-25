# Issue 6441: [with patch, needs review] Charpoly (plus adjoint and det)

archive/issues_006441.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: charpoly, division-free\n\n[Description of the problem]\n\nThere are some problems in SAGE 4.0.2 when computing characteristic polynomials, determinants and adjoint matrices over general rings or non-exact fields.  A more detailed description follows:\n\n  o Firstly, SAGE sometimes fails to compute the characteristic polynomial of a matrix over a ring which is not an integral domain.  Here is an example:\n    \n    sage: A = matrix(ZZ.quo(12), 3, [5,8,0,10,2,1,8,7,9])\n    sage: A\n    [ 5  8  0]\n    [10  2  1]\n    [ 8  7  9]\n    \n    The call \"A.charpoly()\" results in an error, specifically\n    \n    \"ArithmeticError: The inverse of 10 modulo 12 is not defined.\"\n    \n  o Secondly, when computing over non-exact fields like Qp sometimes the computation of the characteristic polynomial results in precision loss.\n    \n    sage: R = Zp(5, prec = 10, type = 'capped-abs', print_mode = 'series')\n    sage: MS = MatrixSpace(R, 10, 10)\n    sage: A = MS.random_element()\n    sage: A.charpoly()\n    \n    Often, this call results in a characteristic polynomial with coefficients of less precision than the base ring.  Sometimes (whenever the Hessenberg algorithm requires too many divisions in Zp with regards to the chosen precision), it also fails with the following error:\n    \n    ValueError: element valuation cannot be negative.\n\n  o Thirdly, in some cases the current implementation of charpoly is ridiculously slow (because of the use of the field of fractions in the Hessenberg algorithm).  Consider, for example, the following:\n    \n    sage: R.<t> = QQ[]\n    sage: A = matrix(R, [[-2*t^2 - t - 2, -t, t^2 - 3/2*t - 1, 1/2*t^2 - 4*t - 1, -t^2 - 9*t + 2], \\\n                             [-t^2 + 1/2, 7/233*t - 2, -4*t + 1/2, 3*t^2 + 3/2*t + 1, -t^2 - t], \\\n                             [t - 1, t^2 - 5/7*t - 1, 1/2*t - 1/2, 8*t^2 + t - 2/3, t + 1/2], \\\n                             [-t^2 + 11, -1/2*t - 1/4, 8*t^2 + t, 1, -1/4*t^2 + 1/2*t + 1/7], \\\n                             [3/2*t^2 + 5*t, 13/50*t^2 - 11*t + 1, -2*t^2 + t, -1, -1/2*t + 3/2]])\n    \n    (Sorry for the bad formatting.)  Computing the characteristic polynomial in SAGE via A.charpoly takes 91.12s on my laptop (Lenovo T500, Intel Centrino duo core), while the simple implementation of the generic division-free algorithm (attached to the ticket) takes only 0.01s.  During a quick (although not statistically sound) test with matrices in the above matrix space, the new code seemed to be faster by a factor between 1,000 and 10,000.\n\n  o For other reasons, namely using the expansion of co-factors, the computation of the determinant of a matrix over a general ring is also noticeably slow whenever the matrix has more than about 7 rows.  For example, with\n    \n    sage: A = random_matrix(PolynomialRing(QQ, 't'), 7, 7)\n\n    a call to ``A.det()`` takes about 0.5s.  For a random 8x8 matrix, the same call takes about 3s.  (And it gets worse very quickly in the expected way.)\n\n  o Also, just because it's possible, SAGE ought to be able to compute the characteristic polynomial, determinant and adjoint of square matrices over any ring (commutative with unity).  To give an example where this currently fails:\n    \n    sage: R.<a,b> = QQ[]\n    sage: S.<x,y> = R.quo(b^3)\n    sage: A = matrix(S, [[2,x<sup>2],[x</sup>3*y,x*y^2]])\n    sage: A\n    [    2   x^2]\n    [x^3*y x*y^2]\n\n    currently only ``A.det()`` works (and uses expansion by co-factors), but ``A.charpoly()`` throws a ``NotImplementedError`` (because SAGE does not create the univariate polynomial ring over ``S``, because the test whether S is a field passes on an exception as the ideal throws an exception when it is asked about maximality) and ``A.adjoint()`` throws\n\n    NotImplementedError: computation of adjoint not implemented in general yet\n\n[Suggested fix]\n\nImplement a generic division-free algorithm for the characteristic polynomial (and then use this to work out the adjoint, and read off the determinant).\n\n[Problematic points]\n\n- Adjusting current code that calls charpoly, det or adjoint:\n\nTo quickly mention the latter: in the file matrix2.pyx I simply implemented _adjoint(self), since inheriting classes overwrite this.\n\nThe calls to charpoly can choose an algorithm (as before, although it wasn't really used since there wasn't any choice).  This problem thus translates to choosing the most sensible defaults (possibly depending on whether something is a number field, or an exact field, etc) in the implementation of charpoly, and to go through all the calls of charpoly in the current code, to check what the desired behaviour is.  This question only arises as the Hessenberg algorithm runs in time O(n^3) whereas the division-free algorithm implemented here runs in time O(n^4).  Thus the division-free algorithm wouldn't necessarily be the right choice between these two in all cases.\n\nIn the case of number fields (PARI) or exact fields (Hessenberg form) or Z/nZ (lift to Z), the choice is pretty clear.  The same holds in cases where this wasn't implemented before.  I think the only remaining cases for which there may or may not be an obvious (at least to me!) choice are non-exact fields like R or Qp (and their extensions).  Then it's basically a choice between speed (and managing precision as the caller by ensuring one has good bounds on the input) or guaranteed precision.\n\nApart from one instance instance related to modular forms, where I could speak to David Loeffler at SAGE Days 16 and then added the paramater algorithm=\"hessenberg\" to the call, I haven't changed the calls to charpoly anywhere.\n\nThe implementation of determinant reflects this somewhat, although it is no real problem since in the patch the logic of determinant hasn't changed.  The only difference is that the \"last resort\" algorithm using expansion by co-factors has been replaced by the generic computation of the characteristic polynomial (from which one can then read off the determinant), i.e., this has no downside (apart from a tiny problem with symbolic expression rings, as we now need to specify a variable name for the characteristic polynomial, see below).\n\n- A strange problem with symbolic rings:\n\nThe characteristic polynomial needs to have a variable name specified.  This gives an intrinsic problem when computing the determinant (a method which does not require the user to add a variable name as input, and rightfully so shouldn't!) over symbolic rings, as one needs to choose a variable name for the characteristic polynomial different from the already existing symbols or else the computed result will be meaningless.  At SAGE Days 16, Martin Albrecht and I briefly tried a quick way around this (by asking the symbolic expression ring for all symbols, and then forming a new one by concatenating them all, thereby always generating a new symbol), however, this idea did not work out.  Thus at the moment, the fixed choice of the symbol \"A0123456789\" appears hardcoded.\n\nPS: I think the inability of SAGE to compute these three quantities over all rings, even for small-ish matrices, could be potentially offputting for beginners, so I was tempted to choose \"Priority=major\", but then again, it doesn't seem to be a lot of work to fix this.  This is my first ticket to I don't really know how to choose the priority and just went with \"minor\", hope that's OK.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6441\n\n",
    "created_at": "2009-06-28T17:50:33Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] Charpoly (plus adjoint and det)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6441",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```
Assignee: somebody

Keywords: charpoly, division-free

[Description of the problem]

There are some problems in SAGE 4.0.2 when computing characteristic polynomials, determinants and adjoint matrices over general rings or non-exact fields.  A more detailed description follows:

  o Firstly, SAGE sometimes fails to compute the characteristic polynomial of a matrix over a ring which is not an integral domain.  Here is an example:
    
    sage: A = matrix(ZZ.quo(12), 3, [5,8,0,10,2,1,8,7,9])
    sage: A
    [ 5  8  0]
    [10  2  1]
    [ 8  7  9]
    
    The call "A.charpoly()" results in an error, specifically
    
    "ArithmeticError: The inverse of 10 modulo 12 is not defined."
    
  o Secondly, when computing over non-exact fields like Qp sometimes the computation of the characteristic polynomial results in precision loss.
    
    sage: R = Zp(5, prec = 10, type = 'capped-abs', print_mode = 'series')
    sage: MS = MatrixSpace(R, 10, 10)
    sage: A = MS.random_element()
    sage: A.charpoly()
    
    Often, this call results in a characteristic polynomial with coefficients of less precision than the base ring.  Sometimes (whenever the Hessenberg algorithm requires too many divisions in Zp with regards to the chosen precision), it also fails with the following error:
    
    ValueError: element valuation cannot be negative.

  o Thirdly, in some cases the current implementation of charpoly is ridiculously slow (because of the use of the field of fractions in the Hessenberg algorithm).  Consider, for example, the following:
    
    sage: R.<t> = QQ[]
    sage: A = matrix(R, [[-2*t^2 - t - 2, -t, t^2 - 3/2*t - 1, 1/2*t^2 - 4*t - 1, -t^2 - 9*t + 2], \
                             [-t^2 + 1/2, 7/233*t - 2, -4*t + 1/2, 3*t^2 + 3/2*t + 1, -t^2 - t], \
                             [t - 1, t^2 - 5/7*t - 1, 1/2*t - 1/2, 8*t^2 + t - 2/3, t + 1/2], \
                             [-t^2 + 11, -1/2*t - 1/4, 8*t^2 + t, 1, -1/4*t^2 + 1/2*t + 1/7], \
                             [3/2*t^2 + 5*t, 13/50*t^2 - 11*t + 1, -2*t^2 + t, -1, -1/2*t + 3/2]])
    
    (Sorry for the bad formatting.)  Computing the characteristic polynomial in SAGE via A.charpoly takes 91.12s on my laptop (Lenovo T500, Intel Centrino duo core), while the simple implementation of the generic division-free algorithm (attached to the ticket) takes only 0.01s.  During a quick (although not statistically sound) test with matrices in the above matrix space, the new code seemed to be faster by a factor between 1,000 and 10,000.

  o For other reasons, namely using the expansion of co-factors, the computation of the determinant of a matrix over a general ring is also noticeably slow whenever the matrix has more than about 7 rows.  For example, with
    
    sage: A = random_matrix(PolynomialRing(QQ, 't'), 7, 7)

    a call to ``A.det()`` takes about 0.5s.  For a random 8x8 matrix, the same call takes about 3s.  (And it gets worse very quickly in the expected way.)

  o Also, just because it's possible, SAGE ought to be able to compute the characteristic polynomial, determinant and adjoint of square matrices over any ring (commutative with unity).  To give an example where this currently fails:
    
    sage: R.<a,b> = QQ[]
    sage: S.<x,y> = R.quo(b^3)
    sage: A = matrix(S, [[2,x<sup>2],[x</sup>3*y,x*y^2]])
    sage: A
    [    2   x^2]
    [x^3*y x*y^2]

    currently only ``A.det()`` works (and uses expansion by co-factors), but ``A.charpoly()`` throws a ``NotImplementedError`` (because SAGE does not create the univariate polynomial ring over ``S``, because the test whether S is a field passes on an exception as the ideal throws an exception when it is asked about maximality) and ``A.adjoint()`` throws

    NotImplementedError: computation of adjoint not implemented in general yet

[Suggested fix]

Implement a generic division-free algorithm for the characteristic polynomial (and then use this to work out the adjoint, and read off the determinant).

[Problematic points]

- Adjusting current code that calls charpoly, det or adjoint:

To quickly mention the latter: in the file matrix2.pyx I simply implemented _adjoint(self), since inheriting classes overwrite this.

The calls to charpoly can choose an algorithm (as before, although it wasn't really used since there wasn't any choice).  This problem thus translates to choosing the most sensible defaults (possibly depending on whether something is a number field, or an exact field, etc) in the implementation of charpoly, and to go through all the calls of charpoly in the current code, to check what the desired behaviour is.  This question only arises as the Hessenberg algorithm runs in time O(n^3) whereas the division-free algorithm implemented here runs in time O(n^4).  Thus the division-free algorithm wouldn't necessarily be the right choice between these two in all cases.

In the case of number fields (PARI) or exact fields (Hessenberg form) or Z/nZ (lift to Z), the choice is pretty clear.  The same holds in cases where this wasn't implemented before.  I think the only remaining cases for which there may or may not be an obvious (at least to me!) choice are non-exact fields like R or Qp (and their extensions).  Then it's basically a choice between speed (and managing precision as the caller by ensuring one has good bounds on the input) or guaranteed precision.

Apart from one instance instance related to modular forms, where I could speak to David Loeffler at SAGE Days 16 and then added the paramater algorithm="hessenberg" to the call, I haven't changed the calls to charpoly anywhere.

The implementation of determinant reflects this somewhat, although it is no real problem since in the patch the logic of determinant hasn't changed.  The only difference is that the "last resort" algorithm using expansion by co-factors has been replaced by the generic computation of the characteristic polynomial (from which one can then read off the determinant), i.e., this has no downside (apart from a tiny problem with symbolic expression rings, as we now need to specify a variable name for the characteristic polynomial, see below).

- A strange problem with symbolic rings:

The characteristic polynomial needs to have a variable name specified.  This gives an intrinsic problem when computing the determinant (a method which does not require the user to add a variable name as input, and rightfully so shouldn't!) over symbolic rings, as one needs to choose a variable name for the characteristic polynomial different from the already existing symbols or else the computed result will be meaningless.  At SAGE Days 16, Martin Albrecht and I briefly tried a quick way around this (by asking the symbolic expression ring for all symbols, and then forming a new one by concatenating them all, thereby always generating a new symbol), however, this idea did not work out.  Thus at the moment, the fixed choice of the symbol "A0123456789" appears hardcoded.

PS: I think the inability of SAGE to compute these three quantities over all rings, even for small-ish matrices, could be potentially offputting for beginners, so I was tempted to choose "Priority=major", but then again, it doesn't seem to be a lot of work to fix this.  This is my first ticket to I don't really know how to choose the priority and just went with "minor", hope that's OK.

Issue created by migration from https://trac.sagemath.org/ticket/6441





---

archive/issue_comments_051600.json:
```json
{
    "body": "Attachment [dfmatrix.patch](tarball://root/attachments/some-uuid/ticket6441/dfmatrix.patch) by spancratz created at 2009-06-28 17:51:57\n\nCode for division-free matrix computations",
    "created_at": "2009-06-28T17:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51600",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [dfmatrix.patch](tarball://root/attachments/some-uuid/ticket6441/dfmatrix.patch) by spancratz created at 2009-06-28 17:51:57

Code for division-free matrix computations



---

archive/issue_comments_051601.json:
```json
{
    "body": "Hi Sebastian,\n\nThis is a great discussion that you might want to consider including portions of on sage-devel for everybody to see.  You can include a link to Trac for folks who want to peruse the details on the fix.\n\nAlso, there is a \"linear algebra\" component that might be more appropriate than the \"algebra\" component.\n\nI'll take a look at the patch today or tomorrow as I get a chance.\n\nRob",
    "created_at": "2009-06-29T20:36:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51601",
    "user": "https://github.com/rbeezer"
}
```

Hi Sebastian,

This is a great discussion that you might want to consider including portions of on sage-devel for everybody to see.  You can include a link to Trac for folks who want to peruse the details on the fix.

Also, there is a "linear algebra" component that might be more appropriate than the "algebra" component.

I'll take a look at the patch today or tomorrow as I get a chance.

Rob



---

archive/issue_comments_051602.json:
```json
{
    "body": "Hi Sebastian,\n\nthis looks quite nice. I just looked at it quickly so it's not a full review, but it seems you could use on dimension less for F (in F[p,t], t is useless) , A (in A[k,t], t is useless) and a (in a[u][v][w], [v] is useless).\n\n  Yann",
    "created_at": "2009-06-29T20:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51602",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Hi Sebastian,

this looks quite nice. I just looked at it quickly so it's not a full review, but it seems you could use on dimension less for F (in F[p,t], t is useless) , A (in A[k,t], t is useless) and a (in a[u][v][w], [v] is useless).

  Yann



---

archive/issue_comments_051603.json:
```json
{
    "body": "Sebastian,\n\nHaving these algorithms in Sage will a great addition.  Any chance you have an electronic copy of [Se02] you might be able to send me (at beezer`@`ups.edu)?  It'd make it easier to review the main chunks of new code.\n\nOn a first pass, I've noticed a few things with Sage style and procedures that need attention.  Not the fun stuff, but required to get code included.  In no real order.\n\n1.  In docstrings, lists don't need blank lines to split them, and sublists (like the choices for \"algorithm\" options) should be indented (ala Python code) to make them render properly.\n\n2.  Constructions like ``\"hessenberg\"`` would not usually include the inner quotes, I think, though I can see the argument for including them.  In any event, I can't recall seeing them before.  The back-quotes will cause different formatting anyway.\n\n3.  There was just a discussion on sage-devel about style on error messages.  No period on the end. (\"self must be a square matrix.\" for one `ArithemticError`)  I've been inclined to use `ValueError` in a case like a matrix of the wrong shape.\n\n4.  In docstrings the :: always begins a verbatim block, but it is \"smart\" and behaves 3 ways.\n\n(a)  On a line all by itself, then doesn't appear in output.\n\n(b)  At end of a sentence with no space, then output as a single semi-colon (like on TESTS::).\n\n(c)  At end of sentence, with space between, then no output.\n\n\nSo you have several places where you can replace a couple of blank lines and a :: line by just using placing :: after a preceding sentence with space.\n\n5.  No need to write INPUT:: if there isn't any.  I saw one \"Tests\" that needed capitalization.\n\n6.  A big one - every function needs a doctest, even underscore functions.  You can meet the letter of the law, or work hard to make tests that will expose broken code when others \"improve\" your work or other places.  For example, `_is_certainly_integral_domain` needs doctests (which in this particular case might test a case that is True and a case that is False).\n\n7.  I like lots of author's names in the files, but they also migrate to the reference manual, where minor changes don't really need reporting and I think clutter up the manual.  I like the names in the source so I know who to go to with questions.  So maybe go for a bit more balance and *do* include your name on the new big routines and the places where they have a big impact, and perhaps not in places where minor changes are needed in doctests.  In theory, the Mercurial log and Trac can be used to chase down the origin of minor changes.\n\n8.  `sage -docbuild reference html`\n\nwill rebuild the HTML reference manual.  First time takes a while, but subsequent uses just update changed files.  This is a good way to see what the docstrings become (and something any reviewer should be checking).\n\n9.  `sage -coverage <file>`\n\nwill give you a doctest coverage report - again, something a reviewer will be checking.\n\nI'll continue looking at the code, but I thought I'd pass these along right away.  Since this is your first patch, I hope you don't mind all the advice on the mundane (yet important) stuff.  This looks like a very solid first contribution, and as I said above, will be very welcome in Sage.\n\nRob",
    "created_at": "2009-06-30T03:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51603",
    "user": "https://github.com/rbeezer"
}
```

Sebastian,

Having these algorithms in Sage will a great addition.  Any chance you have an electronic copy of [Se02] you might be able to send me (at beezer`@`ups.edu)?  It'd make it easier to review the main chunks of new code.

On a first pass, I've noticed a few things with Sage style and procedures that need attention.  Not the fun stuff, but required to get code included.  In no real order.

1.  In docstrings, lists don't need blank lines to split them, and sublists (like the choices for "algorithm" options) should be indented (ala Python code) to make them render properly.

2.  Constructions like ``"hessenberg"`` would not usually include the inner quotes, I think, though I can see the argument for including them.  In any event, I can't recall seeing them before.  The back-quotes will cause different formatting anyway.

3.  There was just a discussion on sage-devel about style on error messages.  No period on the end. ("self must be a square matrix." for one `ArithemticError`)  I've been inclined to use `ValueError` in a case like a matrix of the wrong shape.

4.  In docstrings the :: always begins a verbatim block, but it is "smart" and behaves 3 ways.

(a)  On a line all by itself, then doesn't appear in output.

(b)  At end of a sentence with no space, then output as a single semi-colon (like on TESTS::).

(c)  At end of sentence, with space between, then no output.


So you have several places where you can replace a couple of blank lines and a :: line by just using placing :: after a preceding sentence with space.

5.  No need to write INPUT:: if there isn't any.  I saw one "Tests" that needed capitalization.

6.  A big one - every function needs a doctest, even underscore functions.  You can meet the letter of the law, or work hard to make tests that will expose broken code when others "improve" your work or other places.  For example, `_is_certainly_integral_domain` needs doctests (which in this particular case might test a case that is True and a case that is False).

7.  I like lots of author's names in the files, but they also migrate to the reference manual, where minor changes don't really need reporting and I think clutter up the manual.  I like the names in the source so I know who to go to with questions.  So maybe go for a bit more balance and *do* include your name on the new big routines and the places where they have a big impact, and perhaps not in places where minor changes are needed in doctests.  In theory, the Mercurial log and Trac can be used to chase down the origin of minor changes.

8.  `sage -docbuild reference html`

will rebuild the HTML reference manual.  First time takes a while, but subsequent uses just update changed files.  This is a good way to see what the docstrings become (and something any reviewer should be checking).

9.  `sage -coverage <file>`

will give you a doctest coverage report - again, something a reviewer will be checking.

I'll continue looking at the code, but I thought I'd pass these along right away.  Since this is your first patch, I hope you don't mind all the advice on the mundane (yet important) stuff.  This looks like a very solid first contribution, and as I said above, will be very welcome in Sage.

Rob



---

archive/issue_comments_051604.json:
```json
{
    "body": "Sebastian,\n\nI got my hands on a copy of the paper, so ignore my request above.  Thanks.\n\nRob",
    "created_at": "2009-07-01T20:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51604",
    "user": "https://github.com/rbeezer"
}
```

Sebastian,

I got my hands on a copy of the paper, so ignore my request above.  Thanks.

Rob



---

archive/issue_comments_051605.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2009-07-05T08:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51605",
    "user": "https://github.com/loefflerd"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_051606.json:
```json
{
    "body": "Dear Rob,\n\nThanks for taking up the review.  I am sorry for the delayed reply --- I was racing at the Tour of Wales for the last five days and am only back in Oxford now.  That said, I'll try to get back to you about all the points as soon as possible.\n\n1.  That makes sense; I just went through the file sage/matrix/matrix2.pyx and tried to make these changes whenever suitable.\n\n2.  I wasn't quite sure about this when writing the comments in the first place, but when looking at the code I think I saw three different ways to put this:  no inner quotation marks, double inner quotation marks \", and single inner quotation marks '.  Thus I haven't changed this yet.\n\n3.  I've removed the periods at the of the error messages.  Moreover, I agree it should be a ValueError instead of an ArithmeticError.  I've also changed this in other methods in the same file, which I didn't changed before.\n\n4.  Again, I went through the whole file and hopefully made suitable changes.\n\n5.  Done.\n\n6.  I still need to do this.\n\n7.  That makes sense.  I still have to do that.\n\n8.  Actually, this did not work the last couple of times I tried.  The problem seems to be that SAGE (although it is set up to use the clone \"sage-seb\") tries to build the documentation from \"sage-main\".  So while I'd be happy to build the documentation and check everything is formatted properly, I don't know how to do this.\n\n9.  Sure, I'll do this once I have made all these changes.\n\nOf course, I don't mind the advice at all, thank you very much!  Actually, I think it's much easier to have these points spelled out explicitly at least once...\n\nI'll try make the suggested changes and attach a new file to this thread during the next few days.\n\nMany thanks,\n\nSebastian",
    "created_at": "2009-07-07T00:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51606",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Dear Rob,

Thanks for taking up the review.  I am sorry for the delayed reply --- I was racing at the Tour of Wales for the last five days and am only back in Oxford now.  That said, I'll try to get back to you about all the points as soon as possible.

1.  That makes sense; I just went through the file sage/matrix/matrix2.pyx and tried to make these changes whenever suitable.

2.  I wasn't quite sure about this when writing the comments in the first place, but when looking at the code I think I saw three different ways to put this:  no inner quotation marks, double inner quotation marks ", and single inner quotation marks '.  Thus I haven't changed this yet.

3.  I've removed the periods at the of the error messages.  Moreover, I agree it should be a ValueError instead of an ArithmeticError.  I've also changed this in other methods in the same file, which I didn't changed before.

4.  Again, I went through the whole file and hopefully made suitable changes.

5.  Done.

6.  I still need to do this.

7.  That makes sense.  I still have to do that.

8.  Actually, this did not work the last couple of times I tried.  The problem seems to be that SAGE (although it is set up to use the clone "sage-seb") tries to build the documentation from "sage-main".  So while I'd be happy to build the documentation and check everything is formatted properly, I don't know how to do this.

9.  Sure, I'll do this once I have made all these changes.

Of course, I don't mind the advice at all, thank you very much!  Actually, I think it's much easier to have these points spelled out explicitly at least once...

I'll try make the suggested changes and attach a new file to this thread during the next few days.

Many thanks,

Sebastian



---

archive/issue_comments_051607.json:
```json
{
    "body": "Hi Sebastian,\n\nCycle racing?  Following in Cavendish's footsteps?  ;-)\n\nQuoting (2), and author's names (7), are open to debate, so don't take my word as gospel.  I keep threatening to write up something that will help folks through this sort of thing on their first attempt.  I know a lot was a mystery to me first time through.\n\n(8) Building the docs, try:\n\nsage -br  # reports which branch you are really using\n\nsage -b   # should touch (copy, really) changed files in branch\n\nsage -docbuild reference html  # do it\n\n\nI have one (small) Sage routine I am working on myself right now, then I'll give this much more attention.  I read through [Se02] and was a bit put off by the notation, but I'll knuckle down and try to make some sense of that as well.  So, I'll attend to this, but I'm in no great rush, so just put up a patch when you're not racing.\n\nRob",
    "created_at": "2009-07-07T05:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51607",
    "user": "https://github.com/rbeezer"
}
```

Hi Sebastian,

Cycle racing?  Following in Cavendish's footsteps?  ;-)

Quoting (2), and author's names (7), are open to debate, so don't take my word as gospel.  I keep threatening to write up something that will help folks through this sort of thing on their first attempt.  I know a lot was a mystery to me first time through.

(8) Building the docs, try:

sage -br  # reports which branch you are really using

sage -b   # should touch (copy, really) changed files in branch

sage -docbuild reference html  # do it


I have one (small) Sage routine I am working on myself right now, then I'll give this much more attention.  I read through [Se02] and was a bit put off by the notation, but I'll knuckle down and try to make some sense of that as well.  So, I'll attend to this, but I'm in no great rush, so just put up a patch when you're not racing.

Rob



---

archive/issue_comments_051608.json:
```json
{
    "body": "Dear Rob,\n\nThanks for the quick reply. Re cycling, well, I only started at the age of 24, but we'll see ;).\n\nI've attached a new patch to this thread, hopefully that incorporates all the necessary changes.\n\nRe (3), I've now turned most errors about square matrices into \"ValueError?\"s, although when I chased the through inheriting classes, I noticed that there is somewhat of an inconsistency, where in similar places any one of ValueError?, ArithmeticError? or TypeError? is being used.\n\nRe (9), well, all the methods I've written or changed have documentations and tests attached to them now, although in some files I touched (e.g. matrix/matrix2.pyx) there are still methods without documentation, although I didn't change or even look at them and so won't do anything about this.\n\nConcerning the paper describing the article, I guess one way of reading it is going through it and trying to understand it. Alternatively, what would be very easy is to read Algorithm 3.1 and compare that to the implementation in the patch.\n\nKind regards,\n\nSebastian",
    "created_at": "2009-07-07T16:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51608",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Dear Rob,

Thanks for the quick reply. Re cycling, well, I only started at the age of 24, but we'll see ;).

I've attached a new patch to this thread, hopefully that incorporates all the necessary changes.

Re (3), I've now turned most errors about square matrices into "ValueError?"s, although when I chased the through inheriting classes, I noticed that there is somewhat of an inconsistency, where in similar places any one of ValueError?, ArithmeticError? or TypeError? is being used.

Re (9), well, all the methods I've written or changed have documentations and tests attached to them now, although in some files I touched (e.g. matrix/matrix2.pyx) there are still methods without documentation, although I didn't change or even look at them and so won't do anything about this.

Concerning the paper describing the article, I guess one way of reading it is going through it and trying to understand it. Alternatively, what would be very easy is to read Algorithm 3.1 and compare that to the implementation in the patch.

Kind regards,

Sebastian



---

archive/issue_comments_051609.json:
```json
{
    "body": "Updated patch (20090707)",
    "created_at": "2009-07-07T16:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51609",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Updated patch (20090707)



---

archive/issue_comments_051610.json:
```json
{
    "body": "Attachment [dfmatrix20090707.patch](tarball://root/attachments/some-uuid/ticket6441/dfmatrix20090707.patch) by @rbeezer created at 2009-08-05 06:47:55\n\nHi Sebastian,\n\n1.  I understand [Se02] a lot better now - well enough to have caught the typo in Algorithm 3.1 (missing minus sign before last term in penultimate line).  That might be a good thing to mention in the docstring near the citation.\n\n2.  So I should be OK with `_charpoly_df()` now.  One question, why did you choose to accumulate for sums using a construction like the following?\n\n\n```\nfor k in xrange(p): \n    F.set_unsafe(p, t, F.get_unsafe(p, t) - A.get_unsafe(k, t) * F.get_unsafe(p-k-1, t))\n```\n\n\nA few lines above you used a temporary variable `s`, which is what I would have expected later.  Just wondering about the rationale?\n\n3.  I'm not sure `_is_certainly_field()` (and its integral domain companion) are the best way around the \"not-implemented\" problem.  I see the problem, and understand the fix, but I'd rather see fewer global functions in Sage and more object methods.  And I am familiar with the linear algebra routines, but less familiar with design decisions for rings.  Would you mind presenting the problem (and perhaps your solution) on sage-devel and see if there is a cleaner way to solve it or some kind of explanation?  Or perhaps your solution is the best idea.  Me, I'd probably just try to handle the exception where it happens rather than make a function that looks so much like `is_field()`, but isn't really the same at all.\n\n\n4.  You've included lots of formatting fixes - which is fantastic.  But Sage likes to have small patches that address one thing.  How hard would it be for you to separate the documentation clean-up from the division-free stuff?  For example, right now, it is hard to notice where your changes to the determinant have affected doctests in unrelated modules, since they are mixed in with lots of other small changes.  You could put the formatting fixes in a new ticket (e.g. \"docstring clean-up for matrices\"), and I could review that patch very quickly.  Then when somebody comes back to look at the df stuff, they can see exactly what changed, while nobody will probably ever look at the dosctring clean-up patch again.  and you'll get credit for two patches.  ;-)\n\n\nAs I've said, this is a great addition to Sage and very carefully done, which is really appreciated.  None of the above will keep me from looking at this some more in the next couple of days, so at your leisure.\n\nRob",
    "created_at": "2009-08-05T06:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51610",
    "user": "https://github.com/rbeezer"
}
```

Attachment [dfmatrix20090707.patch](tarball://root/attachments/some-uuid/ticket6441/dfmatrix20090707.patch) by @rbeezer created at 2009-08-05 06:47:55

Hi Sebastian,

1.  I understand [Se02] a lot better now - well enough to have caught the typo in Algorithm 3.1 (missing minus sign before last term in penultimate line).  That might be a good thing to mention in the docstring near the citation.

2.  So I should be OK with `_charpoly_df()` now.  One question, why did you choose to accumulate for sums using a construction like the following?


```
for k in xrange(p): 
    F.set_unsafe(p, t, F.get_unsafe(p, t) - A.get_unsafe(k, t) * F.get_unsafe(p-k-1, t))
```


A few lines above you used a temporary variable `s`, which is what I would have expected later.  Just wondering about the rationale?

3.  I'm not sure `_is_certainly_field()` (and its integral domain companion) are the best way around the "not-implemented" problem.  I see the problem, and understand the fix, but I'd rather see fewer global functions in Sage and more object methods.  And I am familiar with the linear algebra routines, but less familiar with design decisions for rings.  Would you mind presenting the problem (and perhaps your solution) on sage-devel and see if there is a cleaner way to solve it or some kind of explanation?  Or perhaps your solution is the best idea.  Me, I'd probably just try to handle the exception where it happens rather than make a function that looks so much like `is_field()`, but isn't really the same at all.


4.  You've included lots of formatting fixes - which is fantastic.  But Sage likes to have small patches that address one thing.  How hard would it be for you to separate the documentation clean-up from the division-free stuff?  For example, right now, it is hard to notice where your changes to the determinant have affected doctests in unrelated modules, since they are mixed in with lots of other small changes.  You could put the formatting fixes in a new ticket (e.g. "docstring clean-up for matrices"), and I could review that patch very quickly.  Then when somebody comes back to look at the df stuff, they can see exactly what changed, while nobody will probably ever look at the dosctring clean-up patch again.  and you'll get credit for two patches.  ;-)


As I've said, this is a great addition to Sage and very carefully done, which is really appreciated.  None of the above will keep me from looking at this some more in the next couple of days, so at your leisure.

Rob



---

archive/issue_comments_051611.json:
```json
{
    "body": "Changing the summary in light of Rob's latest review.  It would be great to be able to get this in soon.",
    "created_at": "2009-08-16T08:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51611",
    "user": "https://github.com/aghitza"
}
```

Changing the summary in light of Rob's latest review.  It would be great to be able to get this in soon.



---

archive/issue_comments_051612.json:
```json
{
    "body": "Hi Sebastian,\nmy last remark might have been unclear, but look at this:\n\n```\ndef charpoly_divfree(M):\n\tn = M.ncols()\n\tR  = M.base_ring() \n\tS  = PolynomialRing(R, 'x') \n\n\tF = [ R(0) for i in xrange(n) ]\n\ta = [[R(0) for i in xrange(n)] for p in xrange(n-1)] \n\tA = [ R(0) for i in xrange(n) ]\n\n\tF[0] = - M[0, 0]\n\n\tfor t in xrange(1,n):\n\t\tfor i in xrange(t+1):\n\t\t\ta[0][i] = M[i, t]\n\t\tA[0] = M[t, t]\n\t\tfor p in xrange(1, t): \n\t\t\tapm=a[p-1]\n\t\t\tfor i in xrange(t+1): \n\t\t\t\ts = R(0) \n\t\t\t\tfor j in xrange(t+1): \n\t\t\t\t\ts += M[i, j] * apm[j] \n\t\t\t\ta[p][i] = s\n\t\t\tA[p] = a[p][t]\n\t\tatm=a[t-1]\n\t\tfor j in xrange(t+1):\n\t\t\tA[t] += M[t, j] * atm[j]\n\t\tfor p in xrange(t+1):\n\t\t\tfor k in xrange(p): \n\t\t\t\tF[p] -= A[k] * F[p-k-1]\n\t\t\tF[p] -= A[p]\n\n\tF.reverse()\n\tF.append(R(1))\n\treturn S(F)\n```\n\nthis works, with smaller F,A,a using n**2 memory instead of n**3...\n\nYann",
    "created_at": "2009-08-16T10:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51612",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Hi Sebastian,
my last remark might have been unclear, but look at this:

```
def charpoly_divfree(M):
	n = M.ncols()
	R  = M.base_ring() 
	S  = PolynomialRing(R, 'x') 

	F = [ R(0) for i in xrange(n) ]
	a = [[R(0) for i in xrange(n)] for p in xrange(n-1)] 
	A = [ R(0) for i in xrange(n) ]

	F[0] = - M[0, 0]

	for t in xrange(1,n):
		for i in xrange(t+1):
			a[0][i] = M[i, t]
		A[0] = M[t, t]
		for p in xrange(1, t): 
			apm=a[p-1]
			for i in xrange(t+1): 
				s = R(0) 
				for j in xrange(t+1): 
					s += M[i, j] * apm[j] 
				a[p][i] = s
			A[p] = a[p][t]
		atm=a[t-1]
		for j in xrange(t+1):
			A[t] += M[t, j] * atm[j]
		for p in xrange(t+1):
			for k in xrange(p): 
				F[p] -= A[k] * F[p-k-1]
			F[p] -= A[p]

	F.reverse()
	F.append(R(1))
	return S(F)
```

this works, with smaller F,A,a using n**2 memory instead of n**3...

Yann



---

archive/issue_comments_051613.json:
```json
{
    "body": "Sebastian,\n\nI'll second Yann's suggestion above.  The arrays a, A and F all have the index t fixed in the second location, and the F array is initalized each time t increments with its previous values, so these values can just rollover.  Thus these main arrays this could all be one dimension smaller, notably a.  Then the storage requirement for the algorithm is roughly the same as for the matrix (assuming it is dense), rather than being a factor of n larger, which could be problematic for very large matrices.  And the code seems correspondingly simpler to read and understand.\n\nI've looked over how this gets used (determinant, adjoint, etc) and if the main algorithm and its effects were isolated in a patch separate from the unrelated documentation clean-ups then I ought to be able to finish off the review without too much more work.\n\nRob",
    "created_at": "2009-08-18T06:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51613",
    "user": "https://github.com/rbeezer"
}
```

Sebastian,

I'll second Yann's suggestion above.  The arrays a, A and F all have the index t fixed in the second location, and the F array is initalized each time t increments with its previous values, so these values can just rollover.  Thus these main arrays this could all be one dimension smaller, notably a.  Then the storage requirement for the algorithm is roughly the same as for the matrix (assuming it is dense), rather than being a factor of n larger, which could be problematic for very large matrices.  And the code seems correspondingly simpler to read and understand.

I've looked over how this gets used (determinant, adjoint, etc) and if the main algorithm and its effects were isolated in a patch separate from the unrelated documentation clean-ups then I ought to be able to finish off the review without too much more work.

Rob



---

archive/issue_comments_051614.json:
```json
{
    "body": "Dear Rob and Yann,\n\nThis is only a brief note to let you know that I have read your comments, and that I should be able to work on this in the next few days.\n\nKind regards,\n\nSebastian",
    "created_at": "2009-08-19T16:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51614",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Dear Rob and Yann,

This is only a brief note to let you know that I have read your comments, and that I should be able to work on this in the next few days.

Kind regards,

Sebastian



---

archive/issue_comments_051615.json:
```json
{
    "body": "Replying to [comment:14 spancratz]:\n> This is only a brief note to let you know that I have read your comments, and that I should be able to work on this in the next few days.\n\nThanks, Sebastian.  Despite my slothfulness on this one, the more I look at it, the more I'm motivated to get into Sage sooner rather than later.\n\nSaw some good applications for this in Chris Godsil's graph theory talk today at the Univ of Washington - the slides just got posted on sage-devel and the wiki.\n\nRob",
    "created_at": "2009-08-20T01:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51615",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:14 spancratz]:
> This is only a brief note to let you know that I have read your comments, and that I should be able to work on this in the next few days.

Thanks, Sebastian.  Despite my slothfulness on this one, the more I look at it, the more I'm motivated to get into Sage sooner rather than later.

Saw some good applications for this in Chris Godsil's graph theory talk today at the Univ of Washington - the slides just got posted on sage-devel and the wiki.

Rob



---

archive/issue_comments_051616.json:
```json
{
    "body": "I think I've now separated the changes and am attaching a patch to this message, containing only the new method \"_charpoly_df\" and all necessary changes to make everything work and see the doctests pass.  At the moment, the question whether a ring is a field (or an integral domain) is still handled in the same way as in the other patch.  I think that in principle this is the right way to handle this (because the problem comes up in other similar places, too, for example when creating vectors over certain rings), but in the next few days I'll post something to sage-devel to have a discussion there.\n\nAbout the attached patch file, all the doctests pass, but when building the reference manual there are three warnings, and it seems (I put it this way because I don't know much about it) as if it does have to do with the file sage/matrix/matrix2.pyx.  The warning messages say something about indentation of some docstrings, but when looking at those I could not find any problems.  Perhaps you could have a quick look at this?\n\nI'll sort out the other miscellaneous changes that got mixed in with this in the earlier patch file at some later point.\n\nPlease let me know if there is anything else you want me to change about this.\n\nSebastian",
    "created_at": "2009-08-21T22:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51616",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

I think I've now separated the changes and am attaching a patch to this message, containing only the new method "_charpoly_df" and all necessary changes to make everything work and see the doctests pass.  At the moment, the question whether a ring is a field (or an integral domain) is still handled in the same way as in the other patch.  I think that in principle this is the right way to handle this (because the problem comes up in other similar places, too, for example when creating vectors over certain rings), but in the next few days I'll post something to sage-devel to have a discussion there.

About the attached patch file, all the doctests pass, but when building the reference manual there are three warnings, and it seems (I put it this way because I don't know much about it) as if it does have to do with the file sage/matrix/matrix2.pyx.  The warning messages say something about indentation of some docstrings, but when looking at those I could not find any problems.  Perhaps you could have a quick look at this?

I'll sort out the other miscellaneous changes that got mixed in with this in the earlier patch file at some later point.

Please let me know if there is anything else you want me to change about this.

Sebastian



---

archive/issue_comments_051617.json:
```json
{
    "body": "Division-free matrix computations (20090821)",
    "created_at": "2009-08-21T22:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51617",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Division-free matrix computations (20090821)



---

archive/issue_comments_051618.json:
```json
{
    "body": "Attachment [20090821_Charpoly.patch](tarball://root/attachments/some-uuid/ticket6441/20090821_Charpoly.patch) by @rbeezer created at 2009-08-22 05:11:51\n\nHi Sebastian,\n\nI've been using this routine to explore some characteristic polynomials with symbolic coefficients that Chris Godsil is interested in for graph theory.  Its great to have this efficient routine available.  It also seems that this latest version is about twice as fast as the first one, so the revisions here are providing a real speed-up.\n\n1.  Documentation warnings:  I only got two warnings from matrix2.pyx.  In the docstring for `adjoint()` the description of `N` as input has its second line aligned relative to the second dash, where it is the text off the first dash that sets the indent location.   In the docstring for `charpoly()` the line that begins `If an algorithm is specified explicitly,...` needs to be pulled left to align properly.\n\nThe warnings you get when you build the documentation tell you the file and the method where it happens, then there is a line number, which is relative to the start of that particular docstring and give the location (roughly - plus/minus a line?).  If you still have a third warning, maybe you can locate it this way to help figure out the problem (or post the location here).\n\n2.  Patch failures:  I had two parts of the patch which failed.  One was the spelling of \"determinant\" in `matrix_space.py` which is no big deal, the other was the first portion of the `determinant()` definition, which is important, and I made that change by hand so I could test the patch.  Is this patch relative to 4.1.1 now?  If not, it should be \"rebased\" to 4.1.1 which I can explain how to do if you are not sure how (or what that is).\n\n3.  Doctest failure:  I'm getting one doctest failure.  In `matrix_space.py` the test `tinv(QQ, sparse=False)` seems to be throwing an `ArithmeticError` rather than a `ValueError` for a non-square matrix.  Presumably this should be easy for you to fix, since there are several other fixes like this already.\n\n4.  Patch name:  the file for the patch should eventually be named  `trac_6441_description.patch` where \"description\" is something really simple like \"df_charpoly\"\n\n5.  Ring and Field checks:  Yes, lets go through the exercise of seeing what sage-devel says about the `is_certainly_xx` methods and go with the consensus there.\n\n6.  Overconvergent Modular Forms:  I know nothing about these, or the need to use the \"hessenberg\" algorithm, so we can defer to David Loeffler's judgment on this one?\n\nAlmost there!\n\nRob",
    "created_at": "2009-08-22T05:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51618",
    "user": "https://github.com/rbeezer"
}
```

Attachment [20090821_Charpoly.patch](tarball://root/attachments/some-uuid/ticket6441/20090821_Charpoly.patch) by @rbeezer created at 2009-08-22 05:11:51

Hi Sebastian,

I've been using this routine to explore some characteristic polynomials with symbolic coefficients that Chris Godsil is interested in for graph theory.  Its great to have this efficient routine available.  It also seems that this latest version is about twice as fast as the first one, so the revisions here are providing a real speed-up.

1.  Documentation warnings:  I only got two warnings from matrix2.pyx.  In the docstring for `adjoint()` the description of `N` as input has its second line aligned relative to the second dash, where it is the text off the first dash that sets the indent location.   In the docstring for `charpoly()` the line that begins `If an algorithm is specified explicitly,...` needs to be pulled left to align properly.

The warnings you get when you build the documentation tell you the file and the method where it happens, then there is a line number, which is relative to the start of that particular docstring and give the location (roughly - plus/minus a line?).  If you still have a third warning, maybe you can locate it this way to help figure out the problem (or post the location here).

2.  Patch failures:  I had two parts of the patch which failed.  One was the spelling of "determinant" in `matrix_space.py` which is no big deal, the other was the first portion of the `determinant()` definition, which is important, and I made that change by hand so I could test the patch.  Is this patch relative to 4.1.1 now?  If not, it should be "rebased" to 4.1.1 which I can explain how to do if you are not sure how (or what that is).

3.  Doctest failure:  I'm getting one doctest failure.  In `matrix_space.py` the test `tinv(QQ, sparse=False)` seems to be throwing an `ArithmeticError` rather than a `ValueError` for a non-square matrix.  Presumably this should be easy for you to fix, since there are several other fixes like this already.

4.  Patch name:  the file for the patch should eventually be named  `trac_6441_description.patch` where "description" is something really simple like "df_charpoly"

5.  Ring and Field checks:  Yes, lets go through the exercise of seeing what sage-devel says about the `is_certainly_xx` methods and go with the consensus there.

6.  Overconvergent Modular Forms:  I know nothing about these, or the need to use the "hessenberg" algorithm, so we can defer to David Loeffler's judgment on this one?

Almost there!

Rob



---

archive/issue_comments_051619.json:
```json
{
    "body": "Dear Rob,\n\nI'll reply to your point one by one.\n\n1) OK, I should be able to fix those two warnings now, thank you for the explanation.  The third warning has to do with the html favicon I believe, so nothing with this patch.\n\n2) I am still running SAGE 4.0.2.  I wouldn't know how to sensibly rebase the patch to 4.1.1.  I am sure this is far from elegant, but what I'd do is download the SAGE 4.1.1 source, build from that, and then go through applying all the changes by hand again, much like it did yesterday to separate the different kinds of changes.  Could you perhaps explain a more sensible way to do this?\n\n3) Yes, that should be easy to fix.  I am surprised I didn't see that error when testing it myself.\n\n4) OK.\n\n5) Yes, I'll do that today.\n\n6) Yes, that's OK.  I talked to him about this at SAGE Days 16 before making the changes to his code.  He did not really care that much about the choice of the method here, but because the sensible default for charpoly computations should be division-free computations, we had to make a choice (and that's the current code in the patch).\n\nThanks!\n\nSebastian",
    "created_at": "2009-08-22T08:19:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51619",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Dear Rob,

I'll reply to your point one by one.

1) OK, I should be able to fix those two warnings now, thank you for the explanation.  The third warning has to do with the html favicon I believe, so nothing with this patch.

2) I am still running SAGE 4.0.2.  I wouldn't know how to sensibly rebase the patch to 4.1.1.  I am sure this is far from elegant, but what I'd do is download the SAGE 4.1.1 source, build from that, and then go through applying all the changes by hand again, much like it did yesterday to separate the different kinds of changes.  Could you perhaps explain a more sensible way to do this?

3) Yes, that should be easy to fix.  I am surprised I didn't see that error when testing it myself.

4) OK.

5) Yes, I'll do that today.

6) Yes, that's OK.  I talked to him about this at SAGE Days 16 before making the changes to his code.  He did not really care that much about the choice of the method here, but because the sensible default for charpoly computations should be division-free computations, we had to make a choice (and that's the current code in the patch).

Thanks!

Sebastian



---

archive/issue_comments_051620.json:
```json
{
    "body": "Replying to [comment:18 spancratz]:\n> 2) I am still running SAGE 4.0.2.  I wouldn't know how to sensibly rebase the patch to 4.1.1.  I am sure this is far from elegant, but what I'd do is download the SAGE 4.1.1 source, build from that, and then go through applying all the changes by hand again, much like it did yesterday to separate the different kinds of changes.  Could you perhaps explain a more sensible way to do this?\n\nThis is (potentially) a little better than what you wrote above: build 4.1.1 (or get a binary for your particular architecture from sagemath.org), and try to apply your patch to it.  If your patch touches several files in the Sage library, some of them might get patched properly, while others might get rejected.  Mercurial will let you know about these, and save the pieces that it couldn't figure out as e.g. `matrix1.pyx.rej`.  It is then a matter of dealing with them manually, as you described above.\n\nIf the patch is not too bit-rotten, this is normally manageable.  Good luck, I'll be happy to see your code included.\n\nPS: I do think this qualifies as \"major\" so I changed the priority.",
    "created_at": "2009-08-22T10:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51620",
    "user": "https://github.com/aghitza"
}
```

Replying to [comment:18 spancratz]:
> 2) I am still running SAGE 4.0.2.  I wouldn't know how to sensibly rebase the patch to 4.1.1.  I am sure this is far from elegant, but what I'd do is download the SAGE 4.1.1 source, build from that, and then go through applying all the changes by hand again, much like it did yesterday to separate the different kinds of changes.  Could you perhaps explain a more sensible way to do this?

This is (potentially) a little better than what you wrote above: build 4.1.1 (or get a binary for your particular architecture from sagemath.org), and try to apply your patch to it.  If your patch touches several files in the Sage library, some of them might get patched properly, while others might get rejected.  Mercurial will let you know about these, and save the pieces that it couldn't figure out as e.g. `matrix1.pyx.rej`.  It is then a matter of dealing with them manually, as you described above.

If the patch is not too bit-rotten, this is normally manageable.  Good luck, I'll be happy to see your code included.

PS: I do think this qualifies as "major" so I changed the priority.



---

archive/issue_comments_051621.json:
```json
{
    "body": "Sebastian,\n\nYes, the favicon is a long-standing annoyance.  Not your problem.\n\nRebasing is never elegant.  I'll add to what Alex has written (thanks, Alex, for weighing in).  I use the GNU `patch` program to apply the old patch to the new source, outside of any Sage environment (just need to set the working directory properly and use the -p switch right).  In other words, I don't use Mercurial, or `hg_sage` methods to apply the broken patch, just `patch` at the system command line.  So the net effect is as if I edited the source by hand, and as Alex says you get the rejects in appropriately named files.  Then I make the rejected changes by hand (this will be easy for you here, just two of them and they are obvious) and then I use `hg_sage.commit()`, etc to roll up everything into one changeset and thus one complete new patch (you can add in the docstring fixes, etc before doing the commit).  I'd imagine there are better ways, but that's my routine.\n\nRob",
    "created_at": "2009-08-22T17:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51621",
    "user": "https://github.com/rbeezer"
}
```

Sebastian,

Yes, the favicon is a long-standing annoyance.  Not your problem.

Rebasing is never elegant.  I'll add to what Alex has written (thanks, Alex, for weighing in).  I use the GNU `patch` program to apply the old patch to the new source, outside of any Sage environment (just need to set the working directory properly and use the -p switch right).  In other words, I don't use Mercurial, or `hg_sage` methods to apply the broken patch, just `patch` at the system command line.  So the net effect is as if I edited the source by hand, and as Alex says you get the rejects in appropriately named files.  Then I make the rejected changes by hand (this will be easy for you here, just two of them and they are obvious) and then I use `hg_sage.commit()`, etc to roll up everything into one changeset and thus one complete new patch (you can add in the docstring fixes, etc before doing the commit).  I'd imagine there are better ways, but that's my routine.

Rob



---

archive/issue_comments_051622.json:
```json
{
    "body": "Hi Sebastian,\n\nGood discussion on sage-devel.  I suspected it would get a reaction, and some good suggestions.\n\nIf you decide to do the assert-field stuff, lets do that on another ticket.  You don't need it here, do you?\n\nIf you wanted, the is_field changes could also go on another ticket (which could be a very easy review) so that change was isolated, then the charpoly stuff here could depend on it (just via comments in Trac for the release manager) and just use it.  Not necessary, but it'd leave a nicer looking history.  Your call.\n\nRob",
    "created_at": "2009-08-23T20:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51622",
    "user": "https://github.com/rbeezer"
}
```

Hi Sebastian,

Good discussion on sage-devel.  I suspected it would get a reaction, and some good suggestions.

If you decide to do the assert-field stuff, lets do that on another ticket.  You don't need it here, do you?

If you wanted, the is_field changes could also go on another ticket (which could be a very easy review) so that change was isolated, then the charpoly stuff here could depend on it (just via comments in Trac for the release manager) and just use it.  Not necessary, but it'd leave a nicer looking history.  Your call.

Rob



---

archive/issue_comments_051623.json:
```json
{
    "body": "Dear Rob,\n\nI've added two patch files to this now, one to include \"is_field\" and \"is_integral_domain\" and another one to include the division-free matrix methods (and some doctest fixes).\n\nI think for the time being it would be easier to not create a ticket for the assert-field stuff (and then work on it right away!) which this ticket would depend on.  One reason is that in a way I'd quite like to get this done, but more importantly (a) the recent idea contributed by Robert Bradshaw suggests to me that it's not quite clear how this should be done properly in the long run and (b) once one has something like the \"_properties\" attribute and \"assert_foo\" methods suggested in the thread on sage-devel, this will require those little changes in many places calling \"is_field\" etc, not just in the _charpoly_df method introduced with this ticket.\n\nThat said, I think it's a good idea to create a separate trac ticket.  If you think it's a good idea, I'd be happy to follow the discussion on sage-devel and create a trac ticket (with a link to the thread and a few examples of what doesn't work in SAGE at the moment).\n\nKind regards,\n\nSebastian",
    "created_at": "2009-08-25T10:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51623",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Dear Rob,

I've added two patch files to this now, one to include "is_field" and "is_integral_domain" and another one to include the division-free matrix methods (and some doctest fixes).

I think for the time being it would be easier to not create a ticket for the assert-field stuff (and then work on it right away!) which this ticket would depend on.  One reason is that in a way I'd quite like to get this done, but more importantly (a) the recent idea contributed by Robert Bradshaw suggests to me that it's not quite clear how this should be done properly in the long run and (b) once one has something like the "_properties" attribute and "assert_foo" methods suggested in the thread on sage-devel, this will require those little changes in many places calling "is_field" etc, not just in the _charpoly_df method introduced with this ticket.

That said, I think it's a good idea to create a separate trac ticket.  If you think it's a good idea, I'd be happy to follow the discussion on sage-devel and create a trac ticket (with a link to the thread and a few examples of what doesn't work in SAGE at the moment).

Kind regards,

Sebastian



---

archive/issue_comments_051624.json:
```json
{
    "body": "20090825 - Including \"is_field\" etc for rings, to facilitate the division-free matrix operations",
    "created_at": "2009-08-25T10:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51624",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

20090825 - Including "is_field" etc for rings, to facilitate the division-free matrix operations



---

archive/issue_comments_051625.json:
```json
{
    "body": "Attachment [trac_6441_a_rings.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_a_rings.patch) by spancratz created at 2009-08-25 10:18:13\n\n20090825 - Including divison-free adjoint, charpoly and det",
    "created_at": "2009-08-25T10:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51625",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac_6441_a_rings.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_a_rings.patch) by spancratz created at 2009-08-25 10:18:13

20090825 - Including divison-free adjoint, charpoly and det



---

archive/issue_comments_051626.json:
```json
{
    "body": "Attachment [trac_6441_b_df_charpoly.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_b_df_charpoly.patch) by @rbeezer created at 2009-08-26 05:55:19\n\nHi Sebastian,\n\nWorking in batches - this is just about `is_field()` and friends.\n\n1.  In `sage/algebras/group_algebra.py` you have `self.base_ring.is_integral()` which needs to be completed to `.is_integral_domain()`.\n\n2.  Patch attached - it has a doctest for `is_field` in `sage/rings/ring.pyx` to illustrate the `proof` parameter in action (which I think should be illustrated at least once).  You'll recognize it from your sage-devel post.  Do you have something similar that would work well for `is_integral_domain()`?\n\n3.  When I applied the patch a colon was missing in `sage/rings/quotient_ring.py` after a `try`.  No idea why - since the colon is in your patch.  But I fixed it by hand, and so its in my attached patch, along with the fix for (1) above.  So you might just cut out the doctest by hand to build it in rather than applying the patch.\n\nI'll look at part (b) in the next couple of days.\n\nRob",
    "created_at": "2009-08-26T05:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51626",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_6441_b_df_charpoly.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_b_df_charpoly.patch) by @rbeezer created at 2009-08-26 05:55:19

Hi Sebastian,

Working in batches - this is just about `is_field()` and friends.

1.  In `sage/algebras/group_algebra.py` you have `self.base_ring.is_integral()` which needs to be completed to `.is_integral_domain()`.

2.  Patch attached - it has a doctest for `is_field` in `sage/rings/ring.pyx` to illustrate the `proof` parameter in action (which I think should be illustrated at least once).  You'll recognize it from your sage-devel post.  Do you have something similar that would work well for `is_integral_domain()`?

3.  When I applied the patch a colon was missing in `sage/rings/quotient_ring.py` after a `try`.  No idea why - since the colon is in your patch.  But I fixed it by hand, and so its in my attached patch, along with the fix for (1) above.  So you might just cut out the doctest by hand to build it in rather than applying the patch.

I'll look at part (b) in the next couple of days.

Rob



---

archive/issue_comments_051627.json:
```json
{
    "body": "Attachment [trac_6441_a_reviewer.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_a_reviewer.patch) by @rbeezer created at 2009-08-27 04:59:43\n\nSebastian,\n\nLooks to me like maybe  `trac_6441_b_df_charpoly.patch`  is the wrong file?  It has 3-D arrays in the main routine and lots of minor (unrelated) documentation fixes, though it does fix the integral domain problem from the \"a\" patch.  I liked the looks of `20090821_Charpoly.patch` better, which incorporates Yann's suggestions.  Am I mis-understanding something?\n\nRob",
    "created_at": "2009-08-27T04:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51627",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_6441_a_reviewer.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_a_reviewer.patch) by @rbeezer created at 2009-08-27 04:59:43

Sebastian,

Looks to me like maybe  `trac_6441_b_df_charpoly.patch`  is the wrong file?  It has 3-D arrays in the main routine and lots of minor (unrelated) documentation fixes, though it does fix the integral domain problem from the "a" patch.  I liked the looks of `20090821_Charpoly.patch` better, which incorporates Yann's suggestions.  Am I mis-understanding something?

Rob



---

archive/issue_comments_051628.json:
```json
{
    "body": "Dear Rob,\n\nI don't know how that happened, I am sorry for that mistake.  I am working on it right now, but each time I am going through the process of setting up a clone of 4.1.1, making the changes, and then running make test and creating a patch, it takes a couple of hours on my laptop.  I should be able to attach new files later tonight.\n\nSebastian",
    "created_at": "2009-08-27T15:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51628",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Dear Rob,

I don't know how that happened, I am sorry for that mistake.  I am working on it right now, but each time I am going through the process of setting up a clone of 4.1.1, making the changes, and then running make test and creating a patch, it takes a couple of hours on my laptop.  I should be able to attach new files later tonight.

Sebastian



---

archive/issue_comments_051629.json:
```json
{
    "body": "Replying to [comment:25 spancratz]:\n> I don't know how that happened, I am sorry for that mistake.  I am working on it right now, but each time I am going through the process of setting up a clone of 4.1.1, making the changes, and then running make test and creating a patch, it takes a couple of hours on my laptop.  I should be able to attach new files later tonight.\n\nNo problem at all.  Just confused me temporarily.  ;-)\n\nI'll maybe check back tonight, which will be in the wee hours of the morning for you.  Otherwise, over the weekend.",
    "created_at": "2009-08-27T19:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51629",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:25 spancratz]:
> I don't know how that happened, I am sorry for that mistake.  I am working on it right now, but each time I am going through the process of setting up a clone of 4.1.1, making the changes, and then running make test and creating a patch, it takes a couple of hours on my laptop.  I should be able to attach new files later tonight.

No problem at all.  Just confused me temporarily.  ;-)

I'll maybe check back tonight, which will be in the wee hours of the morning for you.  Otherwise, over the weekend.



---

archive/issue_comments_051630.json:
```json
{
    "body": "I've added newer versions of the two files, hopefully this does it.\n\nSebastian",
    "created_at": "2009-08-27T23:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51630",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

I've added newer versions of the two files, hopefully this does it.

Sebastian



---

archive/issue_comments_051631.json:
```json
{
    "body": "20090827 - Including \"is_field\" etc for rings, to facilitate the division-free matrix operations",
    "created_at": "2009-08-27T23:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51631",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

20090827 - Including "is_field" etc for rings, to facilitate the division-free matrix operations



---

archive/issue_comments_051632.json:
```json
{
    "body": "Attachment [trac_6441_b_df_charpoly.2.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_b_df_charpoly.2.patch) by spancratz created at 2009-08-27 23:36:38\n\n20090827 - Including divison-free adjoint, charpoly and det",
    "created_at": "2009-08-27T23:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51632",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac_6441_b_df_charpoly.2.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_b_df_charpoly.2.patch) by spancratz created at 2009-08-27 23:36:38

20090827 - Including divison-free adjoint, charpoly and det



---

archive/issue_comments_051633.json:
```json
{
    "body": "Hi Sebastian,\n\nI think everything is in here, but the patches aren't quite right.\n\n\"a\" patch is just a generic patch/diff file, not a Mercurial patch.\n\nTry the following (which worked for me)\n\n1.  Make a fresh clone (mine is called df-4).\n\n2.  sage: hg_sage.apply( \"the-a-patch-file\" )\n\n3.  Type in a commit message when asked.\n\n4.  Build and test.\n\n5.  sage: hg_sage.export( change-set-number, \"file-name-for-patch\" )\n\n\nI did the first four steps, and would have done step 5 for you, but then the patch would have my name, not yours.\n\nBTW, do you want the \"[ui]\" bit in your name in your .hgrc file?\n\n\"b\" patch is a Mercurial patch, but still has the 3-D-index version of `_charpoly_df()`.  Here's what I did next:\n\n1.  At system prompt: cd devel/sage-df-4\n\n2.  At system prompt: patch -p1 < file-name-of-b-patch\n\n(makes the changes, but no changeset is created, no commit message)\n\n3.  Then I edited sage/matrix/matrix2.pyx by copying the entire `_charpoly_df()` routine out of `20090821_Charpoly.patch`, replacing the entire 3-index version with the 2-index version.\n\n4.  Build and test as usual.\n\n5.  Commit, export.\n\n\nAs above, I'd have built a patch from this, but it'd have my name, not yours.\n\nI was able to pass all tests this way, but I can't be certain that the \"b\" patch has everything it should have, especially since the most important part was not the latest version.  Can you duplicate the procedures above to make proper patches with your name on them AND especially review what you build to be sure it really has everything in it that it should have?  I don't think I can be trusted to recognize what is old and what is new unless it is pretty obvious.\n\nYou can repeat step 3 on the \"b\" patch if you see anything else that needs fixing.\n\nWith a couple of proper patches that pass all tests and build the docs, we'll be done.\n\nRob",
    "created_at": "2009-08-28T04:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51633",
    "user": "https://github.com/rbeezer"
}
```

Hi Sebastian,

I think everything is in here, but the patches aren't quite right.

"a" patch is just a generic patch/diff file, not a Mercurial patch.

Try the following (which worked for me)

1.  Make a fresh clone (mine is called df-4).

2.  sage: hg_sage.apply( "the-a-patch-file" )

3.  Type in a commit message when asked.

4.  Build and test.

5.  sage: hg_sage.export( change-set-number, "file-name-for-patch" )


I did the first four steps, and would have done step 5 for you, but then the patch would have my name, not yours.

BTW, do you want the "[ui]" bit in your name in your .hgrc file?

"b" patch is a Mercurial patch, but still has the 3-D-index version of `_charpoly_df()`.  Here's what I did next:

1.  At system prompt: cd devel/sage-df-4

2.  At system prompt: patch -p1 < file-name-of-b-patch

(makes the changes, but no changeset is created, no commit message)

3.  Then I edited sage/matrix/matrix2.pyx by copying the entire `_charpoly_df()` routine out of `20090821_Charpoly.patch`, replacing the entire 3-index version with the 2-index version.

4.  Build and test as usual.

5.  Commit, export.


As above, I'd have built a patch from this, but it'd have my name, not yours.

I was able to pass all tests this way, but I can't be certain that the "b" patch has everything it should have, especially since the most important part was not the latest version.  Can you duplicate the procedures above to make proper patches with your name on them AND especially review what you build to be sure it really has everything in it that it should have?  I don't think I can be trusted to recognize what is old and what is new unless it is pretty obvious.

You can repeat step 3 on the "b" patch if you see anything else that needs fixing.

With a couple of proper patches that pass all tests and build the docs, we'll be done.

Rob



---

archive/issue_comments_051634.json:
```json
{
    "body": "OK, here it goes again...\n\nSebastian",
    "created_at": "2009-08-28T14:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51634",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

OK, here it goes again...

Sebastian



---

archive/issue_comments_051635.json:
```json
{
    "body": "20090828 - Including \"is_field\" etc for rings, to facilitate the division-free matrix operations",
    "created_at": "2009-08-28T14:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51635",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

20090828 - Including "is_field" etc for rings, to facilitate the division-free matrix operations



---

archive/issue_comments_051636.json:
```json
{
    "body": "Attachment [trac_6441_a_rings.3.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_a_rings.3.patch) by spancratz created at 2009-08-28 14:13:05\n\n20090828 - Including divison-free adjoint, charpoly and det",
    "created_at": "2009-08-28T14:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51636",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac_6441_a_rings.3.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_a_rings.3.patch) by spancratz created at 2009-08-28 14:13:05

20090828 - Including divison-free adjoint, charpoly and det



---

archive/issue_comments_051637.json:
```json
{
    "body": "Attachment [trac_6441_b_df_charpoly.3.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_b_df_charpoly.3.patch) by @rbeezer created at 2009-08-30 05:26:44\n\nSebstian,\n\nVery good!  Builds cleanly and passes all tests.  I got two warnings building the documentation, I think these were leftovers from the discussion above.  I've attached a patch that fixes both.\n\nSo this is a positive review, though you need to accept my changes in the documentation patch.  If the changes look OK, then change the subject line to `[with patch, positive review]` and then it'll get merged into the next release.\n\nThis will be a great addition to Sage.  Thanks for your patience with all the details.  Your next patch should be a whole lot easier.\n\nRelease manager:  Apply the two patches from 2009/08/28 (version 3), first the \"a_rings\" and then the \"b_df_charpoly\", then the reviewer patch.\n\nRob",
    "created_at": "2009-08-30T05:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51637",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_6441_b_df_charpoly.3.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_b_df_charpoly.3.patch) by @rbeezer created at 2009-08-30 05:26:44

Sebstian,

Very good!  Builds cleanly and passes all tests.  I got two warnings building the documentation, I think these were leftovers from the discussion above.  I've attached a patch that fixes both.

So this is a positive review, though you need to accept my changes in the documentation patch.  If the changes look OK, then change the subject line to `[with patch, positive review]` and then it'll get merged into the next release.

This will be a great addition to Sage.  Thanks for your patience with all the details.  Your next patch should be a whole lot easier.

Release manager:  Apply the two patches from 2009/08/28 (version 3), first the "a_rings" and then the "b_df_charpoly", then the reviewer patch.

Rob



---

archive/issue_comments_051638.json:
```json
{
    "body": "Attachment [trac_6441_reviewer_doctests.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_reviewer_doctests.patch) by @rbeezer created at 2009-08-30 05:27:30",
    "created_at": "2009-08-30T05:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51638",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_6441_reviewer_doctests.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_reviewer_doctests.patch) by @rbeezer created at 2009-08-30 05:27:30



---

archive/issue_comments_051639.json:
```json
{
    "body": "Dear Rob,\n\nYes, the patch you attached is OK.  I am sorry for not fixing these two small problems in the documentation myself.\n\nTalking about patience, I think I need to thank you at least as much for the patience you had while reviewing this, and I hope (and am quite confident) that my next bit of work on SAGE will be a lot smoother.\n\nMany thanks for the help!\n\nSebastian",
    "created_at": "2009-08-31T21:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51639",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Dear Rob,

Yes, the patch you attached is OK.  I am sorry for not fixing these two small problems in the documentation myself.

Talking about patience, I think I need to thank you at least as much for the patience you had while reviewing this, and I hope (and am quite confident) that my next bit of work on SAGE will be a lot smoother.

Many thanks for the help!

Sebastian



---

archive/issue_comments_051640.json:
```json
{
    "body": "I'm getting two hunk rejections when applying `trac_6441_a_rings.3.patch`:\n\n```\n[mvngu@mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6441/trac_6441_a_rings.3.patch && hg qpush\nadding trac_6441_a_rings.3.patch to series file\napplying trac_6441_a_rings.3.patch\npatching file sage/rings/ring.pyx\nHunk #1 FAILED at 402\nHunk #3 FAILED at 515\n2 out of 9 hunks FAILED -- saving rejects to file sage/rings/ring.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nErrors during apply, please fix and refresh trac_6441_a_rings.3.patch\n```\n\nThis ticket would have to wait until after Sage 4.1.2.alpha0 is released (easy option) or the three patches would need to be rebased now (hard option).",
    "created_at": "2009-09-02T05:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51640",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I'm getting two hunk rejections when applying `trac_6441_a_rings.3.patch`:

```
[mvngu@mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6441/trac_6441_a_rings.3.patch && hg qpush
adding trac_6441_a_rings.3.patch to series file
applying trac_6441_a_rings.3.patch
patching file sage/rings/ring.pyx
Hunk #1 FAILED at 402
Hunk #3 FAILED at 515
2 out of 9 hunks FAILED -- saving rejects to file sage/rings/ring.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_6441_a_rings.3.patch
```

This ticket would have to wait until after Sage 4.1.2.alpha0 is released (easy option) or the three patches would need to be rebased now (hard option).



---

archive/issue_comments_051641.json:
```json
{
    "body": "Which version would it have to be rebased for?  The above patches worked fine on my installation (SAGE 4.1.1, release date 2009-08-14, build from source).  If you think the version of sage/rings.ring.pyx that the patch needs to be rebased for is \"stable\" in some suitable sense, I'd be happy to rebase it now as it only concerns two hunks.  Otherwise, I don't mind.\n\nKind regards,\n\nSebastian",
    "created_at": "2009-09-02T11:32:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51641",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Which version would it have to be rebased for?  The above patches worked fine on my installation (SAGE 4.1.1, release date 2009-08-14, build from source).  If you think the version of sage/rings.ring.pyx that the patch needs to be rebased for is "stable" in some suitable sense, I'd be happy to rebase it now as it only concerns two hunks.  Otherwise, I don't mind.

Kind regards,

Sebastian



---

archive/issue_comments_051642.json:
```json
{
    "body": "Replying to [comment:33 spancratz]:\n> Which version would it have to be rebased for?  The above patches worked fine on my installation (SAGE 4.1.1, release date 2009-08-14, build from source).\nI can confirm that the patches apply without problems on Sage 4.1.1.\n\n\n\n> If you think the version of sage/rings.ring.pyx that the patch needs to be rebased for is \"stable\" in some suitable sense, I'd be happy to rebase it now as it only concerns two hunks.  Otherwise, I don't mind.\nI got the hunk failures because I first applied the patches at #6531 and #6850 prior to applying the patches on this ticket. The patches at #6531 and #6850 substantially modify the module `sage/rings/ring.pyx` and the patch `trac_6441_a_rings.3.patch` also adds more stuff to that module. An easy way to resolve dependencies is to wait for Sage 4.1.2.alpha0 to come out and then rebase your patches against that version. Or you can try to first apply the patches at #6531 and #6850, then rebase your patches on top of those.",
    "created_at": "2009-09-02T14:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51642",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:33 spancratz]:
> Which version would it have to be rebased for?  The above patches worked fine on my installation (SAGE 4.1.1, release date 2009-08-14, build from source).
I can confirm that the patches apply without problems on Sage 4.1.1.



> If you think the version of sage/rings.ring.pyx that the patch needs to be rebased for is "stable" in some suitable sense, I'd be happy to rebase it now as it only concerns two hunks.  Otherwise, I don't mind.
I got the hunk failures because I first applied the patches at #6531 and #6850 prior to applying the patches on this ticket. The patches at #6531 and #6850 substantially modify the module `sage/rings/ring.pyx` and the patch `trac_6441_a_rings.3.patch` also adds more stuff to that module. An easy way to resolve dependencies is to wait for Sage 4.1.2.alpha0 to come out and then rebase your patches against that version. Or you can try to first apply the patches at #6531 and #6850, then rebase your patches on top of those.



---

archive/issue_comments_051643.json:
```json
{
    "body": "I've attached the two rebased patches.  The second one now also includes the two changes previously added in \"trac_6441_reviewer_doctests.patch\".\n\nSebastian",
    "created_at": "2009-09-02T17:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51643",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

I've attached the two rebased patches.  The second one now also includes the two changes previously added in "trac_6441_reviewer_doctests.patch".

Sebastian



---

archive/issue_comments_051644.json:
```json
{
    "body": "Attachment [trac_6441_a_rings_rebase.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_a_rings_rebase.patch) by spancratz created at 2009-09-02 17:22:37\n\n20090902 - Including \"is_field\" etc for rings, to facilitate the division-free matrix operations",
    "created_at": "2009-09-02T17:22:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51644",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac_6441_a_rings_rebase.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_a_rings_rebase.patch) by spancratz created at 2009-09-02 17:22:37

20090902 - Including "is_field" etc for rings, to facilitate the division-free matrix operations



---

archive/issue_comments_051645.json:
```json
{
    "body": "20090902 - Including divison-free adjoint, charpoly and det",
    "created_at": "2009-09-02T17:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51645",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

20090902 - Including divison-free adjoint, charpoly and det



---

archive/issue_comments_051646.json:
```json
{
    "body": "Attachment [trac_6441_b_df_charpoly_rebase.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_b_df_charpoly_rebase.patch) by mvngu created at 2009-09-03 22:27:50\n\nApplying the patches `trac_6441_a_rings_rebase.patch` and `trac_6441_b_df_charpoly_rebase.patch` results in some doctest failures:\n\n```\nsage -t -long devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py\", line 122:\n    sage: EllipticCurve([0, 0, 1, -79, 342]).sha().an_numerical(prec=10, proof=False) # long time -- about 30 seconds.\nExpected:\n    1.0\nGot:\n    0.95\n**********************************************************************\n1 items had failures:\n   1 of  11 in __main__.example_2\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_sha_tate.py\n\t [189.8 s]\n\n<SNIP>\n\nsage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py\", line 2008:\n    sage: EllipticCurve([1, -1, 0, -79, 289]).regulator()  # long time (seconds)\nExpected:\n    1.50434488827528\nGot:\n    1.50434488827530\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py\", line 2010:\n    sage: EllipticCurve([0, 0, 1, -79, 342]).regulator(proof=False)  # long time (seconds)\nExpected:\n    14.790527570131...\nGot:\n    14.7905275701307\n**********************************************************************\n1 items had failures:\n   2 of  10 in __main__.example_36\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_ell_rational_field.py\n\t [200.7 s]\n```\n\nThis is a known failure:\n\n```\nsage -t -long devel/sage-main/sage/server/simple/twist.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py\", line 51:\n    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))\nExpected:\n    {\n    \"status\": \"done\",\n    \"files\": [],\n    \"cell_id\": 1\n    }\n    ___S_A_G_E___\n    4\nGot:\n    {\n    \"status\": \"computing\",\n    \"files\": [],\n    \"cell_id\": 1\n    }\n    ___S_A_G_E___\n    <BLANKLINE>\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py\", line 95:\n    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=%s' % (port, session, urllib.quote(code)))\nExpected:\n    {\n    \"status\": \"done\",\n    \"files\": [\"a.txt\"],\n    \"cell_id\": 3\n    }\n    ___S_A_G_E___\nGot:\n    {\n    \"status\": \"done\",\n    \"files\": [],\n    \"cell_id\": 3\n    }\n    ___S_A_G_E___\n    <BLANKLINE>\n    Traceback (most recent call last):    h = open('a.txt', 'w'); h.write('test'); h.close()\n    NameError: name 'os' is not defined\n    THERE WAS AN ERROR LOADING THE SAGE LIBRARIES.  Try starting Sage from the command line to see what the error is.\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py\", line 103:\n    sage: print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))\nExpected:\n    test\nGot:\n    No such file a.txt in cell 3.\n**********************************************************************\n1 items had failures:\n   3 of  24 in __main__.example_0\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_twist.py\n\t [30.6 s]\n```\n",
    "created_at": "2009-09-03T22:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51646",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6441_b_df_charpoly_rebase.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_b_df_charpoly_rebase.patch) by mvngu created at 2009-09-03 22:27:50

Applying the patches `trac_6441_a_rings_rebase.patch` and `trac_6441_b_df_charpoly_rebase.patch` results in some doctest failures:

```
sage -t -long devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py", line 122:
    sage: EllipticCurve([0, 0, 1, -79, 342]).sha().an_numerical(prec=10, proof=False) # long time -- about 30 seconds.
Expected:
    1.0
Got:
    0.95
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_sha_tate.py
	 [189.8 s]

<SNIP>

sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py", line 2008:
    sage: EllipticCurve([1, -1, 0, -79, 289]).regulator()  # long time (seconds)
Expected:
    1.50434488827528
Got:
    1.50434488827530
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py", line 2010:
    sage: EllipticCurve([0, 0, 1, -79, 342]).regulator(proof=False)  # long time (seconds)
Expected:
    14.790527570131...
Got:
    14.7905275701307
**********************************************************************
1 items had failures:
   2 of  10 in __main__.example_36
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_ell_rational_field.py
	 [200.7 s]
```

This is a known failure:

```
sage -t -long devel/sage-main/sage/server/simple/twist.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py", line 51:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
Expected:
    {
    "status": "done",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    4
Got:
    {
    "status": "computing",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    <BLANKLINE>
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py", line 95:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=%s' % (port, session, urllib.quote(code)))
Expected:
    {
    "status": "done",
    "files": ["a.txt"],
    "cell_id": 3
    }
    ___S_A_G_E___
Got:
    {
    "status": "done",
    "files": [],
    "cell_id": 3
    }
    ___S_A_G_E___
    <BLANKLINE>
    Traceback (most recent call last):    h = open('a.txt', 'w'); h.write('test'); h.close()
    NameError: name 'os' is not defined
    THERE WAS AN ERROR LOADING THE SAGE LIBRARIES.  Try starting Sage from the command line to see what the error is.
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/server/simple/twist.py", line 103:
    sage: print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))
Expected:
    test
Got:
    No such file a.txt in cell 3.
**********************************************************************
1 items had failures:
   3 of  24 in __main__.example_0
***Test Failed*** 3 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_twist.py
	 [30.6 s]
```




---

archive/issue_comments_051647.json:
```json
{
    "body": "Minh and Sebastian,\n\nI've not been in the habit of running \"-long\" tests, and I'd guess Sebastian didn't either.  Probably need to change my habits.\n\nThe latter two look like numerical noise, and I know Sebastian fixed up one very similar doctest for very much the same reason.  I don't know enough about the elliptic curve stuff to be certain about the discrepancy between 1.0 and 0.95 on the first one.  That probably needs a closer look.  Maybe with 4.1.2.alpha0 now out, Sebastian can get some clean patches together and put this one behind him finally!  Hopefully.\n\nRob",
    "created_at": "2009-09-04T03:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51647",
    "user": "https://github.com/rbeezer"
}
```

Minh and Sebastian,

I've not been in the habit of running "-long" tests, and I'd guess Sebastian didn't either.  Probably need to change my habits.

The latter two look like numerical noise, and I know Sebastian fixed up one very similar doctest for very much the same reason.  I don't know enough about the elliptic curve stuff to be certain about the discrepancy between 1.0 and 0.95 on the first one.  That probably needs a closer look.  Maybe with 4.1.2.alpha0 now out, Sebastian can get some clean patches together and put this one behind him finally!  Hopefully.

Rob



---

archive/issue_comments_051648.json:
```json
{
    "body": "Dear Rob,\n\nYes, you're right.  I hadn't even heard about the \"-long\" tests.  Regarding the above problems, I take it I only need to look at the first few problems and not the known failures, right?\n\nI've already checked that they definitely are \"just\" numerical noise, running the methods in question with the parameter \"prec\" in {10,20,30} gave answers 0.95, 1.0001, 0.99999994, respectively.  However, I think the right way to fix this is not to change the doctests, but to pass the parameter algorithm=\"hessenberg\" at the appropriate place to ensure that the behaviour isn't changed.  I'll look into this probably tomorrow.\n\nSebastian",
    "created_at": "2009-09-04T13:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51648",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Dear Rob,

Yes, you're right.  I hadn't even heard about the "-long" tests.  Regarding the above problems, I take it I only need to look at the first few problems and not the known failures, right?

I've already checked that they definitely are "just" numerical noise, running the methods in question with the parameter "prec" in {10,20,30} gave answers 0.95, 1.0001, 0.99999994, respectively.  However, I think the right way to fix this is not to change the doctests, but to pass the parameter algorithm="hessenberg" at the appropriate place to ensure that the behaviour isn't changed.  I'll look into this probably tomorrow.

Sebastian



---

archive/issue_comments_051649.json:
```json
{
    "body": "Replying to [comment:38 spancratz]:\n> I hadn't even heard about the \"-long\" tests.\n\nSorry, my fault.  First time it got me as well.\n\n> I take it I only need to look at the first few problems and not the known failures, right?\n\nYes, you can expect those other failures, but they are not yours to deal with.\n\n> I've already checked that they definitely are \"just\" numerical noise, running the methods in question with the parameter \"prec\" in {10,20,30} gave answers 0.95, 1.0001, 0.99999994, respectively.  However, I think the right way to fix this is not to change the doctests, but to pass the parameter algorithm=\"hessenberg\" at the appropriate place to ensure that the behaviour isn't changed.  I'll look into this probably tomorrow.\n\nSounds good.\n\nRob",
    "created_at": "2009-09-04T14:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51649",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:38 spancratz]:
> I hadn't even heard about the "-long" tests.

Sorry, my fault.  First time it got me as well.

> I take it I only need to look at the first few problems and not the known failures, right?

Yes, you can expect those other failures, but they are not yours to deal with.

> I've already checked that they definitely are "just" numerical noise, running the methods in question with the parameter "prec" in {10,20,30} gave answers 0.95, 1.0001, 0.99999994, respectively.  However, I think the right way to fix this is not to change the doctests, but to pass the parameter algorithm="hessenberg" at the appropriate place to ensure that the behaviour isn't changed.  I'll look into this probably tomorrow.

Sounds good.

Rob



---

archive/issue_comments_051650.json:
```json
{
    "body": "I am now adding two updated patches, rebased against 4.1.2.alpha0.\n\nSebastian",
    "created_at": "2009-09-06T21:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51650",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

I am now adding two updated patches, rebased against 4.1.2.alpha0.

Sebastian



---

archive/issue_comments_051651.json:
```json
{
    "body": "20090906 - Including \"is_field\" etc for rings, to facilitate the division-free matrix operations",
    "created_at": "2009-09-06T21:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51651",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

20090906 - Including "is_field" etc for rings, to facilitate the division-free matrix operations



---

archive/issue_comments_051652.json:
```json
{
    "body": "Attachment [trac_6441_b_df_charpoly_412rebase.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_b_df_charpoly_412rebase.patch) by spancratz created at 2009-09-06 21:37:19\n\n20090906 - Including divison-free adjoint, charpoly and det",
    "created_at": "2009-09-06T21:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51652",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac_6441_b_df_charpoly_412rebase.patch](tarball://root/attachments/some-uuid/ticket6441/trac_6441_b_df_charpoly_412rebase.patch) by spancratz created at 2009-09-06 21:37:19

20090906 - Including divison-free adjoint, charpoly and det



---

archive/issue_comments_051653.json:
```json
{
    "body": "Working with the 20090906 patches on 4.1.2.alpha1.\n\nBuilds fine, HTML docs constructed with no warnings, and passes all tests with options: -testall -long \n\nLooks ready to go from here.\n\nRob",
    "created_at": "2009-09-08T00:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51653",
    "user": "https://github.com/rbeezer"
}
```

Working with the 20090906 patches on 4.1.2.alpha1.

Builds fine, HTML docs constructed with no warnings, and passes all tests with options: -testall -long 

Looks ready to go from here.

Rob



---

archive/issue_comments_051654.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-09T05:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51654",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_051655.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6441_a_rings_412rebase.patch`\n2. `trac_6441_b_df_charpoly_412rebase.patch`",
    "created_at": "2009-09-09T05:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6441#issuecomment-51655",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged patches in this order:

1. `trac_6441_a_rings_412rebase.patch`
2. `trac_6441_b_df_charpoly_412rebase.patch`



---

archive/issue_events_015192.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-09T05:56:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6441",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6441#event-15192"
}
```
