# Issue 9671: Improve bar chart and histogram support

archive/issues_009671.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  davidm jguzman @eviatarbach @jondo\n\nThe current state is not ideal.  One either uses `bar_chart`, which doesn't allow any control of where the bars actually go, or `IndexedSequence.plot_histogram`, which looks sort of clunky (at least the one example in the doc).  Matplotlib has very nice bar charts and histograms, obviously, so combining the approaches of these two to unify this would be very good.  Ideally one could do labels or place bars of given height at various locations.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9671\n\n",
    "created_at": "2010-08-02T20:51:19Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Improve bar chart and histogram support",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9671",
    "user": "https://github.com/kcrisman"
}
```
Assignee: jason, was

CC:  davidm jguzman @eviatarbach @jondo

The current state is not ideal.  One either uses `bar_chart`, which doesn't allow any control of where the bars actually go, or `IndexedSequence.plot_histogram`, which looks sort of clunky (at least the one example in the doc).  Matplotlib has very nice bar charts and histograms, obviously, so combining the approaches of these two to unify this would be very good.  Ideally one could do labels or place bars of given height at various locations.

Issue created by migration from https://trac.sagemath.org/ticket/9671





---

archive/issue_comments_093789.json:
```json
{
    "body": "Attachment [trac-9671-histogram.patch](tarball://root/attachments/some-uuid/ticket9671/trac-9671-histogram.patch) by @jasongrout created at 2010-08-09 20:28:18",
    "created_at": "2010-08-09T20:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93789",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9671-histogram.patch](tarball://root/attachments/some-uuid/ticket9671/trac-9671-histogram.patch) by @jasongrout created at 2010-08-09 20:28:18



---

archive/issue_comments_093790.json:
```json
{
    "body": "This definitely needs documentation work.  But the code seems to work okay.",
    "created_at": "2010-08-09T20:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93790",
    "user": "https://github.com/jasongrout"
}
```

This definitely needs documentation work.  But the code seems to work okay.



---

archive/issue_comments_093791.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-09T20:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93791",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_093792.json:
```json
{
    "body": "See http://matplotlib.sourceforge.net/examples/pylab_examples/histogram_demo_extended.html?highlight=codex%20histogram for more possibilities.",
    "created_at": "2010-08-14T15:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93792",
    "user": "https://github.com/jasongrout"
}
```

See http://matplotlib.sourceforge.net/examples/pylab_examples/histogram_demo_extended.html?highlight=codex%20histogram for more possibilities.



---

archive/issue_comments_093793.json:
```json
{
    "body": "Note that we have `np.histogram` if you want as well.\n\nAnd `TimeSeries.histogram?`\n\nAlso here is something random in some code of Willliam's: \n\n```\ndef dist(v, b, left=float(0), right=float(pi)):\n    \"\"\"\n    We divide the interval between left (default: 0) and \n    right (default: pi) up into b bins.\n   \n    For each number in v (which must left and right), \n    we find which bin it lies in and add this to a counter.\n    This function then returns the bins and the number of\n    elements of v that lie in each one. \n\n    ALGORITHM: To find the index of the bin that a given \n    number x lies in, we multiply x by b/length and take the \n    floor. \n    \"\"\"\n    length = right - left\n    normalize = float(b/length)\n    vals = {}\n    d = dict([(i,0) for i in range(b)])\n    for x in v:\n        n = int(normalize*(float(x)-left))\n        d[n] += 1\n    return d, len(v)\n    \ndef graph(d, b, num=5000, left=float(0), right=float(pi)):\n    s = Graphics()\n    left = float(left); right = float(right)\n    length = right - left\n    w = length/b\n    k = 0\n    for i, n in d.iteritems():\n        k += n\n        # ith bin has n objects in it. \n        s += polygon([(w*i+left,0), (w*(i+1)+left,0), \\\n                     (w*(i+1)+left, n/(num*w)), (w*i+left, n/(num*w))],\\\n                     rgbcolor=(0,0,0.5))\n    return s    \n```\n\n\nThe point being that this should be unified.",
    "created_at": "2011-06-13T19:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93793",
    "user": "https://github.com/kcrisman"
}
```

Note that we have `np.histogram` if you want as well.

And `TimeSeries.histogram?`

Also here is something random in some code of Willliam's: 

```
def dist(v, b, left=float(0), right=float(pi)):
    """
    We divide the interval between left (default: 0) and 
    right (default: pi) up into b bins.
   
    For each number in v (which must left and right), 
    we find which bin it lies in and add this to a counter.
    This function then returns the bins and the number of
    elements of v that lie in each one. 

    ALGORITHM: To find the index of the bin that a given 
    number x lies in, we multiply x by b/length and take the 
    floor. 
    """
    length = right - left
    normalize = float(b/length)
    vals = {}
    d = dict([(i,0) for i in range(b)])
    for x in v:
        n = int(normalize*(float(x)-left))
        d[n] += 1
    return d, len(v)
    
