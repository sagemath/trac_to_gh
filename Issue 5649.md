# Issue 5649: plot doesn't work when x-range too small

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-31 15:48:08

Assignee: was


```
How about:

plot(P(6.403124+x), 0, 0.00001) -> okay
plot(P(6.403124+x), 0, 0.000001) -> tick marks on both axes are
missing
plot(P(6.403124+x), 0, 0.0000001) -> IndexError: list index out of
range
plot(P(x), 0, 0.0001) -> ZeroDivisionError: float division

This doesn't look too good...
```




---

Comment by kcrisman created at 2009-06-26 18:39:33

See [http://groups.google.com/group/sage-devel/browse_thread/thread/ddd9584a4bf457db](http://groups.google.com/group/sage-devel/browse_thread/thread/ddd9584a4bf457db) for a y-axis variant on this, namely


```
plot(2^(-20*x),(x,1,10)) 
```



---

Comment by kcrisman created at 2009-06-26 20:29:57

Changing status from new to assigned.


---

Comment by kcrisman created at 2009-06-26 20:29:57

Changing assignee from was to kcrisman.


---

Comment by kcrisman created at 2009-06-26 20:29:57

This patch fixes most of the problems above, and has a doctest for it.

This does not fix the final example, because that is a bug in _tasteless_ticks and the numbers it is inputting to srange (presumably someone step is 0, though I couldn't reproduce it with actual numbers).  Assuming this patch is okay, recommend opening a separate ticket for improving _tasteless_ticks handling of small numbers.


---

Attachment

I would like to review this patch, but I don't understand how to reproduce the bug. What is "P" from the examples in the ticket description?


---

Comment by kcrisman created at 2009-07-16 18:52:25

It was from a sage-devel discussion the reporter didn't include (http://groups.google.com/group/sage-devel/browse_thread/thread/0e9c7b897851e5de).    Anway, 

```
P(x)=5*x^2 - 205 
```

in that case. But you can replicate it by making sure you have a small enough range (e.g. somewhat less than <10**-6) on any plot.   There's a small chance this will have to be rebased, but I hope that no one has been messing with axes much recently.


---

Comment by wcauchois created at 2009-07-16 19:09:20

Replying to [comment:4 kcrisman]:

It applies fine to Sage 4.1. The first three examples work great with your changes, but the last one still raises a ZeroDivisionError. I'm using that function you gave me. Is there still a problem?


---

Comment by kcrisman created at 2009-07-16 19:12:29

No, as I say above, that is a problem with _tasteless_ticks and its handling of small numbers.  That should really be in a separate ticket, but I don't want to open it until I'm ready to tackle it.  You can feel free to do so, however :)


---

Comment by wcauchois created at 2009-07-16 19:59:22

REFEREE REPORT

I'd like to give this a positive review. Applies fine to Sage 4.1, and plot tick marks work better now in a great many cases.

I feel like the readability of _tasteful_ticks() could be improved. Better variable names would help ("d0", "d1", and "p" were hard to decipher). It also looks like there is some duplicated code that could be factored out into a separate method like maybe "extract_two_digits_and_place_value". We can leave the refactor for another ticket perhaps :).


---

Comment by mvngu created at 2009-07-16 22:59:33

Resolution: fixed


---

Comment by kcrisman created at 2009-07-17 13:00:48

> I feel like the readability of _tasteful_ticks() could be improved. Better variable names would help ("d0", "d1", and "p" were hard to decipher). It also looks like there is some duplicated code that could be factored out into a separate method like maybe "extract_two_digits_and_place_value". We can leave the refactor for another ticket perhaps :).

See #6548.  In general there is a lot of work that could be done in axes.py when it comes to documentation and functionality.  There are several other open tickets that have partial code to either significantly rewrite it or to use matplotlib axes - but so far both these solutions have proved more difficult than just slowly improving what already exists.
