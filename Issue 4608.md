# Issue 4608: roots method broken for root system lattices

Issue created by migration from Trac.

Original creator: saliola

Original creation time: 2008-11-25 00:33:55

Assignee: mhansen

CC:  sage-combinat

This works:

```
sage: R = RootSystem(['A',2])
sage: R.ambient_lattice()
Ambient lattice of the Root system of type ['A', 2]
sage: R.ambient_lattice().roots()
[(1, -1, 0), (1, 0, -1), (0, 1, -1), (-1, 1, 0), (-1, 0, 1), (0, -1, 1)]
sage: 
```

But this method does not work for any of the other associated lattices.

```
sage: R = RootSystem(['A',2])
sage: R.coroot_lattice().roots()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
...
AttributeError: 'RootSpace' object has no attribute 'positive_roots'
sage: R.coweight_lattice().roots()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
...
AttributeError: 'WeightSpace' object has no attribute 'positive_roots'
sage: R.root_lattice().roots()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
...
AttributeError: 'RootSpace' object has no attribute 'positive_roots'
sage: R.weight_lattice().roots()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
...
AttributeError: 'WeightSpace' object has no attribute 'positive_roots'
```





---

Comment by hivert created at 2010-04-16 10:31:45

This ticket should be closed. The issues is now fixed:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: combinat
sage: R = RootSystem(['A',2])
sage: R.coroot_lattice().roots()
[alphacheck[1], alphacheck[2], alphacheck[1] + alphacheck[2], -alphacheck[1], -alphacheck[2], -alphacheck[1] - alphacheck[2]]
sage: R.coweight_lattice().roots()
[-Lambdacheck[1] + 2*Lambdacheck[2], Lambdacheck[1] + Lambdacheck[2], 2*Lambdacheck[1] - Lambdacheck[2], Lambdacheck[1] - 2*Lambdacheck[2], -Lambdacheck[1] - Lambdacheck[2], -2*Lambdacheck[1] + Lambdacheck[2]]
sage: R.root_lattice().roots()
[alpha[2], alpha[1], alpha[1] + alpha[2], -alpha[2], -alpha[1], -alpha[1] - alpha[2]]
sage: R.weight_lattice().roots()
[-Lambda[1] + 2*Lambda[2], Lambda[1] + Lambda[2], 2*Lambda[1] - Lambda[2], Lambda[1] - 2*Lambda[2], -Lambda[1] - Lambda[2], -2*Lambda[1] + Lambda[2]]
```

| Sage Version 4.3.4, Release Date: 2010-03-19                       |
| Type notebook() for the GUI, and license() for information.        |
Florent


---

Comment by hivert created at 2010-04-16 10:31:45

Changing assignee from mhansen to hivert.


---

Comment by mvngu created at 2010-04-30 16:11:42

It works now:

```sh
[mvngu`@`sage graphs]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R = RootSystem(['A',2])
sage: R.ambient_lattice()
Ambient lattice of the Root system of type ['A', 2]
sage: R.ambient_lattice().roots()
[(1, -1, 0), (1, 0, -1), (0, 1, -1), (-1, 1, 0), (-1, 0, 1), (0, -1, 1)]
sage: R = RootSystem(['A',2])
sage: R.coroot_lattice().roots()
[alphacheck[1], alphacheck[2], alphacheck[1] + alphacheck[2], -alphacheck[1], -alphacheck[2], -alphacheck[1] - alphacheck[2]]
sage: R.coweight_lattice().roots()
[-Lambdacheck[1] + 2*Lambdacheck[2], Lambdacheck[1] + Lambdacheck[2], 2*Lambdacheck[1] - Lambdacheck[2], Lambdacheck[1] - 2*Lambdacheck[2], -Lambdacheck[1] - Lambdacheck[2], -2*Lambdacheck[1] + Lambdacheck[2]]
sage: R.root_lattice().roots()
[alpha[2], alpha[1], alpha[1] + alpha[2], -alpha[2], -alpha[1], -alpha[1] - alpha[2]]
sage: 
sage: R.weight_lattice().roots()
[-Lambda[1] + 2*Lambda[2], Lambda[1] + Lambda[2], 2*Lambda[1] - Lambda[2], Lambda[1] - 2*Lambda[2], -Lambda[1] - Lambda[2], -2*Lambda[1] + Lambda[2]]
```



---

Comment by mvngu created at 2010-04-30 16:25:35

Resolution: fixed


---

Comment by mvngu created at 2010-04-30 16:25:35

Close as fixed by #4326:

```
09:22 < hivert> mvngu: this was fixed by #4326: Root systems: refactoring and 
                improvements
09:23 < hivert> And some similar doctests are performed. So I don't think more 
                work is need on this one. 
09:24 < hivert> I should have guessed ! #4326 is a huge patch with no less than 
                6 authors :-)
09:24 < hivert> Please close the ticket.
```

