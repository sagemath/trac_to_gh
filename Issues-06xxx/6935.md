# Issue 6935: Improve documentation for plots with new axis code

archive/issues_006935.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout\n\nThere are a few issues that are left over from #5448, which at the very least should be documented.  None of them are major.\n\nContour plot - if fill=False and contours are grayscale, the axes could be misinterpreted\n\nContour plot - show(axes=False) and show(axes=True) seem to be identical on the last example\n\nPlotting - how well documented is the new axis behavior, where it does NOT intersect? This should be clear, e.g. the Riemann zeta example in plot.py looks funny, until you realize it's from 1 to 27. It still seems weird to me when it's that close, but I suppose it's okay as long as it is very very clear in documentation.\n\nAxis labels - should point out difference between ['x','y'] and ['$x$','$y$']. Some people might not like the LaTeXed? version\n\nWhen scientific notation comes into play is not always clear, and should be in the documentation - compare plot(x**2, 490,500) and plot(x**2,-490,500), which have the same \"height\" but only one gets e, presumably since it covers a larger range\n\nIssue created by migration from https://trac.sagemath.org/ticket/6935\n\n",
    "closed_at": "2009-10-19T05:56:45Z",
    "created_at": "2009-09-15T17:39:04Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "Improve documentation for plots with new axis code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6935",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @williamstein

CC:  @jasongrout

There are a few issues that are left over from #5448, which at the very least should be documented.  None of them are major.

Contour plot - if fill=False and contours are grayscale, the axes could be misinterpreted

Contour plot - show(axes=False) and show(axes=True) seem to be identical on the last example

Plotting - how well documented is the new axis behavior, where it does NOT intersect? This should be clear, e.g. the Riemann zeta example in plot.py looks funny, until you realize it's from 1 to 27. It still seems weird to me when it's that close, but I suppose it's okay as long as it is very very clear in documentation.

Axis labels - should point out difference between ['x','y'] and ['$x$','$y$']. Some people might not like the LaTeXed? version

When scientific notation comes into play is not always clear, and should be in the documentation - compare plot(x**2, 490,500) and plot(x**2,-490,500), which have the same "height" but only one gets e, presumably since it covers a larger range

Issue created by migration from https://trac.sagemath.org/ticket/6935





---

archive/issue_comments_057209.json:
```json
{
    "body": "The first issue is dealt with in #6996, but needed a bit more documentation.  The second issue turned out not to be an issue.\n\nOtherwise documentation has been updated for all these things as appropriate.",
    "created_at": "2009-10-05T18:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6935#issuecomment-57209",
    "user": "https://github.com/kcrisman"
}
```

The first issue is dealt with in #6996, but needed a bit more documentation.  The second issue turned out not to be an issue.

Otherwise documentation has been updated for all these things as appropriate.



---

archive/issue_comments_057210.json:
```json
{
    "body": "Attachment [trac_6935-mpl-upgrade-documentation.patch](tarball://root/attachments/some-uuid/ticket6935/trac_6935-mpl-upgrade-documentation.patch) by @kcrisman created at 2009-10-05 18:05:18\n\nBased on 4.1.2.alpha4",
    "created_at": "2009-10-05T18:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6935#issuecomment-57210",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_6935-mpl-upgrade-documentation.patch](tarball://root/attachments/some-uuid/ticket6935/trac_6935-mpl-upgrade-documentation.patch) by @kcrisman created at 2009-10-05 18:05:18

Based on 4.1.2.alpha4



---

archive/issue_comments_057211.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-06T20:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6935#issuecomment-57211",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057212.json:
```json
{
    "body": "Looks great!",
    "created_at": "2009-10-06T20:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6935#issuecomment-57212",
    "user": "https://github.com/jasongrout"
}
```

Looks great!



---

archive/issue_events_016316.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2009-10-06T20:49:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6935",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6935#event-16316"
}
```



---

archive/issue_comments_057213.json:
```json
{
    "body": "When we merged #6996, it was understood that this documentation should make it into the same release so that people wouldn't be really confused by the new axes behavior.",
    "created_at": "2009-10-06T20:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6935#issuecomment-57213",
    "user": "https://github.com/jasongrout"
}
```

When we merged #6996, it was understood that this documentation should make it into the same release so that people wouldn't be really confused by the new axes behavior.



---

archive/issue_comments_057214.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-19T05:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6935#issuecomment-57214",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_016317.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-19T05:56:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6935",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6935#event-16317"
}
```