def graph(d, b, num=5000, left=float(0), right=float(pi)):
    s = Graphics()
    left = float(left); right = float(right)
    length = right - left
    w = length/b
    k = 0
    for i, n in d.iteritems():
        k += n
        # ith bin has n objects in it. 
        s += polygon([(w*i+left,0), (w*(i+1)+left,0), \
                     (w*(i+1)+left, n/(num*w)), (w*i+left, n/(num*w))],\
                     rgbcolor=(0,0,0.5))
    return s    
```


The point being that this should be unified.



---

archive/issue_comments_093794.json:
```json
{
    "body": "In the help string it says that only one list of data is implemented, but the code above seemed to work fine with a list of data because matplotlib's hist handles them nativity. The only thing that didn't seem to work is the axis wasn't being computed correctly. (I think because numpy.histogram was just combining the datasets) So I have attached a patch to histogram.py which I think fixes this. You can download it here:\n\nhttp://dl.dropbox.com/u/1768136/sage-main_rev15695.patch",
    "created_at": "2011-07-14T22:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93794",
    "user": "https://trac.sagemath.org/admin/accounts/users/davidm"
}
```

In the help string it says that only one list of data is implemented, but the code above seemed to work fine with a list of data because matplotlib's hist handles them nativity. The only thing that didn't seem to work is the axis wasn't being computed correctly. (I think because numpy.histogram was just combining the datasets) So I have attached a patch to histogram.py which I think fixes this. You can download it here:

http://dl.dropbox.com/u/1768136/sage-main_rev15695.patch



---

archive/issue_comments_093795.json:
```json
{
    "body": "davidm, can you actually attach the patch here as well?  That will make it easier to compare them, perhaps integrate things further.  Thanks!",
    "created_at": "2011-07-29T19:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93795",
    "user": "https://github.com/kcrisman"
}
```

davidm, can you actually attach the patch here as well?  That will make it easier to compare them, perhaps integrate things further.  Thanks!



---

archive/issue_comments_093796.json:
```json
{
    "body": "Attachment [sage-main_rev15695.patch](tarball://root/attachments/some-uuid/ticket9671/sage-main_rev15695.patch) by davidm created at 2011-07-29 20:51:07",
    "created_at": "2011-07-29T20:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93796",
    "user": "https://trac.sagemath.org/admin/accounts/users/davidm"
}
```

Attachment [sage-main_rev15695.patch](tarball://root/attachments/some-uuid/ticket9671/sage-main_rev15695.patch) by davidm created at 2011-07-29 20:51:07



---

archive/issue_comments_093797.json:
```json
{
    "body": "Thanks!",
    "created_at": "2011-08-01T16:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93797",
    "user": "https://github.com/kcrisman"
}
```

Thanks!



---

archive/issue_comments_093798.json:
```json
{
    "body": "Attachment [trac9671-histogram-docchange.patch](tarball://root/attachments/some-uuid/ticket9671/trac9671-histogram-docchange.patch) by davidm created at 2011-09-24 00:24:41",
    "created_at": "2011-09-24T00:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93798",
    "user": "https://trac.sagemath.org/admin/accounts/users/davidm"
}
```

Attachment [trac9671-histogram-docchange.patch](tarball://root/attachments/some-uuid/ticket9671/trac9671-histogram-docchange.patch) by davidm created at 2011-09-24 00:24:41



---

archive/issue_comments_093799.json:
```json
{
    "body": "Just added a few changes to the docs and exposed more of the matplotlib options.  I want to add things like x and y axis labeling and a legend but have to think about the best way to do it. Right now we are just passing all of the options directly to matplotlib 's hist which doesn't understand the keyword options title or xlabel. I am going to think about the best way to separate the two, unless there is some obvious way to do this.",
    "created_at": "2011-09-24T00:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93799",
    "user": "https://trac.sagemath.org/admin/accounts/users/davidm"
}
```

Just added a few changes to the docs and exposed more of the matplotlib options.  I want to add things like x and y axis labeling and a legend but have to think about the best way to do it. Right now we are just passing all of the options directly to matplotlib 's hist which doesn't understand the keyword options title or xlabel. I am going to think about the best way to separate the two, unless there is some obvious way to do this.



---

archive/issue_comments_093800.json:
```json
{
    "body": "Attachment [histogram_fixes.patch](tarball://root/attachments/some-uuid/ticket9671/histogram_fixes.patch) by @jasongrout created at 2011-12-06 13:33:37",
    "created_at": "2011-12-06T13:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93800",
    "user": "https://github.com/jasongrout"
}
```

Attachment [histogram_fixes.patch](tarball://root/attachments/some-uuid/ticket9671/histogram_fixes.patch) by @jasongrout created at 2011-12-06 13:33:37



---

archive/issue_comments_093801.json:
```json
{
    "body": "I added a few more tiny fixes for 4.7.2.",
    "created_at": "2011-12-06T13:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93801",
    "user": "https://github.com/jasongrout"
}
```

I added a few more tiny fixes for 4.7.2.



---

archive/issue_comments_093802.json:
```json
{
    "body": "What needs to be done for this histogram patch? And are all the four patches necessary for the histogram to work?",
    "created_at": "2012-04-17T06:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93802",
    "user": "https://github.com/ppurka"
}
```

What needs to be done for this histogram patch? And are all the four patches necessary for the histogram to work?



---

archive/issue_comments_093803.json:
```json
{
    "body": "> And are all the four patches necessary for the histogram to work?\nLooks like all four patches need to be used, at least for the ticket if not for the pure functionality.\n\n> What needs to be done for this histogram patch?\nGood question.  I'd say, for one, that it would be very good to have more documentation - nobody actually plots histograms with four data points.  We would also want some examples of the multiple data sets option.  Someone to go over the code again... \n\nOn a different ticket, we might want to change the `TimeSeries` histogram and the `RealDistribution` histograms as well to use this, I'm not quite sure what they are up to.  It's not very unified.  But that would be a second step.",
    "created_at": "2012-06-29T15:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93803",
    "user": "https://github.com/kcrisman"
}
```

> And are all the four patches necessary for the histogram to work?
Looks like all four patches need to be used, at least for the ticket if not for the pure functionality.

> What needs to be done for this histogram patch?
Good question.  I'd say, for one, that it would be very good to have more documentation - nobody actually plots histograms with four data points.  We would also want some examples of the multiple data sets option.  Someone to go over the code again... 

On a different ticket, we might want to change the `TimeSeries` histogram and the `RealDistribution` histograms as well to use this, I'm not quite sure what they are up to.  It's not very unified.  But that would be a second step.



---

archive/issue_comments_093804.json:
```json
{
    "body": "Thanks very much for putting this into a branch, Volker!  My previous comments obviously still apply but this should be the incentive I (or someone) need to get this finished up.\n----\nNew commits:",
    "created_at": "2014-09-08T13:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93804",
    "user": "https://github.com/kcrisman"
}
```

Thanks very much for putting this into a branch, Volker!  My previous comments obviously still apply but this should be the incentive I (or someone) need to get this finished up.
----
New commits:



---

archive/issue_comments_093805.json:
```json
{
    "body": "This is good. I don't see any problems with this patch. It provides a basic histogram support that was missing in Sage.\n\nRegarding `RealDistribution` - this can be done in another ticket. Regarding `TimeSeries` - the histogram function there should not be replaced with this one, because that one does not return a plot.\n\nIf there are no objections, we should do the following:\n\n1. Merge this ticket\n2. Open a new ticket for `TimeSeries` to add a `histogram_plot` method to it (or something named similarly)\n3. Open another new ticket for `RealDistribution` to modify its `RealDistribution.generate_histogram_plot` to be an alias to  or call this function. That one has some additional parameters which we have to take care of.",
    "created_at": "2014-10-18T13:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93805",
    "user": "https://github.com/ppurka"
}
```

This is good. I don't see any problems with this patch. It provides a basic histogram support that was missing in Sage.

Regarding `RealDistribution` - this can be done in another ticket. Regarding `TimeSeries` - the histogram function there should not be replaced with this one, because that one does not return a plot.

If there are no objections, we should do the following:

1. Merge this ticket
2. Open a new ticket for `TimeSeries` to add a `histogram_plot` method to it (or something named similarly)
3. Open another new ticket for `RealDistribution` to modify its `RealDistribution.generate_histogram_plot` to be an alias to  or call this function. That one has some additional parameters which we have to take care of.



---

archive/issue_comments_093806.json:
```json
{
    "body": "Thanks for looking at this, Basu.  I do think that a *real* example or more would be good - unless something has changed, there are no realistic examples (see comment:11).  The other comment there about the extra option should also be tested.",
    "created_at": "2014-10-19T00:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93806",
    "user": "https://github.com/kcrisman"
}
```

Thanks for looking at this, Basu.  I do think that a *real* example or more would be good - unless something has changed, there are no realistic examples (see comment:11).  The other comment there about the extra option should also be tested.



---

archive/issue_comments_093807.json:
```json
{
    "body": "You are right. This needs a bit more work. I was testing some distributions yesterday with it and it was working fine. Things like:\n\n```\nhistogram([normalvariate(0, 1) for _ in xrange(500)], bins=20)\nhistogram([random() for _ in xrange(500)])\n```\n\nBut testing this more rigorously today, I find that it doesn't even pass the doctests. I will have a closer look at fixing that when I get some time.",
    "created_at": "2014-10-19T00:45:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93807",
    "user": "https://github.com/ppurka"
}
```

You are right. This needs a bit more work. I was testing some distributions yesterday with it and it was working fine. Things like:

```
histogram([normalvariate(0, 1) for _ in xrange(500)], bins=20)
histogram([random() for _ in xrange(500)])
```

But testing this more rigorously today, I find that it doesn't even pass the doctests. I will have a closer look at fixing that when I get some time.



---

archive/issue_comments_093808.json:
```json
{
    "body": "Hopefully the jsmol thing will be finished off soon so I can get back to this too.  Maybe we can show a few cool graphics about some interesting theorems :)",
    "created_at": "2014-10-19T01:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93808",
    "user": "https://github.com/kcrisman"
}
```

Hopefully the jsmol thing will be finished off soon so I can get back to this too.  Maybe we can show a few cool graphics about some interesting theorems :)



---

archive/issue_comments_093809.json:
```json
{
    "body": "For completeness, here are the (relevant) failing tests.\n\n```\n    g = Histogram(range(4), [1,3,2,0], {}); g\n    Histogram(range(3), [10,3,5], {'width':0.7})\n    g = Histogram(range(4), [1,3,2,0], {})\n    g = Histogram(range(4), [1,3,2,0], {})\n(all give)\n    TypeError: __init__() takes exactly 3 arguments (4 given)\n(this is probably because they're taken from bar_chart but a histogram only takes one list)\n\n    histogram([1,2,10])\n    histogram([1,2,3,4])\n    histogram([-3,4,-6,11])\n(all give)\n    Graphics object consisting of 1 graphics primitive\n(maybe this is from the change in display hook in Ipython)\n\nFailed example:\n    histogram([-3,5,-6,11], rgbcolor=(1,0,0))\nExpected nothing\nGot:\n    doctest:239: FormatterWarning: Exception in text/plain formatter: Unknown property rgbcolor\n    None\n```\n\nAlso, `get_minmax_data` doesn't even have any doctests, and one of the ones that fails now because of `g` not being defined in `_allowed_options` will need to be updated since there are a lot more options in the histograms (and this should be easy).  And `_repr_` makes no sense - what is an `n` datalist?  Oh, *and* we want to document the multiple dataset option.  Wow, more to do than I realized.  http://matplotlib.org/_sources/examples/pylab_examples/histogram_demo_extended.txt is a useful resource.\n\nBut I do agree that the underlying matplotlib functionality is very likely to be awesome.  And in fact there are even more options now",
    "created_at": "2014-10-22T03:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93809",
    "user": "https://github.com/kcrisman"
}
```

For completeness, here are the (relevant) failing tests.

```
    g = Histogram(range(4), [1,3,2,0], {}); g
    Histogram(range(3), [10,3,5], {'width':0.7})
    g = Histogram(range(4), [1,3,2,0], {})
    g = Histogram(range(4), [1,3,2,0], {})
