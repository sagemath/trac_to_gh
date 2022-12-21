# Issue 4047: [with patch, needs review] automorphism groups/canonical labels for hypergraphs

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-09-03 17:40:41

Assignee: rlm

Also known as nonlinear binary codes. This patch sets up the framework needed for matrix automorphism groups, and automorphism groups of nonbinary linear codes.


---

Comment by wdj created at 2008-09-03 21:38:23

This seems like an awesome patch. It applies to 3.1.2.alpha4 fine and passes sage -testall.
I don't understand the cython code, though it appears to be well-documented. However, I have a few general questions anyway:-)

1. Where is there written a "big picture" explanation of what the general idea is and where it is going. I know rlm-blog has some details but it seems a lot of details (even in vague global terms) are missing from that, so it would be great to see how this fits into the grand scheme. 

2. It seems (based on my vague understanding) that the automorphism group function could be replaced by a more general equivalence function, which returns the group of equivalences if two "non-linear codes" are equivalent (and "False" otherwise, or something). Is this true?

3. What exactly is a hypergraph and how does it correspond to a non-linear code? (And by non-linear I assume you mean a subset of GF(2)^n which is not necessarily closed under the usual coordinate-wise addition.)

Hope these comments help. If not feel free to ignore them!


---

Comment by rlm created at 2008-09-03 23:12:20

> 1. Where is there written a "big picture" explanation of what the general idea is and where it is going. I know rlm-blog has some details but it seems a lot of details (even in vague global terms) are missing from that, so it would be great to see how this fits into the grand scheme. 

Check the top of the file sage/groups/perm_gps/partn_ref/automorphism_group_canonical_label.pyx

> 2. It seems (based on my vague understanding) that the automorphism group function could be replaced by a more general equivalence function, which returns the group of equivalences if two "non-linear codes" are equivalent (and "False" otherwise, or something). Is this true?

This isn't quite true, the set of isomorphisms does not form a subgroup, but a double coset. If you know the automorphism groups `A1 = Aut(G1)` and `A2 = Aut(G2)`, and you have an isomorphism `g : G1 --> G2`, then any other isomorphism is going to be something in the double coset `A2 g A1.` There's no point computing all the isomorphisms...

> 3. What exactly is a hypergraph and how does it correspond to a non-linear code? (And by non-linear I assume you mean a subset of GF(2)^n which is not necessarily closed under the usual coordinate-wise addition.)

Exactly. A hypergraph is a "graph" whose "edges" need only be subsets of the vertex set, not necessarily of size 2.


---

Comment by mhansen created at 2008-09-05 19:24:14

Looks good to me.


---

Attachment

The updated patch is good too :-)


---

Comment by mabshoff created at 2008-09-06 00:52:16

Merged in Sage 3.1.2.rc0


---

Comment by mabshoff created at 2008-09-06 00:52:16

Resolution: fixed
