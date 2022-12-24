# Issue 9878: allow preventing automatic evaluation of symbolic expressions (hold)

archive/issues_009878.json:
```json
{
    "body": "Assignee: burcin\n\nKeywords: pynac\n\nSymbolic expressions automatically evaluate themselves to simplify the data structures, representation, etc. For example,\n\n\n```\nsage: x+x\n2*x\nsage: x*x\nx^2\n```\n\n\nThe ability to disable this evaluation is a feature requested very often.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9879\n\n",
    "created_at": "2010-09-09T08:46:26Z",
    "labels": [
        "symbolics",
        "major",
        "enhancement"
    ],
    "title": "allow preventing automatic evaluation of symbolic expressions (hold)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9878",
    "user": "burcin"
}
```
Assignee: burcin

Keywords: pynac

Symbolic expressions automatically evaluate themselves to simplify the data structures, representation, etc. For example,


```
sage: x+x
2*x
sage: x*x
x^2
```


The ability to disable this evaluation is a feature requested very often.

Issue created by migration from https://trac.sagemath.org/ticket/9879





---

archive/issue_comments_097796.json:
```json
{
    "body": "Attachment [trac_9879-hold.patch](tarball://root/attachments/some-uuid/ticket9879/trac_9879-hold.patch) by burcin created at 2010-09-12 12:17:49\n\nWith attachment:trac_9879-hold.patch and the new pynac package at #9201, one can do:\n\n\n```\nsage: x.add(x,(x+1), hold=True)\nx + x + (x + 1)\nsage: sin(pi, hold=True)\nsin(pi)\n```\n\n\nThe pynac package includes patches for #9394, #9834, #9878, #9881, #9900 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.",
    "created_at": "2010-09-12T12:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97796",
    "user": "burcin"
}
```

