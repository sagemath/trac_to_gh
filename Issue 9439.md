# Issue 9439: hyperbolic geometry

archive/issues_009439.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  kcrisman pbruin\n\nKeywords: hyperbolic geometry, Poincare disc, upper half plane\n\nImplementation of three conformal models for hyperbolic geometry (half plane, disc, hyperboloid) with actions of their isometry groups.\n\nThe actual file is almost complete for working with the hyperbolic plane as the following will plot a hyperbolic triangle\n\n```\nsage: HH.polygon(CC(0), CC(1), CC(2,2)).plot(face_color='red')\n```\n\nThere are more examples in the file.\n\n\nDepandancy:\n\n* #9076: plot arc of circles\n\nIssue created by migration from https://trac.sagemath.org/ticket/9439\n\n",
    "created_at": "2010-07-06T16:13:33Z",
    "labels": [
        "geometry",
        "major",
        "enhancement"
    ],
    "title": "hyperbolic geometry",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9439",
    "user": "vdelecroix"
}
```
Assignee: mhampton

CC:  kcrisman pbruin

Keywords: hyperbolic geometry, Poincare disc, upper half plane

Implementation of three conformal models for hyperbolic geometry (half plane, disc, hyperboloid) with actions of their isometry groups.

The actual file is almost complete for working with the hyperbolic plane as the following will plot a hyperbolic triangle

```
sage: HH.polygon(CC(0), CC(1), CC(2,2)).plot(face_color='red')
```

There are more examples in the file.


Depandancy:

* #9076: plot arc of circles

Issue created by migration from https://trac.sagemath.org/ticket/9439





---

archive/issue_comments_090362.json:
```json
{
    "body": "Attachment\n\ndraft of hyperbolic geometry space",
    "created_at": "2010-07-06T16:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90362",
    "user": "vdelecroix"
}
```

Attachment

draft of hyperbolic geometry space



---

archive/issue_comments_090363.json:
```json
{
    "body": "Changing assignee from mhampton to vdelecroix.",
    "created_at": "2010-07-06T16:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90363",
    "user": "vdelecroix"
}
```

Changing assignee from mhampton to vdelecroix.



---

archive/issue_comments_090364.json:
```json
{
    "body": "Attachment\n\nthis patch contains the previous one",
    "created_at": "2010-07-20T17:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90364",
    "user": "vdelecroix"
}
```

Attachment

this patch contains the previous one



---

archive/issue_comments_090365.json:
```json
{
    "body": "*ping* :)\n\nAre you planning on finishing this?  It would be very good to have an upper half plane implementation.  \n\nThere are a few things that need to be improved though.  Accessing attributes directly (e.g. with spam._value) is not good.  Please use accessor methods instead (i.e. a method named value() that returns _value); this improves the separation of interface and implementation.\n\nNear the real line, the hyperbolic distance becomes become HUGE compared to the Euclidean distance.  Representing a point as a complex number thus leads to numeric instability.  It is therefore better to implement a point by a pair of a matrix ((a,b),(c,d)) and a complex number z (thus representing (az+b)/(cz+d)).",
    "created_at": "2011-12-10T13:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90365",
    "user": "johanbosman"
}
```

*ping* :)

Are you planning on finishing this?  It would be very good to have an upper half plane implementation.  

There are a few things that need to be improved though.  Accessing attributes directly (e.g. with spam._value) is not good.  Please use accessor methods instead (i.e. a method named value() that returns _value); this improves the separation of interface and implementation.

Near the real line, the hyperbolic distance becomes become HUGE compared to the Euclidean distance.  Representing a point as a complex number thus leads to numeric instability.  It is therefore better to implement a point by a pair of a matrix ((a,b),(c,d)) and a complex number z (thus representing (az+b)/(cz+d)).



---

archive/issue_comments_090366.json:
```json
{
    "body": "> Are you planning on finishing this?  It would be very good to have an upper half plane implementation.  \n\nYes. But if you have time and motivation, go on. But there are problems (see below)\n\n> There are a few things that need to be improved though.  Accessing attributes directly (e.g. with spam._value) is not good.  Please use accessor methods instead (i.e. a method named value() that returns _value); this improves the separation of interface and implementation.\n\nCan be done.\n\n> Near the real line, the hyperbolic distance becomes become HUGE compared to the Euclidean distance.  Representing a point as a complex number thus leads to numeric instability.  It is therefore better to implement a point by a pair of a matrix ((a,b),(c,d)) and a complex number z (thus representing (az+b)/(cz+d)).\n\nI agree on the fact that near the real line it is unstable but disagree on the fact that we need a 5 dimensional object (an element of SL(2,R) and a complex number) to record a 2 dimensional object (a point in the half plane). The best option would be to store only the SL(2,R) matrix m such that the point is the image by z of the point i. Two matrices give the same point iff they are congruent modulo SO(2).\n\nProblems\n--------\n\n1) The main problem with that project is about of action by matrices. It would be natural that matrices act on the upper half plane. But there are many instances\n* element of ArithmeticSubgroup (SL(2,Z)) which is implemented\n* element of groups SL(2,R) or GL(2,R) or ...\n* a matrix with real coefficient\n* ...\nI had trouble with the coercion system in order to be able to use any of the type above.\n\n2) In the actual implementation, the geodesics that pass to infinity in the half plane model have an arbitrary maximum height. I did not find a good way to draw them depending on what is asked in the final .show(). In the same veine, a circle with radius 1 very near the boundary should not be drawn as it is less than one pixel...",
    "created_at": "2011-12-10T19:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90366",
    "user": "vdelecroix"
}
```

> Are you planning on finishing this?  It would be very good to have an upper half plane implementation.  

Yes. But if you have time and motivation, go on. But there are problems (see below)

> There are a few things that need to be improved though.  Accessing attributes directly (e.g. with spam._value) is not good.  Please use accessor methods instead (i.e. a method named value() that returns _value); this improves the separation of interface and implementation.

Can be done.

> Near the real line, the hyperbolic distance becomes become HUGE compared to the Euclidean distance.  Representing a point as a complex number thus leads to numeric instability.  It is therefore better to implement a point by a pair of a matrix ((a,b),(c,d)) and a complex number z (thus representing (az+b)/(cz+d)).

I agree on the fact that near the real line it is unstable but disagree on the fact that we need a 5 dimensional object (an element of SL(2,R) and a complex number) to record a 2 dimensional object (a point in the half plane). The best option would be to store only the SL(2,R) matrix m such that the point is the image by z of the point i. Two matrices give the same point iff they are congruent modulo SO(2).

Problems
--------

1) The main problem with that project is about of action by matrices. It would be natural that matrices act on the upper half plane. But there are many instances
* element of ArithmeticSubgroup (SL(2,Z)) which is implemented
* element of groups SL(2,R) or GL(2,R) or ...
* a matrix with real coefficient
* ...
I had trouble with the coercion system in order to be able to use any of the type above.

2) In the actual implementation, the geodesics that pass to infinity in the half plane model have an arbitrary maximum height. I did not find a good way to draw them depending on what is asked in the final .show(). In the same veine, a circle with radius 1 very near the boundary should not be drawn as it is less than one pixel...



---

archive/issue_comments_090367.json:
```json
{
    "body": "Replying to [comment:4 vdelecroix]:\n> \n> I agree on the fact that near the real line it is unstable but disagree on the fact that we need a 5 dimensional object (an element of SL(2,R) and a complex number) to record a 2 dimensional object (a point in the half plane). The best option would be to store only the SL(2,R) matrix m such that the point is the image by z of the point i. Two matrices give the same point iff they are congruent modulo SO(2).\n> \nOkay.  Another possibility is to have the matrix ((a, b), (c, d)) in SL_2(ZZ) and the complex number z in the standard fundamental domain for this group.  Or use both representations (and allow oneself to convert between them).",
    "created_at": "2011-12-10T21:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90367",
    "user": "johanbosman"
}
```

Replying to [comment:4 vdelecroix]:
> 
> I agree on the fact that near the real line it is unstable but disagree on the fact that we need a 5 dimensional object (an element of SL(2,R) and a complex number) to record a 2 dimensional object (a point in the half plane). The best option would be to store only the SL(2,R) matrix m such that the point is the image by z of the point i. Two matrices give the same point iff they are congruent modulo SO(2).
> 
Okay.  Another possibility is to have the matrix ((a, b), (c, d)) in SL_2(ZZ) and the complex number z in the standard fundamental domain for this group.  Or use both representations (and allow oneself to convert between them).



---

archive/issue_comments_090368.json:
```json
{
    "body": "Attachment\n\nA sketch for hyperbolic 2-space implementation.",
    "created_at": "2011-12-20T15:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90368",
    "user": "mraum"
}
```

Attachment

A sketch for hyperbolic 2-space implementation.



---

archive/issue_comments_090369.json:
```json
{
    "body": "Attachment\n\nSame patch with .py~ files removed",
    "created_at": "2011-12-20T16:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90369",
    "user": "johanbosman"
}
```

Attachment

Same patch with .py~ files removed



---

archive/issue_comments_090370.json:
```json
{
    "body": "Changing keywords from \"hyperbolic geometry, Poincare disc, upper half plane\" to \"hyperbolic geometry, Poincare disc, upper half plane, sd35\".",
    "created_at": "2011-12-20T16:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90370",
    "user": "johanbosman"
}
```

Changing keywords from "hyperbolic geometry, Poincare disc, upper half plane" to "hyperbolic geometry, Poincare disc, upper half plane, sd35".



---

archive/issue_comments_090371.json:
```json
{
    "body": "Attachment\n\nimplementations of geodesics, triangles, and polygons",
    "created_at": "2011-12-20T18:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90371",
    "user": "mraum"
}
```

Attachment

implementations of geodesics, triangles, and polygons



---

archive/issue_comments_090372.json:
```json
{
    "body": "Attachment\n\nContains (and thus replaces) previous patch",
    "created_at": "2011-12-20T23:25:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90372",
    "user": "johanbosman"
}
```

Attachment

Contains (and thus replaces) previous patch



---

archive/issue_comments_090373.json:
```json
{
    "body": "The patch I've just uploaded makes Sage import HH at startup.  I propose that we clean up all the mess first (including all the doctest failures) before we add further functionality.",
    "created_at": "2011-12-20T23:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90373",
    "user": "johanbosman"
}
```

The patch I've just uploaded makes Sage import HH at startup.  I propose that we clean up all the mess first (including all the doctest failures) before we add further functionality.



---

archive/issue_comments_090374.json:
```json
{
    "body": "Attachment\n\nSecond attempt; hopefully the point file is added. :).",
    "created_at": "2011-12-21T12:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90374",
    "user": "johanbosman"
}
```

Attachment

Second attempt; hopefully the point file is added. :).



---

archive/issue_comments_090375.json:
```json
{
    "body": "Apparently not, so let's just upload the file. :P.",
    "created_at": "2011-12-21T12:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90375",
    "user": "johanbosman"
}
```

Apparently not, so let's just upload the file. :P.



---

archive/issue_comments_090376.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-12-21T20:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90376",
    "user": "mraum"
}
```

