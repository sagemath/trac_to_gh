# Issue 9936: PARI real precision is broken in many ways

Issue created by migration from https://trac.sagemath.org/ticket/9937

Original creator: jdemeyer

Original creation time: 2010-09-17 20:48:18

Assignee: was

Keywords: pari gp real precision

The following do not work as they should (try these examples with a freshly started copy of Sage, such that everything is default). 


```
# Default: 2 significant words (while we really should get only 1)
sage: pari('Pi').debug()
[&=0000000004fc9620] REAL(lg=4):0400000000000004 (+,expo=1):6000000000000001 c90fdaa22168c234 c4c6628b80dc1cd1

# Change precision and then change it back: we get 1 word
sage: n = pari.get_real_precision(); pari.set_real_precision(100); pari.set_real_precision(n);
sage: pari('Pi').debug()
[&=00000000012bf200] REAL(lg=3):0400000000000003 (+,expo=1):6000000000000001 c90fdaa22168c235
```



```
# We cannot compute constants with high precision:
sage: pari.set_real_precision(1000);
sage: pari.euler().debug()
[&=0000000004f75e20] REAL(lg=3):0400000000000003 (+,expo=-1):5fffffffffffffff 93c467e37db0c7a5
```


Dependencies: #9898, #9893


---

Comment by jdemeyer created at 2010-09-17 21:05:10

Changing keywords from "pari gp real precision" to "pari gp real precision set_real_precision".


---

Comment by cremona created at 2010-09-21 20:27:05

There's a lot of relevant information written by Alex Ghitza and me a couple of years ago in the file gen.pyx.  Yes, it is counterintuitive;  but not undocumented.


---

Comment by jdemeyer created at 2010-09-21 20:43:05

Replying to [comment:3 cremona]:
> There's a lot of relevant information written by Alex Ghitza and me a couple of years ago in the file gen.pyx.  Yes, it is counterintuitive;  but not undocumented.

I know it is documented (although not too clearly), but the question is: does it make sense?  (In my opinion: no).


---

Comment by jdemeyer created at 2010-09-21 20:47:09

More precisely: this is counter-intuitive:

```
sage: pari.set_real_precision(100);
sage: pari('Euler')   # Precision changes
0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495
sage: pari.euler()    # Precision does NOT change
0.5772156649015328607
```



---

Comment by jdemeyer created at 2011-04-14 20:03:29

Changing status from new to needs_work.


---

Attachment


---

Comment by jdemeyer created at 2017-02-21 07:56:21

Resolution: invalid
