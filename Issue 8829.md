# Issue 8829: Saturation for curves over number fields.

archive/issues_008829.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  @pjbruin @kedlaya\n\nI also implemented the simple case of E.gens() for E(K) when E/Q and [K:Q] = 2.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8829\n\n",
    "created_at": "2010-04-30T06:49:16Z",
    "labels": [
        "component: elliptic curves"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.1",
    "title": "Saturation for curves over number fields.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8829",
    "user": "https://github.com/robertwb"
}
```
Assignee: @JohnCremona

CC:  @pjbruin @kedlaya

I also implemented the simple case of E.gens() for E(K) when E/Q and [K:Q] = 2.

Issue created by migration from https://trac.sagemath.org/ticket/8829





---

archive/issue_comments_080984.json:
```json
{
    "body": "Some dependance on #8828.",
    "created_at": "2010-04-30T06:50:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80984",
    "user": "https://github.com/robertwb"
}
```

Some dependance on #8828.



---

archive/issue_comments_080985.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-30T06:50:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80985",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080986.json:
```json
{
    "body": "I have had a quick look and will go through this in more detail later (after #8828 is completed, probably).  I spent a long time on my C++ implementation of this (over QQ but the algorithm is general) so am quite familiar with the details.\n\nHere are two references you should give:  [1] S. Siksek \"Infinite descent on elliptic curves\", Rocky Mountain J of M, Vol 25 No. 4 (1995), 1501-1538.  [2] M. Prickett, \"Saturation of Mordell-Weil groups of elliptic curves over number fields\", U of Nottingham PhD thesis (2004), http://etheses.nottingham.ac.uk/52/.\n\nMartin Prickett implemented this in Magma, but the code was very slow and hard to read so it never got incorporated into Magma releases.\n\nIncidentally, it was for this that I implemented group structure for curves over GF(q) in the first place!  In my C++ implementation I cache a lot of the information of this group structure so that when you do p-saturation for larger and larger p, the structures are already there.  A good example is to take one of those curves of very high rank:  I think I once successfully p-saturated the rank 24 curve at all p < `10^6`  (the bound was totally out of reach, something like `10^100`).\n\nAnother point which might be useful over number fields:  it suffices to use degree one primes to reduce modulo.",
    "created_at": "2010-04-30T08:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80986",
    "user": "https://github.com/JohnCremona"
}
```

I have had a quick look and will go through this in more detail later (after #8828 is completed, probably).  I spent a long time on my C++ implementation of this (over QQ but the algorithm is general) so am quite familiar with the details.

Here are two references you should give:  [1] S. Siksek "Infinite descent on elliptic curves", Rocky Mountain J of M, Vol 25 No. 4 (1995), 1501-1538.  [2] M. Prickett, "Saturation of Mordell-Weil groups of elliptic curves over number fields", U of Nottingham PhD thesis (2004), http://etheses.nottingham.ac.uk/52/.

Martin Prickett implemented this in Magma, but the code was very slow and hard to read so it never got incorporated into Magma releases.

Incidentally, it was for this that I implemented group structure for curves over GF(q) in the first place!  In my C++ implementation I cache a lot of the information of this group structure so that when you do p-saturation for larger and larger p, the structures are already there.  A good example is to take one of those curves of very high rank:  I think I once successfully p-saturated the rank 24 curve at all p < `10^6`  (the bound was totally out of reach, something like `10^100`).

Another point which might be useful over number fields:  it suffices to use degree one primes to reduce modulo.



---

archive/issue_comments_080987.json:
```json
{
    "body": "Attachment [8829-ec-nf-sat.patch](tarball://root/attachments/some-uuid/ticket8829/8829-ec-nf-sat.patch) by @robertwb created at 2010-04-30 08:39:16",
    "created_at": "2010-04-30T08:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80987",
    "user": "https://github.com/robertwb"
}
```

Attachment [8829-ec-nf-sat.patch](tarball://root/attachments/some-uuid/ticket8829/8829-ec-nf-sat.patch) by @robertwb created at 2010-04-30 08:39:16



---

archive/issue_comments_080988.json:
```json
{
    "body": "Replying to [comment:2 cremona]:\n> I have had a quick look and will go through this in more detail later (after #8828 is completed, probably).  I spent a long time on my C++ implementation of this (over QQ but the algorithm is general) so am quite familiar with the details.\n> \n> Here are two references you should give:  [1] S. Siksek \"Infinite descent on elliptic curves\", Rocky Mountain J of M, Vol 25 No. 4 (1995), 1501-1538.  [2] M. Prickett, \"Saturation of Mordell-Weil groups of elliptic curves over number fields\", U of Nottingham PhD thesis (2004), http://etheses.nottingham.ac.uk/52/.\n\nAh, those look like good references to read too :). \n\n> Martin Prickett implemented this in Magma, but the code was very slow and hard to read so it never got incorporated into Magma releases.\n> \n> Incidentally, it was for this that I implemented group structure for curves over GF(q) in the first place!  In my C++ implementation I cache a lot of the information of this group structure so that when you do p-saturation for larger and larger p, the structures are already there.  \n\nThe way I do it is consider many p at once, and for each curve over GF(q) I see which primes in my set it could help with, though this won't scale as far. I'm sure there's still lots of room for improvement. \n\n> A good example is to take one of those curves of very high rank:  I think I once successfully p-saturated the rank 24 curve at all p < `10^6`  (the bound was totally out of reach, something like `10^100`).\n\nThat reminds me--I was wondering if there's any way to go from min(h(P)) to a bound on the regulator for rank > 1. \n\n> Another point which might be useful over number fields:  it suffices to use degree one primes to reduce modulo.\n\nGood point. Those get pretty rare for large degree number fields though, right?",
    "created_at": "2010-04-30T08:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80988",
    "user": "https://github.com/robertwb"
}
```

Replying to [comment:2 cremona]:
> I have had a quick look and will go through this in more detail later (after #8828 is completed, probably).  I spent a long time on my C++ implementation of this (over QQ but the algorithm is general) so am quite familiar with the details.
> 
> Here are two references you should give:  [1] S. Siksek "Infinite descent on elliptic curves", Rocky Mountain J of M, Vol 25 No. 4 (1995), 1501-1538.  [2] M. Prickett, "Saturation of Mordell-Weil groups of elliptic curves over number fields", U of Nottingham PhD thesis (2004), http://etheses.nottingham.ac.uk/52/.

Ah, those look like good references to read too :). 

> Martin Prickett implemented this in Magma, but the code was very slow and hard to read so it never got incorporated into Magma releases.
> 
> Incidentally, it was for this that I implemented group structure for curves over GF(q) in the first place!  In my C++ implementation I cache a lot of the information of this group structure so that when you do p-saturation for larger and larger p, the structures are already there.  

The way I do it is consider many p at once, and for each curve over GF(q) I see which primes in my set it could help with, though this won't scale as far. I'm sure there's still lots of room for improvement. 

> A good example is to take one of those curves of very high rank:  I think I once successfully p-saturated the rank 24 curve at all p < `10^6`  (the bound was totally out of reach, something like `10^100`).

That reminds me--I was wondering if there's any way to go from min(h(P)) to a bound on the regulator for rank > 1. 

> Another point which might be useful over number fields:  it suffices to use degree one primes to reduce modulo.

Good point. Those get pretty rare for large degree number fields though, right?



---

archive/issue_comments_080989.json:
```json
{
    "body": "You might also like to look at my C++ code which is in eclib, in src/qcurves.  I can point to the right files if it is not clear.  In case you wonder, \"TLSS\" stands for \"Tate-Lichtenbaum-Samir_Siksek\" since I use the TL map when the p-torsion in E(GF(q)) is not cyclic and Samir's original method when it is.  Samir only used reduction modulo primes where p exactly divided the order, and in particular for which the reduction had cyclic p-part.  But Martin and I discovered that this can fail when there is a p-isogeny.  Here, fail means in the sense that there can exist points which are not multiples of p in E(QQ) but which map to zero in E(GF(q))/p for all q.\n\nIn MP's thesis he proves that this cannot happen if you use all q, or all but a finite number, or all but a finite number of degree 1 primes, .... some of these  results we then found had been proved elsewhere (3 or 4 times, independently, within 3 or 4 years!).  But it can happen if you leave out the q for which the quotient has non-cyclic p-part.",
    "created_at": "2010-04-30T11:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80989",
    "user": "https://github.com/JohnCremona"
}
```

You might also like to look at my C++ code which is in eclib, in src/qcurves.  I can point to the right files if it is not clear.  In case you wonder, "TLSS" stands for "Tate-Lichtenbaum-Samir_Siksek" since I use the TL map when the p-torsion in E(GF(q)) is not cyclic and Samir's original method when it is.  Samir only used reduction modulo primes where p exactly divided the order, and in particular for which the reduction had cyclic p-part.  But Martin and I discovered that this can fail when there is a p-isogeny.  Here, fail means in the sense that there can exist points which are not multiples of p in E(QQ) but which map to zero in E(GF(q))/p for all q.

In MP's thesis he proves that this cannot happen if you use all q, or all but a finite number, or all but a finite number of degree 1 primes, .... some of these  results we then found had been proved elsewhere (3 or 4 times, independently, within 3 or 4 years!).  But it can happen if you leave out the q for which the quotient has non-cyclic p-part.



---

archive/issue_comments_080990.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-09T17:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80990",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080991.json:
```json
{
    "body": "Patch applies fine to 4.4.1 and tests pass.\n\nThis functionality is badly needed!\n\nWe now have heights for points on curves defined over number_fields\nbut no associated regulator function.  I suggest that the function\nregulator_of_points() be moved up from ell_rational_field to\nell_number_field.  This tcan then be called instead of the code in\nlines 424-432 [line numbers are from the patched file, not the patch].\n\nLine 439 uses a function self.height_function() which does not exist.\nThis block needs to be replaced by something sensible.  If one has a lower bound on the height of non-torsion\npoints, then a bound on the index can be deduced from standard\ngeometry of numbers estimates.   To get such a lower bound, see papers\nof Cremona & Siksek (over Q) and Thongjunthug (over number fields) for\nan algorithm which would need to be implemented.  (Not hard over Q,\nnot much harder for totally real fields, quite a lot worse over fields\nwith a complex embedding).  Until this is done, I don't think this\nsaturation function can allow maxprime==0.\n\nIn the rank one code:   when large primes p (say, over 20!) are being\ntested then the division_points code will be expensive since it\ninvolves constructing the multiplication-by-p map.  I would recommend\nusing a reduction strategy here just as in the general case.  To check\np-saturation just find primes q such that #E(Fq) is divisible by p and\nthen see if the reduction of P mod q is a multiple of p.  This will\nalmost always prove saturation very quickly.  If it fails for several\n(say 5) q then try to divide P by p;  else use more q, and so on.\nThere is one theoretical drawback here:  this strategy might fail if\nthere is a rational p-isogeny.  Over Q,  we know which p this might\nhappen for and I would first test for the existence of isogenies of\nprimes degree, and use the division test (as here) for any primes that\nshow up.  Over number fields that's harder to deal with, but again we\ncan fall back on the division test to rpove that P cannot be divided\nby p.\n\nThe function list_of_multiples(P,n) duplicated the generic function\nmultiples() which I wrote for just this sort of purpose!\n\nI don't like the loop through all linear combinations for small\nprimes.  Even with p=2 there are curves with 24 independent points out\nthere and `2^24` divisions is not nice to contemplate.  If you want this\nshort cut, do it based on the size of `p^r`.\n\nThe main code with reduction etc looks fine to me (but I did not check\nthe logic rigorously).\n\nThe gens function for E(K) when E is defined over Q and [K:Q]=2 looks\nfine.  For a more general case we could always try using\nsimon_two_descent (followed by saturation).  Trying such an examples\nled me to:\n\n```\nsage: K.<a> = NumberField(x^2-2)\nsage: E = EllipticCurve([a,0])\nsage: P = E(0,0)\nsage: P.has_finite_order()\nTrue\nsage: P.order()\n2\nsage: P.height()\n0\nsage: E.saturation([P], verbose=True, max_prime=5)\n## infinite loop\n```\n\nThis is caused as follows:   The height matrix is [0] with det=0 but\nreg / min(heights) is NaN so reg / min(heights) < 1e-6 is False!.\nThis will need fixing.  At the very least, I would discard any points\nof finite order before doing anything else with them.  Then\nmin(heights) will never be 0.\n\nMost of the above is easy to deal with.  The hard part is computing a\nsuitable max_prime form a lower height bound on points.  I suggest\nthat for now you make it compulsory to have a positive max_prime and\nadd a TODO.",
    "created_at": "2010-05-09T17:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80991",
    "user": "https://github.com/JohnCremona"
}
```

Patch applies fine to 4.4.1 and tests pass.

This functionality is badly needed!

We now have heights for points on curves defined over number_fields
but no associated regulator function.  I suggest that the function
regulator_of_points() be moved up from ell_rational_field to
ell_number_field.  This tcan then be called instead of the code in
lines 424-432 [line numbers are from the patched file, not the patch].

Line 439 uses a function self.height_function() which does not exist.
This block needs to be replaced by something sensible.  If one has a lower bound on the height of non-torsion
points, then a bound on the index can be deduced from standard
geometry of numbers estimates.   To get such a lower bound, see papers
of Cremona & Siksek (over Q) and Thongjunthug (over number fields) for
an algorithm which would need to be implemented.  (Not hard over Q,
not much harder for totally real fields, quite a lot worse over fields
with a complex embedding).  Until this is done, I don't think this
saturation function can allow maxprime==0.

In the rank one code:   when large primes p (say, over 20!) are being
tested then the division_points code will be expensive since it
involves constructing the multiplication-by-p map.  I would recommend
using a reduction strategy here just as in the general case.  To check
p-saturation just find primes q such that #E(Fq) is divisible by p and
then see if the reduction of P mod q is a multiple of p.  This will
almost always prove saturation very quickly.  If it fails for several
(say 5) q then try to divide P by p;  else use more q, and so on.
There is one theoretical drawback here:  this strategy might fail if
there is a rational p-isogeny.  Over Q,  we know which p this might
happen for and I would first test for the existence of isogenies of
primes degree, and use the division test (as here) for any primes that
show up.  Over number fields that's harder to deal with, but again we
can fall back on the division test to rpove that P cannot be divided
by p.

The function list_of_multiples(P,n) duplicated the generic function
multiples() which I wrote for just this sort of purpose!

I don't like the loop through all linear combinations for small
primes.  Even with p=2 there are curves with 24 independent points out
there and `2^24` divisions is not nice to contemplate.  If you want this
short cut, do it based on the size of `p^r`.

The main code with reduction etc looks fine to me (but I did not check
the logic rigorously).

The gens function for E(K) when E is defined over Q and [K:Q]=2 looks
fine.  For a more general case we could always try using
simon_two_descent (followed by saturation).  Trying such an examples
led me to:

```
sage: K.<a> = NumberField(x^2-2)
sage: E = EllipticCurve([a,0])
sage: P = E(0,0)
sage: P.has_finite_order()
True
sage: P.order()
2
sage: P.height()
0
sage: E.saturation([P], verbose=True, max_prime=5)
## infinite loop
```

This is caused as follows:   The height matrix is [0] with det=0 but
reg / min(heights) is NaN so reg / min(heights) < 1e-6 is False!.
This will need fixing.  At the very least, I would discard any points
of finite order before doing anything else with them.  Then
min(heights) will never be 0.

Most of the above is easy to deal with.  The hard part is computing a
suitable max_prime form a lower height bound on points.  I suggest
that for now you make it compulsory to have a positive max_prime and
add a TODO.



---

archive/issue_comments_080992.json:
```json
{
    "body": "Thank you for all your input. `self.height_function` comes from #8828, though as you suggest we could make max_prime mandatory for now (and for rank > 1 once that goes in). That's a good point about large primes in the rank one case. I found the loop through all linear combinations to be much faster in practice for small primes, but the hard coded `p == 2` case was left by accident, I meant to cap that on `p^r` as I did the others. \n\nI probably won't fix and polish this up before finishing my thesis, but at the latest we should be able to get it done during the workshop at MSRI next month.",
    "created_at": "2010-05-11T18:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80992",
    "user": "https://github.com/robertwb"
}
```

Thank you for all your input. `self.height_function` comes from #8828, though as you suggest we could make max_prime mandatory for now (and for rank > 1 once that goes in). That's a good point about large primes in the rank one case. I found the loop through all linear combinations to be much faster in practice for small primes, but the hard coded `p == 2` case was left by accident, I meant to cap that on `p^r` as I did the others. 

I probably won't fix and polish this up before finishing my thesis, but at the latest we should be able to get it done during the workshop at MSRI next month.



---

archive/issue_comments_080993.json:
```json
{
    "body": "Replying to [comment:6 robertwb]:\n> Thank you for all your input. `self.height_function` comes from #8828, though as you suggest we could make max_prime mandatory for now (and for rank > 1 once that goes in). That's a good point about large primes in the rank one case. I found the loop through all linear combinations to be much faster in practice for small primes, but the hard coded `p == 2` case was left by accident, I meant to cap that on `p^r` as I did the others. \n> \n> I probably won't fix and polish this up before finishing my thesis, but at the latest we should be able to get it done during the workshop at MSRI next month. \n\nOK -- looking forward to it!  I'll take a look at #8828 by then as well.",
    "created_at": "2010-05-11T20:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80993",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:6 robertwb]:
