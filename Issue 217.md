# Issue 217: optimize matrix permanents

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-25 18:58:54

Assignee: was




---

Comment by mabshoff created at 2007-10-27 05:19:23

There was some work done for QQ and Jaap seems to be working on this for ZZ, so what is the status of this?

Cheers,

Michael


---

Comment by jsp created at 2007-10-27 11:43:39

There was track #931 and there is more optimization in the pipeline.

This will not only work for ZZ, but for all base rings.

I will send a patch (relative to sage-2.8.9) shortly.

Jaap


---

Comment by jsp created at 2007-10-27 11:55:53

With patches:


```
sage: time dance(7)
h^7 - 14*h^6 + 126*h^5 - 700*h^4 + 2625*h^3 - 6342*h^2 + 9072*h - 5840
CPU times: user 18.85 s, sys: 0.18 s, total: 19.04 s
Wall time: 19.48

```


in sage-2.8.9:


```
sage: time dance(7)
h^7 - 14*h^6 + 126*h^5 - 700*h^4 + 2625*h^3 - 6342*h^2 + 9072*h - 5840
CPU times: user 47.02 s, sys: 1.12 s, total: 48.14 s
Wall time: 48.96

```



---

Comment by jsp created at 2007-10-27 12:42:46

optimization relative to #931


---

Attachment


---

Comment by cwitty created at 2007-10-27 19:13:04

Resolution: fixed


---

Comment by was created at 2007-10-29 01:19:23


```
> As I wrote, I see a lot of cdef Py_ssize_t in for example matrix2.pyx
> that should be cdef int.


> I did change some of them in trac #217, but I think a new trac
> ticket should be created.


Are you sure?    I just had a look at trac #217, and your changing Py_ssize_t
into int specifically *introduces* bugs into that code.  E.g., suppose the input
were a 1 x 2^33 matrix.  Then you did this in your patch:

-        cdef Py_ssize_t m, n, r
+        cdef int m, n, r

Lower down one has:
        m = self._nrows
	n = self._ncols

Now, instead if the code working like it used to, there will be an overflow,
and one will get total nonsense.

William
```



---

Comment by was created at 2007-10-29 01:19:23

Changing status from closed to reopened.


---

Comment by was created at 2007-10-29 01:19:23

Resolution changed from fixed to 


---

Comment by was created at 2007-10-29 01:45:58

This patch is likely fine if the int's are changed back to Py_ssize_t.


---

Comment by was created at 2007-10-29 14:30:21


```
On 10/29/07, Jaap Spies <j.spies`@`hccnet.nl> wrote:
> > Now, instead if the code working like it used to, there will be an overflow,
> > and one will get total nonsense.
> >
> 
> In your example the permanent is just the product of the entries.
> 
> You deserve to get total nonsense when you try to calculate the permanent
> of matrices of that size! In practice you know that m and n are small ints.
> 
> The permanent is a really hard problem. For example the calculation of a 40 x 40
> (0,1)-matrix with the implemented Ryser algorithm will take forever. Let alone
> a general matrix of that size! This best known Ryser algorithm is of time O(n^2*2^n).
> The best we can hope is doing better for certain types of (0,1) matrices.

I am of course well aware of the fact that it would be impractical to compute permanents of large matrices.  But still, writing code that
overflows and gives nonsense on "impractical input" is bad coding
style.  Especially because such code my give nonsense quite quickly.
This is almost exactly the same situation in spirit as the situation
that leads to people writing insecure code that leads to buffer overflows,
because they don't bother doing proper error checking, since "nobody
would give input like that...". 
```



---

Comment by jsp created at 2007-10-29 20:01:27

Canged back


---

Attachment

Lesson learned! I hope.

Jaap


---

Comment by mabshoff created at 2007-11-01 09:31:30

Resolution: fixed


---

Comment by mabshoff created at 2007-11-01 09:31:30

applied to 2.8.11.alpha0
