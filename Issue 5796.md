# Issue 5796: document bitsets and make interface consistent with python sets

archive/issues_005796.json:
```json
{
    "body": "Assignee: rlm, robertwb\n\nCC:  rlm robertwb\n\nThe attached patch adds a lot of documentation to the bitsets in misc/bitset.*.  It also fixes a bug or two dealing with entries that are past the size of the set, but still within the last limb.\n\nThe other major contribution of the patch is to make the bitset interface consistent with the python set interface.  This is to make it very easy to transition from code that is written using python sets to changing it to use this bitset class.  Another advantage to changing the interface is that the language is more set-theoretic instead of demanding the user to understand the implementation details.\n\nThat said, the only big incompatible change in the interface is to make `bitset_clear` empty the set, rather than deallocate the set.  This is because the python set clear() function just empties a set.  To deallocate a bitset, use the `bitset_free` function after this patch.\n\nI grepped through the sage library and changed the uses of bitset to use the more pythonic interface.\n\nAfter this patch, doctests in misc/misc_c.pyx, groups/perm_gps/partn_ref/*.pyx, and coding/binary_code.pyx all pass (those were the places I found using bitsets).\n\nIssue created by migration from https://trac.sagemath.org/ticket/5796\n\n",
    "created_at": "2009-04-16T03:12:06Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "document bitsets and make interface consistent with python sets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5796",
    "user": "jason"
}
```
Assignee: rlm, robertwb

CC:  rlm robertwb

The attached patch adds a lot of documentation to the bitsets in misc/bitset.*.  It also fixes a bug or two dealing with entries that are past the size of the set, but still within the last limb.

The other major contribution of the patch is to make the bitset interface consistent with the python set interface.  This is to make it very easy to transition from code that is written using python sets to changing it to use this bitset class.  Another advantage to changing the interface is that the language is more set-theoretic instead of demanding the user to understand the implementation details.

That said, the only big incompatible change in the interface is to make `bitset_clear` empty the set, rather than deallocate the set.  This is because the python set clear() function just empties a set.  To deallocate a bitset, use the `bitset_free` function after this patch.

I grepped through the sage library and changed the uses of bitset to use the more pythonic interface.

After this patch, doctests in misc/misc_c.pyx, groups/perm_gps/partn_ref/*.pyx, and coding/binary_code.pyx all pass (those were the places I found using bitsets).

Issue created by migration from https://trac.sagemath.org/ticket/5796





---

archive/issue_comments_045450.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-16T03:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45450",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045451.json:
```json
{
    "body": "Please delete the .2.patch file.",
    "created_at": "2009-04-16T03:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45451",
    "user": "jason"
}
```

Please delete the .2.patch file.



---

archive/issue_comments_045452.json:
```json
{
    "body": "Changing assignee from rlm, robertwb to jason.",
    "created_at": "2009-04-16T03:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45452",
    "user": "jason"
}
```

Changing assignee from rlm, robertwb to jason.



---

archive/issue_comments_045453.json:
```json
{
    "body": "Robert and Robert: could one or both of you review this?  Thanks!",
    "created_at": "2009-04-16T03:30:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45453",
    "user": "jason"
}
```

Robert and Robert: could one or both of you review this?  Thanks!



---

archive/issue_comments_045454.json:
```json
{
    "body": "Looks good. Thanks!\n\nInterestingly, I originally thought of \"bitset\" as packed, ordered sets of bits, more like a bit list, where your interpretation is clearly as sets implemented using bits. Of course, this works for both.",
    "created_at": "2009-04-16T05:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45454",
    "user": "robertwb"
}
```

Looks good. Thanks!

Interestingly, I originally thought of "bitset" as packed, ordered sets of bits, more like a bit list, where your interpretation is clearly as sets implemented using bits. Of course, this works for both.



---

archive/issue_comments_045455.json:
```json
{
    "body": "BTW, followup at #5800",
    "created_at": "2009-04-16T05:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45455",
    "user": "robertwb"
}
```

BTW, followup at #5800



---

archive/issue_comments_045456.json:
```json
{
    "body": "Mhh, two issues:\n\n* None of the old functions get deprecated. While this probably isn't too popular an interface I am still not too happy about this.\n* Did anyone valgrind this? While it seems like straightforward search and replace I am still not too comfortable merging this patch this late in the merge process.\n\nSo: bounced to 3.4.2 for now.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T06:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45456",
    "user": "mabshoff"
}
```

Mhh, two issues:

* None of the old functions get deprecated. While this probably isn't too popular an interface I am still not too happy about this.
* Did anyone valgrind this? While it seems like straightforward search and replace I am still not too comfortable merging this patch this late in the merge process.

So: bounced to 3.4.2 for now.

Cheers,

Michael



---

archive/issue_comments_045457.json:
```json
{
    "body": "3.4.2 is fine, we need to get 3.4.1 out (I'm getting ready to assemble the release notes for Cython right now :). No, I didn't valgrind it. \n\nThe old functions are still there in the \"Aliases for functions\" section. (I don't think any got removed...) Actually, I would be happier if the aliases were placed right next to the implementations, rather than elsewhere.",
    "created_at": "2009-04-16T06:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45457",
    "user": "robertwb"
}
```

3.4.2 is fine, we need to get 3.4.1 out (I'm getting ready to assemble the release notes for Cython right now :). No, I didn't valgrind it. 

The old functions are still there in the "Aliases for functions" section. (I don't think any got removed...) Actually, I would be happier if the aliases were placed right next to the implementations, rather than elsewhere.



---

archive/issue_comments_045458.json:
```json
{
    "body": "I agree it's probably a wise idea to bump this to 3.4.2 so any memory leaks can show up in testing.\n\nI didn't delete any of the other functions.  I clumped them all together so that they would be easy to delete, though.  We don't have a deprecation procedure on cdef functions, do we?  Regardless, I'm okay with the aliases staying in.  The aliases also sort of follow some of the python set guidelines too (i.e., if a and b are python sets, then a & b == a intersect b, etc.)\n\nI'll move the function aliases to be next to the original functions to make Robert happier.",
    "created_at": "2009-04-16T07:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45458",
    "user": "jason"
}
```

I agree it's probably a wise idea to bump this to 3.4.2 so any memory leaks can show up in testing.

I didn't delete any of the other functions.  I clumped them all together so that they would be easy to delete, though.  We don't have a deprecation procedure on cdef functions, do we?  Regardless, I'm okay with the aliases staying in.  The aliases also sort of follow some of the python set guidelines too (i.e., if a and b are python sets, then a & b == a intersect b, etc.)

I'll move the function aliases to be next to the original functions to make Robert happier.



---

archive/issue_comments_045459.json:
```json
{
    "body": "Thanks. I am not sure if we can deprecate cdef'ed functions, but I guess if we cannot do that yet we should implement it :)\n\nAside from that I want to avoid having *confusing* APIs for the same thing, so this might be a candidate for 4.0. Since 3.4.2 should be rather short (famous last words ;)) it might get bumped even further, but we will see.\n\nJason: Anyway, thanks for cleaning this up. Is anything coming down the pipeline since you are working on this code? \n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T07:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45459",
    "user": "mabshoff"
}
```

Thanks. I am not sure if we can deprecate cdef'ed functions, but I guess if we cannot do that yet we should implement it :)

Aside from that I want to avoid having *confusing* APIs for the same thing, so this might be a candidate for 4.0. Since 3.4.2 should be rather short (famous last words ;)) it might get bumped even further, but we will see.

Jason: Anyway, thanks for cleaning this up. Is anything coming down the pipeline since you are working on this code? 

Cheers,

Michael



---

archive/issue_comments_045460.json:
```json
{
    "body": "Robert,\n\nIt'd probably be good if you glanced at the new patch that goes on top of the original patch.  I moved the function definitions like you wanted, and also noticed that bitset_pop() was not tested, so I added a couple of tests for it.",
    "created_at": "2009-04-16T07:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45460",
    "user": "jason"
}
```

Robert,

It'd probably be good if you glanced at the new patch that goes on top of the original patch.  I moved the function definitions like you wanted, and also noticed that bitset_pop() was not tested, so I added a couple of tests for it.



---

archive/issue_comments_045461.json:
```json
{
    "body": "mabshoff: yes, there is new code that will probably be using this this week.  That's why I was hoping to get it into 3.4.1, but it'd be great to get it into 3.4.2.\n\nI left the old API in there just in case people really wanted to think about bitsets as bitlists and they wanted to and/or/xor them together, not necessarily \"intersect/union/symmetric_difference\" them together.  For example, if someone wanted a poor-man's GF(2) vector, for example.  The other reason I left them in there is for a deprecation period; didn't want to just delete the functions right off.  So I think the patch should go in with both APIs active (but notices in the docstrings for the non-set API).  Later on, we can deprecate and remove the API, but there's the \"mandatory\" 6-month rule, right?",
    "created_at": "2009-04-16T07:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45461",
    "user": "jason"
}
```

mabshoff: yes, there is new code that will probably be using this this week.  That's why I was hoping to get it into 3.4.1, but it'd be great to get it into 3.4.2.

I left the old API in there just in case people really wanted to think about bitsets as bitlists and they wanted to and/or/xor them together, not necessarily "intersect/union/symmetric_difference" them together.  For example, if someone wanted a poor-man's GF(2) vector, for example.  The other reason I left them in there is for a deprecation period; didn't want to just delete the functions right off.  So I think the patch should go in with both APIs active (but notices in the docstrings for the non-set API).  Later on, we can deprecate and remove the API, but there's the "mandatory" 6-month rule, right?



---

archive/issue_comments_045462.json:
```json
{
    "body": "Thanks, looks good.",
    "created_at": "2009-04-16T07:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45462",
    "user": "robertwb"
}
```

Thanks, looks good.



---

archive/issue_comments_045463.json:
```json
{
    "body": "Whoa, why on Earth would we want to deprecate easy notation for hard?\n\nbitset_not -> bitset_complement\nbitset_and -> bitset_intersection\nbitset_or -> bitset_union\nbitset_xor -> bitset_symmetric_difference\n\nAll of these are much longer to type, and I don't see why any are better. I also don't think that making things more like Python is a good reason to deprecate what was originally there.\n\nAs one of bitset's main consumers, I must say I really dislike having to type \"symmetric_difference\" when all I want is an \"xor\". I vote against deprecation.",
    "created_at": "2009-04-16T16:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45463",
    "user": "rlm"
}
```

Whoa, why on Earth would we want to deprecate easy notation for hard?

bitset_not -> bitset_complement
bitset_and -> bitset_intersection
bitset_or -> bitset_union
bitset_xor -> bitset_symmetric_difference

All of these are much longer to type, and I don't see why any are better. I also don't think that making things more like Python is a good reason to deprecate what was originally there.

As one of bitset's main consumers, I must say I really dislike having to type "symmetric_difference" when all I want is an "xor". I vote against deprecation.



---

archive/issue_comments_045464.json:
```json
{
    "body": "Okay, so we have one strong vote against deprecation (rlm), one mild vote against deprecation (me---I think both ways are equally valid ways to think about it), and some not-sure-how-to-count votes.  Sounds like we keep two interfaces, which I think is great.\n\nrlm, seeing your feelings, I apologize for changing all of the partitioning code to use symmetric_difference instead of xor.  I'll change it back.  How about I revert the patch so that it just makes the following changes in the groups/perm_gps/partn_ref/*.pyx and coding/binary_code.pyx:\n\nbitset_clear -> bitset_free\n\nbitset_zero -> bitset_clear\n\nWill that make you happier?",
    "created_at": "2009-04-16T17:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45464",
    "user": "jason"
}
```

Okay, so we have one strong vote against deprecation (rlm), one mild vote against deprecation (me---I think both ways are equally valid ways to think about it), and some not-sure-how-to-count votes.  Sounds like we keep two interfaces, which I think is great.

rlm, seeing your feelings, I apologize for changing all of the partitioning code to use symmetric_difference instead of xor.  I'll change it back.  How about I revert the patch so that it just makes the following changes in the groups/perm_gps/partn_ref/*.pyx and coding/binary_code.pyx:

bitset_clear -> bitset_free

bitset_zero -> bitset_clear

Will that make you happier?



---

archive/issue_comments_045465.json:
```json
{
    "body": "In fact, how about just the following change:\n\nbitset_clear -> bitset_free\n\n(so that we can use clear() the way python sets use it)\n\nI'll leave bitset_zero alone.",
    "created_at": "2009-04-16T17:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45465",
    "user": "jason"
}
```

In fact, how about just the following change:

bitset_clear -> bitset_free

(so that we can use clear() the way python sets use it)

I'll leave bitset_zero alone.



---

archive/issue_comments_045466.json:
```json
{
    "body": "I definitely like the use of the word \"free\" there. It's more obvious that you're deallocating.\n\nI'm happy with less changes in partn_ref. Thanks for offering to do that.",
    "created_at": "2009-04-16T17:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45466",
    "user": "rlm"
}
```

I definitely like the use of the word "free" there. It's more obvious that you're deallocating.

I'm happy with less changes in partn_ref. Thanks for offering to do that.



---

archive/issue_comments_045467.json:
```json
{
    "body": "Attachment [trac-5796-bitset-docs-api-cleanup.3.patch](tarball://root/attachments/some-uuid/ticket5796/trac-5796-bitset-docs-api-cleanup.3.patch) by jason created at 2009-04-16 18:55:38\n\nOkay, either Robert, I think the .3.patch file is a good final version.  Can you look at it one more time?  I drastically cut down on the number of changes to existing code, just doing the necessary bitset_clear to bitset_free transition talked about above.\n\nAll tests pass in groups/perm_gps/partn_ref/*.pyx, coding/binary_code.pyx, and misc/*.pyx\n\nYou can delete all patches prior to the .3.patch.\n\nFurthermore, after the patch:\n\n\n```\nsage: search_src('bitset_clear')\nmisc/misc_c.pyx:    bitset_clear(r)\nmisc/misc_c.pyx:        bitset_clear(r)\nmisc/misc_c.pyx:        bitset_clear(r)\nmisc/misc_c.pyx:        bitset_clear(r)\nmisc/misc_c.pyx:        bitset_clear(r)\nmisc/bitset.pxi:cdef inline void bitset_clear(bitset_t bits):\nmisc/bitset.pxi:    This function is the same as bitset_clear(bits).\nmisc/bitset.pxi:    bitset_clear(bits)\nmisc/bitset.pxi:        bitset_clear(r)\nmisc/bitset.pxi:        bitset_clear(r)\n```\n\n\nSo I took care of all bitset_clear functions in existing code (the ones above in the misc/ directory use the new bitset_clear).\n\nBecause this was such a massive revision of the original patch, I'm calling for review again.",
    "created_at": "2009-04-16T18:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45467",
    "user": "jason"
}
```

Attachment [trac-5796-bitset-docs-api-cleanup.3.patch](tarball://root/attachments/some-uuid/ticket5796/trac-5796-bitset-docs-api-cleanup.3.patch) by jason created at 2009-04-16 18:55:38

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

archive/issue_comments_045468.json:
```json
{
    "body": "I was just writing a comment to that effect. I think we should definitely keep the xor, etc. methods around (somehow I missed that you were going to get rid of them). \n\nI reaffirm my positive review, and think it's even better now.",
    "created_at": "2009-04-16T19:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45468",
    "user": "robertwb"
}
```

I was just writing a comment to that effect. I think we should definitely keep the xor, etc. methods around (somehow I missed that you were going to get rid of them). 

I reaffirm my positive review, and think it's even better now.



---

archive/issue_comments_045469.json:
```json
{
    "body": "Replying to [comment:18 robertwb]:\n> I was just writing a comment to that effect. I think we should definitely keep the xor, etc. methods around (somehow I missed that you were going to get rid of them). \n> \n> I reaffirm my positive review, and think it's even better now. \n\nI second.",
    "created_at": "2009-04-16T20:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45469",
    "user": "rlm"
}
```

Replying to [comment:18 robertwb]:
> I was just writing a comment to that effect. I think we should definitely keep the xor, etc. methods around (somehow I missed that you were going to get rid of them). 
> 
> I reaffirm my positive review, and think it's even better now. 

I second.



---

archive/issue_comments_045470.json:
```json
{
    "body": "Robert and Robert,\n\nWhen using this code this weekend, I found a bug in bitset_pop (it forgot to actually discard an element!).  I also implemented a bitset_len function, which corresponds to len(python set) and gives the number of things in the set.\n\nCould you glance at the trac-5796-bitset-bugfix-len-function.patch and, if you like it, again put this patch as positive review?",
    "created_at": "2009-04-20T17:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45470",
    "user": "jason"
}
```

Robert and Robert,

When using this code this weekend, I found a bug in bitset_pop (it forgot to actually discard an element!).  I also implemented a bitset_len function, which corresponds to len(python set) and gives the number of things in the set.

Could you glance at the trac-5796-bitset-bugfix-len-function.patch and, if you like it, again put this patch as positive review?



---

archive/issue_comments_045471.json:
```json
{
    "body": "Attachment [trac-5796-bitset-bugfix-len-function.patch](tarball://root/attachments/some-uuid/ticket5796/trac-5796-bitset-bugfix-len-function.patch) by jason created at 2009-04-20 17:54:49\n\napply on top of first patch.",
    "created_at": "2009-04-20T17:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45471",
    "user": "jason"
}
```

Attachment [trac-5796-bitset-bugfix-len-function.patch](tarball://root/attachments/some-uuid/ticket5796/trac-5796-bitset-bugfix-len-function.patch) by jason created at 2009-04-20 17:54:49

apply on top of first patch.



---

archive/issue_comments_045472.json:
```json
{
    "body": "Robert and Robert,\n\nJust pinging you (through trac email notifications) about this ticket.  If one of you could just look at the last patch (the bugfix-len one) and then positive-review the ticket, it'd be great.  In the patch, I fix one bug and add a bitset_len() function.  I put it on this ticket instead of opening a new ticket because of the bugfix.\n\nThanks, Jason",
    "created_at": "2009-04-24T19:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45472",
    "user": "jason"
}
```

Robert and Robert,

Just pinging you (through trac email notifications) about this ticket.  If one of you could just look at the last patch (the bugfix-len one) and then positive-review the ticket, it'd be great.  In the patch, I fix one bug and add a bitset_len() function.  I put it on this ticket instead of opening a new ticket because of the bugfix.

Thanks, Jason



---

archive/issue_comments_045473.json:
```json
{
    "body": "Moving to 3.4.2 now that it has a positive review to keep things cleaner.",
    "created_at": "2009-04-27T17:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45473",
    "user": "jason"
}
```

Moving to 3.4.2 now that it has a positive review to keep things cleaner.



---

archive/issue_comments_045474.json:
```json
{
    "body": "Unfortunately with both patches applied on sage.math I get one doctest failure in \n\n```\nsage -t -long devel/sage/sage/misc/misc_c.pyx\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T02:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45474",
    "user": "mabshoff"
}
```

Unfortunately with both patches applied on sage.math I get one doctest failure in 

```
sage -t -long devel/sage/sage/misc/misc_c.pyx
```


Cheers,

Michael



---

archive/issue_comments_045475.json:
```json
{
    "body": "apply on top of previous patches",
    "created_at": "2009-05-06T04:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45475",
    "user": "jason"
}
```

apply on top of previous patches



---

archive/issue_comments_045476.json:
```json
{
    "body": "Attachment [64-bit-doctest.patch](tarball://root/attachments/some-uuid/ticket5796/64-bit-doctest.patch) by jason created at 2009-05-06 04:12:44\n\nThe 64-bit-doctest.patch addresses the doctest failure on 64-bit machines.",
    "created_at": "2009-05-06T04:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45476",
    "user": "jason"
}
```

Attachment [64-bit-doctest.patch](tarball://root/attachments/some-uuid/ticket5796/64-bit-doctest.patch) by jason created at 2009-05-06 04:12:44

The 64-bit-doctest.patch addresses the doctest failure on 64-bit machines.



---

archive/issue_comments_045477.json:
```json
{
    "body": "Ok, positive review for 64-bit-doctest.patch resulting in a combined positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-06T04:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45477",
    "user": "mabshoff"
}
```

Ok, positive review for 64-bit-doctest.patch resulting in a combined positive review.

Cheers,

Michael



---

archive/issue_comments_045478.json:
```json
{
    "body": "Merged all three patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T11:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45478",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_045479.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T11:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5796#issuecomment-45479",
    "user": "mabshoff"
}
```

Resolution: fixed
