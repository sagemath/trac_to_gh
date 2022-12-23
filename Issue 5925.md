# Issue 5925: [with patch, needs review] Improve speed of CombinatorialAlgebra.multiply()

Issue created by migration from https://trac.sagemath.org/ticket/5925

Original creator: jdc

Original creation time: 2009-04-29 01:04:40

Assignee: mhansen

CC:  sage-combinat

- Treat the case where _multiply_basis returns a monomial specially, to avoid creating lots of temporary dictionaries.  Speeds things up significantly.
- Use z_elt.get(m,ABRzero) to provide a default value.  Faster.
- Pull left_c * right_c out of inner loop.  Didn't time this, but it must be faster.
- Replace first use of BR with ABR so that BR isn't used twice in the same function for different rings.
- Add doctests so the four major cases are all tested locally.


---

Attachment

patch against 3.4


---

Comment by jdc created at 2009-04-29 01:09:02

I'm happy to rebase if needed.

Timing test on 2.2GHz Core2Duo running 32-bit Ubuntu 8.04:

Y=[[1,2,3,4],[5,6]]
time eY=e(Y)
time eY2=eY*eY

The second time is the one I'm looking to improve.

Before patch:

Time: CPU 0.56 s, Wall: 0.75 s
Time: CPU 1.93 s, Wall: 1.93 s

After patch:

Time: CPU 0.56 s, Wall: 0.75 s
Time: CPU 1.61 s, Wall: 1.61 s

I tested each change separately, and each showed an improvement in the
second time.


---

Comment by mabshoff created at 2009-04-30 07:11:45

Hi Dan,

two things:

 * make sure to assign a milestone to each ticket when you open it. In most cases it should be the next release.
 * please add yourself to the account listing at http://trac.sagemath.org/sage_trac/wiki

Cheers,

Michael


---

Comment by mhansen created at 2009-06-04 19:23:05

Resolution: fixed


---

Comment by mhansen created at 2009-06-04 19:23:05

Looks good.

Merged in 4.0.1.rc1.


---

Comment by mvngu created at 2009-06-07 06:47:03

Replying to [comment:1 jdc]:
> Timing test on 2.2GHz Core2Duo running 32-bit Ubuntu 8.04:
> 
> Y=[[1,2,3,4],[5,6]]
> time eY=e(Y)
> time eY2=eY*eY


Hi Dan. I'm showcasing the feature of this ticket in the release tour. The above code doesn't look sensible to me, since `time eY=e(Y)` results in a `ValueError` under Sage 4.0 and 4.0.1. Can you post sample code to illustrate the timing improvement introduced by the patch? The code should illustrate this both before and after applying the patch.


---

Comment by jdc created at 2009-06-08 15:19:53

Replying to [comment:7 mvngu]:
> Replying to [comment:1 jdc]:
> > Timing test on 2.2GHz Core2Duo running 32-bit Ubuntu 8.04:


```
Y=[[1,2,3,4],[5,6]]
time eY=e(Y)
time eY2=eY*eY
```


> Hi Dan. I'm showcasing the feature of this ticket in the release tour. The above code doesn't look sensible to me, since `time eY=e(Y)` results in a `ValueError` under Sage 4.0 and 4.0.1. Can you post sample code to illustrate the timing improvement introduced by the patch? The code should illustrate this both before and after applying the patch.

Did you try doing:


```
from sage.combinat.symmetric_group_algebra import e
```


before running the above code?  I don't have sage 4.0 or higher installed yet, and I'm about to be offline for about a month, so I'm not going to be able to look into this further for a while.


---

Comment by nthiery created at 2009-06-09 22:50:15

Why the hell was sage-combinat not in CC to that one?

This change should have gone through the Sage-Combinat server to merge with the changes there.
Besides CombinatorialAlgebra is deprecated.

Now I get one more conflict to handle.

(anyone complaining about our changes in Sage-Combinat not going into Sage quickly enough is welcome to give a hand
on the review process for #5891).


---

Comment by craigcitro created at 2009-06-09 23:48:30

Hi Nicolas,

> Why the hell was sage-combinat not in CC to that one?
> 
> This change should have gone through the Sage-Combinat server to merge with the changes there.
> Besides CombinatorialAlgebra is deprecated.
> 

I think Dan (djc) is new to Sage, and I don't know that there's any information anywhere saying that all changes to combinatorics must pass through sage-combinat, or that this is even the policy. I agree it's frustrating, but I don't think Dan is at fault at all. This was probably an overly harsh reply ... so Dan, please don't take it personally, since I'm sure Nicolas didn't intend that. `:)`

On a related note, I agree that it would be nice if all combinatorics trac tickets got automatically cc'd to sage-combinat, or a separate sage-combinat-trac mailing list. This ticket was set to component: combinatorics; Mike seems to be the owner for that component, but would it be better if we set it to an account whose email address was a sage-combinat mailing list? Then the list would automatically receive notifications of any new tickets with component combinatorics (unless someone set the owner on creation). A better choice would be to set up an email account that was subscribed to sage-trac (which is *every* trac email) and forwarded along anything that had the word "combinatorics". This would be pretty trivial to do with a dedicated gmail account, though there's probably an even more lightweight solution out there ...


---

Comment by nthiery created at 2009-06-10 03:16:04

Replying to [comment:10 craigcitro]:
> Hi Nicolas,
> I think Dan (djc) is new to Sage, and I don't know that there's any information anywhere saying that all changes to combinatorics must pass through sage-combinat, or that this is even the policy. I agree it's frustrating, but I don't think Dan is at fault at all. This was probably an overly harsh reply ... so Dan, please don't take it personally, since I'm sure Nicolas didn't intend that. `:)`

Yes, thanks Craig for pointing this out. 

Sorry Dan: My comment was absolutely not targeting you. I definitely appreciate your contribution, and I very much hope to hear from you soon about other parts of the combinat code!

On the other hand, it's not like noone who handled this patch was aware of Sage-Combinat and CombinatorialAlgebra.
Well, the point is not to find a culprit. But, with the current pile of patches, the Sage-Combinat server is getting really hard to maintain. So please all be careful (or step to up to maintain it). Thanks!

> On a related note, I agree that it would be nice if all combinatorics trac tickets got automatically cc'd to sage-combinat, or a separate sage-combinat-trac mailing list. This ticket was set to component: combinatorics; Mike seems to be the owner for that component, but would it be better if we set it to an account whose email address was a sage-combinat mailing list? Then the list would automatically receive notifications of any new tickets with component combinatorics (unless someone set the owner on creation). A better choice would be to set up an email account that was subscribed to sage-trac (which is *every* trac email) and forwarded along anything that had the word "combinatorics". This would be pretty trivial to do with a dedicated gmail account, though there's probably an even more lightweight solution out there ...

Yup. There readily is a sage-combinat account, which is forwarded to sage-combinat-commits. Yes, it would be great if any change to the combinatorics component was forwarded there.

Cheers
