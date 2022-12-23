# Issue 9107: Nested class name mangling can be wrong in case of double nesting

Issue created by migration from https://trac.sagemath.org/ticket/9107

Original creator: hivert

Original creation time: 2010-05-31 20:52:31

Assignee: nthiery

CC:  simonking zabrocki

In the following class tree:

```
class Bla(UniqueRepresentation):
    class Bla1(UniqueRepresentation):
        class Bla11:
	    Pass
    class Bla2:
        class Bla21:
	    Pass
```

The names are set to

```
        sage: Bla.Bla1.__name__
        'Bla.Bla1'
        sage: Bla.Bla2.__name__
        'Bla.Bla2'
        sage: Bla.Bla2.Bla21.__name__
        'Bla.Bla2.Bla21'
```

But

```
        sage: Bla.Bla1.Bla11.__name__
        'Bla1.Bla11'
```

whereas one would expect `'Bla.Bla1.Bla11'`
This breaks a lot of doc in categories and in particular in functorial constructions.

Florent


---

Comment by SimonKing created at 2012-05-02 14:42:54

I think we should make this depend on #12808, because it cythonises nested classes.

Here is my analysis:

 1. In sage.misc.nested_class.modify_for_nested_pickling, only those attributes of a class are (recursively) renamed that are instances of type or of `ClassType`. However, ironically, instances of `NestedClassMetaclass` are ignored.
 2. It is verified that the name of the to-be-changed class is identical with its name as an attribute of the calling class. But the renaming breaks the identity.


---

Comment by SimonKing created at 2012-05-02 16:37:49

I think the attached patch solves the problem. I get:

```
sage: class Bla(UniqueRepresentation):
....:     class Bla1(UniqueRepresentation):
....:         class Bla11:
....:             pass
....:     class Bla2:                   
....:         class Bla21:   
....:             pass
....:         
sage: Bla.Bla1.Bla11
<class __main__.Bla.Bla1.Bla11 at 0x46e7808>
```


The change is in `modify_for_nested_pickle`, which is called recursively. The idea is that the function should have an extra argument `first_run`, that is True by default. If the extra argument is False, then it is assumed that it is not applied for the first time.

Here: Since Bla.Bla1 is an instance of `NestedClassMetaclass`, `modify_for_nested_pickle` is called on `Bla.Bla1.Bla11`, resulting in `Bla.Bla1.Bla11.__name__=='Bla1.Bla11'`. However, since Bla is an instance of `NestedClassMetaclass` as well, the function is applied to `Bla.Bla1` and thus recursively to `Bla.Bla1.Bla11` another time.

Now, without my patch, in the second run, `modify_for_nested_pickle` would be confused by the fact that `Bla.Bla1.__dict__` lists `Bla.Bla1.Bla11` under the name `Bla11`, but `Bla11.__name__=='Bla1.Bla11'`. With my patch, `modify_for_nested_pickle` expects exactly that naming scheme, and is thus changing `Bla.Bla1.Bla11.__name__` into `"Bla.Bla1.Bla11"`.

Much BlaBla, but I think it works...

*__Potential problems__*


```
sage: module = sys.modules['__main__']
sage: getattr(module, 'Bla1.Bla11')                      
<class __main__.Bla.Bla1.Bla11 at 0x46e7808>
sage: getattr(module, 'Bla.Bla1.Bla11')
<class __main__.Bla.Bla1.Bla11 at 0x46e7808>
```

Hence, Bla.Bla1.Bla11 is listed in the module under two different names. If you think it is bad, then one could probably modify the function when first_run is false, such that the name given in the first run is erased from the module.

Moreover, the reviewer will likely find a speed regression, when excessively creating nested unique representations. But that's hardly realistic...


---

Comment by SimonKing created at 2012-05-02 16:37:49

Changing status from new to needs_review.


---

Comment by SimonKing created at 2012-05-02 16:46:54

Another problem: Source inspection does not work yet in the following example.

```
sage: cython_code = [
... "from sage.structure.unique_representation import UniqueRepresentation",
... "class A1(UniqueRepresentation):",
... "    class B1(UniqueRepresentation):",
... "        class C1: pass",
... "    class B2:",
... "        class C2: pass"]
sage: import os
sage: cython(os.linesep.join(cython_code))
sage: A1.B1.C1??          
Error getting source: class A1.B1.C1 has no attribute '__class__'
Type:		classobj
String Form:	_mnt_local_king__sage_temp_mpc622_6475_tmp_0_spyx_0.A1.B1.C1
Namespace:	Interactive
Loaded File:	/mnt/local/king/.sage/temp/mpc622/6475/spyx/_mnt_local_king__sage_temp_mpc622_6475_tmp_0_spyx/_mnt_local_king__sage_temp_mpc622_6475_tmp_0_spyx_0.so
Source File:	/mnt/local/king/.sage/temp/mpc622/6475/spyx/_mnt_local_king__sage_temp_mpc622_6475_tmp_0_spyx/_mnt_local_king__sage_temp_mpc622_6475_tmp_0_spyx_0.so
```

Even #11768 does not solve the problem.

Shall that be dealt with on a different ticket? Or in one go?

Probably on a different ticket, since I just find that even source inspection for A1 (which has a usual name) does not work...


---

Comment by SimonKing created at 2012-05-03 16:16:56

For the record: If #11791 is applied after this ticket, source inspection in the example above works (and is doctested).


---

Comment by SimonKing created at 2012-08-13 13:10:22

Is there a reviewer to fix name mangling of nested classes (needed in the category framework)?


---

Comment by saliola created at 2012-08-23 01:01:17

This patch also fixes an issue that came up in #8899 regarding documentation of nested classes not appearing in the reference manual.

