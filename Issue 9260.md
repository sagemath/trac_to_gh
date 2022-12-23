# Issue 9260: missing pointer in documentation

Issue created by migration from https://trac.sagemath.org/ticket/9260

Original creator: zimmerma

Original creation time: 2010-06-18 09:52:05

Assignee: mvngu

CC:  kcrisman

The documentation from `RealIntervalField` says:

```
       See the documentation for ``RealIntervalField_class`` for many more
       examples.
```

However there is no documentation for `RealIntervalField_class`:

```
sage: RealIntervalField_class?
Object `RealIntervalField_class` not found.
```



---

Comment by kcrisman created at 2012-01-12 15:50:48

Current code is actually

```

    See the documentation for :class:`RealIntervalField_class` for many more
    examples.

```


So this would just have to add a little so that users at the command line could see where to find this; in the documentation it would still look the same and have the right link.


---

Comment by zimmerma created at 2012-01-13 08:24:54

Karl-Dieter,
do you know how to find the documentation from the command line?

```
sage: :class:RealIntervalField_class?
Object `:class:RealIntervalField_class` not found.
```

Paul


---

Comment by kcrisman created at 2012-01-13 19:31:27

Yes, and I thought one of my students had made a patch for this.  It turns out to live in `sage.rings.real_mpfi.RealIntervalField_class?`


---

Comment by kcrisman created at 2012-05-26 19:57:53

I see what you were asking now in comment:3.  Most Sage documentation now has these hyperlinks, but it does mean one has to ignore the backticks and things like `:class` or `:meth:`.  I think this is standard now.

```
sage.rings.real_mpfi.RealIntervalField_class?
```

is the correct command, and the patch coming up changes the doc so that this can at least be found, modulo the extra formatting.


---

Comment by kcrisman created at 2012-05-26 19:57:53

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-05-26 19:58:39

Based on Sage 5.1.beta0


---

Attachment


---

Comment by kcrisman created at 2012-05-26 19:59:31

Changing keywords from "" to "sd40.5".


---

Comment by kini created at 2012-05-26 22:32:41

Other than the fact that you have created an excessively long line in the docstring, this ticket looks good to go.


---

Comment by kini created at 2012-05-26 22:32:41

Changing status from needs_review to positive_review.


---

Comment by kini created at 2012-05-27 17:00:02

apply to $SAGE_ROOT/devel/sage


---

Attachment

Here's a reviewer patch to fix the "excessively long line", per your suggestion :)


---

Comment by kini created at 2012-05-27 17:00:57

patchbot, please, please, please apply trac_9260.patch trac_9260.reviewer.patch (pretty please)


---

Comment by jdemeyer created at 2012-06-09 19:23:04

Please fill in your real name in the Author / Reviewer fields.


---

Comment by kini created at 2012-06-09 19:29:20

Done.


---

Comment by kcrisman created at 2012-06-10 00:39:41

Hmm, that is a good change in the reviewer patch - I wasn't aware that syntax was an option.

Jeroen, I think you know who kini is - wouldn't that have taken fewer characters?  ;-)


---

Comment by kini created at 2012-06-10 01:06:07

Jeroen is correct in asking me to add my name. Ideally a release manager should need to do as little work as possible - and what work he does do should be limited to administrative oversight. The more automation we can add to the system of getting Sage releases out, the better.


---

Comment by kcrisman created at 2012-06-10 04:47:58

I agree that you (or I) should have done it!  I was just pointing out that in this particular case it actually took him more effort than doing it himself - hence the winky emoticon.  Presumably this will save him effort in the long run, though, I agree.


---

Comment by kini created at 2012-06-11 03:01:44

Well, since he left exactly the same message on two other tickets which I had forgotten to put my name on, there's a strong possibility that he had scripted it :) And that's a good thing!


---

Comment by jdemeyer created at 2012-06-18 10:22:07

Resolution: fixed
