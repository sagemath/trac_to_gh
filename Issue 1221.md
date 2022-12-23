# Issue 1221: Use Mathematica syntax for integration

Issue created by migration from https://trac.sagemath.org/ticket/1221

Original creator: certik

Original creation time: 2007-11-20 22:22:35

Assignee: was

CC:  jason

I think we should use this syntax for integration:

```
>>> integrate(x**3, (x, -1, 1))
0
>>> integrate(sin(x), (x, 0, pi/2))
1
>>> integrate(cos(x), (x, -pi/2, pi/2))
2
```


instead of

```
sage: integral(x/(x^2+1), x, 0, 1)
     log(2)/2
```


as in SAGE currently, to be close to Mathematica. Because then you can
use the syntax:

integrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))

for multiple integrals.

See also [1], how we discussed this in SymPy.

[1] http://code.google.com/p/sympy/issues/detail?id=25


---

Comment by was created at 2007-11-21 16:11:19

I changed this to sage-2.9, since it will be very easy to implement.


---

Comment by was created at 2007-11-21 16:11:57


```
Sage math appInbox
Reply to all
Forward
Reply by chat
Filter messages like this
Print
Add to Contacts list
Delete this message
Report phishing
Report not phishing
Show original
Message text garbled?
Why is this spam/nonspam?
chris@seberino.org	
W. Stein I wanted to commend you for leading Sage. I think it is a great idea...
	
Nov 19 (2 days ago)
William Stein	
On Nov 20, 2007 11:10 AM, seberino@spawar.navy.mil So do I. I think we should...
	
11:17 AM (20 hours ago)
Ondrej Certik to sage-devel
	
show details 2:22 PM (17 hours ago)
	
	
	
Reply
	
	

On Nov 20, 2007 8:17 PM, William Stein <wstein@gmail.com> wrote:
>
> On Nov 20, 2007 11:10 AM, seberino@spawar.navy.mil
> <seberino@spawar.navy.mil> wrote:
> > > As to syntax, I think in Python we could use:
> > > >>> integrate(cos(x), (x, -pi/2, pi/2))
> > >  Because then you can
> > > use the syntax:
> > >
> > > integrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))
> > >
> > > for multiple integrals. But anyway, it's just a cosmetic issue.
> >
> > When I commended Sage's syntax I was assuming you were using this
> > Mathematica like syntax already.  I agree with Ondrej and think his
> > suggestion above is the way to go.
>
> So do I.  I think we should change that functions as suggested.  Anybody
> want to submit a patch?  Ondrej, could you create a trac ticket making precise
> what you want, etc.?

http://sagetrac.org/sage_trac/ticket/1221

Ondrej
- Show quoted text -

--~--~---------~--~----~------------~-------~--~----~
To post to this group, send email to sage-devel@googlegroups.com
To unsubscribe from this group, send email to sage-devel-unsubscribe@googlegroups.com
For more options, visit this group at http://groups.google.com/group/sage-devel
URLs: http://sage.scipy.org/sage/ and http://modular.math.washington.edu/sage/
-~----------~----~----~----~------~----~------~--~---

Reply
		
Forward
		
	
Stephen Forrest to sage-devel
	
show details 2:44 PM (17 hours ago)
	
	
	
Reply
	
	

On Nov 20, 2007 2:10 PM, seberino@spawar.navy.mil
<seberino@spawar.navy.mil> wrote:

[snip]
> >  Because then you can
> > use the syntax:
> >
> > integrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))
> >
> > for multiple integrals. But anyway, it's just a cosmetic issue.
>
> When I commended Sage's syntax I was assuming you were using this
> Mathematica like syntax already.  I agree with Ondrej and think his
> suggestion above is the way to go.

This probably goes without saying, but presumably after the change one
will still be able to use the syntax 'integrate(sin(x),x) ' for
indefinite integration?  That is, the second argument may be a triple
or a symbol?

Steve
- Show quoted text -

--~--~---------~--~----~------------~-------~--~----~
To post to this group, send email to sage-devel@googlegroups.com
To unsubscribe from this group, send email to sage-devel-unsubscribe@googlegroups.com
For more options, visit this group at http://groups.google.com/group/sage-devel
URLs: http://sage.scipy.org/sage/ and http://modular.math.washington.edu/sage/
-~----------~----~----~----~------~----~------~--~---

Reply
		
Forward
		
Invite Stephen Forrest to chat
	
Ondrej Certik to sage-devel
	
show details 5:11 PM (14 hours ago)
	
	
	
Reply
	
	

On Nov 20, 2007 11:44 PM, Stephen Forrest <stephen.forrest@gmail.com> wrote:
>
> On Nov 20, 2007 2:10 PM, seberino@spawar.navy.mil
> <seberino@spawar.navy.mil> wrote:
>
> [snip]
> > >  Because then you can
> > > use the syntax:
> > >
> > > integrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))
> > >
> > > for multiple integrals. But anyway, it's just a cosmetic issue.
> >
> > When I commended Sage's syntax I was assuming you were using this
> > Mathematica like syntax already.  I agree with Ondrej and think his
> > suggestion above is the way to go.
>
> This probably goes without saying, but presumably after the change one
> will still be able to use the syntax 'integrate(sin(x),x) ' for
> indefinite integration?  That is, the second argument may be a triple
> or a symbol?

Exactly as you say.

Ondrej
- Show quoted text -
```



---

Comment by mhansen created at 2007-12-06 21:10:21

Changing component from algebraic geometry to calculus.


---

Comment by mhansen created at 2007-12-06 21:10:21

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-12-06 21:10:21

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-10 08:08:29

This will break backward compatibility in a massive way, so I would suggest setting it to "won't fix".

Cheers,

Michael


---

Comment by certik created at 2008-08-31 00:06:05

Well, I haven't replied here when you suggested won't fix, as I was thinking about this.

I understand that breaking code is bad.

But still consistency is consistency. There are ways to improve the API in a non compatible way, e.g. introduce both versions and raise python warning for the old API. and after couple releases, remove it.

Also this was agreed on the sage-devel, so if you seek a different conclusion, you should (imho) advocate that on the list.


---

Comment by jwmerrill created at 2008-08-31 14:40:47

See also #2787.


---

Comment by burcin created at 2010-05-01 21:10:05

I suggest we close this ticket since we now support the suggested syntax:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: integrate(x**3, (x, -1, 1))
0
sage: integrate(sin(x), (x, 0, pi/2))
1
sage: integrate(cos(x), (x, -pi/2, pi/2))
2
```

| Sage Version 4.4.1.alpha2-patched, Release Date: 2010-04-29        |
| Type notebook() for the GUI, and license() for information.        |
The docstring for `sage.misc.functional.integrate()` and `sage.symbolic.integration.integral.integral()` contains plenty of doctests to test the tuple syntax.

Further discussion on
 * implementing multiple integrals with `integrate(cos(x*y), (x, -pi/2, pi/2), (y, 0, pi))` and
 * replacing the examples in the docstrings with the tuple syntax and deprecating the old one
can be continued in #2787.

Comments?


---

Comment by robert.marik created at 2010-08-24 20:13:13

I think so, the one-variable issue is resolved and the double integrals are covered in #2787


---

Comment by robert.marik created at 2010-08-24 20:13:13

Changing status from new to needs_info.


---

Comment by burcin created at 2010-09-08 12:29:13

Resolution: fixed


---

Comment by burcin created at 2010-09-08 12:29:13

I'm closing this as fixed. See comment:8 for more info.