Attachment



---

archive/issue_comments_090377.json:
```json
{
    "body": "Attachment\n\nI simply uploaded all current files, because I messed up my HG status.\n\nI couldn't fix the problem with conversion into CC, which is now #12216. I replaced it by the method toCC.\n\nI haven't checked whether triangles work, but I am exhausted. Plotting polygons works and it should be easy to fill in the tests, that are all stubs for the moment.",
    "created_at": "2011-12-21T20:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90377",
    "user": "mraum"
}
```

Attachment

I simply uploaded all current files, because I messed up my HG status.

I couldn't fix the problem with conversion into CC, which is now #12216. I replaced it by the method toCC.

I haven't checked whether triangles work, but I am exhausted. Plotting polygons works and it should be easy to fill in the tests, that are all stubs for the moment.



---

archive/issue_comments_090378.json:
```json
{
    "body": "This looks neat: I just wanted to encourage you guys to keep working on it.  I just had a request for plotting fundamental domains of congruence subgroups....",
    "created_at": "2012-07-20T19:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90378",
    "user": "roed"
}
```

This looks neat: I just wanted to encourage you guys to keep working on it.  I just had a request for plotting fundamental domains of congruence subgroups....



---

archive/issue_comments_090379.json:
```json
{
    "body": "Replying to [comment:9 roed]:\n> This looks neat: I just wanted to encourage you guys to keep working on it.  I just had a request for plotting fundamental domains of congruence subgroups....\n\nI just notice that it is yet possible to draw fundamental domain for congruence subgroups using Farey symbols (#11709, integrated since sage-5.0).\n\n\n```\nsage: FareySymbol(Gamma(3)).fundamental_domain()\n```\n",
    "created_at": "2012-07-22T00:51:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90379",
    "user": "vdelecroix"
}
```

Replying to [comment:9 roed]:
> This looks neat: I just wanted to encourage you guys to keep working on it.  I just had a request for plotting fundamental domains of congruence subgroups....

I just notice that it is yet possible to draw fundamental domain for congruence subgroups using Farey symbols (#11709, integrated since sage-5.0).


```
sage: FareySymbol(Gamma(3)).fundamental_domain()
```




---

archive/issue_comments_090380.json:
```json
{
    "body": "I have a working implementation of hyperbolic two-space in sage that includes the upper half plane, Poincare disk, Klein disk, and hyperboloid model. For each model, geodesics, points, and isometry groups are implemented. \n\nConversion between each model to another is implemented*, as are a number of useful calculation routines.  For example, geodesics can compute the corresponding reflection, two geodesics can compute their common perpendiculars, isometries can factor themselves into products of reflections.\n\nThe code originated as a series of Mathematica notebooks from Bill Goldman's lab at UMD.  We had some students port it to a sage script, which was then fleshed out.  I have refrained from publishing it here because I'm completely refactoring into something resembling readable code.  It's taken me a few month longer than I thought it would to refactor, so I wanted to write a note here so that efforts aren't redoubled.\n\nIs there a best course of action as far as posting code goes?  I think that merging the patches posted here and my code won't be too bad.  Should I finish refactoring my code first, and then post it?  Should I post the original script?  In the original code, there are lots of test and all tests pass, so it's usable.  Should I post the bit of refactoring I've done so far?\n\n*Actually, not quite.  I don't have a great way to go from SO(2,1) to SL(2,R). So this makes converting from the hyperboloid model to the other models somewhat tricky.",
    "created_at": "2012-10-07T14:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90380",
    "user": "glaun"
}
```

I have a working implementation of hyperbolic two-space in sage that includes the upper half plane, Poincare disk, Klein disk, and hyperboloid model. For each model, geodesics, points, and isometry groups are implemented. 

Conversion between each model to another is implemented*, as are a number of useful calculation routines.  For example, geodesics can compute the corresponding reflection, two geodesics can compute their common perpendiculars, isometries can factor themselves into products of reflections.

The code originated as a series of Mathematica notebooks from Bill Goldman's lab at UMD.  We had some students port it to a sage script, which was then fleshed out.  I have refrained from publishing it here because I'm completely refactoring into something resembling readable code.  It's taken me a few month longer than I thought it would to refactor, so I wanted to write a note here so that efforts aren't redoubled.

Is there a best course of action as far as posting code goes?  I think that merging the patches posted here and my code won't be too bad.  Should I finish refactoring my code first, and then post it?  Should I post the original script?  In the original code, there are lots of test and all tests pass, so it's usable.  Should I post the bit of refactoring I've done so far?

*Actually, not quite.  I don't have a great way to go from SO(2,1) to SL(2,R). So this makes converting from the hyperboloid model to the other models somewhat tricky.



---

archive/issue_comments_090381.json:
```json
{
    "body": "Hi Greg,\n\nYou should either post your code here or provide a link. If your code does work, we will definitely use it !\n\nNote that several things should be merged\n* the different code in that ticket\n* fundamental domain of FareySymbol\n* your code\n\nBest,\nVincent",
    "created_at": "2012-10-08T09:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90381",
    "user": "vdelecroix"
}
```

Hi Greg,

You should either post your code here or provide a link. If your code does work, we will definitely use it !

Note that several things should be merged
* the different code in that ticket
* fundamental domain of FareySymbol
* your code

Best,
Vincent



---

archive/issue_comments_090382.json:
```json
{
    "body": "Okay great.  I'll post it by the end of the week.  That should be enough time to clean up the remaining refactoring (which will greatly improve the ability to merge the code).",
    "created_at": "2012-10-08T12:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90382",
    "user": "glaun"
}
```

Okay great.  I'll post it by the end of the week.  That should be enough time to clean up the remaining refactoring (which will greatly improve the ability to merge the code).



---

archive/issue_comments_090383.json:
```json
{
    "body": "Obviously it's been longer than a week.  I had to attend a long conference and then hurricanes etc.  It will be at the very least another week before I get it up.",
    "created_at": "2012-11-02T19:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90383",
    "user": "glaun"
}
```

Obviously it's been longer than a week.  I had to attend a long conference and then hurricanes etc.  It will be at the very least another week before I get it up.



---

archive/issue_comments_090384.json:
```json
{
    "body": "What a mess ! can some of you say what patches have to be applied and in which order ?\n\nLet me try with just one patch:\n\napply trac_9439-hyperbolic_geometry.patch",
    "created_at": "2013-03-07T15:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90384",
    "user": "chapoton"
}
```

What a mess ! can some of you say what patches have to be applied and in which order ?

Let me try with just one patch:

apply trac_9439-hyperbolic_geometry.patch



---

archive/issue_comments_090385.json:
```json
{
    "body": "A review patch, so that tests pass. But there lacks a lot of documentation !",
    "created_at": "2013-03-15T21:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90385",
    "user": "chapoton"
}
```

A review patch, so that tests pass. But there lacks a lot of documentation !



---

archive/issue_comments_090386.json:
```json
{
    "body": "50% coverage",
    "created_at": "2013-06-05T19:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90386",
    "user": "chapoton"
}
```

50% coverage



---

archive/issue_comments_090387.json:
```json
{
    "body": "Attachment\n\n77% coverage",
    "created_at": "2013-06-10T19:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90387",
    "user": "chapoton"
}
```

Attachment

77% coverage



---

archive/issue_comments_090388.json:
```json
{
    "body": "Attachment\n\nalternative implementation of hyperbolic space",
    "created_at": "2013-06-26T06:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90388",
    "user": "glaun"
}
```

Attachment

alternative implementation of hyperbolic space



---

archive/issue_comments_090389.json:
```json
{
    "body": "demonstration of the hyperbolic geometry functionality",
    "created_at": "2013-06-26T06:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90389",
    "user": "glaun"
}
```

demonstration of the hyperbolic geometry functionality



---

archive/issue_comments_090390.json:
```json
{
    "body": "Attachment\n\nI atteched the long-overdue patch that I mentioned 9 months ago.  Sorry for the delay.  The patch has the following positive properties:\n* Hyperbolic point, geodesic, and isometry objects are implemented for each model.\n* Upper half plane, Poincare disk, Klein disk, and hyperboloid model all implemented.\n* Round-trip conversion among models works.  E.g. converting from the upper half plane to the hyperboloid and then back to the half plane gives the same point (up to numerical precision).  This was harder than might first be apparent since there are so many isomorphisms to choose from and they all have to play well together.\n* 100% test coverage, all tests pass\nAlso note the following negative things:\n* Points are not yet implemented as (point, isometry) pairs as suggested in Comment 3.\n* My handling of numerical computations could probably be significantly improved, as can the overall organization.  There may be features that are unnecessary or are vestigial from earlier versions.\n* Symbolic computations can take an incredibly long time.  I'm not sure if this is my fault (e.g. I should write functions to deal with this) or simply a drawback of allowing symbolic computations.\nI intend to comb through the previously attached patches and merge what I can.  I have also attached a filecalled hyp_demo.sage that demos the functionality of the implementation.",
    "created_at": "2013-06-26T06:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90390",
    "user": "glaun"
}
```

Attachment

I atteched the long-overdue patch that I mentioned 9 months ago.  Sorry for the delay.  The patch has the following positive properties:
* Hyperbolic point, geodesic, and isometry objects are implemented for each model.
* Upper half plane, Poincare disk, Klein disk, and hyperboloid model all implemented.
* Round-trip conversion among models works.  E.g. converting from the upper half plane to the hyperboloid and then back to the half plane gives the same point (up to numerical precision).  This was harder than might first be apparent since there are so many isomorphisms to choose from and they all have to play well together.
* 100% test coverage, all tests pass
Also note the following negative things:
* Points are not yet implemented as (point, isometry) pairs as suggested in Comment 3.
* My handling of numerical computations could probably be significantly improved, as can the overall organization.  There may be features that are unnecessary or are vestigial from earlier versions.
* Symbolic computations can take an incredibly long time.  I'm not sure if this is my fault (e.g. I should write functions to deal with this) or simply a drawback of allowing symbolic computations.
I intend to comb through the previously attached patches and merge what I can.  I have also attached a filecalled hyp_demo.sage that demos the functionality of the implementation.



---

archive/issue_comments_090391.json:
```json
{
    "body": "Replying to [comment:21 glaun]:\n> I atteched the long-overdue patch that I mentioned 9 months ago.  Sorry for the delay.  The patch has the following positive properties:\n\nGreat! Good job!\n\n> Also note the following negative things:\n> * Points are not yet implemented as (point, isometry) pairs as suggested in Comment 3.\n\nThis was a *bad* suggestion! It's great that you avoid it.\n\n> * My handling of numerical computations could probably be significantly improved, as can the overall organization.  There may be features that are unnecessary or are vestigial from earlier versions.\n\nI will have a look as soon as possible.\n\n> * Symbolic computations can take an incredibly long time.  I'm not sure if this is my fault (e.g. I should write functions to deal with this) or simply a drawback of allowing symbolic computations.\n> I intend to comb through the previously attached patches and merge what I can.  I have also attached a filecalled hyp_demo.sage that demos the functionality of the implementation.\n\nidem.\n\nTwo points:\n\n- an important feature that you seem to avoid is the unit tangent bundle of the hyperbolic plane which is isomorphic to PSL(2,R). One great thing would be to have another object `TangentVector` (with a matrix as data). The action of PSL(2,R) on the unit tangent bundle is then just matrix multiplication. \n- your example worksheet should definitely be a thematic tutorial for the Sage documentation\n\nI suggest that we open two new tickets for those features.\n\nThanks again for your work on this. I am starting the review and will be back with more technical remarks shortly.",
    "created_at": "2013-06-26T14:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90391",
    "user": "vdelecroix"
}
```

Replying to [comment:21 glaun]:
> I atteched the long-overdue patch that I mentioned 9 months ago.  Sorry for the delay.  The patch has the following positive properties:

Great! Good job!

> Also note the following negative things:
> * Points are not yet implemented as (point, isometry) pairs as suggested in Comment 3.

This was a *bad* suggestion! It's great that you avoid it.

> * My handling of numerical computations could probably be significantly improved, as can the overall organization.  There may be features that are unnecessary or are vestigial from earlier versions.

I will have a look as soon as possible.

> * Symbolic computations can take an incredibly long time.  I'm not sure if this is my fault (e.g. I should write functions to deal with this) or simply a drawback of allowing symbolic computations.
> I intend to comb through the previously attached patches and merge what I can.  I have also attached a filecalled hyp_demo.sage that demos the functionality of the implementation.

idem.

Two points:

- an important feature that you seem to avoid is the unit tangent bundle of the hyperbolic plane which is isomorphic to PSL(2,R). One great thing would be to have another object `TangentVector` (with a matrix as data). The action of PSL(2,R) on the unit tangent bundle is then just matrix multiplication. 
- your example worksheet should definitely be a thematic tutorial for the Sage documentation

I suggest that we open two new tickets for those features.

Thanks again for your work on this. I am starting the review and will be back with more technical remarks shortly.



---

archive/issue_comments_090392.json:
```json
{
    "body": "> Two points:\n> \n> - an important feature that you seem to avoid is the unit tangent bundle of the hyperbolic plane which is isomorphic to PSL(2,R). One great thing would be to have another object `TangentVector` (with a matrix as data). The action of PSL(2,R) on the unit tangent bundle is then just matrix multiplication. \n> - your example worksheet should definitely be a thematic tutorial for the Sage documentation\n\nThanks, I'll look into both of these soon.  I have some code for working in Minkowski (2,1) space that I want to use to implement the hyperboloid model in the Lie algebra sl(2,R) since that's what I use in my own research.  Several of the functions are for working in SL(2,R)/PSL(2,R).  I can take a look at that and see what can be appropriated for use in a TangentVector object.",
    "created_at": "2013-06-26T18:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90392",
    "user": "glaun"
}
```

> Two points:
> 
> - an important feature that you seem to avoid is the unit tangent bundle of the hyperbolic plane which is isomorphic to PSL(2,R). One great thing would be to have another object `TangentVector` (with a matrix as data). The action of PSL(2,R) on the unit tangent bundle is then just matrix multiplication. 
> - your example worksheet should definitely be a thematic tutorial for the Sage documentation

Thanks, I'll look into both of these soon.  I have some code for working in Minkowski (2,1) space that I want to use to implement the hyperboloid model in the Lie algebra sl(2,R) since that's what I use in my own research.  Several of the functions are for working in SL(2,R)/PSL(2,R).  I can take a look at that and see what can be appropriated for use in a TangentVector object.



---

archive/issue_comments_090393.json:
```json
{
    "body": "Hi Greg,\n\nThere are many nice features in the patch but I did not start to play with. You should start by a big clean:\n\n1) there should be no trailing whitespace\n\n2) the organization of each file should be a header which consists of a string with authors the copyright statement and then the code. There should not be several headers and copyright statements.\n\n3) all methods and functions should be commented and doctested. Running `sage -coverage` gives\n\n```\nSCORE hyperbolic_object.py: 10.0% (1 of 10)\n\nMissing documentation:\n     * line 40: def to_model(self, model)\n     * line 49: def to_UHP(self)\n     * line 52: def uhp_representation(self)\n     * line 55: def model_representation(self)\n     * line 58: def representation_in_model(self, model=None)\n     * line 96: def to_model(self, model, **options)\n     * line 108: def graphics_options(self)\n\nMissing doctests:\n     * line 33: def __init__(self, args, **graphics_options)\n     * line 88: def __init__(self, args, **graphics_options)\n```\n\n\n4) the files should be properly included in the sage documentation\n\nNow, more serious issues\n\n5) the objects from your module must be lazy imported and not imported in the global namespace (in order to not slow down sage startup)\n\n6) the method `show` should not return a graphics object but should rather shows it! You could rename it `plot`.\n\n7) I agree that it is misleading but `CC` in Sage is not the set of complex number! In particular the test `x in CC` does not answer to the question \"does my object `x` modelizes some complex number ?\". Precisely `CC` is the set of floating point complex number with 53 bits of precision. But is it on purpose that you want `x in CC` as coordinates for a point in the upper half plane ?\n\n8) The string representation \"Hyperbolic point whose representation in the Upper Half Plane is +Infinity\" is definitely too long! Why not \"Point in HH +Infinity\".\n\nAnd finally a design question (which perhaps should be thought of first)\n\n9) I think that the fact of being conformal or bounded etc is not a property of a HyperbolicObject but rather a property of the underlying model. You decided to not design a class for each model, was it on purpose? Such a class may contain all these property. As you see, in my initial patch, it was possible to write\n\n```\nsage: HH\nHyperbolic plane\nsage: HH(0)\nBoundary point 0\n```\n\nI would prefer to have a dedicated class for each model and be able to construct point/geodesic/polygons from the class (via for example ``HH.point(data)``, ``HH.geodesic(data)``, etc). You may also move the `random_element` methods and the various conversions between the models into this parent class.",
    "created_at": "2013-06-26T19:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90393",
    "user": "vdelecroix"
}
```

Hi Greg,

There are many nice features in the patch but I did not start to play with. You should start by a big clean:

1) there should be no trailing whitespace

2) the organization of each file should be a header which consists of a string with authors the copyright statement and then the code. There should not be several headers and copyright statements.

3) all methods and functions should be commented and doctested. Running `sage -coverage` gives

```
SCORE hyperbolic_object.py: 10.0% (1 of 10)

Missing documentation:
     * line 40: def to_model(self, model)
     * line 49: def to_UHP(self)
     * line 52: def uhp_representation(self)
     * line 55: def model_representation(self)
     * line 58: def representation_in_model(self, model=None)
     * line 96: def to_model(self, model, **options)
     * line 108: def graphics_options(self)

Missing doctests:
     * line 33: def __init__(self, args, **graphics_options)
     * line 88: def __init__(self, args, **graphics_options)
```


4) the files should be properly included in the sage documentation

Now, more serious issues

5) the objects from your module must be lazy imported and not imported in the global namespace (in order to not slow down sage startup)

6) the method `show` should not return a graphics object but should rather shows it! You could rename it `plot`.

7) I agree that it is misleading but `CC` in Sage is not the set of complex number! In particular the test `x in CC` does not answer to the question "does my object `x` modelizes some complex number ?". Precisely `CC` is the set of floating point complex number with 53 bits of precision. But is it on purpose that you want `x in CC` as coordinates for a point in the upper half plane ?

8) The string representation "Hyperbolic point whose representation in the Upper Half Plane is +Infinity" is definitely too long! Why not "Point in HH +Infinity".

And finally a design question (which perhaps should be thought of first)

9) I think that the fact of being conformal or bounded etc is not a property of a HyperbolicObject but rather a property of the underlying model. You decided to not design a class for each model, was it on purpose? Such a class may contain all these property. As you see, in my initial patch, it was possible to write

```
sage: HH
Hyperbolic plane
sage: HH(0)
Boundary point 0
```

I would prefer to have a dedicated class for each model and be able to construct point/geodesic/polygons from the class (via for example ``HH.point(data)``, ``HH.geodesic(data)``, etc). You may also move the `random_element` methods and the various conversions between the models into this parent class.



---

