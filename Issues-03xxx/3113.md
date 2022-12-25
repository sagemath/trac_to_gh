# Issue 3113: [with patch, with positive review] Major segfault related to modular symbols and pickling

archive/issues_003113.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @wjp\n\n```\nDATA = '/tmp/'\ndef ranks(N):\n    filename = '%sranks-%s.sobj'%(DATA,N)\n    if os.path.exists(filename):\n         D = load(filename)\n    else:\n         D = ModularSymbols(N,sign=1).cuspidal_submodule().new_submodule().decomposition()\n    for i,A in enumerate(D):\n        eps = -A.atkin_lehner_operator().matrix()[0,0]\n        winding_element = A.rational_period_mapping()(A.ambient_module()([0,oo]))\n        print N, i, eps, winding_element == 0\n    save(D, filename)\n\n```\n\nthen\n\n```\nsage: ranks(11)\n11 0 1 False\nsage: ranks(11)\nBOOM!\n```\n\nGDB gives\n\n```\nsage: ranks(11)\n\nProgram received signal EXC_BAD_ACCESS, Could not access memory.\nReason: KERN_PROTECTION_FAILURE at address: 0x00000001\n0x0077231c in __gmpn_gcd_1 ()\n(gdb) bt\n#0  0x0077231c in __gmpn_gcd_1 ()\n#1  0x0075ba88 in __gmpz_gcd ()\nCannot access memory at address 0x5\n(gdb) The program is running.  Exit anyway? (y or n) lo^H^H\nPlease answer y or n.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3113\n\n",
    "closed_at": "2008-06-15T08:27:20Z",
    "created_at": "2008-05-06T20:14:27Z",
    "labels": [
        "component: modular forms",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch, with positive review] Major segfault related to modular symbols and pickling",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3113",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro

CC:  @wjp

```
DATA = '/tmp/'
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

Issue created by migration from https://trac.sagemath.org/ticket/3113





---

archive/issue_comments_021505.json:
```json
{
    "body": "This throws an error for me the first time around:\n\n```\nsage: ranks(11)\n11 0 1 False\n---------------------------------------------------------------------------\n<type 'exceptions.IOError'>               Traceback (most recent call last)\n\n/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/<ipython console> in <module>()\n\n/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/<ipython console> in ranks(N)\n\n/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/sage_object.pyx in sage.structure.sage_object.save (sage/structure/sage_object.c:4720)()\n\n/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/sage_object.pyx in sage.structure.sage_object.SageObject.save (sage/structure/sage_object.c:1213)()\n\n<type 'exceptions.IOError'>: [Errno 13] Permission denied: '/tmpranks-11.sobj'\nsage: ranks(11)\n```\nBut with some slight fix I also get a crash:\n\n```\nsage: DATA = '/tmp/'\nsage: def ranks(N):\n....:         filename = '%sranks-%s.sobj'%(DATA,N)\n....:     if os.path.exists(filename):\n....:              D = load(filename)\n....:     else:\n....:              D = ModularSymbols(N,sign=1).cuspidal_submodule().new_submodule().decomposition()\n....:     for i,A in enumerate(D):\n....:             eps = -A.atkin_lehner_operator().matrix()[0,0]\n....:         winding_element = A.rational_period_mapping()(A.ambient_module()([0,oo]))\n....:         print N, i, eps, winding_element == 0\n....:     save(D, filename)\n....:\nsage: ranks(11)\n11 0 1 False\nsage: ranks(11)\n*** glibc detected *** realloc(): invalid size: 0x00007fffef1a3ba0 ***\n/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/bin/sage-sage: line 214: 15662 Aborted                 sage-ipython \"$@\" -c \"$SAGE_STARTUP_COMMAND;\"\n```\nPoking around!\n\nCheers,\n\nMichael",
    "created_at": "2008-05-06T20:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3113#issuecomment-21505",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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
