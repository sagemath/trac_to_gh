# Issue 1163: assume seems to have some undesired side-effects

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2007-11-13 11:58:31

Assignee: was

CC:  burcin robertwb jason robert.marik


```
sage: assume(x > 0)
sage: sqrt(x^2)
x
sage: assume(x < 0)
sage: sqrt(x^2)
x
```


Maybe it is not allowed to make two assumptions on the same variable, without any forget inbetween, anyway the documentation should be clear about this, or a warning should be issued.
Also, is there a way to know which assumptions were made on a given variable (like about in
Maple)?




---

Comment by jason created at 2007-11-13 20:41:41

A couple of notes:

The "assumptions()" command lists assumptions.  See assumptions? for documentation.

It seems that the order in which the assumptions are made matters (only the first assumption is used below).  

Should assume complain if we say that x>0 and x<0?


```
sage: assumptions()
[]
sage: assume(x<0)
sage: sqrt(x^2)
-x
sage: assume(x>0)
sage: sqrt(x^2)
-x
sage: assumptions()
[x < 0, x > 0]
sage: forget()
sage: assumptions()
[]
sage: assume(x>0)
sage: assume(x<0)
sage: assumptions()
[x > 0, x < 0]
sage: sqrt(x^2)
x
```



---

Comment by zimmerma created at 2007-11-13 22:51:26