See here for a description of the issue, see the [thread on sage-combinat-devel](https://groups.google.com/d/topic/sage-combinat-devel/gWVx1It60ao/discussion).

See here for the confirmation that this works: http://trac.sagemath.org/sage_trac/ticket/8899#comment:31


---

Comment by vbraun created at 2012-11-27 10:42:39

LGTM!


---

Comment by vbraun created at 2012-11-27 10:42:39

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-12-19 15:37:28

This causes trouble when building the documentation from scratch (i.e. after deleting 'devel/sage/doc/output`):

```
/usr/local/src/sage-5.5.rc1/local/lib/python2.7/site-packages/sage/categories/algebras_with_basis.py:docstring of sage.categories.algebras_with_basis.AlgebrasWithBasis.CartesianProducts.ParentMethods.one_from_cartesian_product_of_one_basis:3: WARNING: more than one target found for cross-reference u'one_basis': sage.combinat.sf.new_kschur.KBoundedSubspaceBases.ParentMethods.one_basis, sage.categories.algebras_with_basis.AlgebrasWithBasis.ParentMethods.one_basis, sage.combinat.ncsf_qsym.generic_basis_code.BasesOfQSymOrNCSF.ParentMethods.one_basis, sage.algebras.steenrod.steenrod_algebra.SteenrodAlgebra_generic.one_basis, sage.categories.examples.with_realizations.SubsetAlgebra.Fundamental.one_basis, sage.combinat.root_system.weyl_characters.WeightRing.one_basis, sage.categories.monoids.Monoids.Algebras.ParentMethods.one_basis, sage.categories.examples.hopf_algebras_with_basis.MyGroupAlgebra.one_basis, sage.categories.algebras_with_basis.AlgebrasWithBasis.TensorProducts.ParentMethods.one_basis, sage.algebras.affine_nil_temperley_lieb.AffineNilTemperleyLiebTypeA.one_basis, sage.categories.examples.algebras_with_basis.FreeAlgebra.one_basis, sage.combinat.symmetric_group_algebra.SymmetricGroupAlgebra_n.one_basis, sage.algebras.iwahori_hecke_algebra.IwahoriHeckeAlgebraT.one_basis, sage.algebras.group_algebra_new.GroupAlgebra.one_basis, sage.combinat.sf.sfa.SymmetricFunctionsBases.ParentMethods.one_basis, sage.combinat.root_system.weyl_characters.WeylCharacterRing.one_basis, sage.combinat.combinatorial_algebra.CombinatorialAlgebra.one_basis
```



---

Comment by jdemeyer created at 2012-12-19 15:38:07

Changing status from positive_review to needs_work.


---

Comment by SimonKing created at 2013-01-19 18:30:18

Jeroen, can you elaborate a bit what went wrong?


---

Comment by SimonKing created at 2013-01-19 20:27:44

Aha, now I see that the very long single line contains warnings about cross references that were not found. I'll try to identify them.


---

Comment by SimonKing created at 2013-01-19 20:33:29

Aha, here is an example:

The docstring of `sage.categories.algebras_with_basis.AlgebrasWithBasis.CartesianProducts.ParentMethods.one_from_cartesian_product_of_one_basis` is as follows:

```
            @cached_method   # todo: reinstate once #5843 is fixed
            def one_from_cartesian_product_of_one_basis(self):
                """
                Returns the one of this cartesian product of algebras, as per ``Monoids.ParentMethods.one``

                It is constructed as the cartesian product of the ones of the
                summands, using their :meth:`.one_basis` methods.

                This implementation does not require multiplication by
                scalars nor calling cartesian_product. This might help keeping
                things as lazy as possible upon initialization.
...
```


Could this simply be a misspelling? Note that it is written

```
:meth:`.one_basis`
```

but should certainly be

```
:meth:`one_basis`
```


If that's the case for the other warnings as well, then my patch would just uncover mistakes that happened earlier.


---

Comment by jhpalmieri created at 2013-01-19 20:49:19

The same issue arose in #13851 (see [comment 10](http://trac.sagemath.org/sage_trac/ticket/13851#comment:10)). I'm not sure why those dots are there, and I personally think they should be removed, but someone intentionally put them there.


---

Comment by SimonKing created at 2013-01-19 20:54:54

Replying to [comment:14 jhpalmieri]:
> The same issue arose in #13851 (see [comment 10](http://trac.sagemath.org/sage_trac/ticket/13851#comment:10)). I'm not sure why those dots are there, and I personally think they should be removed, but someone intentionally put them there.

I think the dot is simply wrong - or is it ignored by Sphinx?

Actually here it is even worse. The text is documentation of a functorial construction, but refers to a parent method - that can't possibly work without an explicit reference to the method which must include the class which the method belongs to.


---

Attachment

Fix a cross reference in some functorial construction


---

Comment by SimonKing created at 2013-01-19 21:13:25

Does the second patch fix the problem? I am now explicitly referring to the `one_basis` method of `AlgebrasWithBasis.ParentMethods`.


---

Comment by SimonKing created at 2013-01-19 21:13:25

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2013-03-20 15:25:03

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2013-03-20 15:25:03

Hi Simon,

I again hit this one compiling the doc. Your patches look all good to me, including the one problem.

Thanks,

Florent


---

Comment by jdemeyer created at 2013-03-21 06:36:57

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-03-21 06:36:57

Applying this patch causes the PDF docbuilder to hang after it's done building all documents. All documents are built but there are still 6 (I'm building with `MAKE="make -j6"`) child processes which are stuck in the `multiprocessing.Pool` code. Interrupting those child processes simply causes new child processes to start which are then stuck again. It might be a bug in `multiprocessing.Pool` which is somehow triggered, I have no idea...


---

Comment by jdemeyer created at 2013-03-21 06:38:33

Perhaps an instance of #14323 (wild guess)?


---

Comment by jdemeyer created at 2013-03-24 12:31:50

No, #14323 doesn't help.


---

Comment by SimonKing created at 2013-05-22 11:06:20

Jeroen, does the problem persist with the new doc builder? I have just applied the two patches, and succeeded with `export MAKE="make -j2"` followed by `make`.

However, there is continuation by `...` that needs fixing.


---

Attachment


---

Comment by SimonKing created at 2013-05-22 13:00:25

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2013-05-22 13:00:25

Building the docs works for me, and the `...` should be fixed now. Hence: Needs review!

Apply trac9107_nesting_nested_classes.patch trac_9107_fix_cross_reference.patch


---

Comment by jdemeyer created at 2013-05-22 15:05:04

Replying to [comment:22 SimonKing]:
> Building the docs works for me
Also the PDF docs?


---

Comment by jdemeyer created at 2013-05-22 15:08:05

There is a problem with latex and the fact that the docbuilder _hangs_ is a bug in the new docbuilder: #14626

```
! LaTeX Error: Too deeply nested.

See the LaTeX manual or LaTeX Companion for explanation.
Type  H <return>  for immediate help.
 ...                                              
                                                  
l.27819 \begin{Verbatim}[commandchars=\\\{\}]
                                             
? 
Implicit mode ON; LaTeX internals redefined
(/usr/share/texmf-texlive/tex/latex/ltxmisc/url.sty
(/usr/share/texmf-texlive/tex/latex/base/t1enc.def)
! Emergency stop.
 ...                                              
                                                  
l.27819 \begin{Verbatim}[commandchars=\\\{\}]
                                             
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on categories.log.
)make[1]: *** [categories.pdf] Error 1
```



---

Comment by jdemeyer created at 2013-05-22 15:10:38

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2013-05-22 15:23:15

Yes, I did not consider the pdf docs.

If I understand correctly, we have two problems. The first problem is that with this patch, `LaTeX` is produced that can not be processed because it is two deeply nested. The second problem is independent, namely if latex fails, then the docbuilder hangs.

Do you have any clue what object is being processed when things hang?


---

Comment by jdemeyer created at 2013-05-22 15:29:04

Replying to [comment:26 SimonKing]:
> The second problem is independent, namely if latex fails, then the docbuilder hangs.
Which is #14626 and indeed has nothing to do with this ticket.

> Do you have any clue what object is being processed when things hang?
Not yet, I will reproduce the `.tex` file and then it should be clear.


---

Comment by jdemeyer created at 2013-05-22 15:48:01

Offending `.tex` file: [http://boxen.math.washington.edu/home/jdemeyer/badlatex/categories.tex](http://boxen.math.washington.edu/home/jdemeyer/badlatex/categories.tex)

The relevant lines are

```
\begin{fulllineitems}
\phantomsection\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods}\pysigline{\strong{class }\bfcode{ParentMethods}}~\index{Sets.WithRealizations.ParentMethods.Realizations (class in sage.categories.sets\_cat)}

\begin{fulllineitems}
\phantomsection\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods.Realizations}\pysiglinewithargsret{\strong{class }\bfcode{Realizations}}{\emph{parent\_with\_realization}}{}
Bases: {\hyperref[sage/categories/realizations:sage.categories.realizations.Category_realization_of_parent]{\code{sage.categories.realizations.Category\_realization\_of\_parent}}}

TESTS:

\begin{Verbatim}[commandchars=\\\{\}]
\PYG{g+gp}{sage: }\PYG{k+kn}{from} \PYG{n+nn}{sage.categories.realizations} \PYG{k+kn}{import} \PYG{n}{Category\PYGZus{}realization\PYGZus{}of\PYGZus{}parent}
\PYG{g+gp}{sage: }\PYG{n}{A} \PYG{o}{=} \PYG{n}{Sets}\PYG{p}{(}\PYG{p}{)}\PYG{o}{.}\PYG{n}{WithRealizations}\PYG{p}{(}\PYG{p}{)}\PYG{o}{.}\PYG{n}{example}\PYG{p}{(}\PYG{p}{)}\PYG{p}{;} \PYG{n}{A}
\PYG{g+go}{The subset algebra of \PYGZob{}1, 2, 3\PYGZcb{} over Rational Field}
\PYG{g+gp}{sage: }\PYG{n}{C} \PYG{o}{=} \PYG{n}{A}\PYG{o}{.}\PYG{n}{Realizations}\PYG{p}{(}\PYG{p}{)}\PYG{p}{;} \PYG{n}{C}
\PYG{g+go}{Category of realizations of The subset algebra of \PYGZob{}1, 2, 3\PYGZcb{} over Rational Field}
\PYG{g+gp}{sage: }\PYG{n+nb}{isinstance}\PYG{p}{(}\PYG{n}{C}\PYG{p}{,} \PYG{n}{Category\PYGZus{}realization\PYGZus{}of\PYGZus{}parent}\PYG{p}{)}
\PYG{g+go}{True}
\PYG{g+gp}{sage: }\PYG{n}{C}\PYG{o}{.}\PYG{n}{parent\PYGZus{}with\PYGZus{}realization}
\PYG{g+go}{The subset algebra of \PYGZob{}1, 2, 3\PYGZcb{} over Rational Field}
\PYG{g+gp}{sage: }\PYG{n}{TestSuite}\PYG{p}{(}\PYG{n}{C}\PYG{p}{)}\PYG{o}{.}\PYG{n}{run}\PYG{p}{(}\PYG{p}{)}
\end{Verbatim}
\index{super\_categories() (sage.categories.sets\_cat.Sets.WithRealizations.ParentMethods.Realizations method)}

\begin{fulllineitems}
\phantomsection\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods.Realizations.super_categories}\pysiglinewithargsret{\bfcode{super\_categories}}{}{}
EXAMPLES:

\begin{Verbatim}[commandchars=\\\{\}]   %% PROBLEM IS THIS LINE %%
\PYG{g+gp}{sage: }\PYG{n}{A} \PYG{o}{=} \PYG{n}{Sets}\PYG{p}{(}\PYG{p}{)}\PYG{o}{.}\PYG{n}{WithRealizations}\PYG{p}{(}\PYG{p}{)}\PYG{o}{.}\PYG{n}{example}\PYG{p}{(}\PYG{p}{)}\PYG{p}{;} \PYG{n}{A}
\PYG{g+go}{The subset algebra of \PYGZob{}1, 2, 3\PYGZcb{} over Rational Field}
\PYG{g+gp}{sage: }\PYG{n}{A}\PYG{o}{.}\PYG{n}{Realizations}\PYG{p}{(}\PYG{p}{)}\PYG{o}{.}\PYG{n}{super\PYGZus{}categories}\PYG{p}{(}\PYG{p}{)}
\PYG{g+go}{[Category of realizations of sets]}
\end{Verbatim}

\end{fulllineitems}


\end{fulllineitems}

\index{facade\_for() (sage.categories.sets\_cat.Sets.WithRealizations.ParentMethods method)}
```



---

Comment by jdemeyer created at 2013-05-22 15:54:55

*before* this patch (good):

```
\phantomsection\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods}\pysigline{\bfcode{ParentMethods}}
alias of \code{WithRealizations.ParentMethods}
```

*after* this patch (bad):

```
\phantomsection\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods.Realizations}\pysiglinewithargsret{\strong{class }\bfcode{Realizations}}{\emph{parent\_with\_realization}}{}
Bases: {\hyperref[sage/categories/realizations:sage.categories.realizations.Category_realization_of_parent]{\code{sage.categories.realizations.Category\_realization\_of\_parent}}}
```



---

Comment by SimonKing created at 2013-05-22 19:35:19

Replying to [comment:29 jdemeyer]:
> *before* this patch (good):
> {{{
> \phantomsection\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods}\pysigline{\bfcode{ParentMethods}}
> alias of \code{WithRealizations.ParentMethods}
> }}}
> *after* this patch (bad):
> {{{
> \phantomsection\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods.Realizations}\pysiglinewithargsret{\strong{class }\bfcode{Realizations}}{\emph{parent\_with\_realization}}{}
> Bases: {\hyperref[sage/categories/realizations:sage.categories.realizations.Category_realization_of_parent]{\code{sage.categories.realizations.Category\_realization\_of\_parent}}}
> }}}

Three questions:

1. Why is it bad? I don't see why latex should have a problem with it.
2. Isn't the "good" output without my patch just plain wrong? After all, we do have
   {{{
sage: sage.categories.sets_cat.Sets.WithRealizations.ParentMethods.Realizations.__bases__
(sage.categories.realizations.Category_realization_of_parent,)
   }}}
   and also `sage.categories.sets_cat.Sets.WithRealizations.ParentMethods.Realizations` is certainly _not_ simply an alias of `WithRealizations.ParentMethods`.
3. Can you also point me to the code that created the latex output?


---

Comment by jhpalmieri created at 2013-05-22 22:21:48

When I build the pdf docs, it works. On what machine do you see the failure? If it's on sage.math, it might have to do with the fact that the LaTeX installation is quite old...

Edit: maybe I'm seeing the failure now. Never mind.


---

Comment by SimonKing created at 2013-05-23 05:32:38

OK, I see it, too.

```
../../sage -docbuild reference pdf
...
Output written on tensor.pdf (24 pages, 144532 bytes).
Transcript written on tensor.log.
Build finished.  The built documents can be found in /home/simon/SAGE/prerelease/sage-5.9.rc0/devel/sage/doc/output/pdf/en/reference/tensor
```

and then it hangs.

Nevertheless, I have no clue what is happening here. See my three questions in comment:30.


---

Comment by jdemeyer created at 2013-05-23 08:03:29

Replying to [comment:30 SimonKing]:
> 1. Why is it bad?
I just used "bad" because `latex` doesn't compile it correctly.

> 3. Can you also point me to the code that created the latex output?
I guess that's Sphinx, but I don't know much about it.


---

Comment by SimonKing created at 2013-05-23 09:35:49

Replying to [comment:33 jdemeyer]:
> Replying to [comment:30 SimonKing]:
> > 1. Why is it bad?
> I just used "bad" because `latex` doesn't compile it correctly.

That was my question: Why does `latex` not compile it correctly?

And we should keep in mind that the old output has simply been wrong.


---

Comment by jhpalmieri created at 2013-05-23 19:20:36

I think that the first line in the LaTeX error message is correct:

```
! LaTeX Error: Too deeply nested.
```

I think that there are too many levels of nesting of lists (from the `fulllineitems` environment). If I comment out the `Verbatim` environment that it's complaining about, I don't get an error message any more.


---

Comment by SimonKing created at 2013-05-23 20:35:57

Replying to [comment:35 jhpalmieri]:
> I think that the first line in the LaTeX error message is correct:
> {{{
> ! LaTeX Error: Too deeply nested.
> }}}
> I think that there are too many levels of nesting of lists (from the `fulllineitems` environment). If I comment out the `Verbatim` environment that it's complaining about, I don't get an error message any more.

Please, where is the nesting? I suppose by "comment out the `Verbatim` environment that it's complaining about", you mean one of two `Verbatim` environments that were cited in comment:28.

The first is

```
\begin{Verbatim}[commandchars=\\\{\}]
\PYG{g+gp}{sage: }\PYG{k+kn}{from} \PYG{n+nn}{sage.categories.realizations} \PYG{k+kn}{import} \PYG{n}{Category\PYGZus{}realization\PYGZus{}of\PYGZus{}parent}
\PYG{g+gp}{sage: }\PYG{n}{A} \PYG{o}{=} \PYG{n}{Sets}\PYG{p}{(}\PYG{p}{)}\PYG{o}{.}\PYG{n}{WithRealizations}\PYG{p}{(}\PYG{p}{)}\PYG{o}{.}\PYG{n}{example}\PYG{p}{(}\PYG{p}{)}\PYG{p}{;} \PYG{n}{A}
\PYG{g+go}{The subset algebra of \PYGZob{}1, 2, 3\PYGZcb{} over Rational Field}
\PYG{g+gp}{sage: }\PYG{n}{C} \PYG{o}{=} \PYG{n}{A}\PYG{o}{.}\PYG{n}{Realizations}\PYG{p}{(}\PYG{p}{)}\PYG{p}{;} \PYG{n}{C}
\PYG{g+go}{Category of realizations of The subset algebra of \PYGZob{}1, 2, 3\PYGZcb{} over Rational Field}
\PYG{g+gp}{sage: }\PYG{n+nb}{isinstance}\PYG{p}{(}\PYG{n}{C}\PYG{p}{,} \PYG{n}{Category\PYGZus{}realization\PYGZus{}of\PYGZus{}parent}\PYG{p}{)}
\PYG{g+go}{True}
\PYG{g+gp}{sage: }\PYG{n}{C}\PYG{o}{.}\PYG{n}{parent\PYGZus{}with\PYGZus{}realization}
\PYG{g+go}{The subset algebra of \PYGZob{}1, 2, 3\PYGZcb{} over Rational Field}
\PYG{g+gp}{sage: }\PYG{n}{TestSuite}\PYG{p}{(}\PYG{n}{C}\PYG{p}{)}\PYG{o}{.}\PYG{n}{run}\PYG{p}{(}\PYG{p}{)}
\end{Verbatim}
```

the second is

```
\begin{Verbatim}[commandchars=\\\{\}]   %% PROBLEM IS THIS LINE %%
\PYG{g+gp}{sage: }\PYG{n}{A} \PYG{o}{=} \PYG{n}{Sets}\PYG{p}{(}\PYG{p}{)}\PYG{o}{.}\PYG{n}{WithRealizations}\PYG{p}{(}\PYG{p}{)}\PYG{o}{.}\PYG{n}{example}\PYG{p}{(}\PYG{p}{)}\PYG{p}{;} \PYG{n}{A}
\PYG{g+go}{The subset algebra of \PYGZob{}1, 2, 3\PYGZcb{} over Rational Field}
\PYG{g+gp}{sage: }\PYG{n}{A}\PYG{o}{.}\PYG{n}{Realizations}\PYG{p}{(}\PYG{p}{)}\PYG{o}{.}\PYG{n}{super\PYGZus{}categories}\PYG{p}{(}\PYG{p}{)}
\PYG{g+go}{[Category of realizations of sets]}
\end{Verbatim}
```


I suppose `%% PROBLEM IS THIS LINE %%` in the second environment was Jeroen's addition.

So, what is "too deeply nested"? I can't believe that such a short piece of text has even enough characters to nest too deeply for latex!


---

Comment by jhpalmieri created at 2013-05-23 23:25:05

If I take the file categories.tex in `SAGE_ROOT/devel/sage/doc/output/latex/en/reference/categories/` and truncate it just before the line starting `\index{facade\_for() ...`, then I need to add in a few lines of the form

```
\end{fulllineitems}
```

to get it to compile (after I comment out the last Verbatim block before the line `\index{facade\_for() ...`). So there are several `fulllineitems` environments nested within each other. Maybe too many, and maybe that's the problem. That's my current guess.


---

Comment by tscrim created at 2013-08-22 19:13:24

Hey Nicolas and Simon,

The problem comes from the fact that there is a 4 level deep class nesting with a method (which is 5 levels deep) in the `Sets.WithRealizations.ParentMethods.Realizations.super_categories`. I've tried moving this subclass into a separate class, and this solves the pdf build issue but introduces some doctesting errors. I don't think there is a  to extend the nesting level since that is a latex thing, nor do I think we should try since 4 nested classes is a lot IMO. I'm guessing beforehand because of the improper naming, latex did the environments differently...?

Anyways the fix for the pdf build is to remove a level (or two) of class nesting.

Best,

Travis

Edit: Here are the errors I get when I move `Sets.WithRealizations` out as a separate class and then assign it into `Sets`:

```
sage -t ../categories/sets_cat.py
**********************************************************************
File "../categories/sets_cat.py", line 1408, in sage.categories.sets_cat.ParentMethodsForWithRealizations.realizations
Failed example:
    A.realizations()
Expected:
    [The subset algebra of {1, 2, 3} over Rational Field in the Fundamental basis, The subset algebra of {1, 2, 3} over Rational Field in the In basis, The subset algebra of {1, 2, 3} over Rational Field in the Out basis]
Got:
    [The subset algebra of {1, 2, 3} over Rational Field in the Fundamental basis, The subset algebra of {1, 2, 3} over Rational Field in the In basis, The subset algebra of {1, 2, 3} over Rational Field in the Out basis, The subset algebra of {1, 2, 3} over Rational Field in the realization Blah]
**********************************************************************
File "../categories/sets_cat.py", line 1428, in sage.categories.sets_cat.ParentMethodsForWithRealizations.facade_for
Failed example:
    A.facade_for()
Expected:
    [The subset algebra of {1, 2, 3} over Rational Field in the Fundamental basis, The subset algebra of {1, 2, 3} over Rational Field in the In basis, The subset algebra of {1, 2, 3} over Rational Field in the Out basis]
Got:
    [The subset algebra of {1, 2, 3} over Rational Field in the Fundamental basis, The subset algebra of {1, 2, 3} over Rational Field in the In basis, The subset algebra of {1, 2, 3} over Rational Field in the Out basis, The subset algebra of {1, 2, 3} over Rational Field in the realization Blah]
**********************************************************************
2 items had failures:
   1 of   8 in sage.categories.sets_cat.ParentMethodsForWithRealizations.facade_for
   1 of   3 in sage.categories.sets_cat.ParentMethodsForWithRealizations.realizations
    [241 tests, 2 failures, 0.76 s]
----------------------------------------------------------------------
sage -t ../categories/sets_cat.py  # 2 doctests failed
----------------------------------------------------------------------
```

Any ideas why moving the class out of the nesting doesn't work?


---

Comment by SimonKing created at 2013-08-22 19:27:35

Replying to [comment:39 tscrim]:
> I don't think there is a  to extend the nesting level since that is a latex thing,

