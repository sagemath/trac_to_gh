# Issue 2486: [with patch, positive review] remove unused/broken vector and matrix pyx files

archive/issues_002486.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nThis file does not compile with cython currently but is in the tree.  It is currently disabled in setup.py and should be removed or fixed.  This is a significant priority as it makes the development of efficient(parallel) build systems problematic and wastes space, especially for files which have not been touched in ages. Code that does not build should not be in the main repository.\n\n```\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\ncimport matrix_pid_sparse\n       ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_sparse.pxd:1:8: 'matrix_pid_sparse.pxd' not found\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\ncdef class Matrix_field_sparse(matrix_pid_sparse.Matrix_pid_sparse):\n    ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_sparse.pxd:3:5: 'Matrix_pid_sparse' is not declared\n\n\ncython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o matrix_field_sparse.c matrix_field_sparse.pyx\n```\n\n```\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\ncimport matrix_pid_sparse\n       ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_sparse.pxd:1:8: 'matrix_pid_sparse.pxd' not found\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\ncdef class Matrix_field_sparse(matrix_pid_sparse.Matrix_pid_sparse):\n    ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_sparse.pxd:3:5: 'Matrix_pid_sparse' is not declared\n\n\ncython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o matrix_cyclo_dense.c matrix_cyclo_dense.pyx\n```\n\n```\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n#  The full text of the GPL is available at:\n#\n#                  http://www.gnu.org/licenses/\n#*****************************************************************************\n\ninclude 'interrupt.pxi'\n^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/mpc.pyx:27:0: 'interrupt.pxi' not found\n\n\ncython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o mpc.c mpc.pyx\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n       ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_dense.pyx:5:8: 'matrix_pid_dense.pxd' not found\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\nfrom sage.rings.finite_field import is_FiniteField\nfrom sage.rings.integer_mod_ring import is_IntegerModRing\n\n\ncdef class Matrix_field_dense(matrix_pid_dense.Matrix_pid_dense):\n    ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_dense.pyx:17:5: 'Matrix_pid_dense' is not declared\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n            [          1           5       z - 1]\n            sage: print A.denominator()\n            3\n        \"\"\"\n        if self.nrows() == 0 or self.ncols() == 0:\n            return integer.Integer(1)\n                         ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_dense.pyx:202:26: undeclared name not builtin: integer\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n            R = range(n)\n        else:\n            R = [t]\n        for i in R:\n            tm = sage.misc.misc.verbose('applying berlekamp-massey')\n            g = berlekamp_massey.berlekamp_massey(cols[i].list())\n                               ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_dense.pyx:718:32: undeclared name not builtin: berlekamp_massey\n\n\ncython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o matrix_field_dense.c matrix_field_dense.pyx\n```\n\n```\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ########################################################################\n    #def __new__(self, parent, entries, copy, coerce):\n    #    allocate memory\n    #def __dealloc__(self):\n    #    free memory\n    def __richcmp__(Matrix self, right, int op):  # always need for mysterious reasons.\n                          ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/template.pyx:29:27: Expected ')'\n\n\ncython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o template.c template.pyx\n```\n\n```\ncython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o totallyreal_data.c totallyreal_data.pyx\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ########################################################################\n    #def __new__(self, parent, entries, copy, coerce):\n    #    allocate memory\n    #def __dealloc__(self):\n    #    free memory\n    def __richcmp__(Matrix self, right, int op):  # always need for mysterious reasons.\n                          ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_RR_dense.pyx:28:27: Expected ')'\n\n\ncython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o matrix_RR_dense.c matrix_RR_dense.pyx\n```\n\n```\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    that *must* have been initialized using mpq_init.\n    \"\"\"\n    if n >= v.degree:\n        raise IndexError, \"Index must be between 0 and %s.\"%(v.degree - 1)\n    cdef Py_ssize_t m\n    m = binary_search0(v.positions, v.num_nonzero, n)\n                     ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/modules/vector_rational_sparse_c.pxi:150:22: undeclared name not builtin: binary_search0\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    cdef Py_ssize_t i, m, ins\n    cdef Py_ssize_t m2, ins2\n    cdef Py_ssize_t *pos\n    cdef mpq_t *e\n\n    m = binary_search(v.positions, v.num_nonzero, n, &ins)\n                    ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/modules/vector_rational_sparse_c.pxi:185:21: undeclared name not builtin: binary_search\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n                z = Rational(entries[i])\n                mpq_set(self.v.entries[i], z.value)\n                self.v.positions[i] = entries[i][0]\n\n    def __dealloc__(self):\n        clear_mpq_vector(&self.v)\n                       ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/modules/vector_rational_sparse.pyx:39:24: undeclared name not builtin: clear_mpq_vector\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\n    def list(self):\n        return mpq_vector_to_list(&self.v)\n\n    cdef void rescale(self, mpq_t x):\n        scale_mpq_vector(&self.v, x)\n                       ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/modules/vector_rational_sparse.pyx:90:24: undeclared name not builtin: scale_mpq_vector\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        add_mpq_vector_init(&z1, &self.v, &other.v, ONE)\n        mpq_clear(ONE)\n\n        w = Vector_mpq(self.v.degree)\n        z2 = &(w.v)\n        clear_mpq_vector(z2)   # free memory wasted on allocated w\n                       ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/modules/vector_rational_sparse.pyx:105:24: undeclared name not builtin: clear_mpq_vector\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        \n        The sparcity is a bound on the number of nonzeros per row.\n        \"\"\"\n        cdef int i\n        for i from 0 <= i < sparcity:\n            self[random.randrange(self.v.degree)] = random.randrange(1,bound)\n                                                         ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/modules/vector_rational_sparse.pyx:150:58: undeclared name not builtin: random\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        \n        The sparcity is a bound on the number of nonzeros per row.\n        \"\"\"\n        cdef int i\n        for i from 0 <= i < sparcity:\n            self[random.randrange(self.v.degree)] = random.randrange(1,bound)\n                      ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/modules/vector_rational_sparse.pyx:150:23: undeclared name not builtin: random\n\n\ncython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o vector_rational_sparse.c vector_rational_sparse.pyx\n```\n\n```\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n            h = h ^ (i * hash(v[i]))\n        h = h ^ self._value_matrix._hash()    \n        self.cache('hash', h)\n        return h\n\n    cdef _comp_valaddeds(self):\n        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:142:9: Signature not compatible with previous declaration\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n            for i from 0 <= i < self._nrows:\n                self._value_matrix.set_unsafe(i, i, xint)\n                self._relprecs_mat[i][i] = xrprec\n            self._initialized = True                    \n            \n    cdef void _comp_valaddeds(self):\n        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:292:9: '_comp_valaddeds' already defined\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n                n += 1\n\n    cdef void _adjust_prec_info_global(self, RingElement absolute, RingElement relative):\n        pass\n\n    cdef void _adjust_prec_info_global_local(self, RingElement absolute, object relative, coerce):\n        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:306:9: Signature not compatible with previous declaration\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        pass\n\n    cdef void _adjust_prec_info_global_local(self, RingElement absolute, object relative, coerce):\n        pass\n\n    cdef void _adjust_prec_info_local_global(self, object absolute, RingElement relative, coerce):\n        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:309:9: Signature not compatible with previous declaration\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        pass\n\n    cdef void _adjust_prec_info_local_global(self, object absolute, RingElement relative, coerce):\n        pass\n\n    cdef void _adjust_prec_info_local_local(self, object absolute, object relative, coerce):\n        ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:312:9: Signature not compatible with previous declaration\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        Matrix_dense.__init__(self, parent)\n        self._nrows = parent.nrows()\n        self._ncols = parent.ncols()\n        # Allocate an array for the precisions of the elements\n        _sig_on\n        self._relprecs = <ulong *>sage_malloc(size_of(ulong) * (self._nrows * self._ncols))\n                                                    ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:88:53: undeclared name not builtin: size_of\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        Matrix_dense.__init__(self, parent)\n        self._nrows = parent.nrows()\n        self._ncols = parent.ncols()\n        # Allocate an array for the precisions of the elements\n        _sig_on\n        self._relprecs = <ulong *>sage_malloc(size_of(ulong) * (self._nrows * self._ncols))\n                                                          ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:88:59: 'ulong' is not a constant, variable or function identifier\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        if not x is None: return x\n\n        if not self._mutability._is_immutable:\n            raise TypeError, \"mutable matrices are unhashable\"\n        \n        v = self._relprecs\n               ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:131:16: Cannot convert 'matrix_padic_capped_relative_dense.ulong *' to Python object\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        self._valaddeds = {}\n\n        if entries is None:\n            x = self.base_ring()(0)\n            is_list = 0\n        elif isinstance(entries, (int,long)) or is_Element(entries):\n                                                         ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:165:58: undeclared name not builtin: is_Element\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n                raise TypeError, \"unable to coerce entry to a p-adic\"\n            is_list = 0\n        elif isinstance(entries, tuple) and len(entries) == 4 and entries[3] is None: # The None entry is a flag to use this constructor\n            # Format is (int_matrix, valbase, prec_info, valaddeds, \n            #First we fill the _value_matrix with values from entries[0]\n            self._value_matrix = Matrix_integer_dense(MatrixSpace(ZZ, self._nrows, self._ncols), entries[0], copy=copy, coerce = coerce)\n                                                                ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:175:65: undeclared name not builtin: MatrixSpace\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n                #Use precision_cap of base_ring\n                self._comp_valaddeds()\n                self._adjust_prec_info_global(infinity, self._base_ring.precision_cap())\n                self._initialized = True\n                return\n            elif isinstance(entries[1], (int, long)) or is_Element(entries[1]):\n                                                                 ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:185:66: undeclared name not builtin: is_Element\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n                    except TypeError:\n                        self._initialized = False\n                        raise TypeError, \"unable to create an integer out of desired precision\"\n                if alist:\n                    if blist:\n                        self._adjust_prec_info_local_local(a, b, coerce)\n                                                         ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:219:58: Call with wrong number of arguments (expected 3, got 4)\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n                        raise TypeError, \"unable to create an integer out of desired precision\"\n                if alist:\n                    if blist:\n                        self._adjust_prec_info_local_local(a, b, coerce)\n                    else:\n                        self._adjust_prec_info_local_global(a, min(b, self._base_ring.precision_cap()), coerce)\n                                                          ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:221:59: Call with wrong number of arguments (expected 3, got 4)\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n                        self._adjust_prec_info_local_local(a, b, coerce)\n                    else:\n                        self._adjust_prec_info_local_global(a, min(b, self._base_ring.precision_cap()), coerce)\n                else:\n                    if blist:\n                        self._adjust_prec_info_global_local(a, b, coerce)\n                                                          ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:224:59: Call with wrong number of arguments (expected 3, got 4)\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n                raise TypeError, \"entries has the wrong length\"\n            if coerce:\n                # How do I declare a list in Pyrex?\n                coerced_list = [self.base_ring()(e) for e in entries]\n                self._valbase = min([e.valuation() for e in coerced_list]) #should eventually not make this a list before passing to min\n                self._value_matrix = Matrix_integer_dense(MatrixSpace(ZZ, self._nrows, self._ncols), 0, copy = False, coerce = True)\n\n\n                                                                    ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:252:69: undeclared name not builtin: MatrixSpace\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        if val is None:\n            self._valbase = Integer(0)\n        else:\n            self._valbase = val\n        if precs:\n            self._relprecs = [infinity] * (self._nrows * self._ncols)\n                                       ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:322:40: Cannot convert Python object to 'matrix_padic_capped_relative_dense.ulong *'\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        \"\"\"\n        cdef Integer a\n        cdef Integer b, c # should eventually be an unsigned long int\n        cdef Integer ppow\n        cdef Py_ssize_t i, j\n        if PyTupleCheck(value):\n                      ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:357:23: undeclared name not builtin: PyTupleCheck\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n            self._value_matrix.set_unsafe(i, j, a)\n            self._value_matrix.reduce_entry_unsafe(i, j, self._base_ring.prime_pow(c))\n            self._relprec_mat[i][j] =  mpz_get_ui(c.value)\n        else:\n            #d = self._base_ring(value)\n            a = <Integer> d._unit_part().lift()\n                          ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:365:27: undeclared name not builtin: d\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n            self._value_matrix.reduce_entry_unsafe(i, j, self._base_ring.prime_pow(c))\n            self._relprec_mat[i][j] =  mpz_get_ui(c.value)\n        else:\n            #d = self._base_ring(value)\n            a = <Integer> d._unit_part().lift()\n            b = <Integer> d.valuation() - self._valbase\n                          ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:366:27: undeclared name not builtin: d\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n            self._relprec_mat[i][j] =  mpz_get_ui(c.value)\n        else:\n            #d = self._base_ring(value)\n            a = <Integer> d._unit_part().lift()\n            b = <Integer> d.valuation() - self._valbase\n            c = <Integer> d.precision_absolute() - self._valbase\n                          ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:367:27: undeclared name not builtin: d\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n            return self.fetch('list')[n]\n        if not self._valaddeds.has_key(n):\n            m = self._value_matrix.get_unsafe(i, j)\n            self._valaddeds[n] = m.valuation()\n        relprec = self._relprecs[n] - self._valaddeds[n]\n        return pAdicCappedRelativeElement(self._base_ring, (self._valbase + self._valaddeds[n], Mod(self._value_matrix.get_unsafe(i, j) // self._base_ring.prime_pow(self._valaddeds[n]), self._base_ring.prime_pow(relprec)), relprec), construct = True)\n                                                                                                  ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:407:99: undeclared name not builtin: Mod\n\n\ncython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o matrix_padic_capped_relative_dense.c\n```\n\n```\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\ncimport matrix_pid_sparse\n       ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_sparse.pxd:1:8: 'matrix_pid_sparse.pxd' not found\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\ncdef class Matrix_field_sparse(matrix_pid_sparse.Matrix_pid_sparse):\n    ^\n------------------------------------------------------------\n\n/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_sparse.pxd:3:5: 'Matrix_pid_sparse' is not declared\n\n\ncython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o matrix_cyclo_sparse.c matrix_cyclo_sparse.pyx\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2486\n\n",
    "closed_at": "2008-03-14T22:35:07Z",
    "created_at": "2008-03-12T09:27:44Z",
    "labels": [
        "component: linear algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, positive review] remove unused/broken vector and matrix pyx files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2486",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @garyfurnish

This file does not compile with cython currently but is in the tree.  It is currently disabled in setup.py and should be removed or fixed.  This is a significant priority as it makes the development of efficient(parallel) build systems problematic and wastes space, especially for files which have not been touched in ages. Code that does not build should not be in the main repository.

```
Error converting Pyrex file to C:
------------------------------------------------------------
...
cimport matrix_pid_sparse
       ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_sparse.pxd:1:8: 'matrix_pid_sparse.pxd' not found

