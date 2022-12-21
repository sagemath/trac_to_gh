# Issue 1138: add implementation of tonelli-shanks to sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-10 12:15:35

Assignee: somebody

CC:  dmharvey


```
Hi, I have implemented the Tonelli and Shanks algorithm which has a
complexity of O(ln^4(p)) and appears to be amazing fast. So far its a
quick and dirty implementation directly in my Sage file and without
error handling. I will ask Martin (when meeting him next time in the
office) how to integrate the implentation properly in Sage. Of course,
if somebody else does it, I am even more happy :-) Here is the current
code which returns x such that x^2 == a mod p:

def step3(b,p,r,x):
       # Step 3: Find exponent
       if GF(p)(b) == GF(p)(1):
               return b,r,x,0
       m = 0
       while GF(p)(b**(2**m)) != 1:
               m = m + 1
       if m == r:
               return b,r,0,0
       return b,r,x,m

def s_root(a,p):
       # Step 0: Determine q:
       q = 0
       e = 0
       while q % 2 != 1:
               e = e+1
               q = (p-1) / 2**e
       # Step 1: Find generator
       n = ZZ.random_element()
       while kronecker(n,p) != -1:
               n = ZZ.random_element()
       n = GF(p)(n)
       z = GF(p)(n**q)
       # Step 2: Initialize
       y = z
       r = e
       a = GF(p)(a)
       x = GF(p)(a**((q-1)/2))
       b = GF(p)(a*(x**2))
       x = GF(p)(a*x)
       # Step 3:
       b,r,x,m = step3(b,p,r,x)
       # Step 4: Reduce exponent
       while ZZ(m) != ZZ(0):
               t = GF(p)(y**(2**(r-m-1)))
               y = GF(p)(t**2)
               r = GF(p)(m)
               x = GF(p)(x*t)
               b = GF(p)(b*y)
               b,r,x,m = step3(b,p,r,x)
       return x

a = GF(17)(13)
print s_root(a,17)
```


Benchmarks

```
Hi,

> Could you post some cool impressive benchmarks? :-)
>
>  william

ok :-)

Here the result for finding one root in GF(p) where p is 128, 256 and
512 bit prime:

Results for 128 bit prime:
Original:
Time: CPU 0.04 s, Wall: 0.04 s
Number of roots found:
1
Tonelli:
Time: CPU 0.00 s, Wall: 0.00 s
Number of roots found:
1
Results for 256 bit prime:
Original:
Time: CPU 0.96 s, Wall: 0.96 s
Number of roots found:
0
Tonelli:
Time: CPU 0.00 s, Wall: 0.00 s
Number of roots found:
0
Results for 512 bit prime:
Original:
Time: CPU 9.94 s, Wall: 10.09 s
Number of roots found:
0
Tonelli:
Time: CPU 0.00 s, Wall: 0.00 s
Number of roots found:
0

This shows only that the old implementation was inefficient for large
p. The results for the original implementation for 256 and 512 bit are
not contained in the following results, since sqrt(a) returned an
error for the 256 bit and 512 bit case. Here are the results for 100
random values for a. Find x: x^2==a mod p

Results for 128 bit prime:
Original:
Time: CPU 5.36 s, Wall: 5.41 s
Number of roots found:
47
Tonelli:
Time: CPU 0.07 s, Wall: 0.08 s
Number of roots found:
47
Results for 256 bit prime:
Tonelli:
Time: CPU 0.10 s, Wall: 0.10 s
Number of roots found:
48
Results for 512 bit prime:
Tonelli:
Time: CPU 0.30 s, Wall: 0.33 s
Number of roots found:
50


Here is the complete code I used:
- Show quoted text -

def step3(b,p,r,x):
       # Step 3: Find exponent
       if GF(p)(b) == GF(p)(1):
               return b,r,x,0
       m = 0
       while GF(p)(b**(2**m)) != 1:
               m = m + 1
       if m == r:
               return b,r,0,0
       return b,r,x,m

def s_root(a,p):
       # Step 0: Determine q:
       q = 0
       e = 0
       while q % 2 != 1:
               e = e+1
               q = (p-1) / 2**e
       # Step 1: Find generator
       n = ZZ.random_element()
       while kronecker(n,p) != -1:
               n = ZZ.random_element()
       n = GF(p)(n)
       z = GF(p)(n**q)
       # Step 2: Initialize
       y = z
       r = e
       a = GF(p)(a)
       x = GF(p)(a**((q-1)/2))
       b = GF(p)(a*(x**2))
       x = GF(p)(a*x)
       # Step 3:
       b,r,x,m = step3(b,p,r,x)
       # Step 4: Reduce exponent
       while ZZ(m) != ZZ(0):
               t = GF(p)(y**(2**(r-m-1)))
               y = GF(p)(t**2)
               r = GF(p)(m)
               x = GF(p)(x*t)
               b = GF(p)(b*y)
               b,r,x,m = step3(b,p,r,x)
       return x

A = {}

def go1(p):
       X = {}
       for i in range(0,len(A)):
               X[i] = sqrt(GF(p)(A[i]))
       return X

def go2(p):
       X ={}
       for i in range(0,len(A)):
               X[i] = s_root(A[i], p)
       return X

def analyseResult(A,X,p):
       numberRoots = 0
       for i in range(0,len(A)):
               x = X[i]
               a = A[i]
               if x in GF(p):
                       if (GF(p)(x) != GF(p)(0)) & (GF(p)(x**2) != GF(p)(a)):
                               print 'Error in implemenation'
                       elif GF(p)(x) != GF(p)(0):
                               numberRoots = numberRoots + 1
       print 'Number of roots found:'
       print numberRoots

n = 100

print 'Results for 128 bit prime:'
p = next_prime(2^(128))
while p % 4 != 1:
       p = next_prime(p+1)

for i in range(0,n):
       A[i] = GF(p).random_element()

print 'Original:'
time X = go1(p)
analyseResult(A,X,p)

print 'Tonelli:'
time X = go2(p)
analyseResult(A,X,p)

print 'Results for 256 bit prime:'
p = next_prime(2^(256))
while p % 4 != 1:
       p = next_prime(p+1)

for i in range(0,n):
       A[i] = GF(p).random_element()

#print 'Original:'
#time X = go1(p)
#analyseResult(A,X,p)

print 'Tonelli:'
time X = go2(p)
analyseResult(A,X,p)

print 'Results for 512 bit prime:'
p = next_prime(2^(512))
while p % 4 != 1:
       p = next_prime(p+1)

for i in range(0,n):
       A[i] = GF(p).random_element()

#print 'Original:'
#time X = go1(p)
#analyseResult(A,X,p)

print 'Tonelli:'
time X = go2(p)
analyseResult(A,X,p)


```



