# Issue 7401: Derivative at a point is not translated into Maxima

archive/issues_007401.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @eviatarbach\n\nKeywords: derivative, at, maxima\n\nAlex reported [http://groups.google.cz/group/sage-support/browse_thread/thread/81b96a7731600ec2](http://groups.google.cz/group/sage-support/browse_thread/thread/81b96a7731600ec2) this bug (see the link for short discussion related to the problem)\n\n```\nHi all:\n\nI found some strange behavior in solve that's related to function\ncomposition.  Check out this short example.\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: var('x,t')\n(x, t)\nsage: f= function('f',x)\nsage: e= {x:exp(t)}\nsage: ft= f.subs(e); ft\nf(e^t)\nsage: Ft = t^2 + ft^2; Ft\nt^2 + f(e^t)^2\nsage: a= diff(Ft,t); a\n2*e^t*f(e^t)*D[0](f)(e^t) + 2*t\nsage: solve(a==0,diff(f,x).subs(e))\n[D[0](f)(t) == -t*e^(-t)/f(e^t)]\n| Sage Version 4.2, Release Date: 2009-10-24                         |\n| Type notebook() for the GUI, and license() for information.        |\nDid you spot the strangeness?  Somehow diff(f,x).subs(e) became diff\n(f,x).subs({x:t}) after solving.  Does anybody know how to fix this?\n\nAlex \n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7401\n\n",
    "created_at": "2009-11-06T10:53:17Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.5",
    "title": "Derivative at a point is not translated into Maxima",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7401",
    "user": "https://github.com/robert-marik"
}
```
Assignee: @williamstein

CC:  @eviatarbach

Keywords: derivative, at, maxima

Alex reported [http://groups.google.cz/group/sage-support/browse_thread/thread/81b96a7731600ec2](http://groups.google.cz/group/sage-support/browse_thread/thread/81b96a7731600ec2) this bug (see the link for short discussion related to the problem)

```
Hi all:

I found some strange behavior in solve that's related to function
composition.  Check out this short example.

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: var('x,t')
(x, t)
sage: f= function('f',x)
sage: e= {x:exp(t)}
sage: ft= f.subs(e); ft
f(e^t)
sage: Ft = t^2 + ft^2; Ft
t^2 + f(e^t)^2
sage: a= diff(Ft,t); a
2*e^t*f(e^t)*D[0](f)(e^t) + 2*t
sage: solve(a==0,diff(f,x).subs(e))
[D[0](f)(t) == -t*e^(-t)/f(e^t)]
| Sage Version 4.2, Release Date: 2009-10-24                         |
| Type notebook() for the GUI, and license() for information.        |
Did you spot the strangeness?  Somehow diff(f,x).subs(e) became diff
(f,x).subs({x:t}) after solving.  Does anybody know how to fix this?

Alex 

```


Issue created by migration from https://trac.sagemath.org/ticket/7401





---

archive/issue_comments_062128.json:
```json
{
    "body": "Attachment [trac_7401_marik_initial.patch](tarball://root/attachments/some-uuid/ticket7401/trac_7401_marik_initial.patch) by @robert-marik created at 2009-11-06 10:56:42\n\napply together with the patch for #385 (if necessary)",
    "created_at": "2009-11-06T10:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62128",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac_7401_marik_initial.patch](tarball://root/attachments/some-uuid/ticket7401/trac_7401_marik_initial.patch) by @robert-marik created at 2009-11-06 10:56:42

apply together with the patch for #385 (if necessary)



---

archive/issue_comments_062129.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-06T10:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62129",
    "user": "https://github.com/robert-marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062130.json:
```json
{
    "body": "Submitted patch solves the problem described above\n\nlimitation and disadvantage of this patch are:\n\n* it works for univariable functions only\n\n* introduces new dummy variable into Maxima session\n\nAll comments are welcomed and any help appretiated",
    "created_at": "2009-11-06T10:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62130",
    "user": "https://github.com/robert-marik"
}
```

Submitted patch solves the problem described above

limitation and disadvantage of this patch are:

* it works for univariable functions only

* introduces new dummy variable into Maxima session

All comments are welcomed and any help appretiated



---

archive/issue_comments_062131.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-10T15:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62131",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062132.json:
```json
{
    "body": "Replying to [comment:1 robert.marik]:\n> Submitted patch solves the problem described above\n> \n\nYes, this should do so.  It would probably be best to add one more doctest, just to show that the original one works (i.e. without showing the Maxima internals). \n\n> limitation and disadvantage of this patch are:\n> \n> * it works for univariable functions only\n\nThat's fine - that's still improving the previous situation, correct?  Looking at the code, it would be helpful to know what happens if params has more than one element - particularly in \n\n```\nreturn \"at(diff('%s(dummy_var_der), %s),dummy_var_der=%s)\"%(f.name(), \", \".join(params), opnds[0]) \n```\n\nit seems like one could have more items in the substitution tuple than there are %s to fill up, even if for some reason len(args)==1.  What is the relation between args and params - could there be more params than args?\n\nAlso, make sure to add a doctest showing that the NotImplementedError comes into play.  Search for 'Traceback' in the file to see how the doctests for errors look.\n\n> \n> * introduces new dummy variable into Maxima session\n\nThis is unfortunate, but probably unavoidable currently.  You should test whether this breaks anything in Maxima, but I don't see why it would.",
    "created_at": "2009-11-10T15:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62132",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:1 robert.marik]:
> Submitted patch solves the problem described above
> 

Yes, this should do so.  It would probably be best to add one more doctest, just to show that the original one works (i.e. without showing the Maxima internals). 

> limitation and disadvantage of this patch are:
> 
> * it works for univariable functions only

That's fine - that's still improving the previous situation, correct?  Looking at the code, it would be helpful to know what happens if params has more than one element - particularly in 

```
return "at(diff('%s(dummy_var_der), %s),dummy_var_der=%s)"%(f.name(), ", ".join(params), opnds[0]) 
```

it seems like one could have more items in the substitution tuple than there are %s to fill up, even if for some reason len(args)==1.  What is the relation between args and params - could there be more params than args?

Also, make sure to add a doctest showing that the NotImplementedError comes into play.  Search for 'Traceback' in the file to see how the doctests for errors look.

> 
> * introduces new dummy variable into Maxima session

This is unfortunate, but probably unavoidable currently.  You should test whether this breaks anything in Maxima, but I don't see why it would.



---

archive/issue_comments_062133.json:
```json
{
    "body": "Also, there needs to be a blank line after \"TESTS::\" for documentation formatting.",
    "created_at": "2009-11-10T16:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62133",
    "user": "https://github.com/jasongrout"
}
```

Also, there needs to be a blank line after "TESTS::" for documentation formatting.



---

archive/issue_comments_062134.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> This is unfortunate, but probably unavoidable currently.  You should test whether this breaks anything in Maxima, but I don't see why it would.\n\n\nPerhaps we can use variable from f.variables() instead of introducing dummy variable.",
    "created_at": "2009-11-12T14:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62134",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:2 kcrisman]:
> This is unfortunate, but probably unavoidable currently.  You should test whether this breaks anything in Maxima, but I don't see why it would.


Perhaps we can use variable from f.variables() instead of introducing dummy variable.



---

archive/issue_comments_062135.json:
```json
{
    "body": "Why not see if that works, then update the patch?  One might have to be careful in testing for how many variables/args there are.  I am never clear on the difference between those two things, anyway, in Sage.",
    "created_at": "2009-11-12T15:48:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62135",
    "user": "https://github.com/kcrisman"
}
```

Why not see if that works, then update the patch?  One might have to be careful in testing for how many variables/args there are.  I am never clear on the difference between those two things, anyway, in Sage.



---

archive/issue_comments_062136.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> Why not see if that works, then update the patch?  One might have to be careful in testing for how many variables/args there are.  I am never clear on the difference between those two things, anyway, in Sage.\n\nMy suggestion related to f.variables() does not work, since I cannot acces the variables inside the function derivative. \n\nThe original patch does not work for something like diff(f(x,y),x).subs(x=3) so I updated it and tested for various combination how many variables are in the function, how many variables appear at the resulting expression, how many variables are substituted etc.\n\nPerhaps could be improved for multivariable functions, but Maxima expression \"at (expr, [eqn_1, ..., eqn_n])\" cannot be translated to current Sage and both issues should be fixed together. Perhaps in this ticket? (leaving as needs_work, despite the fact that the original problem has been fixed and doctested)",
    "created_at": "2009-11-13T12:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62136",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:5 kcrisman]:
> Why not see if that works, then update the patch?  One might have to be careful in testing for how many variables/args there are.  I am never clear on the difference between those two things, anyway, in Sage.

My suggestion related to f.variables() does not work, since I cannot acces the variables inside the function derivative. 

The original patch does not work for something like diff(f(x,y),x).subs(x=3) so I updated it and tested for various combination how many variables are in the function, how many variables appear at the resulting expression, how many variables are substituted etc.

Perhaps could be improved for multivariable functions, but Maxima expression "at (expr, [eqn_1, ..., eqn_n])" cannot be translated to current Sage and both issues should be fixed together. Perhaps in this ticket? (leaving as needs_work, despite the fact that the original problem has been fixed and doctested)



---

archive/issue_comments_062137.json:
```json
{
    "body": "Attachment [trac-7401-revision-1.patch](tarball://root/attachments/some-uuid/ticket7401/trac-7401-revision-1.patch) by @robert-marik created at 2009-11-13 12:33:10\n\nApply only this patch.",
    "created_at": "2009-11-13T12:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62137",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac-7401-revision-1.patch](tarball://root/attachments/some-uuid/ticket7401/trac-7401-revision-1.patch) by @robert-marik created at 2009-11-13 12:33:10

Apply only this patch.



---

archive/issue_comments_062138.json:
```json
{
    "body": "> Perhaps could be improved for multivariable functions, but Maxima expression \"at (expr, [eqn_1, ..., eqn_n])\" cannot be translated to current Sage and both issues should be fixed together. Perhaps in this ticket? (leaving as needs_work, despite the fact that the original problem has been fixed and doctested)\n\nCan you give an example of Sage command -> Maxima command -> Maxima output that would give rise to such a situation?  That should make it fairly straightforward to change the at function appropriately.",
    "created_at": "2009-11-13T13:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62138",
    "user": "https://github.com/kcrisman"
}
```

> Perhaps could be improved for multivariable functions, but Maxima expression "at (expr, [eqn_1, ..., eqn_n])" cannot be translated to current Sage and both issues should be fixed together. Perhaps in this ticket? (leaving as needs_work, despite the fact that the original problem has been fixed and doctested)

Can you give an example of Sage command -> Maxima command -> Maxima output that would give rise to such a situation?  That should make it fairly straightforward to change the at function appropriately.



---

archive/issue_comments_062139.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-16T10:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62139",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062140.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> \n> Can you give an example of Sage command -> Maxima command -> Maxima output that would give rise to such a situation?  That should make it fairly straightforward to change the at function appropriately.\n\nI thought that this happens for taylor polynomial in more variables. However, it is not the case (btw. taylor polynomial in more variables seem to be not supported in Sage and I submited patch for #7472).\n\nHence I think that the problem is patched and if someone finds situation where she/he needs to enhace the functionallity, this can be solved in another ticket.",
    "created_at": "2009-11-16T10:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62140",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:7 kcrisman]:
> 
> Can you give an example of Sage command -> Maxima command -> Maxima output that would give rise to such a situation?  That should make it fairly straightforward to change the at function appropriately.

I thought that this happens for taylor polynomial in more variables. However, it is not the case (btw. taylor polynomial in more variables seem to be not supported in Sage and I submited patch for #7472).

Hence I think that the problem is patched and if someone finds situation where she/he needs to enhace the functionallity, this can be solved in another ticket.



---

archive/issue_comments_062141.json:
```json
{
    "body": "The patch fixes also #6376.",
    "created_at": "2009-11-17T14:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62141",
    "user": "https://github.com/robert-marik"
}
```

The patch fixes also #6376.



---

archive/issue_comments_062142.json:
```json
{
    "body": "Okay, positive review, and all relevant tests pass.  It is not optimal because of the dummy variable, one variable, etc., but it fixes things and there are open tickets (some with patches!) for making it even better.  Great.  I will also put a comment on #6376.",
    "created_at": "2009-11-17T16:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62142",
    "user": "https://github.com/kcrisman"
}
```

Okay, positive review, and all relevant tests pass.  It is not optimal because of the dummy variable, one variable, etc., but it fixes things and there are open tickets (some with patches!) for making it even better.  Great.  I will also put a comment on #6376.



---

archive/issue_comments_062143.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-17T16:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62143",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062144.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T17:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62144",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_062145.json:
```json
{
    "body": "This causes a failure in sage/interfaces/maxima.py with this example\n\n\n```\nmaxima(derivative(ceil(x*y*d), d,x,x,y))\n```\n\n\nsince multivariate derivatives are not supported.",
    "created_at": "2009-11-22T05:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62145",
    "user": "https://github.com/mwhansen"
}
```

This causes a failure in sage/interfaces/maxima.py with this example


```
maxima(derivative(ceil(x*y*d), d,x,x,y))
```


since multivariate derivatives are not supported.



---

archive/issue_comments_062146.json:
```json
{
    "body": "I've backed this out for now.",
    "created_at": "2009-11-22T07:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62146",
    "user": "https://github.com/mwhansen"
}
```

I've backed this out for now.



---

archive/issue_comments_062147.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2009-11-22T07:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62147",
    "user": "https://github.com/mwhansen"
}
```

