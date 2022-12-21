# Issue 7541: LexBFS and is_chordal

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-11-27 13:01:17

Assignee: rlm

Lex BFS is a variant of the breadth first search. It is used to detect whether a Graph is chordal. Both algorithms are described there :

http://en.wikipedia.org/wiki/Lexicographic_breadth-first_search

Nathann


---

Comment by ncohen created at 2009-11-29 13:03:58

Changing status from new to needs_review.


---

Comment by rlm created at 2009-12-15 17:42:58

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2009-12-15 17:42:58

Looks good!


---

Comment by rlm created at 2009-12-15 17:45:03

changed successor to neighbor_out


---

Comment by mhansen created at 2009-12-19 21:26:33

Resolution: fixed


---

Attachment
