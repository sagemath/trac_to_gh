# Issue 5002: CrystalOfTableaux call method breaks on legitimate data

Issue created by migration from https://trac.sagemath.org/ticket/5002

Original creator: bump

Original creation time: 2009-01-17 17:03:36

Assignee: mhansen

CC:  sage-combinat


```
sage: C = CrystalOfTableaux(['B',2],shape=[3]) 
sage: C(rows=[[1,1,0]])
```


raises an exception though this is a legitimate B2 tableaux. This was
analyzed by Anne Schilling and others in this thread:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/cb02f961c41947e2?hl=en



---

Comment by aschilling created at 2009-04-02 22:02:11

Changing assignee from mhansen to aschilling.


---

Comment by aschilling created at 2009-04-02 22:02:11

Changing status from new to assigned.


---

Attachment


---

Comment by aschilling created at 2009-04-06 20:30:11

The patch depends on 4549 and 5308.


---

Comment by aschilling created at 2009-04-07 19:58:30

* fixes the bug when legitimate tableau of type B is entered
* allows to enter several shapes for tableaux (which will be
essential for the Kirillov-Reshetikhin crystals later)
* fixes a small bug in partitions when adding a box to the
empty partition 
* fixes errors in comparison of the elements in crystal of letters


---

Comment by bump created at 2009-04-08 15:15:21

This patch fixes three bugs.

First, there is the bug originally reported in this ticket.
Second, there is the bug described at
http://groups.google.com/group/sage-combinat-devel/msg/bce932c675b8b04a?hl=en
Third, it fixes an exception on 
`Partition([]).outside_corners()`.

In addition there are a lot of documentation improvements.

The new class CrystalOfWords needs a docstring. Otherwise I found no problems.

The patch does not change the effect of `sage --testall`.

The patch applies cleanly on sage-3.4.1.rc1.

Patch summary:


```
Adds index_set as a lazy_attribute method in class Crystal.
Removes class AffineCrystal which was prematurely implemented
Replaces the cmp_elements method => lt_elements in ClassicalCrystalOfLetters.
Implements __ne__, __lt__, __ge__ methods in class Letter.
Properly indents docstrings for TensorProductOfCrystals.
New class CrystalOfWords.
FullTensorProductOfCrystals inherits from CrystalOfWords.
call method of FullTensorProductOfCrystals is taken down.
CrystalOfTableaux inherits from CrystalOfWords.
Docstring revision for CrystalOfTableaux.
CrystalOfTableaux __init__ method allows multiple shapes.
CrystalOfTableaux gets new methods cartan_type and module_generator
CrystalOfTableauxElement __init__ revisions
```



---

Comment by aschilling created at 2009-04-08 17:24:23

Added docstring to CrystalOfWords as requested by Dan Bump.


---

Comment by mabshoff created at 2009-04-08 19:11:15

Hi, 

after some discussion about lazy attributed at SD 14 with Nicolas the consensus at least from the non-combinat developers was that lazy attributes should be avoided for public API data structures. If you want to access the index_set of a crystal we see no reason for the inconsistency *A.data_set* while everywhere else in Sage it would be *A.data_set()*. Caching can be done in some other ways.


Cheers,

Michael


---

Comment by was created at 2009-04-08 19:15:07

Replying to [comment:8 mabshoff]:
> Hi, 
> 
> after some discussion about lazy attributed at SD 14 with 
> Nicolas the consensus at least from the non-combinat 
> developers was that lazy attributes should be avoided for 
> public API data structures. If you want to access the 
> index_set of a crystal we see no reason for the 
> inconsistency *A.data_set* while everywhere else 
> in Sage it would be *A.data_set()*. Caching can be done 
> in some other ways.

+10   I very strongly agree with this.  The point isn't to argue about whether lazy attributes are good or bad, but that using them is inconsistent with hundreds of thousands of lines of existing Sage code, and we're definitely not going to change all that code.  For consistency, do not use them in the Sage library for "user facing" code.


---

Comment by nthiery created at 2009-04-08 19:35:54

Peace. The lazy_attribute here is just a temporary workaround. Anne precisely did send an e-mail
to the mailing list 2 days ago asking for confirmation for changing it systematically to a method
in all the crystal library. This will come as a subsequent patch.

Refactoring all the crap in the combinatorics code will take a while. No need to jump on every occasion to repeat the same arguments. We have heard them, and fully taken points for them.

That being said, I still think that lazy attributes have their role to play in some well localized places in the user interface. I will run a complete discussion about this when time is ready for it. And the final code will follow whatever consensus emerges.


---

Comment by bump created at 2009-04-08 23:35:25

Can the patch be merged (and this issue sorted out later) or does it need to be revised to avoid lazy_attributes?

I suppose this is Michael's call, so this question is addressed mainly to him.


---

Comment by mabshoff created at 2009-04-09 01:25:01

Replying to [comment:11 bump]:
> Can the patch be merged (and this issue sorted out later) or does it need to be revised to avoid lazy_attributes?
> 
> I suppose this is Michael's call, so this question is addressed mainly to him.

I am reluctant to merge any large patch that is not on my blocker list at this point in general, but I would greatly prefer if the lazy_attribute issue in this patch was fixed. The main reason is that otherwise some of the API in crystals will be different in 3.4.1 until the fix is merged and there is no clean way to handle this. I think since this is a combinat patch, i.e. no Cython, it is relatively low risk. But we are at the moment sitting around trying to get all blockers resolved and put out 3.4.1.rc2, so if the fix appears it should appear quickly. 

`@`Nicolas: I did not see the patch by Anne, but I will look it up.

Cheers,

Michael


---

Comment by aschilling created at 2009-04-09 07:03:07

removed reference to lazy attribute


---

Attachment

I removed the reference to lazy attribute. I hope it is now ok to be integrated.
In the process I also had to touch fast_crystals.py and spins.py.


---

Comment by mabshoff created at 2009-04-09 07:21:11

Merged crystal-5002-track.patch only in Sage 3.4.1.rc2. 

I did reread the changes Anne made and they look good to me. Doctests do pass, too.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 07:22:16

Merged crystal-5002-track.patch only in Sage 3.4.1.rc2.

I did reread the changes Anne made and they look good to me. Doctests do pass, too. And this time I closed the ticket, too :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 07:22:16

Resolution: fixed
