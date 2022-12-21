# Issue 5956: image dimensions for show() are in inches

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-05-01 07:17:25

Assignee: was

CC:  kcrisman

Keywords: image dimensions, figsize

As discussed at this [sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/c411254b7bc0bb97), the optional argument `figsize` of the command `show()` needs to clearly state that the units of the image are in inches. As of Sage 3.4.1, the docstring for `show()` says:

```
- ``figsize``- [width, height] (same for square aspect)
```

which can be interpreted to mean that one can do something like `figsize=[w,h]`. But something like the following produces a segmentation fault:

```
[mvngu`@`sage ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: q = var("q")
sage: f(q) = (q^4 - q^2 + 1) * (q^4 + q^3 + q^2 + q + 1) * (q^4 - q^3 \
+ q^2 - q + 1) * (q^6 + q^5 + q^4 + q^3 + q^2 + q + 1) * (q^6 - q^5 + \
q^4 - q^3 + q^2 - q + 1) * (q^(20) - q^(18) - q^(14) - q^(12) + q^(10) \
- q^8 - q^6 - q^2 + 1)
sage: g(q) = q^8 * (q^4 + q^2 + 1)^2 * (q^4 + 1)^5
sage: p = complex_plot(f/g, (-2,2), (-2,2))
sage: p.show(figsize=[256,256])
```

while the following results in a `ValueError`:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: q = var("q")
sage: f(q) = (q^4 - q^2 + 1) * (q^4 + q^3 + q^2 + q + 1) * (q^4 - q^3 \
+ q^2 - q + 1) * (q^6 + q^5 + q^4 + q^3 + q^2 + q + 1) * (q^6 - q^5 + \
q^4 - q^3 + q^2 - q + 1) * (q^(20) - q^(18) - q^(14) - q^(12) + q^(10) \
- q^8 - q^6 - q^2 + 1)
sage: g(q) = q^8 * (q^4 + q^2 + 1)^2 * (q^4 + 1)^5
sage: p = complex_plot(f/g, (-2,2), (-2,2))
sage: p.show(figsize=[500,500])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: width and height must each be below 32768
```

Essentially, the documentation for `show()` needs to be updated, especially the optional arguments, to clearly explain the units of measurement of the width and height of the image size. Also, it would be a good idea to specify how one can pass in values for those dimensions. For example, can one do this `figsize=[124,124]`?


---

Comment by jason created at 2010-05-26 15:32:53

Changing keywords from "image dimensions, figsize" to "image dimensions, figsize, beginner".


---

Comment by emchennyc created at 2012-11-03 21:42:35

Changing status from new to needs_review.


---

Comment by emchennyc created at 2012-11-03 21:42:35

Made a doc update after reading this thread:  https://groups.google.com/forum/?fromgroups=#!topic/sage-devel/xBElS3vAu5c

Do you think any more info should be included in the changes?


---

Comment by kcrisman created at 2012-11-04 01:57:01

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2012-11-04 01:57:01

This would be a good start.  

What's the reference for the dpi, just out of curiosity?  (I assume it's right in the Sage or mpl source.)  Also, telling us the maximum possible would be helpful, given the errors - especially since the one above is confusing since the `32768` is in "dots", not inches.  Presumably if one reset the default dpi...

```
sage: P.show(figsize=[1,327],dpi=100)
sage: P.show(figsize=[1,328],dpi=100)
<ValueError>
sage: P.show(figsize=[1,328],dpi=80)
```

So this should be very, very clear, in order to resolve this ticket.

Additionally, you'll want to add a doctest to verify that some things don't go boom, and that the error is correctly raised, etc.  Maybe even a `# not tested` line with the segfault.

Finally, we may also want to report the segfault upstream with a "pure" matplotlib example, if you can concoct one.

But all that said, thanks very much for looking at this - this is just part of the normal review process, good start.


---

Comment by emchennyc created at 2012-11-10 18:49:29

Changing status from needs_work to needs_review.


---

Comment by emchennyc created at 2012-11-10 18:49:29

Thank you for the pointers. In matplotlib/rcsetup.py the default figure properties start at line 508. 
line 509 # figure size in inches: width by height 'figure.figsize'    : [ [8.0,6.0], validate_nseq_float(2)]
line 523 'savefig.dpi'         : [100, validate_float],   # DPI

I submitted a new patch to include what I think you mean by a doctest. I wasn't sure what you meant about including '# not tested line with the segfault'. Should I include an example with the segfault in the docstring?