Error converting Pyrex file to C:
------------------------------------------------------------
...

cdef class Matrix_field_sparse(matrix_pid_sparse.Matrix_pid_sparse):
    ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_sparse.pxd:3:5: 'Matrix_pid_sparse' is not declared


cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o matrix_field_sparse.c matrix_field_sparse.pyx
```

```

Error converting Pyrex file to C:
------------------------------------------------------------
...
cimport matrix_pid_sparse
       ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_sparse.pxd:1:8: 'matrix_pid_sparse.pxd' not found

Error converting Pyrex file to C:
------------------------------------------------------------
...

cdef class Matrix_field_sparse(matrix_pid_sparse.Matrix_pid_sparse):
    ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_sparse.pxd:3:5: 'Matrix_pid_sparse' is not declared


cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o matrix_cyclo_dense.c matrix_cyclo_dense.pyx
```

```
Error converting Pyrex file to C:
------------------------------------------------------------
...
#  The full text of the GPL is available at:
#
#                  http://www.gnu.org/licenses/
#*****************************************************************************

include 'interrupt.pxi'
^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/rings/mpc.pyx:27:0: 'interrupt.pxi' not found


cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o mpc.c mpc.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...
       ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_dense.pyx:5:8: 'matrix_pid_dense.pxd' not found

Error converting Pyrex file to C:
------------------------------------------------------------
...

