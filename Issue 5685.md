# Issue 5685: enhanced nth_root in ZZ and QQ and related utilities

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-04-04 20:55:32

Assignee: somebody

Keywords: nth root rational integer

As discussed here: http://groups.google.co.uk/group/sage-nt/browse_thread/thread/4c6e60b6a20cabae#

I do not like this inconsistency between ZZ and QQ:


```
sage: a=ZZ(8)
sage: a.nth_root(3)
2
sage: b=QQ(8)
sage: b.nth_root(3)
2
sage: a.nth_root(2)
2
sage: b.nth_root(2)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/masgaj/.sage/temp/host_56_150/13463/_home_masgaj_sage_egros_sage_5.py
in <module>()

/local/jec/sage-3.4/local/lib/python2.5/site-packages/sage/rings/rational.so
in sage.rings.rational.Rational.nth_root
(sage/rings/rational.c:8888)()

ValueError: not a perfect nth power
```


I cannot think of a reason why we have an nth_root function on
integers which silently truncates a real root for positive argument
and gives a ValueError for negative ones.

The attached ticket deals with this, and at the same time adds a couple of extra utilities which I needed for rational numbers.


---

Comment by cremona created at 2009-04-04 20:56:03

Applies to 3.4.1.alpha0


---

Attachment


---

Comment by was created at 2009-04-10 14:49:18

* The new code you added to extended_integer_ring.py is this:

```
 	199	    def nth_root(self, n, truncate_mode=0): 
 	200	        temp = Integer.nth_root(self, n, truncate_mode) 
 	201	        if truncate_mode: 
 	202	            return self.parent()(temp[0]), temp[1]
```

There is no documentation or docstring or doctests.

* In integer.pyx:

```
def nth_root(self, int n, int truncate_mode=0): 
```

Should the truncate_mode be of type bint (=boolean int)?

Otherwise, I like this patch. 

 -- William


---

Comment by cremona created at 2009-04-10 14:54:57

Thanks for the review (and implied joke!).  I will add tests, and change int to bint (which I did not know about...)


---

Attachment

I have added a new patch which replaces the previous one and adds a docstring as requested, and changes the int type to bint.  I wanted to add a doctest which tests the nth_root() function on an Infinite value, but totally failed to construct such a value in the correct class.  This could be revisited when the person who wrote this class documents some more basic things like that.


---

Comment by was created at 2009-04-12 04:47:37

I'm fine with this patch.  John, if you want to polish it some more, this error message reads funny:


```
sage: a = 9
sage: a.nth_root(3)
...
ValueError: 9 is not an 3'th power
```



---

Comment by cremona created at 2009-04-12 10:36:57

Apply all three patches


---

Attachment

The extra patch does the suggested polishing, by adding a method to the integer class, ordinal_str(), which adds the correct suffix ('st', 'nd', 'th'), and then uses that.  I knew of one other place where similar messages were output in rings/number_fields/order.py and changed that too.  I hope I got it right!  Suitable doctests have been added.

I made the 3rd patch based on 3.4.1.rc2 + the first patch, forgetting the second, so I hope it applies ok.


---

Comment by mabshoff created at 2009-04-13 06:08:36

Hmm, this patch set depends on the existence of sage/rings/extended_integer_ring.py which was removed in #5735. Could you rebase these three patches or is the removal of that file an issue? 

Cheers,

Michael


---

Comment by cremona created at 2009-04-13 09:41:11

Replying to [comment:7 mabshoff]:
> Hmm, this patch set depends on the existence of sage/rings/extended_integer_ring.py which was removed in #5735. Could you rebase these three patches or is the removal of that file an issue? 
> 
> Cheers,
> 
> Michael
That should not be an issue at all, just ignore the bit of the patch which touches the removed file.  I can do it but not right now, duty calls.   John


---

Comment by mabshoff created at 2009-04-13 09:49:58

Replying to [comment:8 cremona]:

Hi John,

> That should not be an issue at all, just ignore the bit of the patch which touches the removed file.  I can do it but not right now, duty calls.   John

