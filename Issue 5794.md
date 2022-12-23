# Issue 5794: [with patch, needs review] G2 branching rules

Issue created by migration from https://trac.sagemath.org/ticket/5794

Original creator: bump

Original creation time: 2009-04-16 01:16:30

Assignee: tbd

CC:  sage-combinat

This patch implements branching rules for the following inclusions
of Lie groups: 


```
A1 in G2 (along short root) 
A2 in G2
G2 in B3
G2 in D4
```


It goes on top of the following patches:


```
trac_5721-a.patch
trac_5721-b.patch
trac_5751.patch
```



---

Comment by bump created at 2009-04-16 04:59:41

Changing assignee from tbd to joyner.


---

Comment by bump created at 2009-04-16 04:59:41

Changing component from algebra to group_theory.


---

Comment by bump created at 2009-04-16 04:59:41

Changing keywords from "" to "lie groups".


---

Comment by bump created at 2009-04-18 13:09:12

The last change indicates that I changed the owner from tbd to joyner. I don't
remember doing that, and I don't see how I could have done it accidentally.
Maybe someone else changed the owner, presumably wdj or mabshoff, but then
trac shouldn't show that I did. I am puzzled by this.

Here are some comments about the G2=>A1 Levi branching rule. There is a
branching rule G2=>A1xA1 (rule = "extended"). This is not implemented yet.
Currently Weyl character rings are broke for reducible root systems. (I have a
patch for that but it is not posted on trac yet.) I intend to implement branching
to reducible root systems but first I want to do a few exceptional branching
rules first before tackling the *many* cases of branching to reducible root systems.

So G2=>A1xA1 will come in a later patch but it is relevant here so I will discuss it.

In the branching rule G2=>A1xA1, the second A1 is almost but not
quite the A1 in the G2=>A1 Levi branching rule. (The short root A1.) So it might
seem that one should implement G2=>A1xA1 and then you would get the G2=>A1
(rule = "levi") branching rule. However this is not quite true. The A1 in the G2=>A1
branching rule is GL(2) and the A1 in A1xA1 is SL(2).


---

Comment by bump created at 2009-04-18 13:56:14

I uploaded a second patch trac_5794-f4.patch which goes on top of
the first. It implements branching rules F4=>B3 (levi), F4=>C3 (levi)
and F4=>B4 (extended).

There is another extended rule F4=>C3xA1 (not implemented yet,
but hopefully to be implemented later).

In contrast with G2, for F4, both Levi branching rules are redundant
since the Levi subgroups are not maximal. They factor through branching
rules F4=>B4=>B3 and F4=>C3xA1=>C3. However I implemented them
for convenience. You can check directly that
F4(x).branch(B3,rule="levi") and
F4(x).branch(B4,rule="extended").branch(B3,rule="levi") return the
same thing for x in F4.fundamental_weights().

I compared the output for these rules against those that I could find in a book, 
Patera and Sankoff, Branching rules for representations of simple Lie algebras.


---

Comment by mabshoff created at 2009-04-18 16:49:17

Hi Dan,

the change in ownership happend because you changed the component to "group_thoery". For every ticket you work on and post patches you should accept it (see the bottom left), that way ownership stays with you.

Cheers,

Michael


---

Comment by bump created at 2009-04-18 19:18:10

Changing status from new to assigned.


---

Comment by bump created at 2009-04-18 19:18:10

Changing assignee from joyner to bump.


---

Attachment


---

Comment by bump created at 2009-05-06 20:21:36

I'm taking the liberty of changing the milestone to 4.0 in case there
is a chance of getting this merged. It is quite a substantial enhancement.


---

Comment by bump created at 2009-05-07 04:28:09

Here are some tests supplementing those implemented in the doctests:

http://sporadic.stanford.edu/bump/branch.sage


---

Attachment


---

Comment by bump created at 2009-05-16 22:26:44

Is it possible to remove the first two patches:


```
trac_5794.patch
trac_5794-f4.patch
```


They are superceded by the other patches. I am going to be adding some
more patches to this series, and I think it would be less confusing if the
first two patches are removed. I don't think I can do this without help
from admin.

Dan


---

Attachment


---

Attachment


---

Comment by mvngu created at 2009-06-08 03:54:29

Since I don't know the order in which patches should be applied, let alone which one to apply, I skimmed through all 4 patches. Most docstrings adhere to the ReST format, but some don't. I'm merely enforcing proper ReST formatting, not reviewing the patches.


---

Comment by bump created at 2009-06-11 05:34:59

Apply all four patches in order.


