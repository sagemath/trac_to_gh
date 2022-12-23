# Issue 4715: Small bug in KodairaSymbol

Issue created by migration from https://trac.sagemath.org/ticket/4715

Original creator: cremona

Original creation time: 2008-12-05 11:58:25

Assignee: was

CC:  tnagel

#4412 had a buglet:  for Kodaira Class Im the _roman field was not being set (it should be 1).  This is only currently used in the tamagawa_exponent() function for elliptic curves over number fields.

One-line patch coming up, plus a corresponding doctest.

This was reported by Tobias Nagel:

```
sage: E=EllipticCurve('117a3');                        
sage: E.tamagawa_exponent(13)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/tobi/test_Sint/<ipython console> in <module>()

/home/tobi/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in tamagawa_exponent(self, p)
 2190             return cp
 2191         ks = self.kodaira_type(p)
-> 2192         if ks._roman==1 and ks._n%2==0 and ks._starred:
 2193             return 2
 2194         return 4

AttributeError: 'KodairaSymbol_class' object has no attribute '_roman'
```




---

Attachment


---

Comment by cremona created at 2008-12-05 12:17:43

There's another problem, watch this space:

```
sage: E=EllipticCurve('153c2')
sage: E.tamagawa_exponent(3)
<boom>
```



---

Attachment

Fixing that also showed up the following completely independent bug (only on 32-bit machines though):

```
sage: E=EllipticCurve('903b3')
sage: E.pari_curve()
<boom> (PariError: precision too low)
```


The second patch fixes that as well as the other (which only applied to type I*0).  Now I have checked tamagawa_index() for all curves in the database up to conductor 10000 and all bad primes for each, so I hope that's that.

To fix the pari precision problem I did a try/except which keeps doubling the precision until it's ok.  I hope that is not against the rules:  if pari's ellinit every crashes for a reason other than precision, this would be an infinite loop.

In the course of this testing I found that looping through thousands of curves ate up a lot of memory.  I made a change so that for curves over QQ, local_data() uses prime integers arther than prime ideals, and that helps a bit, but there is still more memory begin eaten up than I would like.  For example:

```
sage: for e in cremona_curves(srange(11,10000)):
    for p in e.conductor().support():
        ld = e.local_data(p)
        print e.cremona_label()   
```

On my machine the used RAM creeps up gradually, hits 1GB at around conductor 2400, and if I let it continue it starts to make my machine really suffer at 1.7GB (no prizes for guessing the amount of RAM I have).

This might deserve a separate ticket.


---

Comment by mabshoff created at 2008-12-05 18:42:47

Hi John,

please open a ticket for the memory issues/leaks you are seeing. We are current chasing a number of leaks, most of which seem coercion related.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-07 09:07:17

Resolution: fixed


---

Comment by mabshoff created at 2008-12-07 09:07:17

Merged both patches in Sage 3.2.2.alpha1


---

Comment by jdemeyer created at 2010-09-19 09:34:41

In #9931, I plan to revert this ticket's patch to `sage/schemes/elliptic_curves/ell_rational_field.py`, since the workaround seems not needed anymore.