> Thank you for all your input. `self.height_function` comes from #8828, though as you suggest we could make max_prime mandatory for now (and for rank > 1 once that goes in). That's a good point about large primes in the rank one case. I found the loop through all linear combinations to be much faster in practice for small primes, but the hard coded `p == 2` case was left by accident, I meant to cap that on `p^r` as I did the others. 
> 
> I probably won't fix and polish this up before finishing my thesis, but at the latest we should be able to get it done during the workshop at MSRI next month. 

OK -- looking forward to it!  I'll take a look at #8828 by then as well.



---

archive/issue_comments_080994.json:
```json
{
    "body": "Since rwb is now busy at Google, and I want this functionality, I am now implementing the changes I suggested above!",
    "created_at": "2010-06-29T04:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80994",
    "user": "https://github.com/JohnCremona"
}
```

Since rwb is now busy at Google, and I want this functionality, I am now implementing the changes I suggested above!



---

archive/issue_comments_080995.json:
```json
{
    "body": "I made a separate ticket for the regulator functions.  See #9372.",
    "created_at": "2010-06-29T04:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80995",
    "user": "https://github.com/JohnCremona"
}
```

I made a separate ticket for the regulator functions.  See #9372.



---

archive/issue_comments_080996.json:
```json
{
    "body": "How is this going John?  It seems to have been awhile....",
    "created_at": "2012-10-15T09:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80996",
    "user": "https://github.com/roed314"
}
```

