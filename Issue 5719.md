# Issue 5719: [with patch, needs review] Corrected a bad deprecation message.

Issue created by migration from https://trac.sagemath.org/ticket/5719

Original creator: hivert

Original creation time: 2009-04-08 21:20:05

Assignee: hivert

CC:  sage-combinat

Keywords: Warning message

Currenctly when calling count on a combinatorial class the deprecation message is:
   
   The usage of iterator for combinatorial classes is deprecated. Please use the class itself

Whereas it should be

   The usage of count for combinatorial classes is deprecated. Please use cardinality

Corrected my patch. Apologies for this mistake. Thanks to Daniel Bump for reporting it. 

Florent


---

Attachment


---

Comment by mabshoff created at 2009-04-08 21:22:24

Looks good to me, I am doctesting this now. Positive review pending passing doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-08 21:37:17

Merged in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-08 21:37:17

Resolution: fixed
