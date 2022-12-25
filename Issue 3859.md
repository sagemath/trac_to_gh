# Issue 3859: Line's corner_cutoff is poorly documented, and buggy

archive/issues_003859.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout @kcrisman\n\nKeywords: plot3d, Line, corner_cutoff, smoothing\n\nsage.plot.plot3d.shapes2.Line defines a corner_cutoff parameter.\n\nIt functions to smooth lines passed to it if the cosine of the angle is greater than corner_cutoff (why??? - I'm filing another ticket about this).\n\nWe want to be able to turn the smoothing of lines off, which would happen if corner_cutoff = 1 worked.\n\nExample of breakage:  (line3d calles sage.plot.plot3d.shapes2.Line)\n\n```\nline3d([[-1, 3, 369.26], [-1, -10.11, 125.33], [0.21, -10.13, 99.42]], corner_cutoff = 1)\n```\n\nA doctest sage: from sage.plot.plot3d.shapes2 import Line\n\n```\n              sage: Line([(0,0,0),(1,0,0),(2,1,0),(0,1,0)], corner_cutoff=1).corners()\n              [(0, 0, 0), (1, 0, 0), (2, 1, 0)]\n```\n\nWorks, but calling line3d or Line with these parameters fails with NoneType object unsubscriptable.\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3859\n\n",
    "created_at": "2008-08-14T22:11:31Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.1",
    "title": "Line's corner_cutoff is poorly documented, and buggy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3859",
    "user": "https://trac.sagemath.org/admin/accounts/users/mclean"
}
```
Assignee: @williamstein

CC:  @jasongrout @kcrisman

Keywords: plot3d, Line, corner_cutoff, smoothing

sage.plot.plot3d.shapes2.Line defines a corner_cutoff parameter.

It functions to smooth lines passed to it if the cosine of the angle is greater than corner_cutoff (why??? - I'm filing another ticket about this).

We want to be able to turn the smoothing of lines off, which would happen if corner_cutoff = 1 worked.

Example of breakage:  (line3d calles sage.plot.plot3d.shapes2.Line)

```
line3d([[-1, 3, 369.26], [-1, -10.11, 125.33], [0.21, -10.13, 99.42]], corner_cutoff = 1)
```

A doctest sage: from sage.plot.plot3d.shapes2 import Line

```
              sage: Line([(0,0,0),(1,0,0),(2,1,0),(0,1,0)], corner_cutoff=1).corners()
              [(0, 0, 0), (1, 0, 0), (2, 1, 0)]
