# Issue 2719: bitset is completely broken on os x 10.4 G5

Issue created by migration from https://trac.sagemath.org/ticket/2719

Original creator: was

Original creation time: 2008-03-29 16:30:06

Assignee: cwitty


```
FERMAT -- os x 10.4 g5 -- has interesting failures here in the 
new bitset code:
          sage -t  devel/sage-main/sage/misc/misc_c.pyx

    sage: test_bitset('00101', '01110', 4)
Expected:
    a 00101
    a.size 5
    a.limbs 1
    b 01110
    a.check(n)   True
    a.set(n)     00101
    a.unset(n)   00100
    a.set_to(n)  00101
    a.flip(n)    00100
    a.is_zero()  False
    a.eq(b)      False
    a.cmp(b)     1
    a.copy()     00101
    r.zero()     00000
    not a        11010
    a and b      00100
    a or b       01111
    a xor b      01011
    a.rshift(n)  10000
    a.lshift(n)  00000
    a.first()           2
    a.next(n)           4
    a.first_diff(b)     1
    a.next_diff(b, n)   4
    a.hamming_weight()  2
    a.hamming_weight_sparse()  2
Got:
    a 00101
    a.size 5
    a.limbs 1
    b 01110
    a.check(n)   True
    a.set(n)     00101
    a.unset(n)   00100
    a.set_to(n)  00101
    a.flip(n)    00100
    a.is_zero()  False
    a.eq(b)      True
    a.cmp(b)     1
    a.copy()     00000
    r.zero()     00000
    not a        11010
    a and b      00100
    a or b       01111
    a xor b      01011
    a.rshift(n)  10000
    a.lshift(n)  00000
    a.first()           2
    a.next(n)           4
    a.first_diff(b)     1
    a.next_diff(b, n)   4
    a.hamming_weight()  2
    a.hamming_weight_sparse()  2
```



---

Attachment


---

Comment by robertwb created at 2008-03-29 18:19:57

fix endianness issues (thanks to cwitty for pointing this out)


---

Comment by was created at 2008-03-29 18:46:04

It works.


---

Comment by mabshoff created at 2008-03-29 18:47:54

Resolution: fixed


---

Comment by mabshoff created at 2008-03-29 18:47:54

Merged in Sage 2.11.rc0