Shame on LaTeX!

> Anyways the fix for the pdf build is to remove a level (or two) of class nesting.

What exactly are we talking about? `Sets.WithRealizations.ParentMethods.Realizations`?

Interestingly, there is the comment

```
# Do we really want this feature?
```


So, can we do without this feature? Nicolas?


---

Comment by tscrim created at 2013-08-23 04:02:07

Replying to [comment:40 SimonKing]:
> Replying to [comment:39 tscrim]:
> > Anyways the fix for the pdf build is to remove a level (or two) of class nesting.
> 
> What exactly are we talking about? `Sets.WithRealizations.ParentMethods.Realizations`?

Yes. Removing a level of nesting allowed the pdf for categories to build for me.


---

Comment by nthiery created at 2013-08-23 08:52:45

Thanks much Travis for investigating!

I agree that there should be a recommendation for not nesting classes
too deep, for the sake of readability. But having a hard arbitrary
limit -- especially that small -- is annoying. Shame on LaTeX. Of
course, one can always spin off a subtree of nested classes into a
separate tree, but there are cases where one has a deep tree with very
few lines and no natural splitting point. For example, #10963
introduces

```
    DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative.AdditiveUnital.AdditiveInverse
```


Hmm. Altogether, I would call this a LaTeX arbitrary hard
limitation. Luckily there seems to be an easy solution to increase
this limitation to something large enough to cover our current use
cases, namely to use the package enumitem [1]. By itself, it brings
the nesting level to 6, and we could even increase it further (10
should be really safe) using \setlistdepth{9}.

I have attached the little latex file I used for testing.

What do you think? Shall we add enumitems to the list of latex
packages loaded by Sphinx? Is this standard enough, or shall we add
enumitem.sty to the Sage distribution?

Cheers,
                                     Nicolas

[1] http://stackoverflow.com/questions/1935952/maximum-nesting-level-of-lists-in-latex


---

Attachment


---

Comment by jdemeyer created at 2013-08-23 09:02:52

`enumitem.sty` looks pretty standard, so I'd say it's fine to use it.


---

Comment by SimonKing created at 2013-08-23 10:31:04

Replying to [comment:43 jdemeyer]:
> `enumitem.sty` looks pretty standard, so I'd say it's fine to use it.

... which means there should be a separate ticket for adding it?


---

Comment by jdemeyer created at 2013-08-23 11:28:29

Replying to [comment:44 SimonKing]:

> ... which means there should be a separate ticket for adding it?
Adding an `\usepackage{}` somewhere (don't ask me where) should be trivial enough that it can be done on this ticket.


---

Comment by SimonKing created at 2013-08-23 11:55:58

Replying to [comment:45 jdemeyer]:
> Replying to [comment:44 SimonKing]:
> > ... which means there should be a separate ticket for adding it?
> Adding an `\usepackage{}` somewhere (don't ask me where) should be trivial enough that it can be done on this ticket.

So, whom *do* we ask?


---

Comment by tscrim created at 2013-08-23 15:31:26

Me; I just did this with Ben on #14787. You need to add it to `doc/common/conf.py`, and we also added it to `misc/latex.py`, which might be some overkill, but it doesn't really hurt to be extra safe here.


---

Comment by SimonKing created at 2013-08-23 19:39:18

Replying to [comment:47 tscrim]:
> Me; I just did this with Ben on #14787. You need to add it to `doc/common/conf.py`, and we also added it to `misc/latex.py`, which might be some overkill, but it doesn't really hurt to be extra safe here.

Are you saying that the problem is fixed by #14787? Then I suggest to add it as dependency.


---

Comment by tscrim created at 2013-08-23 23:44:41

Replying to [comment:48 SimonKing]:
> Replying to [comment:47 tscrim]:
> > Me; I just did this with Ben on #14787. You need to add it to `doc/common/conf.py`, and we also added it to `misc/latex.py`, which might be some overkill, but it doesn't really hurt to be extra safe here.
> 
> Are you saying that the problem is fixed by #14787? Then I suggest to add it as dependency.

Sorry, that was phrased badly. Ben and I added a latex package to the pdf builder in #14787, but it was not `enumitem.sty`.


---

Comment by nthiery created at 2013-08-27 11:04:52

For the record: someone else got a similar issue when using sphinx [1], and suggested the same fix. Alas this fix does not seem to be enough. I am still getting a "Too deeply nested" with the attached file categories.tex (obtained by reducing that produced by sphinx). I am working on reducing it further.


[1] http://mail.scipy.org/pipermail/ipython-user/2012-May/010144.html


---

Attachment


---

Comment by SimonKing created at 2013-08-27 11:11:36

Hi Nicolas,

Replying to [comment:51 nthiery]:
> For the record: someone else got a similar issue when using sphinx [1], and suggested the same fix. Alas this fix does not seem to be enough.

What exactly did you do? Change sphinx.sty, as in the source you are giving? Or change doc/common/conf.py and misc/latex.py, as advised by Travis in comment:47?

Could it be that the following comment from [the page you are citing](http://mail.scipy.org/pipermail/ipython-user/2012-May/010144.html) applies?

```
However this requires version 3.0 of enumitem, which doesn't yet ship
with many linux latex distributions.
```



---

Comment by nthiery created at 2013-08-27 12:36:17

Replying to [comment:52 SimonKing]:
> Replying to [comment:51 nthiery]:
> > For the record: someone else got a similar issue when using sphinx [1], and suggested the same fix. Alas this fix does not seem to be enough.
> 
> What exactly did you do? Change sphinx.sty, as in the source you are giving? Or change doc/common/conf.py and misc/latex.py, as advised by Travis in comment:47?

I changed conf.py which properly added it to the generated
categories.tex file (see the top of that file).

> Could it be that the following comment from [the page you are citing](http://mail.scipy.org/pipermail/ipython-user/2012-May/010144.html) applies?
> {{{
> However this requires version 3.0 of enumitem, which doesn't yet ship
> with many linux latex distributions.
> }}}
> 

I have 3.5.2 ...


---

Comment by SimonKing created at 2013-08-27 12:53:53

Replying to [comment:53 nthiery]:
> Replying to [comment:52 SimonKing]:
> > What exactly did you do? Change sphinx.sty, as in the source you are giving? Or change doc/common/conf.py and misc/latex.py, as advised by Travis in comment:47?
> 
> I changed conf.py which properly added it to the generated
> categories.tex file (see the top of that file).

Hm. Then, we are back to the question: What the heck is going wrong? Could we
perhaps ask on some `LaTeX` forum about the problem? I mean, if we have a tex
file that does not compile, even though nesting should not be the problem any
more, then I think `LaTeX` people should be made aware.


---

Comment by SimonKing created at 2013-08-27 12:56:29

How can one test [attachment:categories.tex]? I can not run pdflatex on it, because it can't find `sphinxmanual.cls`. Where do I get this file (and probably other files) from?


---

Comment by SimonKing created at 2013-08-27 14:55:09

Replying to [comment:55 SimonKing]:
> How can one test [attachment:categories.tex]? I can not run pdflatex on it, because it can't find `sphinxmanual.cls`. Where do I get this file (and probably other files) from?

When I do `declare -x TEXINPUTS=.:$SAGE_ROOT/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/texinputs/` then it does find sphinxmanual.cls, but the next attempt to call pdflatex on categories.tex fails as well. This time, it can't find `report.cls`.

So, please tell me how one is supposed to run pdflatex on this file, so that I can reproduce the problem.


---

Comment by nthiery created at 2013-08-28 09:23:49

Replying to [comment:56 SimonKing]:
> Replying to [comment:55 SimonKing]:
> > How can one test [attachment:categories.tex]? I can not run pdflatex on it, because it can't find `sphinxmanual.cls`. Where do I get this file (and probably other files) from?

> When I do `declare -x TEXINPUTS=.:$SAGE_ROOT/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/texinputs/` then it does find sphinxmanual.cls, but the next attempt to call pdflatex on categories.tex fails as well. This time, it can't find `report.cls`.

You are missing a : at the end of TEXINPUT to let latex use its own library (report.cls is a standard class). 

Or you can just be lazy and put the categories.tex file in the directory 

```
        <SAGE>/devel/sage/doc/output/latex/en/reference/categories
```

and run pdflatex from there.


---

Comment by SimonKing created at 2013-08-28 09:43:54

Replying to [comment:57 nthiery]:
> Replying to [comment:56 SimonKing]:
> > When I do `declare -x TEXINPUTS=.:$SAGE_ROOT/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/texinputs/` then it does find sphinxmanual.cls, but the next attempt to call pdflatex on categories.tex fails as well. This time, it can't find `report.cls`.
>
> You are missing a : at the end of TEXINPUT to let latex use its own library (report.cls is a standard class). 

Nope. After

```
declare -x TEXINPUTS=.:~/SAGE/prerelease/sage-5.11.beta3/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/texinputs/:
```

`pdflatex categories.tex` results in

```
! Undefined control sequence.
<recently read> \setlistdepth 
                              
l.19 \setlistdepth
                  {9}
? 
! Emergency stop.
<recently read> \setlistdepth 
                              
l.19 \setlistdepth
                  {9}
!  ==> Fatal error occurred, no output PDF file produced!
```


 > Or you can just be lazy and put the categories.tex file in the directory 
> {{{
>         <SAGE>/devel/sage/doc/output/latex/en/reference/categories
> }}}
> and run pdflatex from there.

Nope, because this folder doesn't exist. Do I need to attempt building the pdf documentation first?


---

Comment by SimonKing created at 2013-08-28 09:45:45

PS: Changing

```
\RequirePackage{enumitem}
```

into

```
\usepackage{enumitem}
```

did not help.


---

Comment by SimonKing created at 2013-08-28 10:24:17

Aha. The log shows:

```
enumitem 2009/05/18 v2.2 Customized lists
```

and I guess that's too old.


---

Comment by SimonKing created at 2013-08-28 10:41:56

OK, after getting a more recent version of the enumitem package, I first get a "too deeply nested" error on [attachment:categories.tex]. However, after doing

```
\setlistdepth{10}
```

(and not just depth 9), it compiles fine.

So, in other words, the problem _can_ be solved. But I really wonder about the requirement that the user has to have a latex installation with a very recent enumitem. Can this be really required? Or would we be allowed to ship enumitem.sty with Sage?


---

Comment by SimonKing created at 2013-08-28 10:44:29

Output of pdflatex after doing setlistdept(10) in categories.tex


---

Attachment

Well, it does compile, but it does not work. Look at the ugly output in [attachment:categories.pdf].


---

Comment by nthiery created at 2013-08-28 12:54:14

Replying to [comment:61 SimonKing]:
> OK, after getting a more recent version of the enumitem package, I first get a "too deeply nested" error on [attachment:categories.tex]. However, after doing
> {{{
> \setlistdepth{10}
> }}}
> (and not just depth 9), it compiles fine.
> So, in other words, the problem _can_ be solved.

What? Really? I thought I had tried that. Ah, I see, the level that
you have to put seems to actually have nothing to do with the actual
depth of your itemize. Now I can compile the full categories
documentation, but that requires `\setlistdepth{275`}!!! There
must be something wrong in the depth-counting logic of enumitem ...

> But I really wonder about the requirement that the user has to have
> a latex installation with a very recent enumitem. Can this be really
> required? Or would we be allowed to ship enumitem.sty with Sage?

I would vote for shipping enumitem.sty if that's easy. Jeroen/Volker/..., can we just throw it in
`/opt/sage-dev/local/share/texmf/tex/generic` ?


Cheers,
                                Nicolas


---

Comment by nthiery created at 2013-08-28 12:59:17

Replying to [comment:62 SimonKing]:
> Well, it does compile, but it does not work. Look at the ugly output in [attachment:categories.pdf].

Nothing to worry about: this filed was obtained by stripping lots of stuff from an actual tex file; I am not surprised it does not look good. On the other hand, I had a look at the full categories.pdf produced by sphinx, and it looked reasonable.


---

Comment by SimonKing created at 2013-08-28 13:06:04

Replying to [comment:63 nthiery]:
> Now I can compile the full categories
> documentation, but that requires `\setlistdepth{275`}!!! There
> must be something wrong in the depth-counting logic of enumitem ...

Ouch. So, if it really turns out that the depth-counting is broken (did you check that the nesting of lists in the created tex file are not broken?), then we should perhaps consider to search for an alternative solution.

For example, is it really needed to use nesting in the resulting tex file? Or could one create a nice layout without nesting? If I understand correctly, _we_ (i.e., Sage) are creating the tex file. Hence, we can control what happens.

> I would vote for shipping enumitem.sty if that's easy. Jeroen/Volker/..., can we just throw it in
> `/opt/sage-dev/local/share/texmf/tex/generic` ?

I have already asked on [sage-devel](https://groups.google.com/forum/#!topic/sage-devel/8Q-I0e2OESE)...


---

Comment by nthiery created at 2013-08-29 16:14:35

Replying to [comment:65 SimonKing]:
> I have already asked on [sage-devel](https://groups.google.com/forum/#!topic/sage-devel/8Q-I0e2OESE)...

Thanks for the pointer. I answered there.


---

Comment by vbraun created at 2014-06-12 14:01:04

Just require enumitems, geez... Afair we already require a number of packages that are not part of a "small"/"medium" TeXLive install. One more doesn't make a difference.


---

Comment by nthiery created at 2014-06-12 14:55:47

Yeah, you are right, let's make it simple. I for example had to install a bunch of language packages (russian, ...) to get the pdf doc to install a couple days ago.

First attempt pushed. Compiling the doc and running the tests now.

Cheers,
                            Nicolas


---

Comment by SimonKing created at 2014-06-12 15:54:38

Replying to [comment:69 vbraun]:
> Just require enumitems, geez... 

What exactly do you mean? Would it be sufficient to let Sage insert `usepackage{enumitem}` (I have not heard about the plural, `enumitems`), or will we also need to change the latex code emitted for nested classes? And how?


---

Comment by nthiery created at 2014-06-12 21:50:49

Replying to [comment:72 SimonKing]:
> What exactly do you mean? Would it be sufficient to let Sage insert `usepackage{enumitem}`

That's my understanding and what I did in my latest commit. Plus raising the depth limit to a stupidly high value.

There seems to still be some compilation issue, but I guess they are just due to more stuff getting compiled, hence catching glitches that had gone unnoticed so far. I'll check this out tomorrow.

Cheers,
                                Nicolas


---

Comment by nthiery created at 2014-06-13 09:24:44

Gosh, it turned out that using `\setlistdepth{275}` was not sufficient
anymore: I had to use `\setlistdepth{2000}`! This meant the problem
would just keep going to be worst and worst with time.

So I investigated a further and got lucky this time: if we replace
list by trivlist in the customized Verbatim defined by `sphinx.sty`,
then our documenation compiles smoothly, without even using enumitem.

I proposed this fix upstream:

https://bitbucket.org/birkenfeld/sphinx/issue/777/latex-output-too-deeply-nested

For the time being, I tweaked our conf.py to redefine and fix sphinx's
Verbatim.

Ok, now there just remains to check that all tests pass, and this will
be a needs review.

Cheers,
                              Nicolas
----
New commits:


---

Comment by tscrim created at 2014-06-13 16:52:40

Is there a reason why you don't patch the sphinx spkg directly?


---

Comment by nthiery created at 2014-06-13 19:35:15

Replying to [comment:76 tscrim]:
> Is there a reason why you don't patch the sphinx spkg directly?

Lazyness mostly. If someone whats to create a patch, adapt the spkg, ... please go ahead!


---

Comment by git created at 2014-06-13 19:43:01

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by nthiery created at 2014-06-13 19:44:51

Ok, there were a couple doctest failures, all to be expected since nested classes now have a correct name. Fixed now. So that's a needs review!


---

Comment by nthiery created at 2014-06-13 19:44:51

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2014-06-13 21:05:26

Here's a version with a patched version of the sphinx spkg. Although I think your pull request is based on v1.2 (but it still applied (for me) to our current v1.1). Could someone check to make sure I created the patch correctly (and tell me what I should do instead if it isn't right).
----
New commits:


---

Comment by git created at 2014-06-16 19:57:32

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by nthiery created at 2014-06-16 20:03:36

Replying to [comment:80 tscrim]:
> Here's a version with a patched version of the sphinx spkg.

Ah, that's nice: modifying standard spkgs is much simpler now that we have a single repository. Thanks!

> Although I think your pull request is based on v1.2 (but it still applied (for me) to our current v1.1). Could someone check to make sure I created the patch correctly (and tell me what I should do instead if it isn't right).

It seems to apply as it's supposed to (modulo trivial line offset).

I have made some minor improvement to the patch description.

I am a bit nervous about the removal of the former change log in SPKG.txt. But if someone can confirm that this is the right thing to do, that's ok for me.

Other than this, this sounds good to go!

Thanks again,
                                            Nicolas


---

Comment by vbraun created at 2014-06-16 21:02:55

Replying to [comment:82 nthiery]:
> I am a bit nervous about the removal of the former change log in SPKG.txt. But if someone can confirm that this is the right thing to do, that's ok for me.

Do it! ;-)


---

Comment by tscrim created at 2014-06-17 02:03:46

Then away we go.


---

Comment by tscrim created at 2014-06-17 02:03:46

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2014-06-18 12:39:16

Thanks for fixing this !!!


---

Comment by vbraun created at 2014-06-18 14:11:28

Resolution: fixed
