# Issue 6942: jordan_form with transformation=true returns non-invertible transformation

Issue created by migration from https://trac.sagemath.org/ticket/6942

Original creator: syazdani

Original creation time: 2009-09-16 01:35:43

Assignee: tbd

CC:  jason

Keywords: jordan_form, transformation

The following code returns an incorrect result:

```
mm=Matrix(GF(2),[[1,0,1,0,0,0,1],[1,0,0,1,1,1,0],[1,1,0,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,0,0,1,0],[1,1,1,0,1,0,0],[1,1,1,1,1,1,0]])
_,S = mm.jordan_form(transformation=True)
S.rank()
```

S should be invertible, so the rank should be 7, but the rank of the above is 5.


---

Comment by AlexGhitza created at 2009-11-15 13:07:45

Changing component from algebra to linear algebra.


---

Comment by jason created at 2009-11-23 23:33:21

According to Magma:


```
u,v:=JordanForm(Matrix(GF(2),7,7,StringToIntegerSequence("1 0 1 0 0 0 1 1 0 0 1 1 1 0 1 1 0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0 0 1 0 1 1 1 0 1 0 0 1 1 1 1 1 1 0")));

print "jordan form:";
u;
print "transformation";
v;

gives

Magma V2.15-14    Tue Nov 24 2009 10:36:58    [Seed = 4156006409]
   -------------------------------------

jordan form:
[1 0 0 0 0 0 0]
[0 1 1 0 0 0 0]
[0 0 1 0 0 0 0]
[0 0 0 1 1 0 0]
[0 0 0 0 1 0 0]
[0 0 0 0 0 1 1]
[0 0 0 0 0 0 1]
transformation
[0 0 0 0 1 1 0]
[0 0 0 0 0 0 1]
[1 1 1 1 1 1 1]
[0 0 0 0 0 1 0]
[1 1 1 0 1 1 0]
[1 0 1 0 0 0 0]
[1 1 0 1 1 1 0]

Total time: 0.180 seconds, Total memory usage: 7.27MB
```



---

Comment by jason created at 2009-11-23 23:36:37

Or more verbosely:


```
m:=Matrix(GF(2),7,7,StringToIntegerSequence("1 0 1 0 0 0 1 1 0 0 1 1 1 0 1 1 0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0 0 1 0 1 1 1 0 1 0 0 1 1 1 1 1 1 0"));
jor,trans:=JordanForm(m);

print "jordan form:";
jor;
print "transformation";
trans;
print "m*transformation";
trans*m;
print "transformation*jordan form";
jor*trans; 

gives

Magma V2.15-14    Tue Nov 24 2009 10:41:01    [Seed = 3482294566]
   -------------------------------------

jordan form:
[1 0 0 0 0 0 0]
[0 1 1 0 0 0 0]
[0 0 1 0 0 0 0]
[0 0 0 1 1 0 0]
[0 0 0 0 1 0 0]
[0 0 0 0 0 1 1]
[0 0 0 0 0 0 1]
transformation
[0 0 0 0 1 1 0]
[0 0 0 0 0 0 1]
[1 1 1 1 1 1 1]
[0 0 0 0 0 1 0]
[1 1 1 0 1 1 0]
[1 0 1 0 0 0 0]
[1 1 0 1 1 1 0]
m*transformation
[0 0 0 0 1 1 0]
[1 1 1 1 1 1 0]
[1 1 1 1 1 1 1]
[1 1 1 0 1 0 0]
[1 1 1 0 1 1 0]
[0 1 1 1 1 1 0]
[1 1 0 1 1 1 0]
transformation*jordan form
[0 0 0 0 1 1 0]
[1 1 1 1 1 1 0]
[1 1 1 1 1 1 1]
[1 1 1 0 1 0 0]
[1 1 1 0 1 1 0]
[0 1 1 1 1 1 0]
[1 1 0 1 1 1 0]

Total time: 0.170 seconds, Total memory usage: 7.27MB

```



---

Comment by spancratz created at 2010-01-19 12:28:03

Changing status from new to needs_review.


---

Attachment

The above patch fixes this problem, and also resolves ticket #6932.


---

Comment by spancratz created at 2010-01-20 02:17:27

Additional doctests


---

Attachment

The second patch adds additional doctests.  There are three of them, all for 10 by 10 matrices over the rationals and with only one eigenvalue.  The Jordan blocks are of sizes (a) 3,3,3,1, (b) 3,3,2,2, and (c) 3,2,2,2,1.

