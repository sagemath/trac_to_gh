# Issue 5567: [with patch, needs review] bug in region_plot

archive/issues_005567.json:
```json
{
    "body": "Assignee: whuss\n\n\n```\nHello, this command produces one half of a cirle, not 1/4 as excepted.\nI think that this is a bug in sage 3.4\n\nRobert\n\nregion_plot([y>0,x>0,x^2+y^2<3], (-3, 3), (-3,3),plot_points=100,incol='gray').show(aspect_ratio=1)\n```\n\n\nThe attached patch fixes this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5567\n\n",
    "created_at": "2009-03-19T16:29:16Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] bug in region_plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5567",
    "user": "whuss"
}
```
Assignee: whuss


```
Hello, this command produces one half of a cirle, not 1/4 as excepted.
I think that this is a bug in sage 3.4

Robert

region_plot([y>0,x>0,x^2+y^2<3], (-3, 3), (-3,3),plot_points=100,incol='gray').show(aspect_ratio=1)
```


The attached patch fixes this.

Issue created by migration from https://trac.sagemath.org/ticket/5567





---

archive/issue_comments_043379.json:
```json
{
    "body": "REFEREE REPORT:\n\nApplies fine to Sage 3.4, fixes the bug as described, passes its doctests. This looks like a solid patch. Positive review.",
    "created_at": "2009-04-13T22:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5567#issuecomment-43379",
    "user": "wcauchois"
}
```

REFEREE REPORT:

Applies fine to Sage 3.4, fixes the bug as described, passes its doctests. This looks like a solid patch. Positive review.



---

