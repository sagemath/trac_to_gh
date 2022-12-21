# Issue 9827: Upgrade to Cython 0.13

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-08-28 00:36:27

Assignee: tbd

CC:  robertwb leif jason craigcitro timdumol mpatel

[Here](http://wiki.cython.org/ReleaseNotes-0.13) are the release notes for [Cython](http://www.cython.org/) 0.13.


---

Comment by leif created at 2010-09-15 16:56:34


```
...
byte-compiling /home/leif/Sage/sage-4.6.alpha0/local/lib/python2.6/site-packages/Cython/Compiler/Tests/TestBuffer.py to TestBuffer.pyc
running install_scripts
copying build/scripts-2.6/cython -> /home/leif/Sage/sage-4.6.alpha0/local/bin
changing mode of /home/leif/Sage/sage-4.6.alpha0/local/bin/cython to 755
running install_egg_info
Writing /home/leif/Sage/sage-4.6.alpha0/local/lib/python2.6/site-packages/Cython-0.13-py2.6.egg-info

real	0m33.965s
user	0m28.080s
sys	0m0.800s
Successfully installed cython-0.13
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing cython-0.13.spkg
$ ./sage -ba-force
*** TOUCHING ALL CYTHON (.pyx) FILES ***
scons: `install' is up to date.

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Building modified file sage/algebras/quatalg/quaternion_algebra_element.pyx.
Building modified file sage/algebras/quatalg/quaternion_algebra_cython.pyx.
Building modified file sage/calculus/var.pyx.
Building modified file sage/calculus/riemann.pyx.
Building modified file sage/calculus/interpolators.pyx.
Building modified file sage/categories/action.pyx.
Building modified file sage/categories/functor.pyx.
Building modified file sage/categories/map.pyx.
Building modified file sage/categories/morphism.pyx.
Building modified file sage/categories/examples/semigroups_cython.pyx.
Building modified file sage/coding/binary_code.pyx.
Building modified file sage/combinat/expnums.pyx.
Building modified file sage/combinat/matrices/dancing_links.pyx.
Building modified file sage/combinat/partitions.pyx.
Building modified file sage/combinat/words/word_datatypes.pyx.
Building modified file sage/combinat/permutation_cython.pyx.
Building modified file sage/crypto/boolean_function.pyx.
Building modified file sage/ext/fast_callable.pyx.
Building modified file sage/ext/fast_eval.pyx.
Building modified file sage/ext/interactive_constructors_c.pyx.
Building modified file sage/ext/multi_modular.pyx.
Building modified file sage/ext/sig.pyx.
Building modified file sage/finance/fractal.pyx.
Building modified file sage/finance/markov_multifractal_cython.pyx.
Building modified file sage/finance/time_series.pyx.
Building modified file sage/functions/prime_pi.pyx.
Building modified file sage/games/sudoku_backtrack.pyx.
Building modified file sage/geometry/toric_lattice_element.pyx.
Building modified file sage/graphs/chrompoly.pyx.
Building modified file sage/graphs/cliquer.pyx.
Building modified file sage/graphs/generic_graph_pyx.pyx.
Building modified file sage/graphs/modular_decomposition/modular_decomposition.pyx.
Building modified file sage/graphs/planarity.pyx.
Building modified file sage/graphs/trees.pyx.
Building modified file sage/graphs/genus.pyx.
Building modified file sage/graphs/base/c_graph.pyx.
Building modified file sage/graphs/base/sparse_graph.pyx.
Building modified file sage/graphs/base/dense_graph.pyx.
Building modified file sage/groups/group.pyx.
Building modified file sage/groups/perm_gps/permgroup_element.pyx.
Building modified file sage/groups/perm_gps/partn_ref/automorphism_group_canonical_label.pyx.
Building modified file sage/groups/perm_gps/partn_ref/double_coset.pyx.
Building modified file sage/groups/perm_gps/partn_ref/refinement_binary.pyx.
Building modified file sage/groups/perm_gps/partn_ref/refinement_graphs.pyx.
Building modified file sage/groups/perm_gps/partn_ref/refinement_lists.pyx.
Building modified file sage/groups/perm_gps/partn_ref/refinement_matrices.pyx.
Building modified file sage/groups/perm_gps/partn_ref/refinement_python.pyx.
Building modified file sage/gsl/callback.pyx.
Building modified file sage/gsl/dwt.pyx.
Building modified file sage/gsl/fft.pyx.
Building modified file sage/gsl/gsl_array.pyx.
Building modified file sage/gsl/integration.pyx.
Building modified file sage/gsl/interpolation.pyx.
Building modified file sage/gsl/ode.pyx.
Building modified file sage/gsl/probability_distribution.pyx.
Building modified file sage/libs/ecl.pyx.
Building modified file sage/libs/flint/flint.pyx.
Building modified file sage/libs/flint/fmpz_poly.pyx.
Building modified file sage/libs/fplll/fplll.pyx.
Building modified file sage/libs/linbox/linbox.pyx.
Building modified file sage/libs/lcalc/lcalc_Lfunction.pyx.
Building modified file sage/libs/libecm.pyx.
Building modified file sage/libs/mwrank/mwrank.pyx.
Building modified file sage/libs/pari/gen.pyx.
Building modified file sage/libs/ratpoints.pyx.
Building modified file sage/libs/singular/singular.pyx.
Building modified file sage/libs/singular/polynomial.pyx.
Building modified file sage/libs/singular/ring.pyx.
Building modified file sage/libs/singular/groebner_strategy.pyx.
Building modified file sage/libs/singular/function.pyx.
Building modified file sage/libs/singular/option.pyx.
Building modified file sage/libs/symmetrica/symmetrica.pyx.
Building modified file sage/libs/mpmath/utils.pyx.
Building modified file sage/libs/mpmath/ext_impl.pyx.
Building modified file sage/libs/mpmath/ext_main.pyx.
Building modified file sage/libs/mpmath/ext_libmp.pyx.
Building modified file sage/libs/cremona/homspace.pyx.
Building modified file sage/libs/cremona/mat.pyx.
Building modified file sage/libs/cremona/newforms.pyx.
Building modified file sage/libs/ntl/ntl_GF2.pyx.
Building modified file sage/libs/ntl/ntl_GF2E.pyx.
Building modified file sage/libs/ntl/ntl_GF2EContext.pyx.
Building modified file sage/libs/ntl/ntl_GF2EX.pyx.
Building modified file sage/libs/ntl/ntl_GF2X.pyx.
Building modified file sage/libs/ntl/ntl_lzz_p.pyx.
Building modified file sage/libs/ntl/ntl_lzz_pContext.pyx.
Building modified file sage/libs/ntl/ntl_lzz_pX.pyx.
Building modified file sage/libs/ntl/ntl_mat_GF2.pyx.
Building modified file sage/libs/ntl/ntl_mat_GF2E.pyx.
Building modified file sage/libs/ntl/ntl_mat_ZZ.pyx.
Building modified file sage/libs/ntl/ntl_ZZ.pyx.
Building modified file sage/libs/ntl/ntl_ZZX.pyx.
Building modified file sage/libs/ntl/ntl_ZZ_p.pyx.
Building modified file sage/libs/ntl/ntl_ZZ_pContext.pyx.
Building modified file sage/libs/ntl/ntl_ZZ_pE.pyx.
Building modified file sage/libs/ntl/ntl_ZZ_pEContext.pyx.
Building modified file sage/libs/ntl/ntl_ZZ_pEX.pyx.
Building modified file sage/libs/ntl/ntl_ZZ_pX.pyx.
Building modified file sage/matrix/action.pyx.
Building modified file sage/matrix/change_ring.pyx.
Building modified file sage/matrix/matrix.pyx.
Building modified file sage/matrix/matrix0.pyx.
Building modified file sage/matrix/matrix1.pyx.
Building modified file sage/matrix/matrix2.pyx.
Building modified file sage/matrix/matrix_complex_double_dense.pyx.
Building modified file sage/matrix/matrix_cyclo_dense.pyx.
Building modified file sage/matrix/matrix_dense.pyx.
Building modified file sage/matrix/matrix_double_dense.pyx.
Building modified file sage/matrix/matrix_generic_dense.pyx.
Building modified file sage/matrix/matrix_generic_sparse.pyx.
Building modified file sage/matrix/matrix_integer_2x2.pyx.
Building modified file sage/matrix/matrix_integer_dense.pyx.
Building modified file sage/matrix/matrix_integer_sparse.pyx.
Building modified file sage/matrix/matrix_mod2_dense.pyx.
Building modified file sage/matrix/matrix_modn_dense.pyx.
Building modified file sage/matrix/matrix_modn_sparse.pyx.
Building modified file sage/matrix/matrix_mpolynomial_dense.pyx.
Building modified file sage/matrix/matrix_rational_dense.pyx.
Building modified file sage/matrix/matrix_rational_sparse.pyx.
Building modified file sage/matrix/matrix_real_double_dense.pyx.
Building modified file sage/matrix/matrix_sparse.pyx.
Building modified file sage/matrix/matrix_symbolic_dense.pyx.
Building modified file sage/matrix/matrix_window.pyx.
Building modified file sage/matrix/matrix_window_modn_dense.pyx.
Building modified file sage/matrix/misc.pyx.
Building modified file sage/matrix/strassen.pyx.
Building modified file sage/media/channels.pyx.
Building modified file sage/misc/allocator.pyx.
Building modified file sage/misc/bitset.pyx.
Building modified file sage/misc/citation.pyx.
Building modified file sage/misc/cython_c.pyx.
Building modified file sage/misc/derivative.pyx.
Building modified file sage/misc/fpickle.pyx.
Building modified file sage/misc/misc_c.pyx.
Building modified file sage/misc/parser.pyx.
Building modified file sage/misc/pickle_old.pyx.
Building modified file sage/misc/randstate.pyx.
Building modified file sage/misc/refcount.pyx.
Building modified file sage/misc/reset.pyx.
Building modified file sage/misc/sage_timeit_class.pyx.
Building modified file sage/misc/sagex_ds.pyx.
Building modified file sage/misc/search.pyx.
Building modified file sage/misc/session.pyx.
Building modified file sage/modular/arithgroup/congroup_pyx.pyx.
Building modified file sage/modular/modform/eis_series_cython.pyx.
Building modified file sage/modular/modsym/apply.pyx.
Building modified file sage/modular/modsym/heilbronn.pyx.
Building modified file sage/modular/modsym/p1list.pyx.
Building modified file sage/modules/free_module_element.pyx.
Building modified file sage/modules/module.pyx.
Building modified file sage/modules/vector_complex_double_dense.pyx.
Building modified file sage/modules/vector_double_dense.pyx.
Building modified file sage/modules/vector_integer_dense.pyx.
Building modified file sage/modules/vector_modn_dense.pyx.
Building modified file sage/modules/vector_mod2_dense.pyx.
Building modified file sage/modules/vector_rational_dense.pyx.
Building modified file sage/modules/vector_real_double_dense.pyx.
Building modified file sage/numerical/mip.pyx.
Building modified file sage/plot/complex_plot.pyx.
Building modified file sage/plot/plot3d/base.pyx.
Building modified file sage/plot/plot3d/implicit_surface.pyx.
Building modified file sage/plot/plot3d/index_face_set.pyx.
Traceback (most recent call last):
  File "setup.py", line 753, in <module>
    queue = compile_command_list(ext_modules, deps)
  File "setup.py", line 713, in compile_command_list
    dep_file, dep_time = deps.newest_dep(f)
  File "setup.py", line 628, in newest_dep
    for f in self.all_deps(filename):
  File "setup.py", line 611, in all_deps
    deps.update(self.all_deps(f, path))
  File "setup.py", line 609, in all_deps
    for f in self.immediate_deps(filename):
  File "setup.py", line 591, in immediate_deps
    self._deps[filename] = self.parse_deps(filename)
  File "setup.py", line 581, in parse_deps
    raise IOError, "could not find dependency %s included in %s."%(path, filename)
IOError: could not find dependency sage/ext/interpreters/python_object.pxd included in sage/ext/interpreters/wrapper_rdf.pxd.
sage: There was an error installing modified sage library code.
```



---

Comment by leif created at 2010-09-15 17:06:47

I get the same when trying to reinstall `sage-4.6.alpha0.spkg`, or afterwards again running `./sage -ba`.


---

Comment by leif created at 2010-09-15 17:14:56

From the release notes:
  _"More shipped standard library declarations. The `python_*` and `stdlib/stdio .pxd` files have been deprecated in favor of `clib.*` and `cpython[.*]` and may get removed in a future release. "_


---

Comment by mpatel created at 2010-09-15 19:52:27

Did you apply the 8 Sage library patches mentioned [in this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/0239f712a39fce4a/ba4e7b77e4de1b10?#ba4e7b77e4de1b10)?

Disclaimer: I haven't checked whether all of these patches are necessary and sufficient for Cython 0.13 final.


---

Comment by leif created at 2010-09-15 20:04:10

Replying to [comment:5 mpatel]:
> Did you apply the 8 Sage library patches mentioned [in this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/0239f712a39fce4a/ba4e7b77e4de1b10?#ba4e7b77e4de1b10)?

No (I haven't read that thread), I just tried and looked what happens... :)

I've created symbolic links to the pxds in the `Deprecated/` directory and now run (at least) into the missing `from cpython import bool` problem.

I would have expected some more info / notes here or at the Cython site; Volker Braun asked on the IRC when Cython will get updated (I knew there was 0.12.2 and a new release coming up), so I took a look at this ticket.


---

Comment by robertwb created at 2010-09-16 00:46:05

I've got an 0.13 spkg that has a tiny patch on top to fix the performance regression with `__getattr__`. Yes, you need to appply all 8 Sage library patches, though I plan to clean at least one of them up 'cause it's got unnecessary garbage in it. (I was actually working on this last night, and planned to finish it up tonight.)


---

Comment by robertwb created at 2010-09-16 09:18:13

Spkg up at http://sage.math.washington.edu/home/robertwb/cython/cython-0.13.p0.spkg . I'm attaching a set of patches that should be necessary and sufficient.


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by robertwb created at 2010-09-16 09:27:36

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-09-16 09:27:36

The last one, hudson_results.patch, isn't needed for Sage but makes continuous testing of Sage against cython-devel much easier.


---

Comment by leif created at 2010-09-16 09:34:08

`spkg-install` and `SPKG.txt` (Changelog!) need little clean-up. (I made my own spkg yesterday, so I could carry the changes over.)


---

Comment by robertwb created at 2010-09-16 16:12:28

Feel free to carry your changes over. SPKG.txt doesn't have a changelog because it's all in the revision control and there's very little to say anyways (other than "bumped revision" which is pretty redundant). I'd be happy to review whatever you have.


---

Comment by leif created at 2010-09-16 16:29:15

Replying to [comment:13 robertwb]:
> Feel free to carry your changes over.

Ok.

> SPKG.txt doesn't have a changelog because it's all in the revision control and there's very little to say anyways (other than "bumped revision" which is pretty redundant).

Well, it wouldn't be bad to see in SPKG.txt which version was packaged when for Sage...

It's of course (at least currently) unlikely that Sage will patch Cython rather than report problems "upstream" and include a (quickly) fixed upstream version.

Hope you'll stay at Sage and Cython... ;-)


---

Comment by leif created at 2010-09-16 16:37:51

Funny, my patch (also) intended to avoid exactly the error which is currently made in `spkg-install`. :D

Coming soon...


---

Comment by leif created at 2010-09-16 17:07:14

Patch is up.


---

Comment by robertwb created at 2010-09-16 17:21:44

Looks fine to me, except that the change was to speed up `__getattr__` not `__getitem__` (specifically for Python descendants of cdef classes).


---

Comment by leif created at 2010-09-16 17:23:22

Oooops...


---

Attachment

SPKG patch. As the name says... (also quotes SAGE_LOCAL; some clean-up) Now with corrected SPKG.txt (__getattr__).


---

Comment by leif created at 2010-09-16 17:57:19

I've replaced the patch with a corrected one (`__getitem__()` -> `__getattr__()` in the changelog).


---

Attachment

apply to sage local repo


---

Attachment

Okay, now I'm really confused about what patches I should apply where to review this.  Can someone give directions for reviewing?  Thanks!


---

Comment by robertwb created at 2010-09-29 07:38:58

Thanks for being willing to take a look. Apply patches 0-7 and hudson_results.patch to the sage library in order. I have incorporated trac_9828-fix_applying_patch_and_more-spkg.patch into the spkg (at the same address as above). sage-local-hudson.patch gets applied to sage/local/bin. If you have any other questions, please don't hesitate to ask.


---

Comment by leif created at 2010-09-30 05:29:56

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-09-30 05:29:56

Hmmm, patches still apply (without rejects) to Sage 4.6.alpha2[pre2], spkg installs ok, and `./sage -b` also works.

But after that, Sage doesn't start (Sphinx raises the same exception):

```
...
Testing that Sage starts...
Traceback (most recent call last):
  File "/home/leif/Sage/sage-4.6.alpha2pre2/local/bin/sage-eval", line 4, in <module>
    from sage.all import *
  File "/home/leif/Sage/sage-4.6.alpha2pre2/local/lib/python2.6/site-packages/sage/all.py", line 64, in <module>
    from sage.misc.all       import *         # takes a while
  File "/home/leif/Sage/sage-4.6.alpha2pre2/local/lib/python2.6/site-packages/sage/misc/all.py", line 67, in <module>
    from sage_input import sage_input
  File "/home/leif/Sage/sage-4.6.alpha2pre2/local/lib/python2.6/site-packages/sage/misc/sage_input.py", line 163, in <module>
    from sage.misc.functional import parent
  File "/home/leif/Sage/sage-4.6.alpha2pre2/local/lib/python2.6/site-packages/sage/misc/functional.py", line 34, in <module>
    import sage.interfaces.expect
  File "/home/leif/Sage/sage-4.6.alpha2pre2/local/lib/python2.6/site-packages/sage/interfaces/expect.py", line 52, in <module>
    from sage.structure.parent_base import ParentWithBase
  File "parent_base.pyx", line 1, in init sage.structure.parent_base (sage/structure/parent_base.c:1934)
  File "parent_old.pyx", line 1, in init sage.structure.parent_old (sage/structure/parent_old.c:7031)
  File "parent.pyx", line 383, in init sage.structure.parent (sage/structure/parent.c:20048)
AttributeError: type object 'sage.structure.parent.Parent' has no attribute '__getattr__'
Sage failed to startup.
make: *** [ptestlong] Error 1
```


`./sage -ba` (tried after that) doesn't work either, due to newly merged Cython code:

```
*** TOUCHING ALL CYTHON (.pyx) FILES ***
scons: `install' is up to date.

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Building modified file sage/algebras/quatalg/quaternion_algebra_element.pyx.
Building modified file sage/algebras/quatalg/quaternion_algebra_cython.pyx.
Building modified file sage/calculus/var.pyx.
...
Building modified file sage/ext/interpreters/wrapper_rr.pyx.
Building modified file sage/ext/interpreters/wrapper_py.pyx.
Building modified file sage/ext/interpreters/wrapper_el.pyx.
Execute 271 commands (using 8 threads)

Error converting Pyrex file to C:
------------------------------------------------------------
...
    cdef int *vertices
    cdef int **line_h_out
    cdef int **line_h_in
    cdef list g_vertices
    cdef int i
    cdef bool directed
        ^
------------------------------------------------------------

/home/leif/Sage/sage-4.6.alpha2pre2/devel/sage-9828-cython/sage/graphs/generic_graph_pyx.pxd:26:9: 'bool' is not a type identifier
...
python `which cython` --embed-positions --directive cdivision=True,autotestdict=False -I/home/leif/Sage/sage-4.6.alpha2pre2/devel/sage-9828-cython -o sage/gsl/callback.c sage/gsl/callback.pyx
sage/gsl/callback.pyx --> /home/leif/Sage/sage-4.6.alpha2pre2/local//lib/python/site-packages//sage/gsl/callback.pyx
python `which cython` --embed-positions --directive cdivision=True,autotestdictwarning: /home/leif/Sage/sage-4.6.alpha2pre2/devel/sage-9828-cython/sage/gsl/gsl_array.pyx:1:0: __getslice__, __setslice__, and __delslice__ are not supported by Python 3, use __getitem__, __setitem__, and __delitem__ instead
warning: /home/leif/Sage/sage-4.6.alpha2pre2/devel/sage-9828-cython/sage/gsl/fft.pyx:1:0: __getslice__, __setslice__, and __delslice__ are not supported by Python 3, use __getitem__, __setitem__, and __delitem__ instead
Error running command, failed with status 256.
sage: There was an error installing modified sage library code.
```



---

Comment by jason created at 2010-09-30 05:34:57

Looks like a bool->bint was missed?


---

Comment by robertwb created at 2010-09-30 16:04:10

Replying to [comment:23 jason]:
> Looks like a bool->bint was missed?

Or added since this spkg was created--it used to all work fine. I suppose I'll download the latest alpha and see what's up.


---

Comment by robertwb created at 2010-10-01 08:33:51

Changing status from needs_work to needs_review.


---

Attachment

OK, one more patch, and an updated spkg.


---

Comment by jason created at 2010-10-05 03:37:13

I see Craig is the author of a lot of the patches.  robertwb: have you reviewed those patches?  Which patches still need review?

I applied all patches and installed on a fresh copy of 4.6.alpha2 (I think it's a fresh copy), and had the following failures in ptestlong on Ubuntu 10.04 64-bit:


```
File "/home/grout/sage-4.6.alpha2/devel/sage-main/sage/misc/sageinspect.py", line 1058:
    sage: sage_getdef(sage.rings.integer.Integer.__init__, obj_name='__init__')
Expected:
    '__init__(x=None, base=0)'
Got:
    '__init__( [noargspec] )'
```


(that's a test that I thought one of the patches changed to the expected value listed above).


```
        sage -t  -long 4.6.alpha2/devel/sage/sage/plot/misc.py # 4 doctests failed
        sage -t  -long 4.6.alpha2/devel/sage/sage/plot/plot.py # 12 doctests failed
```


These are corrected in #9221, I think.


---

Comment by robertwb created at 2010-10-05 05:05:24

I've looked at all of the ones Craig wrote (way back) and they're all fine. I assume you did a sage -ba after installing Cython? The sageinspect output is what I got on a fresh 4.6.alpha2 on sage.math. I doubt the plot ones are related, but I didn't see them when I ran the tests which is strange.


---

Comment by jason created at 2010-10-05 17:16:46

Replying to [comment:27 robertwb]:
> I've looked at all of the ones Craig wrote (way back) and they're all fine. I assume you did a sage -ba after installing Cython? The sageinspect output is what I got on a fresh 4.6.alpha2 on sage.math. I doubt the plot ones are related, but I didn't see them when I ran the tests which is strange. 

I didn't do sage -ba.  I'm trying again now.


---

Comment by jason created at 2010-10-05 18:42:34

I did sage -ba (4.6.alpha2, the above patches applied, and the new Cython spkg), and still got the following failures (Ubuntu 10.04 64-bit):


```
sage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py
**********************************************************************
File "/home/grout/sage-4.6.alpha2/local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py", line 1074:
    sage: sage_getsource(sage.rings.integer.Integer.__init__, is_binary=True)
Expected:    Traceback (most recent call last):    ...    TypeError: arg is not a module, class, method, function, traceback, frame, or code objectGot:    '    def __init__(self, x=None, unsigned int base=0):\n        """\n        EXAMPLES::\n        \n            sage: a = long(-901824309821093821093812093810928309183091832091)\n            sage: b = ZZ(a); b\n            -901824309821093821093812093810928309183091832091\n            sage: ZZ(b)\n            -901824309821093821093812093810928309183091832091\n            sage: ZZ(\'-901824309821093821093812093810928309183091832091\')\n            -901824309821093821093812093810928309183091832091\n            sage: ZZ(int(-93820984323))\n            -93820984323\n            sage: ZZ(ZZ(-901824309821093821093812093810928309183091832091))\n            -901824309821093821093812093810928309183091832091\n            sage: ZZ(QQ(-901824309821093821093812093810928309183091832091))\n            -901824309821093821093812093810928309183091832091\n            sage: ZZ(RR(2.0)^80)\n            1208925819614629174706176\n            sage: ZZ(QQbar(sqrt(28-10*sqrt(3)) + sqrt(3)))\n            5\n            sage: ZZ(AA(32).nth_root(5))\n            2\n            sage: ZZ(pari(\'Mod(-3,7)\'))\n            4\n            sage: ZZ(\'sage\')\n            Traceback (most recent call last):\n            ...\n            TypeError: unable to convert x (=sage) to an integer\n            sage: Integer(\'zz\',36).str(36)\n            \'zz\'\n            sage: ZZ(\'0x3b\').str(16)\n            \'3b\'\n            sage: ZZ( ZZ(5).digits(3) , 3)\n            5\n            sage: import numpy\n            sage: ZZ(numpy.int64(7^7))\n            823543\n            sage: ZZ(numpy.ubyte(-7))\n            249\n            sage: ZZ(True)\n            1\n            sage: ZZ(False)\n            0\n            sage: ZZ(1==0)\n            0\n            sage: ZZ(\'+10\')\n            10\n        \n        ::\n        \n            sage: k = GF(2)\n            sage: ZZ( (k(0),k(1)), 2)\n            2\n        \n        ::\n        \n            sage: t = pari(0*ZZ[x].0 + 3)\n            sage: t.type()\n            \'t_POL\'\n            sage: ZZ(t)\n            3\n\n            sage: ZZ(float(2.0))\n            2\n            sage: ZZ(float(1.0/0.0))\n            Traceback (most recent call last):\n            ...\n            OverflowError: cannot convert float infinity to integer\n            sage: ZZ(float(0.0/0.0))\n            Traceback (most recent call last):\n            ...\n            ValueError: cannot convert float NaN to integer\n\n        ::\n\n            sage: class MyInt(int):\n            ...       pass\n            sage: class MyLong(long):\n            ...       pass\n            sage: class MyFloat(float):\n            ...       pass\n            sage: ZZ(MyInt(3))\n            3\n            sage: ZZ(MyLong(4))\n            4\n            sage: ZZ(MyFloat(5))\n            5\n        """\n\n        # TODO: All the code below should somehow be in an external\n        # cdef\'d function.  Then e.g., if a matrix or vector or\n        # polynomial is getting filled by mpz_t\'s, it can use the\n        # rules below to do the fill construction of mpz_t\'s, but\n        # without the overhead of creating any Python objects at all.\n        # The cdef\'s function should be of the form\n        #     mpz_init_set_sage(mpz_t y, object x)\n        # Then this function becomes the one liner:\n        #     mpz_init_set_sage(self.value, x)\n\n        cdef Integer tmp\n        cdef char* xs\n        \n        cdef Element lift\n        \n        if x is None:\n            if mpz_sgn(self.value) != 0:\n                mpz_set_si(self.value, 0)\n            \n        else:\n            # First do all the type-check versions; these are fast.\n\n            if PY_TYPE_CHECK(x, Integer):\n                set_from_Integer(self, <Integer>x)\n\n            elif PY_TYPE_CHECK(x, bool):\n                mpz_set_si(self.value, PyInt_AS_LONG(x))\n\n            elif PyInt_Check(x):\n                mpz_set_si(self.value, PyInt_AS_LONG(x))\n\n            elif PyLong_Check(x):\n                mpz_set_pylong(self.value, x)\n\n            elif PyFloat_Check(x):\n                n = long(x)\n                if n == x:\n                    mpz_set_pylong(self.value, n)\n                else:\n                    raise TypeError, "Cannot convert non-integral float to integer"\n\n            elif PY_TYPE_CHECK(x, pari_gen):\n                \n                if typ((<pari_gen>x).g) == t_INT:\n                    t_INT_to_ZZ(self.value, (<pari_gen>x).g)\n                    \n                else:\n                    if typ((<pari_gen>x).g) == t_INTMOD:\n                        x = x.lift()\n                    # TODO: figure out how to convert to pari integer in base 16 ?\n                    \n                    # todo: having this "s" variable around here is causing\n                    # Cython to play games with refcount for the None object, which\n                    # seems really stupid.\n                \n                    try:\n                        s = hex(x)\n                        base = 16\n                    except:\n                        s = str(x)\n                        base = 10\n                        \n                    if mpz_set_str(self.value, s, base) != 0:\n                        raise TypeError, "Unable to coerce PARI %s to an Integer."%x\n\n            elif PyString_Check(x):\n                if base < 0 or base > 36:\n                    raise ValueError, "base (=%s) must be between 2 and 36"%base\n                \n                xs = x\n                if xs[0] == c\'+\':\n                    xs += 1\n                if mpz_set_str(self.value, xs, base) != 0:\n                    raise TypeError, "unable to convert x (=%s) to an integer"%x\n                \n            elif PyObject_HasAttrString(x, "_integer_"):\n                # todo: Note that PyObject_GetAttrString returns NULL if\n                # the attribute was not found. If we could test for this,\n                # we could skip the double lookup. Unfortunately Cython doesn\'t\n                # seem to let us do this; it flags an error if the function\n                # returns NULL, because it can\'t construct an "object" object\n                # out of the NULL pointer. This really sucks. Perhaps we could\n                # make the function prototype have return type void*, but\n                # then how do we make Cython handle the reference counting?\n                set_from_Integer(self, (<object> PyObject_GetAttrString(x, "_integer_"))(the_integer_ring))\n\n            elif (PY_TYPE_CHECK(x,
 list) or PY_TYPE_CHECK(x, tuple)) and base > 1:\n                b = the_integer_ring(base)\n                tmp = the_integer_ring(0)\n                for i in range(len(x)):\n                    tmp += t
he_integer_ring(x[i])*b**i\n                mpz_set(self.value, tmp.value)\n\n            else:\n                import numpy\n                if isinstance(x, numpy.integer):\n                    mpz_set_p
ylong(self.value, x.__long__())\n                    return\n                    \n                elif PY_TYPE_CHECK(x, Element):\n                    try:\n                        lift = x.lift()\n       
                 if lift._parent != (<Element>x)._parent:\n                            tmp = the_integer_ring(lift)\n                            mpz_swap(tmp.value, self.value)\n                            
return\n                    except AttributeError:\n                        pass\n                        \n                raise TypeError, "unable to coerce %s to an integer" % type(x)\n'
**********************************************************************
File "/home/grout/sage-4.6.alpha2/local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/sageinspect.py", line 1079:
    sage: sage_getdef(sage.rings.integer.Integer.__init__, obj_name='__init__')
Expected:
    '__init__( [noargspec] )'
Got:
    '__init__(x=None, base=0)'
**********************************************************************
1 items had failures:
   2 of  26 in __main__.example_23
***Test Failed*** 2 failures.
```



---

Comment by jason created at 2010-10-05 18:49:16

I just noticed those two failures were in sagenb.  I can replicate them doing `sage -t -sagenb`.  It looks like the same changes that were needed in sage/misc/sageinspect.py are also needed in the notebook version of that file?  (see the 8_alpha_fixes.patch above).

I'm not sure how the two sageinspect.py files are related (in the library and in the notebook), so I'm CCing Tim and Mitesh on this.


---

Comment by timdumol created at 2010-10-05 18:52:30

Replying to [comment:30 jason]:
> I just noticed those two failures were in sagenb.  I can replicate them doing `sage -t -sagenb`.  It looks like the same changes that were needed in sage/misc/sageinspect.py are also needed in the notebook version of that file?  (see the 8_alpha_fixes.patch above).
> 
> I'm not sure how the two sageinspect.py files are related (in the library and in the notebook), so I'm CCing Tim and Mitesh on this.

The `sageinspect.py` in SageNB was derived from the `sageinspect.py` of the main Sage library by William when the new SageNB was separated from the main Sage library. Feel free to make the same changes.


---

Comment by jason created at 2010-10-05 19:01:18

Replying to [comment:31 timdumol]:
> Replying to [comment:30 jason]:
> > I just noticed those two failures were in sagenb.  I can replicate them doing `sage -t -sagenb`.  It looks like the same changes that were needed in sage/misc/sageinspect.py are also needed in the notebook version of that file?  (see the 8_alpha_fixes.patch above).
> > 
> > I'm not sure how the two sageinspect.py files are related (in the library and in the notebook), so I'm CCing Tim and Mitesh on this.
> 
> The `sageinspect.py` in SageNB was derived from the `sageinspect.py` of the main Sage library by William when the new SageNB was separated from the main Sage library. Feel free to make the same changes.


Is there any reason why it is not just imported, rather than being copied?


---

Comment by timdumol created at 2010-10-05 19:09:47

Replying to [comment:32 jason]:
> Replying to [comment:31 timdumol]:
> > Replying to [comment:30 jason]:
> > > I just noticed those two failures were in sagenb.  I can replicate them doing `sage -t -sagenb`.  It looks like the same changes that were needed in sage/misc/sageinspect.py are also needed in the notebook version of that file?  (see the 8_alpha_fixes.patch above).
> > > 
> > > I'm not sure how the two sageinspect.py files are related (in the library and in the notebook), so I'm CCing Tim and Mitesh on this.
> > 
> > The `sageinspect.py` in SageNB was derived from the `sageinspect.py` of the main Sage library by William when the new SageNB was separated from the main Sage library. Feel free to make the same changes.
> 
> 
> Is there any reason why it is not just imported, rather than being copied?

William stated that he wanted SageNB to be usable separately from Sage, which means not having to import Sage libraries to function.


---

Comment by robertwb created at 2010-10-05 23:25:46

Yes, the sagenb version needs to be updated as well. Should I post a new sagenb spkg, or is there one already in the works? 

Anything else?


---

Comment by mpatel created at 2010-10-05 23:33:37

Replying to [comment:34 robertwb]:
> Yes, the sagenb version needs to be updated as well. Should I post a new sagenb spkg, or is there one already in the works? 

You can just post patches here against #10036's SageNB 0.8.4.  I can add them to a 0.8.5 and update #10036.


---

Comment by mpatel created at 2010-10-07 08:34:01

Is a SageNB patch the only barrier to a positive review?


---

Comment by mpatel created at 2010-10-07 09:24:53

SageNB doctest  fixes.  Apply to sagenb repository.


---

Attachment

Folded sage repository patch.  Apply only this patch to the sage repository.


---

Attachment

Ticket number in scripts repo patch.  Apply only this patch to the scripts repo.


---

Comment by mpatel created at 2010-10-07 10:00:51

I've added a SageNB patch, folded sage repository patch, and updated scripts repository patch with the ticket number in the commit string.  The SageNB package link is in the description


---

Comment by mpatel created at 2010-10-07 10:11:44

The long doctests pass for me on sage.math with 4.6.alpha2 + the spkgs and patches in the description.

If no one objects, I'm giving this a positive review.  Can someone please review #10036 soon?

By the way, does `XML_RESULTS = os.environ.get('XML_RESULTS', None)` internally do the same as

```python
try:
    XML_RESULTS = os.environ['XML_RESULTS']
except KeyError:
    XML_RESULTS = None
```

?


---

Comment by mpatel created at 2010-10-07 10:11:44

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-10-07 11:19:25

Resolution: fixed


---

Comment by jason created at 2010-10-07 13:39:56

Replying to [comment:38 mpatel]:
> The long doctests pass for me on sage.math with 4.6.alpha2 + the spkgs and patches in the description.
> 
> If no one objects, I'm giving this a positive review.  Can someone please review #10036 soon?
> 
> By the way, does `XML_RESULTS = os.environ.get('XML_RESULTS', None)` internally do the same as
> {{{
> #!python
> try:
>     XML_RESULTS = os.environ['XML_RESULTS']
> except KeyError:
>     XML_RESULTS = None
> }}}
> ?

Yes.  See http://docs.python.org/library/stdtypes.html#dict.get


---

Comment by robertwb created at 2010-10-07 15:59:07

Replying to [comment:38 mpatel]:
> The long doctests pass for me on sage.math with 4.6.alpha2 + the spkgs and patches in the description.
> 
> If no one objects, I'm giving this a positive review.  

Thanks all! Next up, Cython 0.13.1 :) I'm neither planning to wait as long nor make as many changes, so it won't be near as bad...

> Can someone please review #10036 soon?
> 
> By the way, does `XML_RESULTS = os.environ.get('XML_RESULTS', None)` internally do the same as
> {{{
> #!python
> try:
>     XML_RESULTS = os.environ['XML_RESULTS']
> except KeyError:
>     XML_RESULTS = None
> }}}
> ?

Yes, that would have probably been cleaner.


---

Comment by jason created at 2010-10-07 16:07:50

Replying to [comment:42 robertwb]:

> > 
> > By the way, does `XML_RESULTS = os.environ.get('XML_RESULTS', None)` internally do the same as
> > {{{
> > #!python
> > try:
> >     XML_RESULTS = os.environ['XML_RESULTS']
> > except KeyError:
> >     XML_RESULTS = None
> > }}}
> > ?
> 
> Yes, that would have probably been cleaner. 

Since None is the default default value, it could even be shortened to `XML_RESULTS = os.environ.get('XML_RESULTS')`


---

Comment by jdemeyer created at 2019-01-11 13:31:41

What is the purpose of this `XML_RESULTS` stuff which was introduced here?
