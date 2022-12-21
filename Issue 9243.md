# Issue 9243: sage-doctest should use powers of 2 for return codes

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2010-06-15 09:33:59

Assignee: mvngu

CC:  wjp

Right now, sage-doctest uses these return codes:

```
# Return value in process exit code:
# 0: all tests passed
# 1: file not found
# 2: KeyboardInterrupt
# 3: doctest process was terminated by a signal
# 4: the doctesting framework raised an exception
# 100: failed doctests
```

In #8641 and #9224, we make sure that the return code gets passed on to the user, and for multiple files, we `or' the return codes together. It would be much nicer for the user if we used powers of 2 for return codes, so that it's easy to see exactly what happened. 

I recommend we change 3->4, 4->8, and 100->128 in sage-doctest.


---

Comment by ddrake created at 2010-06-16 04:50:43

Patch up, please review. This depends on #8641. I added an exit code of 16 for "bad options"; previously, sage-doctest exited with code 1 for both "file not found" and "bad options".


---

Comment by ddrake created at 2010-06-16 04:50:43

Changing status from new to needs_review.


---

Attachment

apply to scripts repo


---

Comment by ddrake created at 2010-06-18 02:03:51

The new patch changes the absurdly accurate reporting of how long the tests took when you hit Ctrl-C; before we had "KeyboardInterrupt -- interrupted after 2.2340259552 seconds!" and now it just uses one decimal place, instead of 10.


---

Comment by mpatel created at 2010-07-06 07:43:46

When #9316 merges, will we need to use 256, too, or use a different collection scheme?


---

Comment by wjp created at 2010-07-06 08:04:52

Thanks for adding me to CC.

I like this patch. There's one more instance, though: test_file in sage-ptest uses 5 as its own internal error code for unhandled exception. We should probably change that to 32. (And keep that one reserved.)

If #9316 is rebased on top of this one (which I can do), it will use error code 64 for timeouts.

All 8 available bits are then in use, so if we want to add more error conditions after that, we'll have to re-think this, or merge some error flags together.


Meta-comment: there are now three doctest related patches that I'm aware of, and that should probably all be merged. I would suggest this order: #9243, #9316, #8641.


---

Comment by wjp created at 2010-07-06 16:23:25

Meta-meta-comment: sorry, I'm blind. This patch already depends on #8641 of course. I'll rebase #9316 to apply after #8641 and #9243.


---

Comment by wjp created at 2010-07-06 20:51:27

apply after trac_9243.patch


---

Attachment

I added a patch to address the internally used error code 5.

Positive review for the rest of the patch. Could someone review my small reviewer patch?


---

Comment by mpatel created at 2010-07-07 03:14:50

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-07 03:14:50

To release manager: Apply _both_ patches to 4.5.alpha4 + #8641.


---

Comment by ddrake created at 2010-07-22 07:51:37

Resolution: fixed


---

Comment by ddrake created at 2010-07-22 07:51:37

Merged both patches in 4.5.2.alpha1.
