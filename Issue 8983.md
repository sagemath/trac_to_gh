# Issue 8983: solve(erf(x)==0,x) should return x==0 as a solution

archive/issues_008983.json:
```json
{
    "body": "Assignee: RossK\n\nCC:  @burcin @kcrisman\n\nKeywords: erf zero\n\nCurrently it doesnt...\n\n```\nsage: solve(erf(x)==0,x)\n[erf(x) == 0]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8983\n\n",
    "created_at": "2010-05-17T13:15:56Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "solve(erf(x)==0,x) should return x==0 as a solution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8983",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```
Assignee: RossK

CC:  @burcin @kcrisman

Keywords: erf zero

Currently it doesnt...

```
sage: solve(erf(x)==0,x)
[erf(x) == 0]
```

Issue created by migration from https://trac.sagemath.org/ticket/8983





---

archive/issue_comments_082732.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-05-17T13:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82732",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_082733.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-05-17T13:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82733",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Changing priority from major to minor.



---

archive/issue_comments_082734.json:
```json
{
    "body": "Here is the relevant thread on sage-devel:\n\nhttp://groups.google.com/group/sage-devel/t/d236e80bf7826bff\n\nThe main problem is this:\n\n```\nsage: erf(0)\nerf(0)\n```\n\nWe should just return 0.",
    "created_at": "2010-05-17T13:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82734",
    "user": "https://github.com/burcin"
}
```

Here is the relevant thread on sage-devel:

http://groups.google.com/group/sage-devel/t/d236e80bf7826bff

The main problem is this:

```
sage: erf(0)
erf(0)
```

We should just return 0.



---

archive/issue_comments_082735.json:
```json
{
    "body": "Changing keywords from \"erf zero\" to \"erf, beginner\".",
    "created_at": "2010-08-28T16:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82735",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "erf zero" to "erf, beginner".



---

archive/issue_comments_082736.json:
```json
{
    "body": "Beginner reporting for duty!  So I have a patch which sets erf(0) to 0 -- or, rather, to parent(x)(0) if x==0, so that it's the \"right\" zero; I think this is the right idiom -- and adds complex arguments from mpmath.\n\nBut I have a few questions that came up along the way:\n\n(1) In 4.6.1, solve(erf(x)==0,x) seems to work for me already, before the patch.  Did I get my binaries confused somehow, or did something change elsewhere?\n\n(2) It'd be nice if #8720 (fixing str(CC(0))) were finished, it surprised me when writing tests for the zero type preservation. Maybe I should have a look, I think it's mostly fixing some doctests left.\n\n(3) My patch broke a doctest in functions/special.py, which expected erf(0.5) to be evaluated to 0.520499877813047, but the existing doctests for erf demand that erf(2) = erf(2). I can get that behaviour, namely to evaluate for reals and to hold for integers except for zero, but I don't quite follow it.\n\n(4) Since I'm doing a bit more, should I open an enhancement ticket instead?",
    "created_at": "2011-02-20T05:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82736",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Beginner reporting for duty!  So I have a patch which sets erf(0) to 0 -- or, rather, to parent(x)(0) if x==0, so that it's the "right" zero; I think this is the right idiom -- and adds complex arguments from mpmath.

But I have a few questions that came up along the way:

(1) In 4.6.1, solve(erf(x)==0,x) seems to work for me already, before the patch.  Did I get my binaries confused somehow, or did something change elsewhere?

(2) It'd be nice if #8720 (fixing str(CC(0))) were finished, it surprised me when writing tests for the zero type preservation. Maybe I should have a look, I think it's mostly fixing some doctests left.

(3) My patch broke a doctest in functions/special.py, which expected erf(0.5) to be evaluated to 0.520499877813047, but the existing doctests for erf demand that erf(2) = erf(2). I can get that behaviour, namely to evaluate for reals and to hold for integers except for zero, but I don't quite follow it.

(4) Since I'm doing a bit more, should I open an enhancement ticket instead?



---

archive/issue_comments_082737.json:
```json
{
    "body": "You should always feel free to add patches - it's MUCH easier to tell what people are talking about, even if the patch is really, really preliminary.\n> (1) In 4.6.1, solve(erf(x)==0,x) seems to work for me already, before the patch.  Did I get my binaries confused somehow, or did something change elsewhere?\n\nThis must be from an improvement in Maxima during the several recent upgrades.  I've updated the description.\n> (3) My patch broke a doctest in functions/special.py, which expected erf(0.5) to be evaluated to 0.520499877813047, but the existing doctests for erf demand that erf(2) = erf(2). I can get that behaviour, namely to evaluate for reals and to hold for integers except for zero, but I don't quite follow it.\n\nNo, the usual practice is to not evaluate (give symbolic back) for \"exact\" rings and evaluate (give numeric back) for \"inexact\" rings.  There is some disagreement among developers about exactly what these words mean, but basically `erf(x),erf(1/2),erf(2),erf(e)` should all return something symbolic and `erf(.1),erf(RDF(1))`, etc. should return something numeric.  I.e. `erf2)!=erf(2.)`.\n> \n> (4) Since I'm doing a bit more, should I open an enhancement ticket instead?\n\nI believe there already is a ticket for the complex pieces at #1173, similarly at #9044.  If you have a good solution to the whole thing, you could do it at one of those and then say this ticket can be closed when they are (if you have also documented that it's fixed.",
    "created_at": "2011-02-21T16:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82737",
    "user": "https://github.com/kcrisman"
}
```

