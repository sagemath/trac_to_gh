# Issue 3991: [with patch, needs review] Matrix_mod2_dense.__hash__ 32-bit doctest failure

Issue created by migration from https://trac.sagemath.org/ticket/3991

Original creator: malb

Original creation time: 2008-08-29 11:30:54

Assignee: malb

CC:  cremona

Keywords: doctest failure

John reported this:
> The third is this:
>> File "/home/john/sage-3.1.2.alpha1/tmp/matrix_mod2_dense.py", line 267:
>>     sage: hex(hash(A))
>> Expected:
>>     '0xdeadbeed'
>> Got:
>>     '-0x21524113'


---

Attachment

John,

can you verify that this patch fixes the issue for you on your 32 bit box? Otherwise this is an "obvious" positive review.

Cheers,

Michael


---

Comment by cremona created at 2008-08-30 10:59:42

Patch applies fine and all doctests in sage.matrix pass.  OK!


---

Comment by mabshoff created at 2008-08-30 18:10:55

Merged in Sage 3.1.2.alpha3


---

Comment by mabshoff created at 2008-08-30 18:10:55

Resolution: fixed
