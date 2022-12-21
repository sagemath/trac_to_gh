# Issue 5796: document bitsets and make interface consistent with python sets

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-04-16 03:12:06

Assignee: rlm, robertwb

CC:  rlm robertwb

The attached patch adds a lot of documentation to the bitsets in misc/bitset.*.  It also fixes a bug or two dealing with entries that are past the size of the set, but still within the last limb.

The other major contribution of the patch is to make the bitset interface consistent with the python set interface.  This is to make it very easy to transition from code that is written using python sets to changing it to use this bitset class.  Another advantage to changing the interface is that the language is more set-theoretic instead of demanding the user to understand the implementation details.

That said, the only big incompatible change in the interface is to make `bitset_clear` empty the set, rather than deallocate the set.  This is because the python set clear() function just empties a set.  To deallocate a bitset, use the `bitset_free` function after this patch.

I grepped through the sage library and changed the uses of bitset to use the more pythonic interface.

After this patch, doctests in misc/misc_c.pyx, groups/perm_gps/partn_ref/*.pyx, and coding/binary_code.pyx all pass (those were the places I found using bitsets).


---

Comment by jason created at 2009-04-16 03:30:18

Changing status from new to assigned.


---

Comment by jason created at 2009-04-16 03:30:18

Please delete the .2.patch file.


---

Comment by jason created at 2009-04-16 03:30:18

Changing assignee from rlm, robertwb to jason.


---

Comment by jason created at 2009-04-16 03:30:45

Robert and Robert: could one or both of you review this?  Thanks!


---

Comment by robertwb created at 2009-04-16 05:03:43

Looks good. Thanks!

Interestingly, I originally thought of "bitset" as packed, ordered sets of bits, more like a bit list, where your interpretation is clearly as sets implemented using bits. Of course, this works for both.


---

Comment by robertwb created at 2009-04-16 05:04:28

BTW, followup at #5800


---

Comment by mabshoff created at 2009-04-16 06:09:04

Mhh, two issues:

 * None of the old functions get deprecated. While this probably isn't too popular an interface I am still not too happy about this.
 * Did anyone valgrind this? While it seems like straightforward search and replace I am still not too comfortable merging this patch this late in the merge process.

So: bounced to 3.4.2 for now.

Cheers,

Michael


---

Comment by robertwb created at 2009-04-16 06:12:34

3.4.2 is fine, we need to get 3.4.1 out (I'm getting ready to assemble the release notes for Cython right now :). No, I didn't valgrind it. 

The old functions are still there in the "Aliases for functions" section. (I don't think any got removed...) Actually, I would be happier if the aliases were placed right next to the implementations, rather than elsewhere.


---

Comment by jason created at 2009-04-16 07:14:45

I agree it's probably a wise idea to bump this to 3.4.2 so any memory leaks can show up in testing.

I didn't delete any of the other functions.  I clumped them all together so that they would be easy to delete, though.  We don't have a deprecation procedure on cdef functions, do we?  Regardless, I'm okay with the aliases staying in.  The aliases also sort of follow some of the python set guidelines too (i.e., if a and b are python sets, then a & b == a intersect b, etc.)

I'll move the function aliases to be next to the original functions to make Robert happier.


---

Comment by mabshoff created at 2009-04-16 07:21:29

Thanks. I am not sure if we can deprecate cdef'ed functions, but I guess if we cannot do that yet we should implement it :)

Aside from that I want to avoid having _confusing_ APIs for the same thing, so this might be a candidate for 4.0. Since 3.4.2 should be rather short (famous last words ;)) it might get bumped even further, but we will see.

Jason: Anyway, thanks for cleaning this up. Is anything coming down the pipeline since you are working on this code? 

Cheers,

Michael


---

Comment by jason created at 2009-04-16 07:35:34

Robert,

It'd probably be good if you glanced at the new patch that goes on top of the original patch.  I moved the function definitions like you wanted, and also noticed that bitset_pop() was not tested, so I added a couple of tests for it.


---

Comment by jason created at 2009-04-16 07:41:00

mabshoff: yes, there is new code that will probably be using this this week.  That's why I was hoping to get it into 3.4.1, but it'd be great to get it into 3.4.2.

I left the old API in there just in case people really wanted to think about bitsets as bitlists and they wanted to and/or/xor them together, not necessarily "intersect/union/symmetric_difference" them together.  For example, if someone wanted a poor-man's GF(2) vector, for example.  The other reason I left them in there is for a deprecation period; didn't want to just delete the functions right off.  So I think the patch should go in with both APIs active (but notices in the docstrings for the non-set API).  Later on, we can deprecate and remove the API, but there's the "mandatory" 6-month rule, right?


---

Comment by robertwb created at 2009-04-16 07:46:15

Thanks, looks good.


---

Comment by rlm created at 2009-04-16 16:52:34

Whoa, why on Earth would we want to deprecate easy notation for hard?

bitset_not -> bitset_complement
bitset_and -> bitset_intersection
bitset_or -> bitset_union
bitset_xor -> bitset_symmetric_difference

All of these are much longer to type, and I don't see why any are better. I also don't think that making things more like Python is a good reason to deprecate what was originally there.

As one of bitset's main consumers, I must say I really dislike having to type "symmetric_difference" when all I want is an "xor". I vote against deprecation.


---

Comment by jason created at 2009-04-16 17:27:00

Okay, so we have one strong vote against deprecation (rlm), one mild vote against deprecation (me---I think both ways are equally valid ways to think about it), and some not-sure-how-to-count votes.  Sounds like we keep two interfaces, which I think is great.

rlm, seeing your feelings, I apologize for changing all of the partitioning code to use symmetric_difference instead of xor.  I'll change it back.  How about I revert the patch so that it just makes the following changes in the groups/perm_gps/partn_ref/*.pyx and coding/binary_code.pyx:

bitset_clear -> bitset_free

bitset_zero -> bitset_clear

Will that make you happier?


---

Comment by jason created at 2009-04-16 17:28:09

In fact, how about just the following change:

bitset_clear -> bitset_free

(so that we can use clear() the way python sets use it)

I'll leave bitset_zero alone.


---

Comment by rlm created at 2009-04-16 17:31:32

I definitely like the use of the word "free" there. It's more obvious that you're deallocating.

I'm happy with less changes in partn_ref. Thanks for offering to do that.


---

Attachment

Okay, either Robert, I think the .3.patch file is a good final version.  Can you look at it one more time?  I drastically cut down on the number of changes to existing code, just doing the necessary bitset_clear to bitset_free transition talked about above.

All tests pass in groups/perm_gps/partn_ref/*.pyx, coding/binary_code.pyx, and misc/*.pyx

You can delete all patches prior to the .3.patch.

Furthermore, after the patch:


```
sage: search_src('bitset_clear')
misc/misc_c.pyx:    bitset_clear(r)
misc/misc_c.pyx:        bitset_clear(r)
misc/misc_c.pyx:        bitset_clear(r)
misc/misc_c.pyx:        bitset_clear(r)
misc/misc_c.pyx:        bitset_clear(r)
misc/bitset.pxi:cdef inline void bitset_clear(bitset_t bits):
misc/bitset.pxi:    This function is the same as bitset_clear(bits).
misc/bitset.pxi:    bitset_clear(bits)
misc/bitset.pxi:        bitset_clear(r)
misc/bitset.pxi:        bitset_clear(r)
```


So I took care of all bitset_clear functions in existing code (the ones above in the misc/ directory use the new bitset_clear).

Because this was such a massive revision of the original patch, I'm calling for review again.


---

Comment by robertwb created at 2009-04-16 19:04:07

I was just writing a comment to that effect. I think we should definitely keep the xor, etc. methods around (somehow I missed that you were going to get rid of them). 

I reaffirm my positive review, and think it's even better now.


---

Comment by rlm created at 2009-04-16 20:25:55

Replying to [comment:18 robertwb]:
> I was just writing a comment to that effect. I think we should definitely keep the xor, etc. methods around (somehow I missed that you were going to get rid of them). 
> 
> I reaffirm my positive review, and think it's even better now. 

I second.


---

Comment by jason created at 2009-04-20 17:54:24

Robert and Robert,

When using this code this weekend, I found a bug in bitset_pop (it forgot to actually discard an element!).  I also implemented a bitset_len function, which corresponds to len(python set) and gives the number of things in the set.

Could you glance at the trac-5796-bitset-bugfix-len-function.patch and, if you like it, again put this patch as positive review?


---

Attachment

apply on top of first patch.


---

Comment by jason created at 2009-04-24 19:52:50

Robert and Robert,

Just pinging you (through trac email notifications) about this ticket.  If one of you could just look at the last patch (the bugfix-len one) and then positive-review the ticket, it'd be great.  In the patch, I fix one bug and add a bitset_len() function.  I put it on this ticket instead of opening a new ticket because of the bugfix.

Thanks, Jason


---

Comment by jason created at 2009-04-27 17:04:25

Moving to 3.4.2 now that it has a positive review to keep things cleaner.


---

Comment by mabshoff created at 2009-04-30 02:11:44

Unfortunately with both patches applied on sage.math I get one doctest failure in 

```
sage -t -long devel/sage/sage/misc/misc_c.pyx
```


Cheers,

Michael


---

Comment by jason created at 2009-05-06 04:11:49

apply on top of previous patches


---

Attachment

The 64-bit-doctest.patch addresses the doctest failure on 64-bit machines.


---

Comment by mabshoff created at 2009-05-06 04:23:25

Ok, positive review for 64-bit-doctest.patch resulting in a combined positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-11 11:41:48

Merged all three patches in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-11 11:41:48

Resolution: fixed
