# Issue 4735: Make e^X try calling X.exp() before trying to coerce X to the symbolic ring

archive/issues_004735.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @kcrisman\n\nFrom sage-devel:\n\n> I'd like to add an exponential function to RDF/CDF matrices (and  \n> > enhance\n> > the existing exp function for SR matrices) so that:\n> >\n> > sage: A = matrix(SR, [[1,2],[3,4]])\n> > sage: e^A\n> >\n> > gives the same as\n> >\n> > sage: A.exp()\n> >\n> > (I'd also like this to work for other matrices, like over RDF or CDF,\n> > where the returned matrix would be another RDF/CDF matrix---scipy has\n> > functions that do this).\n> >\n> > However, currently for constants (in sage/functions/constants.py), the\n> > __pow__ function automatically converts the exponent to an SR object,\n> > which fails for a matrix.\n> >\n> > I have not worked with the constants code before.  Would there be a\n> > problem with, for the E constant, overriding __pow__ so that if the\n> > object had an \"_exp\" method, that was called instead of the default\n> > conversion to SR objects?\n\n+1, this was my first though when I started reading your email. I  \ndon't think it makes sense for other constants, but for E it  \ncertainly does. Also, I'd just call exp (not _exp), making sure that  \nit doesn't introduce a recursive call...\n\n> > Would that be the proper way to get the above functionality?  The goal\n> > is also to get exp(A) to work as well; would I get that for free?\n\nYes. When you do exp(A) it attempts to return A.exp() before doing  \nanything symbolic.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4735\n\n",
    "created_at": "2008-12-07T04:53:37Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.1",
    "title": "Make e^X try calling X.exp() before trying to coerce X to the symbolic ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4735",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @burcin

CC:  @kcrisman

From sage-devel:

> I'd like to add an exponential function to RDF/CDF matrices (and  
> > enhance
> > the existing exp function for SR matrices) so that:
> >
> > sage: A = matrix(SR, [[1,2],[3,4]])
> > sage: e^A
> >
> > gives the same as
> >
> > sage: A.exp()
> >
> > (I'd also like this to work for other matrices, like over RDF or CDF,
> > where the returned matrix would be another RDF/CDF matrix---scipy has
> > functions that do this).
> >
> > However, currently for constants (in sage/functions/constants.py), the
> > __pow__ function automatically converts the exponent to an SR object,
> > which fails for a matrix.
> >
> > I have not worked with the constants code before.  Would there be a
> > problem with, for the E constant, overriding __pow__ so that if the
> > object had an "_exp" method, that was called instead of the default
> > conversion to SR objects?

+1, this was my first though when I started reading your email. I  
don't think it makes sense for other constants, but for E it  
certainly does. Also, I'd just call exp (not _exp), making sure that  
it doesn't introduce a recursive call...

> > Would that be the proper way to get the above functionality?  The goal
> > is also to get exp(A) to work as well; would I get that for free?

Yes. When you do exp(A) it attempts to return A.exp() before doing  
anything symbolic.

Issue created by migration from https://trac.sagemath.org/ticket/4735





---

archive/issue_comments_035672.json:
```json
{
    "body": "To do this, you'd have to add a check before every __pow__ operation with elements of SR, which may or may not be too much overhead.",
    "created_at": "2009-06-05T02:07:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35672",
    "user": "https://github.com/mwhansen"
}
```

To do this, you'd have to add a check before every __pow__ operation with elements of SR, which may or may not be too much overhead.



---

archive/issue_comments_035673.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2011-03-16T15:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35673",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_035674.json:
```json
{
    "body": "I don't think that this is necessarily a good idea to implement due to the reason I gave before.",
    "created_at": "2012-03-29T05:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35674",
    "user": "https://github.com/mwhansen"
}
```

I don't think that this is necessarily a good idea to implement due to the reason I gave before.



---