from sage.rings.finite_field import is_FiniteField
from sage.rings.integer_mod_ring import is_IntegerModRing


cdef class Matrix_field_dense(matrix_pid_dense.Matrix_pid_dense):
    ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_dense.pyx:17:5: 'Matrix_pid_dense' is not declared

Error converting Pyrex file to C:
------------------------------------------------------------
...
            [          1           5       z - 1]
            sage: print A.denominator()
            3
        """
        if self.nrows() == 0 or self.ncols() == 0:
            return integer.Integer(1)
                         ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_dense.pyx:202:26: undeclared name not builtin: integer

Error converting Pyrex file to C:
------------------------------------------------------------
...
            R = range(n)
        else:
            R = [t]
        for i in R:
            tm = sage.misc.misc.verbose('applying berlekamp-massey')
            g = berlekamp_massey.berlekamp_massey(cols[i].list())
                               ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_dense.pyx:718:32: undeclared name not builtin: berlekamp_massey


cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o matrix_field_dense.c matrix_field_dense.pyx
```

```
Error converting Pyrex file to C:
------------------------------------------------------------
...
    ########################################################################
    #def __new__(self, parent, entries, copy, coerce):
    #    allocate memory
    #def __dealloc__(self):
    #    free memory
    def __richcmp__(Matrix self, right, int op):  # always need for mysterious reasons.
                          ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/template.pyx:29:27: Expected ')'


cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o template.c template.pyx
```

```
cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o totallyreal_data.c totallyreal_data.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ########################################################################
    #def __new__(self, parent, entries, copy, coerce):
    #    allocate memory
    #def __dealloc__(self):
    #    free memory
    def __richcmp__(Matrix self, right, int op):  # always need for mysterious reasons.
                          ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_RR_dense.pyx:28:27: Expected ')'


cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o matrix_RR_dense.c matrix_RR_dense.pyx
```

```
Error converting Pyrex file to C:
------------------------------------------------------------
...
    that *must* have been initialized using mpq_init.
    """
    if n >= v.degree:
        raise IndexError, "Index must be between 0 and %s."%(v.degree - 1)
    cdef Py_ssize_t m
    m = binary_search0(v.positions, v.num_nonzero, n)
                     ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/modules/vector_rational_sparse_c.pxi:150:22: undeclared name not builtin: binary_search0

Error converting Pyrex file to C:
------------------------------------------------------------
...
    cdef Py_ssize_t i, m, ins
    cdef Py_ssize_t m2, ins2
    cdef Py_ssize_t *pos
    cdef mpq_t *e

    m = binary_search(v.positions, v.num_nonzero, n, &ins)
                    ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/modules/vector_rational_sparse_c.pxi:185:21: undeclared name not builtin: binary_search

Error converting Pyrex file to C:
------------------------------------------------------------
...
                z = Rational(entries[i])
                mpq_set(self.v.entries[i], z.value)
                self.v.positions[i] = entries[i][0]

    def __dealloc__(self):
        clear_mpq_vector(&self.v)
                       ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/modules/vector_rational_sparse.pyx:39:24: undeclared name not builtin: clear_mpq_vector

Error converting Pyrex file to C:
------------------------------------------------------------
...

    def list(self):
        return mpq_vector_to_list(&self.v)

    cdef void rescale(self, mpq_t x):
        scale_mpq_vector(&self.v, x)
                       ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/modules/vector_rational_sparse.pyx:90:24: undeclared name not builtin: scale_mpq_vector

Error converting Pyrex file to C:
------------------------------------------------------------
...
        add_mpq_vector_init(&z1, &self.v, &other.v, ONE)
        mpq_clear(ONE)

        w = Vector_mpq(self.v.degree)
        z2 = &(w.v)
        clear_mpq_vector(z2)   # free memory wasted on allocated w
                       ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/modules/vector_rational_sparse.pyx:105:24: undeclared name not builtin: clear_mpq_vector

