# Issue 7085: fix this laurent series coercion bug

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-30 23:10:18

Assignee: somebody

CC:  mhampton


```
> Ok, I am completely baffled by the following situation:
>
> sage: A.<z>=LaurentSeriesRing(QQ)
> sage: B.<w>=LaurentSeriesRing(A)
> sage: z/w
>  1
> Maybe you will agree this is a bug?

That's definitely a coercion bug.   You can workaround it like this:


sage: sage: A.<z>=LaurentSeriesRing(QQ)
sage: sage: B.<w>=LaurentSeriesRing(A)
sage: z/w
1
sage: (1/w) * z
z*w^-1
```



---

Comment by mhampton created at 2011-01-11 01:56:31

Before any division takes place, z is getting incorrectly coerced to w.  I think this is because in laurent_series_ring_element.pyx, in the LaurentSeries class __init__ method the represention (variable)^n*f is shifted by the code:

```
        else:
            val = f.valuation()
            if val == 0:
                self.__n = n    # power of the variable
                self.__u = f    # unit part
            else:
                self.__n = n + val
                self.__u = f >> val
```


and I think that shifting is missing that different variables are involved.


---

Comment by mhampton created at 2011-01-11 02:14:14

Now I'm not sure the above code is the critical place, but this shows that its a coercion rather than a division issue:

```
sage: A.<z>=LaurentSeriesRing(QQ)
sage: B.<w>=LaurentSeriesRing(A)
sage: B(z)
w
```



---

Attachment

Solves problem, but in a very hackish way.


---

Comment by mhampton created at 2011-01-11 06:09:10

Changing status from new to needs_review.


---

Comment by mhampton created at 2011-01-11 06:09:10

The attach patch solves the problem, but not in a very robust way.  I suspect that Simon King's efforts at #8972 are related and might fix the problem in a more fundamental way.  I also hope that my patch rekindles interest in this module and that someone with a deeper understanding of the code can provide a better solution.

On the positive side, I think this doesn't break anything and solves the immediate problem.  Perhaps when #8972 is ready my workaround can be deleted.


---

Comment by wjp created at 2011-01-11 19:03:19

I suspect the prolem is that `laurent_series_ring_element.LaurentSeries.__init__` doesn't realize that the base ring may be a LaurentSeriesRing itself. (But I haven't thought about it too much yet.)


---

Comment by wjp created at 2011-01-11 19:12:28

Changing status from needs_review to needs_work.


---

Comment by wjp created at 2011-01-11 19:12:28

This seems to fix it, but I haven't looked at the code closely enough to be sure it's correct:

http://www.math.leidenuniv.nl/~wpalenst/sage/7085_attempt.patch


---

Comment by wjp created at 2011-01-11 19:39:39

...but it unfortunately also breaks coercions between different `LaurentSeriesRings`.


---

Comment by chapoton created at 2014-03-04 12:30:22

Changing keywords from "" to "laurent series".


---

Comment by pbruin created at 2014-05-04 22:40:30

The attached branch fixes the bug by converting `LaurentSeriesRing` to the new coercion framework.  In the situation where _A_ -> _B_ are two rings with a coercion map between them, this allows us to define a coercion map from _A_ to _B_((_u_)) as the composition of the obvious maps _A_ -> _B_ -> _B_((_u_)).  The `_element_constructor_(x)` for _B_((_u_)) then only has to consider one new special case, namely where _x_ is in _B_.  It turns out that the easiest way to treat this case is to convert _x_ into a (constant) power series, which has to be done anyway due to the internal representation of Laurent series.


---

Comment by pbruin created at 2014-05-04 22:40:30

Changing component from basic arithmetic to coercion.


---

Comment by pbruin created at 2014-05-04 22:40:30

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2014-05-05 20:48:55

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2014-05-05 20:48:55

Very trivial change of removing a double colon `::`. LGTM otherwise.
----
New commits:


---

Comment by vbraun created at 2014-05-06 22:02:51

Resolution: fixed
