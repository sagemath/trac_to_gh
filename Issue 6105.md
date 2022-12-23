# Issue 6105: [with patch, need review] Additions and changes in Group Algebras

Issue created by migration from https://trac.sagemath.org/ticket/6105

Original creator: jlefebvre

Original creation time: 2009-05-21 05:08:16

Assignee: tbd

Keywords: Group Algebra

Added helper functions to better exchange character information between gap and Sage and then use those to build a system of idempotent for any group algebra defined over a finite group. Also, made small fixes in the group algebra.


---

Attachment

Part 2


---

Comment by mvngu created at 2009-05-21 06:07:09

Hi Jerome. Are there any special reasons why you use camel case for the following functions?
 * `goodFor`
 * `inCon`
 * `complexGtoS`
 * `charValue`
 * `systemOfIdempotent`
 * `Augmentation`
I'm just asking, since I'm not at Sage Days 15 so I have no idea why you did so. But I trust that you've read the coding conventions at



http://www.sagemath.org/doc/developer/conventions.html


---

Attachment

Fixed to follow coding convention


---

Comment by jlefebvre created at 2009-05-21 06:29:51

Hi Minh, there was no particular reason. Thanks for pointing out the coding convention to me.


---

Comment by jlefebvre created at 2009-05-21 07:33:25

Hey again, I noticed some bugs in my conversion from gap to Sage. I'm going to try to fix it as soon as  I can.


---

Attachment

Fix to gap to complex conversion


---

Attachment

A new patch against sage 4.0.1


---

Comment by davidloeffler created at 2009-06-10 10:10:26

Here's a silly thing: this patch has never appeared in the list of patches needing review, because that list does a text search in the summary field for "needs review", and "need review" doesn't show up.


---

Comment by davidloeffler created at 2009-06-14 11:48:13

I haven't tried installing this, but here are some comments based on browsing the code. 

It looks like this is excellent functionality, but there are some things I'm not very happy with. 

(1) Brutally converting all finite groups into permutation groups will mean we can't generally create an element of the group algebra from an element of the group, which means that most of the basic arithmetic operations that I originally wrote the class for won't work any more. Please don't do this; rather, add more functionality to the basic Group class, or (if absolutely necessary) make GroupAlgebra store both the original group and its permutation form (and the mapping between them).

(2) Many of these docstrings are somewhat confusing; I can't for the life of me work out what the docstring for "good_for" is trying to say -- some of it seems to be about the function at hand, some about another unnamed function, and nowhere is it defined what the function actually does.

(3) Lots of these functions need more testing. There are some obvious typos, e.g. in is_noetherian:  

```
if self.group().is_polycyclic and self.base_ring().is_field():
```

should read

```
if self.group().is_polycyclic() and self.base_ring().is_field():
```


When there are lots of different cases handled in a function, it's good to have a test for each case -- the aim is that "sage -testall" should test every single line of code in the Sage library, and much of this code simply won't get hit. Then typos like this come out in the wash.

(4) It would be good if the GroupAlgebra class could be incorporated into the reference manual (by adding a line to `sage/doc/en/reference/algebras.rst`). To do this will require lots of formatting changes to the docstrings (e.g. example blocks must look like

```
EXAMPLE::

    sage: some code
```

with two colons and a blank line). This is somewhat orthogonal to your patch and is actually my fault -- when I wrote the group algebra class, I forgot to add it to the reference manual, so it never got updated when we changed to a new and better reference manual compilation system -- but it seems a shame to make the problem worse by adding many new functions with new docstrings that are not ReSTified.

Much of this is cosmetic, but (1) is a big issue -- I don't think we can consider merging this into Sage if it's going to break creating elements of group algebras for most of our finite group classes. So I'm changing this back to "needs work"; sorry.


---

Comment by jlefebvre created at 2009-06-15 04:17:28

Thanks for the feed back!
I've started to attack (1), it looks like I needed to convert group to their permutation group representation to deal with AbelianGroup class. I couldn't fix some of the issues I ran into, so created tracs about them; 6291, 6292, 6293.


---

Comment by davidloeffler created at 2009-06-15 09:02:04

Replying to [comment:6 jlefebvre]:
> it looks like I needed to convert group to their permutation group representation to deal with AbelianGroup class.

I would be *extremely* surprised if this were the best way of doing it. 

By the way, there are some major changes pending to the abelian group implementation -- the plan is to implement them directly in Sage via the machinery we already have for linear algebra over ZZ, using William Stein's work at ticket #5882, rather than relying on Gap. (This is for several reasons, one of which being the speed penalty of communicating with Gap via the pexpect interface.)

David


---

Comment by was created at 2009-06-15 12:54:36

> By the way, there are some major changes pending to the abelian group implementation --
>  the plan is to implement them directly in Sage via the machinery we already have for 
> linear algebra over ZZ, using William Stein's work at ticket #5882, 

And amazingly, I will have time to work on this soon! (I claim.)
