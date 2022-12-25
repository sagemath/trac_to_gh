# Issue 5153: bug in simon_two_descent  for elliptic curves

archive/issues_005153.json:
```json
{
    "body": "Assignee: @williamstein\n\nWe have\n\n```\nsage: E = EllipticCurve('65a1')\nsage: G = E.change_ring(QuadraticField(-56,'a'))\nsage: G.simon_two_descent()\n(3, 4, [(-9/4 : -3/8*a + 9/8 : 1), (-8/7 : -1/49*a + 4/7 : 1), (1 : 0 : 1), \n  (-6/25*a - 47/25 : 36/125*a - 368/125 : 1), (1/4 : 1/16*a - 1/8 : 1)])\n```\n\n\nThe documentation for simon_two_descent says that the output of Simon 2-descent is\n\n```\n        OUTPUT:\n            integer -- \"probably\" the rank of self\n            integer -- the 2-rank of the Selmer group\n            list    -- list of independent points on the curve.\n```\n\n\nOur curve does have rank 3, but the output list above contains *five* points, so they can't be independent!   \n\nOur curve has torsion of order 2, so E(K)/2 E(K) has rank four, so the 3 and four output by Simon descent are right.  The only problem is the list, which has too many points in it. \n\nMaybe this is simply a documentation issue, and the docs for simon_two_descent should be changed to say that list is a list of points that *generate* a subgroup of the MW group of rank r, where r is the first number output by simon_two_descent.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5153\n\n",
    "created_at": "2009-02-01T22:24:47Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.1",
    "title": "bug in simon_two_descent  for elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5153",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

We have

```
sage: E = EllipticCurve('65a1')
sage: G = E.change_ring(QuadraticField(-56,'a'))
sage: G.simon_two_descent()
(3, 4, [(-9/4 : -3/8*a + 9/8 : 1), (-8/7 : -1/49*a + 4/7 : 1), (1 : 0 : 1), 
  (-6/25*a - 47/25 : 36/125*a - 368/125 : 1), (1/4 : 1/16*a - 1/8 : 1)])
```


The documentation for simon_two_descent says that the output of Simon 2-descent is

```
        OUTPUT:
            integer -- "probably" the rank of self
            integer -- the 2-rank of the Selmer group
            list    -- list of independent points on the curve.
```


Our curve does have rank 3, but the output list above contains *five* points, so they can't be independent!   

Our curve has torsion of order 2, so E(K)/2 E(K) has rank four, so the 3 and four output by Simon descent are right.  The only problem is the list, which has too many points in it. 

Maybe this is simply a documentation issue, and the docs for simon_two_descent should be changed to say that list is a list of points that *generate* a subgroup of the MW group of rank r, where r is the first number output by simon_two_descent.

Issue created by migration from https://trac.sagemath.org/ticket/5153





---

archive/issue_comments_039348.json:
```json
{
    "body": "I will email Denis Simon about this, since he has just done another bug fix in ell.gp after I reported a bug to him.  Unfortunately the fix he sent works in the latest pari but not with the one Sage uses.",
    "created_at": "2009-06-09T11:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39348",
    "user": "https://github.com/JohnCremona"
}
```

I will email Denis Simon about this, since he has just done another bug fix in ell.gp after I reported a bug to him.  Unfortunately the fix he sent works in the latest pari but not with the one Sage uses.



---

archive/issue_comments_039349.json:
```json
{
    "body": "Looking at the example in more detail, I see that the points returned do generate a rank 3 group (though I had to use Magma to check the independence), so there are two problems: (1) the points in the list are not independent (even in E(K)/2E(K)) and (2) the numbers 3,4 which are supposed to be lower and upper bounds on the rank are wrong and should be 3,3.\n\nI know how the first happens (since it is doing a descent via 2-isogeny).\n\nThis will be possible to fix once I (or someone) have eventually implemented heights of points over number fields, as I promised to do  in trac #360 !",
    "created_at": "2009-06-09T12:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39349",
    "user": "https://github.com/JohnCremona"
}
```

Looking at the example in more detail, I see that the points returned do generate a rank 3 group (though I had to use Magma to check the independence), so there are two problems: (1) the points in the list are not independent (even in E(K)/2E(K)) and (2) the numbers 3,4 which are supposed to be lower and upper bounds on the rank are wrong and should be 3,3.

I know how the first happens (since it is doing a descent via 2-isogeny).

This will be possible to fix once I (or someone) have eventually implemented heights of points over number fields, as I promised to do  in trac #360 !



---

archive/issue_comments_039350.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T19:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39350",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_039351.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T19:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39351",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_039352.json:
```json
{
    "body": "Remove assignee @loefflerd.",
    "created_at": "2009-10-09T09:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39352",
    "user": "https://github.com/loefflerd"
}
```

Remove assignee @loefflerd.



---

archive/issue_comments_039353.json:
```json
{
    "body": "Replying to [comment:2 cremona]:\n> This will be possible to fix once I (or someone) have eventually implemented heights of points over number fields, as I promised to do  in trac #360 !\n\nI am not sure that using heights is the best way to get independence if you are doing a 2-descent anyway. The easier thing to do would be to just report back a set of points that minimally generate the 2-selmer group (or at least minimally generate the part of the 2-selmer group generated by the found points)\nThe only thing you'd miss that way would be if one finds generators for an even index 2 subgroup of the full Mordell-Weil group. I think it's highly unlikely that that would happen.",
    "created_at": "2010-01-17T01:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39353",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:2 cremona]:
> This will be possible to fix once I (or someone) have eventually implemented heights of points over number fields, as I promised to do  in trac #360 !

I am not sure that using heights is the best way to get independence if you are doing a 2-descent anyway. The easier thing to do would be to just report back a set of points that minimally generate the 2-selmer group (or at least minimally generate the part of the 2-selmer group generated by the found points)
The only thing you'd miss that way would be if one finds generators for an even index 2 subgroup of the full Mordell-Weil group. I think it's highly unlikely that that would happen.



---

archive/issue_comments_039354.json:
```json
{
    "body": "> I am not sure that using heights is the best way to get independence\n\nAnother excellent trick I learned from Cremona for getting independence is to use *homomorphic images*.  I.e., reduce to a direct sum of groups of points over a finite field (all tensored with F_p, with p coprime to torsion).  Then the rank of the group you have is a bounded below by the dimension of the image.",
    "created_at": "2010-01-17T05:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39354",
    "user": "https://github.com/williamstein"
}
```

> I am not sure that using heights is the best way to get independence

Another excellent trick I learned from Cremona for getting independence is to use *homomorphic images*.  I.e., reduce to a direct sum of groups of points over a finite field (all tensored with F_p, with p coprime to torsion).  Then the rank of the group you have is a bounded below by the dimension of the image.



---

archive/issue_comments_039355.json:
```json
{
    "body": "Good point -- the reference is On the computation of Mordell-Weil and 2-Selmer Groups of Elliptic Curves. Rocky Mountain Journal of Mathematics (2002) vol. 32, no. 3, pp.953--967.   This is implemeneted over Q in eclib, and it would be possible to do an implementation over number fields.  As Mestre points out, this method for testing independence has the great advantage that it does not depend on precision of height computations, only on linear algebra over F_2.",
    "created_at": "2010-01-17T11:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39355",
    "user": "https://github.com/JohnCremona"
}
```

Good point -- the reference is On the computation of Mordell-Weil and 2-Selmer Groups of Elliptic Curves. Rocky Mountain Journal of Mathematics (2002) vol. 32, no. 3, pp.953--967.   This is implemeneted over Q in eclib, and it would be possible to do an implementation over number fields.  As Mestre points out, this method for testing independence has the great advantage that it does not depend on precision of height computations, only on linear algebra over F_2.



---

archive/issue_comments_039356.json:
```json
{
    "body": "Replying to [comment:6 was]:\n> Another excellent trick I learned from Cremona for getting independence is to use *homomorphic images*.  I.e., reduce to a direct sum of groups of points over a finite field (all tensored with F_p, with p coprime to torsion).  Then the rank of the group you have is a bounded below by the dimension of the image. \n\nAnd those same images can also yield information on p-saturation of the group generated by the given points inside the Mordell-Weil group\n(just as an independence proof via 2-Selmer groups also gives 2-saturation)\nThis starts to sound like a nice student project.",
    "created_at": "2010-01-24T03:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39356",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:6 was]:
> Another excellent trick I learned from Cremona for getting independence is to use *homomorphic images*.  I.e., reduce to a direct sum of groups of points over a finite field (all tensored with F_p, with p coprime to torsion).  Then the rank of the group you have is a bounded below by the dimension of the image. 

And those same images can also yield information on p-saturation of the group generated by the given points inside the Mordell-Weil group
(just as an independence proof via 2-Selmer groups also gives 2-saturation)
This starts to sound like a nice student project.



---

archive/issue_comments_039357.json:
```json
{
    "body": "Replying to [comment:8 nbruin]:\n> Replying to [comment:6 was]:\n> > Another excellent trick I learned from Cremona for getting independence is to use *homomorphic images*.  I.e., reduce to a direct sum of groups of points over a finite field (all tensored with F_p, with p coprime to torsion).  Then the rank of the group you have is a bounded below by the dimension of the image. \n> \n> And those same images can also yield information on p-saturation of the group generated by the given points inside the Mordell-Weil group\n> (just as an independence proof via 2-Selmer groups also gives 2-saturation)\n> This starts to sound like a nice student project.\nIt was!  The thesis of my student Martin Prickett was about saturating Mordell-Weil groups this way, and he implemented it in Magma.  See http://www.warwick.ac.uk/staff/J.E.Cremona/theses/index.html .  I have Martin's magma code but it is not easy to use.  Hence the project still remains, namely to rewrite all that.",
    "created_at": "2010-01-24T12:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39357",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:8 nbruin]:
> Replying to [comment:6 was]:
> > Another excellent trick I learned from Cremona for getting independence is to use *homomorphic images*.  I.e., reduce to a direct sum of groups of points over a finite field (all tensored with F_p, with p coprime to torsion).  Then the rank of the group you have is a bounded below by the dimension of the image. 
> 
> And those same images can also yield information on p-saturation of the group generated by the given points inside the Mordell-Weil group
> (just as an independence proof via 2-Selmer groups also gives 2-saturation)
> This starts to sound like a nice student project.
It was!  The thesis of my student Martin Prickett was about saturating Mordell-Weil groups this way, and he implemented it in Magma.  See http://www.warwick.ac.uk/staff/J.E.Cremona/theses/index.html .  I have Martin's magma code but it is not easy to use.  Hence the project still remains, namely to rewrite all that.



---

archive/issue_comments_039358.json:
```json
{
    "body": "> the numbers 3,4 which are supposed to be lower and upper bounds on the rank are wrong and\n> should be 3,3.\n\nThe numbers 3,4, are correct. G has a point of order 2 over its base feild, so the 2-rank of the 2-Selmer group is 4. However, an error like the one you're describing does occur with 438e1 over Q.",
    "created_at": "2010-03-28T03:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39358",
    "user": "https://trac.sagemath.org/admin/accounts/users/weigandt"
}
```

> the numbers 3,4 which are supposed to be lower and upper bounds on the rank are wrong and
> should be 3,3.

The numbers 3,4, are correct. G has a point of order 2 over its base feild, so the 2-rank of the 2-Selmer group is 4. However, an error like the one you're describing does occur with 438e1 over Q.



---

archive/issue_comments_039359.json:
```json
{
    "body": "Replying to [comment:10 weigandt]:\n> > the numbers 3,4 which are supposed to be lower and upper bounds on the rank are wrong and\n> > should be 3,3.\n> \n> The numbers 3,4, are correct. G has a point of order 2 over its base feild, so the 2-rank of the 2-Selmer group is 4. However, an error like the one you're describing does occur with 438e1 over Q.\n\nDo you mean 438e1 over Q?    #torsion=2 and rank=0 but the first descent via 2-isogeny gives a rank upper bound of 2.  If the rank were 2 then the 2-selmer rank would be 3.  two_descent_simon() gives lower bound of 0 and 3 for the rank of the 2-Selmer group.  That last one is clearly wrong.  I think it is similar to the problem my 2-descent used to have:  Simon does not do a second descent, so het gets the uppoer bound of 3 on the rank (not wrong!) but incorrectly calls it the 2-Selmer rank.\n\nWe should correct the docstring of two_descent_simon, and I will tell Simon that his documentation is incorrect.",
    "created_at": "2010-03-31T12:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39359",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:10 weigandt]:
> > the numbers 3,4 which are supposed to be lower and upper bounds on the rank are wrong and
> > should be 3,3.
> 
> The numbers 3,4, are correct. G has a point of order 2 over its base feild, so the 2-rank of the 2-Selmer group is 4. However, an error like the one you're describing does occur with 438e1 over Q.

Do you mean 438e1 over Q?    #torsion=2 and rank=0 but the first descent via 2-isogeny gives a rank upper bound of 2.  If the rank were 2 then the 2-selmer rank would be 3.  two_descent_simon() gives lower bound of 0 and 3 for the rank of the 2-Selmer group.  That last one is clearly wrong.  I think it is similar to the problem my 2-descent used to have:  Simon does not do a second descent, so het gets the uppoer bound of 3 on the rank (not wrong!) but incorrectly calls it the 2-Selmer rank.

We should correct the docstring of two_descent_simon, and I will tell Simon that his documentation is incorrect.



---

archive/issue_comments_039360.json:
```json
{
    "body": "See #6955 for the updating of Simon's scripts, which I am now testing.",
    "created_at": "2010-04-03T16:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39360",
    "user": "https://github.com/JohnCremona"
}
```

See #6955 for the updating of Simon's scripts, which I am now testing.



---

archive/issue_comments_039361.json:
```json
{
    "body": "Update 15/7/10:  I did tell Simon that his script's documentation is misleading, and he agreed.  But last time I checked he had not changed them.",
    "created_at": "2010-07-15T08:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39361",
    "user": "https://github.com/JohnCremona"
}
```

Update 15/7/10:  I did tell Simon that his script's documentation is misleading, and he agreed.  But last time I checked he had not changed them.



---