Error converting Pyrex file to C:
------------------------------------------------------------
...
        
        The sparcity is a bound on the number of nonzeros per row.
        """
        cdef int i
        for i from 0 <= i < sparcity:
            self[random.randrange(self.v.degree)] = random.randrange(1,bound)
                                                         ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/modules/vector_rational_sparse.pyx:150:58: undeclared name not builtin: random

Error converting Pyrex file to C:
------------------------------------------------------------
...
        
        The sparcity is a bound on the number of nonzeros per row.
        """
        cdef int i
        for i from 0 <= i < sparcity:
            self[random.randrange(self.v.degree)] = random.randrange(1,bound)
                      ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/modules/vector_rational_sparse.pyx:150:23: undeclared name not builtin: random


cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o vector_rational_sparse.c vector_rational_sparse.pyx
```

```
Error converting Pyrex file to C:
------------------------------------------------------------
...
            h = h ^ (i * hash(v[i]))
        h = h ^ self._value_matrix._hash()    
        self.cache('hash', h)
        return h

    cdef _comp_valaddeds(self):
        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:142:9: Signature not compatible with previous declaration

Error converting Pyrex file to C:
------------------------------------------------------------
...
            for i from 0 <= i < self._nrows:
                self._value_matrix.set_unsafe(i, i, xint)
                self._relprecs_mat[i][i] = xrprec
            self._initialized = True                    
            
    cdef void _comp_valaddeds(self):
        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:292:9: '_comp_valaddeds' already defined

