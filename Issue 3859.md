# Issue 3859: Line's corner_cutoff is poorly documented, and buggy

Issue created by migration from Trac.

Original creator: mclean

Original creation time: 2008-08-14 22:11:31

Assignee: was

CC:  jason kcrisman

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






---

Comment by mclean created at 2008-08-14 22:28:11

See also the related: #3861


---

Comment by chapoton created at 2014-12-27 21:00:17

Changing status from new to needs_review.


---

Comment by chapoton created at 2014-12-27 21:00:17

Here is a proposal, that corrects several minor wrong points in the code of *Line* and add more doc.
----
New commits:


---

Comment by kcrisman created at 2015-01-27 02:12:04

See also http://ask.sagemath.org/question/25609/how-to-find-the-full-argument-list-of-a-built-in-function/ - amazingly, I have never heard of this!


---

Comment by chapoton created at 2015-03-25 20:32:09

Hello, review, anybody ?


---

Comment by mmezzarobba created at 2015-04-09 08:11:17

Either I don't understand the description of what `corner_cutoff` is supposed to do, or the first example from the ticket's description still doesn't work for me:

```
sage: line3d([[-1, 3, 369.26], [-1, -10.11, 125.33], [0.21, -10.13, 99.42]], corner_cutoff = 1)
```

produces a smooth line in jmol.


---

Comment by chapoton created at 2015-04-29 12:48:34

I guess there is still a problem.


---

Comment by chapoton created at 2015-04-29 12:48:34

Changing status from needs_review to needs_work.


---

Comment by git created at 2015-10-19 19:33:40

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-10-19 19:37:21

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2015-10-19 19:37:21

This should be better now:

`corner_cutoff = -1` : no smoothing

`corner_cutoff = 1` : all points smoothed

and smoothing is performed in general if the angle is close enough to pi, meaning
that successive segments are close to being aligned.


---

Comment by chapoton created at 2015-11-09 16:38:19

ping ? should be an easy review !


---

Comment by chapoton created at 2015-12-14 19:24:05

PING ? nobody out there ?


---

Comment by kcrisman created at 2015-12-16 03:40:36

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

For instance, I would say that the angle is nearly _zero_ if the segments "keep on going" and is close to 180 degrees if the segments change direction (peak).  So the original seems closer to my thinking - it's not the angle at the actual point of contact of the two segments, but rather the angle between the _vectors_ formed by the two (directed) line segments that is in question.

Does that make sense?

I also have to admit that with #3861 that the output of 

```
Line([(0,0,0),(1,0,0),(2,1,0),(0,1,0)],corner_cutoff=-.5) # current ticket
```

is bizarre and does not look like the 2d version style in any case.

Anyway, otherwise this seems to work as advertised.  Should end users have access to `max_len` in `Line`?  Currently I don't think that's really possible.  But maybe that's okay.


---

Comment by git created at 2015-12-20 20:49:28

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-12-20 20:53:34

Thanks for having a look. I know well that time is precious.

I have now, as required, changed back to the original convention that angle 0 means that
the path goes straight. I hope I have made no error in doing that.

Maybe this is good enough, for a 7 years old ticket ?


---

Comment by chapoton created at 2016-01-21 20:21:36

**ping** ?


---

Comment by tscrim created at 2016-01-21 22:03:01

This LGTM, but I'd like to see if Karl-Dieter has any more comments before we set this to a positive review.


---

Comment by kcrisman created at 2016-01-22 00:56:12

If Travis can confirm that the original convention is now followed and that the awesome examples still look as they should, please do put it to positive!  I just continue to have no time for anything involving branches :( somehow that takes me much more time than e.g. reporting tickets.


---

Comment by tscrim created at 2016-01-22 02:30:40

AFAIK it is correct. At the very least, it is better than the current behavior of erroring out.


---

Comment by tscrim created at 2016-01-22 02:30:40

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-01-23 20:42:40

Resolution: fixed