Changing status from closed to needs_work.



---

archive/issue_comments_062148.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-12-05T04:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62148",
    "user": "https://github.com/nbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062149.json:
```json
{
    "body": "On sage 6.5beta1 I get\n\n```\nsage: solve(a==0,diff(f,x).subs(e))\n[D[0](f)(e^t) == -t*e^(-t)/f(e^t)]\n```\n\nso I think this problem has been resolved. Do we close it as (now) invalid?",
    "created_at": "2014-12-05T04:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62149",
    "user": "https://github.com/nbruin"
}
```

On sage 6.5beta1 I get

```
sage: solve(a==0,diff(f,x).subs(e))
[D[0](f)(e^t) == -t*e^(-t)/f(e^t)]
```

so I think this problem has been resolved. Do we close it as (now) invalid?



---

archive/issue_comments_062150.json:
```json
{
    "body": "All doctests in the patch now work without the patch, even the ones that were expected to fail.",
    "created_at": "2014-12-05T08:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62150",
    "user": "https://github.com/pjbruin"
}
```

All doctests in the patch now work without the patch, even the ones that were expected to fail.



---

archive/issue_comments_062151.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-05T08:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62151",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062152.json:
```json
{
    "body": "Awesome!  I tested this last night but it must have been too late, because I didn't notice it worked. :P\n\nIn which case we should *document* that it is fixed so we don't get bitten if (say) we switch symbolics or something again.",
    "created_at": "2014-12-05T14:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62152",
    "user": "https://github.com/kcrisman"
}
```

Awesome!  I tested this last night but it must have been too late, because I didn't notice it worked. :P

In which case we should *document* that it is fixed so we don't get bitten if (say) we switch symbolics or something again.



---

archive/issue_comments_062153.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2014-12-05T14:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62153",
    "user": "https://github.com/kcrisman"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_062154.json:
```json
{
    "body": "As you say, e.g.\n\n```\nsage: x,y,=var('x y') \nsage: a = function('f', x, y).diff(x).subs(x=4).subs(y=8) \nsage: b=maxima(a); b         \n?%at('diff('f(t0,t1),t0,1),[t0=4,t1=8])\nsage: b.sage()\nD[0](f)(4, 8)\n```\n\nHuh.  Maybe this is a side effect of making symbolic variables unique in Maxima?  Or the library interface?  I bet no one has looked at this for a *long* time.",
    "created_at": "2014-12-05T14:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62154",
    "user": "https://github.com/kcrisman"
}
```

As you say, e.g.

```
sage: x,y,=var('x y') 
sage: a = function('f', x, y).diff(x).subs(x=4).subs(y=8) 
sage: b=maxima(a); b         
?%at('diff('f(t0,t1),t0,1),[t0=4,t1=8])
sage: b.sage()
D[0](f)(4, 8)
```

