# Issue 9635: symbolic sum gives wrong answer

Issue created by migration from Trac.

Original creator: Henryk.Trappmann

Original creation time: 2010-07-29 07:34:28

Assignee: AlexGhitza


```
sage: (n,k,j)=var('n,k,j')
sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
0
sage: (n,j)=(5,3)
sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j) for k in range(j
+1,n+1))
1 
```

The above sum should be 1 for n>=j and 0 otherwise.

From kcrisman:
This appears to be a bug in Maxima. 

```
(%i1) load(simplify_sum);
<snip>
(%i3) simplify_sum(sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j
+1,n));

(%o3)                                  0
(%i4) simplify_sum(sum(binomial(5,k)*binomial(k-1,3)*(-1)**(k-1-3),k,
4,5));
(%o4)                                  1
(%i5) 5*1*1+1*4*(-1);
(%o5)                                  1 
```



---

Comment by kcrisman created at 2010-07-29 13:12:31

Changing assignee from AlexGhitza to burcin.


---

Comment by kcrisman created at 2010-07-29 13:12:31

Changing component from basic arithmetic to calculus.


---

Comment by kcrisman created at 2010-07-29 13:12:31

This is now Maxima bug 3036579.


---

Comment by kcrisman created at 2011-03-14 20:40:32

Maxima 5.23.2 still has this, and no movement on the original bug report.


---

Comment by kcrisman created at 2012-07-07 03:18:26

The [bug report](http://sourceforge.net/tracker/?func=detail&aid=3036579&group_id=4933&atid=104933) got updated over a year ago.

In the current Sage:

```
(%i1) load(simplify_sum); 
(%o1) /Users/karl-dietercrisman/Downloads/sage-5.0/local/share/maxima/5.26.0/s\
hare/contrib/solve_rec/simplify_sum.mac
(%i2) simplify_sum(sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j +1,n)); 

Is  j + 1  positive, negative, or zero?

pos;
(%o2)                                  1
```

So just need a doctest.

```
sage: (n,k,j)=var('n,k,j')
sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
-sum((-1)^(-j + k)*binomial(k - 1, j)*binomial(n, k), k, j + 1, n)
sage: assume(j>-1)
sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
1
sage: forget()
sage: assume(n>=j)
sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
-sum((-1)^(-j + k)*binomial(k - 1, j)*binomial(n, k), k, j + 1, n)
sage: forget()
sage: assume(j==-1)
sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
1
sage: forget()
sage: assume(j<-1)
sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
-sum((-1)^(-j + k)*binomial(k - 1, j)*binomial(n, k), k, j + 1, n)
```

Was the original report here wrong?  Maxima currently says that the sign of `j+1` is all that matters, which sort of makes sense


---

Comment by rws created at 2015-02-01 10:22:42

Now it's no longer solved at all, i.e., the sum is returned. Since there is no longer an erroneous result the ticket can be closed I think.


---

Comment by rws created at 2015-02-01 10:22:42

Changing status from new to needs_review.


---

Comment by kcrisman created at 2015-02-02 01:00:18

Changing status from needs_review to needs_info.


---

Comment by kcrisman created at 2015-02-02 01:00:18

All closures like this should be doctested - in case the bad behavior returns.


---

Comment by rws created at 2015-02-02 08:46:43

Changing status from needs_info to needs_review.


---

Comment by rws created at 2015-02-02 08:46:43

New commits:


---

Comment by kcrisman created at 2015-02-03 02:35:03

Actually, in this case the doctest I pasted above is absolutely correct.  One still has to _assume_ the right thing for it to return anything other than the original sum!  Your part is fine, you can just review the additional ones (unless you think they are too much).
----
New commits:


---

Comment by rws created at 2015-02-03 08:45:00

Somehow I still expect results like `a (for x<0); b (for x==0); c (else)` but I digress...


---

Comment by rws created at 2015-02-03 08:49:18

Changing status from needs_review to positive_review.


---

Comment by rws created at 2015-02-03 08:49:18

Tests OK, is fine.


---

Comment by kcrisman created at 2015-02-03 13:52:22

> Somehow I still expect results like a (for x<0); b (for x==0); c (else) but I digress...

That isn't possible with the current Maxima setup (at least not in a useful way, given the crazy number of branches Maxima gives us) but perhaps via sympy?  That would be a very, very good improvement.


---

Comment by vbraun created at 2015-02-08 15:26:26

Resolution: fixed