Strangely enough, I did not raise any errors when I tried a 'pure' matplotlib example...


```
from matplotlib import pyplot as plt
f=plt.figure(figsize=[28,10],dpi=100)
f.show()
```



Would someone kindly review  and let me know what else should be included in the doctest? I appreciate your patience with this, as I am (obviously) new and hoping to learn. Thank you!


---

Comment by ppurka created at 2012-11-16 10:05:46

This ticket is awesome! Brought my laptop to a crawl! :)

`@`emchennyc: I might come back to this ticket if kcrisman doesn't. For now, it seems that matplotlib (even the latest 1.2.0 release) does not handle the parameters `[256,256]` properly. It tries to allocate memory and then fails, resulting in a segfault.

What kcrisman asks is a doctest like this (under a `TEST:` section; look at how these sections are written in other functions or other files):

```
TEST:

The following plot segfaults sage and should not be doctested.::

    sage: plot(x).show(figsize=[256,256]) # not tested

```


If you do happen to run this command, be very careful. I suggest you set a ulimit before you start sage. If you have, say 3G, of memory/RAM, then set ulimit to 2G and only then start sage. If you have even less memory then you will need to set even lower ulimit, but sage won't run properly below 1G.

```
$ ulimit -v 2000000
$ sage
sage: plot(x).show(figsize=[256,256]) # boom, segv!!
```


That said, I would like you to set some defaults in your editor. Currently, your patch contains a mixture of tabs and spaces. I suggest you change the settings in your editor to not insert tabs, and instead insert 4 spaces every time you press a tab key.


---

Comment by kcrisman created at 2013-01-03 20:16:35

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2013-01-03 20:16:35

Needs work due to the issues raise by ppurka, but getting close!


---

Comment by emchennyc created at 2013-01-05 13:40:15

`@`ppurka Thank you for the feedback! The tests I included in the attached patch pass when I run:
./sage -t -verbose 'devel/sage-5956/sage/plot/graphics.py'

Then, I
- ran ./sage -docbuild reference html
- navigated to SAGEROOT/devel/branch/doc/output/html/en/reference
- opened plotting.html in a browser
- visited the doc page for Graphics objects
but did not see the documentation that I added. Did I miss a step?

Also, here is a matplotlib example which I believe this bug is related to. Please correct me if I'm wrong and feel free to advise if I should use this example to report as a matplotlib issue: http://pastebin.com/raw.php?i=5Arg52e2


---

Comment by kcrisman created at 2013-01-05 13:54:46

Replying to [comment:9 emchennyc]:
> `@`ppurka Thank you for the feedback! The tests I included in the attached patch pass when I run:
> ./sage -t -verbose 'devel/sage-5956/sage/plot/graphics.py'
> 
> Then, I

You have to do ./sage -b first.  The tests run on the copy of the code in the devel/sage directory, but the docs build off the ones in the build directory which that command does.

> - ran ./sage -docbuild reference html
> - navigated to SAGEROOT/devel/branch/doc/output/html/en/reference
> - opened plotting.html in a browser
> - visited the doc page for Graphics objects
> but did not see the documentation that I added. Did I miss a step?
> 
> Also, here is a matplotlib example which I believe this bug is related to. Please correct me if I'm wrong and feel free to advise if I should use this example to report as a matplotlib issue: http://pastebin.com/raw.php?i=5Arg52e2


---

Comment by ppurka created at 2013-01-05 14:25:33

Thanks for the update. There is one more thing that I overlooked earlier. The documentation should mention that the number `32768` is in dots per inch. Maybe the text of `ValueError` should also end in *32768 dots per inch*.

```
sage: e.show(figsize=[328,10],dpi=100)
ValueError: width and height must each be below 32768 dots per inch.
```

I think the following modification to the `figsize` documentation is warranted.

```
- ``figsize`` - (default: [8.0,6.0]) [width, height] inches. The maximum value
  of each of the width and the height can be 327 inches, at the default ``dpi``
  of 100 dpi, which is just shy of the maximum allowed value of 32768 dots
  per inch.
```

Then, the test should have the following description:

```
        The figsize width and height parameters must be less than 328 inches each,
        corresponding to the maximum allowed dpi of 32768.::
```

This will make the number 32768 more clear to anyone who is curious what that number means in the `ValueError`.

I am unable to replicate your matplotlib example. A figure doesn't seem to have a `show()` attribute. However, the following example successfully crashes matplotlib.

