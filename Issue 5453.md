# Issue 5453: [with patch, needs review] Create a ring for working with polynomials in countably infinitely many variables

archive/issues_005453.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  simonking\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5453\n\n",
    "created_at": "2009-03-07T19:12:56Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] Create a ring for working with polynomials in countably infinitely many variables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5453",
    "user": "@mwhansen"
}
```
Assignee: @malb

CC:  simonking



Issue created by migration from https://trac.sagemath.org/ticket/5453





---

archive/issue_comments_042224.json:
```json
{
    "body": "Attachment [trac_5453.patch](tarball://root/attachments/some-uuid/ticket5453/trac_5453.patch) by @mwhansen created at 2009-03-07 19:14:08",
    "created_at": "2009-03-07T19:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42224",
    "user": "@mwhansen"
}
```

Attachment [trac_5453.patch](tarball://root/attachments/some-uuid/ticket5453/trac_5453.patch) by @mwhansen created at 2009-03-07 19:14:08



---

archive/issue_comments_042225.json:
```json
{
    "body": "Dear Mike,\n\nCool! Thank you that you started an implementation!\n\nCertainly from your patch I learn a lot about how to create a (unique) parent structure. \n\nI don't quite understand how the method `stretch` works, but I'll try to figure out. However, I think a more useful thing to implement would be the action by permutation of variables. I.e., \n\n```\nsage: X.<x,y> = InfinitePolynomialRing(QQ) \nsage: P = Permutation(((0,1),(2,3,4)))\nsage: a = x[3] + y[2] + x[0]*y[1]\nsage: a^P\nx1*y0 + x4 + y3\n```\n\nThat's to say, `x[i]` is mapped by `P` to `x[P(i)]`.\n\nHowever I am not sure whether it is a good idea to implement things on top of usual finitely generated polynomial algebras. After all, they are parent structures and are thus cached -- and my successively fill up memory. \n\nWhat happens if you do the following?\n\n```\nsage: X.<x> = InfinitePolynomialRing(QQ) \nsage: p = x[0]\nsage: while(1):\n....:     p = p.stretch(2)\n....:     print p\n```\n\n\nDoes it soon fill up the whole memory with huge (but finite) polynomial rings? And is much time being spent with creating these rings?\n\nSorry that I can't test the example myself (will only be possible next week). But perhaps you can tell me what happens.\n\nCheers,\n     Simon",
    "created_at": "2009-03-07T21:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42225",
    "user": "@simon-king-jena"
}
```

Dear Mike,

Cool! Thank you that you started an implementation!

Certainly from your patch I learn a lot about how to create a (unique) parent structure. 

I don't quite understand how the method `stretch` works, but I'll try to figure out. However, I think a more useful thing to implement would be the action by permutation of variables. I.e., 

```
sage: X.<x,y> = InfinitePolynomialRing(QQ) 
sage: P = Permutation(((0,1),(2,3,4)))
sage: a = x[3] + y[2] + x[0]*y[1]
sage: a^P
x1*y0 + x4 + y3
```

That's to say, `x[i]` is mapped by `P` to `x[P(i)]`.

However I am not sure whether it is a good idea to implement things on top of usual finitely generated polynomial algebras. After all, they are parent structures and are thus cached -- and my successively fill up memory. 

What happens if you do the following?

```
sage: X.<x> = InfinitePolynomialRing(QQ) 
sage: p = x[0]
sage: while(1):
....:     p = p.stretch(2)
....:     print p
```


Does it soon fill up the whole memory with huge (but finite) polynomial rings? And is much time being spent with creating these rings?

Sorry that I can't test the example myself (will only be possible next week). But perhaps you can tell me what happens.

Cheers,
     Simon



---

archive/issue_comments_042226.json:
```json
{
    "body": "Replying to [comment:1 SimonKing]:\nOops, I had a typo in this example:\n\n> What happens if you do the following?\n> {{{\n> sage: X.<x> = InfinitePolynomialRing(QQ) \n> sage: p = x[0]\n> sage: while(1):\n> ....:     p = p.stretch(2)\n> ....:     print p\n> }}}\n\nIt should be `p = x[1]`, to that in the loop `p` becomes `x[2]`, `x[4]`, `x[8]`, ...",
    "created_at": "2009-03-07T21:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42226",
    "user": "@simon-king-jena"
}
```

Replying to [comment:1 SimonKing]:
Oops, I had a typo in this example:

> What happens if you do the following?
> {{{
> sage: X.<x> = InfinitePolynomialRing(QQ) 
> sage: p = x[0]
> sage: while(1):
> ....:     p = p.stretch(2)
> ....:     print p
> }}}

It should be `p = x[1]`, to that in the loop `p` becomes `x[2]`, `x[4]`, `x[8]`, ...



---

archive/issue_comments_042227.json:
```json
{
    "body": "Changing assignee from @malb to @mwhansen.",
    "created_at": "2009-03-07T21:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42227",
    "user": "@mwhansen"
}
```

Changing assignee from @malb to @mwhansen.



---

archive/issue_comments_042228.json:
```json
{
    "body": "Replying to [comment:1 SimonKing]:\n> Cool! Thank you that you started an implementation!\n\nActually, it's code that I've had on the combinat patch server for awhile since I have code that makes use of these things.\n \n> I don't quite understand how the method `stretch` works, but I'll try to figure out. \n\nStretch is actually something that I needed.\n\n> However, I think a more useful thing to implement would be the action by permutation of variables. I.e., \n> {{{\n> sage: X.<x,y> = InfinitePolynomialRing(QQ) \n> sage: P = Permutation(((0,1),(2,3,4)))\n> sage: a = x[3] + y[2] + x[0]*y[1]\n> sage: a^P\n> x1*y0 + x4 + y3\n> }}}\n> That's to say, `x[i]` is mapped by `P` to `x[P(i)]`.\n\nSure.\n\n> However I am not sure whether it is a good idea to implement things on top of usual finitely generated polynomial algebras. After all, they are parent structures and are thus cached -- and my successively fill up memory. \n> What happens if you do the following?\n> ...\n> Does it soon fill up the whole memory with huge (but finite) polynomial rings? And is much time being spent with creating these rings?\n\nYep (that's what you can with infinite loops :-)  For my application, doing the arithmetic will the primary bottleneck.\n\nLike I said, this was a very basic implementation that I wrote because it does what I need and I was able to write it relatively quickly.  I used the existing finite polynomial rings because they already do fast arithmetic that I (personally) have no desire to duplicate.",
    "created_at": "2009-03-07T21:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42228",
    "user": "@mwhansen"
}
```

Replying to [comment:1 SimonKing]:
> Cool! Thank you that you started an implementation!

Actually, it's code that I've had on the combinat patch server for awhile since I have code that makes use of these things.
 
> I don't quite understand how the method `stretch` works, but I'll try to figure out. 

Stretch is actually something that I needed.

> However, I think a more useful thing to implement would be the action by permutation of variables. I.e., 
> {{{
> sage: X.<x,y> = InfinitePolynomialRing(QQ) 
> sage: P = Permutation(((0,1),(2,3,4)))
> sage: a = x[3] + y[2] + x[0]*y[1]
> sage: a^P
> x1*y0 + x4 + y3
> }}}
> That's to say, `x[i]` is mapped by `P` to `x[P(i)]`.

Sure.

> However I am not sure whether it is a good idea to implement things on top of usual finitely generated polynomial algebras. After all, they are parent structures and are thus cached -- and my successively fill up memory. 
> What happens if you do the following?
> ...
> Does it soon fill up the whole memory with huge (but finite) polynomial rings? And is much time being spent with creating these rings?

Yep (that's what you can with infinite loops :-)  For my application, doing the arithmetic will the primary bottleneck.

Like I said, this was a very basic implementation that I wrote because it does what I need and I was able to write it relatively quickly.  I used the existing finite polynomial rings because they already do fast arithmetic that I (personally) have no desire to duplicate.



---

archive/issue_comments_042229.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-07T21:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42229",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042230.json:
```json
{
    "body": "Hi Mike,\n\nReplying to [comment:3 mhansen]:\n> Stretch is actually something that I needed.\n\nOf course, this is why one implements things. My aim is to have the Gr\u00f6bner basis theory of Aschenbrenner and Hillar implemented in Sage, and actually I have potential applications to 3-dimensional topology in the background. \n\nAnd for this, the permutation actions are essential. \n\nBut independent from this, I think the implementation should be more sparse.\n\n> Yep (that's what you can with infinite loops :-)  For my application, doing the arithmetic will the primary bottleneck.\n\nFor me, arithmetic will certainly be a bottleneck, too. I mean, it is about computing Gr\u00f6bner bases, and if this is done then there still remains to compute normal forms for really *really* huge polynomials.\n\n> I used the existing finite polynomial rings because they already do fast arithmetic that I (personally) have no desire to duplicate.\n\nYep. It is very reasonable to try and avoid duplication! \n\nBut how? Perhaps it would be better if the f.g. polynomial rings were more hidden. For example, the elements of an infinite polynomial ring could be described not simply as a polynomial (say, `x100*x101+x90`) but as a pair formed by a polynomial in a smaller ring and an offset, say `(90,x10*x11+x0)`, or perhaps by an even smaller polynomial and a permutation, say `(((0,90),(1,100),(2,101)), x1*x2+x0)`.\n\nI think a compromise between speed and size makes sense. Or perhaps even concurrent models, similar to dense vs. sparse matrices.\n\nSince I am rather tired, I don't know if all this makes sense, though...",
    "created_at": "2009-03-07T22:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42230",
    "user": "@simon-king-jena"
}
```

Hi Mike,

Replying to [comment:3 mhansen]:
> Stretch is actually something that I needed.

Of course, this is why one implements things. My aim is to have the Gröbner basis theory of Aschenbrenner and Hillar implemented in Sage, and actually I have potential applications to 3-dimensional topology in the background. 

And for this, the permutation actions are essential. 

But independent from this, I think the implementation should be more sparse.

> Yep (that's what you can with infinite loops :-)  For my application, doing the arithmetic will the primary bottleneck.

For me, arithmetic will certainly be a bottleneck, too. I mean, it is about computing Gröbner bases, and if this is done then there still remains to compute normal forms for really *really* huge polynomials.

> I used the existing finite polynomial rings because they already do fast arithmetic that I (personally) have no desire to duplicate.

Yep. It is very reasonable to try and avoid duplication! 

But how? Perhaps it would be better if the f.g. polynomial rings were more hidden. For example, the elements of an infinite polynomial ring could be described not simply as a polynomial (say, `x100*x101+x90`) but as a pair formed by a polynomial in a smaller ring and an offset, say `(90,x10*x11+x0)`, or perhaps by an even smaller polynomial and a permutation, say `(((0,90),(1,100),(2,101)), x1*x2+x0)`.

I think a compromise between speed and size makes sense. Or perhaps even concurrent models, similar to dense vs. sparse matrices.

Since I am rather tired, I don't know if all this makes sense, though...



---

archive/issue_comments_042231.json:
```json
{
    "body": "Replying to [comment:4 SimonKing]:\n\n> But how? Perhaps it would be better if the f.g. polynomial rings were more hidden. For example, the elements of an infinite polynomial ring could be described not simply as a polynomial (say, `x100*x101+x90`) but as a pair formed by a polynomial in a smaller ring and an offset, say `(90,x10*x11+x0)`, or perhaps by an even smaller polynomial and a permutation, say `(((0,90),(1,100),(2,101)), x1*x2+x0)`.\n> \n> I think a compromise between speed and size makes sense. Or perhaps even concurrent models, similar to dense vs. sparse matrices.\n\nYes, I even mention this in the documentation that the current implementation is definitely tailored to what I needed and that it would be a good project to have different backends.\n\nThe primary problem will be doing the arithmetic efficiently.  This is not my area of expertise though.",
    "created_at": "2009-03-07T22:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42231",
    "user": "@mwhansen"
}
```

Replying to [comment:4 SimonKing]:

> But how? Perhaps it would be better if the f.g. polynomial rings were more hidden. For example, the elements of an infinite polynomial ring could be described not simply as a polynomial (say, `x100*x101+x90`) but as a pair formed by a polynomial in a smaller ring and an offset, say `(90,x10*x11+x0)`, or perhaps by an even smaller polynomial and a permutation, say `(((0,90),(1,100),(2,101)), x1*x2+x0)`.
> 
> I think a compromise between speed and size makes sense. Or perhaps even concurrent models, similar to dense vs. sparse matrices.

Yes, I even mention this in the documentation that the current implementation is definitely tailored to what I needed and that it would be a good project to have different backends.

The primary problem will be doing the arithmetic efficiently.  This is not my area of expertise though.



---

archive/issue_comments_042232.json:
```json
{
    "body": "Sorry, the patch failed to apply. It says\n\n```\nunable to find 'doc/en/reference/polynomial_rings.rst' for patching\n1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/polynomial_rings.rst.rej\nabort: patch failed to apply\n```\n\n\nWhat went wrong?",
    "created_at": "2009-03-08T16:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42232",
    "user": "@simon-king-jena"
}
```

Sorry, the patch failed to apply. It says

```
unable to find 'doc/en/reference/polynomial_rings.rst' for patching
1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/polynomial_rings.rst.rej
abort: patch failed to apply
```


What went wrong?



---

archive/issue_comments_042233.json:
```json
{
    "body": "Are you running a Sage 3.4 release?  If not, that is the problem because the patch touches the new documentation.",
    "created_at": "2009-03-08T18:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42233",
    "user": "@mwhansen"
}
```

Are you running a Sage 3.4 release?  If not, that is the problem because the patch touches the new documentation.



---

archive/issue_comments_042234.json:
```json
{
    "body": "Replying to [comment:7 mhansen]:\n> Are you running a Sage 3.4 release?  If not, that is the problem because the patch touches the new documentation.\n\nNo, I only have Sage 3.3. Is Sage 3.4 already out? I'll upgrade, or get the 3.4-sources.\n\nCheers\n      Simon",
    "created_at": "2009-03-09T07:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42234",
    "user": "@simon-king-jena"
}
```

Replying to [comment:7 mhansen]:
> Are you running a Sage 3.4 release?  If not, that is the problem because the patch touches the new documentation.

No, I only have Sage 3.3. Is Sage 3.4 already out? I'll upgrade, or get the 3.4-sources.

Cheers
      Simon



---

archive/issue_comments_042235.json:
```json
{
    "body": "Replying to [comment:8 SimonKing]:\n> No, I only have Sage 3.3. Is Sage 3.4 already out? I'll upgrade, or get the 3.4-sources.\n\nI made it differently: I removed the .rst-part from the patch; after removing ReST, the rest worked in Sage 3.3...\n\nAnyway. I think the whole story should be made more sparse. \n\nI suggest to use the method `change_ring()` of polynomial rings in the background. Then, `stretch()` could be implemented along these lines:\n\n```\nsage: R.<x1,y1>=QQ[]\nsage: p=R.random_element()\nsage: p\n-x1^2 - 1/4*y1^2 - 1/2*y1 - 1\nsage: S=R.change_ring(names=['x2','y2'])\nsage: p=S(p)\nsage: p\n-x2^2 - 1/4*y2^2 - 1/2*y2 - 1\nsage: S=S.change_ring(names=['x4','y4'])\nsage: p=S(p)\nsage: p\n-x4^2 - 1/4*y4^2 - 1/2*y4 - 1\n```\n\n\nIn that way, one could keep the underlying ring small.\n\nProblem though: How to add things, if the underlying polynomial rings are different? Probably you know much more about coercion than I do. But I guess it should be possible to automatically find a common parent for the summands as follows:\n\n```\nsage: q=R.random_element()\nsage: q\n1/3*x1^2 + 1/12*x1*y1 - 3/10*y1^2 + x1\nsage: Varnames=set([str(X) for X in p.variables()]+[str(X) for X in q.variables()])\nsage: T=PolynomialRing(QQ,list(Varnames))\nsage: T(p)+T(q)\n-3/10*y1^2 + 1/12*y1*x1 + 1/3*x1^2 - 1/4*y4^2 - x4^2 + x1 - 1/2*y4 - 1\n```\n\n\nThis could be done behind the scenes.\n\nIn the example above, I did not take care about the monomial order, though. This needs to be dealt with in a proper implementation.\n\nCheers,\n    Simon",
    "created_at": "2009-03-09T09:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42235",
    "user": "@simon-king-jena"
}
```

Replying to [comment:8 SimonKing]:
> No, I only have Sage 3.3. Is Sage 3.4 already out? I'll upgrade, or get the 3.4-sources.

I made it differently: I removed the .rst-part from the patch; after removing ReST, the rest worked in Sage 3.3...

Anyway. I think the whole story should be made more sparse. 

I suggest to use the method `change_ring()` of polynomial rings in the background. Then, `stretch()` could be implemented along these lines:

```
sage: R.<x1,y1>=QQ[]
sage: p=R.random_element()
sage: p
-x1^2 - 1/4*y1^2 - 1/2*y1 - 1
sage: S=R.change_ring(names=['x2','y2'])
sage: p=S(p)
sage: p
-x2^2 - 1/4*y2^2 - 1/2*y2 - 1
sage: S=S.change_ring(names=['x4','y4'])
sage: p=S(p)
sage: p
-x4^2 - 1/4*y4^2 - 1/2*y4 - 1
```


In that way, one could keep the underlying ring small.

Problem though: How to add things, if the underlying polynomial rings are different? Probably you know much more about coercion than I do. But I guess it should be possible to automatically find a common parent for the summands as follows:

```
sage: q=R.random_element()
sage: q
1/3*x1^2 + 1/12*x1*y1 - 3/10*y1^2 + x1
sage: Varnames=set([str(X) for X in p.variables()]+[str(X) for X in q.variables()])
sage: T=PolynomialRing(QQ,list(Varnames))
sage: T(p)+T(q)
-3/10*y1^2 + 1/12*y1*x1 + 1/3*x1^2 - 1/4*y4^2 - x4^2 + x1 - 1/2*y4 - 1
```


This could be done behind the scenes.

In the example above, I did not take care about the monomial order, though. This needs to be dealt with in a proper implementation.

Cheers,
    Simon



---

archive/issue_comments_042236.json:
```json
{
    "body": "Replying to [comment:9 SimonKing]:\n> I suggest to use the method `change_ring()` of polynomial rings in the background. Then, `stretch()` could be implemented along these lines:\n...\n\nIt seems that indeed the `while` loop that I gave above is both faster and goes further when using my suggestion:\n\n```\nsage: R.<x1,y1>=QQ[]\nsage: p=x1\nsage: S=R.change_ring(names=['x2','y2'])\nsage: n=2\nsage: while(1):\n....:     p=S(p)\n....:     n=2*n\n....:     S=S.change_ring(names=['x%d'%(n),'y%d'%(n)])\n....:     print p\n....:\nx2\nx4\nx8\nx16\nx32\nx64\nx128\nx256\nx512\nx1024\nx2048\nx4096\nx8192\nx16384\nx32768\nx65536\nx131072\nx262144\nx524288\nx1048576\nx2097152\nx4194304\nx8388608\nx16777216\nx33554432\nx67108864\nx134217728\nx268435456\nx536870912\nx1073741824\nx2147483648\nx4294967296\nx8589934592\nx17179869184\nx34359738368\nx68719476736\nx137438953472\nx274877906944\nx549755813888\nx1099511627776\nx2199023255552\nx4398046511104\nx8796093022208\nx17592186044416\nx35184372088832\nx70368744177664\nx140737488355328\nx281474976710656\nx562949953421312\nx1125899906842624\nx2251799813685248\nx4503599627370496\nx9007199254740992\nx18014398509481984\nx36028797018963968\nx72057594037927936\nx144115188075855872\nx288230376151711744\nx576460752303423488\nx1152921504606846976\nx2305843009213693952\n```\n\n\nOnly at that point was a type error, because the next number is not an `int` anymore.\n\nSo, my suggestions are: \n* An `InfinitePolynomialRing` should *not* have an underlying polynomial ring by itself.\n* Only the *elements* of an `InfinitePolynomialRing` should have an underlying polynomial ring.\n\nThe advantage of my suggestion is that the rings become much smaller.\n\nCheers,\n     Simon",
    "created_at": "2009-03-09T11:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42236",
    "user": "@simon-king-jena"
}
```

Replying to [comment:9 SimonKing]:
> I suggest to use the method `change_ring()` of polynomial rings in the background. Then, `stretch()` could be implemented along these lines:
...

It seems that indeed the `while` loop that I gave above is both faster and goes further when using my suggestion:

```
sage: R.<x1,y1>=QQ[]
sage: p=x1
sage: S=R.change_ring(names=['x2','y2'])
sage: n=2
sage: while(1):
....:     p=S(p)
....:     n=2*n
....:     S=S.change_ring(names=['x%d'%(n),'y%d'%(n)])
....:     print p
....:
x2
x4
x8
x16
x32
x64
x128
x256
x512
x1024
x2048
x4096
x8192
x16384
x32768
x65536
x131072
x262144
x524288
x1048576
x2097152
x4194304
x8388608
x16777216
x33554432
x67108864
x134217728
x268435456
x536870912
x1073741824
x2147483648
x4294967296
x8589934592
x17179869184
x34359738368
x68719476736
x137438953472
x274877906944
x549755813888
x1099511627776
x2199023255552
x4398046511104
x8796093022208
x17592186044416
x35184372088832
x70368744177664
x140737488355328
x281474976710656
x562949953421312
x1125899906842624
x2251799813685248
x4503599627370496
x9007199254740992
x18014398509481984
x36028797018963968
x72057594037927936
x144115188075855872
x288230376151711744
x576460752303423488
x1152921504606846976
x2305843009213693952
```


Only at that point was a type error, because the next number is not an `int` anymore.

So, my suggestions are: 
* An `InfinitePolynomialRing` should *not* have an underlying polynomial ring by itself.
* Only the *elements* of an `InfinitePolynomialRing` should have an underlying polynomial ring.

The advantage of my suggestion is that the rings become much smaller.

Cheers,
     Simon



---

archive/issue_comments_042237.json:
```json
{
    "body": "I think I will be able to provide an alternative (=sparse) implementation soon. I think for `stretch` and the to-be-implemented permutation action, the sparse version is more convenient, while arithmetic might be faster in the dense version. However, I can only start the work on Wednesday.\n\nCan you tell me what (coercion?) methods are needed to provide in order to have a smooth transition from sparse to dense and from dense to sparse?\n\nAnd then I think there should also be a `subs` method, based on which it would be easy to implement a permutation action.",
    "created_at": "2009-03-09T16:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42237",
    "user": "@simon-king-jena"
}
```

I think I will be able to provide an alternative (=sparse) implementation soon. I think for `stretch` and the to-be-implemented permutation action, the sparse version is more convenient, while arithmetic might be faster in the dense version. However, I can only start the work on Wednesday.

Can you tell me what (coercion?) methods are needed to provide in order to have a smooth transition from sparse to dense and from dense to sparse?

And then I think there should also be a `subs` method, based on which it would be easy to implement a permutation action.



---

archive/issue_comments_042238.json:
```json
{
    "body": "Hi Mike!\n\nNow, being back at work, I try an alternative implementation.\n\nI wondered why you define `_coerce_map_from_` to return False whenever the second argument is an infinite polynomial ring (different from self, of course).\n\nWhat do you think:\n* Should there be a coercion between two infinite polynomial rings that have the same variables in different order, such as \n\n```\nsage: X.<x,y> = InfinitePolynomialRing(QQ)\nsage: Y.<y,x> = InfinitePolynomialRing(QQ)\n```\n\n I believe it should, because one also has \n\n```\nsage: X.<x,y> = PolynomialRing(QQ)\nsage: Y.<y,x> = PolynomialRing(QQ)\nsage: X.has_coerce_map_from(Y)\nTrue\n```\n",
    "created_at": "2009-03-12T09:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42238",
    "user": "@simon-king-jena"
}
```

Hi Mike!

Now, being back at work, I try an alternative implementation.

I wondered why you define `_coerce_map_from_` to return False whenever the second argument is an infinite polynomial ring (different from self, of course).

What do you think:
* Should there be a coercion between two infinite polynomial rings that have the same variables in different order, such as 

```
sage: X.<x,y> = InfinitePolynomialRing(QQ)
sage: Y.<y,x> = InfinitePolynomialRing(QQ)
```

 I believe it should, because one also has 

```
sage: X.<x,y> = PolynomialRing(QQ)
sage: Y.<y,x> = PolynomialRing(QQ)
sage: X.has_coerce_map_from(Y)
True
```




---

archive/issue_comments_042239.json:
```json
{
    "body": "Hi Mike,\n\nI found a point that I think requires more work:\n\n```\nsage: X.<x,y> = InfinitePolynomialRing(QQ)\nsage: x[1]/y[2]\nx1/y2\nsage: _.parent()\nInfinite polynomial ring in x, y over Rational Field\n```\n\n\nHence, suddenly one has fractions, but they still belong to a **polynomial** ring. And:\n\n```\nsage: (x[1]/y[2]).parent().polynomial_ring()\nMultivariate Polynomial Ring in x0, y0, x1, y1, x2, y2 over Rational Field\nsage: (x[1]/y[2])._p.parent()\nFraction Field of Multivariate Polynomial Ring in x0, y0, x1, y1, x2, y2 over Rational Field\n```\n\n\nSo, the parent of `x[1]/y[1]` expressed as a finite polynomial is a fraction field and is different from the underlying ring of the parent of `x[1]/y[1]`.\n\nDo you agree that this should be sorted out?",
    "created_at": "2009-03-12T12:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42239",
    "user": "@simon-king-jena"
}
```

Hi Mike,

I found a point that I think requires more work:

```
sage: X.<x,y> = InfinitePolynomialRing(QQ)
sage: x[1]/y[2]
x1/y2
sage: _.parent()
Infinite polynomial ring in x, y over Rational Field
```


Hence, suddenly one has fractions, but they still belong to a **polynomial** ring. And:

```
sage: (x[1]/y[2]).parent().polynomial_ring()
Multivariate Polynomial Ring in x0, y0, x1, y1, x2, y2 over Rational Field
sage: (x[1]/y[2])._p.parent()
Fraction Field of Multivariate Polynomial Ring in x0, y0, x1, y1, x2, y2 over Rational Field
```


So, the parent of `x[1]/y[1]` expressed as a finite polynomial is a fraction field and is different from the underlying ring of the parent of `x[1]/y[1]`.

Do you agree that this should be sorted out?



---

archive/issue_comments_042240.json:
```json
{
    "body": "Meanwhile I implemented my approach to infinite polynomial rings. For the moment, I call them \"symmetric polynomials\", since Aschenbrenner and Hillar use the notion \"symmetric ideals\" (and implementing the algorithms of Aschenbrenner and Hillar is my aim).\n\nMike, since I took your implementation as a template, I named both you and me in the copyright notes.\n\nI provide essentially the same methods than you. Main changes, compared with your implementation:\n* The `__pow__` method now also provides a permutation action.\n* The stretch method is **much** faster than in your implementation.\n* In order to have a sparse implementation, I probably had to take a compromise speed-wise. Can you please look whether the arithmetic in `SymmetricPolynomialRing` is sufficient for your purposes?\n* I allow coercions whenever variable names match (i.e., I coerce R into S if the generator names of R form a subset of the generator names of S, regardless of the order). Is this acceptable behaviour?\n\nI took care about term orders. We have x[m]<y[n] iff\n* x appears before y in the list of generators, or\n* x=y and m<n\n\nOne technical question: I marked the `_coerce_map_from_` method as `@`cached. Is this allowed (probably yes, since we talk about parent structures, and they can be used in dictionaries)? Is this not necessary (perhaps the existence of coercions is cached anyway?)?\n\nHere some examples:\n\n```\nsage: X.<x,y> = SymmetricPolynomialRing(QQ)\nsage: p=x[10]*y[2]^3+2*x[1]*y[3]\nsage: P=Permutation(((1,2),(3,4,5)))\nsage: p^P\ny1^3*x10 + 2*y4*x2\nsage: x[5]<y[3]\nTrue\nsage: y[5]<y[3]\nFalse\nsage: p(x1=x[3],x10=y[1])\ny2^3*y1 + 2*y3*x3\n```\n\n\nI could imagine to have both implementations in Sage, in particular if it turns out that there is a big speed difference in arithmetic. Please test!\n\nTo be continued (probably on a different ticket): Implement symmetric ideals (= ideals in an infinite polynomial ring that are set-wise invariant under variable permutations).",
    "created_at": "2009-03-13T10:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42240",
    "user": "@simon-king-jena"
}
```

Meanwhile I implemented my approach to infinite polynomial rings. For the moment, I call them "symmetric polynomials", since Aschenbrenner and Hillar use the notion "symmetric ideals" (and implementing the algorithms of Aschenbrenner and Hillar is my aim).

Mike, since I took your implementation as a template, I named both you and me in the copyright notes.

I provide essentially the same methods than you. Main changes, compared with your implementation:
* The `__pow__` method now also provides a permutation action.
* The stretch method is **much** faster than in your implementation.
* In order to have a sparse implementation, I probably had to take a compromise speed-wise. Can you please look whether the arithmetic in `SymmetricPolynomialRing` is sufficient for your purposes?
* I allow coercions whenever variable names match (i.e., I coerce R into S if the generator names of R form a subset of the generator names of S, regardless of the order). Is this acceptable behaviour?

I took care about term orders. We have x[m]<y[n] iff
* x appears before y in the list of generators, or
* x=y and m<n

One technical question: I marked the `_coerce_map_from_` method as `@`cached. Is this allowed (probably yes, since we talk about parent structures, and they can be used in dictionaries)? Is this not necessary (perhaps the existence of coercions is cached anyway?)?

Here some examples:

```
sage: X.<x,y> = SymmetricPolynomialRing(QQ)
sage: p=x[10]*y[2]^3+2*x[1]*y[3]
sage: P=Permutation(((1,2),(3,4,5)))
sage: p^P
y1^3*x10 + 2*y4*x2
sage: x[5]<y[3]
True
sage: y[5]<y[3]
False
sage: p(x1=x[3],x10=y[1])
y2^3*y1 + 2*y3*x3
```


I could imagine to have both implementations in Sage, in particular if it turns out that there is a big speed difference in arithmetic. Please test!

To be continued (probably on a different ticket): Implement symmetric ideals (= ideals in an infinite polynomial ring that are set-wise invariant under variable permutations).



---

archive/issue_comments_042241.json:
```json
{
    "body": "This patch removes some print commands that I forgot to remove after debugging. To be applied after the other two patches",
    "created_at": "2009-03-13T10:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42241",
    "user": "@simon-king-jena"
}
```

This patch removes some print commands that I forgot to remove after debugging. To be applied after the other two patches



---

archive/issue_comments_042242.json:
```json
{
    "body": "Attachment [symmetric_polynomial_update.patch](tarball://root/attachments/some-uuid/ticket5453/symmetric_polynomial_update.patch) by @simon-king-jena created at 2009-03-13 10:44:55\n\nI forgot one change w.r.t. your implementation: Division is not implemented except for scalar divisors.\n\nContinuing the example from above:\n\n```\nsage: p/X(3)\n1/3*y2^3*x10 + 2/3*y3*x1\nsage: p/p\nNotImplementedError                       Traceback (most recent call last)\n...\nNotImplementedError: Fraction Fields of Symmetric Polynomial Rings are not implemented\n```\n\n\nCheers,\n    Simon",
    "created_at": "2009-03-13T10:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42242",
    "user": "@simon-king-jena"
}
```

Attachment [symmetric_polynomial_update.patch](tarball://root/attachments/some-uuid/ticket5453/symmetric_polynomial_update.patch) by @simon-king-jena created at 2009-03-13 10:44:55

I forgot one change w.r.t. your implementation: Division is not implemented except for scalar divisors.

Continuing the example from above:

```
sage: p/X(3)
1/3*y2^3*x10 + 2/3*y3*x1
sage: p/p
NotImplementedError                       Traceback (most recent call last)
...
NotImplementedError: Fraction Fields of Symmetric Polynomial Rings are not implemented
```


Cheers,
    Simon



---

archive/issue_comments_042243.json:
```json
{
    "body": "Sorry. I just realized that it works when I *attach* `symmetric_polynomial.py` (this is how I obtained my examples above), but when I apply the patches and do ` sage -b` then sage fails on start-up, apparently when my file tries to import `Permutation_class`.\n\nCan you explain this? I have to return home right now, but perhaps you know how to fix it.\n\nCheers,\n   Simon",
    "created_at": "2009-03-13T10:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42243",
    "user": "@simon-king-jena"
}
```

Sorry. I just realized that it works when I *attach* `symmetric_polynomial.py` (this is how I obtained my examples above), but when I apply the patches and do ` sage -b` then sage fails on start-up, apparently when my file tries to import `Permutation_class`.

Can you explain this? I have to return home right now, but perhaps you know how to fix it.

Cheers,
   Simon



---

archive/issue_comments_042244.json:
```json
{
    "body": "Attachment [symmetric_polynomial.patch](tarball://root/attachments/some-uuid/ticket5453/symmetric_polynomial.patch) by @simon-king-jena created at 2009-03-13 20:09:45\n\nTo be applied after mhansen's patch. Replaces the other 'symmetric polynomial' patches",
    "created_at": "2009-03-13T20:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42244",
    "user": "@simon-king-jena"
}
```

Attachment [symmetric_polynomial.patch](tarball://root/attachments/some-uuid/ticket5453/symmetric_polynomial.patch) by @simon-king-jena created at 2009-03-13 20:09:45

To be applied after mhansen's patch. Replaces the other 'symmetric polynomial' patches



---

archive/issue_comments_042245.json:
```json
{
    "body": "(Concerning the patches: Please first apply `trac_5453.patch` and then `symmetric_polynomial.patch`. The third patch is now obsolete.)\n\nI sorted the above mentioned import problem out (import of `Permutation_class`). Instead of importing this class and doing `is_instance`, I now test the presence of the attribute {{{to_cycles()}.\n\nAnd, to my surprise, the arithmetics is faster than the \"dense\" implementation. I don't know the reason. \nHere, I make some very basic timings for `InfinitePolynomialRing` versus `SymmetricPolynomialRing`:\n\n```\nsage: X.<x,y> = SymmetricPolynomialRing(QQ)\nsage: Y.<a,b> = InfinitePolynomialRing(QQ)\nsage: p=x[10]*y[2]^3+2*x[1]*y[3]\nsage: p2=x[100]*y[20]^3+2*x[10]*y[30]\nsage: q=a[10]*b[2]^3+2*a[1]*b[3]\nsage: q2=a[100]*b[20]^3+2*a[10]*b[30]\nsage: timeit('r=p*p2')\n625 loops, best of 3: 1.15 ms per loop\nsage: timeit('r=q*q2')\n125 loops, best of 3: 3.68 ms per loop\nsage: timeit('r=p+p2')\n625 loops, best of 3: 1.14 ms per loop\nsage: timeit('r=q+q2')\n125 loops, best of 3: 3.69 ms per loop\n```\n\n\nCheers,\n  Simon",
    "created_at": "2009-03-13T20:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42245",
    "user": "@simon-king-jena"
}
```

(Concerning the patches: Please first apply `trac_5453.patch` and then `symmetric_polynomial.patch`. The third patch is now obsolete.)

I sorted the above mentioned import problem out (import of `Permutation_class`). Instead of importing this class and doing `is_instance`, I now test the presence of the attribute {{{to_cycles()}.

And, to my surprise, the arithmetics is faster than the "dense" implementation. I don't know the reason. 
Here, I make some very basic timings for `InfinitePolynomialRing` versus `SymmetricPolynomialRing`:

```
sage: X.<x,y> = SymmetricPolynomialRing(QQ)
sage: Y.<a,b> = InfinitePolynomialRing(QQ)
sage: p=x[10]*y[2]^3+2*x[1]*y[3]
sage: p2=x[100]*y[20]^3+2*x[10]*y[30]
sage: q=a[10]*b[2]^3+2*a[1]*b[3]
sage: q2=a[100]*b[20]^3+2*a[10]*b[30]
sage: timeit('r=p*p2')
625 loops, best of 3: 1.15 ms per loop
sage: timeit('r=q*q2')
125 loops, best of 3: 3.68 ms per loop
sage: timeit('r=p+p2')
625 loops, best of 3: 1.14 ms per loop
sage: timeit('r=q+q2')
125 loops, best of 3: 3.69 ms per loop
```


Cheers,
  Simon



---

archive/issue_comments_042246.json:
```json
{
    "body": "Recall that the starting point of my implementation was that the stretch method of the dense implementation requires too many resources in some cases.\n\nHowever, my stretch implementation is *slower* than yours, as long as the stretch factor is small and as long as one uses `timeit` and not `time`. \n\nThe reason is: The critical part of the dense stretch method is the creation of a large polynomial ring. Once this is done, the ring is re-used, and it is very fast. In contrast, the sparse stretch method only creates a small ring (faster), but this has to be repeated over and over again.\n\nTherefore one has:\n\n```\nsage: X.<x,y> = SymmetricPolynomialRing(QQ)\nsage: Y.<a,b> = InfinitePolynomialRing(QQ)\nsage: timeit('t=x[10].stretch(10)')\n625 loops, best of 3: 194 \u00c2\u00b5s per loop\nsage: timeit('t=a[10].stretch(10)')\n625 loops, best of 3: 92.8 \u00c2\u00b5s per loop\nsage: timeit('t=(x[10]*y[5]+x[100]*y[83]).stretch(500)')\n125 loops, best of 3: 2.29 ms per loop\nsage: time t=(a[10]*b[5]+a[100]*b[83]).stretch(500) # fails after 2:30 minutes:\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\n\nSo again, this is an argument to include *both* implementation into Sage. That way, one can pick the method that is better for the respective application.\n\nBut who will review our patches? I guess neither of us. Should we ping malb?",
    "created_at": "2009-03-14T10:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42246",
    "user": "@simon-king-jena"
}
```

Recall that the starting point of my implementation was that the stretch method of the dense implementation requires too many resources in some cases.

However, my stretch implementation is *slower* than yours, as long as the stretch factor is small and as long as one uses `timeit` and not `time`. 

The reason is: The critical part of the dense stretch method is the creation of a large polynomial ring. Once this is done, the ring is re-used, and it is very fast. In contrast, the sparse stretch method only creates a small ring (faster), but this has to be repeated over and over again.

Therefore one has:

```
sage: X.<x,y> = SymmetricPolynomialRing(QQ)
sage: Y.<a,b> = InfinitePolynomialRing(QQ)
sage: timeit('t=x[10].stretch(10)')
625 loops, best of 3: 194 Âµs per loop
sage: timeit('t=a[10].stretch(10)')
625 loops, best of 3: 92.8 Âµs per loop
sage: timeit('t=(x[10]*y[5]+x[100]*y[83]).stretch(500)')
125 loops, best of 3: 2.29 ms per loop
sage: time t=(a[10]*b[5]+a[100]*b[83]).stretch(500) # fails after 2:30 minutes:
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```


So again, this is an argument to include *both* implementation into Sage. That way, one can pick the method that is better for the respective application.

But who will review our patches? I guess neither of us. Should we ping malb?



---

archive/issue_comments_042247.json:
```json
{
    "body": "From the outstanding discussion it seems this needs work rather than review already.",
    "created_at": "2009-03-16T11:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42247",
    "user": "@malb"
}
```

From the outstanding discussion it seems this needs work rather than review already.



---

archive/issue_comments_042248.json:
```json
{
    "body": "Replying to [comment:19 malb]:\n> From the outstanding discussion it seems this needs work rather than review already.\n\nYes, I think you are right. \n\nAt least I would like to work a lot more on my implementation. But perhaps you think that Mike's patch is ready for inclusion? I wouldn't mind to let Mike's patch being merged and open a different ticket for my patch.",
    "created_at": "2009-03-16T12:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42248",
    "user": "@simon-king-jena"
}
```

Replying to [comment:19 malb]:
> From the outstanding discussion it seems this needs work rather than review already.

Yes, I think you are right. 

At least I would like to work a lot more on my implementation. But perhaps you think that Mike's patch is ready for inclusion? I wouldn't mind to let Mike's patch being merged and open a different ticket for my patch.



---

archive/issue_comments_042249.json:
```json
{
    "body": "I think at least the interface should be agreed upon first. \n\n\n```\nsage: X.<x,y> = SymmetricPolynomialRing(QQ)\nsage: Y.<a,b> = InfinitePolynomialRing(QQ)\n```\n\n\nshould be one name only and a parameters `dense`/`sparse` just like matrices.",
    "created_at": "2009-03-16T12:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42249",
    "user": "@malb"
}
```

I think at least the interface should be agreed upon first. 


```
sage: X.<x,y> = SymmetricPolynomialRing(QQ)
sage: Y.<a,b> = InfinitePolynomialRing(QQ)
```


should be one name only and a parameters `dense`/`sparse` just like matrices.



---

archive/issue_comments_042250.json:
```json
{
    "body": "Replying to [comment:21 malb]:\n> I think at least the interface should be agreed upon first. \n> \n> {{{\n> sage: X.<x,y> = SymmetricPolynomialRing(QQ)\n> sage: Y.<a,b> = InfinitePolynomialRing(QQ)\n> }}}\n> \n> should be one name only and a parameters `dense`/`sparse` just like matrices.\n\nMakes sense.\n\nI vote for the name `SymmetricPolynomialRing`, since Aschenbrenner and Hillar use the notion \"Symmetric Ideals\", e.g. in  arXiv:math/0411514 (\"Finite generation of symmetric ideals\"). Of course, when choosing this name, a permutation action should be implemented. But this can be easily done for Mike's approach as well.\n\nBut then, we should also agree on monomial orderings. Meanwhile, I am implementing support for different orderings (lex, deglex, degrevlex). But in either case, I have\n  X.gen(i)[m] < X.gen(j)[n] iff i<j or (i==j and m<n)\n\nIs this acceptable for you, Mike and Martin?",
    "created_at": "2009-03-16T12:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42250",
    "user": "@simon-king-jena"
}
```

Replying to [comment:21 malb]:
> I think at least the interface should be agreed upon first. 
> 
> {{{
> sage: X.<x,y> = SymmetricPolynomialRing(QQ)
> sage: Y.<a,b> = InfinitePolynomialRing(QQ)
> }}}
> 
> should be one name only and a parameters `dense`/`sparse` just like matrices.

Makes sense.

I vote for the name `SymmetricPolynomialRing`, since Aschenbrenner and Hillar use the notion "Symmetric Ideals", e.g. in  arXiv:math/0411514 ("Finite generation of symmetric ideals"). Of course, when choosing this name, a permutation action should be implemented. But this can be easily done for Mike's approach as well.

But then, we should also agree on monomial orderings. Meanwhile, I am implementing support for different orderings (lex, deglex, degrevlex). But in either case, I have
  X.gen(i)[m] < X.gen(j)[n] iff i<j or (i==j and m<n)

Is this acceptable for you, Mike and Martin?



---

archive/issue_comments_042251.json:
```json
{
    "body": "I think it makes more sense to develop the *sparse* approach on a different ticket -- see [#5566].\nHence, one should disregard my attachments, as everything is now at [#5566]...\n\nAnd, concerning a common interface, I think it would be almost trivial to change the whole thing so that `SymmetricPolynomialRing(QQ,['x'],implementation='dense')` returns the same as `InfinitePolynomialRing(QQ,['x'])`\n\nCan we agree to split the tickets, so that Mike's original ticket is now 'with patch, needs review'?",
    "created_at": "2009-03-19T15:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42251",
    "user": "@simon-king-jena"
}
```

I think it makes more sense to develop the *sparse* approach on a different ticket -- see [#5566].
Hence, one should disregard my attachments, as everything is now at [#5566]...

And, concerning a common interface, I think it would be almost trivial to change the whole thing so that `SymmetricPolynomialRing(QQ,['x'],implementation='dense')` returns the same as `InfinitePolynomialRing(QQ,['x'])`

Can we agree to split the tickets, so that Mike's original ticket is now 'with patch, needs review'?



---

archive/issue_comments_042252.json:
```json
{
    "body": "Replying to [comment:23 SimonKing]:\n> And, concerning a common interface, I think it would be almost trivial to change the whole thing so that `SymmetricPolynomialRing(QQ,['x'],implementation='dense')` returns the same as `InfinitePolynomialRing(QQ,['x'])`\n\nAt least some agreement on the name should be reached.",
    "created_at": "2009-03-19T15:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42252",
    "user": "@malb"
}
```

Replying to [comment:23 SimonKing]:
> And, concerning a common interface, I think it would be almost trivial to change the whole thing so that `SymmetricPolynomialRing(QQ,['x'],implementation='dense')` returns the same as `InfinitePolynomialRing(QQ,['x'])`

At least some agreement on the name should be reached.



---

archive/issue_comments_042253.json:
```json
{
    "body": "Replying to [comment:24 malb]:\n> At least some agreement on the name should be reached.\n\nI sketched my opinion already: \n* If the aim is an implementation of the algorithm of Aschenbrenner and Hillar, we should use the word ``Symmetric``, since they do.\n* If it is just about having a convenient way to provide an unbounded number of variables, than ``InfinitePolynomialRing`` is fine as well. \n* Since i think that the most ambitious part of the implementation is in fact the Gr\u00f6bner basis computation, I vote for 'Symmetric'.\n\nBut what do you think?",
    "created_at": "2009-03-20T20:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42253",
    "user": "@simon-king-jena"
}
```

Replying to [comment:24 malb]:
> At least some agreement on the name should be reached.

I sketched my opinion already: 
* If the aim is an implementation of the algorithm of Aschenbrenner and Hillar, we should use the word ``Symmetric``, since they do.
* If it is just about having a convenient way to provide an unbounded number of variables, than ``InfinitePolynomialRing`` is fine as well. 
* Since i think that the most ambitious part of the implementation is in fact the Gröbner basis computation, I vote for 'Symmetric'.

But what do you think?



---

archive/issue_comments_042254.json:
```json
{
    "body": "Let me add my two cents: It seems to me that the if something is called \"the ring of symmetric polynomials\" this is *not* what you implement under the name `SymetricPolynomialRing` so that I'm against such a name. \n\nAnother argument is that it is extremely likely that some people working in combinatorics will need \"the ring of symmetric polynomials\" (in a finite number of variable). We already have a the ring of \"symmetric functions\" that is the case of an infinite number of variables. Note that, whether they are polynomials or not is always subject to discussion: they have an infinite number of monomials but they have a finite degree. We (combinatorician) choose the name functions for those finite degree series in an infinite number of variables.\n\nAnyway, going back to your case, what about `PolynomialRingWithSymmetry` ?\n\nCheers,\n\nFlorent",
    "created_at": "2009-03-28T19:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42254",
    "user": "@hivert"
}
```

Let me add my two cents: It seems to me that the if something is called "the ring of symmetric polynomials" this is *not* what you implement under the name `SymetricPolynomialRing` so that I'm against such a name. 

Another argument is that it is extremely likely that some people working in combinatorics will need "the ring of symmetric polynomials" (in a finite number of variable). We already have a the ring of "symmetric functions" that is the case of an infinite number of variables. Note that, whether they are polynomials or not is always subject to discussion: they have an infinite number of monomials but they have a finite degree. We (combinatorician) choose the name functions for those finite degree series in an infinite number of variables.

Anyway, going back to your case, what about `PolynomialRingWithSymmetry` ?

Cheers,

Florent



---

archive/issue_comments_042255.json:
```json
{
    "body": "Dear Florent,\n\nthank you very much for the input!\n\nReplying to [comment:26 hivert]:\n> Let me add my two cents: It seems to me that the if something is called \"the ring of symmetric polynomials\" this is *not* what you implement under the name `SymetricPolynomialRing` so that I'm against such a name. \n\nIt is correct that the *polynomials* are not symmetric. But the ring has an action of an infinite symmetric group, and the (or at least *my*) motivation was an implementation of Symmetric Ideals (they do deserve the attribute 'symmetric') and their Gr\u00f6bner bases (see ticket #5566). So, it is not the 'ring of symmetric polynomials' but a 'symmetric ring of polynomials'.\n\n> Another argument is that it is extremely likely that some people working in combinatorics will need \"the ring of symmetric polynomials\" (in a finite number of variable). \n\nThat's half right. Aren't these called 'invariant rings' rather than 'symmetric rings'?\n\n> We already have a the ring of \"symmetric functions\" that is the case of an infinite number of variables. Note that, whether they are polynomials or not is always subject to discussion: they have an infinite number of monomials but they have a finite degree. We (combinatorician) choose the name functions for those finite degree series in an infinite number of variables.\n\nHere we clearly talk about polynomials: The elements of the 'infinite' or 'symmetric' polynomial ring are *finite* sums of monomials. While the number of variables in the ring is infinite, the number of variables occuring in one polynomial is finite.",
    "created_at": "2009-03-28T20:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42255",
    "user": "@simon-king-jena"
}
```

Dear Florent,

thank you very much for the input!

Replying to [comment:26 hivert]:
> Let me add my two cents: It seems to me that the if something is called "the ring of symmetric polynomials" this is *not* what you implement under the name `SymetricPolynomialRing` so that I'm against such a name. 

It is correct that the *polynomials* are not symmetric. But the ring has an action of an infinite symmetric group, and the (or at least *my*) motivation was an implementation of Symmetric Ideals (they do deserve the attribute 'symmetric') and their Gröbner bases (see ticket #5566). So, it is not the 'ring of symmetric polynomials' but a 'symmetric ring of polynomials'.

> Another argument is that it is extremely likely that some people working in combinatorics will need "the ring of symmetric polynomials" (in a finite number of variable). 

That's half right. Aren't these called 'invariant rings' rather than 'symmetric rings'?

> We already have a the ring of "symmetric functions" that is the case of an infinite number of variables. Note that, whether they are polynomials or not is always subject to discussion: they have an infinite number of monomials but they have a finite degree. We (combinatorician) choose the name functions for those finite degree series in an infinite number of variables.

Here we clearly talk about polynomials: The elements of the 'infinite' or 'symmetric' polynomial ring are *finite* sums of monomials. While the number of variables in the ring is infinite, the number of variables occuring in one polynomial is finite.



---

archive/issue_comments_042256.json:
```json
{
    "body": "Dear Florent,\n\nReplying to [comment:27 SimonKing]:\n> It is correct that the *polynomials* are not symmetric. But the ring has an action of an infinite symmetric group, and the (or at least *my*) motivation was an implementation of Symmetric Ideals (they do deserve the attribute 'symmetric') and their Gr\u00f6bner bases (see ticket #5566). So, it is not the 'ring of symmetric polynomials' but a 'symmetric ring of polynomials'.\n\nI think my suggestion \"symmetric polynomial ring\" is partially due to the fact that in German it is \"symmetrischer Polynomring\" -- hence, clearly it is a polynomial ring that has a symmetry, and not a ring of symmetric polynomials (\"Ring symmetrischer Polynome\" in German). \n\nPerhaps native english speakers can help here:\n\nIs your suggestion \"polynomial ring with symmetry\" the shortest way to express \"symmetrischer Polynomring\" in English? \n\nIs the natural English understanding \"((symmetric polynomial) ring)\" or \"(symmetric (polynomial ring))\"?\n\nBest regards,\n     Simon",
    "created_at": "2009-03-28T22:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42256",
    "user": "@simon-king-jena"
}
```

Dear Florent,

Replying to [comment:27 SimonKing]:
> It is correct that the *polynomials* are not symmetric. But the ring has an action of an infinite symmetric group, and the (or at least *my*) motivation was an implementation of Symmetric Ideals (they do deserve the attribute 'symmetric') and their Gröbner bases (see ticket #5566). So, it is not the 'ring of symmetric polynomials' but a 'symmetric ring of polynomials'.

I think my suggestion "symmetric polynomial ring" is partially due to the fact that in German it is "symmetrischer Polynomring" -- hence, clearly it is a polynomial ring that has a symmetry, and not a ring of symmetric polynomials ("Ring symmetrischer Polynome" in German). 

Perhaps native english speakers can help here:

Is your suggestion "polynomial ring with symmetry" the shortest way to express "symmetrischer Polynomring" in English? 

Is the natural English understanding "((symmetric polynomial) ring)" or "(symmetric (polynomial ring))"?

Best regards,
     Simon



---

archive/issue_comments_042257.json:
```json
{
    "body": "Hi!\n\nI just had a look at the abstract of Aschenbrenner's and Hillar's articles. The title of one article is \"An Algorithm for Finding Symmetric Gr\u00f6bner Bases in Infinite Dimensional Rings\". They talk about \"symmetric ideals\", but again they say \"infinite dimensional polynomial ring\", not \"symmetric polynomial ring\".\n\nThis convinces me that Mike's InfinitePolynomialRing is better than SymmetricPolynomialRing, and that the word \"symmetric\" should be reserved to the ideals and Gr\u00f6bner bases of that ring.\n\nHere some thoughts about a unification:\n   Both in Mike's and my implementation, an element p of the ring R essentially has an attribute _p, which is a 'usual' polynomial: p._p gives the value of p. \n   In Mike's implementation, the ring R has and attribute P (a polynomial ring) so that p._p is guaranteed to be coercible into P, for any `p \\in R`. This allows for usual arithmetic.\n   In my implementation, it is possible that coercion does not provide arithmetic for p._p and q._p, for p and q in R. *Only* if it does not, then i explicitly construct a common parent for p._p and q._p. So, Mike's arithmetic is a special case of mine.\n\nDo we agree on the following technical details of a potential unification?\n* Compared with SymmetricPolynomialRing_class, InfinitePolynomialRing_class has one additional attribute `P`, and the arithmetic of InfinitePolynomial is just a special case of the arithmetic of SymmetricPolynomial. So, the init method might have an optional parameter `implementation`, and if this is 'dense' then the ring is initialized together with an attribute `P`. Otherwise, it is without `P`.\n* In the methods of InfinitePolynomial and SymmetricIdeal, we could test whether the underlying infinite ring has an attribute P. If it has (dense implementation), the methods choose your algorithm, otherwise they choose mine. \n\nIn the end, we would have a dense and a sparse implementation, and the computation of symmetric Gr\u00f6bner bases would be possible in *both* cases.\n\nDo you think it works? How should the work be organised? Here? #5566? New ticket?\n\nCheers\n     Simon",
    "created_at": "2009-03-29T00:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42257",
    "user": "@simon-king-jena"
}
```

Hi!

I just had a look at the abstract of Aschenbrenner's and Hillar's articles. The title of one article is "An Algorithm for Finding Symmetric Gröbner Bases in Infinite Dimensional Rings". They talk about "symmetric ideals", but again they say "infinite dimensional polynomial ring", not "symmetric polynomial ring".

This convinces me that Mike's InfinitePolynomialRing is better than SymmetricPolynomialRing, and that the word "symmetric" should be reserved to the ideals and Gröbner bases of that ring.

Here some thoughts about a unification:
   Both in Mike's and my implementation, an element p of the ring R essentially has an attribute _p, which is a 'usual' polynomial: p._p gives the value of p. 
   In Mike's implementation, the ring R has and attribute P (a polynomial ring) so that p._p is guaranteed to be coercible into P, for any `p \in R`. This allows for usual arithmetic.
   In my implementation, it is possible that coercion does not provide arithmetic for p._p and q._p, for p and q in R. *Only* if it does not, then i explicitly construct a common parent for p._p and q._p. So, Mike's arithmetic is a special case of mine.

Do we agree on the following technical details of a potential unification?
* Compared with SymmetricPolynomialRing_class, InfinitePolynomialRing_class has one additional attribute `P`, and the arithmetic of InfinitePolynomial is just a special case of the arithmetic of SymmetricPolynomial. So, the init method might have an optional parameter `implementation`, and if this is 'dense' then the ring is initialized together with an attribute `P`. Otherwise, it is without `P`.
* In the methods of InfinitePolynomial and SymmetricIdeal, we could test whether the underlying infinite ring has an attribute P. If it has (dense implementation), the methods choose your algorithm, otherwise they choose mine. 

In the end, we would have a dense and a sparse implementation, and the computation of symmetric Gröbner bases would be possible in *both* cases.

Do you think it works? How should the work be organised? Here? #5566? New ticket?

Cheers
     Simon



---

archive/issue_comments_042258.json:
```json
{
    "body": "Meanwhile i can provide a uniform interface for the dense and the sparse approach. In both approaches, one can compute symmetric Gr\u00f6bner bases. And: Dense seems indeed to be faster.\n\nSince i am owner for #5566, i've put my patch there. Hope you are not upset.\n\nThe name of the rings is now InfinitePolynomialRing, and they can be created in dense or sparse implementation.\n\nDue to differences in the interface of uni- and multivariate polynomials, a bug occured in the reduce method; i need to fix this, thus #5566 currently is 'needs work'. But perhaps you can already have a look if the implementation makes sense.",
    "created_at": "2009-03-30T11:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42258",
    "user": "@simon-king-jena"
}
```

Meanwhile i can provide a uniform interface for the dense and the sparse approach. In both approaches, one can compute symmetric Gröbner bases. And: Dense seems indeed to be faster.

Since i am owner for #5566, i've put my patch there. Hope you are not upset.

The name of the rings is now InfinitePolynomialRing, and they can be created in dense or sparse implementation.

Due to differences in the interface of uni- and multivariate polynomials, a bug occured in the reduce method; i need to fix this, thus #5566 currently is 'needs work'. But perhaps you can already have a look if the implementation makes sense.



---

archive/issue_comments_042259.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T18:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42259",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_042260.json:
```json
{
    "body": "This was fixed due to #5556.",
    "created_at": "2009-06-04T18:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5453#issuecomment-42260",
    "user": "@mwhansen"
}
```

This was fixed due to #5556.
