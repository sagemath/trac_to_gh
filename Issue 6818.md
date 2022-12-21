# Issue 6818: [with patch; needs review] maxima interface gets dramatically slower over time

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-08-24 14:43:39

Assignee: was

If you do a few hundred calls to the maxima interface, it gets way way slower.


```
sage: timeit("str(maxima.eval('1+2'))")
5 loops, best of 3: 758 µs per loop
sage: timeit("str(maxima.eval('1+2'))")
625 loops, best of 3: 1.22 ms per loop
sage: timeit("str(maxima.eval('1+2'))")
125 loops, best of 3: 2.98 ms per loop
sage: timeit("str(maxima.eval('1+2'))")
125 loops, best of 3: 3.97 ms per loop
```


It turns out that this is caused by computation of the maxima input prompt number, which uses the following "clever" algorithm to compute "n+1":


```
(defmfun makelabel (x)
  (when (and $dskuse (not $nolabels) (> (incf dcount) $filesize))
    (setq dcount 0)
    (dsksave))
  (setq linelable ($concat '|| x $linenum))
  (unless $nolabels
    (when (or (null (cdr $labels))
              (when (member linelable (cddr $labels) :test #'equal)
                (setf $labels (delete linelable $labels :count 1 :test #'eq)) t)
              (not (eq linelable (cadr $labels))))
      (setq $labels (cons (car $labels) (cons linelable (cdr $labels))))))
  linelable)
```


More precisely, this code "checks
that the list containing all labels does not contain the new label
which it generates. After you create 2*35150 labels, this takes longer than when maxima starts.", according to Andrej Vodopivec who tracked this down and told us a simple fix.  Put:


```
nolabels:true;
```


at the beginning of our Maxima session.  This is fine for Sage, since Sage doesn't use the labels in any way.


---

Attachment


---

Comment by AlexGhitza created at 2009-08-24 23:49:53

Looks good.


---

Comment by mvngu created at 2009-08-25 01:17:06

Resolution: fixed
