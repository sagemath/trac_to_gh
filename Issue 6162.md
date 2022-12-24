# Issue 6162: plot_histogram improvments

archive/issues_006162.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  cswiercz\n\nSince R's histogram plotting is not working for me, I added some functionality to dft.py's plot_histogram method for IndexedSequences.\nHope this is useful to other.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6162\n\n",
    "created_at": "2009-05-30T22:16:10Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "plot_histogram improvments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6162",
    "user": "wdj"
}
```
Assignee: tbd

CC:  cswiercz

Since R's histogram plotting is not working for me, I added some functionality to dft.py's plot_histogram method for IndexedSequences.
Hope this is useful to other.

Issue created by migration from https://trac.sagemath.org/ticket/6162





---

archive/issue_comments_049144.json:
```json
{
    "body": "Attachment [trac_6162-histogram.patch](tarball://root/attachments/some-uuid/ticket6162/trac_6162-histogram.patch) by wdj created at 2009-05-30 22:20:45\n\nbased on 4.0.rc1",
    "created_at": "2009-05-30T22:20:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49144",
    "user": "wdj"
}
```

Attachment [trac_6162-histogram.patch](tarball://root/attachments/some-uuid/ticket6162/trac_6162-histogram.patch) by wdj created at 2009-05-30 22:20:45

based on 4.0.rc1



---

archive/issue_comments_049145.json:
```json
{
    "body": "This passes sage -testall on an amd64 ubuntu 9.04 machine.",
    "created_at": "2009-05-31T01:42:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49145",
    "user": "wdj"
}
```

This passes sage -testall on an amd64 ubuntu 9.04 machine.



---

archive/issue_comments_049146.json:
```json
{
    "body": "Changing component from algebra to graphics.",
    "created_at": "2009-06-01T03:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49146",
    "user": "wdj"
}
```

Changing component from algebra to graphics.



---

archive/issue_comments_049147.json:
```json
{
    "body": "Changing assignee from tbd to was.",
    "created_at": "2009-06-01T03:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49147",
    "user": "wdj"
}
```

Changing assignee from tbd to was.



---

archive/issue_comments_049148.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-06-01T03:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49148",
    "user": "wdj"
}
```

Changing priority from major to minor.



---

archive/issue_comments_049149.json:
```json
{
    "body": "Original patch was not great; this one is more configurable, fixes a bug in the plot command, and fixes some of the zillion typos throughout.\n\nwdj, ispell-comments-and-strings in emacs is your friend.  That and flyspell-mode.",
    "created_at": "2009-06-15T19:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49149",
    "user": "ncalexan"
}
```

Original patch was not great; this one is more configurable, fixes a bug in the plot command, and fixes some of the zillion typos throughout.

wdj, ispell-comments-and-strings in emacs is your friend.  That and flyspell-mode.



---

archive/issue_comments_049150.json:
```json
{
    "body": "Changing keywords from \"\" to \"plot histogram\".",
    "created_at": "2009-06-15T19:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49150",
    "user": "ncalexan"
}
```

Changing keywords from "" to "plot histogram".



---

archive/issue_comments_049151.json:
```json
{
    "body": "Attachment [trac_6162-plotting.patch](tarball://root/attachments/some-uuid/ticket6162/trac_6162-plotting.patch) by wdj created at 2009-06-15 20:35:28\n\nThanks Nick!\n\nShould I review your patches or does someone other than the 2 of us review both patches?",
    "created_at": "2009-06-15T20:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49151",
    "user": "wdj"
}
```

