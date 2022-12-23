# Issue 9590: Doctest failures in cone.py and toric_lattice_element.pyx on 32-bit Linux

Issue created by migration from https://trac.sagemath.org/ticket/9590

Original creator: mpatel

Original creation time: 2010-07-24 02:56:51

Assignee: mhampton

CC:  cremona davidloeffler leif novoselt vbraun

[Seen by John Cremona and Leif Leonhardy on 32-bit SUSE and 32-bit Ubuntu, respectively](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/6b8cef45c9f5e56c#6b8cef45c9f5e56c):

```
sage -t -long "devel/sage/sage/geometry/toric_lattice_element.pyx"
**********************************************************************
File "/local/jec/sage-4.5.2.alpha0/devel/sage/sage/geometry/toric_lattice_element.pyx",
line 235:
    sage: n.set_immutable()
Expected:
    2528502973977326415
Got nothing

sage -t -long "devel/sage/sage/geometry/cone.py"
**********************************************************************
File "/local/jec/sage-4.5.2.alpha0/devel/sage/sage/geometry/cone.py", line 559:
    sage: c = Cone([(1,0), (0,1)])
Expected:
    4372618627376133801
Got nothing
```

These may stem from one or more of #8986, #8987, and #9062.


---

Attachment


---

Comment by novoselt created at 2010-07-24 05:20:56

This should work, please test it on a 32-bit system as I don't have one set up.


---

Comment by novoselt created at 2010-07-24 05:20:56

Changing status from new to needs_review.


---

Comment by leif created at 2010-07-24 13:38:18


```sh
leif@californication:~/sage-4.5.2.alpha0-j6/devel/sage-9590$ ../../sage -t -long sage/geometry/
sage -t -long "devel/sage-9590/sage/geometry/fan.py"        
	 [10.9 s]
sage -t -long "devel/sage-9590/sage/geometry/polytope.py"   
	 [3.0 s]
sage -t -long "devel/sage-9590/sage/geometry/__init__.py"   
	 [0.1 s]
sage -t -long "devel/sage-9590/sage/geometry/all.py"        
	 [0.1 s]
sage -t -long "devel/sage-9590/sage/geometry/cone.py"       
	 [7.9 s]
sage -t -long "devel/sage-9590/sage/geometry/lattice_polytope.py"
	 [13.0 s]
sage -t -long "devel/sage-9590/sage/geometry/polyhedra.py"  
	 [152.0 s]
sage -t -long "devel/sage-9590/sage/geometry/toric_lattice.py"
	 [3.1 s]
sage -t -long "devel/sage-9590/sage/geometry/toric_lattice_element.pyx"
	 [3.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 193.4 seconds
leif@californication:~/sage-4.5.2.alpha0-j6/devel/sage-9590$ hg log | head -n 11
changeset:   14742:ebb1e171e138
tag:         tip
user:        Andrey Novoseltsev <novoselt@gmail.com>
date:        Fri Jul 23 23:09:59 2010 -0600
summary:     Trac 9590: Doctest failures in cone and toric_lattice_element.

changeset:   14741:af5f40a73eda
user:        Mitesh Patel <qed777@gmail.com>
date:        Wed Jul 21 20:13:55 2010 -0700
summary:     4.5.2.alpha0

```

(This is on Ubuntu 9.04 x86, Pentium 4 Prescott, gcc 4.3.3.)

So I can give Andrey's patch a positive review.

We could have added the hash codes for 32-bit systems, too, instead.


---

Comment by novoselt created at 2010-07-24 15:20:14

Replying to [comment:2 leif]:
> We could have added the hash codes for 32-bit systems, too, instead.

We could, but I don't know how to get those values for 32-bit systems on 64-bit ones and as I understand those numbers don't have any sense anyway and can potentially change. So these doctests just check that `hash` can be used and it returns the same value. If adding 32-bit hashes would be better, please add them.

I find it very peculiar how slow is `polyhedra.py` in this test. On sage.math most tests are a little bit faster, but this one takes only 41 second! On my quite old Mobile AMD Athlon 64 3000+ (1.8GHz) results are closer to those above, but `polyhedra.py` still tests only in 74 seconds! Is it just the difference between 32 and 64 bits?..


---

Comment by leif created at 2010-07-24 16:07:25

Replying to [comment:3 novoselt]:
> I find it very peculiar how slow is `polyhedra.py` in this test. On sage.math most tests are a little bit faster, but this one takes only 41 second! On my quite old Mobile AMD Athlon 64 3000+ (1.8GHz) results are closer to those above, but `polyhedra.py` still tests only in 74 seconds! Is it just the difference between 32 and 64 bits?..

This is on an otherwise idle Core2 (64-bit):

```sh
leif@quadriga:~/sage-4.5.2.alpha0$ ./sage -t -long devel/sage/sage/geometry/
sage -t -long "devel/sage/sage/geometry/__init__.py"
         [0.0 s]
sage -t -long "devel/sage/sage/geometry/toric_lattice_element.pyx"
         [1.0 s]
sage -t -long "devel/sage/sage/geometry/toric_lattice.py"
         [1.0 s]
sage -t -long "devel/sage/sage/geometry/polytope.py"
         [1.0 s]
sage -t -long "devel/sage/sage/geometry/lattice_polytope.py"
         [5.1 s]
sage -t -long "devel/sage/sage/geometry/fan.py"
         [4.7 s]
sage -t -long "devel/sage/sage/geometry/cone.py"
         [3.3 s]
sage -t -long "devel/sage/sage/geometry/all.py"
         [0.0 s]
sage -t -long "devel/sage/sage/geometry/polyhedra.py"
         [58.7 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 74.9 seconds
```



---

Comment by leif created at 2010-07-24 16:21:03

Just for the record: I've just tested the patch on that system, too. All tests in `sage/geometry` now take 0.4s less in total... ;-)

(The timings per file vary by sometimes more than 0.1s even on an idling machine.)


---

Comment by leif created at 2010-07-24 19:29:30

If anyone wants this to be fixed in a different way, here are two alternatives in a single patch:

```patch
diff --git a/sage/geometry/cone.py b/sage/geometry/cone.py
--- a/sage/geometry/cone.py
+++ b/sage/geometry/cone.py
@@ -557,8 +557,12 @@
         TESTS::
 
             sage: c = Cone([(1,0), (0,1)])
-            sage: hash(c)  # 64-bit
-            4372618627376133801
+            sage: hash(c)
+            1996666537 # 32-bit
+            4372618627376133801 # 64-bit
+            sage: c2 = Cone([(1,0), (0,1)])
+            sage: hash(c) == hash(c2)
+            True
         """
         if "_hash" not in self.__dict__:
             self._hash = hash(self._rays)
diff --git a/sage/geometry/toric_lattice_element.pyx b/sage/geometry/toric_lattice_element.pyx
--- a/sage/geometry/toric_lattice_element.pyx
+++ b/sage/geometry/toric_lattice_element.pyx
@@ -233,8 +233,13 @@
             ...
             TypeError: mutable vectors are unhashable
             sage: n.set_immutable()
-            sage: hash(n)  # 64-bit
-            2528502973977326415
+            sage: hash(n)
+            -378539185 # 32-bit
+            2528502973977326415 # 64-bit
+            sage: n2 = N(1,2,3)
+            sage: n2.set_immutable()
+            sage: hash(n) == hash(n2)
+            True
         """
         return Vector_integer_dense.__hash__(self)
```

(This is against vanilla alpha0.)

Otherwise (Seattle, wake up!) I'll set this to "positive review" (as is), s.t. it can be merged into alpha1.


---

Comment by leif created at 2010-07-25 08:17:13

Ok, since nobody complained [in time], I'll set this to "positive review".

Mitesh, please merge... ;-)


---

Comment by leif created at 2010-07-25 08:17:13

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-26 00:32:47

I also see the failures in the description on t2 with 4.5.2.alpha0 + #8059 (I ignored the patch rejects).  But the patch above fixes them.


---

Comment by ddrake created at 2010-07-26 07:36:58

I thought that maybe Leif's suggestions would be preferred, but Carl Witty said (https://groups.google.com/group/sage-devel/browse_thread/thread/9a0f357c8ec9bbd):

```
Hmm... looks like the current state of affairs is a mess.  Looking
through the 'def __hash__' grep hits in sage/rings, there are quite a
few of each of the following:

1) no doctest at all
2) provide both 32-bit and 64-bit doctests
3) define your hash function to produce a 32-bit output that's the
same on 32-bit and 64-bit systems; doctest an instance of that output
4) doctest hash value equality without ever showing a doctest output

plus one instance where the hash output is marked "# random".

So whatever you do with this particular patch, it won't make things
much worse :) 
```

So, I'll merge this, and maybe we'll figure out a better way to test hashing later.


---

Comment by ddrake created at 2010-07-26 07:40:42

Resolution: fixed