Error converting Pyrex file to C:
------------------------------------------------------------
...
                n += 1

    cdef void _adjust_prec_info_global(self, RingElement absolute, RingElement relative):
        pass

    cdef void _adjust_prec_info_global_local(self, RingElement absolute, object relative, coerce):
        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:306:9: Signature not compatible with previous declaration

Error converting Pyrex file to C:
------------------------------------------------------------
...
        pass

    cdef void _adjust_prec_info_global_local(self, RingElement absolute, object relative, coerce):
        pass

    cdef void _adjust_prec_info_local_global(self, object absolute, RingElement relative, coerce):
        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:309:9: Signature not compatible with previous declaration

Error converting Pyrex file to C:
------------------------------------------------------------
...
        pass

    cdef void _adjust_prec_info_local_global(self, object absolute, RingElement relative, coerce):
        pass

    cdef void _adjust_prec_info_local_local(self, object absolute, object relative, coerce):
        ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:312:9: Signature not compatible with previous declaration

Error converting Pyrex file to C:
------------------------------------------------------------
...
        Matrix_dense.__init__(self, parent)
        self._nrows = parent.nrows()
        self._ncols = parent.ncols()
        # Allocate an array for the precisions of the elements
        _sig_on
        self._relprecs = <ulong *>sage_malloc(size_of(ulong) * (self._nrows * self._ncols))
                                                    ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:88:53: undeclared name not builtin: size_of

Error converting Pyrex file to C:
------------------------------------------------------------
...
        Matrix_dense.__init__(self, parent)
        self._nrows = parent.nrows()
        self._ncols = parent.ncols()
        # Allocate an array for the precisions of the elements
        _sig_on
        self._relprecs = <ulong *>sage_malloc(size_of(ulong) * (self._nrows * self._ncols))
                                                          ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:88:59: 'ulong' is not a constant, variable or function identifier

Error converting Pyrex file to C:
------------------------------------------------------------
...
        if not x is None: return x

        if not self._mutability._is_immutable:
            raise TypeError, "mutable matrices are unhashable"
        
        v = self._relprecs
               ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:131:16: Cannot convert 'matrix_padic_capped_relative_dense.ulong *' to Python object

Error converting Pyrex file to C:
------------------------------------------------------------
...
        self._valaddeds = {}

        if entries is None:
            x = self.base_ring()(0)
            is_list = 0
        elif isinstance(entries, (int,long)) or is_Element(entries):
                                                         ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:165:58: undeclared name not builtin: is_Element

Error converting Pyrex file to C:
------------------------------------------------------------
...
                raise TypeError, "unable to coerce entry to a p-adic"
            is_list = 0
        elif isinstance(entries, tuple) and len(entries) == 4 and entries[3] is None: # The None entry is a flag to use this constructor
            # Format is (int_matrix, valbase, prec_info, valaddeds, 
            #First we fill the _value_matrix with values from entries[0]
            self._value_matrix = Matrix_integer_dense(MatrixSpace(ZZ, self._nrows, self._ncols), entries[0], copy=copy, coerce = coerce)
                                                                ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:175:65: undeclared name not builtin: MatrixSpace

Error converting Pyrex file to C:
------------------------------------------------------------
...
                #Use precision_cap of base_ring
                self._comp_valaddeds()
                self._adjust_prec_info_global(infinity, self._base_ring.precision_cap())
                self._initialized = True
                return
            elif isinstance(entries[1], (int, long)) or is_Element(entries[1]):
                                                                 ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:185:66: undeclared name not builtin: is_Element

Error converting Pyrex file to C:
------------------------------------------------------------
...
                    except TypeError:
                        self._initialized = False
                        raise TypeError, "unable to create an integer out of desired precision"
                if alist:
                    if blist:
                        self._adjust_prec_info_local_local(a, b, coerce)
                                                         ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:219:58: Call with wrong number of arguments (expected 3, got 4)

Error converting Pyrex file to C:
------------------------------------------------------------
...
                        raise TypeError, "unable to create an integer out of desired precision"
                if alist:
                    if blist:
                        self._adjust_prec_info_local_local(a, b, coerce)
                    else:
                        self._adjust_prec_info_local_global(a, min(b, self._base_ring.precision_cap()), coerce)
                                                          ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:221:59: Call with wrong number of arguments (expected 3, got 4)