(all give)
    TypeError: __init__() takes exactly 3 arguments (4 given)
(this is probably because they're taken from bar_chart but a histogram only takes one list)

    histogram([1,2,10])
    histogram([1,2,3,4])
    histogram([-3,4,-6,11])
(all give)
    Graphics object consisting of 1 graphics primitive
(maybe this is from the change in display hook in Ipython)

Failed example:
    histogram([-3,5,-6,11], rgbcolor=(1,0,0))
Expected nothing
Got:
    doctest:239: FormatterWarning: Exception in text/plain formatter: Unknown property rgbcolor
    None
```

Also, `get_minmax_data` doesn't even have any doctests, and one of the ones that fails now because of `g` not being defined in `_allowed_options` will need to be updated since there are a lot more options in the histograms (and this should be easy).  And `_repr_` makes no sense - what is an `n` datalist?  Oh, *and* we want to document the multiple dataset option.  Wow, more to do than I realized.  http://matplotlib.org/_sources/examples/pylab_examples/histogram_demo_extended.txt is a useful resource.

But I do agree that the underlying matplotlib functionality is very likely to be awesome.  And in fact there are even more options now



---

archive/issue_comments_093810.json:
```json
{
    "body": "Okay, I'm going to push something fairly better in a moment.  Key things to still add:\n\n* Let's put in a few more good examples from http://matplotlib.org/_sources/examples/pylab_examples/histogram_demo_extended.txt\n* Let's make sure we have a good set of options from http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist and http://matplotlib.org/api/patches_api.html#matplotlib.patches.Patch\n* ~~Figuring out who user `davidm` was/is so we can give credit.~~\u00a0Fixed that.",
    "created_at": "2014-10-23T02:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93810",
    "user": "https://github.com/kcrisman"
}
```

Okay, I'm going to push something fairly better in a moment.  Key things to still add:

* Let's put in a few more good examples from http://matplotlib.org/_sources/examples/pylab_examples/histogram_demo_extended.txt
* Let's make sure we have a good set of options from http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist and http://matplotlib.org/api/patches_api.html#matplotlib.patches.Patch
* ~~Figuring out who user `davidm` was/is so we can give credit.~~ Fixed that.



---

archive/issue_comments_093811.json:
```json
{
    "body": "Such as \n\n```\nsage: histogram(range(100), color=(1,0,0), label='mydata', hatch='/')\n```\n\nwhich looks great but needs extra options to be provided... I made that example basic (no options) for now but it needs to be elaborated with lots of stuff.",
    "created_at": "2014-10-23T02:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93811",
    "user": "https://github.com/kcrisman"
}
```

Such as 

```
sage: histogram(range(100), color=(1,0,0), label='mydata', hatch='/')
```

which looks great but needs extra options to be provided... I made that example basic (no options) for now but it needs to be elaborated with lots of stuff.



---

archive/issue_comments_093812.json:
```json
{
    "body": "Basu (or others), feel free to add some examples and get the (a more) correct set of options in.\n----\nNew commits:",
    "created_at": "2014-10-23T02:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93812",
    "user": "https://github.com/kcrisman"
}
```

Basu (or others), feel free to add some examples and get the (a more) correct set of options in.
----
New commits:



---

archive/issue_comments_093813.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-10-28T20:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93813",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_093814.json:
```json
{
    "body": "Ready for review!",
    "created_at": "2014-10-28T20:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93814",
    "user": "https://github.com/kcrisman"
}
```

Ready for review!



---

archive/issue_comments_093815.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-10-28T20:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93815",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093816.json:
```json
{
    "body": "By the way, I give positive review to everything I didn't do in the last few days.",
    "created_at": "2014-10-28T20:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93816",
    "user": "https://github.com/kcrisman"
}
```

By the way, I give positive review to everything I didn't do in the last few days.



---

archive/issue_comments_093817.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-11-16T16:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93817",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_093818.json:
```json
{
    "body": "`@`kcrisman Your changes look good to me. I added only a few things in the commit above. Feel free to put this to positive review.",
    "created_at": "2014-11-16T23:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93818",
    "user": "https://github.com/ppurka"
}
```

`@`kcrisman Your changes look good to me. I added only a few things in the commit above. Feel free to put this to positive review.



---

archive/issue_comments_093819.json:
```json
{
    "body": "Thanks.  Can you add a doctest for the linestyle thing?  I wasn't aware of that.  Otherwise this looks good.",
    "created_at": "2014-11-17T14:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93819",
    "user": "https://github.com/kcrisman"
}
```

Thanks.  Can you add a doctest for the linestyle thing?  I wasn't aware of that.  Otherwise this looks good.



---

archive/issue_comments_093820.json:
```json
{
    "body": "`note::` should be `.. NOTE::`",
    "created_at": "2014-11-17T15:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93820",
    "user": "https://github.com/fchapoton"
}
```

`note::` should be `.. NOTE::`



---

archive/issue_comments_093821.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-11-17T23:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93821",
    "user": "https://github.com/ppurka"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093822.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-11-18T02:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93822",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_093823.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-11-18T02:40:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93823",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093824.json:
```json
{
    "body": "I think this last commit fixes everything - including a formatting thing I didn't catch before.  Check it, would you?  Thanks!",
    "created_at": "2014-11-18T02:40:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93824",
    "user": "https://github.com/kcrisman"
}
```

I think this last commit fixes everything - including a formatting thing I didn't catch before.  Check it, would you?  Thanks!



---

archive/issue_comments_093825.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-11-18T02:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93825",
    "user": "https://github.com/ppurka"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093826.json:
```json
{
    "body": "Thanks. Looks good to me.",
    "created_at": "2014-11-18T02:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93826",
    "user": "https://github.com/ppurka"
}
```

Thanks. Looks good to me.



---

archive/issue_comments_093827.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-11-19T08:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9671#issuecomment-93827",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