Huh.  Maybe this is a side effect of making symbolic variables unique in Maxima?  Or the library interface?  I bet no one has looked at this for a *long* time.



---

archive/issue_comments_062155.json:
```json
{
    "body": "Changing type from defect to task.",
    "created_at": "2014-12-05T15:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62155",
    "user": "https://github.com/pjbruin"
}
```

Changing type from defect to task.



---

archive/issue_comments_062156.json:
```json
{
    "body": "Replying to [comment:21 kcrisman]:\n> Awesome!  I tested this last night but it must have been too late, because I didn't notice it worked. :P\n> \n> In which case we should *document* that it is fixed so we don't get bitten if (say) we switch symbolics or something again.\nGood point, I guess we can just add the doctests from the patch.",
    "created_at": "2014-12-05T15:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62156",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:21 kcrisman]:
> Awesome!  I tested this last night but it must have been too late, because I didn't notice it worked. :P
> 
> In which case we should *document* that it is fixed so we don't get bitten if (say) we switch symbolics or something again.
Good point, I guess we can just add the doctests from the patch.



---

archive/issue_comments_062157.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2014-12-05T15:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62157",
    "user": "https://github.com/pjbruin"
}
```

Changing priority from major to minor.



---

archive/issue_comments_062158.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-12-05T18:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62158",
    "user": "https://github.com/kcrisman"
}
```

New commits:



---

archive/issue_comments_062159.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-12-05T18:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62159",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062160.json:
```json
{
    "body": "Replying to [comment:24 kcrisman]:\n> New commits:\n> ||[476d8c4](http://git.sagemath.org/sage.git/commit/?id=476d8c43f23185ea22c46a9b30fd37c9ead46668)||`Add doctests for #7401 about derivatives at a point`||\nTwo comments:\n* use `a = function('f')(x,y).diff(x)` to avoid the confusing (and hopefully to deprecated) function('f',x,y).\n* perhaps include an example that also tests the behaviour when the auxiliary variables aren't necessary:\n\n```\nsage: a = function('f')(x,y).diff(x)\nsage: a\nD[0](f)(x, y)\nsage: maxima(a)\n'diff('f(_SAGE_VAR_x,_SAGE_VAR_y),_SAGE_VAR_x,1)\n```\n\nsince that also illustrates a template how to arrive at more user-friendly printing.",
    "created_at": "2014-12-05T19:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62160",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:24 kcrisman]:
> New commits:
> ||[476d8c4](http://git.sagemath.org/sage.git/commit/?id=476d8c43f23185ea22c46a9b30fd37c9ead46668)||`Add doctests for #7401 about derivatives at a point`||
Two comments:
* use `a = function('f')(x,y).diff(x)` to avoid the confusing (and hopefully to deprecated) function('f',x,y).
* perhaps include an example that also tests the behaviour when the auxiliary variables aren't necessary:

```
sage: a = function('f')(x,y).diff(x)
sage: a
D[0](f)(x, y)
sage: maxima(a)
'diff('f(_SAGE_VAR_x,_SAGE_VAR_y),_SAGE_VAR_x,1)
```

since that also illustrates a template how to arrive at more user-friendly printing.



---

archive/issue_comments_062161.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-12-09T01:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62161",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_062162.json:
```json
{
    "body": "Since you basically wrote all the other tests, adding to authors.",
    "created_at": "2014-12-09T02:00:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62162",
    "user": "https://github.com/kcrisman"
}
```

Since you basically wrote all the other tests, adding to authors.



---

archive/issue_comments_062163.json:
```json
{
    "body": "The reviewer patch (typesetting, logical ordering of doctests, checking a few more intermediate results) adds/changes nothing essential.",
    "created_at": "2014-12-15T14:37:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62163",
    "user": "https://github.com/pjbruin"
}
```

The reviewer patch (typesetting, logical ordering of doctests, checking a few more intermediate results) adds/changes nothing essential.



---

archive/issue_comments_062164.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-15T14:37:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7401#issuecomment-62164",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_review to positive_review.