How is this going John?  It seems to have been awhile....



---

archive/issue_comments_080997.json:
```json
{
    "body": "See #12509: until we can fix the height computation, saturation cannot be carried out properly.  It's still on my to-do list though.",
    "created_at": "2013-01-08T09:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80997",
    "user": "https://github.com/JohnCremona"
}
```

See #12509: until we can fix the height computation, saturation cannot be carried out properly.  It's still on my to-do list though.



---

archive/issue_comments_080998.json:
```json
{
    "body": "Replying to [comment:11 cremona]:\n> See #12509: until we can fix the height computation, saturation cannot be carried out properly.  It's still on my to-do list though.\n\n#12509 is now up for review.",
    "created_at": "2013-01-10T09:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80998",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:11 cremona]:
> See #12509: until we can fix the height computation, saturation cannot be carried out properly.  It's still on my to-do list though.

#12509 is now up for review.



---

archive/issue_events_021551.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8829#event-21551"
}
```



---

archive/issue_events_021552.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8829#event-21552"
}
```



---

archive/issue_events_021553.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8829#event-21553"
}
```



---

archive/issue_events_021554.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8829#event-21554"
}
```



---

archive/issue_events_021555.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8829#event-21555"
}
```



---

archive/issue_events_021556.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8829#event-21556"
}
```



---

archive/issue_events_021557.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8829#event-21557"
}
```



