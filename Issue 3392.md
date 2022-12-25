# Issue 3392: upgrade matplotlib to 0.98.0 release

archive/issues_003392.json:
```json
{
    "body": "Assignee: mabshoff\n\nmatplotlib 0.98.0 is a major release which requires python2.4 and numpy 1.1. It contains significant improvements and may require some advanced users to update their code; see migration and API_CHANGES. We are supporting a maintenance \n\nIssue created by migration from https://trac.sagemath.org/ticket/3392\n\n",
    "created_at": "2008-06-10T19:08:37Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "upgrade matplotlib to 0.98.0 release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3392",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

matplotlib 0.98.0 is a major release which requires python2.4 and numpy 1.1. It contains significant improvements and may require some advanced users to update their code; see migration and API_CHANGES. We are supporting a maintenance 

Issue created by migration from https://trac.sagemath.org/ticket/3392





---

archive/issue_comments_023708.json:
```json
{
    "body": "I think we need to upgrade to numpy 1.1.0 and do this upgrade simultaneously.  I think they each require the other.",
    "created_at": "2008-07-14T20:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3392#issuecomment-23708",
    "user": "https://github.com/jasongrout"
}
```

I think we need to upgrade to numpy 1.1.0 and do this upgrade simultaneously.  I think they each require the other.



---

archive/issue_comments_023709.json:
```json
{
    "body": "(see #3390 for the numpy 1.1.0 upgrade spkg).",
    "created_at": "2008-07-14T20:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3392#issuecomment-23709",
    "user": "https://github.com/jasongrout"
}
```

(see #3390 for the numpy 1.1.0 upgrade spkg).



---

archive/issue_comments_023710.json:
```json
{
    "body": "matplotlib-sage.patch is (at least part of) what is needed to get sage to work with matplotlib 0.98;  (they renamed matplotlib.patches.lines to matplotlib.lines).\n\nIgnore matplotlib-sage.2.patch.",
    "created_at": "2008-07-20T23:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3392#issuecomment-23710",
    "user": "https://github.com/timabbott"
}
```

matplotlib-sage.patch is (at least part of) what is needed to get sage to work with matplotlib 0.98;  (they renamed matplotlib.patches.lines to matplotlib.lines).

Ignore matplotlib-sage.2.patch.



---

archive/issue_comments_023711.json:
```json
{
    "body": "We might as well upgrade to matplotlib 0.98.3 now.",
    "created_at": "2008-08-15T13:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3392#issuecomment-23711",
    "user": "https://github.com/jasongrout"
}
```

We might as well upgrade to matplotlib 0.98.3 now.



---

archive/issue_comments_023712.json:
```json
{
    "body": "Apply instead of above",
    "created_at": "2008-08-21T22:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3392#issuecomment-23712",
    "user": "https://github.com/jasongrout"
}
```

Apply instead of above



---

archive/issue_comments_023713.json:
```json
{
    "body": "Attachment [matplotlib-sage.3.patch](tarball://root/attachments/some-uuid/ticket3392/matplotlib-sage.3.patch) by @jasongrout created at 2008-08-21 22:28:23\n\nthe matplotlib-sage.3.patch above includes the other two patches and should be applied instead.  the .3.patch file also includes several more fixes for things added in 3.1.1.",
    "created_at": "2008-08-21T22:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3392#issuecomment-23713",
    "user": "https://github.com/jasongrout"
}
```

Attachment [matplotlib-sage.3.patch](tarball://root/attachments/some-uuid/ticket3392/matplotlib-sage.3.patch) by @jasongrout created at 2008-08-21 22:28:23

the matplotlib-sage.3.patch above includes the other two patches and should be applied instead.  the .3.patch file also includes several more fixes for things added in 3.1.1.



---

archive/issue_comments_023714.json:
```json
{
    "body": "New spkg up at http://sage.math.washington.edu/home/jason/matplotlib-0.98.3.spkg\n\nThis depends on the numpy 1.1 spkg at #3390.",
    "created_at": "2008-08-21T22:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3392#issuecomment-23714",
    "user": "https://github.com/jasongrout"
}
```

New spkg up at http://sage.math.washington.edu/home/jason/matplotlib-0.98.3.spkg

This depends on the numpy 1.1 spkg at #3390.



---

archive/issue_comments_023715.json:
```json
{
    "body": "Spkg and patch look good to me. I integrated Ondrej's fix from #3792 and did some cleanups to SPKG.txt. The new spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha1/matplotlib-0.98.3.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T09:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3392#issuecomment-23715",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Spkg and patch look good to me. I integrated Ondrej's fix from #3792 and did some cleanups to SPKG.txt. The new spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha1/matplotlib-0.98.3.p0.spkg

Cheers,

Michael



---

archive/issue_comments_023716.json:
```json
{
    "body": "We have some deprecation warning that causes a number of doctests:\n\n```\n        sage -t -long devel/sage/sage/schemes/elliptic_curves/lseries_ell.py # 1 doctests failed\n        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py # 1 doctests failed\n        sage -t -long devel/sage/sage/rings/padics/padic_base_generic.py # 1 doctests failed\n        sage -t -long devel/sage/sage/rings/polynomial/polynomial_element.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/modules/free_module_element.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/gsl/interpolation.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/gsl/fft.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/gsl/dwt.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/gsl/ode.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/plot/plot.py # 1 doctests failed\n        sage -t -long devel/sage/sage/finance/time_series.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/calculus/desolvers.py # 1 doctests failed\n```\n\nSpecifically:\n\n```\nsage -t -long devel/sage/sage/finance/time_series.pyx       \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/tmp/time_series.py\", line 926:\n    sage: v.plot(points=True)\nExpected nothing\nGot:\n    doctest:4821: DeprecationWarning: replace \"faceted=False\" with \"edgecolors='none'\"\n    <BLANKLINE>\n**********************************************************************\n```\n\nPatch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T10:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3392#issuecomment-23716",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We have some deprecation warning that causes a number of doctests:

```
        sage -t -long devel/sage/sage/schemes/elliptic_curves/lseries_ell.py # 1 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py # 1 doctests failed
        sage -t -long devel/sage/sage/rings/padics/padic_base_generic.py # 1 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/polynomial_element.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/modules/free_module_element.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/gsl/interpolation.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/gsl/fft.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/gsl/dwt.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/gsl/ode.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/plot/plot.py # 1 doctests failed
        sage -t -long devel/sage/sage/finance/time_series.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/calculus/desolvers.py # 1 doctests failed
```

Specifically:

```
sage -t -long devel/sage/sage/finance/time_series.pyx       
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/tmp/time_series.py", line 926:
    sage: v.plot(points=True)
Expected nothing
Got:
    doctest:4821: DeprecationWarning: replace "faceted=False" with "edgecolors='none'"
    <BLANKLINE>
**********************************************************************
```

Patch coming up.

Cheers,

Michael



---

archive/issue_comments_023717.json:
```json
{
    "body": "With the following code all doctests pass:\n\n```\n    def _render_on_subplot(self,subplot):\n        options = self.options()\n        c = to_mpl_color(options['rgbcolor'])\n        a = float(options['alpha'])\n        s = int(options['pointsize'])\n        scatteroptions={}\n        if not faceted: scatteroptions['edgecolors'] = 'none'\n        subplot.scatter(self.xdata, self.ydata, s=s, c=c, alpha=a, **scatteroptions)\n\n```\n",
    "created_at": "2008-08-27T11:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3392#issuecomment-23717",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With the following code all doctests pass:

```
    def _render_on_subplot(self,subplot):
        options = self.options()
        c = to_mpl_color(options['rgbcolor'])
        a = float(options['alpha'])
        s = int(options['pointsize'])
        scatteroptions={}
        if not faceted: scatteroptions['edgecolors'] = 'none'
        subplot.scatter(self.xdata, self.ydata, s=s, c=c, alpha=a, **scatteroptions)

```




---

archive/issue_comments_023718.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T12:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3392#issuecomment-23718",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003609.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-27T12:16:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3392",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3392#event-3609"
}
```



---

archive/issue_comments_023719.json:
```json
{
    "body": "Attachment [trac_3392_doctest-fix.patch](tarball://root/attachments/some-uuid/ticket3392/trac_3392_doctest-fix.patch) by mabshoff created at 2008-08-27 12:16:03\n\nMerged both patches in Sage 3.1.2.alpha1",
    "created_at": "2008-08-27T12:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3392#issuecomment-23719",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3392_doctest-fix.patch](tarball://root/attachments/some-uuid/ticket3392/trac_3392_doctest-fix.patch) by mabshoff created at 2008-08-27 12:16:03

Merged both patches in Sage 3.1.2.alpha1



---

archive/issue_comments_023720.json:
```json
{
    "body": "uh, as per mabshoff's request that I post something here, that last patch that he merged fixing the doctest looks reasonable, but I haven't actually applied it or doctested it or anything.",
    "created_at": "2008-08-27T12:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3392#issuecomment-23720",
    "user": "https://github.com/jasongrout"
}
```

uh, as per mabshoff's request that I post something here, that last patch that he merged fixing the doctest looks reasonable, but I haven't actually applied it or doctested it or anything.
