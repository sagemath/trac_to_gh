# Issue 765: Ctrl-C unresponsive in rational_points

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-09-30 20:25:27

Assignee: was

The following isn't implemented in a useful way anyway, but the fact that crtl-C does not work properly is a bad sign:

```
P.<x>=QQ[]
f=x^6+x^2+1
C=HyperellipticCurve(f)
J=C.jacobian()
K=J.kummer_surface()
K.rational_points(bound=100)
```



---

Comment by was created at 2007-11-03 15:27:30

Weird.


---

Comment by was created at 2007-11-03 18:11:08

Control-c works fine now (tested on linux and osx).  Maybe this was fixed by the other control-c related fixes that Gonzalo Tornaria and I made at SD5.


---

Comment by was created at 2007-11-03 18:11:08

Resolution: fixed


---

Comment by cremona created at 2013-07-11 10:28:38

I found this ancient ticket while looking for anything mentioning kummer_surface.  With Sage 5.10 it does not work at all:

```
sage: P.<x>=QQ[]
sage: f=x^6+x^2+1                                                                                
sage: C=HyperellipticCurve(f)                                                                    
sage: J=C.jacobian()                                                                             
sage: K=J.kummer_surface()
...
/home/jec/sage-5.10/local/lib/python2.7/site-packages/sage/schemes/projective/projective_morphism.pyc in __init__(self, parent, polys, check)
    139                 d = polys[0].degree()
    140             except AttributeError:
--> 141                 polys = [f.lift() for f in polys]
    142             if not all([f.is_homogeneous() for f in polys]):
    143                 raise  ValueError("polys (=%s) must be homogeneous"%polys)

AttributeError: 'int' object has no attribute 'lift'
```

