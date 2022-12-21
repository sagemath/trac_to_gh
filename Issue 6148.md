# Issue 6148: functions involving ceil and floor are plotted incorrectly

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2009-05-28 12:27:21

In sage-4.0.rc1 if I define:



```
sage: r(u) = floor(u) - 2*floor(u/2)
sage: s(u) = ceil(u) - 2*ceil(u/2)
```


The following gives an incorrect plot:


```
sage: plot(r, (0, 10))
```


but


```
sage: plot([r], (0, 10))
```


gives the correct plot.

For ceil it is even worse


```
sage: plot([s], (0, 10))
```


gives the correct plot, but


```
sage: plot(s, (0, 10))
```


gives a runtime error:


```
RuntimeError: maximum recursion depth exceeded
```


All of this works correctly in sage-3.4.2, so it is probably
related to the new symbolics.

Additionally


```
sage: r(0)
-2*floor(0)
```


but

```
sage: s(0)
0
```


as expected.


```



---

Comment by mhansen created at 2009-05-28 18:27:03

Changing status from new to assigned.


---

Comment by mhansen created at 2009-05-28 18:27:03

Set assignee to mhansen.


---

Attachment


---

Comment by jason created at 2009-05-29 04:25:12

This patch fixes the stated problems; both graphs are the same for me now.


---

Comment by was created at 2009-05-29 13:37:48

I also read the patch and tried things and it looks fine to me.


---

Comment by mhansen created at 2009-05-29 17:31:35

Resolution: fixed


---

Comment by mhansen created at 2009-05-29 17:31:35

Merged in 4.0.rc2.