```

Works, but calling line3d or Line with these parameters fails with NoneType object unsubscriptable.





Issue created by migration from https://trac.sagemath.org/ticket/3859





---

archive/issue_comments_027428.json:
```json
{
    "body": "See also the related: #3861",
    "created_at": "2008-08-14T22:28:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27428",
    "user": "https://trac.sagemath.org/admin/accounts/users/mclean"
}
```

See also the related: #3861



---

archive/issue_comments_027429.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-12-27T21:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27429",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_027430.json:
```json
{
    "body": "Here is a proposal, that corrects several minor wrong points in the code of **Line** and add more doc.\n----\nNew commits:",
    "created_at": "2014-12-27T21:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27430",
    "user": "https://github.com/fchapoton"
}
```

Here is a proposal, that corrects several minor wrong points in the code of **Line** and add more doc.
----
New commits:



---

archive/issue_comments_027431.json:
```json
{
    "body": "See also http://ask.sagemath.org/question/25609/how-to-find-the-full-argument-list-of-a-built-in-function/ - amazingly, I have never heard of this!",
    "created_at": "2015-01-27T02:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27431",
    "user": "https://github.com/kcrisman"
}
```

See also http://ask.sagemath.org/question/25609/how-to-find-the-full-argument-list-of-a-built-in-function/ - amazingly, I have never heard of this!



---

archive/issue_comments_027432.json:
```json
{
    "body": "Hello, review, anybody ?",
    "created_at": "2015-03-25T20:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27432",
    "user": "https://github.com/fchapoton"
}
```

Hello, review, anybody ?



---

archive/issue_comments_027433.json:
```json
{
    "body": "Either I don't understand the description of what `corner_cutoff` is supposed to do, or the first example from the ticket's description still doesn't work for me:\n\n```\nsage: line3d([[-1, 3, 369.26], [-1, -10.11, 125.33], [0.21, -10.13, 99.42]], corner_cutoff = 1)\n```\n\nproduces a smooth line in jmol.",
    "created_at": "2015-04-09T08:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27433",
    "user": "https://github.com/mezzarobba"
}
```

Either I don't understand the description of what `corner_cutoff` is supposed to do, or the first example from the ticket's description still doesn't work for me:

```
sage: line3d([[-1, 3, 369.26], [-1, -10.11, 125.33], [0.21, -10.13, 99.42]], corner_cutoff = 1)
```

produces a smooth line in jmol.



---

archive/issue_comments_027434.json:
```json
{
    "body": "I guess there is still a problem.",
    "created_at": "2015-04-29T12:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27434",
    "user": "https://github.com/fchapoton"
}
```

I guess there is still a problem.



---

archive/issue_comments_027435.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-04-29T12:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27435",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_027436.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-10-19T19:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27436",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_027437.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-10-19T19:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27437",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_027438.json:
```json
{
    "body": "This should be better now:\n\n`corner_cutoff = -1` : no smoothing\n\n`corner_cutoff = 1` : all points smoothed\n\nand smoothing is performed in general if the angle is close enough to pi, meaning\nthat successive segments are close to being aligned.",
    "created_at": "2015-10-19T19:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27438",
    "user": "https://github.com/fchapoton"
}
```

This should be better now:

`corner_cutoff = -1` : no smoothing

`corner_cutoff = 1` : all points smoothed

and smoothing is performed in general if the angle is close enough to pi, meaning
that successive segments are close to being aligned.



---

archive/issue_comments_027439.json:
```json
{
    "body": "ping ? should be an easy review !",
    "created_at": "2015-11-09T16:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27439",
    "user": "https://github.com/fchapoton"
}
```

ping ? should be an easy review !



---

archive/issue_comments_027440.json:
```json
{
    "body": "PING ? nobody out there ?",
    "created_at": "2015-12-14T19:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27440",
    "user": "https://github.com/fchapoton"
}
```

PING ? nobody out there ?



---

archive/issue_comments_027441.json:
```json
{
    "body": "Well, someone is out there but they don't always have time... My only Sage time has been with sagenb lately.  But I felt sorry for your ping so I try to make time tonight.\n\n\n```\nThe parameter ``corner_cutoff`` is a bound for the cosine of the\n        angle made by two successive segments. This angle is close to\n        `\\pi` if the two successive segments are almost aligned and close\n        to `0` if the path has a strong peak. \n```\n\nMaybe one could add parenthetically \"(and hence the cosine is close to 1)\" or the like as appropriate in the two places this occurs?\n\n\n```\n+        sage: N = 11\n+        sage: c = -0.4\n+        sage: sum([Line([(i,1,0), (i,0,0), (i,cos(2*pi*i/N), sin(2*pi*i/N))],\n+        ....:     corner_cutoff=c,\n+        ....:     color='red' if cos(2*pi*i/N)>=c else 'blue')\n+        ....:     for i in range(N+1)])\n```\n\nSuper-useful!  I made it into an interact to test things, very nice.\n\nI do have a question about this.  Why do you have to change the way this works?  Why not leave the bounds at 1 and -1 and not switch them?  I hate to say the magic word deprecation, and in any case this is just a flat-out change.\n\nFor instance, I would say that the angle is nearly *zero* if the segments \"keep on going\" and is close to 180 degrees if the segments change direction (peak).  So the original seems closer to my thinking - it's not the angle at the actual point of contact of the two segments, but rather the angle between the *vectors* formed by the two (directed) line segments that is in question.\n\nDoes that make sense?\n\nI also have to admit that with #3861 that the output of \n\n```\nLine([(0,0,0),(1,0,0),(2,1,0),(0,1,0)],corner_cutoff=-.5) # current ticket\n```\n\nis bizarre and does not look like the 2d version style in any case.\n\nAnyway, otherwise this seems to work as advertised.  Should end users have access to `max_len` in `Line`?  Currently I don't think that's really possible.  But maybe that's okay.",
    "created_at": "2015-12-16T03:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27441",
    "user": "https://github.com/kcrisman"
}
```

Well, someone is out there but they don't always have time... My only Sage time has been with sagenb lately.  But I felt sorry for your ping so I try to make time tonight.


```
The parameter ``corner_cutoff`` is a bound for the cosine of the
        angle made by two successive segments. This angle is close to
        `\pi` if the two successive segments are almost aligned and close
        to `0` if the path has a strong peak. 
```

Maybe one could add parenthetically "(and hence the cosine is close to 1)" or the like as appropriate in the two places this occurs?


```
+        sage: N = 11
+        sage: c = -0.4
+        sage: sum([Line([(i,1,0), (i,0,0), (i,cos(2*pi*i/N), sin(2*pi*i/N))],
+        ....:     corner_cutoff=c,
+        ....:     color='red' if cos(2*pi*i/N)>=c else 'blue')
+        ....:     for i in range(N+1)])
```

Super-useful!  I made it into an interact to test things, very nice.

I do have a question about this.  Why do you have to change the way this works?  Why not leave the bounds at 1 and -1 and not switch them?  I hate to say the magic word deprecation, and in any case this is just a flat-out change.

For instance, I would say that the angle is nearly *zero* if the segments "keep on going" and is close to 180 degrees if the segments change direction (peak).  So the original seems closer to my thinking - it's not the angle at the actual point of contact of the two segments, but rather the angle between the *vectors* formed by the two (directed) line segments that is in question.

Does that make sense?

I also have to admit that with #3861 that the output of 

```
Line([(0,0,0),(1,0,0),(2,1,0),(0,1,0)],corner_cutoff=-.5) # current ticket
```

is bizarre and does not look like the 2d version style in any case.

Anyway, otherwise this seems to work as advertised.  Should end users have access to `max_len` in `Line`?  Currently I don't think that's really possible.  But maybe that's okay.



---

archive/issue_comments_027442.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-12-20T20:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27442",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_027443.json:
```json
{
    "body": "Thanks for having a look. I know well that time is precious.\n\nI have now, as required, changed back to the original convention that angle 0 means that\nthe path goes straight. I hope I have made no error in doing that.\n\nMaybe this is good enough, for a 7 years old ticket ?",
    "created_at": "2015-12-20T20:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27443",
    "user": "https://github.com/fchapoton"
}
```

Thanks for having a look. I know well that time is precious.

I have now, as required, changed back to the original convention that angle 0 means that
the path goes straight. I hope I have made no error in doing that.

Maybe this is good enough, for a 7 years old ticket ?



---

archive/issue_comments_027444.json:
```json
{
    "body": "***ping*** ?",
    "created_at": "2016-01-21T20:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27444",
    "user": "https://github.com/fchapoton"
}
```

***ping*** ?



---

archive/issue_comments_027445.json:
```json
{
    "body": "This LGTM, but I'd like to see if Karl-Dieter has any more comments before we set this to a positive review.",
    "created_at": "2016-01-21T22:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27445",
    "user": "https://github.com/tscrim"
}
```

This LGTM, but I'd like to see if Karl-Dieter has any more comments before we set this to a positive review.



---

archive/issue_comments_027446.json:
```json
{
    "body": "If Travis can confirm that the original convention is now followed and that the awesome examples still look as they should, please do put it to positive!  I just continue to have no time for anything involving branches :( somehow that takes me much more time than e.g. reporting tickets.",
    "created_at": "2016-01-22T00:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27446",
    "user": "https://github.com/kcrisman"
}
```

If Travis can confirm that the original convention is now followed and that the awesome examples still look as they should, please do put it to positive!  I just continue to have no time for anything involving branches :( somehow that takes me much more time than e.g. reporting tickets.



---

archive/issue_comments_027447.json:
```json
{
    "body": "AFAIK it is correct. At the very least, it is better than the current behavior of erroring out.",
    "created_at": "2016-01-22T02:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27447",
    "user": "https://github.com/tscrim"
}
```

AFAIK it is correct. At the very least, it is better than the current behavior of erroring out.



---

archive/issue_comments_027448.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-01-22T02:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27448",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_027449.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-01-23T20:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3859#issuecomment-27449",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_004082.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2016-01-23T20:42:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3859",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3859#event-4082"
}
```
