# Issue 2707: [with patch, needs review] clean and better document is_totally_real(), add is_totally_imaginary() to NumberField_generic

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-03-28 20:21:09

Assignee: was

CC:  ncalexan

Keywords: number field totally real imaginary




---

Attachment

This looks good, but I would like to see three things changed:

 * There's an extra 's' in the documentation for `is_totally_real` -- specifically on line 900. 

 * Personally, I'd like to see some newlines between `is_totally_imaginary`, `is_totally_complex`, and `complex_embeddings`.

 * I think that `is_totally_complex` should be given a full function definition, not just declared as `is_totaly_complex = is_totally_imaginary`. Here's the reason: as I understand it, if you inherit from `NumberField_generic`, and override `is_totally_imaginary`, this will *not* change `is_totally_complex` in the subclass. While this might not be deeply relevant in this case (since it's such a trivial function), I think this means it's a bad habit to be in in general, so we should avoid doing it. I know this means writing an extra docstring, which seems silly, but I think it's worth it.


---

Attachment


---

Comment by ncalexan created at 2008-03-28 20:43:01

Apply both patches.  Second addresses referee's comments.


---

Comment by mabshoff created at 2008-03-28 20:48:36

Merged both patches in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-28 20:48:36

Resolution: fixed
