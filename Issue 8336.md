# Issue 8336: round(x) <> x.round() for x in RealField

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-02-23 18:00:50

Assignee: AlexGhitza

CC:  was jason robertwb ncalexan craigcitro mabshoff

This is related to #188 and #2899.

```
sage: R=RealField(150)
sage: x=R(3493274823748475345934875398475345349.9343498375)
sage: y=round(x)
sage: y, type(y)
(3.49327482375e+36, <type 'sage.rings.real_double.RealDoubleElement'>)
sage: z=x.round()
sage: z, type(z)
(3493274823748475345934875398475345350, <type 'sage.rings.integer.Integer'>)
```

If one performs `ZZ(y)` to convert `y` to an integer, one
has a huge loss of accuracy.

I see no point of forcing coercion to RDF, which has limited precision and exponent range.

I would expect `round(x)` to return the same value as `z`,
either as Integer or RealField.


---

Comment by robertwb created at 2010-02-23 20:16:38

+1 I was bitten by this myself recently.


---

Comment by zimmerma created at 2010-03-13 21:26:38

I removed my name as "author" since I only reported that problem.


---

Comment by donmorrison created at 2010-11-09 01:00:51

Changing status from new to needs_info.


---

Comment by donmorrison created at 2010-11-09 01:00:51

With much help from Robert Bradshaw, I wrote some code for this ticket, that does the rounding, though it leaves trailing zeros in the destination type.  Robert: Is the latter not a separate (display) issue?  You noted off-list that the return type should have the same precision.  If so, I don't think they will uniformly display without treating the issues separately.  (If so, the one issue per ticket rule applies.)  Much thanks.


---

Comment by robertwb created at 2010-11-09 07:31:36

Changing assignee from AlexGhitza to robertwb.


---

Comment by robertwb created at 2010-11-09 07:31:36

Patch? I think 

sage: round(2.5)
2.500000000000

is just fine for elements of RR.


---

Comment by robertwb created at 2010-11-09 07:32:27

Correction: 


```
sage: round(2.5)
3
sage: round(2.5, ndigits=1)
2.500000000000
```



---

Comment by zimmerma created at 2010-11-09 09:53:45

Replying to [comment:5 robertwb]:
> Correction: 
> 
> {{{
> sage: round(2.5)
> 3
> sage: round(2.5, ndigits=1)
> 2.500000000000
> }}}

it is fine for me that `round(x)` returns a float, however I don't understand why it returns
a float of fixed precision (RDF). It should then be called `RDF_round`. It would be more
natural to return a float with the same precision as the input.

Paul


---

Comment by robertwb created at 2010-11-09 21:29:02

I don't think it should return a float of fixed precision, it just so happened that the input was 53 bits. 

What I want is round(x) to call x.round() and possibly x.round(ndigits=ndigits), if available. Thus


```
sage: L = [RDF(pi), RealField(100)(pi), float(pi)]
sage: [x.round() for x in L if hasattr(x, 'round')]
[3, 3]
sage: [round(x) for x in L]
[3, 3, 3]

sage: [x.round(ndigits=2) for x in L if hasattr(x, 'round')]
[3.14, 3.1400000000000000000000000000]
sage: [round(x, ndigits=2) for x in L]
[3.14, 3.1400000000000000000000000000, 3.1400000000000001]
sage: [parent(round(x, ndigits=2)) is parent(x) for x in L]
[True, True, True]
```


Sometimes it seems it'd be quicker to just code this up than keep talking about it :).


---

Comment by donmorrison created at 2010-11-09 22:26:29

patch for release "barnacle" ;)


---

Comment by donmorrison created at 2010-11-09 22:28:25

Changing status from needs_info to needs_work.


---

Attachment

Whoops, I didn't realize uploading the patch would end my comments.  I wanted to say, you didn't like that patch Robert.  What's the next step?


---

Comment by zimmerma created at 2010-11-10 08:42:57

> What I want is round(x) to call x.round() and possibly x.round(ndigits=ndigits), if available. 

this would be ok for me.

Paul

PS: donmorrison, your patch is missing some examples checking the new behaviour.


---

Comment by donmorrison created at 2010-11-10 14:15:14

Thanks Paul.  The patch I sent is incomplete because it breaks doctests for the following:

./sage -t  -force_lib "devel/sage/doc/en/thematic_tutorials/linear_programming.rst";

./sage -t  -force_lib "devel/sage/sage/misc/functional.py";

./sage -t  -force_lib "devel/sage/sage/numerical/mip.pyx";


---

Comment by mhansen created at 2011-12-18 15:43:29

Resolution: invalid


---

Comment by mhansen created at 2011-12-18 15:43:29

I'm going to close this as invalid now since we have the following behavior:


```
sage: R = RealField(150)
sage: x = R(3493274823748475345934875398475345349.9343498375)
sage: y = round(x)
sage: y, type(y)
(3493274823748475345934875398475345350, <type 'sage.rings.integer.Integer'>)
sage: z = x.round()
sage: z, type(z)
(3493274823748475345934875398475345350, <type 'sage.rings.integer.Integer'>)
```



---

Comment by zimmerma created at 2011-12-19 11:26:27

I agree to close that ticket. Just for the record, it would be nice to track down which patch did
fix that issue.

Paul
