# Issue 1616: Change asin to arcsin, etc.

Issue created by migration from https://trac.sagemath.org/ticket/1616

Original creator: was

Original creation time: 2007-12-28 20:59:00

Assignee: was


```
On Dec 25, 2007 9:18 AM, David Joyner <wdjoyner@gmail.com> wrote:
>
> Hi:
>
> (a) I'm not sure if this is a bug or something missing, but it seems
> to me it should be easy to plot y=arccsc(x) in SAGE, since it
> is a basic function of trigonometry and calculus. Two problems:
> (1) it seems arccsc is not defined,

It is acsc, just like asin, etc.   This works fine:

sage: show(plot(acsc, 1,2))

> (2) after defining it, it does not seem easy to plot it:
>
> sage: acsc = lambda x: CDF(x,0).arccsc()
> sage: acsc(1.1)
> 1.14109666064
> sage: acsc(1.9)
> 0.554261834452
> sage: P = plot(RR(acsc(x)),1,2)

RR(acsc(x)) makes no sense; you're pluggin a symbolic variable into
a lambda function, then trying to convert the result to a real field element.
You meant to do

sage: acsc = lambda x: float(abs(CDF(x,0).arccsc()))
sage: show(plot(acsc, 1,2))

Sorry sage is so hard to use!  What can we learn from the above?
The main problem is acsc versus arccsc, which caused confusion.
Should we change the names of the "arc" functions to arc* instead of a*?

Maple: uses arcsin:
sage: maple.eval('arcsin(1)')
'1/2*Pi'
sage: maple.eval('asin(1)')
'asin(1)'

Mathematica: uses ArcSin:
sage: mathematica.eval('ASin[1]')
       ASin[1]
sage: mathematica.eval('ArcSin[1]')

       Pi
       --
       2

Maxima: Uses asin (which is why we currently do):
sage: maxima.eval('arcsin(1)')
'arcsin(1)'
sage: maxima.eval('asin(1)')
'%pi/2'


If nobody strongly objects in a day or two, I'll open a trac ticket
to change a*'s to arc*'s.  Better now than later.   And if something
like this is confusing David Joyner, then it's to be taken seriously.

> ---------------------------------------------------------------------------
> <type 'exceptions.TypeError'>             Traceback (most recent call last)
>
> /home/wdj/sagestuff/sage-2.8.7.rc1/<ipython console> in <module>()
>
> /home/wdj/sagestuff/sage-2.8.7.rc1/<ipython console> in <lambda>(x)
>
> /home/wdj/sagestuff/sage-2.8.7.rc1/complex_double.pyx in
> sage.rings.complex_double.ComplexDoubleField_class.__call__()
>
> /home/wdj/sagestuff/sage-2.8.7.rc1/complex_double.pyx in
> sage.rings.complex_double.ComplexDoubleElement.__init__()
>
> <type 'exceptions.TypeError'>: a float is required
>
> (b) In fact, what I'd like to do is plot in SAGE what calculus teachers draw
> frequently on the board: not just one branch of arccsc but rather
> several of them: ie, the plot of y=csc(x) over say -2\pi to 2*\pi,
> flipped about the 45^o line. Is this easy to do?

This will do it.  I hope it isn't too ugly:

sage: v = [(csc(x),x) for x in srange(-2*float(pi),2*float(pi),0.1) if x]
sage: show(line(v), xmin=-20, xmax=20)

The tricks above:
  (1) use float(pi) so the iteration through the range of inputs is very fast
  (2) don't evaluate csc at 0.
  (3) use a line and flip the order of the points in the graph.
  (4) use xmin, xmax, since otherwise one large value will through
off the whole graph.

```



---

Attachment


---

Comment by mhansen created at 2008-01-16 22:12:19

There is more work left to be done so that the functions always display as arcsin within Sage as well as making sure to treat them as asin when working with Maxima.


I will be posting a new patch here in the near future.


---

Comment by mhansen created at 2008-01-16 22:12:19

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-01-16 22:12:19

Changing status from new to assigned.


---

Attachment


---

Attachment


---

Comment by mhansen created at 2008-01-17 00:02:01

I just put up three new patches (to be applied in order) which pass -testall for me.


---

Comment by was created at 2008-01-17 00:57:34

Looks good to me.


---

Comment by mabshoff created at 2008-01-19 20:57:35

Merged all three of mahnsen's patches in Sage 2.10.1.alpha0


---

Comment by mabshoff created at 2008-01-19 20:57:35

Resolution: fixed
