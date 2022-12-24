# Issue 2859: plotting the vector (0,0,-1) really plots (0,0,1)

archive/issues_002859.json:
```json
{
    "body": "Assignee: was\n\nTry the following:\n\n\n```\nplot(vector((0,0,-1)))\n```\n\n\nThe resulting vector points up, but should point down.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2859\n\n",
    "created_at": "2008-04-08T21:10:09Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "plotting the vector (0,0,-1) really plots (0,0,1)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2859",
    "user": "jason"
}
```
Assignee: was

Try the following:


```
plot(vector((0,0,-1)))
```


The resulting vector points up, but should point down.

Issue created by migration from https://trac.sagemath.org/ticket/2859





---

archive/issue_comments_019615.json:
```json
{
    "body": "The problem is in arrow3d:\n\n\n```\nsage: arrow3d((0,0,0), (0,0,-1))\n*points up*\n```\n",
    "created_at": "2008-04-08T21:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2859#issuecomment-19615",
    "user": "jason"
}
```

The problem is in arrow3d:


```
sage: arrow3d((0,0,0), (0,0,-1))
*points up*
```




---

archive/issue_comments_019616.json:
```json
{
    "body": "All right, this was because we were taking the cross product with (0,0,1) and using that to decide whether or not to rotate the vector, ignoring the case that we point in the opposite direction (but still have a cross product of zero).\n\nPatch will be attached.  I'm marking this a blocker since it gives a *wrong* result and William said that wrong results should be marked as blockers.",
    "created_at": "2008-04-08T22:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2859#issuecomment-19616",
    "user": "jason"
}
```

All right, this was because we were taking the cross product with (0,0,1) and using that to decide whether or not to rotate the vector, ignoring the case that we point in the opposite direction (but still have a cross product of zero).

Patch will be attached.  I'm marking this a blocker since it gives a *wrong* result and William said that wrong results should be marked as blockers.



---

archive/issue_comments_019617.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-04-08T22:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2859#issuecomment-19617",
    "user": "jason"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_019618.json:
```json
{
    "body": "Jason,\n\nhow does this ticket related to #1777? [also opened by you]\n\nCheers,\n\nMichael",
    "created_at": "2008-04-09T01:22:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2859#issuecomment-19618",
    "user": "mabshoff"
}
```

Jason,

how does this ticket related to #1777? [also opened by you]

Cheers,

Michael



---

archive/issue_comments_019619.json:
```json
{
    "body": "It doesn't relate.  \n\nIn this ticket, the arrow is actually wrong (the assumption in the code is that \"parallel to (0,0,1)\" == \"pointing in the same direction as (0,0,1)\", which is just wrong.\n\nThe issue in #1777 is a cosmetic issue related to the menus in JMOL.",
    "created_at": "2008-04-09T01:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2859#issuecomment-19619",
    "user": "jason"
}
```

It doesn't relate.  

In this ticket, the arrow is actually wrong (the assumption in the code is that "parallel to (0,0,1)" == "pointing in the same direction as (0,0,1)", which is just wrong.

The issue in #1777 is a cosmetic issue related to the menus in JMOL.



---

archive/issue_comments_019620.json:
```json
{
    "body": "The patch works as advertised and the code looks good to me. Positive review for the code, and I'll give it full positive review once you sort out this minor complaint about the doctest: instead of \"A downward pointing arrow should have a transformation scaling the points to their negatives\" do you mean to say something like \"a downward-pointing arrow *corresponds* to a transformation *which reverses the z-coordinates* of points\"?\n\nMostly I'm confused because when you give me a vector in R<sup>3</sup> and ask me what linear transformation of R<sup>3</sup> to itself that it's describing, I naturally think of reflection across the perpendicular plane. The vector (0,0,-1) doesn't say \"take (x,y,z) to (-x,-y,-z)\" to me...but maybe this is just me, and perhaps it's more an issue with `get_transformation` than with `arrow3d`.\n\nAt any rate, if you're a bit more clear in that description, you'll be good to go.",
    "created_at": "2008-04-09T07:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2859#issuecomment-19620",
    "user": "ddrake"
}
```

The patch works as advertised and the code looks good to me. Positive review for the code, and I'll give it full positive review once you sort out this minor complaint about the doctest: instead of "A downward pointing arrow should have a transformation scaling the points to their negatives" do you mean to say something like "a downward-pointing arrow *corresponds* to a transformation *which reverses the z-coordinates* of points"?

Mostly I'm confused because when you give me a vector in R<sup>3</sup> and ask me what linear transformation of R<sup>3</sup> to itself that it's describing, I naturally think of reflection across the perpendicular plane. The vector (0,0,-1) doesn't say "take (x,y,z) to (-x,-y,-z)" to me...but maybe this is just me, and perhaps it's more an issue with `get_transformation` than with `arrow3d`.

At any rate, if you're a bit more clear in that description, you'll be good to go.



---

archive/issue_comments_019621.json:
```json
{
    "body": "Arrows are always constructed pointing up in the z direction from the origin, and then rotated/translated into place.  This works for every arrow direction except the -z direction.  I take care of the issue by testing to see if the arrow should point in the -z direction, and if it should, just scaling the constructed arrow by -1 (i.e., every point is sent to its negative).  The scaled arrow then points downwards.  The doctest just tests that the scale of -1 is applied to the arrow.  I'm not sure how to make it clearer.",
    "created_at": "2008-04-09T08:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2859#issuecomment-19621",
    "user": "jason"
}
```

Arrows are always constructed pointing up in the z direction from the origin, and then rotated/translated into place.  This works for every arrow direction except the -z direction.  I take care of the issue by testing to see if the arrow should point in the -z direction, and if it should, just scaling the constructed arrow by -1 (i.e., every point is sent to its negative).  The scaled arrow then points downwards.  The doctest just tests that the scale of -1 is applied to the arrow.  I'm not sure how to make it clearer.



---

archive/issue_comments_019622.json:
```json
{
    "body": "Attachment [trac-2859-arrow3d.patch](tarball://root/attachments/some-uuid/ticket2859/trac-2859-arrow3d.patch) by jason created at 2008-04-09 08:53:34\n\nI put up a new patch with the above explanation above the doctest.",
    "created_at": "2008-04-09T08:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2859#issuecomment-19622",
    "user": "jason"
}
```

Attachment [trac-2859-arrow3d.patch](tarball://root/attachments/some-uuid/ticket2859/trac-2859-arrow3d.patch) by jason created at 2008-04-09 08:53:34

I put up a new patch with the above explanation above the doctest.



---

archive/issue_comments_019623.json:
```json
{
    "body": "Looks good to me. I like the added explanation. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-09T09:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2859#issuecomment-19623",
    "user": "mabshoff"
}
```

Looks good to me. I like the added explanation. Positive review.

Cheers,

Michael



---

archive/issue_comments_019624.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-09T10:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2859#issuecomment-19624",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019625.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-09T10:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2859#issuecomment-19625",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha3