archive/issue_comments_090394.json:
```json
{
    "body": "Thanks for the feedback!  I didn't know exactly what to do about tests in what was intended to be an abstract class (hyperbeolic_object) that shouldn't be instantiated.  I see now that there are other abstract classes in sage and they all have poper doctests, so I'll go ahead and add those in.  That should be very simple, as should the rest of the cleanup.\n\nThe other issues you mentioned are all things I thought might be problems, so I've given them all a little bit of thought already\n\nReplying to [comment:24 vdelecroix]:\n\n\n> 4) the files should be properly included in the sage documentation\n\nOkay, will do.\n\n> Now, more serious issues\n> \n> 5) the objects from your module must be lazy imported and not imported in the global namespace (in order to not slow down sage startup)\n\nOkay, I will change this.\n\n> \n> 6) the method `show` should not return a graphics object but should rather shows it! You could rename it `plot`.\n\nI'm actually not quite sure what the difference is.  Do you mean that show should make a system call to the default viewer?  Is it not sufficient to call a method that makes that call for me?  I've noticed in one other module that plot() is implemented and show() is an alias for plot.  Would this be a workaround?   \n\n> 7) I agree that it is misleading but `CC` in Sage is not the set of complex number! In particular the test `x in CC` does not answer to the question \"does my object `x` modelizes some complex number ?\". Precisely `CC` is the set of floating point complex number with 53 bits of precision. But is it on purpose that you want `x in CC` as coordinates for a point in the upper half plane ?\n\nThis is a hack. I wanted a function that returned True for things that can be converted into floating point complex numbers and \"2 + I in CC\" returns True even though \"2 + I\" is a symbolic expression.  I didn't want to test more explicitly for symbolic complex numbers because I don't know the symbolic system well enough to be sure to catch all possible cases.  And I didn't want to have a test condition that relied on the symbolic apparatus because via profiling I found many cases in which calling functions that were in the symbolics library slowed everything to a crawl.  So \"x in CC\" quickly checks whether something is the right type of object to have \"imag()\" called on it sensibly.  I more than welcome suggestions on how to solve this problem more elegantly without slowing down code.  As an example, the functions _clean_points and _shorten_symbolic are both very ugly to my tastes, but I wrote each to address specific issues that arose in profiling and their impact is significant.  In a similar way, I find 'x in CC' to be unfortunate but useful.\n\n> 8) The string representation \"Hyperbolic point whose representation in the Upper Half Plane is +Infinity\" is definitely too long! Why not \"Point in HH +Infinity\".\n\nThe long strings were a request, and I agree they're much too long.  I'll go ahead and change them.  I'd like them to contain information about the model, though so that there is less confusion when performing conversion. \n \n> And finally a design question (which perhaps should be thought of first)\n> \n> 9) I think that the fact of being conformal or bounded etc is not a property of a HyperbolicObject but rather a property of the underlying model. You decided to not design a class for each model, was it on purpose? Such a class may contain all these property. As you see, in my initial patch, it was possible to write\n> {{{\n> sage: HH\n> Hyperbolic plane\n> sage: HH(0)\n> Boundary point 0\n> }}}\n> I would prefer to have a dedicated class for each model and be able to construct point/geodesic/polygons from the class (via for example ``HH.point(data)``, ``HH.geodesic(data)``, etc). You may also move the `random_element` methods and the various conversions between the models into this parent class.\n\nI think your way of doing it sounds  much better than mine. I had actually been planning on looking more closely at your structure and applying it to mine as a next step.  I'll look into this starting tomorrow.",
    "created_at": "2013-06-27T04:35:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90394",
    "user": "glaun"
}
```

Thanks for the feedback!  I didn't know exactly what to do about tests in what was intended to be an abstract class (hyperbeolic_object) that shouldn't be instantiated.  I see now that there are other abstract classes in sage and they all have poper doctests, so I'll go ahead and add those in.  That should be very simple, as should the rest of the cleanup.

The other issues you mentioned are all things I thought might be problems, so I've given them all a little bit of thought already

Replying to [comment:24 vdelecroix]:


> 4) the files should be properly included in the sage documentation

Okay, will do.

> Now, more serious issues
> 
> 5) the objects from your module must be lazy imported and not imported in the global namespace (in order to not slow down sage startup)

Okay, I will change this.

> 
> 6) the method `show` should not return a graphics object but should rather shows it! You could rename it `plot`.

I'm actually not quite sure what the difference is.  Do you mean that show should make a system call to the default viewer?  Is it not sufficient to call a method that makes that call for me?  I've noticed in one other module that plot() is implemented and show() is an alias for plot.  Would this be a workaround?   

> 7) I agree that it is misleading but `CC` in Sage is not the set of complex number! In particular the test `x in CC` does not answer to the question "does my object `x` modelizes some complex number ?". Precisely `CC` is the set of floating point complex number with 53 bits of precision. But is it on purpose that you want `x in CC` as coordinates for a point in the upper half plane ?

This is a hack. I wanted a function that returned True for things that can be converted into floating point complex numbers and "2 + I in CC" returns True even though "2 + I" is a symbolic expression.  I didn't want to test more explicitly for symbolic complex numbers because I don't know the symbolic system well enough to be sure to catch all possible cases.  And I didn't want to have a test condition that relied on the symbolic apparatus because via profiling I found many cases in which calling functions that were in the symbolics library slowed everything to a crawl.  So "x in CC" quickly checks whether something is the right type of object to have "imag()" called on it sensibly.  I more than welcome suggestions on how to solve this problem more elegantly without slowing down code.  As an example, the functions _clean_points and _shorten_symbolic are both very ugly to my tastes, but I wrote each to address specific issues that arose in profiling and their impact is significant.  In a similar way, I find 'x in CC' to be unfortunate but useful.

> 8) The string representation "Hyperbolic point whose representation in the Upper Half Plane is +Infinity" is definitely too long! Why not "Point in HH +Infinity".

The long strings were a request, and I agree they're much too long.  I'll go ahead and change them.  I'd like them to contain information about the model, though so that there is less confusion when performing conversion. 
 
> And finally a design question (which perhaps should be thought of first)
> 
> 9) I think that the fact of being conformal or bounded etc is not a property of a HyperbolicObject but rather a property of the underlying model. You decided to not design a class for each model, was it on purpose? Such a class may contain all these property. As you see, in my initial patch, it was possible to write
> {{{
> sage: HH
> Hyperbolic plane
> sage: HH(0)
> Boundary point 0
> }}}
> I would prefer to have a dedicated class for each model and be able to construct point/geodesic/polygons from the class (via for example ``HH.point(data)``, ``HH.geodesic(data)``, etc). You may also move the `random_element` methods and the various conversions between the models into this parent class.

I think your way of doing it sounds  much better than mine. I had actually been planning on looking more closely at your structure and applying it to mine as a next step.  I'll look into this starting tomorrow.



---

archive/issue_comments_090395.json:
```json
{
    "body": "Hi Vincent,\n\nI've addressed issues 1-4, and I was hoping you wouldn't mind giving me some guidance about how to handle the remaining issues.  Specifically, I have the following questions:\n\n1) Should I post a patch for the fixes of 1-4?  Or should I wait until I fix the remaining issues?  More generally, should I err on the side of posting more patches (so more people can help) or posting only ones that seem more significant?\n\n2) I like the structure of your code, and I aim to emulate it.  Does it make sense for me to combine your class structure with the features in mine and post it in skeletal form before fixing all of the functions?  For example, I could post a class diagram, or just an outline of the modules with the guts removed. Or is this step likely to be more work with little payoff?  I would ideally like the structure to be as democratically decided as possible.\n\n3) I find your usage of HyperbolicPlane for the upper half plane to be confusing since the HyperbolicDisc is also topologically a plane.  I'm used to referring to both as the hyperbolic plane, and I typically differentiate them by specifying which model of the plane.  I have been using the abbreviations UHP, PD, KM, and HM which were just decided by fiat to be short and convenient.  Is there anything you dislike about this approach to naming?  I worry that HyperbolicUHP is too cryptic, but HyperbolicUpperHalfPlane is too long.",
    "created_at": "2013-07-02T21:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90395",
    "user": "glaun"
}
```

Hi Vincent,

I've addressed issues 1-4, and I was hoping you wouldn't mind giving me some guidance about how to handle the remaining issues.  Specifically, I have the following questions:

1) Should I post a patch for the fixes of 1-4?  Or should I wait until I fix the remaining issues?  More generally, should I err on the side of posting more patches (so more people can help) or posting only ones that seem more significant?

2) I like the structure of your code, and I aim to emulate it.  Does it make sense for me to combine your class structure with the features in mine and post it in skeletal form before fixing all of the functions?  For example, I could post a class diagram, or just an outline of the modules with the guts removed. Or is this step likely to be more work with little payoff?  I would ideally like the structure to be as democratically decided as possible.

3) I find your usage of HyperbolicPlane for the upper half plane to be confusing since the HyperbolicDisc is also topologically a plane.  I'm used to referring to both as the hyperbolic plane, and I typically differentiate them by specifying which model of the plane.  I have been using the abbreviations UHP, PD, KM, and HM which were just decided by fiat to be short and convenient.  Is there anything you dislike about this approach to naming?  I worry that HyperbolicUHP is too cryptic, but HyperbolicUpperHalfPlane is too long.



---

archive/issue_comments_090396.json:
```json
{
    "body": "Hi,\n\nReplying to [comment:26 glaun]:\n> I've addressed issues 1-4, and I was hoping you wouldn't mind giving me some guidance about how to handle the remaining issues.  Specifically, I have the following questions:\n> \n> 1) Should I post a patch for the fixes of 1-4?  Or should I wait until I fix the remaining issues?  More generally, should I err on the side of posting more patches (so more people can help) or posting only ones that seem more significant?\n\nNot necessarily. You can fold your two patches into one and post only the update version of your previous patch (to fold two patches `hg qfold`).\n \n> 2) I like the structure of your code, and I aim to emulate it.  Does it make sense for me to combine your class structure with the features in mine and post it in skeletal form before fixing all of the functions?  For example, I could post a class diagram, or just an outline of the modules with the guts removed. Or is this step likely to be more work with little payoff?  I would ideally like the structure to be as democratically decided as possible.\n\nYour code definitely contains much more material than mine. If you like better the structure I drafted you are free to reuse it. If you post anything on trac it is always better that it is working code.\n\nIn my opinion, as you are currently working on that project, you may choose the datastructure you prefer and indicate **clearly** in the documentation the concept, why did you choose that design and why did you discard the other ones.\n\n> 3) I find your usage of HyperbolicPlane for the upper half plane to be confusing since the HyperbolicDisc is also topologically a plane. \n\nI agree. It was just because I always find HH and DD in textbooks and did not ask myself more questions.\n\n> I'm used to referring to both as the hyperbolic plane, and I typically differentiate them by specifying which model of the plane.  I have been using the abbreviations UHP, PD, KM, and HM which were just decided by fiat to be short and convenient.  Is there anything you dislike about this approach to naming?  I worry that HyperbolicUHP is too cryptic, but HyperbolicUpperHalfPlane is too long.\n\nI like better UHP, PD, KM and HM but I think they should not be imported in the standard namespace as such (because it is not clear how the user may find them). What about something like:\n\n```\nsage: hyperbolic_geometry.upper_half_plane()\nThe upper half plane\nsage: hyperbolic_geometry.UHP\nThe upper half plane\netc\n```\n\nThat way, we may use tab completion. But perhaps, \"hyperbolic_geometry\" is a bit too long. If somebody want it in the global namespace it is still possible to do\n\n```\nsage: from sage.XXX.hyperbolic_geometry import *\nsage: UHP\nThe upper half plane\n```\n\n\nVincent",
    "created_at": "2013-07-03T13:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90396",
    "user": "vdelecroix"
}
```

