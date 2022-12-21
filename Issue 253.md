# Issue 253: Add Integral closure for ideals

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-09 18:39:43

Assignee: somebody


```
On Fri, 09 Feb 2007 11:04:16 -0700, Milena Hering wrote:

> Hi William,
>
> Is it possible to compute the integral closure of an ideal in sage?

It's not nicely integrated into SAGE yet, but the capability is there
via Singular, which is included in SAGE.  For example:

sage: singular.load('reesclos.lib')
sage: R.<x,y> = QQ[]
sage: i = ideal([x^2,x*y^4,y^5])
sage: singular(i).normalI()         # the [1] part gives the normalization
[1]:
   _[1]=x^2
   _[2]=y^5
   _[3]=x*y^3

---

Very likely somebody will add this functionality to the next version of SAGE,
i.e., so you could type i.integral_closure(), and get back the ideal as a SAGE ideal.


William
```



---

Comment by was created at 2007-02-09 18:40:11

See http://www.singular.uni-kl.de/Manual/3-0-1/sing_788.htm


---

Comment by malb created at 2007-02-09 20:56:16

Resolution: fixed


---

Comment by malb created at 2007-02-09 20:56:16

Done in r2854.