archive/issue_comments_035675.json:
```json
{
    "body": "I'm changing the title to address the actual problem reported.\n\nCan you think of a solution to the problem that this doesn't work, though?\n\n```\nsage: A = matrix(SR, [[1,2],[3,4]])\nsage: exp(A)\n[-1/22*((sqrt(33) - 11)*e^sqrt(33) - sqrt(33) - 11)*e^(-1/2*sqrt(33) + 5/2)              2/33*(sqrt(33)*e^sqrt(33) - sqrt(33))*e^(-1/2*sqrt(33) + 5/2)]\n[             1/11*(sqrt(33)*e^sqrt(33) - sqrt(33))*e^(-1/2*sqrt(33) + 5/2)  1/22*((sqrt(33) + 11)*e^sqrt(33) - sqrt(33) + 11)*e^(-1/2*sqrt(33) + 5/2)]\nsage: A.exp()\n[-1/22*((sqrt(33) - 11)*e^sqrt(33) - sqrt(33) - 11)*e^(-1/2*sqrt(33) + 5/2)              2/33*(sqrt(33)*e^sqrt(33) - sqrt(33))*e^(-1/2*sqrt(33) + 5/2)]\n[             1/11*(sqrt(33)*e^sqrt(33) - sqrt(33))*e^(-1/2*sqrt(33) + 5/2)  1/22*((sqrt(33) + 11)*e^sqrt(33) - sqrt(33) + 11)*e^(-1/2*sqrt(33) + 5/2)]\nsage: e^A\n---------------------------------------------------------------------------\nTypeError: mutable matrices are unhashable\n```\n\nI get the same problem with entries in `RR`, and the original post noted `RDF` is also a problem.\n\nI wonder if this is more calculus or more linear algebra... maybe a different component?",
    "created_at": "2012-03-29T14:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35675",
    "user": "https://github.com/kcrisman"
}
```

I'm changing the title to address the actual problem reported.

Can you think of a solution to the problem that this doesn't work, though?

```
sage: A = matrix(SR, [[1,2],[3,4]])
sage: exp(A)
[-1/22*((sqrt(33) - 11)*e^sqrt(33) - sqrt(33) - 11)*e^(-1/2*sqrt(33) + 5/2)              2/33*(sqrt(33)*e^sqrt(33) - sqrt(33))*e^(-1/2*sqrt(33) + 5/2)]
[             1/11*(sqrt(33)*e^sqrt(33) - sqrt(33))*e^(-1/2*sqrt(33) + 5/2)  1/22*((sqrt(33) + 11)*e^sqrt(33) - sqrt(33) + 11)*e^(-1/2*sqrt(33) + 5/2)]
sage: A.exp()
[-1/22*((sqrt(33) - 11)*e^sqrt(33) - sqrt(33) - 11)*e^(-1/2*sqrt(33) + 5/2)              2/33*(sqrt(33)*e^sqrt(33) - sqrt(33))*e^(-1/2*sqrt(33) + 5/2)]
[             1/11*(sqrt(33)*e^sqrt(33) - sqrt(33))*e^(-1/2*sqrt(33) + 5/2)  1/22*((sqrt(33) + 11)*e^sqrt(33) - sqrt(33) + 11)*e^(-1/2*sqrt(33) + 5/2)]
sage: e^A
---------------------------------------------------------------------------
TypeError: mutable matrices are unhashable
```

I get the same problem with entries in `RR`, and the original post noted `RDF` is also a problem.

I wonder if this is more calculus or more linear algebra... maybe a different component?



---

archive/issue_comments_035676.json:
```json
{
    "body": "Wouldn't changing `e.__pow__()` to be smarter work?\n\nThe error message above is raised when you try convert a matrix to a symbolic ring element. In the new symbolics, the constant E (defined in `sage/symbolic/constants.py` has a `__pow__` method that essentially does `e^x -> SR(x).exp()`. (This was probably written by Mike.)\n\nIf you change that to call `x.exp()` first, you might get what you want.",
    "created_at": "2012-03-29T14:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35676",
    "user": "https://github.com/burcin"
}
```

Wouldn't changing `e.__pow__()` to be smarter work?

