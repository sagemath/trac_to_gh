# Issue 8197: Documenting check=True/False parameters

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2010-02-05 20:20:21

Assignee: AlexGhitza

Many functions have a check=True (or check=False) parameter where the caller can avoid come costly checking of the input if they know exactly what they are doing.  That is a Good Thing, but unfortunately it is not always documented well.

For example,

```
age: P2 = ProjectiveSpace(GF(2),2)
sage: P = P2.point((0,0,1))
sage: Q = P2.point([0,0,1])
sage: P
(0 : 0 : 1)
sage: Q
(0 : 0 : 1)
sage: P==Q
True
sage: P._coords
[0, 0, 1]
sage: Q._coords
[0, 0, 1]
```


Now the same but with "check=False":


```
sage: P = P2.point((0,0,1),check=False)
sage: Q = P2.point([0,0,1],check=False)
sage: P
(0 : 0 : 1)
sage: Q
(0 : 0 : 1)
sage: P==Q
False
sage: P._coords
(0, 0, 1)
sage: Q._coords
[0, 0, 1]
```

The point is that on creation of the point, valid tuple input is
converted to a list, unless check=False in which case tuples are left as tuples.  This can result in wrong results.

In this example, the point-creation function should document the check= parameter by stating that the coordinates should be given as a list, not a tuple, with entries in the right parent, of the roght length, and (for curves or other schemes where there are polynomial equations to be satisfied) satisfying the defining equations.

There are surely many places in the source code where these remarks apply, but I have tagged this ticket "algebraic geometry" since that's where I ran into it.


---

Comment by nbruin created at 2010-02-05 21:13:28

In fact, naively, I would have expected that if
`F(arg)`
returns successfully then
`F(arg, check=False)`
will as well. To me this looks like `check=False` does more than turn off checks on whether input is valid -- it changes what valid input is!


---

Comment by fwclarke created at 2010-02-06 10:08:20

Replying to [ticket:8197 cremona]:

> The point is that on creation of the point, valid tuple input is converted to a list, unless check=False in which case tuples are left as tuples.

John, it's not quite accurate what you say:


```
sage: P2 = ProjectiveSpace(GF(2),2)
sage: type(P2.point([0,0,1])._coords)
<class 'sage.structure.sequence.Sequence'>
sage: type(P2.point([0,0,1], check=False)._coords)
<type 'list'>
```

even though


```
sage: P2.point([0,0,1], check=False) == P2.point([0,0,1])
True
```

The relevant code is for the class  `SchemeMorphism_projective_coordinates_field` in  `schemes/generic/morphism.py :` with `check=False,` absolutely nothing is  done except for setting the attribute `_coords`.  Thus


```
sage: P = P2.point("Anything", check=False)
sage: P._coords
'Anything'
sage: P
('A' : 'n' : 'y' : 't' : 'h' : 'i' : 'n' : 'g')
```

So, strictly speaking, the coordinates have to be given as a `Sequence` of the right length.

I think you're right that the key thing is documentation.  In each case there's a design balance to be drawn (when `check=False`) between on the one hand checking nothing at all and on the other making some basic conversions, while not doing time-consuming things such as, for example, verifying that an input satisfies a polynomial.  How this balance is drawn will vary, but the INPUT block ought make it clear how the requirements depend on the value of `check`.

The relevant part of the documentation for `SchemeMorphism_projective_coordinates_field` says


```
     -  ``v`` - a list or tuple of coordinates in K
```

The code shows that this is actually too restrictive when `check` is True, and it is inaccurate when check is False.


---

Comment by cremona created at 2010-02-06 11:45:18

You are quite right -- the code run when check=True converts the input into a sequence.

This does not effect this ticket;  but it means that the patch I put up at #8193 needs adjusting slightly.  (There, I construct a whole lot of points on a curve knowing that they coordinates I pass to the point constructor satisfy the equations, and wanted to save time by not asking for the equations to be checked.  But I now see that setting check=False has so many other negative side-effects that I think I'll put back check=True.  The main point of the patch at that ticket is far more significant than this tiny saving anyway!)