archive/issue_comments_039362.json:
```json
{
    "body": "Changing keywords from \"\" to \"simon_two_descent\".",
    "created_at": "2013-09-21T12:27:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39362",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "simon_two_descent".



---

archive/issue_comments_039363.json:
```json
{
    "body": "The actual issue reported to fix here, seemed first to me just a question of rewording the documentation. But then I realised that there is a bug, quite hidden, but unpleasant, linked to ticket #11372.\n\nSo we want simon_two_descent (over the rationals of number fields) to return three things\n\n* A proven lower bound for the rank\n* The rank of the 2-Selmer group (this is an upper bound but not sharp in general)\n* A list of points.\n\nI propose that the list of points is a list of points of infinite order. So I filter out the ones that are of order 2 in the list that the script returns. However they are not lin. indep. This was already done over number fields in #13593. So here I modify the function over rationals.\n\nOver Q, this function then also saturates these points and, if there are sufficiently many, sets them for `E.gens()`.\n\nThat is what my proposed changes in the forthcoming commit will do. \n\nNow, there are related issues, but they don't belong to this ticket really. The curve 438e1 gives the wrong 2-Selmer and that is #10735. The fact that we don't saturate over number field should not belong to this ticket. One should open a new one for this. Also the script is outdated (see #11005) and has plenty of other issues (#11041).\n\nThe bug introduced by #11372: In the example in the documentation, the only point found is of order 2, while the second descent concludes that the rank is 1. The result shown in the documentation were in fact from mwrank not from simon_two_descent.",
    "created_at": "2013-12-28T16:29:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39363",
    "user": "https://github.com/categorie"
}
```

The actual issue reported to fix here, seemed first to me just a question of rewording the documentation. But then I realised that there is a bug, quite hidden, but unpleasant, linked to ticket #11372.

So we want simon_two_descent (over the rationals of number fields) to return three things

* A proven lower bound for the rank
* The rank of the 2-Selmer group (this is an upper bound but not sharp in general)
* A list of points.

I propose that the list of points is a list of points of infinite order. So I filter out the ones that are of order 2 in the list that the script returns. However they are not lin. indep. This was already done over number fields in #13593. So here I modify the function over rationals.

Over Q, this function then also saturates these points and, if there are sufficiently many, sets them for `E.gens()`.

That is what my proposed changes in the forthcoming commit will do. 

Now, there are related issues, but they don't belong to this ticket really. The curve 438e1 gives the wrong 2-Selmer and that is #10735. The fact that we don't saturate over number field should not belong to this ticket. One should open a new one for this. Also the script is outdated (see #11005) and has plenty of other issues (#11041).

The bug introduced by #11372: In the example in the documentation, the only point found is of order 2, while the second descent concludes that the rank is 1. The result shown in the documentation were in fact from mwrank not from simon_two_descent.



---

archive/issue_comments_039364.json:
```json
{
    "body": "New commits:",
    "created_at": "2013-12-28T16:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39364",
    "user": "https://github.com/categorie"
}
```

New commits:



---

archive/issue_comments_039365.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-12-28T16:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39365",
    "user": "https://github.com/categorie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039366.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2013-12-28T17:56:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39366",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_039367.json:
```json
{
    "body": "I am worried by the documentation sentence\n\n```\nTo obtain a list of generators, use E.gens() after this.\n```\n\nsince the only situation in which `E.gens()` with return points found by this function are when the lower and upper rank bounds agree *and* the list of points returned has that number of points in it.  Otherwise, gens are not cached and a call to E.gens() will use `mwrank`.  So it is a bit misleading?",
    "created_at": "2013-12-30T17:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39367",
    "user": "https://github.com/JohnCremona"
}
```

I am worried by the documentation sentence

```
To obtain a list of generators, use E.gens() after this.
```

since the only situation in which `E.gens()` with return points found by this function are when the lower and upper rank bounds agree *and* the list of points returned has that number of points in it.  Otherwise, gens are not cached and a call to E.gens() will use `mwrank`.  So it is a bit misleading?



---

archive/issue_comments_039368.json:
```json
{
    "body": "I meant this as an advice to the standard user that does not care how this is done, but wants the generators. \nMaybe the \"after this\" is confusing. Or we could add more about what happens at the back, but ?? would tell them that too.",
    "created_at": "2013-12-30T17:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39368",
    "user": "https://github.com/categorie"
}
```

I meant this as an advice to the standard user that does not care how this is done, but wants the generators. 
Maybe the "after this" is confusing. Or we could add more about what happens at the back, but ?? would tell them that too.



---

archive/issue_comments_039369.json:
```json
{
    "body": "I suggest just deleting \"after this\".  We can revisit this once we have put in independence-checking over number fields (which is separate from and rather easier than saturating).  If you do that, I'll give it a positive review!",
    "created_at": "2013-12-30T17:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39369",
    "user": "https://github.com/JohnCremona"
}
```

I suggest just deleting "after this".  We can revisit this once we have put in independence-checking over number fields (which is separate from and rather easier than saturating).  If you do that, I'll give it a positive review!



---

archive/issue_comments_039370.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2013-12-30T19:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39370",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_039371.json:
```json
{
    "body": "Done.",
    "created_at": "2013-12-30T19:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39371",
    "user": "https://github.com/categorie"
}
```

Done.



---

archive/issue_comments_039372.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-12-30T19:58:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39372",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_039373.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-01-05T02:56:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5153#issuecomment-39373",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
