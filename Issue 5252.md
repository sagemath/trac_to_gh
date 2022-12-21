# Issue 5252: elliptic curves: P.height() lies about its precision

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-02-13 04:05:11

Assignee: was

This is a bit weird because it seems to only happen with some elliptic curves.

Anyway, here's the example:

```
sage: E = EllipticCurve([1, -1, 1, -2063758701246626370773726978, 32838647793306133075103747085833809114881])
sage: P = E([-30987785091199, 258909576181697016447])
sage: P.height()               # default precision: 53 bits
sage: P.height(precision=100)  # new precision: 100 bits
25.860317067546190744967149477
sage: P.height(precision=250)  # new precision: 250 bits
25.860317067546190744967149477417933667311444878578186035156250000000000000
```


I don't believe for a second that all the zeroes in the last example are correct.  In fact, if you increase the precision to 1000 bits you only get more zeroes.

There must be "simpler" elliptic curves for which this happens, and I'll try to find some.



---

Comment by AlexGhitza created at 2009-02-13 05:45:04

Running this example in a native GP session works fine, so the problem is either in Sage or in the way Sage communicates with the Pari library.


---

Attachment

Alex, I think that the ellheight() function needs to be given the precision parameter, despite what it says in the docstring for that function:

```
sage: E = EllipticCurve([1, -1, 1, -2063758701246626370773726978, 32838647793306133075103747085833809114881])
sage: P = E([-30987785091199, 258909576181697016447])
sage: PE = E.pari_curve(prec=500)
sage: PE.ellheight([P[0],P[1],P[2]]).python()
25.8603170675461907
sage: PE.ellheight([P[0],P[1],P[2]],precision=500).python()
25.8603170675461907438688407407351103230988729038444162155771710417835725129551130570889813281792157278507639909972112856019190236125362914195452321719909
```

(Here I output the .python() conversion since otherwise it uses the gp default precision for output so you cannot see what is going on).

After my patch, your example works fine:

```
sage: E = EllipticCurve([1, -1, 1, -2063758701246626370773726978, 32838647793306133075103747085833809114881])
sage: P = E([-30987785091199, 258909576181697016447])
sage: P.height()
25.8603170675462
sage: P.height(precision=100)
25.860317067546190743868840741
sage: P.height(precision=250)
25.860317067546190743868840740735110323098872903844416215577171041783572513
sage: P.height(precision=500)
25.8603170675461907438688407407351103230988729038444162155771710417835725129551130570889813281792157278507639909972112856019190236125362914195452321720
```


The patch (based on 3.3.rc0) corrects height(), adds a doctest, and corrects the docstring in gen.pyx.  I also had to correct a doctest output in ell_rational_field.py.

NB The output at precision 500 for the new doctest looks odd on trac but is ok in the source file.


---

Comment by AlexGhitza created at 2009-02-16 08:06:21

Excellent work, John!


---

Comment by mabshoff created at 2009-02-16 08:30:40

Resolution: fixed


---

Comment by mabshoff created at 2009-02-16 08:30:40

Merged in Sage 3.3.rc1.

Cheers,

Michael
