# Issue 3113: Major segfault related to modular symbols and pickling

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-06 20:14:27

Assignee: craigcitro

CC:  wjp


```
DATA = '/tmp'
def ranks(N):
    filename = '%sranks-%s.sobj'%(DATA,N)
    if os.path.exists(filename):
         D = load(filename)
    else:
         D = ModularSymbols(N,sign=1).cuspidal_submodule().new_submodule().decomposition()
    for i,A in enumerate(D):
        eps = -A.atkin_lehner_operator().matrix()[0,0]
        winding_element = A.rational_period_mapping()(A.ambient_module()([0,oo]))
        print N, i, eps, winding_element == 0
    save(D, filename)

```


then


```
sage: ranks(11)
11 0 1 False
sage: ranks(11)
BOOM!
```


GDB gives

```
sage: ranks(11)

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_PROTECTION_FAILURE at address: 0x00000001
0x0077231c in __gmpn_gcd_1 ()
(gdb) bt
#0  0x0077231c in __gmpn_gcd_1 ()
#1  0x0075ba88 in __gmpz_gcd ()
Cannot access memory at address 0x5
(gdb) The program is running.  Exit anyway? (y or n) lo^H^H
Please answer y or n.
```



---

Comment by mabshoff created at 2008-05-06 20:28:29

This throws an error for me the first time around:

```
sage: ranks(11)
11 0 1 False
---------------------------------------------------------------------------
<type 'exceptions.IOError'>               Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/<ipython console> in ranks(N)

/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/sage_object.pyx in sage.structure.sage_object.save (sage/structure/sage_object.c:4720)()

/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/sage_object.pyx in sage.structure.sage_object.SageObject.save (sage/structure/sage_object.c:1213)()

<type 'exceptions.IOError'>: [Errno 13] Permission denied: '/tmpranks-11.sobj'
sage: ranks(11)
```

But with some slight fix I also get a crash:

```
sage: DATA = '/tmp/'
sage: def ranks(N):
....:         filename = '%sranks-%s.sobj'%(DATA,N)
....:     if os.path.exists(filename):
....:              D = load(filename)
....:     else:
....:              D = ModularSymbols(N,sign=1).cuspidal_submodule().new_submodule().decomposition()
....:     for i,A in enumerate(D):
....:             eps = -A.atkin_lehner_operator().matrix()[0,0]
....:         winding_element = A.rational_period_mapping()(A.ambient_module()([0,oo]))
....:         print N, i, eps, winding_element == 0
....:     save(D, filename)
....:
sage: ranks(11)
11 0 1 False
sage: ranks(11)
*** glibc detected *** realloc(): invalid size: 0x00007fffef1a3ba0 ***
/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/bin/sage-sage: line 214: 15662 Aborted                 sage-ipython "$`@`" -c "$SAGE_STARTUP_COMMAND;"
```

Poking around!

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-06 22:48:33

More info:

```
DATA = '/tmp/'
def ranks(N):
    filename = '%sranks-%s.sobj'%(DATA,N)
    if os.path.exists(filename):
         print "loaded pickled object"
         D = load(filename)
    else:
         print "computing modular symbol"
         D = ModularSymbols(N,sign=1).cuspidal_submodule().new_submodule().decomposition()
    for i,A in enumerate(D):
        print "foo"
        eps = -A.atkin_lehner_operator().matrix()[0,0]
        print "bar"
        winding_element = A.rational_period_mapping()(A.ambient_module()([0,oo]))
        print "baz"
        print N, i, eps, winding_element == 0
    save(D, filename)
```

With that I get:

```
sage: ranks(11)
computing modular symbol
foo
bar
baz
11 0 1 False
sage: ranks(11)
loaded pickled object
foo
bar
*** glibc detected *** realloc(): invalid size: 0x00007fffa25d3f90 ***
/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/bin/sage-sage: line 214: 12788 Aborted                 sage-ipython "$`@`" -c "$SAGE_STARTUP_COMMAND;"
```

wjp saw the following under valgrind:

```
Invalid free() / delete / delete[]
==10368==    at 0x4C210F2: realloc (in /usr/lib64/valgrind/amd64-linux/vgpreload_memcheck.so)
==10368==    by 0x925C230: __gmpz_realloc (in /data/sage/sage-3.0.rc0/local/lib/libgmp.so.3.4.1)
==10368==    by 0x92550DE: __gmpz_gcd (in /data/sage/sage-3.0.rc0/local/lib/libgmp.so.3.4.1)
==10368==    by 0x925F796: __gmpq_aors (in /data/sage/sage-3.0.rc0/local/lib/libgmp.so.3.4.1)
==10368==    by 0x25B2D153: __pyx_f_4sage_6matrix_21matrix_rational_dense_21Matrix_rational_dense__vector_times_matrix_c_impl (matrix_rational_dense.c:5570)
==10368==    by 0x2F0EEC19: __pyx_f_4sage_6matrix_6action_18VectorMatrixAction__call_c_impl (action.c:2903)
==10368==    by 0xEE8208B: __pyx_f_4sage_10categories_6action_6Action__call_c (action.c:1684)
==10368==    by 0xEC61415: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_bin_op_c (coerce.c:5018)
==10368==    by 0xE7E180A: __pyx_pf_4sage_9structure_7element_6Vector___mul__ (element.c:10413)
==10368==    by 0x417FDC: binary_op1 (abstract.c:398)
==10368==    by 0x41B717: PyNumber_Multiply (abstract.c:669)
==10368==    by 0x48463C: PyEval_EvalFrameEx (ceval.c:1073)
==10368==  Address 0x7feffd4b0 is on thread 1's stack
==10368== 
==10368== Invalid write of size 8
==10368==    at 0x9254E04: __gmpz_gcd (in /data/sage/sage-3.0.rc0/local/lib/libgmp.so.3.4.1)
==10368==    by 0x925F796: __gmpq_aors (in /data/sage/sage-3.0.rc0/local/lib/libgmp.so.3.4.1)
==10368==    by 0x25B2D153: __pyx_f_4sage_6matrix_21matrix_rational_dense_21Matrix_rational_dense__vector_times_matrix_c_impl (matrix_rational_dense.c:5570)
==10368==    by 0x2F0EEC19: __pyx_f_4sage_6matrix_6action_18VectorMatrixAction__call_c_impl (action.c:2903)
==10368==    by 0xEE8208B: __pyx_f_4sage_10categories_6action_6Action__call_c (action.c:1684)
==10368==    by 0xEC61415: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_bin_op_c (coerce.c:5018)
==10368==    by 0xE7E180A: __pyx_pf_4sage_9structure_7element_6Vector___mul__ (element.c:10413)
==10368==    by 0x417FDC: binary_op1 (abstract.c:398)
==10368==    by 0x41B717: PyNumber_Multiply (abstract.c:669)
==10368==    by 0x48463C: PyEval_EvalFrameEx (ceval.c:1073)
==10368==    by 0x4886B1: PyEval_EvalCodeEx (ceval.c:2836)
==10368==    by 0x4D1E17: function_call (funcobject.c:517)
==10368==  Address 0x0 is not stack'd, malloc'd or (recently) free'd
```

And:

```
[23:50] <mabshoff|zzz> wstein|afk: around?
[23:50] <mabshoff|zzz> #3113 is quite odd to say the least.
[23:50] <mabshoff|zzz> It valgrinds clean, but it either crashes on the first load or not at all it seems.
[23:55] <wjp> I'm getting what appears to be a realloc() of stack memory in valgrind
[23:55] <mabshoff|zzz> wjp: where?
[23:55] <wjp> sec
[23:55] <mabshoff|zzz> It seems to crash every time on OSX 10.5
[23:55] <mabshoff|zzz> But on sage.math it is harder to hit.
[23:56] <wjp> http://www.math.leidenuniv.nl/~wpalenst/sage/3113.valgrind
[23:57] <mabshoff|zzz> ok, I didn't see that at all.
[23:57] <wjp> oh, this is with 3.0.rc0, by the way
[23:57] * wjp should build 3.0.1 at home
[23:59] <mabshoff|zzz> mmh, that corresponds to "mpq_mul(y, w._entries[j], self._matrix[j][i])"
[23:59] <mabshoff|zzz> wjp: I doubt that matters.
[00:00] <wjp> still thought I'd mention it just in case :-)
[00:00] <mabshoff|zzz> :)
[00:00] <wjp> (and for line numbers and such)
[00:00] <mabshoff|zzz> Maybe the pickling is broken
[00:00] <mabshoff|zzz> Otherwise I can't imagine what goes wrong there.
[00:00] <wjp> if it's trying to realloc stack memory, it sounds like the unpickling may be allocating things the wrong way?
[00:01] <mabshoff|zzz> alignment comes to mind.
[00:04] <mabshoff|zzz> wjp: what goes boom is "winding_element = A.rational_period_mapping()(A.ambient_module()([0,oo]))"
[00:04] <wjp> hm, it only seems to crash here if I save and load in the same session
[00:05] <mabshoff|zzz> yep
[00:05] <mabshoff|zzz> When I do not deleted the pickled objects it seems fine.
```


Cheers,

Michael


---

Comment by was created at 2008-05-06 23:42:55

This is a problem in the automatic coercion model code that dispatches how "vector times matrix" is done. To see this:

1. Add print statements in matrix_rational_dense.pyx

```
    cdef Vector _vector_times_matrix_c_impl(self, Vector v):
...

        print "Input: v = ", v
        print "type(v) = ", type(v)
```