Error converting Pyrex file to C:
------------------------------------------------------------
...
                        self._adjust_prec_info_local_local(a, b, coerce)
                    else:
                        self._adjust_prec_info_local_global(a, min(b, self._base_ring.precision_cap()), coerce)
                else:
                    if blist:
                        self._adjust_prec_info_global_local(a, b, coerce)
                                                          ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:224:59: Call with wrong number of arguments (expected 3, got 4)

Error converting Pyrex file to C:
------------------------------------------------------------
...
                raise TypeError, "entries has the wrong length"
            if coerce:
                # How do I declare a list in Pyrex?
                coerced_list = [self.base_ring()(e) for e in entries]
                self._valbase = min([e.valuation() for e in coerced_list]) #should eventually not make this a list before passing to min
                self._value_matrix = Matrix_integer_dense(MatrixSpace(ZZ, self._nrows, self._ncols), 0, copy = False, coerce = True)


                                                                    ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:252:69: undeclared name not builtin: MatrixSpace

Error converting Pyrex file to C:
------------------------------------------------------------
...
        if val is None:
            self._valbase = Integer(0)
        else:
            self._valbase = val
        if precs:
            self._relprecs = [infinity] * (self._nrows * self._ncols)
                                       ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:322:40: Cannot convert Python object to 'matrix_padic_capped_relative_dense.ulong *'

