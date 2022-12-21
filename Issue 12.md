# Issue 12: confusing behaviour of pAdicField with series_print == False

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-09-12 20:15:57

Assignee: somebody

The following behaviour, while strictly speaking not incorrect, is quite confusing:

```
sage: K = pAdicField(5, series_print=False)
sage:  K(37, prec=1)
 5^0 * (37 + O(5^1))
```


Really, it should be reducing 37 mod 5 when you do the conversion, or at the very least when you print it out, otherwise you don't realise that 37 + O(5) and 7 + O(5) are really the same thing. (This caused me a few hours of head-scratching today because I thought that two things didn't agree when actually they did.)

If you use the default series_print=True, then this doesn't happen:

```
sage: K = pAdicField(5)
sage:  K(37, prec=1)
 2 + O(5)
```




---

Comment by was created at 2007-01-13 01:59:20

This option doesn't exist anymore....


---

Comment by was created at 2007-01-13 01:59:20

Resolution: invalid