/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/bin/sage-sage: line 214: 15662 Aborted                 sage-ipython "$@" -c "$SAGE_STARTUP_COMMAND;"
```
Poking around!

Cheers,

Michael



---

archive/issue_comments_021506.json:
```json
{
    "body": "More info:\n\n```\nDATA = '/tmp/'\ndef ranks(N):\n    filename = '%sranks-%s.sobj'%(DATA,N)\n    if os.path.exists(filename):\n         print \"loaded pickled object\"\n         D = load(filename)\n    else:\n         print \"computing modular symbol\"\n         D = ModularSymbols(N,sign=1).cuspidal_submodule().new_submodule().decomposition()\n    for i,A in enumerate(D):\n        print \"foo\"\n        eps = -A.atkin_lehner_operator().matrix()[0,0]\n        print \"bar\"\n        winding_element = A.rational_period_mapping()(A.ambient_module()([0,oo]))\n        print \"baz\"\n        print N, i, eps, winding_element == 0\n    save(D, filename)\n```\nWith that I get:\n\n```\nsage: ranks(11)\ncomputing modular symbol\nfoo\nbar\nbaz\n11 0 1 False\nsage: ranks(11)\nloaded pickled object\nfoo\nbar\n*** glibc detected *** realloc(): invalid size: 0x00007fffa25d3f90 ***\n/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/bin/sage-sage: line 214: 12788 Aborted                 sage-ipython \"$@\" -c \"$SAGE_STARTUP_COMMAND;\"\n```\nwjp saw the following under valgrind:\n\n```\nInvalid free() / delete / delete[]\n==10368==    at 0x4C210F2: realloc (in /usr/lib64/valgrind/amd64-linux/vgpreload_memcheck.so)\n==10368==    by 0x925C230: __gmpz_realloc (in /data/sage/sage-3.0.rc0/local/lib/libgmp.so.3.4.1)\n==10368==    by 0x92550DE: __gmpz_gcd (in /data/sage/sage-3.0.rc0/local/lib/libgmp.so.3.4.1)\n==10368==    by 0x925F796: __gmpq_aors (in /data/sage/sage-3.0.rc0/local/lib/libgmp.so.3.4.1)\n==10368==    by 0x25B2D153: __pyx_f_4sage_6matrix_21matrix_rational_dense_21Matrix_rational_dense__vector_times_matrix_c_impl (matrix_rational_dense.c:5570)\n==10368==    by 0x2F0EEC19: __pyx_f_4sage_6matrix_6action_18VectorMatrixAction__call_c_impl (action.c:2903)\n==10368==    by 0xEE8208B: __pyx_f_4sage_10categories_6action_6Action__call_c (action.c:1684)\n==10368==    by 0xEC61415: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_bin_op_c (coerce.c:5018)\n==10368==    by 0xE7E180A: __pyx_pf_4sage_9structure_7element_6Vector___mul__ (element.c:10413)\n==10368==    by 0x417FDC: binary_op1 (abstract.c:398)\n==10368==    by 0x41B717: PyNumber_Multiply (abstract.c:669)\n==10368==    by 0x48463C: PyEval_EvalFrameEx (ceval.c:1073)\n==10368==  Address 0x7feffd4b0 is on thread 1's stack\n==10368== \n==10368== Invalid write of size 8\n==10368==    at 0x9254E04: __gmpz_gcd (in /data/sage/sage-3.0.rc0/local/lib/libgmp.so.3.4.1)\n==10368==    by 0x925F796: __gmpq_aors (in /data/sage/sage-3.0.rc0/local/lib/libgmp.so.3.4.1)\n==10368==    by 0x25B2D153: __pyx_f_4sage_6matrix_21matrix_rational_dense_21Matrix_rational_dense__vector_times_matrix_c_impl (matrix_rational_dense.c:5570)\n==10368==    by 0x2F0EEC19: __pyx_f_4sage_6matrix_6action_18VectorMatrixAction__call_c_impl (action.c:2903)\n==10368==    by 0xEE8208B: __pyx_f_4sage_10categories_6action_6Action__call_c (action.c:1684)\n==10368==    by 0xEC61415: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_bin_op_c (coerce.c:5018)\n==10368==    by 0xE7E180A: __pyx_pf_4sage_9structure_7element_6Vector___mul__ (element.c:10413)\n==10368==    by 0x417FDC: binary_op1 (abstract.c:398)\n==10368==    by 0x41B717: PyNumber_Multiply (abstract.c:669)\n==10368==    by 0x48463C: PyEval_EvalFrameEx (ceval.c:1073)\n==10368==    by 0x4886B1: PyEval_EvalCodeEx (ceval.c:2836)\n==10368==    by 0x4D1E17: function_call (funcobject.c:517)\n==10368==  Address 0x0 is not stack'd, malloc'd or (recently) free'd\n```\nAnd:\n\n```\n[23:50] <mabshoff|zzz> wstein|afk: around?\n[23:50] <mabshoff|zzz> #3113 is quite odd to say the least.\n[23:50] <mabshoff|zzz> It valgrinds clean, but it either crashes on the first load or not at all it seems.\n[23:55] <wjp> I'm getting what appears to be a realloc() of stack memory in valgrind\n[23:55] <mabshoff|zzz> wjp: where?\n[23:55] <wjp> sec\n[23:55] <mabshoff|zzz> It seems to crash every time on OSX 10.5\n[23:55] <mabshoff|zzz> But on sage.math it is harder to hit.\n[23:56] <wjp> http://www.math.leidenuniv.nl/~wpalenst/sage/3113.valgrind\n[23:57] <mabshoff|zzz> ok, I didn't see that at all.\n[23:57] <wjp> oh, this is with 3.0.rc0, by the way\n[23:57] * wjp should build 3.0.1 at home\n[23:59] <mabshoff|zzz> mmh, that corresponds to \"mpq_mul(y, w._entries[j], self._matrix[j][i])\"\n[23:59] <mabshoff|zzz> wjp: I doubt that matters.\n[00:00] <wjp> still thought I'd mention it just in case :-)\n[00:00] <mabshoff|zzz> :)\n[00:00] <wjp> (and for line numbers and such)\n[00:00] <mabshoff|zzz> Maybe the pickling is broken\n[00:00] <mabshoff|zzz> Otherwise I can't imagine what goes wrong there.\n[00:00] <wjp> if it's trying to realloc stack memory, it sounds like the unpickling may be allocating things the wrong way?\n[00:01] <mabshoff|zzz> alignment comes to mind.\n[00:04] <mabshoff|zzz> wjp: what goes boom is \"winding_element = A.rational_period_mapping()(A.ambient_module()([0,oo]))\"\n[00:04] <wjp> hm, it only seems to crash here if I save and load in the same session\n[00:05] <mabshoff|zzz> yep\n[00:05] <mabshoff|zzz> When I do not deleted the pickled objects it seems fine.\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-05-06T22:48:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3113#issuecomment-21506",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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
/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/bin/sage-sage: line 214: 12788 Aborted                 sage-ipython "$@" -c "$SAGE_STARTUP_COMMAND;"
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

archive/issue_comments_021507.json:
```json
{
    "body": "This is a problem in the automatic coercion model code that dispatches how \"vector times matrix\" is done. To see this:\n\n1. Add print statements in matrix_rational_dense.pyx\n\n```\n    cdef Vector _vector_times_matrix_c_impl(self, Vector v):\n...\n\n        print \"Input: v = \", v\n        print \"type(v) = \", type(v)\n```\n\n2. Run the example (after deleting /tmp/*.sobj!!):\n\n```\n\nsage: DATA = '/tmp/'\nsage: def ranks(N):\n....:         filename = '%sranks-%s.sobj'%(DATA,N)\n....:     if os.path.exists(filename):\n....:              D = load(filename)\n....:     else:\n....:              D = ModularSymbols(N,sign=1).cuspidal_submodule().new_submodule().decomposition()\n....:     for i,A in enumerate(D):\n....:             eps = -A.atkin_lehner_operator().matrix()[0,0]\n....:         winding_element = A.rational_period_mapping()(A.ambient_module()([0,oo]))\n....:         print N, i, eps, winding_element == 0\n....:     save(D, filename)\n....: \nsage: \n\nsage: ranks(11)\nInput: v =  (0, 1)\ntype(v) =  <type 'sage.modules.vector_rational_dense.Vector_rational_dense'>\nInput: v =  (0, 1)\ntype(v) =  <type 'sage.modules.vector_rational_dense.Vector_rational_dense'>\nInput: v =  (-1, 0)\ntype(v) =  <type 'sage.modules.vector_rational_dense.Vector_rational_dense'>\n11 0 1 False\nsage: ranks(11)\nInput: v =  (-1, 0)\ntype(v) =  <type 'sage.modules.free_module_element.FreeModuleElement_generic_sparse'>\n\n\n------------------------------------------------------------\nUnhandled SIGBUS: A bus error occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\n```",
    "created_at": "2008-05-06T23:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3113#issuecomment-21507",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_021508.json:
```json
{
    "body": "This is caused by matrix action caching code and the facts that:\n\n1. sparse and dense matrix spaces of the same dimension and degree are considered \"equal\" in sage.\n\n2. And pickle/unpickle happens to change something from dense to sparse.\n\nCertainly 2 is weird and is probably very specifically caused by a mistake in some pure python code for modular symbols.  But it shouldn't result in segfaults.\n\nIf one add 4 lines to modules/free_module.py to make it so modular symbols spaces are *not* equal if one is sparse and one is dense, then the problem completely disappears. \n\nHere's the diff that would do that:\n\n```\ndiff -r 0a4213d9da78 sage/modules/free_module.py\n--- a/sage/modules/free_module.py       Tue May 06 10:12:53 2008 -0700\n+++ b/sage/modules/free_module.py       Tue May 06 17:06:36 2008 -0700\n@@ -2784,6 +2784,8 @@ class FreeModule_ambient(FreeModule_gene\n         if not isinstance(other, FreeModule_generic):\n             return cmp(type(self), type(other))\n         if isinstance(other, FreeModule_ambient):\n+            c = cmp(self.is_sparse(), other.is_sparse())\n+            if c: return c\n             c = cmp(self.rank(), other.rank())\n             if c: return c\n             c = cmp(self.base_ring(), other.base_ring())\n@@ -3344,6 +3346,8 @@ class FreeModule_submodule_with_basis_pi\n             return 0\n         if not isinstance(other, FreeModule_generic):\n             return cmp(type(self), type(other))\n+        c = cmp(self.is_sparse(), other.is_sparse())\n+        if c: return c\n         c = cmp(self.ambient_vector_space(), other.ambient_vector_space())\n         if c: return c\n         c = cmp(self.dimension(), other.dimension())\n```\n\nI will leave it to Robert Bradshaw to decide what to do.  Probably the right solution is\nthat sparse and dense vector spaces do not compare to be equal no matter what.  Hmmm. \nThoughts?",
    "created_at": "2008-05-07T00:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3113#issuecomment-21508",
    "user": "https://github.com/williamstein"
}
```

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
@@ -2784,6 +2784,8 @@ class FreeModule_ambient(FreeModule_gene
         if not isinstance(other, FreeModule_generic):
             return cmp(type(self), type(other))
         if isinstance(other, FreeModule_ambient):
+            c = cmp(self.is_sparse(), other.is_sparse())
+            if c: return c
             c = cmp(self.rank(), other.rank())
             if c: return c
             c = cmp(self.base_ring(), other.base_ring())
@@ -3344,6 +3346,8 @@ class FreeModule_submodule_with_basis_pi
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

archive/issue_comments_021509.json:
```json
{
    "body": "Probably we shouldn't be using dictionaries (that compare with equals) to cache this information. There should also be a check. The coercion model itself uses a custom dictionary that keys on the object pointer, but the caching in the class itself is done via standard Python dicts. There should be a check at the very least--I'll write a patch to do that.",
    "created_at": "2008-05-07T00:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3113#issuecomment-21509",
    "user": "https://github.com/robertwb"
}
```

Probably we shouldn't be using dictionaries (that compare with equals) to cache this information. There should also be a check. The coercion model itself uses a custom dictionary that keys on the object pointer, but the caching in the class itself is done via standard Python dicts. There should be a check at the very least--I'll write a patch to do that.



---

archive/issue_comments_021510.json:
```json
{
    "body": "Attachment [3113-coerce-checks.patch](tarball://root/attachments/some-uuid/ticket3113/3113-coerce-checks.patch) by @robertwb created at 2008-05-07 06:17:46",
    "created_at": "2008-05-07T06:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3113#issuecomment-21510",
    "user": "https://github.com/robertwb"
}
```

Attachment [3113-coerce-checks.patch](tarball://root/attachments/some-uuid/ticket3113/3113-coerce-checks.patch) by @robertwb created at 2008-05-07 06:17:46



---

archive/issue_comments_021511.json:
```json
{
    "body": "It now adds an extra check to make sure coercion is performed when parents are equal but not unique for actions.",
    "created_at": "2008-05-07T06:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3113#issuecomment-21511",
    "user": "https://github.com/robertwb"
}
```

It now adds an extra check to make sure coercion is performed when parents are equal but not unique for actions.



---

archive/issue_comments_021512.json:
```json
{
    "body": "Patch looks reasonable, but this creates a doctest failure in `sage/coding/linear_code.py`. The `__eq__` code there could probably be improved, but the error seems to be coming up in some sort of internal consistency check with the coercion model. I'm voting to kick this back to robertwb to think about, since he's the expert. \n\nHere's the doctest failure:\n\n```\nsage -t  devel/sage-ref/sage/coding/linear_code.py          **********************************************************************\nFile \"/sage/tmp/linear_code.py\", line 139:\n    age: C == loads(dumps(C))\nException raised:\n    Traceback (most recent call last):\n      File \"/sage/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[13]>\", line 1, in <module>\n        C == loads(dumps(C))###line 139:\n    age: C == loads(dumps(C))\n      File \"/sage/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 984, in __eq__\n        if scheck*c:\n      File \"element.pyx\", line 2122, in sage.structure.element.Matrix.__mul__ (sage/structure/element.c:11352)\n      File \"coerce.pyx\", line 267, in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5039)\n      File \"coerce.pyx\", line 527, in sage.structure.coerce.CoercionModel_cache_maps.get_action_c (sage/structure/coerce.c:7876)\n      File \"coerce.pyx\", line 574, in sage.structure.coerce.CoercionModel_cache_maps.verify_action (sage/structure/coerce.c:8379)\n    RuntimeError: There is a BUG in the coercion model:\n                    Action found for R <built-in function mul> S does not have the correct domains\n                    R = Full MatrixSpace of 3 by 7 dense matrices over Finite Field of size 2 \n                    S = Vector space of dimension 7 over Finite Field of size 2\n                    (should be Full MatrixSpace of 3 by 7 dense matrices over Finite Field of size 2, Vector space of dimension 7 over Finite Field of size 2)\n                    action = Left action by Full MatrixSpace of 3 by 7 dense matrices over Finite Field of size 2 on Vector space of dimension 7 over Finite Field of size 2 (<type 'sage.categories.action.PrecomposedAction'>)\n                    \n**********************************************************************\n\n```\n\nNegative review until this gets corrected, but will be happy to give a positive once this is in order ...",
    "created_at": "2008-05-10T09:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3113#issuecomment-21512",
    "user": "https://github.com/craigcitro"
}
```

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

archive/issue_comments_021513.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-05-16T14:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3113#issuecomment-21513",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_021514.json:
```json
{
    "body": "Attachment [trac-3113-pt2.patch](tarball://root/attachments/some-uuid/ticket3113/trac-3113-pt2.patch) by @craigcitro created at 2008-06-15 05:35:28",
    "created_at": "2008-06-15T05:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3113#issuecomment-21514",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-3113-pt2.patch](tarball://root/attachments/some-uuid/ticket3113/trac-3113-pt2.patch) by @craigcitro created at 2008-06-15 05:35:28



---

archive/issue_comments_021515.json:
```json
{
    "body": "Attached patch fixes the last small problem -- somewhere there was a `left` instead of `right`.",
    "created_at": "2008-06-15T05:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3113#issuecomment-21515",
    "user": "https://github.com/craigcitro"
}
```

Attached patch fixes the last small problem -- somewhere there was a `left` instead of `right`.



---

archive/issue_comments_021516.json:
```json
{
    "body": "Dyslexia strikes again! This is the right fix.",
    "created_at": "2008-06-15T06:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3113#issuecomment-21516",
    "user": "https://github.com/robertwb"
}
```

Dyslexia strikes again! This is the right fix.



---

archive/issue_comments_021517.json:
```json
{
    "body": "Merged in Sage 3.0.3.rc0",
    "created_at": "2008-06-15T08:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3113#issuecomment-21517",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.rc0



---

archive/issue_events_007030.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-15T08:27:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3113#event-7030"
}
```



---

archive/issue_comments_021518.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-15T08:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3113#issuecomment-21518",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_007031.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-15T19:08:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3113",
    "milestone": "sage-3.0.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3113#event-7031"
}
```
