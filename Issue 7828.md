# Issue 7828: There should be a top-level sign() function.

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-01-03 05:34:19

Assignee: AlexGhitza




---

Comment by robertwb created at 2010-01-03 06:05:35

Apparently, it's called `sgn`, but perhaps we should have sign as an alias.


---

Comment by mhansen created at 2010-01-03 18:04:32

Especially, if some of the methods are .sign().


---

Comment by kcrisman created at 2010-05-26 19:17:47

Okay, this makes lots of sense, and in fact we should check hasattr with that first.  Patch coming up, which should work but will also allow (perhaps this is not good):

```
            sage: p = PermutationGroupElement('(3,4,8,7,9)')
            sage: p.sign()
            1
            sage: sign(p)
            1
```



---

Comment by kcrisman created at 2010-05-26 19:26:47

Based on 4.4.2


---

Attachment


---

Comment by kcrisman created at 2010-05-26 19:27:08

Changing status from new to needs_review.


---

Comment by cremona created at 2010-05-27 21:11:30

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-05-27 21:11:30

Looks good, applies fine to 4.4.3.alpha0 and tests pass.

I did wonder whether it would be better to return a Sage integer rather than an int?

Also, I looked for places where sgn() was used/defined and found a redundant  definition of sgn() in quadratic_forms/extras.py, which I am removing in another ticket (#9068).


---

Comment by kcrisman created at 2010-05-28 00:10:31

> I did wonder whether it would be better to return a Sage integer rather than an int?

Hmm, that is an interesting thing I should have considered but did not.  As long as we are consistent, that's probably the main thing, though it is often helpful to return something that has the Integer methods... Are there any current sign()/sgn() methods that return something other than an int?  

Usually one just adds or multiplies it with Integers, but I could imagine that sometimes the output itself would be important and that it should also then be an Integer.  If so... another ticket, or on this one?


---

Comment by cremona created at 2010-05-28 08:18:33

Well, I did look for other places where methods sgn() or sign() were defined;  since in fact I have another comment, which is that as well as looking to see if x has a method sign() you should also look for a method sgn().  The only thing I found was that function in quadratic_forms, and that distracted me from making this comment.

I will do the following now, and report back:

 1. Apply both your patch and mine at #9068
 2. Change the function you changed in two ways: making the return type Integer and also checking for x.sgn()
 3. Test the whole library.

For the moment I have reverted this to "needs work".


---

Comment by cremona created at 2010-05-28 08:18:33

Changing status from positive_review to needs_work.


---

Attachment

Apply after previous


---

Comment by cremona created at 2010-05-28 09:05:20

Changing keywords from "" to "sign sgn".


---

Comment by cremona created at 2010-05-28 09:05:20

Changing component from algebra to basic arithmetic.


---

Comment by cremona created at 2010-05-28 09:05:20

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-05-28 09:05:20

OK, I did that (see the reviewer patch).  All tests pass (note that I also had my patch from #9068 applied).

I think we need an independent reviewer of the combined changes (preferably of #9068 also) so I have put it back to "needs review".


---

Comment by robertwb created at 2010-05-28 17:24:42

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-05-28 17:24:42

Looks good to me.


---

Comment by mhansen created at 2010-06-06 08:37:15

Resolution: fixed


---

Comment by burcin created at 2010-09-09 09:32:29

Was there a concious decision in this ticket (or elsewhere) not to standardize on either `sign()` or `sgn()`. I just saw the relevant part of `sage/functions/generalized.py`, and thought one of these is redundant.


---

Comment by kcrisman created at 2010-09-09 13:11:06

I think the point was that not everyone would think of `sign()` or `sgn()` automatically; depending on where you come from mathematically, one or the other is more natural.  This doesn't seem to me to be a problem; we have lots of aliases, and it seems very unlikely that there would be confusion once someone saw both of them, as sgn is clearly short for sign.

Or maybe you mean we should pick one and leave the other one as an unspoken alias.  

However, I guess in this ticket and #9068 there is an implicit assumption that the methods (as opposed to functions) should be called `.sign()`.  Is that bad?


---

Comment by burcin created at 2010-09-13 09:08:35

I suggest we choose `sign()` as the convention and make `sgn()` an alias where necessary. Then we don't need to check for the existence of both `.sign()` and `.sgn()` methods. That code (around line 474 of `sage/functions/generalized.py`) suggests we encourage sloppy programming.

Shall I open a ticket to look through the library for `sgn()` and `sign()` functions and change them appropriately?


---

Comment by kcrisman created at 2010-09-13 14:52:44

I think that cremona already did this, but put this in there just in case there was another one.   So are you suggesting that the reviewer patch should be modified?  I think that the fear is that someone will put in a `.sgn()` method and won't realize it won't work; on the other hand, one could check for `.sgn()` and raise an error, but that also would make it look weird.  Though I wouldn't say sloppy, but rather decentralized programming.
