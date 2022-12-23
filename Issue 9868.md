# Issue 9868: finite field bug

Issue created by migration from https://trac.sagemath.org/ticket/9869

Original creator: mariah

Original creation time: 2010-09-07 18:27:37

Assignee: AlexGhitza


```
# Demonstrate a finite field bug in which
# a product of nonzero elements is equal to 0 
# (which should not happen in a field)
#
# This is the smallest example I could find. It seems salient that
# the square of p is bigger than a 32-bit C integer. Larger values
# for p also exhibit the bug, smaller ones do not.

p = 2^16 + 1

# Create a quadratic field extension
K.<alpha> = GF(p^2)

# Choose some non-zero element of K, use the random_element
# method.
x = K(0)
while x == K(0):
  x = K.random_element()

K.<alpha> = GF(p^2)  # this line is necessary for bug
x_coerce = K(x)
print 2*x_coerce  # prints zero
```




---

Comment by robertwb created at 2010-10-19 15:41:55

Duplicate of #10045 .


---

Comment by robertwb created at 2010-10-19 15:41:55

Resolution: duplicate