You should always feel free to add patches - it's MUCH easier to tell what people are talking about, even if the patch is really, really preliminary.
> (1) In 4.6.1, solve(erf(x)==0,x) seems to work for me already, before the patch.  Did I get my binaries confused somehow, or did something change elsewhere?

This must be from an improvement in Maxima during the several recent upgrades.  I've updated the description.
> (3) My patch broke a doctest in functions/special.py, which expected erf(0.5) to be evaluated to 0.520499877813047, but the existing doctests for erf demand that erf(2) = erf(2). I can get that behaviour, namely to evaluate for reals and to hold for integers except for zero, but I don't quite follow it.

No, the usual practice is to not evaluate (give symbolic back) for "exact" rings and evaluate (give numeric back) for "inexact" rings.  There is some disagreement among developers about exactly what these words mean, but basically `erf(x),erf(1/2),erf(2),erf(e)` should all return something symbolic and `erf(.1),erf(RDF(1))`, etc. should return something numeric.  I.e. `erf2)!=erf(2.)`.
> 
> (4) Since I'm doing a bit more, should I open an enhancement ticket instead?

I believe there already is a ticket for the complex pieces at #1173, similarly at #9044.  If you have a good solution to the whole thing, you could do it at one of those and then say this ticket can be closed when they are (if you have also documented that it's fixed.



---

