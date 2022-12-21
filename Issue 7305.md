# Issue 7305: Implement the Higman-Sims graph

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-10-26 04:14:49

Assignee: rlm

CC:  ncohen

Add the Higman-Sims graph to the graph generators collection.


---

Attachment


---

Comment by rbeezer created at 2009-10-26 04:18:36

Changing status from new to needs_review.


---

Comment by ncohen created at 2009-11-07 16:33:20

Two remarks :
    * In my memory there are two different lists of graphs in the file graph_generator.py, and you only added yours once
    * I would have written 
      {{{
      relabel - default: True.
      }}}
      
      as 

      {{{
      ``relabel`` - default: ``True``.
      }}}


---

Comment by ncohen created at 2009-11-07 16:33:20

Changing status from needs_review to needs_work.


---

Attachment

Hi Nathann,

Nice catch, on both counts.  Thanks for the review.

The "_2" patch is self-contained (ie apply just the single revised patch on a fresh install) and addresses both your comments.

Rob


---

Comment by rbeezer created at 2009-11-08 22:21:14

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-11-09 16:38:17

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2009-11-09 16:38:17

Then I can swear I never saw any cleaner patch.... Thanks for this addition ! :-)

Nathann


---

Comment by mhansen created at 2009-11-12 08:14:38

Resolution: fixed
