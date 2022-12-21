# Issue 4757: eigenspaces_right over CDF gives total nonsense

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-11 05:17:47

Assignee: was

I don't care what anybody says, this is a BUG.  Either the command should immediately raise a NotImplementedError, or it should give meaningful output (e.g., not vector spaces of dimension 0!)


```
sage: a = random_matrix(CDF,2)
sage: a.eigenspaces_right()

[
(1.68954005899 + 0.570924387184*I, Vector space of degree 2 and dimension 0 over Complex Double Field
User basis matrix:
[]),
(-0.0345737707895 + 0.485480056628*I, Vector space of degree 2 and dimension 0 over Complex Double Field
User basis matrix:
[])
]
```


We easily and quickly have the eigenvectors and eigenvalues in this case, so I don't see what the problem is:

```
sage: a.eigenvectors_right()

([1.68954005899 + 0.570924387184*I, -0.0345737707895 + 0.485480056628*I],
 [                    0.800587795941                     0.758354735061]
[  0.545800288485 - 0.24730795798*I -0.194687766428 + 0.622089036565*I])
```


Same comments for eigenspaces_left.

Note that oddly a.eigenspaces() gives a sensible answer though neither left nor right does.

```
sage: a.eigenspaces_right()
[
(1.68954005899 + 0.570924387184*I, Vector space of degree 2 and dimension 0 over Complex Double Field
User basis matrix:
[]),
(-0.0345737707895 + 0.485480056628*I, Vector space of degree 2 and dimension 0 over Complex Double Field
User basis matrix:
[])
]
```



---

Comment by mhansen created at 2008-12-11 08:06:50

This has to do with the naming and aliases of methods in this and the parent class.

Note that the eigenspaces method is now inherited from the parent class, and does the right thing by giving a deprecation warning and calling the eigenspaces_left method.


---

Comment by mhansen created at 2008-12-11 08:06:50

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-12-11 08:06:50

Changing status from new to assigned.


---

Attachment


---

Comment by jason created at 2008-12-11 09:09:47

The patch code looks good, but I haven't tested it (I should be able to get to this by the weekend, though).

This was due to be looked at during the Christmas holiday as part of the overhaul of linear algebra interfaces (see http://wiki.sagemath.org/LinearAlgebraSEP; there it lists the methods as okay, but I'm aware that problems exist in the different eig* functions of different data types, so each of those implementations was going to be looked at.  For example, I believe the SR eig* functions don't conform to the correct interface right now either).

Thanks for catching and taking care of this.


---

Comment by AlexGhitza created at 2008-12-11 09:55:04

Also looks good to me, and I've played around with it for a little while.  However, should there be a new doctest along the lines of William's example?


---

Comment by jason created at 2008-12-12 21:04:21

apply on top of previous patches


---

Attachment

There already is a doctest which I think adequately covers the issue, but numerical error makes it so that it is marked #random.

Erring on the side of caution, my review patch probably ought to also be reviewed, as it changes code.


---

Comment by mabshoff created at 2008-12-13 01:14:58

Replying to [comment:4 jason]:
> There already is a doctest which I think adequately covers the issue, but numerical error makes it so that it is marked #random.

I am not sure that doctest should be random - if the result truly is #random, i.e. more than the last couple digits, there is something seriously wrong here.

> Erring on the side of caution, my review patch probably ought to also be reviewed, as it changes code.

Yep

Cheers,

Michael


---

Comment by jason created at 2008-12-13 03:08:23

It's not digits that is the problem, it's that the number is on the order of 1e-15, I believe.  However, we should be able to construct the printing of the data to deal with this.


---

Comment by ncalexan created at 2009-01-21 08:12:05

There is a test that the eigenvalues returned are of suitably small magnitude, so I'm not worried by the # random flag.  Positive review!2


---

Comment by mabshoff created at 2009-01-23 07:32:05

Merged in Sage 3.3.alpha1


---

Comment by mabshoff created at 2009-01-23 07:32:05

Resolution: fixed