2. Run the example (after deleting /tmp/*.sobj!!):


```

sage: DATA = '/tmp/'
sage: def ranks(N):
....:         filename = '%sranks-%s.sobj'%(DATA,N)
....:     if os.path.exists(filename):
....:              D = load(filename)
....:     else:
....:              D = ModularSymbols(N,sign=1).cuspidal_submodule().new_submodule().decomposition()
....:     for i,A in enumerate(D):
....:             eps = -A.atkin_lehner_operator().matrix()[0,0]
....:         winding_element = A.rational_period_mapping()(A.ambient_module()([0,oo]))
....:         print N, i, eps, winding_element == 0
....:     save(D, filename)
....: 
sage: 

sage: ranks(11)
Input: v =  (0, 1)
type(v) =  <type 'sage.modules.vector_rational_dense.Vector_rational_dense'>
Input: v =  (0, 1)
type(v) =  <type 'sage.modules.vector_rational_dense.Vector_rational_dense'>
Input: v =  (-1, 0)
type(v) =  <type 'sage.modules.vector_rational_dense.Vector_rational_dense'>
11 0 1 False
sage: ranks(11)
Input: v =  (-1, 0)
type(v) =  <type 'sage.modules.free_module_element.FreeModuleElement_generic_sparse'>


------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

```



---

Comment by was created at 2008-05-07 00:07:38

This is caused by matrix action caching code and the facts that:

   1. sparse and dense matrix spaces of the same dimension and degree are considered "equal" in sage.

   2. And pickle/unpickle happens to change something from dense to sparse.

Certainly 2 is weird and is probably very specifically caused by a mistake in some pure python code for modular symbols.  But it shouldn't result in segfaults.

If one add 4 lines to modules/free_module.py to make it so modular symbols spaces are *not* equal if one is sparse and one is dense, then the problem completely disappears. 

Here's the diff that would do that:

```
diff -r 0a4213d9da78 sage/modules/free_module.py
--- a/sage/modules/free_module.py       Tue May 06 10:12:53 2008 -0700
+++ b/sage/modules/free_module.py       Tue May 06 17:06:36 2008 -0700
`@``@` -2784,6 +2784,8 `@``@` class FreeModule_ambient(FreeModule_gene
         if not isinstance(other, FreeModule_generic):
             return cmp(type(self), type(other))
         if isinstance(other, FreeModule_ambient):
+            c = cmp(self.is_sparse(), other.is_sparse())
+            if c: return c
             c = cmp(self.rank(), other.rank())
             if c: return c
             c = cmp(self.base_ring(), other.base_ring())
`@``@` -3344,6 +3346,8 `@``@` class FreeModule_submodule_with_basis_pi
             return 0
         if not isinstance(other, FreeModule_generic):
             return cmp(type(self), type(other))
+        c = cmp(self.is_sparse(), other.is_sparse())
+        if c: return c
         c = cmp(self.ambient_vector_space(), other.ambient_vector_space())
         if c: return c
         c = cmp(self.dimension(), other.dimension())
```


I will leave it to Robert Bradshaw to decide what to do.  Probably the right solution is
that sparse and dense vector spaces do not compare to be equal no matter what.  Hmmm. 
Thoughts?


---

Comment by robertwb created at 2008-05-07 00:52:41

Probably we shouldn't be using dictionaries (that compare with equals) to cache this information. There should also be a check. The coercion model itself uses a custom dictionary that keys on the object pointer, but the caching in the class itself is done via standard Python dicts. There should be a check at the very least--I'll write a patch to do that.


---

Attachment


---

Comment by robertwb created at 2008-05-07 06:20:07

It now adds an extra check to make sure coercion is performed when parents are equal but not unique for actions.


---

Comment by craigcitro created at 2008-05-10 09:35:41

Patch looks reasonable, but this creates a doctest failure in `sage/coding/linear_code.py`. The `__eq__` code there could probably be improved, but the error seems to be coming up in some sort of internal consistency check with the coercion model. I'm voting to kick this back to robertwb to think about, since he's the expert. 

Here's the doctest failure:


```
sage -t  devel/sage-ref/sage/coding/linear_code.py          **********************************************************************
File "/sage/tmp/linear_code.py", line 139:
    age: C == loads(dumps(C))
Exception raised:
    Traceback (most recent call last):
      File "/sage/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[13]>", line 1, in <module>
        C == loads(dumps(C))###line 139:
    age: C == loads(dumps(C))
      File "/sage/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 984, in __eq__
        if scheck*c:
      File "element.pyx", line 2122, in sage.structure.element.Matrix.__mul__ (sage/structure/element.c:11352)
      File "coerce.pyx", line 267, in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5039)
      File "coerce.pyx", line 527, in sage.structure.coerce.CoercionModel_cache_maps.get_action_c (sage/structure/coerce.c:7876)
      File "coerce.pyx", line 574, in sage.structure.coerce.CoercionModel_cache_maps.verify_action (sage/structure/coerce.c:8379)
    RuntimeError: There is a BUG in the coercion model:
                    Action found for R <built-in function mul> S does not have the correct domains
                    R = Full MatrixSpace of 3 by 7 dense matrices over Finite Field of size 2 
                    S = Vector space of dimension 7 over Finite Field of size 2
                    (should be Full MatrixSpace of 3 by 7 dense matrices over Finite Field of size 2, Vector space of dimension 7 over Finite Field of size 2)
                    action = Left action by Full MatrixSpace of 3 by 7 dense matrices over Finite Field of size 2 on Vector space of dimension 7 over Finite Field of size 2 (<type 'sage.categories.action.PrecomposedAction'>)
                    
**********************************************************************

```


Negative review until this gets corrected, but will be happy to give a positive once this is in order ...


---

Comment by was created at 2008-05-16 14:10:52

Changing priority from major to blocker.


---

Attachment


---

Comment by craigcitro created at 2008-06-15 05:36:06

Attached patch fixes the last small problem -- somewhere there was a `left` instead of `right`.


---

Comment by robertwb created at 2008-06-15 06:03:13

Dyslexia strikes again! This is the right fix.


---

Comment by mabshoff created at 2008-06-15 08:27:20

Merged in Sage 3.0.3.rc0


---

Comment by mabshoff created at 2008-06-15 08:27:20

Resolution: fixed
