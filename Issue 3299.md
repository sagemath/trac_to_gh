# Issue 3299: memleak in PolyBoRi interface

Issue created by migration from https://trac.sagemath.org/ticket/3299

Original creator: malb

Original creation time: 2008-05-25 17:14:26

Assignee: mabshoff

CC:  burcin polybori

Keywords: polybori, memleak


```
==2143== 80 bytes in 2 blocks are still reachable in loss record 481 of 2,900
==2143==    at 0x4C1FFAB: malloc (vg_replace_malloc.c:207)
==2143==    by 0x2158F146: MMalloc (safe_mem.c:62)
==2143==    by 0x215C47AB: cuddInitTable (cuddTable.c:402)
==2143==    by 0x215C4252: Cudd_Init (cuddInit.c:141)
==2143==    by 0x2154B875: polybori::CDDManager<polybori::CCuddInterface>::CDDManager(unsigned) (CCuddCore.h:121)
==2143==    by 0x2154907D: polybori::BoolePolyRing::BoolePolyRing(unsigned, int,bool) (BooleRing.h:80)
==2143==    by 0x215081B8: __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___init__(_object*, _object*, _object*) (ccobject.h:50)
...
==2143== 160 bytes in 2 blocks are still reachable in loss record 534 of 2,900
==2143==    at 0x4C1FFAB: malloc (vg_replace_malloc.c:207)
==2143==    by 0x2158F146: MMalloc (safe_mem.c:62)
==2143==    by 0x215C43A3: Cudd_Init (cuddInit.c:183)
==2143==    by 0x2154B875: polybori::CDDManager<polybori::CCuddInterface>::CDDManager(unsigned) (CCuddCore.h:121)
==2143==    by 0x2154907D: polybori::BoolePolyRing::BoolePolyRing(unsigned, int,bool) (BooleRing.h:80)
==2143==    by 0x215081B8: __pyx_pf_4sage_5rings_10polynomial_5pbori_21BooleanPolynomialRing___init
__(_object*, _object*, _object*) (ccobject.h:50)
```


So it seems we are allocating a buffer for Cudd each time we create a ring but this buffer keeps increasing and is never free'd?



---

Comment by PolyBoRi created at 2008-05-29 07:49:37

Hm, my pure PolyBoRi-tests are clean. Which example code was used above?

Regards,
  Alexander


---

Comment by malb created at 2008-05-29 08:30:38

I just ran `sage -t -valgrind pbori.pyx` which probably isn't much help. Since I bet the problem is in our constructor, maybe you can spot something obviously wrong?


```
cdef class BooleanPolynomialRing(MPolynomialRing_generic):
    def __init__(self, n=None, names=None, order='lex'):
        cdef Py_ssize_t i, j, bstart, bsize

        if n is None and names is not None:
            if PY_TYPE_CHECK(names, tuple) or PY_TYPE_CHECK(names, list):
                n = len(names)
        try:
            n = int(n)
        except TypeError, msg:
            raise TypeError, "Number of variables must be an integer"

        if n < 1:
            raise ValueError, "Number of variables must be greater than 1."

        self.pbind = <Py_ssize_t*>sage_malloc(n*sizeof(Py_ssize_t))
        cdef char *_n

        order = TermOrder(order, n)

        try:
            pb_order_code = order_mapping[order.blocks[0][0]]
        except KeyError:
            raise ValueError, "Only lex, deglex, degrevlex orders are supported."

        if len(order.blocks) > 1:
            if pb_order_code is lp:
                raise ValueError, "Only deglex and degrevlex are supported for block orders."
            elif pb_order_code is dlex:
                pb_order_code = block_dlex
            elif pb_order_code is dp_asc:
                pb_order_code = block_dp_asc
            for i in range(1, len(order.blocks)):
                if order.blocks[0][0] != order.blocks[i][0]:
                    raise ValueError, "Each block must have the same order type (deglex or degrevlex) for block orderings."

        if (pb_order_code is dlex) or (pb_order_code is lp) or \
                (pb_order_code is block_dlex):
            for i from 0 <= i < n:
                self.pbind[i] = i
        elif pb_order_code is dp_asc:
            for i from 0 <= i < n:
                self.pbind[i] = n - i -1
        else:
            # pb_order_code is block_dp_asc:
            bstart = 0
            for i from 0 <= i < len(order.blocks):
                bsize = order.blocks[i][1]
                for j from 0 <= j < bsize:
                    self.pbind[bstart + j] = bstart + bsize - j -1
                bstart += bsize

        PBRing_construct(&self._pbring, n, pb_order_code)

        MPolynomialRing_generic.__init__(self, GF(2), n, names, order)

        counter = 0
        for i in range(len(order.blocks)-1):
            counter += order.blocks[i][1]
            pb_append_block(counter)

        for i from 0 <= i < n:
            _n = self._names[self.pbind[i]]
            pb_set_variable_name(i, _n)

        self._zero_element = new_BP(self)
        PBPoly_construct_int(&(<BooleanPolynomial>self._zero_element)._pbpoly, 0)
        self._one_element  = new_BP(self)
        PBPoly_construct_int(&(<BooleanPolynomial>self._one_element)._pbpoly, 1)

        self._monom_monoid = BooleanMonomialMonoid(self)

        global cur_ring
        cur_ring = self

        self.__interface = {}

    def __dealloc__(self):
        sage_free(self.pbind)
        PBRing_destruct(&self._pbring)
```



---

Comment by PolyBoRi created at 2008-05-29 11:51:13

Replying to [comment:2 malb]:

Hi, 
one "interesting" thing I see is the global ring:


```
         global cur_ring
         cur_ring = self
```


Does something care for its destruction? And what about the destruction of `self._zero_element` and `self._one_element`?

(Since 0.3 non-destructed polynomials delay the destruction of the ring.)

Regards,
  Alexander
