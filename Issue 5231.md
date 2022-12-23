# Issue 5231: [with patch, needs review] make relative number fields lazy

Issue created by migration from https://trac.sagemath.org/ticket/5231

Original creator: ncalexan

Original creation time: 2009-02-11 00:36:08

Assignee: was

CC:  was cc davidloeffler

Keywords: relative number fields lazy pari

The attached patch makes relative number fields truly lazy, meaning that they don't require PARI's nf or bnf structures for the base field nor PARI's rnf structures for the extension.  This means that arithmetic can be done in huge extensions, ones for which there is no hope of finding units, class groups, etc.

Along the way I cleaned some conversions to PARI and fixed a bug relativizing absolute fields over QQ.  I also added many doctests.  I also tested this with #4779's randomized testing; passed with flying colors.

This patch cannot be allowed to bitrot, it's just to much work to understand this part of the code.


---

Attachment


---

Comment by AlexGhitza created at 2009-02-11 05:01:02

Nick,

I hope to have some time to look at this (and hopefully review it) this evening (i.e. in about 6 hours).


---

Attachment


---

Comment by mabshoff created at 2009-02-11 06:05:14

Resolution: fixed


---

Comment by mabshoff created at 2009-02-11 06:05:14

Merged in Sage 3.3.rc0.

Cheers,

Michael
