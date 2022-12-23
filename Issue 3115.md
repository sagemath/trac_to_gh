# Issue 3115: scientific notation exponents should be multiples of 3

Issue created by migration from https://trac.sagemath.org/ticket/3115

Original creator: schilly

Original creation time: 2008-05-06 22:25:57

Assignee: jkantor


```
sage: R = RealField(sci_not=True)
sage: a = R(23.4)
sage: a
2.34000000000000e1
sage: a = R(234.5)
sage: a
2.34500000000000e2
```


The exponent should only be a multiple of three for readability, because of units and its prefix names.


---

Comment by jason created at 2008-05-06 23:26:39

It seems that the calculators I remember distinguished between "scientific notation" (where the powers would be any power to make the number between 1 and 10) and "engineering notation" (where the exponent was a multiple of 3).  Maybe we should make RDF take a notation parameter, which could be "scientific" or "engineering" or None?


---

Comment by mhansen created at 2008-05-07 01:56:16

I think it might be useful to unify the repr mechanism for RDF, CDF, RR, and CC.


---

Comment by schilly created at 2008-05-07 08:19:59

Replying to [comment:1 jason]:
> "scientific notation" ... "engineering notation" 

yes, you are right. regarding calculators something else comes to my mind, too: displaying rounded values. internally it calculates with doubles and full precision, but it  just displays 3 or 4 significant digits. since in engeneering everything is just a "real" value, too many digits make no sense. The most general implementation would then be a format string or parameter list to indicate the number of significant digits and a characterization of the exponent: "4Esci" or "3Eeng" or as parameter list: significant=4, =3, sci_not="sci", ="eng" - e.g. resulting in 13.4e3 for 13391.131423 formatted as significant=3 sci_not="eng"


---

Comment by jason created at 2008-05-07 09:33:55

Can I make a suggestion?  sci_not seems terribly confusing; it sounds like "not sci something-or-other".  Can we make that notation="scientific" or notation="engineering"?

I think it's a good convention in python to always spell things out explicitly if at all possible.  It makes for much more readable code.

It would be nice to have a "display precision" option, if that's not already available.


---

Comment by cwitty created at 2008-05-10 20:17:31

For RR, we have multiple fields that differ only in their printing options, and it's very painful; I wouldn't want to add this pain to RDF (and in fact I would like to remove it from RR).

I've been hoping that "printers" (briefly mentioned at the end of http://wiki.sagemath.org/days7/coercion) would happen; that sounds like a better way to handle this sort of thing.


---

Comment by schilly created at 2008-05-10 20:43:52

cwitty, you are right. i don't really understand your note on that page, but my idea now is, to have a formatter object, that is independent of the number class. then, one could set the formatter in the constructor or later with setFormatter(..).

mockup for engineering, 6 significant digits:


```
f = NumberFormatter("#.#####", exponent="engineering")
[or similar]
f = NumberFormatter(significant=6, exponent="engineering")
r = RealField(formatter=f)
[or later]
r.setFormatter(f)
```


with such a formatter assigned, the string representation is passed through that parser.


---

Comment by cwitty created at 2008-05-10 21:21:12

OK, it looks like I totally misunderstood the "printers" idea.

My contention is that configurable printing should be associated with the top-level read-eval-print loop (that is, basically in a global variable), rather than being associated with particular parents (fields/rings/etc.)  It is the idea of having parents that differ only in how elements print that I consider painful.

Consider:

```
f1 = NumberFormatter(significant=5, exponent="engineering")
f2 = NumberFormatter(significant=6, exponent="engineering")
r1 = RealField(formatter=f1)
r1b = RealField(formatter=f1)
r2 = RealField(formatter=f2)
```

Do we have `r1==RR`?  Do we have `r1==r1b`?  Do we have `r1==r2`?  Do we have `r1 is r1b`?  Do any of these change if we do `r1.setFormatter(f2)`?

(Note that if we have `r1 is r1b` and we also have `setFormatter`, then you can accidentally change the formatting of an existing field when you think you're creating a new field and changing the formatting of the new field.  On the other hand, if we don't have `r1 is r1b`, then we can't cache field creation, which is a horrible performance hit; I've seen Sage programs that speed up by a factor of 2 when field creation is cached.)

How does `r1(pi)+r2(e)` print?

Can you set the formatter on the global `RR`?  If so, does that also change the printing of `CC`?

How should zeta_symmetric(2/3) print?  (Currently this creates a brand new RealField() and the return value will print according to that RealField().)
