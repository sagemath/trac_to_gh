# Issue 9671: Improve bar chart and histogram support

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-08-02 20:51:19

Assignee: jason, was

CC:  davidm jguzman eviatarbach jondo

The current state is not ideal.  One either uses `bar_chart`, which doesn't allow any control of where the bars actually go, or `IndexedSequence.plot_histogram`, which looks sort of clunky (at least the one example in the doc).  Matplotlib has very nice bar charts and histograms, obviously, so combining the approaches of these two to unify this would be very good.  Ideally one could do labels or place bars of given height at various locations.


---

Attachment


---

Comment by jason created at 2010-08-09 20:28:43

This definitely needs documentation work.  But the code seems to work okay.


---

Comment by jason created at 2010-08-09 20:28:43

Changing status from new to needs_work.


---

Comment by jason created at 2010-08-14 15:33:14

See http://matplotlib.sourceforge.net/examples/pylab_examples/histogram_demo_extended.html?highlight=codex%20histogram for more possibilities.


---

Comment by kcrisman created at 2011-06-13 19:28:55

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

Comment by davidm created at 2011-07-14 22:36:42

In the help string it says that only one list of data is implemented, but the code above seemed to work fine with a list of data because matplotlib's hist handles them nativity. The only thing that didn't seem to work is the axis wasn't being computed correctly. (I think because numpy.histogram was just combining the datasets) So I have attached a patch to histogram.py which I think fixes this. You can download it here:

http://dl.dropbox.com/u/1768136/sage-main_rev15695.patch


---

Comment by kcrisman created at 2011-07-29 19:02:42

davidm, can you actually attach the patch here as well?  That will make it easier to compare them, perhaps integrate things further.  Thanks!


---

Attachment


---

Comment by kcrisman created at 2011-08-01 16:48:20

Thanks!


---

Attachment


---

Comment by davidm created at 2011-09-24 00:29:08

Just added a few changes to the docs and exposed more of the matplotlib options.  I want to add things like x and y axis labeling and a legend but have to think about the best way to do it. Right now we are just passing all of the options directly to matplotlib 's hist which doesn't understand the keyword options title or xlabel. I am going to think about the best way to separate the two, unless there is some obvious way to do this.


---

Attachment


---

Comment by jason created at 2011-12-06 13:34:15

I added a few more tiny fixes for 4.7.2.


---

Comment by ppurka created at 2012-04-17 06:59:27

What needs to be done for this histogram patch? And are all the four patches necessary for the histogram to work?


---

Comment by kcrisman created at 2012-06-29 15:48:24

> And are all the four patches necessary for the histogram to work?
Looks like all four patches need to be used, at least for the ticket if not for the pure functionality.

> What needs to be done for this histogram patch?
Good question.  I'd say, for one, that it would be very good to have more documentation - nobody actually plots histograms with four data points.  We would also want some examples of the multiple data sets option.  Someone to go over the code again... 

On a different ticket, we might want to change the `TimeSeries` histogram and the `RealDistribution` histograms as well to use this, I'm not quite sure what they are up to.  It's not very unified.  But that would be a second step.


---

Comment by kcrisman created at 2014-09-08 13:19:51

Thanks very much for putting this into a branch, Volker!  My previous comments obviously still apply but this should be the incentive I (or someone) need to get this finished up.
----
New commits:


---

Comment by ppurka created at 2014-10-18 13:46:14

This is good. I don't see any problems with this patch. It provides a basic histogram support that was missing in Sage.

Regarding `RealDistribution` - this can be done in another ticket. Regarding `TimeSeries` - the histogram function there should not be replaced with this one, because that one does not return a plot.

If there are no objections, we should do the following:

1. Merge this ticket
2. Open a new ticket for `TimeSeries` to add a `histogram_plot` method to it (or something named similarly)
3. Open another new ticket for `RealDistribution` to modify its `RealDistribution.generate_histogram_plot` to be an alias to  or call this function. That one has some additional parameters which we have to take care of.


