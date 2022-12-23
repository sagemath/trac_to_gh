# Issue 7278: eval strings are not escaped

Issue created by migration from https://trac.sagemath.org/ticket/7278

Original creator: jason

Original creation time: 2009-10-24 00:02:04

Assignee: boothby

CC:  was mhansen


```
> When I put this in a cell:
> >
> > %sh
> > '''echo test to close of string
> >
> > I get:
> >
> > Traceback (most recent call last):
> >  File "<stdin>", line 1, in <module>
> >  File "_sage_input_19.py", line 4, in <module>
> >   print _support_.syseval(sh, ur\u0027\u0027\u0027\u0027\u0027\u0027echo
> > test to close of string\u0027\u0027\u0027,
> > \u0027/home/sage/sagenb/sage_notebook-alpha.sagenb/home/jason3/38/cells/6\u0027)
> >  File "", line 1
> >   print _support_.syseval(sh, ur''''''echo test to close of string''',
> > '/home/sage/sagenb/sage_notebook-alpha.sagenb/home/jason3/38/cells/6')
> >                                          ^
> > SyntaxError: invalid syntax
> >
> >
> > It looks like there was no escaping of the single quotes inside the string.
> >
> > Thanks,
> >

Can you report this as a bug to trac.  It's been around foreover.  And
I'm sure it is totally general -- i.e. happens for all the interfaces.

The solution is not to escape certain characters but to base-64 encode
everything.

William

```



---

Comment by timdumol created at 2010-01-18 19:05:13

This was fixed in #3154. Please close?


---

Comment by mhansen created at 2010-01-18 20:17:30

Resolution: invalid