archive/issue_comments_082738.json:
```json
{
    "body": "`@`kcrisman: okay, understood.  Will propose under #1173.",
    "created_at": "2011-02-24T01:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82738",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

`@`kcrisman: okay, understood.  Will propose under #1173.



---

archive/issue_comments_082739.json:
```json
{
    "body": "If #1173 isn't going to happen anytime soon because of #11513, a very simple patch here would be nice.  It would document\n\n```\nsage: solve(erf(x)==0,x)\n[x == 0]\n```\nas mentioned above already works, and take care of the issue in the summary, of course.",
    "created_at": "2011-12-19T17:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82739",
    "user": "https://github.com/kcrisman"
}
```

If #1173 isn't going to happen anytime soon because of #11513, a very simple patch here would be nice.  It would document

```
sage: solve(erf(x)==0,x)
[x == 0]
```
as mentioned above already works, and take care of the issue in the summary, of course.



---

archive/issue_comments_082740.json:
```json
{
    "body": "I think the right thing to do here is to depend on #11513. There are several ways one could address the issue in the summary about erf(0) not returning 0, but when a good patch for 11513 appears, the code being touched here would need to be changed again.",
    "created_at": "2012-01-09T17:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82740",
    "user": "https://github.com/benjaminfjones"
}
```

I think the right thing to do here is to depend on #11513. There are several ways one could address the issue in the summary about erf(0) not returning 0, but when a good patch for 11513 appears, the code being touched here would need to be changed again.



---

archive/issue_comments_082741.json:
```json
{
    "body": "Attachment [trac_8983.patch](tarball://root/attachments/some-uuid/ticket8983/trac_8983.patch) by @benjaminfjones created at 2012-02-12 06:34:43\n\nmake erf(0) return 0",
    "created_at": "2012-02-12T06:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82741",
    "user": "https://github.com/benjaminfjones"
}
```

Attachment [trac_8983.patch](tarball://root/attachments/some-uuid/ticket8983/trac_8983.patch) by @benjaminfjones created at 2012-02-12 06:34:43

make erf(0) return 0



---

archive/issue_comments_082742.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-02-12T06:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82742",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082743.json:
```json
{
    "body": "I uploaded a simple patch now that #11513 is merged.",
    "created_at": "2012-02-12T06:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82743",
    "user": "https://github.com/benjaminfjones"
}
```

I uploaded a simple patch now that #11513 is merged.



---

archive/issue_comments_082744.json:
```json
{
    "body": "Looks good, but I think we should return a Sage zero (or at least match the type):\n\n```\n\nsage: erf(0)\n0\nsage: parent(erf(0))\n<type 'int'>\n\n```",
    "created_at": "2012-02-13T02:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82744",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Looks good, but I think we should return a Sage zero (or at least match the type):

```

sage: erf(0)
0
sage: parent(erf(0))
<type 'int'>

```



---

archive/issue_comments_082745.json:
```json
{
    "body": "That's a good point, this patch addresses the issue by returning the input `x` instead of 0 when a python 0 would have been returned in the previous patch.\n\n```\nsage: erf(0)\n0\nsage: type(erf(0))\n<type 'sage.rings.integer.Integer'>\nsage: parent(erf(0))\nInteger Ring\n```",
    "created_at": "2012-02-13T04:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82745",
    "user": "https://github.com/benjaminfjones"
}
```

That's a good point, this patch addresses the issue by returning the input `x` instead of 0 when a python 0 would have been returned in the previous patch.

```
sage: erf(0)
0
sage: type(erf(0))
<type 'sage.rings.integer.Integer'>
sage: parent(erf(0))
Integer Ring
```



---

archive/issue_comments_082746.json:
```json
{
    "body": "Attachment [trac_8983_v2.patch](tarball://root/attachments/some-uuid/ticket8983/trac_8983_v2.patch) by @benjaminfjones created at 2012-02-13 04:33:25\n\nmake erf(0) return 0",
    "created_at": "2012-02-13T04:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82746",
    "user": "https://github.com/benjaminfjones"
}
```

Attachment [trac_8983_v2.patch](tarball://root/attachments/some-uuid/ticket8983/trac_8983_v2.patch) by @benjaminfjones created at 2012-02-13 04:33:25

make erf(0) return 0



---

archive/issue_comments_082747.json:
```json
{
    "body": "Okay, looks good to me (or at least none of my obvious tricks could break it).",
    "created_at": "2012-02-13T05:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82747",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Okay, looks good to me (or at least none of my obvious tricks could break it).



---

archive/issue_comments_082748.json:
```json
{
    "body": "Thanks for the patch Benjamin. It looks great and gets the job done. However, I'd be much happier if there were a couple more doctests. There are quite a few branches in the new `_eval_()` function, but the patch adds only one doctest.\n\nOne more suggestion: It might be better to leave the last `return None` statement outside the `if`s. IMHO, the following is more compact and readable.\n\n```\nif not isinstance(x, Expression): \n    if is_inexact(x): \n        return self._evalf_(x, parent=parent(x)) \n    elif x == 0: \n        return x \nelif x.is_trivial_zero(): \n        return x \nreturn None \n```",
    "created_at": "2012-02-13T09:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82748",
    "user": "https://github.com/burcin"
}
```

Thanks for the patch Benjamin. It looks great and gets the job done. However, I'd be much happier if there were a couple more doctests. There are quite a few branches in the new `_eval_()` function, but the patch adds only one doctest.

One more suggestion: It might be better to leave the last `return None` statement outside the `if`s. IMHO, the following is more compact and readable.

```
if not isinstance(x, Expression): 
    if is_inexact(x): 
        return self._evalf_(x, parent=parent(x)) 
    elif x == 0: 
        return x 
elif x.is_trivial_zero(): 
        return x 
return None 
```



---

archive/issue_comments_082749.json:
```json
{
    "body": "Replying to [comment:11 dsm]:\n> Looks good, but I think we should return a Sage zero (or at least match the type):\n\nIs this what you were referring to at comment:2:ticket:10133, dsm?\n\nMore generally, does anyone think the present way of ensuring `erf(0)` returns an Integer (or even Symbolic Expression) is a good one for #10133?  Or is it better to address this at the Pynac level?",
    "created_at": "2012-02-13T18:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82749",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:11 dsm]:
> Looks good, but I think we should return a Sage zero (or at least match the type):

Is this what you were referring to at comment:2:ticket:10133, dsm?

More generally, does anyone think the present way of ensuring `erf(0)` returns an Integer (or even Symbolic Expression) is a good one for #10133?  Or is it better to address this at the Pynac level?



---

archive/issue_comments_082750.json:
```json
{
    "body": "Replying to [comment:15 burcin]:\nThat's a good suggestion. I modified the `_eval_` method accordingly and added several doctests verifying that all branches are reached. Maybe that's overkill, but it took me a while to find an input that actually reached the `x.is_trivial_zero()` branch.",
    "created_at": "2012-02-14T05:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82750",
    "user": "https://github.com/benjaminfjones"
}
```

Replying to [comment:15 burcin]:
That's a good suggestion. I modified the `_eval_` method accordingly and added several doctests verifying that all branches are reached. Maybe that's overkill, but it took me a while to find an input that actually reached the `x.is_trivial_zero()` branch.



---

archive/issue_comments_082751.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-14T10:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82751",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082752.json:
```json
{
    "body": "Replying to [comment:17 benjaminfjones]:\n> Maybe that's overkill, but it took me a while to find an input that actually reached the `x.is_trivial_zero()` branch.\n\n\nIt's not overkill at all, after adding _a_ doctest to every function, perhaps we will measure the coverage in terms of percentage of lines executed with those tests. Thanks for spending the time and giving this function 100% coverage. :)\n\nBTW, `erf(SR(0))` should be a simple way of hitting the `is_trivially_zero()` branch.",
    "created_at": "2012-02-14T10:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82752",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:17 benjaminfjones]:
> Maybe that's overkill, but it took me a while to find an input that actually reached the `x.is_trivial_zero()` branch.


It's not overkill at all, after adding _a_ doctest to every function, perhaps we will measure the coverage in terms of percentage of lines executed with those tests. Thanks for spending the time and giving this function 100% coverage. :)

BTW, `erf(SR(0))` should be a simple way of hitting the `is_trivially_zero()` branch.



---

archive/issue_comments_082753.json:
```json
{
    "body": "Attachment [trac_8983_v3.patch](tarball://root/attachments/some-uuid/ticket8983/trac_8983_v3.patch) by @benjaminfjones created at 2012-02-14 16:53:00\n\nmake erf(0) return 0, with added doctests and simplified branching in _eval_",
    "created_at": "2012-02-14T16:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82753",
    "user": "https://github.com/benjaminfjones"
}
```

Attachment [trac_8983_v3.patch](tarball://root/attachments/some-uuid/ticket8983/trac_8983_v3.patch) by @benjaminfjones created at 2012-02-14 16:53:00

make erf(0) return 0, with added doctests and simplified branching in _eval_



---

archive/issue_comments_082754.json:
```json
{
    "body": "Ok, I simplified that last doctest in `_eval_`.",
    "created_at": "2012-02-14T16:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82754",
    "user": "https://github.com/benjaminfjones"
}
```

Ok, I simplified that last doctest in `_eval_`.



---

archive/issue_events_021980.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-02-22T10:44:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8983#event-21980"
}
```



---

archive/issue_comments_082755.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-02-22T10:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8983#issuecomment-82755",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
