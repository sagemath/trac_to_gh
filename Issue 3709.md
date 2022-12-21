# Issue 3709: QuaternionAlgebraElement.sqrt()

Issue created by migration from Trac.

Original creator: epotash

Original creation time: 2008-07-23 00:00:33

Assignee: tbd

This method currently does not exist, but it should.  For an outline of an algorithm see: http://www.mathreference.com/ring-q,sqr.html

The only issue is that, as far as I know, there is no standard for which square root to take like there is over C or R.


---

Comment by fwclarke created at 2011-12-18 17:59:16

Changing status from new to needs_info.


---

Comment by fwclarke created at 2011-12-18 17:59:16

In the quaternions there are infinitely many square-roots of -1: (xi + yj + zk)<sup>2</sup> = -1 for any real numbers x, y, z such that x<sup>2</sup> + y<sup>2</sup> + z<sup>2</sup> = 1.  I don't know how to prefer one of these.