```
~» ulimit -v 2000000
~» sage -ipython
Python 2.7.3 (default, Dec 30 2012, 21:34:30)
Type "copyright", "credits" or "license" for more information.

IPython 0.10.2 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object'. ?object also works, ?? prints more.

In [1]: from matplotlib import pyplot

In [2]: pyplot.figure(figsize=[232,232])
Out[2]: <matplotlib.figure.Figure object at 0x12ba950>

In [3]: pyplot.savefig('/tmp/a.png')
...
RuntimeError: Could not allocate memory for image
```



---

Attachment


---

Attachment

apply only this


---

Attachment

not to be merged. only for review.


---

Comment by ppurka created at 2013-02-02 08:46:52

Changing status from needs_work to needs_review.


---

Comment by ppurka created at 2013-02-02 08:46:52

Updated the patch to sage-5.7beta0 and introduced some other changes.

The patch [attachment:only_for_review.patch] contains the changes I made after rebasing the patch to 5.7beta0. In particular, I have introduced the changes I suggested in my comments, and have fixed failing doctests due to the use/redefining of `e` in the earlier patch.

The changes needs review.

Patchbot apply trac_5956_figsize_units.1.patch


---

Comment by kcrisman created at 2013-03-22 21:08:46

This hit me today in class!  At least, I think so - `figsize=[5,5]` shouldn't necessarily yield this, but it was the same message.  I thought it was in, but high priority now.

Also, I think that #12592 is a dup.


---

Comment by kcrisman created at 2013-03-22 21:14:29

Oh, I figured out my (very stupid) problem - I used `figsize=[-5,5]`, which is of course absurd.  Still, probably wouldn't hurt to put in a check for absurd values... such typos are "all too easy".


---

Comment by kcrisman created at 2013-03-23 01:37:48