Ok, I will take care of this in the morning. I know also know why RobertWB's patch at #5735 had rejection issues since he must have had this patch in his que.

I am reinstating the positive review and will merge all three patches into one modulo the changes for files that no longer exist.

Cheers,

Michael


---

Comment by cremona created at 2009-04-13 13:36:32

replace ALL the above, apply after #5735 patches


---

Attachment

I have uploaded a new rebased patch replacing all three (in fact the first was already subsumed into the second), based on 3.4.1.rc2 + patches at #5735 (deleteding extended_integer, extended_rational).  Hope this works ok.


---

Comment by mabshoff created at 2009-04-13 22:09:33

Hmm, I am not sure what happened, but only the latest rebased patch has some rejection issues in integer.pyx: 

```
sage-3.4.1.rc3/devel/sage$ patch -p1 --dry-run < trac_5685_new.patch 
patching file sage/rings/integer.pyx
patching file sage/rings/qqbar.py
patching file sage/rings/rational.pyx
patching file sage/schemes/elliptic_curves/ell_rational_field.py
patching file sage/rings/integer.pyx
Hunk #2 FAILED at 1538.
Hunk #3 succeeded at 1564 (offset -13 lines).
Hunk #4 FAILED at 1604.
2 out of 4 hunks FAILED -- saving rejects to file sage/rings/integer.pyx.rej
patching file sage/rings/number_field/order.py
patching file sage/rings/rational.pyx
Hunk #1 succeeded at 1218 (offset -37 lines).
Hunk #2 succeeded at 1242 (offset -37 lines).
```


I will poke around later and see what the problem is.

Cheers,

Michael


---

Comment by cremona created at 2009-04-14 11:02:28

Replying to [comment:11 mabshoff]:
> Hmm, I am not sure what happened, but only the latest rebased patch has some rejection issues in integer.pyx: 
> {{{
> sage-3.4.1.rc3/devel/sage$ patch -p1 --dry-run < trac_5685_new.patch 
> patching file sage/rings/integer.pyx
> patching file sage/rings/qqbar.py
> patching file sage/rings/rational.pyx
> patching file sage/schemes/elliptic_curves/ell_rational_field.py
> patching file sage/rings/integer.pyx
> Hunk #2 FAILED at 1538.
> Hunk #3 succeeded at 1564 (offset -13 lines).
> Hunk #4 FAILED at 1604.
> 2 out of 4 hunks FAILED -- saving rejects to file sage/rings/integer.pyx.rej
> patching file sage/rings/number_field/order.py
> patching file sage/rings/rational.pyx
> Hunk #1 succeeded at 1218 (offset -37 lines).
> Hunk #2 succeeded at 1242 (offset -37 lines).
> }}}
> 
> I will poke around later and see what the problem is.
> 
> Cheers,
> 
> Michael

It must be something else merged since 3.4.1.rc2 since I just tried again and had no problems with 3.4.1.rc2 + 5735 patches + the latest one here.


---

Comment by mabshoff created at 2009-04-15 00:23:08

Hi John,

I checked and I did not merge any patch into rc3 so far that touches integer.pyx. It is a problem with patch and not hg, i.e. a hg patch can (and does in this case) contain multiple diff for a file, so running it with --dry-run will not work. My apologies about being dumb in this case, but I am testing the patch right now and will merge it in case it doctests.

Cheers,

Mihcael


---

Comment by mabshoff created at 2009-04-15 00:33:32

Merged trac_5685_new.patch in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-15 00:33:32

Resolution: fixed


---

Comment by cremona created at 2009-04-15 08:20:16

Replying to [comment:14 mabshoff]:
> Merged trac_5685_new.patch in Sage 3.4.1.rc3.
> 
> Cheers,
> 
> Michael

Thanks -- I hope I was not doing anything wrong in making the patch -- I used hg queues to combine the earlier ones and add the new stuff, but did not do a "hg qfold" as I think I should have done.  Sorry.