The error message above is raised when you try convert a matrix to a symbolic ring element. In the new symbolics, the constant E (defined in `sage/symbolic/constants.py` has a `__pow__` method that essentially does `e^x -> SR(x).exp()`. (This was probably written by Mike.)

If you change that to call `x.exp()` first, you might get what you want.



---

archive/issue_comments_035677.json:
```json
{
    "body": "Ah.  And the original posts apparently do refer only to changing for `E`.  Mike, are you saying this could cause a problem in this specific case, or only if we did it more widely?  It would be interesting to compare timings for making this change; naturally, one could potentially have a *lot* of `e^foo` in a given computation, so even microseconds spent checking whether `foo` had a `exp()` method could add up, which I think is his point... maybe?",
    "created_at": "2012-03-29T14:38:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35677",
    "user": "https://github.com/kcrisman"
}
```

Ah.  And the original posts apparently do refer only to changing for `E`.  Mike, are you saying this could cause a problem in this specific case, or only if we did it more widely?  It would be interesting to compare timings for making this change; naturally, one could potentially have a *lot* of `e^foo` in a given computation, so even microseconds spent checking whether `foo` had a `exp()` method could add up, which I think is his point... maybe?



---

archive/issue_comments_035678.json:
```json
{
    "body": "Actually, I was confused -- I was under the impression that `e` was of type `Expression`.  I'll post a patch soon.",
    "created_at": "2012-03-29T16:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35678",
    "user": "https://github.com/mwhansen"
}
```

Actually, I was confused -- I was under the impression that `e` was of type `Expression`.  I'll post a patch soon.



---

archive/issue_comments_035679.json:
```json
{
    "body": "Attachment [trac_4735.patch](tarball://root/attachments/some-uuid/ticket4735/trac_4735.patch) by @mwhansen created at 2012-05-28 07:08:26",
    "created_at": "2012-05-28T07:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35679",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4735.patch](tarball://root/attachments/some-uuid/ticket4735/trac_4735.patch) by @mwhansen created at 2012-05-28 07:08:26



---

archive/issue_comments_035680.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-28T07:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35680",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_035681.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd40.5\".",
    "created_at": "2012-05-28T07:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35681",
    "user": "https://github.com/mwhansen"
}
```

Changing keywords from "" to "sd40.5".



---

archive/issue_comments_035682.json:
```json
{
    "body": "Adds lots of examples",
    "created_at": "2012-05-28T15:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35682",
    "user": "https://github.com/kcrisman"
}
```

Adds lots of examples



---

archive/issue_comments_035683.json:
```json
{
    "body": "Attachment [trac_4735-examples.patch](tarball://root/attachments/some-uuid/ticket4735/trac_4735-examples.patch) by @kcrisman created at 2012-05-28 15:43:01\n\nThis is a **heavily** requested feature, so I've added a number of examples, as well as added the original file in question to the reference manual (though the new doc there from the first patch doesn't show up since it's in a double-underscore method).  The complex matrices were in particular demand, so thank you so much for fixing this.\n\nI've added enough that, though it passes tests, I'd appreciate a further review to make sure I didn't do something silly.  Positive review for Mike's patch.",
    "created_at": "2012-05-28T15:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35683",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_4735-examples.patch](tarball://root/attachments/some-uuid/ticket4735/trac_4735-examples.patch) by @kcrisman created at 2012-05-28 15:43:01

This is a **heavily** requested feature, so I've added a number of examples, as well as added the original file in question to the reference manual (though the new doc there from the first patch doesn't show up since it's in a double-underscore method).  The complex matrices were in particular demand, so thank you so much for fixing this.

I've added enough that, though it passes tests, I'd appreciate a further review to make sure I didn't do something silly.  Positive review for Mike's patch.



---

archive/issue_comments_035684.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-28T17:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35684",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_035685.json:
```json
{
    "body": "Karl-Dieter's patch looks good to me.",
    "created_at": "2012-05-28T17:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35685",
    "user": "https://github.com/mwhansen"
}
```

Karl-Dieter's patch looks good to me.



---

archive/issue_comments_035686.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-06-18T10:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4735#issuecomment-35686",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_004979.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-06-18T10:21:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4735",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4735#event-4979"
}
```
