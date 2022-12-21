# Issue 4458: tutorial and reference manual should explain NameError

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-11-07 01:39:27

Assignee: tba

CC:  kcrisman

Perhaps even a blurb about variables being references (if it's not to complicated). However, at the very least there should be something in the calculus section(s) to the effect of "If you get a NameError, check to see if you either misspelled something or forgot to define a variable with var(...)"



---

Comment by jason created at 2010-05-26 15:17:20

Changing keywords from "" to "beginner".


---

Comment by afleckenstein created at 2012-12-21 14:11:45

I think that the section [Some Common Issues With Functions](http://www.sagemath.org/doc/tutorial/tour_functions.html) in the tutorial explains it quite well. The patch I added specifies an error that is mentioned as a NameError, not just "an error," and is also more specific about how to fix it.


---

Comment by afleckenstein created at 2012-12-21 14:14:41

Changing status from new to needs_review.


---

Comment by knsam created at 2013-01-31 03:30:46

Hello! 

I have two comments about the patch: there is a grammatical error: "an NameError" and I think "NameError" should be codified -- by enclosing it with two backticks. 

So, needs_work. :)


---

Comment by knsam created at 2013-01-31 03:31:10

Changing status from needs_review to needs_work.


---

Attachment

Replying to [comment:5 knsam]:
> Hello! 
> 
> I have two comments about the patch: there is a grammatical error: "an NameError" and I think "NameError" should be codified -- by enclosing it with two backticks. 
> 
> So, needs_work. :) 

Thanks for the input!


---

Comment by afleckenstein created at 2013-02-01 14:01:20

Changing status from needs_work to needs_review.


---

Comment by afleckenstein created at 2013-02-01 14:01:39

Changing assignee from tba to afleckenstein.


---

Comment by knsam created at 2013-02-01 16:00:48

Hello! 

Sorry for not being complete last time. I have one last comment, I am really sorry for doing this:

The description in the patch says: 'at the very least there should be something in the calculus section(s) to the effect of "If you get a NameError?, check to see if you either misspelled something or forgot to define a variable with var(...)"'. 

I think this could be done, by adding a note. Can you please do this, so that there is an explicit place where this is explained? I am also thinking if it might be possible to implement the first suggestion in the description. Hope you'd find an appropriate place to do so. 

Regards, Kannappan.


---

Comment by knsam created at 2013-02-02 15:51:20

Changing status from needs_review to needs_info.


---

Attachment

Replying to [comment:9 knsam]:
> The description in the patch says: 'at the very least there should be something in the calculus section(s) to the effect of "If you get a NameError?, check to see if you either misspelled something or forgot to define a variable with var(...)"'. 
> 
> I think this could be done, by adding a note. Can you please do this, so that there is an explicit place where this is explained? I am also thinking if it might be possible to implement the first suggestion in the description. Hope you'd find an appropriate place to do so. 

Done! I added it to a separate patch, so you can pick either one, or both :-)


---

Comment by afleckenstein created at 2013-02-07 14:15:52

Changing status from needs_info to needs_review.


---

Comment by kcrisman created at 2013-02-12 16:04:42

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2013-02-12 16:04:42

I feel like these are ... a little dangerous.

First, 

```
are defined to be ``var(...)``
```

Is there a noun missing here?  Or "via", or "exist using"?


```
sage: diff(sin(var('u')), var('u'))
```

I'm a little leery of suggesting people do this.  `var('u')` injects things into the global namespace as well, so this is redundant.  Better is

```
sage: var('u')
diff(...)
```


Also, I suspect you'll need an extra line before the new section

```
.. _section-systems: 
```

to avoid some documentation build error.


---

Comment by afleckenstein created at 2013-02-13 14:09:27

Replying to [comment:12 kcrisman]:

>`var('u')` injects things into the global namespace as well, so this is redundant.

I didn't know this happened! That's pretty neat. Why do we have

```
u = var('u')
```

in the tutorial then? Is 

```
var('u')
```

shorthand for u = var('u'), or does it do something a little different?

Andrew


---

Comment by kcrisman created at 2013-02-13 15:49:14

Compare

```
sage: u = var('u')
sage:
```

with 

```
sage: var('u')
u
sage:
```

That's my reason, anyway.  There may be some very subtle other difference as well.


---

Comment by tscrim created at 2013-03-29 22:53:49

You can just get this behavior:

```
sage: v = var('u')
sage: u
u
sage: v
u
```



---

Comment by kcrisman created at 2014-11-20 18:16:16

I'm happy, having done the branch, but I'd appreciate a separate reviewer.
----
New commits:


---

Comment by kcrisman created at 2014-11-20 18:16:16

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2014-12-31 10:50:03

Works for me !

Nathann


---

Comment by ncohen created at 2014-12-31 10:50:03

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-01-02 15:46:32

Resolution: fixed
