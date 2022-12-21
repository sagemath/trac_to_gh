# Issue 8173: segfault in singular resultant

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-02-03 13:40:53

Assignee: malb

CC:  polybori

Keywords: singular

On 4.3.2.alpha2:


```
sage: R.<x,y,a,b,u>=PolynomialRing(ZZ, 5)
sage: r = (x^4*y^2+x^2*y-y).resultant(x*y-y*a-x*b+a*b+u,x)

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0xb7d8b8c0 (LWP 28007)]
0xb72844c5 in __gmpn_copyi ()
   from /scratch/berocal/sage/i686/sage-4.3.rc0/local/lib/libgmp.so.3
Current language:  auto; currently asm
(gdb) bt
#0  0xb72844c5 in __gmpn_copyi ()
   from /scratch/berocal/sage/i686/sage-4.3.rc0/local/lib/libgmp.so.3
#1  0xb72647f2 in __gmpz_init_set ()
   from /scratch/berocal/sage/i686/sage-4.3.rc0/local/lib/libgmp.so.3
#2  0x00000005 in ?? ()
#3  0xbfe225b8 in ?? ()
#4  0xbfe225f8 in ?? ()
#5  0xb3d7fcb5 in conv_SingPFactoryP (p=0xb3efa4a0, r=0xb3db7980)
    at clapconv.cc:143
Backtrace stopped: previous frame inner to this frame (corrupt stack?)
```


Sage calls `singclap_resultant()`.


---

Comment by burcin created at 2010-02-03 14:03:55

This works:


```
sage: R.<x,y,a,b,u>=PolynomialRing(QQ, 5)  
sage: (x^4*y^2+x^2*y-y).resultant(x*y-y*a-x*b+a*b+u,x)
y^6*a^4 - 4*y^5*a^4*b + 6*y^4*a^4*b^2 - 4*y^3*a^4*b^3 + y^2*a^4*b^4 - 4*y^5*a^3*u + 12*y^4*a^3*b*u - 12*y^3*a^3*b^2*u + 4*y^2*a^3*b^3*u + 6*y^4*a^2*u^2 - 12*y^3*a^2*b*u^2 + 6*y^2*a^2*b^2*u^2 + y^5*a^2 - 4*y^4*a^2*b + 6*y^3*a^2*b^2 - 4*y^2*a^2*b^3 + y*a^2*b^4 - 4*y^3*a*u^3 + 4*y^2*a*b*u^3 - 2*y^4*a*u + 6*y^3*a*b*u - 6*y^2*a*b^2*u + 2*y*a*b^3*u + y^2*u^4 - y^5 + 4*y^4*b - 6*y^3*b^2 + 4*y^2*b^3 - y*b^4 + y^3*u^2 - 2*y^2*b*u^2 + y*b^2*u^2
```



---

Comment by malb created at 2010-02-03 14:12:01

In Singular:


```
> ring r = integer,(x,y,a,b,u),dp;
> poly f = x^4*y^2+x^2*y-y;
> resultant(f,x*y-y*a-x*b+a*b+u,x);
   ? not implemented
```


vs.


```
> ring r = 0,(x,y,a,b,u),dp;
> poly f = x^4*y^2+x^2*y-y;
> resultant(f,x*y-y*a-x*b+a*b+u,x);
y6a4-4y5a4b+6y4a4b2-4y3a4b3+y2a4b4-4y5a3u+12y4a3bu-12y3a3b2u+4y2a3b3u+6y4a2u2-12y3a2bu2+6y2a2b2u2+y5a2-4y4a2b+6y3a2b2-4y2a2b3+ya2b4-4y3au3+4y2abu3-2y4au+6y3abu-6y2ab2u+2yab3u+y2u4-y5+4y4b-6y3b2+4y2b3-yb4+y3u2-2y2bu2+yb2u2
```


So shall we lift to QQ, compute the resultant and then convert back?


---

Comment by PolyBoRi created at 2010-02-03 14:49:49

> So shall we lift to QQ, compute the resultant and then convert back?
sounds reasonable.


---

Comment by malb created at 2010-02-09 20:47:37

Changing status from new to needs_review.


---

Comment by malb created at 2010-03-03 12:55:07

Burcin, can you review this ticket?


---

Comment by was created at 2010-03-15 06:37:30

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-03-15 06:37:30

Wow, I just ran into exactly this same segfault "in the wild" while doing some math.  

I'm glad you fixed this.


---

Comment by was created at 2010-03-15 06:41:31

One doctest fails on sage.math after applying the patch:

```
sage -t  devel/sage/sage/rings/polynomial/term_order.py                                
         [3.0 s]                                                                       
sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx             
**********************************************************************                 
File "/virtual/scratch/wstein/build/sage-4.3.4.alpha1/devel/sage-main/sage/rings/polynomial/multi_polynomial_libsingular.pyx", line 4293:                                             
    sage: r                                                                                
Expected:                                                                                  
    y^6*a^4 - 4*y^5*a^4*b - 4*y^5*a^3*u + y^5*a^2 - y^5 + 6*y^4*a^4*b^2 + 12*y^4*a^3*b*u - 4*y^4*a^2*b + 6*y^4*a^2*u^2 - 2*y^4*a*u + 4*y^4*b \                                        
    - 4*y^3*a^4*b^3 - 12*y^3*a^3*b^2*u + 6*y^3*a^2*b^2 - 12*y^3*a^2*b*u^2 + 6*y^3*a*b*u - 4*y^3*a*u^3 - 6*y^3*b^2 + y^3*u^2 + y^2*a^4*b^4 \                                           
    + 4*y^2*a^3*b^3*u - 4*y^2*a^2*b^3 + 6*y^2*a^2*b^2*u^2 - 6*y^2*a*b^2*u + 4*y^2*a*b*u^3 + 4*y^2*b^3 - 2*y^2*b*u^2 + y^2*u^4 + y*a^2*b^4 \                                           
    + 2*y*a*b^3*u - y*b^4 + y*b^2*u^2                                                      
Got:                                                                                       
    y^6*a^4 - 4*y^5*a^4*b - 4*y^5*a^3*u + y^5*a^2 - y^5 + 6*y^4*a^4*b^2 + 12*y^4*a^3*b*u - 4*y^4*a^2*b + 6*y^4*a^2*u^2 - 2*y^4*a*u + 4*y^4*b - 4*y^3*a^4*b^3 - 12*y^3*a^3*b^2*u + 6*y^3*a^2*b^2 - 12*y^3*a^2*b*u^2 + 6*y^3*a*b*u - 4*y^3*a*u^3 - 6*y^3*b^2 + y^3*u^2 + y^2*a^4*b^4 + 4*y^2*a^3*b^3*u - 4*y^2*a^2*b^3 + 6*y^2*a^2*b^2*u^2 - 6*y^2*a*b^2*u + 4*y^2*a*b*u^3 + 4*y^2*b^3 - 2*y^2*b*u^2 + y^2*u^4 + y*a^2*b^4 + 2*y*a*b^3*u - y*b^4 + y*b^2*u^2             
**********************************************************************                     
1 items had failures:                                                                      
   1 of  19 in __main__.example_84                                                         
***Test Failed*** 1 failures.                                                              
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_multi_polynomial_libsingular.py                                                                                
         [9.5 s]            
```



---

Comment by was created at 2010-03-15 06:41:31

Changing status from positive_review to needs_work.


---

Comment by zimmerma created at 2010-06-05 11:56:24

Replying to [comment:7 was]:
> One doctest fails on sage.math after applying the patch: [...]

it seems just a formatting issue, both outputs are equal (and I don't understand why the 'expected'
one was split among several lines).

Note that I also had this problem with:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: P.<x,y> = PolynomialRing(ZZ,2)
sage: f = x+y
sage: g=y^2+x 
sage: f.resultant(g,y)
------------------------------------------------------------
Unhandled SIGFPE: An unhandled floating point exception occured in Sage.
This probably occured because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```

| Sage Version 4.4.2, Release Date: 2010-05-19                       |
| Type notebook() for the GUI, and license() for information.        |
Maybe we can just fix the doctest?


---

Comment by zimmerma created at 2010-06-05 11:56:24

Changing status from needs_work to needs_info.


---

Comment by malb created at 2010-07-14 13:30:56

I just tried the example above in my private Singular 3-1-1-3 + Sage 4.4 copy. 


```
sage: P.<x,y> = PolynomialRing(ZZ,2)
sage: f = x+y
sage: g=y^2+x 
sage: f.resultant(g,y)
y^2 - y
```

Thus, once#8059 is in, we can recheck and merge this patch?


---

Comment by malb created at 2010-07-14 13:30:56

Changing status from needs_info to needs_work.


---

Comment by zimmerma created at 2010-07-14 14:31:36

Replying to [comment:9 malb]:
> Thus, once#8059 is in, we can recheck and merge this patch?

yes this needs work, since the resultant in `y` should not contain `y`!!!


---

Comment by malb created at 2010-07-14 20:35:09

Argh, I didn't even check the output. Btw:


```
sage: P.<x,y> = PolynomialRing(QQ,2)
sage: f = x+
sage: g=y^2+
sage: f.resultant(g,y
x^2 + x
```



---

Attachment

fixed the issue reported bu Paul


---

Comment by malb created at 2010-07-14 21:21:13

Changing status from needs_work to positive_review.


---

Comment by malb created at 2010-07-14 21:21:13

The updated patch should fix the issue.


---

Comment by zimmerma created at 2010-07-15 08:32:13

Martin,

> status  changed from needs_work to positive_review

I guess you meant "needs review" instead of "positive review", since you are the author of the
patch? Otherwise you forgot to fill the author and reviewer fields :-)

Paul


---

Comment by malb created at 2010-07-15 08:39:31

Changing status from positive_review to needs_work.


---

Comment by malb created at 2010-07-15 08:39:59

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-07-15 08:39:59

Paul, I don't know where my head was yesterday. Thanks a lot for spotting this!


---

Comment by zimmerma created at 2010-07-15 09:15:16

Positive review. All doctests pass. Good work!

Paul


---

Comment by zimmerma created at 2010-07-15 09:15:16

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 01:45:02

Resolution: fixed
