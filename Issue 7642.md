# Issue 7642: Add an implementation of LCA to sage.combinat.words.suffix_trees

Issue created by migration from https://trac.sagemath.org/ticket/7642

Original creator: abergeron

Original creation time: 2009-12-09 18:43:15

Assignee: sage-combinat

Keywords: lca suffix_tree

I have implemented the linear time preprocessing, constant-time queries algorithm for the lowest common ancestor (LCA) in the context of the suffix trees for words.

The only thing I'm not very sure about is where to place the bit manipulation functions.


---

Attachment


---

Comment by abergeron created at 2009-12-09 18:46:21

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-02-07 08:57:37

Several comments about this patch :

 * leftmost_one naturally fails on 0, as it computes a logarithm... Shouldn't this be documented, or the exception handled inside the function, to return something like -1 ?

 * bits_left_of seems to me a bit vague for what the function does... What would you think of leftmost_bits ? The docstring could be more explicit, like : substracts from x the leftmost i bits in its "base-2 expression" (I do not know how this is said in english) :-)
   Same remark for bits_right_of

 * I have no idea of what a MSB is, and could find its definition nowhere. Could you at least write its full name ? ( samek remark for lca, which appears very often in the docstrings )

 * I think you should define _ldata inside of the __init__ function

 * I am not a big fan of your algorithm = best argument in LCA. The user is bound to know if the tree has been preprocessed, as he has to call it himself. I think it is just a sourc e of silent failures to use the "fast" algorithm.

What you are doing in this patch is out of my field, so my remarks could just come from this. I thought it would just be an algorithm on trees, but many details not being explicit in the docstrings, it is difficult for me to fill the holes... :-)

Nathann


---

Comment by drkirkby created at 2010-02-21 23:42:42

Has this been checked on Solaris?

There's general information about building on Solaris at

 http://wiki.sagemath.org/solaris

Information specifically for 't2' at

 http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave


---

Comment by drkirkby created at 2010-02-21 23:42:42

Remove assignee sage-combinat.


---

Comment by ncohen created at 2010-05-09 16:48:40

Changing status from needs_review to needs_work.
