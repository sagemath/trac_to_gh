# Issue 8158: efficiency problem with polynomials (SymbolicRing vs PolynomialRing)

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-02-02 22:18:45

Assignee: malb

Consider the following example:

```
sage: var('a,b,c')
(a, b, c)
sage: time d=expand((a+b+c+1)^100)
CPU times: user 2.45 s, sys: 0.07 s, total: 2.52 s
Wall time: 2.53 s
```

I thought it would be more efficient to use PolynomialRing(),
but it is not:

```
sage: P.<a,b,c> = PolynomialRing(QQ)
sage: time d=(a+b+c+1)^100
CPU times: user 10.28 s, sys: 0.07 s, total: 10.35 s
Wall time: 12.59 s
```

However if one wants to factor d, then PolynomialRing is faster
(SymbolicRing seems to loop forever):

```
sage: time e = d.factor()
CPU times: user 28.87 s, sys: 0.36 s, total: 29.23 s
Wall time: 34.20 s
```



---

Comment by zimmerma created at 2013-08-23 14:48:17

PolynomialRing is still slower with Sage 5.11, even with integer coefficients:

```
+--------------------------------------------------------------------+
+--------------------------------------------------------------------+
sage: var('a,b,c')
(a, b, c)
sage: %time d=expand((a+b+c+1)^100)
CPU times: user 16.35 s, sys: 0.26 s, total: 16.61 s
Wall time: 18.59 s
sage: P.<a,b,c> = PolynomialRing(QQ)
sage: %time d=(a+b+c+1)^100
CPU times: user 34.35 s, sys: 0.08 s, total: 34.42 s
Wall time: 35.80 s
sage: P.<a,b,c> = PolynomialRing(ZZ)
sage: %time d=(a+b+c+1)^100         
CPU times: user 32.29 s, sys: 0.07 s, total: 32.36 s
Wall time: 34.89 s
```

Paul


---

Comment by mmezzarobba created at 2014-03-15 17:05:18

I doubt there is much to do here except reduce the overhead of the singular interface (especially regarding memory management) or singular itself. On my system, ginac (1.6.2)  is already faster than singular (3.1.6):
  {{{
   > time(expand((a+b+c+1)^100));
  1.184s
  }}}
  {{{
  > timer=1;
  > ring r=0,(a,b,c),lp;
  > poly p=(a+b+c+1)^100;
  //used time: 1.95 sec
  }}}
Both interfaces have comparable overhead (sage 6.2.beta4):

```
sage: %time _=expand((a+b+c+1)^100)
CPU times: user 3.13 s, sys: 16 ms, total: 3.14 s
Wall time: 3.14 s
```


```
sage: P.<a,b,c> = PolynomialRing(QQ,order='lex')
sage: %time _=(a+b+c+1)^100
CPU times: user 5.59 s, sys: 8 ms, total: 5.6 s
Wall time: 5.59 s
```

but not for the same reason—the advantage of standalone singular over libsingular called from sage seems to be due in large part to its faster memory allocator, and we can make the singular version significantly faster by forcing sage to use tcmalloc instead of the system malloc():

```
$ LD_PRELOAD="/usr/lib/libtcmalloc.so.4" sage
...
sage: var('a,b,c')
(a, b, c)
sage: %time _=expand((a+b+c+1)^100)
CPU times: user 2.89 s, sys: 36 ms, total: 2.92 s
Wall time: 2.92 s
sage: P.<a,b,c> = PolynomialRing(QQ,order='lex')
sage: %time _=(a+b+c+1)^100
CPU times: user 3.4 s, sys: 12 ms, total: 3.41 s
Wall time: 3.41 s
```



---

Comment by zimmerma created at 2014-03-15 22:31:26

the speedup obtained with tcmalloc is impressive, could this be useful in other parts of Sage?

Paul


---

Comment by mmezzarobba created at 2014-03-16 09:19:26

Changing component from commutative algebra to performance.


---

Comment by mmezzarobba created at 2014-03-16 09:19:26

Changing type from defect to enhancement.


---

Comment by mmezzarobba created at 2014-03-16 09:19:26

Changing assignee from malb to tbd.


---

Comment by mmezzarobba created at 2014-03-16 09:42:36

Replying to [comment:5 zimmerma]:
> the speedup obtained with tcmalloc is impressive, could this be useful in other parts of Sage?

I guess so... But that's hard to tell without more profiling, and I don't really know what to test.

See #15950.
