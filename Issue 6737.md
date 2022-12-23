# Issue 6737: change occurrences of "Pyrex" to "Cython"

Issue created by migration from https://trac.sagemath.org/ticket/6737

Original creator: mvngu

Original creation time: 2009-08-11 20:04:35

Assignee: tba

All occurrences of "Pyrex" should now be changed to "Cython". See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/b9b7eea2d9575a7f) thread for some background information.


---

Comment by was created at 2010-01-18 04:13:04


```
sage: search_src('pyrex')
matrix/matrix_modn_sparse.pyx:7:TODO: - move vectors into a pyrex vector class - add _add_ and
server/notebook/worksheet.py:3800:        elif system in ['cython', 'pyrex', 'sagex']:
combinat/expnums.pyx:126:    A vanilla python (but compiled via pyrex) implementation of
combinat/matrices/dancing_links.pyx:106:        # It is the *trick* needed to pickle pyrex extension types.
rings/complex_interval.pyx:12:    -- Joel B. Mohler (2006-12-16): naive rewrite into pyrex
rings/ring.pyx:1040:            #except AttributeError:   # for pyrex classes
rings/rational.pyx:3172:def pyrex_rational_reconstruction(integer.Integer a, integer.Integer m):
rings/rational.pyx:3194:        sage: sage.rings.rational.pyrex_rational_reconstruction(34, 100)
rings/integer.pyx:596:                    # pyrex to play games with refcount for the None object, which
rings/integer.pyx:622:                # we could skip the double lookup. Unfortunately pyrex doesn't
rings/integer.pyx:670:        # It is the *trick* needed to pickle pyrex extension types.
rings/integer.pyx:2616:        return rational.pyrex_rational_reconstruction(self, m)
rings/complex_number.pyx:8:- Joel B. Mohler (2006-12-16): naive rewrite into pyrex
rings/polynomial/polynomial_compiled.pyx:24:    pyrex.
graphs/generic_graph_pyx.pyx:74:    This kind of speed cannot be achieved by naive pyrexification of the
misc/all.py:74:pyrex = cython # synonym -- for now
gsl/all.py:2:# http://wwwteor.mi.infn.it/%7Epernici/pyrexgsl/pyrexgsl.html
```



---

Comment by gaer created at 2010-01-18 06:19:37

Removes Pyrex


---

Comment by gaer created at 2010-01-18 06:24:29

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2010-01-18 06:25:26

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-18 23:46:11

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-01-19 00:15:10

rebased, apply only this patch


---

Comment by rlm created at 2010-01-19 00:26:13

Resolution: fixed


---

Attachment
