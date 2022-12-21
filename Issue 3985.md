# Issue 3985: Asymptote plotting

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2008-08-29 02:28:48

Assignee: was

Plotting functions like 1/x, tan, etc. have asymptotes essentially plotted in Sage at this point.  This is okay, except that the scale is way out of whack, so things look very odd.  Sage should either remove the asymptote piece of these plots somehow (how is not obvious) or fix the ymin and ymax in show so that it just looks like the asymptotes are plotted.  
E.g.

```
sage: plot(tan,-20,20).show(ymin=-5, ymax=5) 
```

except automatic detection of the ymin and ymax.


---

Comment by mabshoff created at 2008-09-09 04:53:27

Hmm, I am wondering if #3907 fixed this issue?

Cheers,

Michael


---

Comment by kcrisman created at 2008-09-09 19:20:02

I doubt it, because e.g. the tangent example above usually won't get 'inf' or '-inf' as something in ydata; it just has weird things happen near asymptotes because of the adaptive plotting, and also will occasionally get random points that are really far from y=0.   I'll try it when 3.1.2 comes out, though.

It's actually kind of fun to evaluate the above command again and again, seeing what you get each time... If you try a few times you can get a ydata point that is 10000 or even more, which requires only that plot "guesses" a number within 10<sup>-5</sup> of pi/2 for the xdata...


---

Comment by kcrisman created at 2009-05-21 18:50:51

Just FYI, #6035 partially resolves this.  

However, 

```
sage: plot(tan,-20,20, detect_poles='show')
sage: plot(tan,-20,20, detect_poles=True)
```

shows that 'show' still keeps the "missing" points (which include not just the asymptote but also the high slopes on either side) and that True doesn't create a uniform height as one might desire in the Description.  

Description changed to indicate this successful partial resolution, however!


---

Comment by jason created at 2010-03-17 05:19:17

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2013-01-14 15:42:59

See also #8341.