Sebastian


---

Comment by rbeezer created at 2010-01-24 08:06:34

This is looking pretty good.  But I'll have to spend some more time with it.  Until then, here's another 10x10 matrix with a nice Jordan form and nearly no fractions in the transformation matrix.


```
matrix(QQ, [
[-6,  9,  -7,  -5,  5,  12,  -22,  14,  8,  21 ],
[ -3,  5,  -3,  -1,  2,  7,  -12,  9,  1,  12 ],
[8,  -9,  8,  6,  0,  -14,  25,  -13,  -4,  -26 ],
[-7,  9,  -7,  -5,  0,  13,  -23,  13,  2,  24 ],
[0,  -1,  0,  -1,  -3,  -2,  3,  -4,  -2,  -3 ],
[3,  2,  1,  2,  9,  -1,  1,  5,  5,  -5 ],
[-1,  3,  -3,  -2,  4,  3,  -6,  4,  4,  3 ],
[3,  -4,  3,  2,  1,  -5,  9,  -5,  1,  -9 ],
[0,  2,  0,  0,  2,  2,  -4,  4,  2,  4 ],
[-4,  4,  -5,  -4,  -1,  6,  -11,  4,  1, 10]
])
```



---

Attachment

One-character reviewer doctest fix


---

Comment by rbeezer created at 2010-01-31 07:17:48

Hi Sebastian,

Very nice!

1.  One line in a list indented one-too-many characters.  Fix in reviewer patch for your convenience.  Accept or not.

2.  Most of the linear algebra matrix decompositions return all the pieces, all the time.  I've always thought it inconsistent Jordan form has this `transformation` switch, sometimes returning one matrix, other times two.  Now would be a good time to change this behavior.  But I see that the form is almost a combinatorial routine (once you have the spectrum), while the basis vectors require a whole lot more work, so maybe best not to compute it unless it is asked for?

3.  The list `Vsmall+Y` ends up in a `span()` in the "vector_in_difference" routine.  The span has an `already_echelonized` switch, so I spent a lot of time trying to decide how (or if it was possible) to somehow "keep" `Vsmall+Y` echelonized, since `Vsmall` will start that way.  Couldn't see a reasonable way to do anything too clever, though.

4.  Do you want the 10x10 matrix above for the doctests?  I'd be happy to package it up with the one-character patch.  ;-)

Other than the doctest fix, this is ready to go.  If you want to accept the doctest fix, then go ahead and mark this as "positive review" - everything else is just for your consideration.

Great to see all your good work since the summer, including this.

Rob


---

Comment by rbeezer created at 2010-01-31 07:17:48

Changing status from needs_review to needs_info.


---

Comment by rbeezer created at 2010-02-03 19:24:56

I've marked this as "needs review"  in hopes it will get merged soon.  The questions above could be addressed on a new ticket.


---

Comment by rbeezer created at 2010-02-03 19:24:56

Changing status from needs_info to needs_review.


---

Comment by mvngu created at 2010-02-03 22:17:03

The reviewer patch [trac_6942-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6942/trac_6942-reviewer.patch) looks good to me.


---

Comment by mvngu created at 2010-02-03 22:17:03

Changing status from needs_review to positive_review.


---

Comment by spancratz created at 2010-02-06 02:23:53

Dear Rob,

I am sorry that I am only looking at this again now.  Of course, the reviewer patch looks fine.  Thanks again for reviewing this!  About your other points...

3) Yes, that is a good observation.  I am almost sure that if one looked closer at the linear algebra operations then this code could easily be improved.  There are currently two reasons why I won't look at this, though.  (a) The previous code was broken, so I think it's important to first have something that "obviously" works, in the sense that it is moderately easy to review since the code only uses "high-level" operations.  (b) I've got my first year interview this coming Monday.

4) This is completely up to you.  The matrix looks quite intriguing and more examples certainly couldn't hurt.  Since this ticket will probably be closed soon, if you decide to include this new example, feel free to let me know (via email or sage-devel) and I'll review it right away.

Also, Minh, thank you for picking up the slack and completing the review process!

Kind regards,

Sebastian


---

Comment by jason created at 2010-02-06 03:10:08

Replying to [comment:11 spancratz]:

> 
> Also, Minh, thank you for picking up the slack and completing the review process!


Minh and Rob---thank you both of you for reviewing this!


---

Comment by mpatel created at 2010-02-11 14:33:05

Resolution: fixed