Hi,

Replying to [comment:26 glaun]:
> I've addressed issues 1-4, and I was hoping you wouldn't mind giving me some guidance about how to handle the remaining issues.  Specifically, I have the following questions:
> 
> 1) Should I post a patch for the fixes of 1-4?  Or should I wait until I fix the remaining issues?  More generally, should I err on the side of posting more patches (so more people can help) or posting only ones that seem more significant?

Not necessarily. You can fold your two patches into one and post only the update version of your previous patch (to fold two patches `hg qfold`).
 
> 2) I like the structure of your code, and I aim to emulate it.  Does it make sense for me to combine your class structure with the features in mine and post it in skeletal form before fixing all of the functions?  For example, I could post a class diagram, or just an outline of the modules with the guts removed. Or is this step likely to be more work with little payoff?  I would ideally like the structure to be as democratically decided as possible.

Your code definitely contains much more material than mine. If you like better the structure I drafted you are free to reuse it. If you post anything on trac it is always better that it is working code.

In my opinion, as you are currently working on that project, you may choose the datastructure you prefer and indicate **clearly** in the documentation the concept, why did you choose that design and why did you discard the other ones.

> 3) I find your usage of HyperbolicPlane for the upper half plane to be confusing since the HyperbolicDisc is also topologically a plane. 

I agree. It was just because I always find HH and DD in textbooks and did not ask myself more questions.

> I'm used to referring to both as the hyperbolic plane, and I typically differentiate them by specifying which model of the plane.  I have been using the abbreviations UHP, PD, KM, and HM which were just decided by fiat to be short and convenient.  Is there anything you dislike about this approach to naming?  I worry that HyperbolicUHP is too cryptic, but HyperbolicUpperHalfPlane is too long.

I like better UHP, PD, KM and HM but I think they should not be imported in the standard namespace as such (because it is not clear how the user may find them). What about something like:

```
sage: hyperbolic_geometry.upper_half_plane()
The upper half plane
sage: hyperbolic_geometry.UHP
The upper half plane
etc
```

That way, we may use tab completion. But perhaps, "hyperbolic_geometry" is a bit too long. If somebody want it in the global namespace it is still possible to do

```
sage: from sage.XXX.hyperbolic_geometry import *
sage: UHP
The upper half plane
```


Vincent



---

archive/issue_comments_090397.json:
```json
{
    "body": "Hi, just to give an update, I've completely revamped the class and module structure in a way that I like much better.  Right now only the basics of the classes are implemented, but those basics are tested and everything is in working order.  I'm now starting to add more functionality.",
    "created_at": "2013-07-30T19:44:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90397",
    "user": "glaun"
}
```

Hi, just to give an update, I've completely revamped the class and module structure in a way that I like much better.  Right now only the basics of the classes are implemented, but those basics are tested and everything is in working order.  I'm now starting to add more functionality.



---

archive/issue_comments_090398.json:
```json
{
    "body": "Updated hyperbolic space implementation.",
    "created_at": "2013-09-10T02:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90398",
    "user": "glaun"
}
```

Updated hyperbolic space implementation.



---

archive/issue_comments_090399.json:
```json
{
    "body": "Attachment\n\nI just attached a new version.  This one allows things like UHP.point(0) or KM.point((1/2, 1/2)), and similarly UHP.geodesic([start, finish]), and UHP.isometry(some_matrix).  \n\nThe class structure is somewhat complicated, but it's designed to make it easy to implement new models of 2D and 3D geometry.  Here's how it works:\n* The hyperbolic_model module contains data about each individual model, such as its name, the name of its isometry group, and dictionaries of maps to convert points and isometries to other models and so on.\n* the hyperbolic_point, hyperbolic_bdry_point, hyperbolic_geodesic, and hyperbolic_isometry modules all do what they sound like.  The methods in these modules are meant to be as general and abstract as possible.  Ideally they should barely have to be touched to implement new models of hyperbolic space.\n* hyperbolic_methods implements any methods that involve doing computations with actual numbers.  These methods have their own module because they are more likely to change if it turns out some computation is not efficient.  Also any model of hyperbolic geometry can choose to do computations in another model and convert the results.  In the current patch, every model does its computations in the upper half plane and then converts back to the desired model.  \n* hyperbolic_factory and model_factory are just factory patterns that make the whole abstract structure work.\n* finally, hyperbolic_interface is the module that contains the objects UHP, HM, KM, and PD that allow operations like UHP.point(1 + I).  These are just more pleasant user interfaces to methods in other classes.\n\nTo implement another 2D model, one mainly has to put the model information in hyperbolic_model and write down maps to all of the other models.  To implement a 3D model, one also has to implement hyperbolic_methods for at least one model (say the upper half space model).  In both cases there is a tiny amount of book keeping that must also be done in updating the factory and other modules with one or two lines of code.",
    "created_at": "2013-09-10T03:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90399",
    "user": "glaun"
}
```

Attachment

I just attached a new version.  This one allows things like UHP.point(0) or KM.point((1/2, 1/2)), and similarly UHP.geodesic([start, finish]), and UHP.isometry(some_matrix).  

The class structure is somewhat complicated, but it's designed to make it easy to implement new models of 2D and 3D geometry.  Here's how it works:
* The hyperbolic_model module contains data about each individual model, such as its name, the name of its isometry group, and dictionaries of maps to convert points and isometries to other models and so on.
* the hyperbolic_point, hyperbolic_bdry_point, hyperbolic_geodesic, and hyperbolic_isometry modules all do what they sound like.  The methods in these modules are meant to be as general and abstract as possible.  Ideally they should barely have to be touched to implement new models of hyperbolic space.
* hyperbolic_methods implements any methods that involve doing computations with actual numbers.  These methods have their own module because they are more likely to change if it turns out some computation is not efficient.  Also any model of hyperbolic geometry can choose to do computations in another model and convert the results.  In the current patch, every model does its computations in the upper half plane and then converts back to the desired model.  
* hyperbolic_factory and model_factory are just factory patterns that make the whole abstract structure work.
* finally, hyperbolic_interface is the module that contains the objects UHP, HM, KM, and PD that allow operations like UHP.point(1 + I).  These are just more pleasant user interfaces to methods in other classes.

To implement another 2D model, one mainly has to put the model information in hyperbolic_model and write down maps to all of the other models.  To implement a 3D model, one also has to implement hyperbolic_methods for at least one model (say the upper half space model).  In both cases there is a tiny amount of book keeping that must also be done in updating the factory and other modules with one or two lines of code.



---

archive/issue_comments_090400.json:
```json
{
    "body": "Updated demo of hyperbolic space.",
    "created_at": "2013-09-10T03:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90400",
    "user": "glaun"
}
```

Updated demo of hyperbolic space.



---

archive/issue_comments_090401.json:
```json
{
    "body": "Attachment\n\nI had occasion yesterday to use my most recent patch for actual computations that involve a lot of model changing, and I realized it's shamefully buggy/nonfunctioning.  I fixed a few of the obvious bugs but I'll add more tests before I repost to make sure that I haven't introduced other bugs.",
    "created_at": "2013-09-19T13:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90401",
    "user": "glaun"
}
```

Attachment

I had occasion yesterday to use my most recent patch for actual computations that involve a lot of model changing, and I realized it's shamefully buggy/nonfunctioning.  I fixed a few of the obvious bugs but I'll add more tests before I repost to make sure that I haven't introduced other bugs.



---

archive/issue_comments_090402.json:
```json
{
    "body": "Bug fixes and some new features.",
    "created_at": "2013-10-03T18:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90402",
    "user": "glaun"
}
```

Bug fixes and some new features.



---

archive/issue_comments_090403.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-11-21T00:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90403",
    "user": "glaun"
}
```

Attachment



---

archive/issue_comments_090404.json:
```json
{
    "body": "Changing keywords from \"hyperbolic geometry, Poincare disc, upper half plane, sd35\" to \"hyperbolic geometry, Poincare disc, upper half plane, Beltrami-Klein, hyperboloid model, sd35\".",
    "created_at": "2013-11-21T00:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90404",
    "user": "glaun"
}
```

Changing keywords from "hyperbolic geometry, Poincare disc, upper half plane, sd35" to "hyperbolic geometry, Poincare disc, upper half plane, Beltrami-Klein, hyperboloid model, sd35".



---

archive/issue_comments_090405.json:
```json
{
    "body": "This patch contains the previous ones as well as some changes to docstrings.",
    "created_at": "2013-11-21T01:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90405",
    "user": "glaun"
}
```

This patch contains the previous ones as well as some changes to docstrings.



---

archive/issue_comments_090406.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-11-21T01:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90406",
    "user": "glaun"
}
```

Attachment



---

archive/issue_comments_090407.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-11-21T01:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90407",
    "user": "glaun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090408.json:
```json
{
    "body": "I uploaded a new patch.  It fixes some docbuild errors that I didn't catch before.  I am marking it as needs_review because I'd like to get some feedback on it.\n\nThere are several things I'd like to add, including\n* support for polygons, circles, and horocycles\n* the ability to return the SageManifolds manifold associated with each model\n* some models of hyperbolic 3 space\nBut I'd like each of these to have their own bug report/feature request so before I do work on them I'd like to get the current patch reviewed.\n\nIf it's easier for reviewers, I can try to submit a bare-bones patch (maybe with just the upper half plane model) to reduce the number of lines of code and then add everything else in incremental patches.",
    "created_at": "2013-11-21T01:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90408",
    "user": "glaun"
}
```

I uploaded a new patch.  It fixes some docbuild errors that I didn't catch before.  I am marking it as needs_review because I'd like to get some feedback on it.