Error converting Pyrex file to C:
------------------------------------------------------------
...
        """
        cdef Integer a
        cdef Integer b, c # should eventually be an unsigned long int
        cdef Integer ppow
        cdef Py_ssize_t i, j
        if PyTupleCheck(value):
                      ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:357:23: undeclared name not builtin: PyTupleCheck

Error converting Pyrex file to C:
------------------------------------------------------------
...
            self._value_matrix.set_unsafe(i, j, a)
            self._value_matrix.reduce_entry_unsafe(i, j, self._base_ring.prime_pow(c))
            self._relprec_mat[i][j] =  mpz_get_ui(c.value)
        else:
            #d = self._base_ring(value)
            a = <Integer> d._unit_part().lift()
                          ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:365:27: undeclared name not builtin: d

Error converting Pyrex file to C:
------------------------------------------------------------
...
            self._value_matrix.reduce_entry_unsafe(i, j, self._base_ring.prime_pow(c))
            self._relprec_mat[i][j] =  mpz_get_ui(c.value)
        else:
            #d = self._base_ring(value)
            a = <Integer> d._unit_part().lift()
            b = <Integer> d.valuation() - self._valbase
                          ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:366:27: undeclared name not builtin: d

Error converting Pyrex file to C:
------------------------------------------------------------
...
            self._relprec_mat[i][j] =  mpz_get_ui(c.value)
        else:
            #d = self._base_ring(value)
            a = <Integer> d._unit_part().lift()
            b = <Integer> d.valuation() - self._valbase
            c = <Integer> d.precision_absolute() - self._valbase
                          ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:367:27: undeclared name not builtin: d

Error converting Pyrex file to C:
------------------------------------------------------------
...
            return self.fetch('list')[n]
        if not self._valaddeds.has_key(n):
            m = self._value_matrix.get_unsafe(i, j)
            self._valaddeds[n] = m.valuation()
        relprec = self._relprecs[n] - self._valaddeds[n]
        return pAdicCappedRelativeElement(self._base_ring, (self._valbase + self._valaddeds[n], Mod(self._value_matrix.get_unsafe(i, j) // self._base_ring.prime_pow(self._valaddeds[n]), self._base_ring.prime_pow(relprec)), relprec), construct = True)
                                                                                                  ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/padics/matrix_padic_capped_relative_dense.pyx:407:99: undeclared name not builtin: Mod


cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o matrix_padic_capped_relative_dense.c
```

```
Error converting Pyrex file to C:
------------------------------------------------------------
...
cimport matrix_pid_sparse
       ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_sparse.pxd:1:8: 'matrix_pid_sparse.pxd' not found

Error converting Pyrex file to C:
------------------------------------------------------------
...

cdef class Matrix_field_sparse(matrix_pid_sparse.Matrix_pid_sparse):
    ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/matrix/matrix_field_sparse.pxd:3:5: 'Matrix_pid_sparse' is not declared


cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o matrix_cyclo_sparse.c matrix_cyclo_sparse.pyx
```

Issue created by migration from https://trac.sagemath.org/ticket/2486





---

archive/issue_comments_016809.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-13T01:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2486#issuecomment-16809",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016810.json:
```json
{
    "body": "Changing assignee from @williamstein to @garyfurnish.",
    "created_at": "2008-03-13T01:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2486#issuecomment-16810",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @williamstein to @garyfurnish.



---

archive/issue_comments_016811.json:
```json
{
    "body": "Adding the following:\n\n```\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n#  The full text of the GPL is available at:\n#\n#                  http://www.gnu.org/licenses/\n#*****************************************************************************\n\ninclude 'interrupt.pxi'\n^\n------------------------------------------------------------\n\n/home/x/build/sage-2.10.3/devel/sage-main/sage/rings/mpc.pyx:27:0: 'interrupt.pxi' not found\n\n\ncython -I/home/x/build/sage-2.10.3/devel/sage-main --incref-local-binop --embed-positions -o mpc.c mpc.pyx\n\n```",
    "created_at": "2008-03-13T02:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2486#issuecomment-16811",
    "user": "https://github.com/garyfurnish"
}
```

Adding the following:

```
Error converting Pyrex file to C:
------------------------------------------------------------
...
#  The full text of the GPL is available at:
#
#                  http://www.gnu.org/licenses/
#*****************************************************************************

include 'interrupt.pxi'
^
------------------------------------------------------------

/home/x/build/sage-2.10.3/devel/sage-main/sage/rings/mpc.pyx:27:0: 'interrupt.pxi' not found


cython -I/home/x/build/sage-2.10.3/devel/sage-main --incref-local-binop --embed-positions -o mpc.c mpc.pyx

```



---

archive/issue_comments_016812.json:
```json
{
    "body": "Attachment [trac_2486.patch](tarball://root/attachments/some-uuid/ticket2486/trac_2486.patch) by @garyfurnish created at 2008-03-13 02:10:32",
    "created_at": "2008-03-13T02:10:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2486#issuecomment-16812",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_2486.patch](tarball://root/attachments/some-uuid/ticket2486/trac_2486.patch) by @garyfurnish created at 2008-03-13 02:10:32



---

archive/issue_comments_016813.json:
```json
{
    "body": "`sage -ba` and a `-testall -long` works after applying this patch. I would suggest contacting the authors of the various files we remove \"just in case\".\n\nCheers,\n\nMichael",
    "created_at": "2008-03-13T07:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2486#issuecomment-16813",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

`sage -ba` and a `-testall -long` works after applying this patch. I would suggest contacting the authors of the various files we remove "just in case".

Cheers,

Michael



---

archive/issue_comments_016814.json:
```json
{
    "body": "You can delete the sage interface to mpc -- it turns out mpc sucks.\n\nI am VERY VERY hesistant for you to delete the matrix code.  Come up with\na way to keep it without deleting it, e.g., put it in a subdirectory that\ndoesn't have an __init__.py file (i.e., the same protocol python uses for\ndecided whether or not files get parsed at load time). \n\n\nI.e. make\n\n   devel/sage/sage/matrix/inactive/\n\nand put those .pyx files there and don't put __init__.py in inactive.",
    "created_at": "2008-03-13T17:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2486#issuecomment-16814",
    "user": "https://github.com/williamstein"
}
```

You can delete the sage interface to mpc -- it turns out mpc sucks.

I am VERY VERY hesistant for you to delete the matrix code.  Come up with
a way to keep it without deleting it, e.g., put it in a subdirectory that
doesn't have an __init__.py file (i.e., the same protocol python uses for
decided whether or not files get parsed at load time). 


I.e. make

   devel/sage/sage/matrix/inactive/

and put those .pyx files there and don't put __init__.py in inactive.



---

archive/issue_comments_016815.json:
```json
{
    "body": "```\n[23:00] <mabshoff> wstein: you are fine with the code removal by gfurnish?\n[23:00] <mabshoff> Then I will apply those patches now. \n[23:00] <wstein> yes\n```",
    "created_at": "2008-03-14T22:28:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2486#issuecomment-16815",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

```
[23:00] <mabshoff> wstein: you are fine with the code removal by gfurnish?
[23:00] <mabshoff> Then I will apply those patches now. 
[23:00] <wstein> yes
```



---

archive/issue_events_005864.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-14T22:35:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2486",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2486#event-5864"
}
```



---

archive/issue_comments_016816.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T22:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2486#issuecomment-16816",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016817.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T22:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2486#issuecomment-16817",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
