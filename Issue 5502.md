# Issue 5502: implement ascii art output for Dynkin diagrams

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-03-12 19:26:49

Assignee: mhansen

CC:  sage-combinat

Keywords: dynkin diagram ascii art lie

Dan Bump requested this in his Sage Days 14 talk: have ascii art output a la LiE for Dynkin diagrams (see interfaces/lie.py for some examples of usage).



---

Comment by bump created at 2009-04-15 13:58:29

I uploaded trac_5502.patch for this. It applies to sage-3.4.1.rc2 and there are no errors in `sage/combinat/rootsystems/*.py.`.

I have not tested it against the combinat patchseries because at the moment hg qpush -a fails in sage-combinat.

After the patch, the `__repr__` method of `class DynkinDiagram` returns ascii art for the classical Cartan Types.

A natural extension would be to give the extended Dynkin diagram for the untwisted affine types.


---

Comment by wdj created at 2009-04-15 15:10:50

Is this related to http://trac.sagemath.org/sage_trac/ticket/2023 ?


---

Comment by nthiery created at 2009-04-15 16:21:52

Replying to [comment:4 wdj]:
> Is this related to http://trac.sagemath.org/sage_trac/ticket/2023 ?

That's indeed the ascii art version of 2023. Thanks for the pointer.


---

Comment by bump created at 2009-04-15 20:43:17

I think the spirit of this patch is the same as #2023.

The idea of this patch is just that if the Cartan type is that
of a classical Lie algebra, you should be able to _somehow_
access it's Dynkin diagram. The solution here is making it part of the string
returned by the `__repr__` method of the class.

We follow the Bourbaki conventions, which is the same as the
programmed-in Cartan types. These diagrams are identical to
those produced by LiE, so you can have them already if you
install that optional package.


```
sage: CartanType("E6").dynkin_diagram()

        O 2
        |
        |
O---O---O---O---O
1   3   4   5   6   
E6
```


You want this if you need to be reminded of what labeling
convention is used. If the Cartan type is not recognized, we get the
old behavior. Thus:


```
sage: CartanType(['E',6,1]).dynkin_diagram()
Dynkin diagram of type ['E', 6, 1]
```


It might be more convenient if untwisted affine types gave the
extended Dynkin diagram, thus:


```
sage: CartanType(['E',6,1]).dynkin_diagram()
        O 0 
        |
        |
        O 2
        |
        |
O---O---O---O---O
1   3   4   5   6
E6~
```


Beyond that, one might implement Dynkin diagrams for twisted
affine types, but that seems less urgent.


---

Comment by bump created at 2009-04-23 15:21:44

The file trac_5502.2.patch add extended Dynkin diagrams as Dynkin diagrams of untwisted affine Cartan types.

Anne Schilling requests twisted affine types, but this is not done.


---

Attachment

The patch `trac_5502-revised.patch` corrects some problems and supercedes
the previous patches.


---

Comment by bump created at 2009-05-06 22:30:08

I changed the milestone to 4.0 in hopes this can be merged.


---

Comment by aschilling created at 2009-05-08 01:41:56

The patch implements ascii art for all finite and untwisted Cartan types,
which is very useful for visual clues about the numbering of the Dynkin nodes.

All doctests pass.


---

Comment by mabshoff created at 2009-05-11 09:06:00

There are two new functions without doctests:

 * extended_dynkin_diagram_ascii_art
 * dynkin_diagram_ascii_art

I know they are tested elsewhere, but the 100% rule still applies. Once the doctests have been added the positive review can be reinstated assuming the doctests in the file modified actually pass ;)

Cheers,

Michael


---

Attachment

The patch trac_5502-doc.patch goes on top of trac_5502-revised.patch.

It adds doctests to the two ascii art functions.


---

Comment by mabshoff created at 2009-05-12 05:29:16

Positive review overall.

Dan: Please remember to change the summary back once you updated the patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 06:04:06

Resolution: fixed


---

Comment by mabshoff created at 2009-05-12 06:04:06

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael
