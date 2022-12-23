# Issue 4647: Disable dependency code cacheing in setup.py

Issue created by migration from https://trac.sagemath.org/ticket/4647

Original creator: mabshoff

Original creation time: 2008-11-29 00:04:28

Assignee: mabshoff

Unless we do the following -upgrade will likely break for a ton of people:

```
[3:57pm] craigcitro: wstein: so i'm only here for 3 seconds between xmas decorating, but i had a thought
[3:57pm] craigcitro: the dependency checking code in setup.py seems to be causing a lot of heartache
[3:57pm] craigcitro: so why don't we just not cache it? it still only takes like .6 seconds to build the whole dependency tree
[3:58pm] mabshoff: +1
[3:58pm] craigcitro: and if it build fresh every time, we'll avoid a ton of these issues
[3:58pm] craigcitro: and then when i have time to sit down and debug a bunch of these crazy situations, we can add it back in
[3:58pm] craigcitro: just comment out all the lines about pickle/unpickle/etc in setup.py
[4:00pm] ghtdak1 left the chat room. (Remote closed the connection)
[4:00pm] craigcitro: mabshoff: do you want to make a patch that does that for rc0?
[4:00pm] craigcitro: and see how it works out?
[4:00pm] craigcitro: i have to run right now -- getting the tree out of the car and putting up xmas lights. 
[4:00pm] mabshoff: I will put it on my list, but no promises.
```

One problem I see is that currently deleting the Cython cache triggers a full rebuild, so that need to be considered. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 06:08:48

Patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 06:08:48

Changing status from new to assigned.


---

Attachment

This patch covers #4645 as well as this ticket #4647. I did the minimally invasive version to make reenabling the caching code as simple as possible.

Once this patch is applied it survives:

 * a sage -b after deleting the Cython cache file
 * a sage -ba
 * a sage -b after applying the patch from #4206 - which caused us to disabled the caching for now.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 06:37:19

Two more data points:

 * disabling the caching adds a little less than a second to each "sage -b" run
 * reverting #4206 and then running sage -b again leads to a working Sage

Cheers,

Michael


---

Comment by craigcitro created at 2008-11-29 07:12:11

This looks good. I've added a second patch which cuts out one or two more lines (it was actually raising and catching an exception every time, which didn't need to happen), and adds comments pointing to this trac ticket, and trac #4651, which is the request to add caching back in. I also deleted a few leftover debugging print statements that were commented out, since they're no longer necessary.


---

Comment by mabshoff created at 2008-11-29 07:28:14

Positive review for the second patch. I left the exception structure in there since someone has to put them back in anyway, but I can live with the changes as is.

Cheers,

Michael


---

Attachment


---

Comment by craigcitro created at 2008-11-29 07:42:04

New patch, rebased against mabshoff's current `setup.py`. Applies fine to the copy I got from `/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/devel/sage-main` on sage.math.


---

Comment by mabshoff created at 2008-11-29 07:48:29

Resolution: fixed


---

Comment by mabshoff created at 2008-11-29 07:48:29

Merged in Sage 3.2.1.rc0