```
trac_5794-revised.patch
trac_5794-continued.patch
trac_5794-exceptional.patch
trac_5794-more-exceptional.patch
```


> Most docstrings adhere to the ReST format, but some don't.

If you find nonconforming docstrings, please cite them by line number.
There is a lot of doc in these patches.


---

Comment by mvngu created at 2009-06-19 21:52:02

Replying to [comment:19 bump]:
> Apply all four patches in order.
> 
> {{{
> trac_5794-revised.patch
> trac_5794-continued.patch
> trac_5794-exceptional.patch
> trac_5794-more-exceptional.patch
> }}}
>
> > Most docstrings adhere to the ReST format, but some don't.
> 
> If you find nonconforming docstrings, please cite them by line number.
> There is a lot of doc in these patches.
Note that I'm not qualified to review the mathematical content of the patch. However, I would like to point out that the following patches and line numbers don't conform to ReST formatting:



In `trac_5794-revised.patch`:
 * Patching against the file `sage/combinat/root_system/type_A.py`, the examples section starting from line 117.
 * Patching against the file `sage/combinat/root_system/type_reducible.py`, the examples section starting from line 249.
 * Patching against the file `sage/combinat/root_system/weyl_characters.py`, the examples section starting from line 458, the example starting from line 1202, the examples section starting from line 1211, the example starting from line 1227, the examples section starting from line 1235, the example starting from line 1280, the example section starting from line 1299.
In `trac_5794-continued.patch`:
 * Patching against the file `sage/combinat/root_system/weyl_characters.py`, the example starting from line 1431, the example starting from line 1443, the example starting from line 1452, the example starting from line 1831, the example starting from line 1842.
The following files are not in the reference manual. You might want to consider exposing their features by adding them to the reference manual:
 1. `sage/combinat/root_system/type_A.py`
 1. `sage/combinat/root_system/type_reducible.py`


---

Attachment

Nicolas Thiery wrote the patch `trac_5794-reviewer-nt.patch`.
It is in the combinat patch queue. I took the liberty of uploading
it.

It addresses at least some of the ReST complaints.

I am changing the title back to [with patch, needs review] since
apart from the issue of the ReST formatting, the patches still
needs a technical review. The following remark is addressed
to whoever does the technical review. (Brant Jones was suggested.)

The patches as posted differ slightly from the versions in the combinat queue.
The reason for the difference is that the meaning of the is_reducible
Cartan type attribute is changed by #4326. After #4326 (which preceed
these patches in the queue) the root system D2 is not reducible. See

http://groups.google.com/group/sage-combinat-devel/msg/8b3569b4e2f2b7e1?hl=en

and thread for discussion. (Note: the `patch cartan_type_temporary-1.patch` 
mentioned in that message was qfolded shortly afterwards.)


---

Comment by sage-combinat created at 2009-07-23 14:40:58

Patch review: trac_5794

The patch author is a widely acknowledged expert in the area, having written a textbook which includes a discussion of the root systems and branching rules implemented here.  Although we did not check all of the details of the algorithms, the root system code has been used by the reviewer to implement the alcove path model for crystals of Lenart and Postnikov, and the branching code has computed some verified data in type E_6.  This patch implements useful mathematics and the extensive documentation includes references to relevant mathematical literature.

There are currently two warnings for the reference manual (sage -docbuild reference html); these require help from Sage developers to be fixed.  The Sage library test passes, and all methods have doctests which pass.

-- Brant Jones


---

Comment by mvngu created at 2009-07-23 14:51:48

This depends on #4326.


---

Attachment

Annotates the long tests with their time, and disables one which took 160s.


---

Comment by nthiery created at 2009-11-19 11:25:33

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2009-11-19 11:25:43

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2009-11-19 15:56:13

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2009-11-19 15:56:13

Positive review from Dan on sage-combinat-devel


---

Comment by mhansen created at 2009-11-19 17:02:33

Resolution: fixed


---

Comment by AlexGhitza created at 2009-12-14 02:06:09

Did `trac_5794-long-time-nt.patch` actually get merged?  I don't see these changes in sage-4.3.rc0, and therefore running long doctests on weyl_characters.py still takes forever:


```
[ghitza@sage root_system]$ sd -t -long weyl_characters.py 
sage -t -long "devel/sage-main/sage/combinat/root_system/weyl_characters.py"
         [242.2 s]
```



---

Comment by mhansen created at 2009-12-14 16:12:24

Thanks for picking that up.  I've merged that one patch in 4.3.rc1.


---

Comment by jdemeyer created at 2013-10-17 07:33:52

I seems the patches here on Trac are not the ones which were actually merged 4 years ago, which was discovered in #15279.
