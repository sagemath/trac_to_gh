# Issue 5939: typo in g.automorphism_group documentation, for g a graph; also partition parameter isn't tested anywhere in the docstring

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-29 16:26:04

Assignee: rlm

There is a typo in the docstring for the graph automorphism function:


```
``translation`` - if True, then output includes a a
           dictionary translating from keys == vertices to entries == elements
           of 1,2,...,n (since permutation groups can currently only act on
           positive integers).
```


Notice that it says "includes a a" (a appears twice). 

Also, the doctests in that docstring do not test the partition parameter at all, and it seems to me that would be a very important parameter to illustrate, especially given that the docstring starts {{{
        Returns the largest subgroup of the automorphism group of the
        (di)graph whose orbit partition is finer than the partition given.
}}}
which suggests that the most important thing the reader should know is that the automorphism_group computes something associated to a partition.


---

Attachment


---

Comment by mvngu created at 2009-07-19 14:32:38

Resolution: fixed
