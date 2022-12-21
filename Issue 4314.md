# Issue 4314: [with patch] Add some functionality to matrices in eclib

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-10-17 17:12:39

Assignee: was

Keywords: eclib CremonaModularSymbols

The attached patch (based on 3.1.4) makes two changes in libs/cremona/mat*:
    1. Adds getitem methods to the matric class so i,j entries may be extracted;
    2. Changes the conversion to sage of matrices so that matrices over ZZ are constructed instead of ZZ.

These were done as part of a hands-on tutorial William gave to John in Bordeaux.


---

Comment by mhansen created at 2008-10-18 10:15:50

This is a dupe of #4313


---

Comment by mhansen created at 2008-10-18 10:15:50

Resolution: duplicate


---

Comment by cremona created at 2008-10-18 14:04:32

Replying to [comment:1 mhansen]:
> This is a dupe of #4313

Thanks.  One day I'll succeed in creating a new ticket with a pre-existing patch without causing a duplication!