Attachment [trac_6162-plotting.patch](tarball://root/attachments/some-uuid/ticket6162/trac_6162-plotting.patch) by wdj created at 2009-06-15 20:35:28

Thanks Nick!

Should I review your patches or does someone other than the 2 of us review both patches?



---

archive/issue_comments_049152.json:
```json
{
    "body": "Nick,\n\nI have very bad luck with your patches. :( Is `trac_6162-plotting.patch` also based on 4.0.rc1? I tried applying it to 4.0.2 after successfully applying `trac_6162-histogram.patch` and I received the following error:\n\n\n```\nsage: hg_sage.apply(\"trac_6162-plotting.patch\")\ncd \"/home/cswiercz/sage/devel/sage\" && hg status\ncd \"/home/cswiercz/sage/devel/sage\" && hg status\ncd \"/home/cswiercz/sage/devel/sage\" && hg import   \"/home/cswiercz/trac_6162-plotting.patch\"\napplying /home/cswiercz/trac_6162-plotting.patch\npatching file sage/gsl/dft.py\nHunk #2 FAILED at 52\nHunk #3 FAILED at 156\n2 out of 4 hunks FAILED -- saving rejects to file sage/gsl/dft.py.rej\nabort: patch failed to apply\n```\n\n\nThis was done on a local sage.math install. I wonder if there were changes to `sage/gsl/dft.py` between the two versions...\n\nI don't have a 4.0.rc1 install anywhere so I'll have to get that up and running in order to review.",
    "created_at": "2009-06-23T16:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49152",
    "user": "cswiercz"
}
```

Nick,

I have very bad luck with your patches. :( Is `trac_6162-plotting.patch` also based on 4.0.rc1? I tried applying it to 4.0.2 after successfully applying `trac_6162-histogram.patch` and I received the following error:


```
sage: hg_sage.apply("trac_6162-plotting.patch")
cd "/home/cswiercz/sage/devel/sage" && hg status
cd "/home/cswiercz/sage/devel/sage" && hg status
cd "/home/cswiercz/sage/devel/sage" && hg import   "/home/cswiercz/trac_6162-plotting.patch"
applying /home/cswiercz/trac_6162-plotting.patch
patching file sage/gsl/dft.py
Hunk #2 FAILED at 52
Hunk #3 FAILED at 156
2 out of 4 hunks FAILED -- saving rejects to file sage/gsl/dft.py.rej
abort: patch failed to apply
```


This was done on a local sage.math install. I wonder if there were changes to `sage/gsl/dft.py` between the two versions...

I don't have a 4.0.rc1 install anywhere so I'll have to get that up and running in order to review.



---

archive/issue_comments_049153.json:
```json
{
    "body": "Replying to [comment:7 cswiercz]:\n> Nick,\n> \n> I have very bad luck with your patches. :( Is `trac_6162-plotting.patch` also based on 4.0.rc1? I tried applying it to 4.0.2 after successfully applying `trac_6162-histogram.patch` and I received the following error:\n\nSorry, I wasn't clear.  Apply *only* `-histogram.patch`.",
    "created_at": "2009-06-23T16:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49153",
    "user": "ncalexan"
}
```

Replying to [comment:7 cswiercz]:
> Nick,
> 
> I have very bad luck with your patches. :( Is `trac_6162-plotting.patch` also based on 4.0.rc1? I tried applying it to 4.0.2 after successfully applying `trac_6162-histogram.patch` and I received the following error:

Sorry, I wasn't clear.  Apply *only* `-histogram.patch`.



---

archive/issue_comments_049154.json:
```json
{
    "body": "Replying to [comment:8 ncalexan]:\n> Sorry, I wasn't clear.  Apply *only* `-histogram.patch`.\n\nPerhaps I don't understand the difference between a histogram of a set of values and a histogram of an _indexed_ set of values but it seems to me that the following should output the familiar \"bell-shaped\" distribution:\n\n```\nsage: J = [ZZ(n) for n in range(10^3)]\nsage: A = [RR(gauss(0,1)) for n in range(10^3)]\nsage: s = IndexedSequence(A,J)\nsage: P = s.plot_histogram()\n```\n\n\nHowever, this looks pretty much the same as\n\n```\nsage: Q = s.plot()\n```\n\n\nAlso, the following is closer to the bell curve but it still doesn't capture what's going on: (swapping the `IndexedSequence` inputs)\n\n```\nsage: t = IndexedSequence(J,A)\nsage: R = t.plot_histogram()\n```\n\n\nI'm just wondering if I'm missing something.\n\nFinally, `finance.timeseries.TimeSeries` has a `plot_histogram` method that seems to work pretty well. Maybe you can use it somehow? Anyway, those are just my thoughts. Again, if I'm missing something I'll be happy to take another look.",
    "created_at": "2009-06-23T20:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49154",
    "user": "cswiercz"
}
```

Replying to [comment:8 ncalexan]:
> Sorry, I wasn't clear.  Apply *only* `-histogram.patch`.

Perhaps I don't understand the difference between a histogram of a set of values and a histogram of an _indexed_ set of values but it seems to me that the following should output the familiar "bell-shaped" distribution:

```
sage: J = [ZZ(n) for n in range(10^3)]
sage: A = [RR(gauss(0,1)) for n in range(10^3)]
sage: s = IndexedSequence(A,J)
sage: P = s.plot_histogram()
```


However, this looks pretty much the same as

```
sage: Q = s.plot()
```


Also, the following is closer to the bell curve but it still doesn't capture what's going on: (swapping the `IndexedSequence` inputs)

```
sage: t = IndexedSequence(J,A)
sage: R = t.plot_histogram()
```


I'm just wondering if I'm missing something.

Finally, `finance.timeseries.TimeSeries` has a `plot_histogram` method that seems to work pretty well. Maybe you can use it somehow? Anyway, those are just my thoughts. Again, if I'm missing something I'll be happy to take another look.



---

archive/issue_comments_049155.json:
```json
{
    "body": "I don't know why you expect your example to look like a bell curve.\nIn any case, there are too many points for plot_histogram to work with your example. Try\n\n\n```\nsage: J = [ZZ(n) for n in range(10)]\nsage: A = [RR(gauss(0,1)) for n in range(10)]\nsage: s = IndexedSequence(A,J)\nsage: P = s.plot_histogram()\nsage: show(P)\n```\n\nRegarding your suggestion to use , I get:\n\n\n```\nsage: import finance.timeseries.TimeSeries\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n\n....\n```\n\nCan you be more specific?",
    "created_at": "2009-06-23T20:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49155",
    "user": "wdj"
}
```

I don't know why you expect your example to look like a bell curve.
In any case, there are too many points for plot_histogram to work with your example. Try


```
sage: J = [ZZ(n) for n in range(10)]
sage: A = [RR(gauss(0,1)) for n in range(10)]
sage: s = IndexedSequence(A,J)
sage: P = s.plot_histogram()
sage: show(P)
```

Regarding your suggestion to use , I get:


```
sage: import finance.timeseries.TimeSeries
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

....
```

Can you be more specific?



---

archive/issue_comments_049156.json:
```json
{
    "body": "Now I see what you meant.\n\nI think you meant to compare the following plots:\n\n\n```\nsage: J = [ZZ(n) for n in range(10)]\nsage: A = [RR(gauss(0,1)) for n in range(10)]\nsage: s = IndexedSequence(A,J)\nsage: s.plot_histogram()\nsage: t = finance.TimeSeries(A); t\n[0.6636, 0.7983, -0.1451, 0.0838, -0.4355, -0.5719, 0.2572, 1.2802, -1.2696, -0.0642]\nsage: t.plot_histogram()\n```\n\nIf so, you can see that they are completely different. I don't see how to use the `sage/finance/time_series.pyx`\nfor this purpose.",
    "created_at": "2009-06-24T08:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49156",
    "user": "wdj"
}
```

Now I see what you meant.

I think you meant to compare the following plots:


```
sage: J = [ZZ(n) for n in range(10)]
sage: A = [RR(gauss(0,1)) for n in range(10)]
sage: s = IndexedSequence(A,J)
sage: s.plot_histogram()
sage: t = finance.TimeSeries(A); t
[0.6636, 0.7983, -0.1451, 0.0838, -0.4355, -0.5719, 0.2572, 1.2802, -1.2696, -0.0642]
sage: t.plot_histogram()
```

If so, you can see that they are completely different. I don't see how to use the `sage/finance/time_series.pyx`
for this purpose.



---

archive/issue_comments_049157.json:
```json
{
    "body": "Using your example, I'm just curious is there's any difference between the following two plots: (aside from the default red indexing below each bar in the plot)\n\n\n```\nsage: J = [ZZ(n) for n in range(10)]\nsage: A = [RR(gauss(0,1)) for n in range(10)]\nsage: s = IndexedSequence(A,J)\nsage: s.plot_histogram()\nsage: bar_chart(s.list())\n```\n\n\nThe only difference I can see is bar placement. (The indexing set easily allows you to place the bars in `IndexedSequence().plot_histogram()` wherever you like.) I'm sure that there's a lot of application for kind of plot with an indexed set.\n\nI tested the functionality of your code and, from my observations, it works great! Therefore, I give it a positive review. I just wanted a little bit of clarification on what kind of information the `plot_histogram()` method was actually presenting.\n\nSorry if my questions caused too much of a problem.",
    "created_at": "2009-06-24T17:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49157",
    "user": "cswiercz"
}
```

Using your example, I'm just curious is there's any difference between the following two plots: (aside from the default red indexing below each bar in the plot)


```
sage: J = [ZZ(n) for n in range(10)]
sage: A = [RR(gauss(0,1)) for n in range(10)]
sage: s = IndexedSequence(A,J)
sage: s.plot_histogram()
sage: bar_chart(s.list())
```


The only difference I can see is bar placement. (The indexing set easily allows you to place the bars in `IndexedSequence().plot_histogram()` wherever you like.) I'm sure that there's a lot of application for kind of plot with an indexed set.

I tested the functionality of your code and, from my observations, it works great! Therefore, I give it a positive review. I just wanted a little bit of clarification on what kind of information the `plot_histogram()` method was actually presenting.

Sorry if my questions caused too much of a problem.



---

archive/issue_comments_049158.json:
```json
{
    "body": "Thanks for the link to {{{bar_chart}}. It is similar, except that plot_histogram has an option which allows you to vary the thickness of the bars. \n\nThese \"improvements\" to the `plot_histogram` function are used to present a histogram of the aggregate totals in a course, especially for a multiple-choice machine-graded exam. Boring but the specific format was required for what I was trying to do.",
    "created_at": "2009-06-24T23:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49158",
    "user": "wdj"
}
```

Thanks for the link to {{{bar_chart}}. It is similar, except that plot_histogram has an option which allows you to vary the thickness of the bars. 

These "improvements" to the `plot_histogram` function are used to present a histogram of the aggregate totals in a course, especially for a multiple-choice machine-graded exam. Boring but the specific format was required for what I was trying to do.



---

archive/issue_comments_049159.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-26T17:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49159",
    "user": "boothby"
}
```

Resolution: fixed



---

archive/issue_comments_049160.json:
```json
{
    "body": "Merged `trac_6162-histogram.patch` in sage-4.1.alpha2. That is David Joyner's patch, and it is now changeset 12600:c169b5109084.",
    "created_at": "2009-07-12T04:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6162#issuecomment-49160",
    "user": "mvngu"
}
```

Merged `trac_6162-histogram.patch` in sage-4.1.alpha2. That is David Joyner's patch, and it is now changeset 12600:c169b5109084.
