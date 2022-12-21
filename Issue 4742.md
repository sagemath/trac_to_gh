# Issue 4742: Wrap Pari's generalised Smith form (when it is fixed)

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2008-12-08 17:15:50

Assignee: somebody

CC:  jdemeyer

Keywords: elementary divisors

Pari has a function ("nfsnf" in GP, "nfsmith" in the C library) that calculates the generalised elementary divisors (a list of ideals rather than elements) for a matrix over the ring of integers of a number field. In the current pari stable (2.3.4) and testing (2.4.2) this is so broken as to be useless, but Karim Belabas has fixed it in svn, so when we catch up with Pari 2.4.3 it would be worth providing a Sage wrapper.


---

Comment by davidloeffler created at 2009-07-21 08:22:03

Changing component from number theory to number fields.


---

Comment by jdemeyer created at 2010-08-01 21:52:40

Maybe one should look into this again after #9343 has been merged?


---

Comment by sbrandhorst created at 2019-04-01 22:19:31

is it fixed?


---

Comment by jdemeyer created at 2019-04-02 08:34:47

I guess so....


---

Comment by alexjbest created at 2019-11-03 19:37:25

I don't see how this is fixed?

It doesn't look to me that `nfsnf` or `nfsmith` is used anywhere in the sage library, and calling elementary_divisors on a matrix over a non-PID can fail, the following example is from the smith_form docstring


```
        Some examples over non-PID's work anyway::

            sage: R.<s> = EquationOrder(x^2 + 5) # class number 2
            sage: A = matrix(R, 2, 2, [s-1,-s,-s,2*s+1])
            sage: D, U, V = A.smith_form()
            sage: D, U, V
            (
            [     1      0]  [    4 s + 4]  [       1 -5*s + 6]
            [     0 -s - 6], [    s s - 1], [       0        1]
            )
            sage: D == U*A*V
            True

        Others don't, but they fail quite constructively::

            sage: matrix(R,2,2,[s-1,-s-2,-2*s,-s-2]).smith_form()
            Traceback (most recent call last):
            ...
            ArithmeticError: Ideal Fractional ideal (2, s + 1) not principal
```


I assume the point of this ticket is that


```
matrix(R,2,2,[s-1,-s-2,-2*s,-s-2]).elementary_divisors() # or .generalized_elementary_divisors()
```


should return the output of PARI nfsnf called on the base field and the appropriate` Z_K` module?

Currently it tries to use Sage's generic algorithm which will only work if it runs on inputs where the ideals


---

Comment by sbrandhorst created at 2019-11-04 13:38:44

I was wondering, whether or not it is fixed in pari.


---

Comment by alexjbest created at 2019-11-07 23:39:00

Oh I see, thank you. Sorry for the noise!

By way of an apology, I did some digging, the last time nfsnf was changed in pari was 2015 to fix a GC bug, and in 2008-12-06 `123- completely wrong results in nfsnf` was merged (also in 2014 `67- possibly wrong result in nfsnf`).

So I'd say definitely yes it was fixed, probably the Dec 08 commit.

Looking at the original message of Davids to the Pari list https://pari.math.u-bordeaux.fr/archives/pari-users-0812/msg00004.html and Karim's simplified version of his example I can run his example under `sage -gp`


```
+? E = nfinit(x^2 - x + 2);
+? M = [1, 0, x; 0, x, 0; 0,0,2+x];
+?   MM = matalgtobasis(E, M);
+? N = [[1, 0; 0, 1], [1, 0; 0, 1], [1, 0; 0, 1]];
+? nfsnf(E, [MM, N, N])
%7 = [[8, 2; 0, 1], [2, 0; 0, 1], [1, 0; 0, 1]]
```



```
  E = nfinit(x^2 - x + 2);
  M = [1, 0, x; 0, x, 0; 0,0,2+x];
  N = [1, 1, 1];
  nfsnf(E, [M, N, N])
 %16 = [[8, 2; 0, 1], [2, 0; 0, 1], [1, 0; 0, 1]]
```



tl; dr: yes!