---

archive/issue_comments_080999.json:
```json
{
    "body": "I do not know why this was left drifting, but I really need it myself now so will look at it again, rebase on 6.8 and see what we can do.  But I only have one day before a week off, so...",
    "created_at": "2015-08-13T16:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-80999",
    "user": "https://github.com/JohnCremona"
}
```

I do not know why this was left drifting, but I really need it myself now so will look at it again, rebase on 6.8 and see what we can do.  But I only have one day before a week off, so...



---

archive/issue_comments_081000.json:
```json
{
    "body": "Changing keywords from \"\" to \"saturation\".",
    "created_at": "2015-09-11T16:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81000",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "" to "saturation".



---

archive/issue_comments_081001.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-09-11T16:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81001",
    "user": "https://github.com/JohnCremona"
}
```

New commits:



---

archive/issue_comments_081002.json:
```json
{
    "body": "Current branch works but more doctests and testing are needed; so not ready for review yet.\n\nI did a lot of rewriting of the main saturation routine, separating off p-saturation and also allowing saturation to be done at just one prime.  This is a useful special case, since if you take the images of some saturated points under a p-isogeny the images may not be p-saturated but will still be saturated at all other primes.\n\nThe code for computing E(K) when K is quadratic and E is a base change has been completely rewritten and will now work in many more cases (not just when the coefficients of E are in Q).",
    "created_at": "2015-09-11T16:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81002",
    "user": "https://github.com/JohnCremona"
}
```

Current branch works but more doctests and testing are needed; so not ready for review yet.

I did a lot of rewriting of the main saturation routine, separating off p-saturation and also allowing saturation to be done at just one prime.  This is a useful special case, since if you take the images of some saturated points under a p-isogeny the images may not be p-saturated but will still be saturated at all other primes.

The code for computing E(K) when K is quadratic and E is a base change has been completely rewritten and will now work in many more cases (not just when the coefficients of E are in Q).



---

archive/issue_comments_081003.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-09-14T16:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81003",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081004.json:
```json
{
    "body": "The latest commit involves more than adding more doctests to the new functions, since bugs were revealed which led to a rewrite of the sieving code for the two cases where the p-rank of the reduction is 1 or 2; the former uses discrete log in the reduction, the latter uses Weil pairing and discrte log in the multiplicative group.  In the sieve I restrict to primes of degree 1.  It is a Theorem (see http://eprints.nottingham.ac.uk/10052/) that this will suffice to prove p-saturation, provided that one does use reductions with p-rank 2 and not just those of p-rank 1 as originally suggested by Siksek in https://ore.exeter.ac.uk/repository/handle/10871/8323 .\n\nI will mark this as ready for review so the bots get to work on it, and of course humans are welcome to look at the new code, but I will now test it thoroughly on the LMFDB curves and report back.",
    "created_at": "2015-09-14T16:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81004",
    "user": "https://github.com/JohnCremona"
}
```

The latest commit involves more than adding more doctests to the new functions, since bugs were revealed which led to a rewrite of the sieving code for the two cases where the p-rank of the reduction is 1 or 2; the former uses discrete log in the reduction, the latter uses Weil pairing and discrte log in the multiplicative group.  In the sieve I restrict to primes of degree 1.  It is a Theorem (see http://eprints.nottingham.ac.uk/10052/) that this will suffice to prove p-saturation, provided that one does use reductions with p-rank 2 and not just those of p-rank 1 as originally suggested by Siksek in https://ore.exeter.ac.uk/repository/handle/10871/8323 .

I will mark this as ready for review so the bots get to work on it, and of course humans are welcome to look at the new code, but I will now test it thoroughly on the LMFDB curves and report back.



---

archive/issue_comments_081005.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-09-14T16:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81005",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081006.json:
```json
{
    "body": "Hello,\n\n1) indent correctly the INPUT and OUTPUT fields:\n\n```\nINPUT:\n\n- first thing\n  goes one there (note the shift of 2 characters)\n```\n\n\n2) use the new syntax for raise:\n\n```\nraise MyError(\"is rich\")\n```\n\n\nPoint 1 may be the source of the doc build failure found by the bot:\n\nOSError: [plane_cur] /home/patchbot/sage-patchbot/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/ell_number_field.py:docstring of sage.schemes.elliptic_curves.ell_number_field.EllipticCurve_number_field.saturation:9: WARNING: Bullet list ends without a blank line; unexpected unindent.",
    "created_at": "2015-09-14T17:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81006",
    "user": "https://github.com/fchapoton"
}
```

Hello,

1) indent correctly the INPUT and OUTPUT fields:

```
INPUT:

- first thing
  goes one there (note the shift of 2 characters)
```


2) use the new syntax for raise:

```
raise MyError("is rich")
```


Point 1 may be the source of the doc build failure found by the bot:

OSError: [plane_cur] /home/patchbot/sage-patchbot/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/ell_number_field.py:docstring of sage.schemes.elliptic_curves.ell_number_field.EllipticCurve_number_field.saturation:9: WARNING: Bullet list ends without a blank line; unexpected unindent.



---

archive/issue_comments_081007.json:
```json
{
    "body": "Replying to [comment:26 chapoton]:\n> Hello,\n> \n> 1) indent correctly the INPUT and OUTPUT fields:\n> {{{\n> INPUT:\n> \n> - first thing\n>   goes one there (note the shift of 2 characters)\n> }}}\n> \n> 2) use the new syntax for raise:\n> {{{\n> raise MyError(\"is rich\")\n> }}}\n> \n> Point 1 may be the source of the doc build failure found by the bot:\n> \n> OSError: [plane_cur] /home/patchbot/sage-patchbot/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/ell_number_field.py:docstring of sage.schemes.elliptic_curves.ell_number_field.EllipticCurve_number_field.saturation:9: WARNING: Bullet list ends without a blank line; unexpected unindent.\n\nThanks, I will fix those.",
    "created_at": "2015-09-14T18:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81007",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:26 chapoton]:
> Hello,
> 
> 1) indent correctly the INPUT and OUTPUT fields:
> {{{
> INPUT:
> 
> - first thing
>   goes one there (note the shift of 2 characters)
> }}}
> 
> 2) use the new syntax for raise:
> {{{
> raise MyError("is rich")
> }}}
> 
> Point 1 may be the source of the doc build failure found by the bot:
> 
> OSError: [plane_cur] /home/patchbot/sage-patchbot/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/ell_number_field.py:docstring of sage.schemes.elliptic_curves.ell_number_field.EllipticCurve_number_field.saturation:9: WARNING: Bullet list ends without a blank line; unexpected unindent.

