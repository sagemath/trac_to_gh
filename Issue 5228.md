# Issue 5228: [with patch, needs review] make composite_fields and galois_closure return maps and preserve embeddings

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-02-10 18:20:38

Assignee: was

Keywords: number fields composite fields galois closure embedding coercion

The patches describe and doctest this better, but...

 * Extends composite_fields and galois_closure to return maps when asked

 * Uses the new coercion embedding to only return "coherent" compositions if embeddings are specified.


---

Attachment


---

Attachment

Apply `trac_5228-composite-fields.patch` and then `trac_5228-composite-fields-embeddings.patch`


---

Comment by mabshoff created at 2009-02-11 05:46:28

Assign it to 3.4.1 for now. If it is reviewed in time and passes doctests it will go into 3.3.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-02-11 09:18:41

Since someone beat me to #5231, I had to review this one...

Looks good.


---

Comment by mabshoff created at 2009-02-13 03:58:29

Merged both patches in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-13 03:58:29

Resolution: fixed
