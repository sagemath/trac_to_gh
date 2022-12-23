# Issue 3683: meataxe interface [with patch, not ready for review]

Issue created by migration from https://trac.sagemath.org/ticket/3683

Original creator: wdj

Original creation time: 2008-07-20 03:02:11

Assignee: joyner

CC:  wdj

This is a start for anyone interested in G-module decompositions using GAP's Meataxe implementations.


---

Comment by was created at 2008-07-20 20:15:14

Changing type from defect to enhancement.


---

Comment by wdj created at 2008-07-27 14:53:06

The patch 10104 contains all the changes, is based on 3.0.6.rc0, and passed sage -testall. It does not require 10092, so you should ignore that one. This patch adds module_composition_factors (an interface to GAP's meataxe implementation) and as_permutation_group (which returns an isomorphic PermutationGroup). The function module_composition_factors is needed for a research paper (in progress, joint with Amy Ksir and Darren Glass) which will probably be presented at the AMS national meeting in January 2009.


---

Comment by SimonKing created at 2008-08-02 21:19:57

Sorry that i was unable to look at this earlier. I'll wait for a patch based on a more recent sage-version before writing a full review.

Note, however, that patch 10104 doesn't do what it is supposed to do. 

The doc-string says:
Returns a _list of triples_ consisting of [base field, dimension, irreducibility], 
for each of the Meataxe composition factors modules.

But it only returns a list, as can be seen in the example from the doc-string:

```
sage: G.module_composition_factors() 
[Finite Field of size 7, 2, True] 
```


The reason is the line 896:

`L = L + [sage_eval(gap.eval("MCF.field")), eval(gap.eval("MCF.dimension")), sage_eval(gap.eval("MCF.IsIrreducible"))]`

which should be

`L = L + [This is the Trac macro *sage_eval* that was inherited from the migration called with arguments (gap.eval)](https://trac.sagemath.org/wiki/WikiMacros#sage_eval-macro)`


---

Comment by wdj created at 2008-08-03 02:56:48

This is a new patch based on sage 3.1.alpha0. Does not require other patches.


---

Attachment

The attached patch 10128 fixes the bug Simon found (thanks Simon!).


---

Comment by SimonKing created at 2008-08-12 13:38:58

The patch applies cleanly to SAGE Version 3.1.alpha0, Release Date: 2008-08-01. It seems to do what it is supposed to do, and the doc-tests for matrix_group.py pass.

Therefore, i recommend inclusion of the patch.

However, i would be glad about "stronger" examples.


 * Is there an example for `as_permutation_group` where the option `method="smaller"` actually yields a smaller result? Then it would be nice to include such example.


 * It would be nice to see an example where `module_composition_factors` yields a non-trivial decomposition. Such as here:

```
sage: F=GF(3);MS=MatrixSpace(F,4,4)
sage: M=MS(0)
sage: M[0,1]=1;M[1,2]=1;M[2,3]=1;M[3,0]=1
sage: G.module_composition_factors()

[[Finite Field of size 3, 1, True],
 [Finite Field of size 3, 1, True],
 [Finite Field of size 3, 2, True]]
```



---

Comment by wdj created at 2008-08-12 15:36:55

Definitely, I'm happy to add the example to the dcstring of module_composition_factors. Thanks for that.

Regarding a "better" "smaller" example, they are not so easy to find! I did find one though. The problem is that the generators are returned randomly. Michael Abshoff told me he doesn't like " # random output" comments in docstrings, so I added a the command current_randstate().set_seed_gap(). This does not work as I think it should, so I don't know the right way to proceed. I guess I'll post a patch that pases tests and worry about the random output stuff later.


---

Attachment

based on 3.1.alpha0


---

Comment by wdj created at 2008-08-12 18:37:44

This latest patch passes sage -testall and adds the examples suggested by the referee. Thanks Simon!


---

Comment by SimonKing created at 2008-08-13 11:15:08

Replying to [comment:7 wdj]:
> Regarding a "better" "smaller" example, they are not so easy to find! I did find one though. The problem is that the generators are returned randomly. Michael Abshoff told me he doesn't like " # random output" comments in docstrings, 

Cc to Michael Abshoff.

I understand that Gap uses a randomized algorithm when getting method="smaller". Hence, if one wants to show the full functionality of a method to the user (which i find important!), one can not avoid to have #random in the doc-tests.

Michael, what do you think?

I think: 
 * Starting with 3.1.alpha0, applying patch 10128 and then applying patch 10129 works.
 * The methods are useful.
 * The doc-string shows the functionality
 * The doc-tests pass
Hence i give it a positive review, but make it dependent on Michael's opinion on random doc-tests and/or on the idea to use current_randstate().set_seed_gap().


---

Comment by mabshoff created at 2008-08-13 15:52:52

David,

no need to CC me, I read every ticket anyway. 

About randomness: GAP should behave deterministically unless there is a third rng we do not know about. For now it seems fine to add the #random to the doctests, but you might want to raise the issue on sage-devel so that Carl Witty can give his input on the problem.

Cheers,

Michael


---

Comment by SimonKing created at 2008-08-13 16:15:00

Resolution: fixed


---

Comment by SimonKing created at 2008-08-13 16:15:00

Replying to [comment:10 mabshoff]:
> no need to CC me, I read every ticket anyway. 

Very impressive!

> ... For now it seems fine to add the #random to the doctests, ...

Then there is a positive review from my side and (if i am allowed to do so) I resolve the ticket as fixed (or is this only allowed to administrators?).


---

Comment by wdj created at 2008-08-13 20:48:11

based on sage-3.1.alpha0, as the others


---

Attachment

The last patch 10130 is a docstring change only. 

Following Michael Abshoff's suggestion, I emailed sage-devel and mentioned the problem I was having with the random comments. It seems I was using the current_randstate().set_seed_gap() command incorrectly for the situation. I added some set_random_seed(n) statements (where n is chosen in a specific way) and removed the "# random output" comments. I did multiple test passes and this seems to work each time now.

Hopefully, with 10130, everyone is okay with this now.


---

Comment by aginiewicz created at 2008-08-14 17:36:28

Changing status from closed to reopened.


---

Comment by aginiewicz created at 2008-08-14 17:36:28

Replying to [comment:11 SimonKing]:
> Then there is a positive review from my side and (if i am allowed to do so) I resolve the ticket as fixed (or is this only allowed to administrators?).

iirc it was that only things that get merged in are closed by admins? :)


---

Comment by aginiewicz created at 2008-08-14 17:36:28

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-08-14 19:16:10

Replying to [comment:13 aginiewicz]:
> Replying to [comment:11 SimonKing]:
> > Then there is a positive review from my side and (if i am allowed to do so) I resolve the ticket as fixed (or is this only allowed to administrators?).
> 
> iirc it was that only things that get merged in are closed by admins? :)

Yes, the release manager closes tickets once the patch/spkg has been merged. How else would be keep track of all the patches?

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-22 20:01:08

Resolution: fixed


---

Comment by mabshoff created at 2008-08-22 20:01:08

Merged 10128.patch, 10129.patch and 10130.patch in Sage 3.1.2.alpha0