Thanks, I will fix those.



---

archive/issue_comments_081008.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-09-14T19:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81008",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081009.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-09-15T09:57:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81009",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081010.json:
```json
{
    "body": "many failing doctests, see bot report",
    "created_at": "2015-09-15T09:57:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81010",
    "user": "https://github.com/fchapoton"
}
```

many failing doctests, see bot report



---

archive/issue_comments_081011.json:
```json
{
    "body": "Apologies, it was a mistake to set this to needs_review prematurely.  Next time I do, I will mean it.",
    "created_at": "2015-09-15T10:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81011",
    "user": "https://github.com/JohnCremona"
}
```

Apologies, it was a mistake to set this to needs_review prematurely.  Next time I do, I will mean it.



---

archive/issue_comments_081012.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-09-15T11:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81012",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081013.json:
```json
{
    "body": "Progress report:  I am currently running the p-saturation (for single primes) on lots of LMFDB curves and all is well so far.  This is almost always for very small p (mainly 2 and 3) though, since I am starting with some saturated points on one curve (provided by Magma) and using p-isogenies to map to other curves in the isogeny class.  Higher degree isogenies are not so common.\n\nI did start to veryify that the points from Magma were fully saturated, but ran into problems computing the saturation index, using (line 3717) the lower bound on the height of all non-torsion points -- previously implemented and merged i n6.3 (see #8828).  For example, I had a curve where the value of 5 in that line was insufficient *and led to an infinite loop in the call to min()*, while 10 worked fine, but now I have a curve where I have not yet found a value which gives anything.  For the record I will give that example here:\n\n```\nK.<phi> = NumberField(x^2-x-1) # Q(sqrt(5))\nE = EllipticCurve([phi + 1, -phi + 1, 1, 20*phi - 39, 196*phi + 237])\nH = E.height_function()\nH.min(.1,10,verbose=True) #  does not appear to terminate\n```\n\n\nStrictly this is about the code merged in #8828, but it will need fixing here before we can let this (useful!) function out into the world.",
    "created_at": "2015-09-16T11:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81013",
    "user": "https://github.com/JohnCremona"
}
```

Progress report:  I am currently running the p-saturation (for single primes) on lots of LMFDB curves and all is well so far.  This is almost always for very small p (mainly 2 and 3) though, since I am starting with some saturated points on one curve (provided by Magma) and using p-isogenies to map to other curves in the isogeny class.  Higher degree isogenies are not so common.

I did start to veryify that the points from Magma were fully saturated, but ran into problems computing the saturation index, using (line 3717) the lower bound on the height of all non-torsion points -- previously implemented and merged i n6.3 (see #8828).  For example, I had a curve where the value of 5 in that line was insufficient *and led to an infinite loop in the call to min()*, while 10 worked fine, but now I have a curve where I have not yet found a value which gives anything.  For the record I will give that example here:

```
K.<phi> = NumberField(x^2-x-1) # Q(sqrt(5))
E = EllipticCurve([phi + 1, -phi + 1, 1, 20*phi - 39, 196*phi + 237])
H = E.height_function()
H.min(.1,10,verbose=True) #  does not appear to terminate
```


Strictly this is about the code merged in #8828, but it will need fixing here before we can let this (useful!) function out into the world.



---

archive/issue_comments_081014.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-09-17T13:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81014",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081015.json:
```json
{
    "body": "The latest branch I just pushed has some merges in it which were not intended but I hope that will not cause any problems -- as well as merging 6.9.beta6 I also merged by branch 'isogs' which has been merged into beta7.\n\nOne bug fix addresses the previous comment -- after re-reading my own 2006 paper I found that the original implementer from #8828 had missed one point (when mu is halved one must increment n_max in order to guarantee termination).   A small additional improvement in the same place (the method min_gr() in height.py) now gives a small improvement in the bound, which is why one doctest there has been changed.\n\nThe second bug was to do with mutability of lists giving unwanted side effects, and is commented at the point in the source which has changed.\n\nIt is likely that users who call the saturation() method will also want to lll_reduce() the output but I have not made that automatic.\n\nI will set this to needs_review once my own full test has completed.",
    "created_at": "2015-09-17T14:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81015",
    "user": "https://github.com/JohnCremona"
}
```

The latest branch I just pushed has some merges in it which were not intended but I hope that will not cause any problems -- as well as merging 6.9.beta6 I also merged by branch 'isogs' which has been merged into beta7.

One bug fix addresses the previous comment -- after re-reading my own 2006 paper I found that the original implementer from #8828 had missed one point (when mu is halved one must increment n_max in order to guarantee termination).   A small additional improvement in the same place (the method min_gr() in height.py) now gives a small improvement in the bound, which is why one doctest there has been changed.

The second bug was to do with mutability of lists giving unwanted side effects, and is commented at the point in the source which has changed.

It is likely that users who call the saturation() method will also want to lll_reduce() the output but I have not made that automatic.

I will set this to needs_review once my own full test has completed.



---

archive/issue_comments_081016.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-09-17T14:13:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81016",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081017.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-09-19T09:00:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81017",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081018.json:
```json
{
    "body": "After further testing (on many thousands of curves but only p-saturating for small p) I saw that it was bad to use discrete_log_lambda() for the dlog in the multiplcative group (in the rarer case where the p-rank of the reduction is 2 and the Weil pairing is used), both unnecessary and less efficient than simply w.log(zeta).\nOne additional commit coming up...",
    "created_at": "2015-09-19T09:00:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81018",
    "user": "https://github.com/JohnCremona"
}
```

After further testing (on many thousands of curves but only p-saturating for small p) I saw that it was bad to use discrete_log_lambda() for the dlog in the multiplcative group (in the rarer case where the p-rank of the reduction is 2 and the Weil pairing is used), both unnecessary and less efficient than simply w.log(zeta).
One additional commit coming up...



---

archive/issue_comments_081019.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-09-19T10:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81019",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081020.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-09-19T10:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81020",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081021.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-09-25T17:09:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81021",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081022.json:
```json
{
    "body": "There's some bug in the Weil pairing section which I don't have time to fix now, and this has missed 6.9 anyway.",
    "created_at": "2015-09-25T17:09:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81022",
    "user": "https://github.com/JohnCremona"
}
```

There's some bug in the Weil pairing section which I don't have time to fix now, and this has missed 6.9 anyway.



---

archive/issue_comments_081023.json:
```json
{
    "body": "I did do more work on that but did not get to the bottom of it.  Just keeping the ticket alive!",
    "created_at": "2015-12-10T16:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81023",
    "user": "https://github.com/JohnCremona"
}
```

I did do more work on that but did not get to the bottom of it.  Just keeping the ticket alive!



---

archive/issue_comments_081024.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-12-28T13:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81024",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081025.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-01-04T15:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81025",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081026.json:
```json
{
    "body": "Merging with 7.1.beta3....",
    "created_at": "2016-02-17T13:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81026",
    "user": "https://github.com/JohnCremona"
}
```

Merging with 7.1.beta3....



---

archive/issue_comments_081027.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-02-17T16:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81027",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081028.json:
```json
{
    "body": "just rebased on 7.5.b3\n----\nNew commits:",
    "created_at": "2016-11-20T08:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81028",
    "user": "https://github.com/fchapoton"
}
```

just rebased on 7.5.b3
----
New commits:



---

archive/issue_comments_081029.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-12-11T11:36:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81029",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081030.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-06T15:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81030",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081031.json:
```json
{
    "body": "I just merged 8,0 into the branch prior to looking at it again.",
    "created_at": "2017-08-06T15:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81031",
    "user": "https://github.com/JohnCremona"
}
```

I just merged 8,0 into the branch prior to looking at it again.



---

archive/issue_comments_081032.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-06T20:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81032",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081033.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-08-06T20:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81033",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081034.json:
```json
{
    "body": "After merging into 8.0 I fixed some newly failing doctests (trivial things caused by the usual pari number field changes).  I moved the two p-saturation functions to a new file saturation.py, and added that to the reference manual.\nReady for review.  I intend to use this a lot soon over number fields of degree up to 6 for the LMFDB and it would be most helpful to have it merged into 8.1.",
    "created_at": "2017-08-06T20:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81034",
    "user": "https://github.com/JohnCremona"
}
```

After merging into 8.0 I fixed some newly failing doctests (trivial things caused by the usual pari number field changes).  I moved the two p-saturation functions to a new file saturation.py, and added that to the reference manual.
Ready for review.  I intend to use this a lot soon over number fields of degree up to 6 for the LMFDB and it would be most helpful to have it merged into 8.1.



---

archive/issue_events_021558.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2017-08-06T20:09:13Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8829#event-21558"
}
```