archive/issue_comments_043380.json:
```json
{
    "body": "This has bitrottet, please rebase:\n\n```\nsage-3.4.1.rc3/devel/sage$ patch -p1 < trac_5567_region_plot.patch \npatching file sage/plot/contour_plot.py\nHunk #1 FAILED at 234.\nHunk #2 FAILED at 247.\nHunk #3 succeeded at 277 (offset 14 lines).\nHunk #4 succeeded at 308 (offset 14 lines).\n2 out of 4 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej\n```\n\n\nBill: When you review please always review against the latest release snapshot.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T00:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5567#issuecomment-43380",
    "user": "mabshoff"
}
```

This has bitrottet, please rebase:

```
sage-3.4.1.rc3/devel/sage$ patch -p1 < trac_5567_region_plot.patch 
patching file sage/plot/contour_plot.py
Hunk #1 FAILED at 234.
Hunk #2 FAILED at 247.
Hunk #3 succeeded at 277 (offset 14 lines).
Hunk #4 succeeded at 308 (offset 14 lines).
2 out of 4 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej
```


Bill: When you review please always review against the latest release snapshot.

Cheers,

Michael



---

archive/issue_comments_043381.json:
```json
{
    "body": "rebased for sage-3.4.1.rc3",
    "created_at": "2009-04-17T14:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5567#issuecomment-43381",
    "user": "whuss"
}
```

rebased for sage-3.4.1.rc3



---

archive/issue_comments_043382.json:
```json
{
    "body": "Attachment [region_plot.patch](tarball://root/attachments/some-uuid/ticket5567/region_plot.patch) by whuss created at 2009-04-17 14:55:20",
    "created_at": "2009-04-17T14:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5567#issuecomment-43382",
    "user": "whuss"
}
```

Attachment [region_plot.patch](tarball://root/attachments/some-uuid/ticket5567/region_plot.patch) by whuss created at 2009-04-17 14:55:20



---

archive/issue_comments_043383.json:
```json
{
    "body": "REFEREE REPORT:\n\nApplies fine to Sage 3.4.1.rc4. Still passes its doctests and implements the changes as described in the ticket. Positive review.",
    "created_at": "2009-04-21T05:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5567#issuecomment-43383",
    "user": "wcauchois"
}
```

REFEREE REPORT:

Applies fine to Sage 3.4.1.rc4. Still passes its doctests and implements the changes as described in the ticket. Positive review.



---

archive/issue_comments_043384.json:
```json
{
    "body": "Merged in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T07:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5567#issuecomment-43384",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_043385.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-23T07:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5567#issuecomment-43385",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043386.json:
```json
{
    "body": "Shouldn't the code in the doctest be deprecated in light of http://trac.sagemath.org/sage_trac/ticket/5413 ?\n\nIn fact, the equify function seems like it is in direct conflict with the deprecation in http://trac.sagemath.org/sage_trac/ticket/5413, is it not?",
    "created_at": "2009-04-24T01:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5567#issuecomment-43386",
    "user": "jason"
}
```

Shouldn't the code in the doctest be deprecated in light of http://trac.sagemath.org/sage_trac/ticket/5413 ?

In fact, the equify function seems like it is in direct conflict with the deprecation in http://trac.sagemath.org/sage_trac/ticket/5413, is it not?



---

archive/issue_comments_043387.json:
```json
{
    "body": "Replying to [comment:6 jason]:\n> Shouldn't the code in the doctest be deprecated in light of http://trac.sagemath.org/sage_trac/ticket/5413 ?\n> \n> In fact, the equify function seems like it is in direct conflict with the deprecation in http://trac.sagemath.org/sage_trac/ticket/5413, is it not?\n\nPlaying around in the REPL, I don't see a way to define an inequality with explicit variables -- since its not really a function. `f(x) = x^2 < 2` throws an exception, for example. For region_plot, the variables can be made explicit by specifying them in the plot ranges, in which case they are passed on to equify via an argument. So the ambiguity which was the motivation for #5413 can be avoided. I think that this is a subtly different situation, and that `equify` is fine.",
    "created_at": "2009-05-04T21:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5567#issuecomment-43387",
    "user": "wcauchois"
}
```

Replying to [comment:6 jason]:
> Shouldn't the code in the doctest be deprecated in light of http://trac.sagemath.org/sage_trac/ticket/5413 ?
> 
> In fact, the equify function seems like it is in direct conflict with the deprecation in http://trac.sagemath.org/sage_trac/ticket/5413, is it not?

Playing around in the REPL, I don't see a way to define an inequality with explicit variables -- since its not really a function. `f(x) = x^2 < 2` throws an exception, for example. For region_plot, the variables can be made explicit by specifying them in the plot ranges, in which case they are passed on to equify via an argument. So the ambiguity which was the motivation for #5413 can be avoided. I think that this is a subtly different situation, and that `equify` is fine.



---

archive/issue_comments_043388.json:
```json
{
    "body": "Replying to [comment:7 wcauchois]:\n> Replying to [comment:6 jason]:\n> > Shouldn't the code in the doctest be deprecated in light of http://trac.sagemath.org/sage_trac/ticket/5413 ?\n> > \n> > In fact, the equify function seems like it is in direct conflict with the deprecation in http://trac.sagemath.org/sage_trac/ticket/5413, is it not?\n> \n> Playing around in the REPL, I don't see a way to define an inequality with explicit variables -- since its not really a function. `f(x) = x^2 < 2` throws an exception, for example. For region_plot, the variables can be made explicit by specifying them in the plot ranges, in which case they are passed on to equify via an argument. So the ambiguity which was the motivation for #5413 can be avoided. I think that this is a subtly different situation, and that `equify` is fine.\n\nThe point is that equify lets variables default to None, and in that case, automatically chooses the order of variables in the call signature.  That's what the deprecation is about---making sure that the user always specified the order of evaluation, and not automatically choosing an order.\n\nAnd while the ambiguity can be avoided in the function call, the doctest in the patch still uses deprecated syntax (which should throw a deprecation warning).  The doctest should still be changed to have the variables specified.",
    "created_at": "2009-05-05T01:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5567#issuecomment-43388",
    "user": "jason"
}
```

Replying to [comment:7 wcauchois]:
> Replying to [comment:6 jason]:
> > Shouldn't the code in the doctest be deprecated in light of http://trac.sagemath.org/sage_trac/ticket/5413 ?
> > 
> > In fact, the equify function seems like it is in direct conflict with the deprecation in http://trac.sagemath.org/sage_trac/ticket/5413, is it not?
> 
> Playing around in the REPL, I don't see a way to define an inequality with explicit variables -- since its not really a function. `f(x) = x^2 < 2` throws an exception, for example. For region_plot, the variables can be made explicit by specifying them in the plot ranges, in which case they are passed on to equify via an argument. So the ambiguity which was the motivation for #5413 can be avoided. I think that this is a subtly different situation, and that `equify` is fine.

The point is that equify lets variables default to None, and in that case, automatically chooses the order of variables in the call signature.  That's what the deprecation is about---making sure that the user always specified the order of evaluation, and not automatically choosing an order.

And while the ambiguity can be avoided in the function call, the doctest in the patch still uses deprecated syntax (which should throw a deprecation warning).  The doctest should still be changed to have the variables specified.