Sorry I did not know about the assumptions() command. Maybe assume? should point to it.
Is a SEE ALSO section possible in the documentation? Also consider (from Wester's test suite):


```
sage: assume(x>=y, y>=z,z>=x)
sage: assumptions()
[x >= y, y >= z, z >= x]
sage: print bool(x==z)
False
```


Yes assume should complain if we say that x>0 and x<0 (at least if it can lead to wrong results).


---

Comment by zimmerma created at 2007-11-13 22:53:44

More strange results:

```
sage: assume(x > 0)
sage: bool (x <> 1)
True
```

and:

```
sage: assume(x <= 1, x >= 1)
sage: bool(x==1)
False
```



---

Comment by jason created at 2007-11-14 00:12:04

Those are some unsettling results.  I don't know if this is the easiest route, but it seems like QEPCAD could handle some of these if it were integrated into SAGE.  For example, we can ask QEPCAD the following questions.  In these, (Ex) means "there exists an x" and (Ax) means "For all x" and "/=" means  "not equal".

 * `(Ex)(Ey)(Ez) [ x>=y /\ y>=z /\ z>=x /\ x/=z]` (returns False)
 * `(Ex) [ x>0 /\ x/= 1]` (returns True)
 * `(Ex) [ x>0 /\ x=1]` (returns True)
 * `(Ex) [ x<=1 /\ x>=1 /\ x /= 1]` (returns False)

Here's another example:

 * `(Ax)(Ay) [x<sup>2+y</sup>2>=0]` (returns True).

We could ask much more general questions too.

I've been (very slowly) working on interfacing QEPCAD to SAGE, but lack of time and the learning process of making an interface is slowing me down.  Also, we need to follow up on the license issue.  For progress in this interface, see #772 )


---

Comment by jason created at 2007-11-14 00:33:36

Apparently Maxima complains (behind the scenes?):


```
Maxima 5.12.0 http://maxima.sourceforge.net
Using Lisp GNU Common Lisp (GCL) GCL 2.6.7 (aka GCL)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) assume(x<0);
(%o1)                               [x < 0]
(%i2) assume(x>0);
(%o2)                           [inconsistent]
```



---

Comment by jason created at 2007-11-14 00:43:11

More results from Maxima:


```

Maxima 5.12.0 http://maxima.sourceforge.net
Using Lisp GNU Common Lisp (GCL) GCL 2.6.7 (aka GCL)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) assume(x>=y,y>=z,z>=x);
(%o1)                      [x >= y, y >= z, z >= x]
(%i2) is(x=z);
(%o2)                                false
```



```
Maxima 5.12.0 http://maxima.sourceforge.net
Using Lisp GNU Common Lisp (GCL) GCL 2.6.7 (aka GCL)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) assume(x>0);
(%o1)                               [x > 0]
(%i2) is(x#1);
(%o2)                                true
```


and


```

Maxima 5.12.0 http://maxima.sourceforge.net
Using Lisp GNU Common Lisp (GCL) GCL 2.6.7 (aka GCL)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) assume(x<=1);
(%o1)                              [x <= 1]
(%i2) assume(x>=1);
(%o2)                              [x >= 1]
(%i3) is(x=1);
(%o3)                                false
```


So it seems like the problem is the Maxima assumptions engine.  According to the documentation at  http://maxima.sourceforge.net/docs/manual/en/maxima_11.html 

```
Maxima's deduction mechanism is not very strong; there are many obvious consequences which cannot be determined by is. This is a known weakness.
```



---

Comment by jason created at 2007-11-14 01:21:11

One more note: 

QEPCAD also simplifies the expression [x>=y /\ y>=z /\ z>= x] to [y-x=0 /\ z-y = 0].


---

Comment by gfurnish created at 2008-03-16 20:11:30

Changing assignee from was to gfurnish.


---

Comment by gfurnish created at 2008-03-16 20:11:30

Changing status from new to assigned.


---

Comment by kcrisman created at 2009-01-29 16:42:34

At the very least this ticket should upgrade the documentation for assume? and assumptions?  to point out that one should always forget() before assuming something new about a variable.

A related ticket is #3277, which would implement a block to automatically call assume and forget if desired.  Also, #772 is now an experimental spkg.


---

Comment by kcrisman created at 2009-09-28 18:09:52

A very interesting exchange on the Maxima list indicates that Maxima isn't so much at fault as Sage's use of it, even in the sketchy-looking cases.  This is Robert Dodier's response:

```
Well, it's true that assume isn't very strong, but at least Maxima
seems to be able to figure out these examples.
What you want is equal(x, z) instead of x = z.
"=" is essentially identity (i.e. are the left and right-hand sides
the same expression), while equal is equivalence (equal value).
Likewise the distinction between "#" and notequal.

Here's what I get with Maxima 5.19.2.

(%i2)  assume(x>=y,y>=z,z>=x);
(%o2)                      [x >= y, y >= z, z >= x]
(%i3) is(equal(x,z));
(%o3)                                true
(%i4) assume(a>=1,1>=a);
(%o4)                          [a >= 1, a <= 1]
(%i5) is(equal(a,1));
(%o5)                                true
(%i6) assume(b>1);
(%o6)                               [b > 1]
(%i7) is(equal(b,1));
(%o7)                                false
(%i8) is(notequal(b,1));
(%o8)                                true

I think %o3, %o5, %o7, and %o8 are all as expected, right?
```


So the real issue is that Sage's "==" is more at Maxima's equal(), while Sage's "is" is more at Maxima's "=".  Fixing this will probably require some interesting futzing with the Maxima parser, though, since usually we want == to become =, I think.


---

Comment by kcrisman created at 2009-10-01 14:39:34

Another comment:
With Pynac symbolics, we do not (unfortunately?) simplify sqrt(x^2) even when we assume things about it.  Interestingly, that is not true for other things, such as a neat example in the documentation.

```
sage: assume(x<0)
sage: sqrt(x^2)
sqrt(x^2)
sage: sqrt(x^2).simplify() # doesn't simplify this
sqrt(x^2)
sage: sqrt(x^2).simplify_full()  # does what used to happen
-x
sage: assumptions()
[x < 0]
sage: forget()
sage: assume(x,'integer')
sage: sin(x*pi)
sin(pi*x)
sage: sin(x*pi).simplify() # nice simplification
0
sage: assumptions()
[x is integer]
sage: forget()
```

So it's good the bug was discovered when it was.


---

Comment by kcrisman created at 2009-10-01 15:31:48

Okay, the following patch (which depends on #7084, I think), resolves *most* of the issues in this ticket.  See below for the one it doesn't, and comments.

```
sage: assume(x<=1)
sage: assume(x>=1)
sage: assumptions()
[x <= 1, x >= 1]  # so far, so good
sage: b = x!=1
sage: b.__nonzero__() 
True # WRONG
sage: bool(b) 
True # WRONG
sage: bool(x==1)
True # right!
sage: forget()
sage: var('x,y,z')
(x, y, z)
sage: assume(x>=y,y>=z,z>=x)
sage: assumptions()
[x >= y, y >= z, z >= x]
sage: bool(x==z)
True # right!
sage: forget()
sage: assume(x>0)
sage: bool(x<>1) # NO!
True
sage: bool(x!=1) # NO!  And note that Python considers <> and != to be identical
True
sage: bool(x==1)
False # right!
```

I've narrowed the problem down to the fact that __nonzero__ has the following lines:

```
            res = relational_to_bool(self._gobj)
            if res:
                return True
```

If you put this code after determining whether you need assumptions, practically every evaluation of bool() yields an infinite loop.  But for some reason the function relational_to_bool (like all these Ginac functions, completely unsearchable because they live somewhere outside of devel/sage) doesn't send (at least) != to the assumptions.  Here is the wrapper code, in c_lib/include/ginac_wrap.h:

```
bool relational_to_bool(const ex& e) {
    if (ex_to<relational>(e))
	return 1;
    else
	return 0;
}
```

Now what?  The documentation of ex_to in Ginac, even when I found it on their website, really only will make sense to someone with good C++ knowledge.


---

Attachment

Based on 4.1.2.alpha4, depends on #7084


---

Comment by kcrisman created at 2009-10-01 15:36:15

Oh, and just for the record, continuing in the same session, where we assumed x>0:

```
sage: bool(x>1)
False # right!
sage: bool(x>-1)
True # right!
```

So the problem really does seem to be the Ginac handling of !=, not something else.


---

Attachment

Based on 4.1.2.alpha4, depends on #7084


---

Comment by kcrisman created at 2009-10-02 16:12:25

The non-experimental patch resolves all but one of the issues above (about which more below).   It also fixes a SLEW of subtle problems and provides better checking in the assumptions code, and fixes a variety of doctests which are improvements (!) based on making assumptions better.   I didn't end up changing the documentation to tell people to use forget, but instead gave lots of examples of what Errors you get if you assume something redundant or inconsistent.

The one "problem" which is still extant is the following:

```
sage: assume(x>0)
sage: bool(x!=1) 
True
```


This is something to which Maxima replies 'unknown', which is a lot better than True or False.  However, Sage doesn't currently have that as an option (that would be a separate ticket, and not necessarily a desirable one).   Further, since anytime one compares a symbolic variable, e.g.

```
def func(x,y):
    if x is not y:
        do something great
    else:
        blow a gasket
```

Expression.__nonzero__ is called, we are forced to have x!=1 be True, since x==1 is False, seeing as != and == have opposite truth tables.  For an example of what can go wrong, see the change made in this patch to desolvers.py, where having x!=1 be False originally meant there was no dependent variable; this one was fixable, but the fact that symbolic matrices essentially all go to zero (!) after making that change was much worse.  

So I have left it alone after checking as many cases as I could, and we'll just have to live with it, unless someone can figure out how to get around this.  I think it's really just a conflict between wanting to say that x!=1 is True unless you are sure that x==1, and wanting to say that x!=1 is False unless you are sure that x!=1; there is no nonstandard logic option for Python.


---

Comment by kcrisman created at 2009-11-10 02:42:52

Okay, with respect to [this discussion](http://groups.google.com/group/sage-devel/browse_thread/thread/ae7d15985d4735cb) on this update adds correct parsing of Maxima output with #, thus:

```
sage: a = maxima("x#0")
sage: a.sage()
x != 0
```

Apply only 'final' patch.


---

Attachment


---

Comment by robert.marik created at 2009-11-10 07:07:14

The code looks good and gives important improvements in Sage. The patch should be installed on the top of #385 (which has been merged in 4.2.1).

Pases tests in sage/calculus and sage/symbolic

More changes in desolvers.py should be done, if the patch is applied on the top of patch #6479, which already got positive review and introduces another lines like 

```
ivars = [t for t in ivars if t != dvar] 
```

which now became problematic.

If it passes all tests and builds documentation (runnning now, takes a long time on my PC) I'll switch the status to posistive review.


---

Comment by robert.marik created at 2009-11-10 08:44:32

Changing status from needs_review to positive_review.


---

Comment by robert.marik created at 2009-11-10 08:44:32

When running "make test" I got 

```
sage -t  "/opt/sage/devel/sage/sage/modules/vector_real_double_dense.pyx"
**********************************************************************
File "/opt/sage/devel/sage/sage/modules/vector_real_double_dense.pyx", line 72:
    sage: v.stats_skew()
Expected:
    0.0
Got:
    doctest:106: SyntaxWarning: assertion is always true, perhaps remove parentheses?
    0.0
**********************************************************************
```

But if I run doctesting by hand to this file only, everything is O.K.

Since this is syntax warinng and not error, I give positiev review. But this should be fiexd as well.


---

Comment by kcrisman created at 2009-11-10 14:17:03

Replying to [comment:17 robert.marik]:
> When running "make test" I got 
> {{{
> sage -t  "/opt/sage/devel/sage/sage/modules/vector_real_double_dense.pyx"
> **********************************************************************
> File "/opt/sage/devel/sage/sage/modules/vector_real_double_dense.pyx", line 72:
>     sage: v.stats_skew()
> Expected:
>     0.0
> Got:
>     doctest:106: SyntaxWarning: assertion is always true, perhaps remove parentheses?
>     0.0
> **********************************************************************
> }}}
> But if I run doctesting by hand to this file only, everything is O.K.
> 
> Since this is syntax warinng and not error, I give positiev review. But this should be fiexd as well.
> 

This is actually #6825, so it's unrelated.

Depending on how the release manager does things, we'll see which patch to resolve the != thing on; it shouldn't be a big deal.


---

Comment by mhansen created at 2009-11-19 17:35:36

Resolution: fixed