---

archive/issue_events_021559.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2017-08-06T20:09:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "milestone": "sage-8.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8829#event-21559"
}
```



---

archive/issue_comments_081035.json:
```json
{
    "body": "Quick comments :\n\n* dot not use $ but backticks\n\n* every function must be doctested",
    "created_at": "2017-08-06T20:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81035",
    "user": "https://github.com/fchapoton"
}
```

Quick comments :

* dot not use $ but backticks

* every function must be doctested



---

archive/issue_comments_081036.json:
```json
{
    "body": "!!! New docstrings use backticks, and new functions are doctested. !!!  The file ell_number_field is 3800 lines  long.  Both the files I just worked on have 100% coverage.",
    "created_at": "2017-08-06T20:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81036",
    "user": "https://github.com/JohnCremona"
}
```

!!! New docstrings use backticks, and new functions are doctested. !!!  The file ell_number_field is 3800 lines  long.  Both the files I just worked on have 100% coverage.



---

archive/issue_comments_081037.json:
```json
{
    "body": "Hello ! some dollars there :\n\n```\n+        For rank 1 subgroups, simply do trial divison up to the maximal\n+        prime divisor. For higher rank subgroups, perform trial divison\n+        on all linear combinations for small primes, and look for\n+        projections $E(K) \\rightarrow \\oplus E(k) \\otimes \\FF_p$ which\n+        are either full rank or provide p-divisble linear combinations,\n+        where the $k$ here are residue fields of $K$.\n```\n\nand no doc for\n\n```\n+    def projections(Q, p):\n```\n\nwhich is indeed an inner function, but quite a complicated one. Maybe just explain its input and output ?",
    "created_at": "2017-08-07T06:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81037",
    "user": "https://github.com/fchapoton"
}
```

Hello ! some dollars there :

```
+        For rank 1 subgroups, simply do trial divison up to the maximal
+        prime divisor. For higher rank subgroups, perform trial divison
+        on all linear combinations for small primes, and look for
+        projections $E(K) \rightarrow \oplus E(k) \otimes \FF_p$ which
+        are either full rank or provide p-divisble linear combinations,
+        where the $k$ here are residue fields of $K$.
```

and no doc for

```
+    def projections(Q, p):
```

which is indeed an inner function, but quite a complicated one. Maybe just explain its input and output ?



---

archive/issue_comments_081038.json:
```json
{
    "body": "I stand corrected and will see to this.",
    "created_at": "2017-08-07T08:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81038",
    "user": "https://github.com/JohnCremona"
}
```

I stand corrected and will see to this.



---

archive/issue_comments_081039.json:
```json
{
    "body": "For the inner function projections(Q, p) there is already a docstring:\n\n```\n        Project points onto (E mod Q)(K mod Q) \\otimes \\F_p.\n\n        Returns a list of 0, 1 or 2 vectors in \\F_p^n\n```\n\nwhich explains what it does.  I'll make sure that all the other inner functions are explained.",
    "created_at": "2017-08-07T08:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81039",
    "user": "https://github.com/JohnCremona"
}
```

For the inner function projections(Q, p) there is already a docstring:

```
        Project points onto (E mod Q)(K mod Q) \otimes \F_p.

        Returns a list of 0, 1 or 2 vectors in \F_p^n