There are several things I'd like to add, including
* support for polygons, circles, and horocycles
* the ability to return the SageManifolds manifold associated with each model
* some models of hyperbolic 3 space
But I'd like each of these to have their own bug report/feature request so before I do work on them I'd like to get the current patch reviewed.

If it's easier for reviewers, I can try to submit a bare-bones patch (maybe with just the upper half plane model) to reduce the number of lines of code and then add everything else in incremental patches.



---

archive/issue_comments_090409.json:
```json
{
    "body": "New commits:",
    "created_at": "2013-11-21T16:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90409",
    "user": "pbruin"
}
```

New commits:



---

archive/issue_comments_090410.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-02-28T02:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90410",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090411.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-16T20:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90411",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090412.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-23T22:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90412",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090413.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-05-16T14:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90413",
    "user": "rws"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090414.json:
```json
{
    "body": "patchbot fails with `make doc`:\n\n```\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/index.rst:47: ERROR: Unexpected indentation.\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/index.rst:56: WARNING: Literal block ends without a blank line; unexpected unindent.\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/index.rst:56: SEVERE: Missing matching underline for section title overline.\n[geometry ] =======\n[geometry ] sage/geometry/hyperplane_arrangement/arrangement\n[geometry ] sage/geometry/hyperplane_arrangement/library\n[geometry ] /scratch/sage/local/lib/python2.7/site-packages/sage/geometry/hyperbolic_space/hyperbolic_model.py:docstring of sage.geometry.hyperbolic_space.hyperbolic_model:14: ERROR: Unexpected indentation.\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperbolic_space/hyperbolic_bdry_point.rst:: WARNING: document isn't included in any toctree\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperbolic_space/hyperbolic_geodesic.rst:: WARNING: document isn't included in any toctree\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperbolic_space/hyperbolic_interface.rst:: WARNING: document isn't included in any toctree\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperbolic_space/hyperbolic_isometry.rst:: WARNING: document isn't included in any toctree\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperbolic_space/hyperbolic_methods.rst:: WARNING: document isn't included in any toctree\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperbolic_space/hyperbolic_model.rst:: WARNING: document isn't included in any toctree\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperbolic_space/hyperbolic_point.rst:: WARNING: document isn't included in any toctree\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperplane_arrangement/affine_subspace.rst:: WARNING: document isn't included in any toctree\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperplane_arrangement/arrangement.rst:: WARNING: document isn't included in any toctree\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperplane_arrangement/hyperplane.rst:: WARNING: document isn't included in any toctree\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperplane_arrangement/library.rst:: WARNING: document isn't included in any toctree\n[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/linear_expression.rst:: WARNING: document isn't included in any toctree\nError building the documentation.\nTraceback (most recent call last):\n  File \"/scratch/sage/src/doc/common/builder.py\", line 1477, in <module>\n    getattr(get_builder(name), type)()\n  File \"/scratch/sage/src/doc/common/builder.py\", line 276, in _wrapper\n    getattr(get_builder(document), 'inventory')(*args, **kwds)\n  File \"/scratch/sage/src/doc/common/builder.py\", line 487, in _wrapper\n    x.get(99999)\n  File \"/scratch/sage/local/lib/python/multiprocessing/pool.py\", line 554, in get\n    raise self._value\nOSError: [geometry ] /scratch/sage/src/doc/en/reference/geometry/index.rst:47: ERROR: Unexpected indentation.\n\nmake: *** [doc-html] Error 1\n```\n",
    "created_at": "2014-05-16T14:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90414",
    "user": "rws"
}
```

patchbot fails with `make doc`:

```
[geometry ] /scratch/sage/src/doc/en/reference/geometry/index.rst:47: ERROR: Unexpected indentation.
[geometry ] /scratch/sage/src/doc/en/reference/geometry/index.rst:56: WARNING: Literal block ends without a blank line; unexpected unindent.
[geometry ] /scratch/sage/src/doc/en/reference/geometry/index.rst:56: SEVERE: Missing matching underline for section title overline.
[geometry ] =======
[geometry ] sage/geometry/hyperplane_arrangement/arrangement
[geometry ] sage/geometry/hyperplane_arrangement/library
[geometry ] /scratch/sage/local/lib/python2.7/site-packages/sage/geometry/hyperbolic_space/hyperbolic_model.py:docstring of sage.geometry.hyperbolic_space.hyperbolic_model:14: ERROR: Unexpected indentation.
[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperbolic_space/hyperbolic_bdry_point.rst:: WARNING: document isn't included in any toctree
[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperbolic_space/hyperbolic_geodesic.rst:: WARNING: document isn't included in any toctree
[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperbolic_space/hyperbolic_interface.rst:: WARNING: document isn't included in any toctree
[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperbolic_space/hyperbolic_isometry.rst:: WARNING: document isn't included in any toctree
[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperbolic_space/hyperbolic_methods.rst:: WARNING: document isn't included in any toctree
[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperbolic_space/hyperbolic_model.rst:: WARNING: document isn't included in any toctree
[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperbolic_space/hyperbolic_point.rst:: WARNING: document isn't included in any toctree
[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperplane_arrangement/affine_subspace.rst:: WARNING: document isn't included in any toctree
[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperplane_arrangement/arrangement.rst:: WARNING: document isn't included in any toctree
[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperplane_arrangement/hyperplane.rst:: WARNING: document isn't included in any toctree
[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/hyperplane_arrangement/library.rst:: WARNING: document isn't included in any toctree
[geometry ] /scratch/sage/src/doc/en/reference/geometry/sage/geometry/linear_expression.rst:: WARNING: document isn't included in any toctree
Error building the documentation.
Traceback (most recent call last):
  File "/scratch/sage/src/doc/common/builder.py", line 1477, in <module>
    getattr(get_builder(name), type)()
  File "/scratch/sage/src/doc/common/builder.py", line 276, in _wrapper
    getattr(get_builder(document), 'inventory')(*args, **kwds)
  File "/scratch/sage/src/doc/common/builder.py", line 487, in _wrapper
    x.get(99999)
  File "/scratch/sage/local/lib/python/multiprocessing/pool.py", line 554, in get
    raise self._value
OSError: [geometry ] /scratch/sage/src/doc/en/reference/geometry/index.rst:47: ERROR: Unexpected indentation.

make: *** [doc-html] Error 1
```




---

archive/issue_comments_090415.json:
```json
{
    "body": "here is new branch, with working doc. I have made small corrections in the doc.\n----\nNew commits:",
    "created_at": "2014-06-25T19:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90415",
    "user": "chapoton"
}
```

here is new branch, with working doc. I have made small corrections in the doc.
----
New commits:



---

archive/issue_comments_090416.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-06-25T19:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90416",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090417.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-06-26T04:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90417",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090418.json:
```json
{
    "body": "I've made some convention fixes and cleanup. I also have the following comments:\n\n- I'm not completely sure the framework that is currently there shouldn't be restructured as abstract base classes as you're not creating an army of hyperbolic spaces, just one in each type with data from a \"database\". Moreover there seems to be a lot of redundancy.\n\n- I think too much is getting imported into the global namespace (ex. `UHP`) which could have potential conflicts and in many ways is a strange acronym. It would probably be better to have them located via `HyperbolicSpace` (which would be a factory function or the base class with a `__classcall__`) and/or a catalog import `hyperbolic_space`.\n\nI will have to think more about the first one. The second should be done at some point unless there is a very good argument otherwise IMO.",
    "created_at": "2014-06-26T04:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90418",
    "user": "tscrim"
}
```

I've made some convention fixes and cleanup. I also have the following comments:

- I'm not completely sure the framework that is currently there shouldn't be restructured as abstract base classes as you're not creating an army of hyperbolic spaces, just one in each type with data from a "database". Moreover there seems to be a lot of redundancy.

- I think too much is getting imported into the global namespace (ex. `UHP`) which could have potential conflicts and in many ways is a strange acronym. It would probably be better to have them located via `HyperbolicSpace` (which would be a factory function or the base class with a `__classcall__`) and/or a catalog import `hyperbolic_space`.

I will have to think more about the first one. The second should be done at some point unless there is a very good argument otherwise IMO.



---

archive/issue_comments_090419.json:
```json
{
    "body": "I'm glad to see other people working on this ticket!  I tried to pull the updates and rebuild sage, but it won't build. It may be a few days before I have time to debug the build process and get back to work on this ticket.\n\nIn response to your points, I'm fine with a restructure as long as we talk it through first.  \n\n* Its design now uses abstract base classes for geodesics, isometries, and points.  In the current organization, the \"database\" of facts about the underlying space are in hyperbolic_model, divided by model.  The \"database\" of calculation methods are in hyperbolic_methods, of which only the methods in the upper half plane are implemented.  I think these should be separate because it allows someone to implement a model without ever having to see the details of how calculations are done. I suppose we could put the database somewhere else, like in a dictionary or database if that's wise.  I don't have strong opinions about that.  Is the organization unclear?  Let me know if you have specific ideas in mind, or even if you just want to discuss overall design philosophy.\n\n* I wasn't aware of `__classcall__` when I wrote it.  I was basically just going for doing a clean design.  It seems like `__classcall__` might be a modularity violation?  I'll look into it more.\n\n* It sounds like you're objecting to importing the interfaces into the global namespace.  I'm fine with getting rid of those imports.  We could do something like\n\n```\nUHP = HyperbolicPlane(\"upper half plane\")\nUHP.point(I)\n```\n\nand then only import HyperbolicPlane.  Is that the sort of thing you had in mind?  Or maybe something like\n\n\n```\np = HyperbolicPoint(I, \"upper half plane\") # Create point 0 + I.\n```\n",
    "created_at": "2014-06-28T12:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90419",
    "user": "glaun"
}
```

I'm glad to see other people working on this ticket!  I tried to pull the updates and rebuild sage, but it won't build. It may be a few days before I have time to debug the build process and get back to work on this ticket.

In response to your points, I'm fine with a restructure as long as we talk it through first.  

* Its design now uses abstract base classes for geodesics, isometries, and points.  In the current organization, the "database" of facts about the underlying space are in hyperbolic_model, divided by model.  The "database" of calculation methods are in hyperbolic_methods, of which only the methods in the upper half plane are implemented.  I think these should be separate because it allows someone to implement a model without ever having to see the details of how calculations are done. I suppose we could put the database somewhere else, like in a dictionary or database if that's wise.  I don't have strong opinions about that.  Is the organization unclear?  Let me know if you have specific ideas in mind, or even if you just want to discuss overall design philosophy.

* I wasn't aware of `__classcall__` when I wrote it.  I was basically just going for doing a clean design.  It seems like `__classcall__` might be a modularity violation?  I'll look into it more.

* It sounds like you're objecting to importing the interfaces into the global namespace.  I'm fine with getting rid of those imports.  We could do something like

```
UHP = HyperbolicPlane("upper half plane")
UHP.point(I)
```

and then only import HyperbolicPlane.  Is that the sort of thing you had in mind?  Or maybe something like


```
p = HyperbolicPoint(I, "upper half plane") # Create point 0 + I.
```




---

archive/issue_comments_090420.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-07-29T20:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90420",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090421.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-20T08:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90421",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090422.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-31T19:58:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90422",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090423.json:
```json
{
    "body": "Okay, so I've done a major refactoring in which I move everything into Sage's category/parent/element framework. In doing so, I figured out why all of the ``@`classmethod` bothered me (beyond the somewhat maze-like path of methods); it was emulating a singleton pattern using classes rather than instances. To me, this is a bad practice, so I'm now using `UniqueRepresentation` (although this would benefit from switching to #15247). So here's the other major points and structure.\n\n* The models are parents using the `WithRealizations` framework, and the points are the elements. I've setup the maps between the models are coercions and have methods to also translate the geodesics and isometries. Geodesics are just `SageObject`'s, but isometries are morphisms.\n* I've changed the naming of some of the methods to better reflect their operation (in particular, `orientation_preserving` to `preserves_orientation`).\n* I've kept most of the ease of implementing new models but by using the coercions instead of the methods class.\n* I've implemented a custom hash for isometries since compared equal but had different hashes.\n* More strict handling of points vs. coordinates and isometries vs. matrices. This makes the programmers/users take more care about where things belong and what one can do with them. This adds a little more burden of wrapping and unwrapping, but it shouldn't make things much (significant) difference in timings (I didn't check). Yet I would argue this is a better way of doing things.\n* Removed the `**graphic_options` from things like `perpendicular_bisector` because it seemed out of place and makes it easier to keep things consistent (plus 2 distinct steps for distinct operations).\n* There is only one big lazy import needed, and that is for `HyperbolicPlane`, which is the global entry point. I've added a method `HyperbolicSpace` for the future, but I didn't import it into the global namespace.\n\nQuestions:\n\n* If given an isometry, does one ask if it \"is orientation preserving\" or \"preserves orientation\"?\n* Should we keep with the `get_*` (ex. `get_point`) or just drop it to `*` (ex. `point` resp.)? I'm somewhat in favor of the way it is now, but I don't have a strong opinion.\n\nTodo for positive review:\n\n* Add doctests to remaining `hyperbolic_coercion.py` methods.\n* Fix doctest failures coming from `_to_std_geod`. I'm pretty sure it is not suppose to return an isometry (which is what causes the doctest failures). Please advise.\n\nTodos for the future:\n\n* Make custom endosets for each model with the isometries as elements and coercions implemented once homsets work with the coersion model (#14279 and possibly others).\n* Implement a category for metric spaces.\n\nI was quite impressed with the code and the interactions between everything and hope we can get more of (hyperbolic) geometry into Sage. So please test out, look over, and play with the refactored version (making sure everything works as before).\n\nPS - Phew, finally had some time to sit down to think and work through this. Sorry it took so long.\n----\nNew commits:",
    "created_at": "2014-09-14T07:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90423",
    "user": "tscrim"
}
```

Okay, so I've done a major refactoring in which I move everything into Sage's category/parent/element framework. In doing so, I figured out why all of the ``@`classmethod` bothered me (beyond the somewhat maze-like path of methods); it was emulating a singleton pattern using classes rather than instances. To me, this is a bad practice, so I'm now using `UniqueRepresentation` (although this would benefit from switching to #15247). So here's the other major points and structure.

* The models are parents using the `WithRealizations` framework, and the points are the elements. I've setup the maps between the models are coercions and have methods to also translate the geodesics and isometries. Geodesics are just `SageObject`'s, but isometries are morphisms.
* I've changed the naming of some of the methods to better reflect their operation (in particular, `orientation_preserving` to `preserves_orientation`).
* I've kept most of the ease of implementing new models but by using the coercions instead of the methods class.
* I've implemented a custom hash for isometries since compared equal but had different hashes.
* More strict handling of points vs. coordinates and isometries vs. matrices. This makes the programmers/users take more care about where things belong and what one can do with them. This adds a little more burden of wrapping and unwrapping, but it shouldn't make things much (significant) difference in timings (I didn't check). Yet I would argue this is a better way of doing things.
* Removed the `**graphic_options` from things like `perpendicular_bisector` because it seemed out of place and makes it easier to keep things consistent (plus 2 distinct steps for distinct operations).
* There is only one big lazy import needed, and that is for `HyperbolicPlane`, which is the global entry point. I've added a method `HyperbolicSpace` for the future, but I didn't import it into the global namespace.

Questions:

* If given an isometry, does one ask if it "is orientation preserving" or "preserves orientation"?
* Should we keep with the `get_*` (ex. `get_point`) or just drop it to `*` (ex. `point` resp.)? I'm somewhat in favor of the way it is now, but I don't have a strong opinion.

Todo for positive review:

* Add doctests to remaining `hyperbolic_coercion.py` methods.
* Fix doctest failures coming from `_to_std_geod`. I'm pretty sure it is not suppose to return an isometry (which is what causes the doctest failures). Please advise.

Todos for the future:

* Make custom endosets for each model with the isometries as elements and coercions implemented once homsets work with the coersion model (#14279 and possibly others).
* Implement a category for metric spaces.

I was quite impressed with the code and the interactions between everything and hope we can get more of (hyperbolic) geometry into Sage. So please test out, look over, and play with the refactored version (making sure everything works as before).

PS - Phew, finally had some time to sit down to think and work through this. Sorry it took so long.
----
New commits:



---

archive/issue_comments_090424.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2014-09-14T07:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90424",
    "user": "tscrim"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_090425.json:
```json
{
    "body": "Thanks for your help on the code.  I'm glad you were able to get things working with the sage parent/element/etc framework.  I wasn't quite sure how to do that.\n\nThere are still bugs that I know about and have fixed in other branches, but which haven't been merged into this branch yet.  I'll hopefully have time to commit a patch that fixes the remaining bugs that I know about in the next week or two.\n----\nNew commits:",
    "created_at": "2014-09-30T01:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90425",
    "user": "glaun"
}
```

Thanks for your help on the code.  I'm glad you were able to get things working with the sage parent/element/etc framework.  I wasn't quite sure how to do that.

There are still bugs that I know about and have fixed in other branches, but which haven't been merged into this branch yet.  I'll hopefully have time to commit a patch that fixes the remaining bugs that I know about in the next week or two.
----
New commits:



---

archive/issue_comments_090426.json:
```json
{
    "body": "Replying to [comment:54 glaun]:\n> Thanks for your help on the code.  I'm glad you were able to get things working with the sage parent/element/etc framework.  I wasn't quite sure how to do that.\n\nNot a problem. I hope a lot of the design is clear and makes sense. There's still a general question of what to do with subsets (here geodesics) of a given set (the entire plane) in terms of parents (so we can induce coercions on the subsets [geodesics]), but that is a separate, quite large, and probably thorny issue that we can't solve here.\n\n> There are still bugs that I know about and have fixed in other branches, but which haven't been merged into this branch yet.  I'll hopefully have time to commit a patch that fixes the remaining bugs that I know about in the next week or two.\n\nLet me know as things get merged in and I can review those changes so we can get this included into Sage.\n\nFYI, a typo got introduced in `c612e31`:\n\n```diff\n@@ -528,7 +528,7 @@ class HyperbolicGeodesic(SageObject):\n          \"\"\"\n          return self._cached_geodesic.reflection_involution().to_model(self._model)\n\n-     def common_perpendicular(self, other):\n+     def common_perpendicula(self, other):\n          r\"\"\"\n          Return the unique hyperbolic geodesic perpendicular to two given\n          geodesics, if such a geodesic exists. If none exists, raise a\n```\n",
    "created_at": "2014-09-30T04:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90426",
    "user": "tscrim"
}
```

Replying to [comment:54 glaun]:
> Thanks for your help on the code.  I'm glad you were able to get things working with the sage parent/element/etc framework.  I wasn't quite sure how to do that.

Not a problem. I hope a lot of the design is clear and makes sense. There's still a general question of what to do with subsets (here geodesics) of a given set (the entire plane) in terms of parents (so we can induce coercions on the subsets [geodesics]), but that is a separate, quite large, and probably thorny issue that we can't solve here.

> There are still bugs that I know about and have fixed in other branches, but which haven't been merged into this branch yet.  I'll hopefully have time to commit a patch that fixes the remaining bugs that I know about in the next week or two.

Let me know as things get merged in and I can review those changes so we can get this included into Sage.

FYI, a typo got introduced in `c612e31`:

```diff
@@ -528,7 +528,7 @@ class HyperbolicGeodesic(SageObject):
          """
          return self._cached_geodesic.reflection_involution().to_model(self._model)

-     def common_perpendicular(self, other):
+     def common_perpendicula(self, other):
          r"""
          Return the unique hyperbolic geodesic perpendicular to two given
          geodesics, if such a geodesic exists. If none exists, raise a
```




---

archive/issue_comments_090427.json:
```json
{
    "body": "Ahh, thanks for finding the typo!\n\nThe design is very clear, and it's nice to read someone's improvement of your code.  I plan to print out the code and make sure it makes sense from a bird's eye view, and to address the issue of what to do with subsets.  But that may not happen until a few weeks from now.\n\nAt present, I'm writing up a paper that uses the code, which means I'll be looking a lot at individual lines of code but not so much at organization.  Once I eliminate the remaining bugs that I've run into, I'll get to work on making the patch suitable for inclusion in Sage.\n\nThere are also some functions whose names I have always disliked -- such as _to_std_geod -- but for which I haven't yet found suitable replacements.  I'll try to clean that up too, when I'm working on making sure the parent/element architecture does everything we need it to.",
    "created_at": "2014-09-30T14:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90427",
    "user": "glaun"
}
```

Ahh, thanks for finding the typo!

The design is very clear, and it's nice to read someone's improvement of your code.  I plan to print out the code and make sure it makes sense from a bird's eye view, and to address the issue of what to do with subsets.  But that may not happen until a few weeks from now.

At present, I'm writing up a paper that uses the code, which means I'll be looking a lot at individual lines of code but not so much at organization.  Once I eliminate the remaining bugs that I've run into, I'll get to work on making the patch suitable for inclusion in Sage.

There are also some functions whose names I have always disliked -- such as _to_std_geod -- but for which I haven't yet found suitable replacements.  I'll try to clean that up too, when I'm working on making sure the parent/element architecture does everything we need it to.



---

archive/issue_comments_090428.json:
```json
{
    "body": "So what's left to review or what other bugs have you come across? Unfortunately we won't get this in 6.4, but I feel like this is very close to being done.\n\nAlso don't worry about dealing with subsets. As I mentioned, there are more general Sage design decisions that will need to be made and what we currently have is sufficient.",
    "created_at": "2014-11-03T03:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90428",
    "user": "tscrim"
}
```

So what's left to review or what other bugs have you come across? Unfortunately we won't get this in 6.4, but I feel like this is very close to being done.

Also don't worry about dealing with subsets. As I mentioned, there are more general Sage design decisions that will need to be made and what we currently have is sufficient.



---

archive/issue_comments_090429.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-11-03T15:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90429",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090430.json:
```json
{
    "body": "Sorry to have disappeared for a while.  I had an insane schedule for a few weeks.  I just pushed the latest code I have.  It passes all tests and has 100% coverage.\n\nI fixed the one major bug that I knew about.  The bug had to do with orientation-reversing isometries in the two models that use SO(2,1); namely, the hyperboloid model and the Klein disk.  I solved the problem by doing isometry multiplication in the upeer half plane model.\n----\nNew commits:\n----\nNew commits:",
    "created_at": "2014-11-03T15:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90430",
    "user": "glaun"
}
```

Sorry to have disappeared for a while.  I had an insane schedule for a few weeks.  I just pushed the latest code I have.  It passes all tests and has 100% coverage.

I fixed the one major bug that I knew about.  The bug had to do with orientation-reversing isometries in the two models that use SO(2,1); namely, the hyperboloid model and the Klein disk.  I solved the problem by doing isometry multiplication in the upeer half plane model.
----
New commits:
----
New commits:



---

archive/issue_comments_090431.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2014-11-03T19:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90431",
    "user": "tscrim"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_090432.json:
```json
{
    "body": "No worries; I completely understand (and will likely have to do the same thing shortly).\n\nSo, I've updated it to the latest develop version, fixed (trivial) doctests from that, and added full coverage to `hyperbolic_coercion.py` (which I should've done in the first place). If there are no obvious major bugs, then you can set a positive review.\n----\nNew commits:",
    "created_at": "2014-11-03T19:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90432",
    "user": "tscrim"
}
```

No worries; I completely understand (and will likely have to do the same thing shortly).

So, I've updated it to the latest develop version, fixed (trivial) doctests from that, and added full coverage to `hyperbolic_coercion.py` (which I should've done in the first place). If there are no obvious major bugs, then you can set a positive review.
----
New commits:



---

archive/issue_comments_090433.json:
```json
{
    "body": "Please remove the trailing whitespaces in:\n- `hyperbolic_geodesic.py`\n- `hyperbolic_model.py`",
    "created_at": "2014-11-07T17:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90433",
    "user": "vdelecroix"
}
```

Please remove the trailing whitespaces in:
- `hyperbolic_geodesic.py`
- `hyperbolic_model.py`



---

archive/issue_comments_090434.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-11-07T19:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90434",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090435.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-11-07T20:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90435",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090436.json:
```json
{
    "body": "Thanks Frederic. I'm happy with your changes. So then I believe the only thing left is for someone to review c5dfd89.",
    "created_at": "2014-11-14T19:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90436",
    "user": "tscrim"
}
```

Thanks Frederic. I'm happy with your changes. So then I believe the only thing left is for someone to review c5dfd89.



---

archive/issue_comments_090437.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-15T20:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90437",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090438.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-15T20:40:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90438",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090439.json:
```json
{
    "body": "I am a bit worried by the fact that some tests are longer than 1s, see\n\n```\nsage -bt --long --warn-long src/sage/geometry/hyperbolic_space/*.py\n```\n\nOtherwise, things look good.",
    "created_at": "2015-03-16T20:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90439",
    "user": "chapoton"
}
```

I am a bit worried by the fact that some tests are longer than 1s, see

```
sage -bt --long --warn-long src/sage/geometry/hyperbolic_space/*.py
```

Otherwise, things look good.



---

archive/issue_comments_090440.json:
```json
{
    "body": "Some of those breakage of pep8 was to make it more readable, but I'm not opposed to those changes. However I am happy overall with your changes, and I'm treating your comments as positive review on the previous part. Also it's okay for long tests to be longer than 1s (at least, you're testing them), but if they were not marked as `# long time`, then my philosophy is if they are longer than 2-3s on my machine, then I mark them as long.\n\nTherefore I'm going to set this to a positive review.",
    "created_at": "2015-03-16T22:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90440",
    "user": "tscrim"
}
```

Some of those breakage of pep8 was to make it more readable, but I'm not opposed to those changes. However I am happy overall with your changes, and I'm treating your comments as positive review on the previous part. Also it's okay for long tests to be longer than 1s (at least, you're testing them), but if they were not marked as `# long time`, then my philosophy is if they are longer than 2-3s on my machine, then I mark them as long.

Therefore I'm going to set this to a positive review.



---

archive/issue_comments_090441.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-03-16T22:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90441",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090442.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-03-19T03:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90442",
    "user": "vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_090443.json:
```json
{
    "body": "Changing keywords from \"hyperbolic geometry, Poincare disc, upper half plane, Beltrami-Klein, hyperboloid model, sd35\" to \"hyperbolic geometry, Poincare disc, upper half plane, Beltrami-Klein, hyperboloid model, sd35, days64\".",
    "created_at": "2015-03-19T05:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90443",
    "user": "tscrim"
}
```

Changing keywords from "hyperbolic geometry, Poincare disc, upper half plane, Beltrami-Klein, hyperboloid model, sd35" to "hyperbolic geometry, Poincare disc, upper half plane, Beltrami-Klein, hyperboloid model, sd35, days64".



---

archive/issue_comments_090444.json:
```json
{
    "body": "First off: It's very nice to see the ticket closed. :-)\n\nJust a side remark: I noticed that complex embeddings are used a lot for points (be it by using imag for boundary points or CC). Unfortunately this doesn't work for relative number fields (no support for specifying default embeddings yet). I use those to do exact calculations with hyperbolic fixed points of hecke triangle group elements. I guess I'm hoping that relative number fields will be improved. :-)",
    "created_at": "2015-03-20T20:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90444",
    "user": "jj"
}
```

First off: It's very nice to see the ticket closed. :-)

Just a side remark: I noticed that complex embeddings are used a lot for points (be it by using imag for boundary points or CC). Unfortunately this doesn't work for relative number fields (no support for specifying default embeddings yet). I use those to do exact calculations with hyperbolic fixed points of hecke triangle group elements. I guess I'm hoping that relative number fields will be improved. :-)



---

archive/issue_comments_090445.json:
```json
{
    "body": "I think it would be good to have as a follow-up being able to specify which field you want to work over (for example, the benefit of being able to specify precision). However I felt that this was a very good step forward to include into Sage (and I don't care so much about having a perfect solution at the beginning but going in steps towards the optimal solution, but perhaps I'm in the minority...).",
    "created_at": "2015-03-20T20:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90445",
    "user": "tscrim"
}
```

I think it would be good to have as a follow-up being able to specify which field you want to work over (for example, the benefit of being able to specify precision). However I felt that this was a very good step forward to include into Sage (and I don't care so much about having a perfect solution at the beginning but going in steps towards the optimal solution, but perhaps I'm in the minority...).



---

archive/issue_comments_090446.json:
```json
{
    "body": "Oh, I very much agree with going in steps and I'm glad the ticket got closed, good job! :-)\n\nAlso: The issue I mentioned is much more about (relative) number fields than this implementation (i.e. I'm off-topic and should probably have sent this to sage-devel).\n\nI guess one of the main issues is that (relative) number fields in sage are mostly \"designed\" without a fixed choice of embedding (\"they are not viewed as part of complex numbers / hyperbolic plane\"). Still they are quite important when doing arithmetic/number theory/exact calculations...\n\nEven in the absolute case a fixed field needs to be choosen for the default embedding. To make it\nwork in general one has to use something that coerces into many fields, e.g. AA/QQbar.\nSide question: Conceptually how would one organize/order the embeddings in a meaningful way? (I'm not sure how they are ordered at the moment.)\n\nThe issue with number fields also comes up when dealing with isometries/matrices over number fields and the group action...\n\n\nRegards\nJonas",
    "created_at": "2015-03-20T21:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90446",
    "user": "jj"
}
```

Oh, I very much agree with going in steps and I'm glad the ticket got closed, good job! :-)

Also: The issue I mentioned is much more about (relative) number fields than this implementation (i.e. I'm off-topic and should probably have sent this to sage-devel).

I guess one of the main issues is that (relative) number fields in sage are mostly "designed" without a fixed choice of embedding ("they are not viewed as part of complex numbers / hyperbolic plane"). Still they are quite important when doing arithmetic/number theory/exact calculations...

Even in the absolute case a fixed field needs to be choosen for the default embedding. To make it
work in general one has to use something that coerces into many fields, e.g. AA/QQbar.
Side question: Conceptually how would one organize/order the embeddings in a meaningful way? (I'm not sure how they are ordered at the moment.)

The issue with number fields also comes up when dealing with isometries/matrices over number fields and the group action...


Regards
Jonas



---

archive/issue_comments_090447.json:
```json
{
    "body": "I don't think I can answer many of those questions because my knowledge in that part of math (and definitely of Sage) is likely insufficient. I think moving this to sage-devel is the best way to get the answers you're after.",
    "created_at": "2015-03-20T21:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9439#issuecomment-90447",
    "user": "tscrim"
}
```

I don't think I can answer many of those questions because my knowledge in that part of math (and definitely of Sage) is likely insufficient. I think moving this to sage-devel is the best way to get the answers you're after.
