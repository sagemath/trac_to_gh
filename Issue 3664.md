# Issue 3664: major updates to root systems

Issue created by migration from https://trac.sagemath.org/ticket/3664

Original creator: mhansen

Original creation time: 2008-07-16 00:43:54

Assignee: mhansen

CC:  sage-combinat




---

Attachment


---

Attachment


---

Comment by mhansen created at 2008-08-06 19:30:05

This depends on #3662 and #3781 .

Credit goes to Dan Bump, Nicolas Thiery, Nicolas Borie (first contribution I believe), and Mike Hansen.


---

Comment by mabshoff created at 2008-08-08 23:07:50

I am seeing doctest failures here:

```
sage -t -long devel/sage/sage/combinat/crystals/spins.py # 2 doctests failed
sage -t -long devel/sage/sage/combinat/crystals/letters.py # 3 doctests failed
sage -t -long devel/sage/sage/combinat/crystals/crystals.py # 13 doctests failed
```

For example:

```
File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/tmp/spins.py", line 81:
    sage: len(TensorProductOfCrystals(C,C,generators=[[C.list()[0],C.list()[0]]]))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[4]>", line 1, in <module>
        len(TensorProductOfCrystals(C,C,generators=[[C.list()[Integer(0)],C.list()[Integer(0)]]]))###line 81:
    sage: len(TensorProductOfCrystals(C,C,generators=[[C.list()[0],C.list()[0]]]))
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/combinat.py", line 767, in __len__
        return self.count()
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py", line 924, in count
        for x in self.highest_weight_vectors())
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py", line 924, in <genexpr>
        for x in self.highest_weight_vectors())
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/tensor_product.py", line 365, in weight
        return sum(self[j].weight() for j in range(len(self))) 
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/tensor_product.py", line 365, in <genexpr>
        return sum(self[j].weight() for j in range(len(self)))
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py", line 590, in weight
        return self.Phi() - self.Epsilon()
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py", line 686, in Phi
        return sum(self.phi(i) * self._parent.Lambda()[i-1] for i in self.index_set())
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py", line 686, in <genexpr>
        return sum(self.phi(i) * self._parent.Lambda()[i-1] for i in self.index_set())
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/local/lib/python2.5/site-packages/sage/combinat/family.py", line 387, in __getitem__
        return self.dictionary.__getitem__(i)
    KeyError: 0
```


Could it be that there is a patch missing in the dependency chain?

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-08-09 03:47:27

I added trac_3664-3.patch that fixes the doctest failures.


---

Comment by mabshoff created at 2008-08-09 22:24:56

Merged all three patches in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-09 22:24:56

Resolution: fixed