```

which explains what it does.  I'll make sure that all the other inner functions are explained.



---

archive/issue_comments_081040.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-07T11:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81040",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081041.json:
```json
{
    "body": "I hope the latest commits do what was wanted for docstrings.  I did remove some rather unnecessary one-liner internal functions.\nIn the course of doing this I found at least 2 bugs ;)  which is good because the reason this was not finished with 18 months ago was the existence of a bug.\n\nPlease review!",
    "created_at": "2017-08-07T11:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81041",
    "user": "https://github.com/JohnCremona"
}
```

I hope the latest commits do what was wanted for docstrings.  I did remove some rather unnecessary one-liner internal functions.
In the course of doing this I found at least 2 bugs ;)  which is good because the reason this was not finished with 18 months ago was the existence of a bug.

Please review!



---

archive/issue_comments_081042.json:
```json
{
    "body": "a typo here:\n\n```\ntrial divison\n```\n\nand also a missing line break here after `r\"\"\"`:\n\n```\n+        r\"\"\" Given a list of rational points on `E` over `K`, compute the\n```\n\nsame here:\n\n```\n        \"\"\"Return generators for the Mordell-Weil group modulo torsion, for a\n```\n\nsame there:\n\n```\n+    r\"\"\" Checks whether the list of points is `p`-saturated.\n```\n\nand\n\n```\n+    r\"\"\" Full `p`-saturation of ``Plist``.\n```\n\n\nanother typo:\n\n```\ndivisble\n```\n\nThis :\n\n```\n+        if len(EE)==0:\n```\n\ncan be replaced by `if not EE`\n\nanother typo:\n\n```\nalgirithm\n```\n",
    "created_at": "2017-08-07T11:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81042",
    "user": "https://github.com/fchapoton"
}
```

a typo here:

```
trial divison
```

and also a missing line break here after `r"""`:

```
+        r""" Given a list of rational points on `E` over `K`, compute the
```

same here:

```
        """Return generators for the Mordell-Weil group modulo torsion, for a
```

same there:

```
+    r""" Checks whether the list of points is `p`-saturated.
```

and

```
+    r""" Full `p`-saturation of ``Plist``.
```


another typo:

```
divisble
```

This :

```
+        if len(EE)==0:
```

can be replaced by `if not EE`

another typo:

```
algirithm
```




---

archive/issue_comments_081043.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-07T12:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81043",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081044.json:
```json
{
    "body": "I fixed those, and at least one more.  Thanks",
    "created_at": "2017-08-07T12:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81044",
    "user": "https://github.com/JohnCremona"
}
```

I fixed those, and at least one more.  Thanks



---

archive/issue_comments_081045.json:
```json
{
    "body": "\"trial divison\" is still there",
    "created_at": "2017-08-07T20:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81045",
    "user": "https://github.com/fchapoton"
}
```

"trial divison" is still there



---

archive/issue_comments_081046.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-08T16:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81046",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081047.json:
```json
{
    "body": "Not now it isn't.  I also used \"grep -r\" to catch 3 more (not mine).\n\nOne day I might get a review of the __code__!",
    "created_at": "2017-08-08T16:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81047",
    "user": "https://github.com/JohnCremona"
}
```

Not now it isn't.  I also used "grep -r" to catch 3 more (not mine).

One day I might get a review of the __code__!



---

archive/issue_comments_081048.json:
```json
{
    "body": "Some comments on code:\n\n* There's something weird with the indentation at `for Q in K.primes_above(q, degree=1):` in `p_saturation` (it looks only indented one space).\n* There are various points where you don't have spaces around `==` and `+=`.  If you feel like fixing it, I think that spaces are the Python coding standard.\n* At various points you add commented out code (either verbose print statements or the definition of `pair_max`).  I'm fine with what you have, but I could also see just deleting it.  I just wanted to make sure that the decision to include it, commented out, was conscious.\n\nThere are also test failures.\n\nOther than these comments, the code looks good to me and I'm happy to give it a positive review once they're addressed.",
    "created_at": "2017-08-22T22:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81048",
    "user": "https://github.com/roed314"
}
```

Some comments on code:

* There's something weird with the indentation at `for Q in K.primes_above(q, degree=1):` in `p_saturation` (it looks only indented one space).
* There are various points where you don't have spaces around `==` and `+=`.  If you feel like fixing it, I think that spaces are the Python coding standard.
* At various points you add commented out code (either verbose print statements or the definition of `pair_max`).  I'm fine with what you have, but I could also see just deleting it.  I just wanted to make sure that the decision to include it, commented out, was conscious.

There are also test failures.

Other than these comments, the code looks good to me and I'm happy to give it a positive review once they're addressed.



---

archive/issue_comments_081049.json:
```json
{
    "body": "Also, the example from comment 5 still seems to go into an infinite loop.",
    "created_at": "2017-08-23T00:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81049",
    "user": "https://github.com/kedlaya"
}
```

Also, the example from comment 5 still seems to go into an infinite loop.



---

archive/issue_comments_081050.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-08-23T08:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81050",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081051.json:
```json
{
    "body": "Thanks to both for the reviews.  I'll look into the spacing issues and the example.  I really really want to get finished with this!",
    "created_at": "2017-08-23T08:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81051",
    "user": "https://github.com/JohnCremona"
}
```

Thanks to both for the reviews.  I'll look into the spacing issues and the example.  I really really want to get finished with this!



---

archive/issue_comments_081052.json:
```json
{
    "body": "I first merged in the current develop (and fixed one small conflict).  this required a rebuild (i.e. 'make' not just './sage -b' which failed).\n\nI fixed that indentation issue -- logically correct but of course non-standard to have just one space of indentation.  I hope the result is OK, that indented block was very long and had a lot of subsidiary indented parts.\n\nI have fixed all (I hope) the == and += spacing.\n\nI changed some commented-out debugging print statements into comments.  I like having lots of comments since the logic is quite complicated (and if further bugs are found it may well be me who has to fix them so I might as well be helpful).\n\nI'll test the example from comment 5 once the rebuild has finished.",
    "created_at": "2017-08-23T08:59:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81052",
    "user": "https://github.com/JohnCremona"
}
```

I first merged in the current develop (and fixed one small conflict).  this required a rebuild (i.e. 'make' not just './sage -b' which failed).

I fixed that indentation issue -- logically correct but of course non-standard to have just one space of indentation.  I hope the result is OK, that indented block was very long and had a lot of subsidiary indented parts.

I have fixed all (I hope) the == and += spacing.

I changed some commented-out debugging print statements into comments.  I like having lots of comments since the logic is quite complicated (and if further bugs are found it may well be me who has to fix them so I might as well be helpful).

I'll test the example from comment 5 once the rebuild has finished.



---

archive/issue_comments_081053.json:
```json
{
    "body": "Dammit, I always use trac branch names of the form u/cremona/nnnnn where nnnnn is the ticket number, but at some point the branch here became public/8829, so I have just been fixing the wrong version.  What a waste of time.  Back soon.",
    "created_at": "2017-08-23T11:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81053",
    "user": "https://github.com/JohnCremona"
}
```

Dammit, I always use trac branch names of the form u/cremona/nnnnn where nnnnn is the ticket number, but at some point the branch here became public/8829, so I have just been fixing the wrong version.  What a waste of time.  Back soon.



---

archive/issue_comments_081054.json:
```json
{
    "body": "New commits:",
    "created_at": "2017-08-23T11:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81054",
    "user": "https://github.com/JohnCremona"
}
```

New commits:



---

archive/issue_comments_081055.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-08-23T11:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81055",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081056.json:
```json
{
    "body": "OK, back to review.  Note that the branch is now u/cremona/8829.",
    "created_at": "2017-08-23T11:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81056",
    "user": "https://github.com/JohnCremona"
}
```

OK, back to review.  Note that the branch is now u/cremona/8829.



---

archive/issue_comments_081057.json:
```json
{
    "body": "\"trial divison\" is back, and probably all the other fixes went away.... Sorry for nitpicking, really..",
    "created_at": "2017-08-23T11:51:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81057",
    "user": "https://github.com/fchapoton"
}
```

"trial divison" is back, and probably all the other fixes went away.... Sorry for nitpicking, really..



---

archive/issue_comments_081058.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-08-23T12:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81058",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081059.json:
```json
{
    "body": "!`@`$#!.  OK, I will check out commit d242123 by hash to be sure that is what was most recently reviewed, and redo the work I did before.  It's the only way to be certain.",
    "created_at": "2017-08-23T12:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81059",
    "user": "https://github.com/JohnCremona"
}
```

!`@`$#!.  OK, I will check out commit d242123 by hash to be sure that is what was most recently reviewed, and redo the work I did before.  It's the only way to be certain.



---

archive/issue_comments_081060.json:
```json
{
    "body": "I hope I got it right this time.  The correct branch is public/8829 and I basically redid the edits I had already done this morning on the wrong branch.\n----\nLast 10 new commits:",
    "created_at": "2017-08-23T14:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81060",
    "user": "https://github.com/JohnCremona"
}
```

I hope I got it right this time.  The correct branch is public/8829 and I basically redid the edits I had already done this morning on the wrong branch.
----
Last 10 new commits:



---

archive/issue_comments_081061.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-08-23T14:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81061",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081062.json:
```json
{
    "body": "It looks like you've addressed everything.  I ran all tests and checked that the loop in comment 5 is no longer a problem.",
    "created_at": "2017-08-23T15:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81062",
    "user": "https://github.com/roed314"
}
```

It looks like you've addressed everything.  I ran all tests and checked that the loop in comment 5 is no longer a problem.



---

archive/issue_comments_081063.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-08-23T15:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81063",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081064.json:
```json
{
    "body": "Thanks a lot!  This ticket was opened in 2010, so I'll be celebrating.  Now, if any of you would like to head on over to #22345...",
    "created_at": "2017-08-23T15:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81064",
    "user": "https://github.com/JohnCremona"
}
```

Thanks a lot!  This ticket was opened in 2010, so I'll be celebrating.  Now, if any of you would like to head on over to #22345...



---

archive/issue_comments_081065.json:
```json
{
    "body": "Very well, and I share your joy, but you introduced a .next(), which is not compatible with python3 (see patchbot plugin report). To be fixed in a later ticket, please.",
    "created_at": "2017-08-23T18:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81065",
    "user": "https://github.com/fchapoton"
}
```

Very well, and I share your joy, but you introduced a .next(), which is not compatible with python3 (see patchbot plugin report). To be fixed in a later ticket, please.



---

archive/issue_comments_081066.json:
```json
{
    "body": "That's a pity I thought the next () was rather neat. You can fix it here if you want.",
    "created_at": "2017-08-23T18:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81066",
    "user": "https://github.com/JohnCremona"
}
```

That's a pity I thought the next () was rather neat. You can fix it here if you want.



---

archive/issue_comments_081067.json:
```json
{
    "body": "no, no, let us wait and do that later",
    "created_at": "2017-08-23T18:40:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81067",
    "user": "https://github.com/fchapoton"
}
```

no, no, let us wait and do that later



---

archive/issue_comments_081068.json:
```json
{
    "body": "By the way, John, could you tell LMFDB people about #23671, please ?",
    "created_at": "2017-08-23T18:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81068",
    "user": "https://github.com/fchapoton"
}
```

By the way, John, could you tell LMFDB people about #23671, please ?



---

archive/issue_comments_081069.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2017-08-23T20:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81069",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_081070.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:",
    "created_at": "2017-08-23T20:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81070",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:



---

archive/issue_comments_081071.json:
```json
{
    "body": "Replying to [comment:80 chapoton]:\n> no, no, let us wait and do that later\n\nIsn't it just this one-line change? If so, no reason to postpone it...",
    "created_at": "2017-08-23T20:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81071",
    "user": "https://github.com/kedlaya"
}
```

Replying to [comment:80 chapoton]:
> no, no, let us wait and do that later

Isn't it just this one-line change? If so, no reason to postpone it...



---

archive/issue_comments_081072.json:
```json
{
    "body": "Looks good to me!",
    "created_at": "2017-08-23T22:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81072",
    "user": "https://github.com/roed314"
}
```

Looks good to me!



---

archive/issue_comments_081073.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-08-23T22:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81073",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081074.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-08-29T19:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81074",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_021560.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2017-08-29T19:51:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8829#event-21560"
}
```



---

archive/issue_comments_081075.json:
```json
{
    "body": "This is causing doctest failures: #23840.",
    "created_at": "2017-09-12T14:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81075",
    "user": "https://github.com/jdemeyer"
}
```

This is causing doctest failures: #23840.



---

archive/issue_comments_081076.json:
```json
{
    "body": "I'm pretty certain it will be the usual nonsense of mathematically equivalent outputs.  I'll look at #23840 and judge properly.",
    "created_at": "2017-09-12T14:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8829#issuecomment-81076",
    "user": "https://github.com/JohnCremona"
}
```

I'm pretty certain it will be the usual nonsense of mathematically equivalent outputs.  I'll look at #23840 and judge properly.