Attachment [trac_9879-hold.patch](tarball://root/attachments/some-uuid/ticket9879/trac_9879-hold.patch) by burcin created at 2010-09-12 12:17:49

With attachment:trac_9879-hold.patch and the new pynac package at #9201, one can do:


```
sage: x.add(x,(x+1), hold=True)
x + x + (x + 1)
sage: sin(pi, hold=True)
sin(pi)
```


The pynac package includes patches for #9394, #9834, #9878, #9881, #9900 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.



---

archive/issue_comments_097797.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-12T12:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97797",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097798.json:
```json
{
    "body": "Replying to [comment:1 burcin]:\n> With attachment:trac_9879-hold.patch and the new pynac package at #9201\n\nat #9901. Sorry for the noise.",
    "created_at": "2010-09-12T12:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97798",
    "user": "burcin"
}
```

Replying to [comment:1 burcin]:
> With attachment:trac_9879-hold.patch and the new pynac package at #9201

at #9901. Sorry for the noise.



---

archive/issue_comments_097799.json:
```json
{
    "body": "A question arises in reviewing:\n\n```\n>> Do all the holds in the Pynac code (such as ``return\n>> conjugate_function(asin(x)).hold();``) prevent someone from ever\n>> evaluating these?  I just don't know how it works.\n>\n> The hold() function sets the evaluated flag of a basic object in\n> GiNaC. The automatic evaluation is skipped if this flag is set. Perhaps\n> the duplicate() method ignores this, I'm not sure.\n>\n> In any case, we should provide a method to force this evaluation, but\n> this should be on a separate ticket. Also see my comments below about\n> this.\n\n```\n\nThis is now #10034.",
    "created_at": "2010-09-29T18:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97799",
    "user": "kcrisman"
}
```

A question arises in reviewing:

```
>> Do all the holds in the Pynac code (such as ``return
>> conjugate_function(asin(x)).hold();``) prevent someone from ever
>> evaluating these?  I just don't know how it works.
>
> The hold() function sets the evaluated flag of a basic object in
> GiNaC. The automatic evaluation is skipped if this flag is set. Perhaps
> the duplicate() method ignores this, I'm not sure.
>
> In any case, we should provide a method to force this evaluation, but
> this should be on a separate ticket. Also see my comments below about
> this.

```

This is now #10034.



---

archive/issue_comments_097800.json:
```json
{
    "body": "Making a context for holding is now #10035.",
    "created_at": "2010-09-29T19:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97800",
    "user": "kcrisman"
}
```

Making a context for holding is now #10035.



---

archive/issue_comments_097801.json:
```json
{
    "body": "Attachment [trac_9879-hold-review.patch](tarball://root/attachments/some-uuid/ticket9879/trac_9879-hold-review.patch) by kcrisman created at 2010-10-04 15:01:55\n\nApply after initial patch",
    "created_at": "2010-10-04T15:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97801",
    "user": "kcrisman"
}
```

Attachment [trac_9879-hold-review.patch](tarball://root/attachments/some-uuid/ticket9879/trac_9879-hold-review.patch) by kcrisman created at 2010-10-04 15:01:55

Apply after initial patch



---

archive/issue_comments_097802.json:
```json
{
    "body": "This still needs review, just because the review patch itself is so long. I've added myself as author, but obviously I didn't do much Pynac - just trying to document thoroughly - so if someone disagrees they can change that.  \n\nBurcin, can you review this?  With this I pass all doctests.\n\nAlso, here are some issues which I believe should NOT be addressed here, but need to be on followup tickets.  My philosophy here is that mathematically correct brand-new functionality can be merged even if there are enhancements to it needed.   This ticket shouldn't be closed until new tickets are opened for these issues.\n\n* Typesetting issues. There is nothing mathematically wrong with these (you can try it), but they are obviously confusing to users.  \n\n```\n\nsage: i.mul(2)\n2*I\nsage: i.mul(2,hold=True)\n2*I*\nsage: i.mul(2,hold=True).simplify()\n2*I\nsage: i.mul(i)\n-1\nsage: i.mul(i,hold=True)\n-\nsage: i.mul(i,hold=True).simplify()\n-1\n```\n\n\n* `heaviside(0) != SR(0).step()` This is already true in Sage, so we don't need to address in this ticket, but it becomes obvious when trying to simplify a 'held' expression with `step()`.\n\n* There is no way to get `Order(hold=True)` to evaluate!  Same problem with `csgn` and `step` (the latter could be fixed via the above).  This is annoying but probably they are still useful.\n\n* Big problem, which is why I didn't make log_gamma symbolic:\n\n```\nsage: log_gamma(i).n()\n-0.0219785471672303 - 0.168184318273662*I\nsage: log_gamma(pari(i))\n-0.650923199301856 - 1.87243664726243*I\n(%i3) ev(log_gamma(%i),numer);\n(%o3)             - 1.872436647262428 %i - .6509231993018556\n```\n\nSo no new error has been introduced with this patch, but it exposed this Pynac difference/bug.\n\n* Enhancement - coth, sech, csch and their arc-guys basically already are purely symbolic and hold doesn't do much for them.  For instance:\n\n```\nsage: cosh(0)\n1\nsage: sech(0)\nsech(0)\n```\n\nSo we should do something about that.  But Maxima knows:\n\n```\nsage: sech(0).simplify()\n1\n```\n\n\n* Here is something where I was able to make it work in the doctests, but honestly don't know what is going on.\n\n```\nsage: I.log(hold=True).simplify()\n1/2*I*pi\nsage: var('I')\nI\nsage: I.log(hold=True).simplify()\nlog(I)\nsage: restore('I')\nsage: I.log(hold=True).simplify()\nlog(I)\n```\n\nThis turns out to cause trouble in doctests.  I don't know why this happens.",
    "created_at": "2010-10-04T15:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97802",
    "user": "kcrisman"
}
```

This still needs review, just because the review patch itself is so long. I've added myself as author, but obviously I didn't do much Pynac - just trying to document thoroughly - so if someone disagrees they can change that.  

Burcin, can you review this?  With this I pass all doctests.

Also, here are some issues which I believe should NOT be addressed here, but need to be on followup tickets.  My philosophy here is that mathematically correct brand-new functionality can be merged even if there are enhancements to it needed.   This ticket shouldn't be closed until new tickets are opened for these issues.

* Typesetting issues. There is nothing mathematically wrong with these (you can try it), but they are obviously confusing to users.  

```

sage: i.mul(2)
2*I
sage: i.mul(2,hold=True)
2*I*
sage: i.mul(2,hold=True).simplify()
2*I
sage: i.mul(i)
-1
sage: i.mul(i,hold=True)
-
sage: i.mul(i,hold=True).simplify()
-1
```


* `heaviside(0) != SR(0).step()` This is already true in Sage, so we don't need to address in this ticket, but it becomes obvious when trying to simplify a 'held' expression with `step()`.

* There is no way to get `Order(hold=True)` to evaluate!  Same problem with `csgn` and `step` (the latter could be fixed via the above).  This is annoying but probably they are still useful.

* Big problem, which is why I didn't make log_gamma symbolic:

```
sage: log_gamma(i).n()
-0.0219785471672303 - 0.168184318273662*I
sage: log_gamma(pari(i))
-0.650923199301856 - 1.87243664726243*I
(%i3) ev(log_gamma(%i),numer);
(%o3)             - 1.872436647262428 %i - .6509231993018556
```

So no new error has been introduced with this patch, but it exposed this Pynac difference/bug.

* Enhancement - coth, sech, csch and their arc-guys basically already are purely symbolic and hold doesn't do much for them.  For instance:

```
sage: cosh(0)
1
sage: sech(0)
sech(0)
```

So we should do something about that.  But Maxima knows:

```
sage: sech(0).simplify()
1
```


* Here is something where I was able to make it work in the doctests, but honestly don't know what is going on.

```
sage: I.log(hold=True).simplify()
1/2*I*pi
sage: var('I')
I
sage: I.log(hold=True).simplify()
log(I)
sage: restore('I')
sage: I.log(hold=True).simplify()
log(I)
```

This turns out to cause trouble in doctests.  I don't know why this happens.



---

archive/issue_comments_097803.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-05T11:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97803",
    "user": "jpflori"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097804.json:
```json
{
    "body": "I ran the doctests and looked at the patch.\nEverything looks fine.\nMaybe at line 392 of sage/functions/hyperbolic.py you changed \"WARNING:\" to \".. warning::\" but Sage doc (http://www.sagemath.org/doc/developer/conventions.html) encourages to use uppercase, so \".. WARNING::\" could be used.\nNothing important however.\n\nOther unrelated problems, I'll try to report :\n\n-By the way there is a problem within http://www.sagemath.org/doc/developer/conventions.html.\nIt says to use \".. NOTE:\" and there is \"NOTES:\" in the example.\nThere is also nothing about \"TESTS:\" section which is often used.\nThe reccurent use of \".. blah ::\", \"::\" and \"sage: \" could also be documented or point to the corresponding pages of Sphynx doc (even if looking at the examples is of course the best way to go and looking through Sphynx doc explains many things).\n\n- In sage/symbolic/relation.py inside a warning block a \"{ does }\" should be replaced by \"*does*\"",
    "created_at": "2010-10-05T11:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97804",
    "user": "jpflori"
}
```

I ran the doctests and looked at the patch.
Everything looks fine.
Maybe at line 392 of sage/functions/hyperbolic.py you changed "WARNING:" to ".. warning::" but Sage doc (http://www.sagemath.org/doc/developer/conventions.html) encourages to use uppercase, so ".. WARNING::" could be used.
Nothing important however.

Other unrelated problems, I'll try to report :

-By the way there is a problem within http://www.sagemath.org/doc/developer/conventions.html.
It says to use ".. NOTE:" and there is "NOTES:" in the example.
There is also nothing about "TESTS:" section which is often used.
The reccurent use of ".. blah ::", "::" and "sage: " could also be documented or point to the corresponding pages of Sphynx doc (even if looking at the examples is of course the best way to go and looking through Sphynx doc explains many things).

- In sage/symbolic/relation.py inside a warning block a "{ does }" should be replaced by "*does*"



---

archive/issue_comments_097805.json:
```json
{
    "body": "Replying to [comment:6 jpflori]:\n> I ran the doctests and looked at the patch.\n> Everything looks fine.\n\nGreat, thanks!  \n\nDo you mind putting your \"real\" name in the \"reviewer\" list, and then adding yourself to the long list of Trac users on the main Trac page?  Thanks - that helps a lot; otherwise I'm not sure how we'd track you down.\n\n> Maybe at line 392 of sage/functions/hyperbolic.py you changed \"WARNING:\" to \".. warning::\" but Sage doc (http://www.sagemath.org/doc/developer/conventions.html) encourages to use uppercase, so \".. WARNING::\" could be used.\n> Nothing important however.\n\nHuh - I just did `search_src('warning')` and LOTS of things came up in exactly this way.  That should probably be a global ticket, I agree. \n\n> Other unrelated problems, I'll try to report :\n> \n> -By the way there is a problem within http://www.sagemath.org/doc/developer/conventions.html.\n> It says to use \".. NOTE:\" and there is \"NOTES:\" in the example.\n> There is also nothing about \"TESTS:\" section which is often used.\n> The reccurent use of \".. blah ::\", \"::\" and \"sage: \" could also be documented or point to the corresponding pages of Sphynx doc (even if looking at the examples is of course the best way to go and looking through Sphynx doc explains many things).\nYes, open a ticket and cc: mvgnu and jhpalmieri on it, who both seem to understand Sphinx and would at least have comments on it.\n> - In sage/symbolic/relation.py inside a warning block a \"{ does }\" should be replaced by \"*does*\"\nThis would have priority \"trivial\", I think ;)",
    "created_at": "2010-10-05T13:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97805",
    "user": "kcrisman"
}
```

Replying to [comment:6 jpflori]:
> I ran the doctests and looked at the patch.
> Everything looks fine.

Great, thanks!  

Do you mind putting your "real" name in the "reviewer" list, and then adding yourself to the long list of Trac users on the main Trac page?  Thanks - that helps a lot; otherwise I'm not sure how we'd track you down.

> Maybe at line 392 of sage/functions/hyperbolic.py you changed "WARNING:" to ".. warning::" but Sage doc (http://www.sagemath.org/doc/developer/conventions.html) encourages to use uppercase, so ".. WARNING::" could be used.
> Nothing important however.

Huh - I just did `search_src('warning')` and LOTS of things came up in exactly this way.  That should probably be a global ticket, I agree. 

> Other unrelated problems, I'll try to report :
> 
> -By the way there is a problem within http://www.sagemath.org/doc/developer/conventions.html.
> It says to use ".. NOTE:" and there is "NOTES:" in the example.
> There is also nothing about "TESTS:" section which is often used.
> The reccurent use of ".. blah ::", "::" and "sage: " could also be documented or point to the corresponding pages of Sphynx doc (even if looking at the examples is of course the best way to go and looking through Sphynx doc explains many things).
Yes, open a ticket and cc: mvgnu and jhpalmieri on it, who both seem to understand Sphinx and would at least have comments on it.
> - In sage/symbolic/relation.py inside a warning block a "{ does }" should be replaced by "*does*"
This would have priority "trivial", I think ;)



---

archive/issue_comments_097806.json:
```json
{
    "body": ">  * Typesetting issues. There is nothing mathematically wrong with these (you can try it), but they are obviously confusing to users.  \nThis is now #10069.\n> \n>  * `heaviside(0) != SR(0).step()` This is already true in Sage, so we don't need to address in this ticket, but it becomes obvious when trying to simplify a 'held' expression with `step()`.\nThis is now #10070.\n>  * There is no way to get `Order(hold=True)` to evaluate!  Same problem with `csgn` and `step` (the latter could be fixed via the above).  This is annoying but probably they are still useful.\nThis is now #10071.\n>  * Big problem, which is why I didn't make log_gamma symbolic:\nThis is now #10072, and making `log_gamma` symbolic is #10075.\n>  * Enhancement - coth, sech, csch and their arc-guys basically already are purely symbolic and hold doesn't do much for them.  For instance:\nThis is now #10074.\n> \n>  * Here is something where I was able to make it work in the doctests, but honestly don't know what is going on.\nThis is now #10073.",
    "created_at": "2010-10-05T13:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97806",
    "user": "kcrisman"
}
```

>  * Typesetting issues. There is nothing mathematically wrong with these (you can try it), but they are obviously confusing to users.  
This is now #10069.
> 
>  * `heaviside(0) != SR(0).step()` This is already true in Sage, so we don't need to address in this ticket, but it becomes obvious when trying to simplify a 'held' expression with `step()`.
This is now #10070.
>  * There is no way to get `Order(hold=True)` to evaluate!  Same problem with `csgn` and `step` (the latter could be fixed via the above).  This is annoying but probably they are still useful.
This is now #10071.
>  * Big problem, which is why I didn't make log_gamma symbolic:
This is now #10072, and making `log_gamma` symbolic is #10075.
>  * Enhancement - coth, sech, csch and their arc-guys basically already are purely symbolic and hold doesn't do much for them.  For instance:
This is now #10074.
> 
>  * Here is something where I was able to make it work in the doctests, but honestly don't know what is going on.
This is now #10073.



---

archive/issue_comments_097807.json:
```json
{
    "body": "> Do you mind putting your \"real\" name in the \"reviewer\" list, and then adding yourself to the long list of Trac users on the main Trac page?  Thanks - that helps a lot; otherwise I'm not sure how we'd track you down.\n\nOkay, I found your name on an email from Burcin on sage-devel - hope you don't mind :)  But you should still add yourself to the list on the main page.  Thanks!",
    "created_at": "2010-10-05T15:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97807",
    "user": "kcrisman"
}
```

> Do you mind putting your "real" name in the "reviewer" list, and then adding yourself to the long list of Trac users on the main Trac page?  Thanks - that helps a lot; otherwise I'm not sure how we'd track you down.

Okay, I found your name on an email from Burcin on sage-devel - hope you don't mind :)  But you should still add yourself to the list on the main page.  Thanks!



---

archive/issue_comments_097808.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n\n> Do you mind putting your \"real\" name in the \"reviewer\" list, and then adding yourself to the long list of Trac users on the main Trac page?  Thanks - that helps a lot; otherwise I'm not sure how we'd track you down.\n\nDone, I thought I already put it somewhere at some point...\n\n> Huh - I just did `search_src('warning')` and LOTS of things came up in exactly this way.  That should probably be a global ticket, I agree.\n\nThis is now ticket #10078.\n\n> Yes, open a ticket and cc: mvgnu and jhpalmieri on it, who both seem to understand Sphinx and would at least have comments on it.\n\nThis is now ticket #10077.\n\n> This would have priority \"trivial\", I think ;)\n\nThis is now #10079 (with a \"patch\" provided).",
    "created_at": "2010-10-05T20:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97808",
    "user": "jpflori"
}
```

Replying to [comment:7 kcrisman]:

> Do you mind putting your "real" name in the "reviewer" list, and then adding yourself to the long list of Trac users on the main Trac page?  Thanks - that helps a lot; otherwise I'm not sure how we'd track you down.

Done, I thought I already put it somewhere at some point...

> Huh - I just did `search_src('warning')` and LOTS of things came up in exactly this way.  That should probably be a global ticket, I agree.

This is now ticket #10078.

> Yes, open a ticket and cc: mvgnu and jhpalmieri on it, who both seem to understand Sphinx and would at least have comments on it.

This is now ticket #10077.

> This would have priority "trivial", I think ;)

This is now #10079 (with a "patch" provided).



---

archive/issue_comments_097809.json:
```json
{
    "body": "Speaking of these doc issues, when reading through the doc in symbolic/expression.pyx I realized that there were some pre-existing problems in the html documentation.  This is now #10080.\n\n11 out of 12 consecutive tickets all as followups from one ticket... this must be a good ticket ;)  Or at least well-proofread, since nearly all of these things have nothing to do with the ticket per se, but were discovered while reviewing it.",
    "created_at": "2010-10-06T01:47:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97809",
    "user": "kcrisman"
}
```

Speaking of these doc issues, when reading through the doc in symbolic/expression.pyx I realized that there were some pre-existing problems in the html documentation.  This is now #10080.

11 out of 12 consecutive tickets all as followups from one ticket... this must be a good ticket ;)  Or at least well-proofread, since nearly all of these things have nothing to do with the ticket per se, but were discovered while reviewing it.



---

archive/issue_comments_097810.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-06T03:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9878#issuecomment-97810",
    "user": "mpatel"
}
```

Resolution: fixed