Needs a bit of work.  The limit is in pixels (dots), not dots per inch.  `2^15` dots per inch would be impressive indeed.  Notice also that [apparently this could be raised](http://matplotlib.1069221.n5.nabble.com/the-32768-pixel-limit-tt30382.html#none) if one really wanted to.

I'll add a reviewer patch momentarily.


---

Attachment

I think this needs some review, since I add some assertions and so forth.   I hope this clarifies things more, though, and adds doc in the main plot page where it is probably needed.

ppurka, if you are an author too, feel free to add yourself.  Positive review to everything before my patch.

Patchbot: apply trac_5956_figsize_units.1.patch and trac_5956-reviewer.patch to devel/sage.


---

Comment by ppurka created at 2013-03-23 07:09:58

Replying to [comment:17 kcrisman]:
> I think this needs some review, since I add some assertions and so forth.   I hope this clarifies things more, though, and adds doc in the main plot page where it is probably needed.

Thanks. Looks good to me.

> ppurka, if you are an author too, feel free to add yourself.  Positive review to everything before my patch.

I did change some doctests.


---

Comment by ppurka created at 2013-03-23 07:09:58

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-23 10:32:26

Use `ValueError` for bad user input, not `AssertionError`. If there is any way to produce an `AssertionError` using public functions, that is by definition a bug.

Assertions are meant to check internal consistency inside algorithms. They express "I _know_ this condition is true", not "I want to _check_ that this condition is true".


---

Comment by jdemeyer created at 2013-03-23 10:32:26

Changing status from positive_review to needs_work.


---

Comment by kcrisman created at 2013-03-23 12:42:42

> Assertions are meant to check internal consistency inside algorithms. They express "I _know_ this condition is true", not "I want to _check_ that this condition is true".
Okay, fair enough.  The problem is that now I have to go remember how to check that something is a numeric type as well - which is better in the long run, but which is tricky with all the zillions of numeric input types Sage has... does something like `isnumeric` work?  It sounds familiar.


---

Comment by jdemeyer created at 2013-03-23 12:47:30

Replying to [comment:20 kcrisman]:
> > Assertions are meant to check internal consistency inside algorithms. They express "I _know_ this condition is true", not "I want to _check_ that this condition is true".
> Okay, fair enough.  The problem is that now I have to go remember how to check that something is a numeric type as well

Just convert, for example

```
x = float(x)
```



---

Comment by ppurka created at 2013-03-23 13:14:44

Why should we go around checking for numeric types? This is not a "critical" application that should ensure sane inputs for all kinds of inputs. If the user sends in garbage, they will eventually get garbage out from at least matplotlib, if not earlier in the process.


---

Comment by kcrisman created at 2013-03-26 03:01:32

It's not critical in that sense, but it's the kind of thing where I figure we might as well make sure that any error message sent makes sense.  The current error

```
ValueError: width and height must each be below 32768
```

doesn't refer to `figsize` and at least made me totally miss that I had somehow smuggled a minus sign in there, since I was frantically trying to make the image smaller and wondering why five was too big :-)  I figure if it can happen to an experienced Sage user "on the spot", it will definitely happen to a new user.  Jeroen's comment seems quite reasonable especially as everything matplotlib is going to end up a float anyway, if I recall correctly.

I'll try to get this all packaged up in the next day or two.


---

Comment by ppurka created at 2014-01-19 14:31:46

Added a git version of the patch. This is based on 6.1.beta5.


---

Comment by kcrisman created at 2014-11-07 19:24:11

> I'll try to get this all packaged up in the next day or two.
Next day or two, next year or two...
> Added a git version of the patch. This is based on 6.1.beta5.
Amazingly, apparently still applies.

But we still haven't taken care of Jeroen's comment.  So I will try to do that now.
----
New commits:


---

Comment by kcrisman created at 2014-11-07 19:39:34

Okay, the last commit only needs review.
----
New commits:


---

Comment by kcrisman created at 2014-11-07 19:39:34

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2014-11-08 11:08:59

Replying to [comment:22 ppurka]:
> Why should we go around checking for numeric types? This is not a "critical" application that should ensure sane inputs for all kinds of inputs. If the user sends in garbage, they will eventually get garbage out from at least matplotlib, if not earlier in the process.

Well, it could be that the user will send some Sage numeric type, which matplotlib might treat like garbage. A conversion like

```
x = float(x)   # assuming that it's a float that you need
```

will solve both problems: it will raise a `TypeError` when true garbage is given but it should work for all Sage numeric types.


---

Comment by jdemeyer created at 2014-11-08 11:13:29

A minor point, but I wouldn't write segfaulting examples. Imagine the user tries those "examples" without reading the surrounding text...


---

Comment by ppurka created at 2014-11-09 14:37:26

Replying to [comment:34 jdemeyer]:
> A minor point, but I wouldn't write segfaulting examples. Imagine the user tries those "examples" without reading the surrounding text...
How about we prepend the segfaulting line with a comment? Like this:

```
sage: #p.show(figsize=[232,232],dpi=100) # not tested
```

So, anyone who blindly copy pastes will get nothing out of it. And has to make two mistakes to make it segfault. I think the reason this example is there is to make the user aware that unreasonable parameters will result in an uncomfortable end.


---

Comment by kcrisman created at 2014-11-10 13:15:27

That sounds very reasonable.

Jeroen, are you saying that my latest commit needs something added like the `float` business?


---

Comment by git created at 2014-11-13 19:02:40

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by kcrisman created at 2014-11-13 19:03:14

Okay, I think this is ready for review.  The `float` stuff is actually unnecessary but it can't hurt, since we definitely only want things that can be floats in there.
----
New commits:


---

Comment by jdemeyer created at 2014-11-13 20:09:39

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2014-11-13 20:09:39

Is there a check that `len(figsize) == 2`?

I would change the logic of those branches to

```
if figure is None:
    # add a good comment here
    ...
elif isinstance(figsize, (list, tuple)):
    # figsize should be two positive numbers
    if len(figsize) != 2:
        raise ValueError('...')
    ...
else:
    # figsize should be a single positive number
    figsize = float(figsize) # to pass to mpl
    if figsize <= 0:
        raise ValueError("figsize should be positive, not {0}".format(figsize))
    ...
```


And add a doctest for some non-float `figsize` argument like

```
sage: var('x')
sage: ...figsize=x...
```



---

Comment by jdemeyer created at 2014-11-13 20:10:36

The `Unhandled SIGSEGV:` message isn't the current message (which is shorter).


---

Comment by git created at 2014-11-13 21:21:53

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by kcrisman created at 2014-11-13 21:22:48

Okay, that's what I can do today.  If you really want the code reorganized that badly it will have to fall to you, I'm afraid.  But everything else should be taken care of.


---

Comment by kcrisman created at 2014-11-13 21:22:48

Changing status from needs_work to needs_review.


---

Comment by ppurka created at 2014-11-16 08:40:29

I think you have addressed Jeroen's concerns.


---

Comment by ppurka created at 2014-11-16 08:40:29

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-11-17 13:17:56

Resolution: fixed


---

Comment by kcrisman created at 2014-11-20 21:51:48

Followup #17057.