---

Comment by robertwb created at 2008-02-16 21:18:52

Changing status from new to assigned.


---

Comment by robertwb created at 2008-02-16 21:18:52

The algorithm as written is NOT faster for actual squares mod p, the timings are poor because sqrt(a) creates symbolic square roots for half the values. 

For p == 1 mod 16, I think there may be an improvement. I am investigating this further.


---

Comment by robertwb created at 2008-02-16 21:18:52

Changing assignee from somebody to robertwb.


---

Comment by robertwb created at 2008-02-16 21:48:04

This algorithm has also been implemented in FLINT, so I am simply going to wrap that.


---

Attachment

I wasn't able to get FLINT to give me the correct answers, the algorithm turns out to be simple enough that I just implemented it right in the library. 

There are several other minor optimizations in the patch too.


---

Comment by dmharvey created at 2008-02-23 03:25:18

Isn't this algorithm already in PARI?


---

Comment by dmharvey created at 2008-02-23 14:43:22

Robert's patch didn't apply cleanly to 2.10.2, I've rebased it, see new patch. I'm going to review it more carefully now.


---

Attachment

Hmmm.... I apply the rebased patch to 2.10.2, and I'm getting one weird doctest failure (mac OS 10.4.11, intel):


```
sage -t  devel/sage-1138b/sage/schemes/generic/projective_space.py
A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [12.9 s]
exit code: 256
```


Robert, could you take a look at this? (Also perhaps check that you agree I haven't mangled your patch during the rebasing.)

Once this is resolved, I'll continue reviewing the patch (I've been meaning to learn this algorithm for a while... :-))


---

Attachment


---

Comment by robertwb created at 2008-03-26 03:14:43

I rebased it again against 2.10.4 and touched it up a bit. It should work now. `sage/schemes/generic/projective_space.py` passes on my OS X 10.4.11 intel laptop.


---

Attachment

Looks good to me.  I've attached 1138.patch which is rebased against sage-3.0.alpha0


---

Comment by mhansen created at 2008-04-04 20:35:29

The original code was from Steffen Reidt: http://groups.google.com/group/sage-devel/browse_frm/thread/e7910523502a641/62d692cb57caf7ff?lnk=gst&q=tonelli+shanks#62d692cb57caf7ff


---

Comment by mabshoff created at 2008-04-04 21:29:23

Merged 1138.patch in Sage 3.0.alpha1


---

Comment by mabshoff created at 2008-04-04 21:29:23

Resolution: fixed
