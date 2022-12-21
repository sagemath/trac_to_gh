# Issue 4716: [with patch, needs review] Small bug in KodairaSymbol

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-12-05 12:02:53

Assignee: was

Keywords: Elliptic curves

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


The patch is based on 3.2.1.


---

Attachment

This is a dupe of #4715.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-05 12:08:09

Resolution: duplicate