---

Comment by kcrisman created at 2014-10-19 00:11:41

Thanks for looking at this, Basu.  I do think that a _real_ example or more would be good - unless something has changed, there are no realistic examples (see comment:11).  The other comment there about the extra option should also be tested.


---

Comment by ppurka created at 2014-10-19 00:45:36

You are right. This needs a bit more work. I was testing some distributions yesterday with it and it was working fine. Things like:

```
histogram([normalvariate(0, 1) for _ in xrange(500)], bins=20)
histogram([random() for _ in xrange(500)])
```

But testing this more rigorously today, I find that it doesn't even pass the doctests. I will have a closer look at fixing that when I get some time.


---

Comment by kcrisman created at 2014-10-19 01:01:34

Hopefully the jsmol thing will be finished off soon so I can get back to this too.  Maybe we can show a few cool graphics about some interesting theorems :)


---

Comment by kcrisman created at 2014-10-22 03:28:00

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

Also, `get_minmax_data` doesn't even have any doctests, and one of the ones that fails now because of `g` not being defined in `_allowed_options` will need to be updated since there are a lot more options in the histograms (and this should be easy).  And `_repr_` makes no sense - what is an `n` datalist?  Oh, _and_ we want to document the multiple dataset option.  Wow, more to do than I realized.  http://matplotlib.org/_sources/examples/pylab_examples/histogram_demo_extended.txt is a useful resource.

But I do agree that the underlying matplotlib functionality is very likely to be awesome.  And in fact there are even more options now


---

Comment by kcrisman created at 2014-10-23 02:09:39

Okay, I'm going to push something fairly better in a moment.  Key things to still add:

 * Let's put in a few more good examples from http://matplotlib.org/_sources/examples/pylab_examples/histogram_demo_extended.txt
 * Let's make sure we have a good set of options from http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist and http://matplotlib.org/api/patches_api.html#matplotlib.patches.Patch
 * ~~Figuring out who user `davidm` was/is so we can give credit.~~ Fixed that.


---

Comment by kcrisman created at 2014-10-23 02:30:25

Such as 

```
sage: histogram(range(100), color=(1,0,0), label='mydata', hatch='/')
```

which looks great but needs extra options to be provided... I made that example basic (no options) for now but it needs to be elaborated with lots of stuff.


---

Comment by kcrisman created at 2014-10-23 02:45:30

Basu (or others), feel free to add some examples and get the (a more) correct set of options in.
----
New commits:


---

Comment by git created at 2014-10-28 20:05:37

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by kcrisman created at 2014-10-28 20:06:39

Ready for review!


---

Comment by kcrisman created at 2014-10-28 20:06:39

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2014-10-28 20:16:16

By the way, I give positive review to everything I didn't do in the last few days.


---

Comment by git created at 2014-11-16 16:00:34

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by ppurka created at 2014-11-16 23:36:31

`@`kcrisman Your changes look good to me. I added only a few things in the commit above. Feel free to put this to positive review.


---

Comment by kcrisman created at 2014-11-17 14:59:31

Thanks.  Can you add a doctest for the linestyle thing?  I wasn't aware of that.  Otherwise this looks good.


---

Comment by chapoton created at 2014-11-17 15:25:27

`note::` should be `.. NOTE::`


---

Comment by ppurka created at 2014-11-17 23:24:49

Changing status from needs_review to needs_work.


---

Comment by git created at 2014-11-18 02:38:50

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by kcrisman created at 2014-11-18 02:40:05

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2014-11-18 02:40:05

I think this last commit fixes everything - including a formatting thing I didn't catch before.  Check it, would you?  Thanks!


---

Comment by ppurka created at 2014-11-18 02:42:59

Changing status from needs_review to positive_review.


---

Comment by ppurka created at 2014-11-18 02:42:59

Thanks. Looks good to me.


---

Comment by vbraun created at 2014-11-19 08:32:15

Resolution: fixed
