# Issue 4530: Implement plots with logarithmic scale

archive/issues_004530.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: plot log scale\n\nCurrently plot() has no option to use logarithmic scales.\n\nOne workaround is to use matplotlib directly, with its semilogy(), semilogx() and loglog() functions, but that wouldn't produce plots with the customisations implemented in sage.\nAnother workaround is messing with the plot figure like:\n\n\n```python\nimport pylab\np=plot(x,marker='.')\nf=pylab.figure()\nf.gca().set_xscale('log')\np.save(figure=f)\n```\n\n\nBut that creates two problems:\n\n* The first problem is that the adaptive choosing of points just considers linear scale, so the points get too much spaced apart in the beginning of the plot and too close in the end.\n* The second problem relates to the axis, which, for the same reason, isn't located right.\n\nAlso, this requires the user to know how to deal with figures, which is not directly exposed by sage.\n\nThere are some possibilities to fix that:\n1. Make plot() detect if the figure changes the scales and modify the adaptive algorithm and the axis codes accordingly\n2. Create a kwarg to tell plot() to implement the scale-change internally\n3. Create other functions to use loglog(), semilogx() and semilogy()\n4. Many (or all) of the above together, since they aren't mutually exclusive\n\nFrom what I noticed, Mathematica implements the separate functions way, but it may be better to fix the issue in plot() itself and if the other functions are wanted, just make it so that they call plot() with the correct arguments\n\nIssue created by migration from https://trac.sagemath.org/ticket/4530\n\n",
    "created_at": "2008-11-15T19:01:25Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "Implement plots with logarithmic scale",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4530",
    "user": "ronanpaixao"
}
```
Assignee: somebody

Keywords: plot log scale

Currently plot() has no option to use logarithmic scales.

One workaround is to use matplotlib directly, with its semilogy(), semilogx() and loglog() functions, but that wouldn't produce plots with the customisations implemented in sage.
Another workaround is messing with the plot figure like:


```python
import pylab
p=plot(x,marker='.')
f=pylab.figure()
f.gca().set_xscale('log')
p.save(figure=f)
```


But that creates two problems:

* The first problem is that the adaptive choosing of points just considers linear scale, so the points get too much spaced apart in the beginning of the plot and too close in the end.
* The second problem relates to the axis, which, for the same reason, isn't located right.

Also, this requires the user to know how to deal with figures, which is not directly exposed by sage.

There are some possibilities to fix that:
1. Make plot() detect if the figure changes the scales and modify the adaptive algorithm and the axis codes accordingly
2. Create a kwarg to tell plot() to implement the scale-change internally
3. Create other functions to use loglog(), semilogx() and semilogy()
4. Many (or all) of the above together, since they aren't mutually exclusive

From what I noticed, Mathematica implements the separate functions way, but it may be better to fix the issue in plot() itself and if the other functions are wanted, just make it so that they call plot() with the correct arguments

Issue created by migration from https://trac.sagemath.org/ticket/4530





---

archive/issue_comments_033745.json:
```json
{
    "body": "\"Wrong\" sage plot with log scale",
    "created_at": "2008-11-15T19:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4530#issuecomment-33745",
    "user": "ronanpaixao"
}
```

"Wrong" sage plot with log scale



---

archive/issue_comments_033746.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-11-15T19:03:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4530#issuecomment-33746",
    "user": "ronanpaixao"
}
```

Resolution: duplicate



---

archive/issue_comments_033747.json:
```json
{
    "body": "Attachment [sage0.png](tarball://root/attachments/some-uuid/ticket4530/sage0.png) by ronanpaixao created at 2008-11-15 19:03:48\n\nDuplicate of bug #4529 (Submitted two times)",
    "created_at": "2008-11-15T19:03:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4530#issuecomment-33747",
    "user": "ronanpaixao"
}
```

Attachment [sage0.png](tarball://root/attachments/some-uuid/ticket4530/sage0.png) by ronanpaixao created at 2008-11-15 19:03:48

Duplicate of bug #4529 (Submitted two times)
