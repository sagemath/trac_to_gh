# Issue 9107: Nested class name mangling can be wrong in case of double nesting

archive/issues_009107.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  simonking zabrocki\n\nIn the following class tree:\n\n```\nclass Bla(UniqueRepresentation):\n    class Bla1(UniqueRepresentation):\n        class Bla11:\n\t    Pass\n    class Bla2:\n        class Bla21:\n\t    Pass\n```\n\nThe names are set to\n\n```\n        sage: Bla.Bla1.__name__\n        'Bla.Bla1'\n        sage: Bla.Bla2.__name__\n        'Bla.Bla2'\n        sage: Bla.Bla2.Bla21.__name__\n        'Bla.Bla2.Bla21'\n```\n\nBut\n\n```\n        sage: Bla.Bla1.Bla11.__name__\n        'Bla1.Bla11'\n```\n\nwhereas one would expect `'Bla.Bla1.Bla11'`\nThis breaks a lot of doc in categories and in particular in functorial constructions.\n\nFlorent\n\nIssue created by migration from https://trac.sagemath.org/ticket/9107\n\n",
    "created_at": "2010-05-31T20:52:31Z",
    "labels": [
        "categories",
        "major",
        "bug"
    ],
    "title": "Nested class name mangling can be wrong in case of double nesting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9107",
    "user": "hivert"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/9107





---

archive/issue_comments_084619.json:
```json
{
    "body": "I think we should make this depend on #12808, because it cythonises nested classes.\n\nHere is my analysis:\n\n1. In sage.misc.nested_class.modify_for_nested_pickling, only those attributes of a class are (recursively) renamed that are instances of type or of `ClassType`. However, ironically, instances of `NestedClassMetaclass` are ignored.\n2. It is verified that the name of the to-be-changed class is identical with its name as an attribute of the calling class. But the renaming breaks the identity.",
    "created_at": "2012-05-02T14:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84619",
    "user": "SimonKing"
}
```

I think we should make this depend on #12808, because it cythonises nested classes.

Here is my analysis:

1. In sage.misc.nested_class.modify_for_nested_pickling, only those attributes of a class are (recursively) renamed that are instances of type or of `ClassType`. However, ironically, instances of `NestedClassMetaclass` are ignored.
2. It is verified that the name of the to-be-changed class is identical with its name as an attribute of the calling class. But the renaming breaks the identity.



---

archive/issue_comments_084620.json:
```json
{
    "body": "I think the attached patch solves the problem. I get:\n\n```\nsage: class Bla(UniqueRepresentation):\n....:     class Bla1(UniqueRepresentation):\n....:         class Bla11:\n....:             pass\n....:     class Bla2:                   \n....:         class Bla21:   \n....:             pass\n....:         \nsage: Bla.Bla1.Bla11\n<class __main__.Bla.Bla1.Bla11 at 0x46e7808>\n```\n\n\nThe change is in `modify_for_nested_pickle`, which is called recursively. The idea is that the function should have an extra argument `first_run`, that is True by default. If the extra argument is False, then it is assumed that it is not applied for the first time.\n\nHere: Since Bla.Bla1 is an instance of `NestedClassMetaclass`, `modify_for_nested_pickle` is called on `Bla.Bla1.Bla11`, resulting in `Bla.Bla1.Bla11.__name__=='Bla1.Bla11'`. However, since Bla is an instance of `NestedClassMetaclass` as well, the function is applied to `Bla.Bla1` and thus recursively to `Bla.Bla1.Bla11` another time.\n\nNow, without my patch, in the second run, `modify_for_nested_pickle` would be confused by the fact that `Bla.Bla1.__dict__` lists `Bla.Bla1.Bla11` under the name `Bla11`, but `Bla11.__name__=='Bla1.Bla11'`. With my patch, `modify_for_nested_pickle` expects exactly that naming scheme, and is thus changing `Bla.Bla1.Bla11.__name__` into `\"Bla.Bla1.Bla11\"`.\n\nMuch BlaBla, but I think it works...\n\n**__Potential problems__**\n\n\n```\nsage: module = sys.modules['__main__']\nsage: getattr(module, 'Bla1.Bla11')                      \n<class __main__.Bla.Bla1.Bla11 at 0x46e7808>\nsage: getattr(module, 'Bla.Bla1.Bla11')\n<class __main__.Bla.Bla1.Bla11 at 0x46e7808>\n```\n\nHence, Bla.Bla1.Bla11 is listed in the module under two different names. If you think it is bad, then one could probably modify the function when first_run is false, such that the name given in the first run is erased from the module.\n\nMoreover, the reviewer will likely find a speed regression, when excessively creating nested unique representations. But that's hardly realistic...",
    "created_at": "2012-05-02T16:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84620",
    "user": "SimonKing"
}
```

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

**__Potential problems__**


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

archive/issue_comments_084621.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-02T16:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84621",
    "user": "SimonKing"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084622.json:
```json
{
    "body": "Another problem: Source inspection does not work yet in the following example.\n\n```\nsage: cython_code = [\n... \"from sage.structure.unique_representation import UniqueRepresentation\",\n... \"class A1(UniqueRepresentation):\",\n... \"    class B1(UniqueRepresentation):\",\n... \"        class C1: pass\",\n... \"    class B2:\",\n... \"        class C2: pass\"]\nsage: import os\nsage: cython(os.linesep.join(cython_code))\nsage: A1.B1.C1??          \nError getting source: class A1.B1.C1 has no attribute '__class__'\nType:\t\tclassobj\nString Form:\t_mnt_local_king__sage_temp_mpc622_6475_tmp_0_spyx_0.A1.B1.C1\nNamespace:\tInteractive\nLoaded File:\t/mnt/local/king/.sage/temp/mpc622/6475/spyx/_mnt_local_king__sage_temp_mpc622_6475_tmp_0_spyx/_mnt_local_king__sage_temp_mpc622_6475_tmp_0_spyx_0.so\nSource File:\t/mnt/local/king/.sage/temp/mpc622/6475/spyx/_mnt_local_king__sage_temp_mpc622_6475_tmp_0_spyx/_mnt_local_king__sage_temp_mpc622_6475_tmp_0_spyx_0.so\n```\n\nEven #11768 does not solve the problem.\n\nShall that be dealt with on a different ticket? Or in one go?\n\nProbably on a different ticket, since I just find that even source inspection for A1 (which has a usual name) does not work...",
    "created_at": "2012-05-02T16:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84622",
    "user": "SimonKing"
}
```

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

archive/issue_comments_084623.json:
```json
{
    "body": "For the record: If #11791 is applied after this ticket, source inspection in the example above works (and is doctested).",
    "created_at": "2012-05-03T16:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84623",
    "user": "SimonKing"
}
```

For the record: If #11791 is applied after this ticket, source inspection in the example above works (and is doctested).



---

archive/issue_comments_084624.json:
```json
{
    "body": "Is there a reviewer to fix name mangling of nested classes (needed in the category framework)?",
    "created_at": "2012-08-13T13:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84624",
    "user": "SimonKing"
}
```

Is there a reviewer to fix name mangling of nested classes (needed in the category framework)?



---

archive/issue_comments_084625.json:
```json
{
    "body": "This patch also fixes an issue that came up in #8899 regarding documentation of nested classes not appearing in the reference manual.\n\nSee here for a description of the issue, see the [thread on sage-combinat-devel](https://groups.google.com/d/topic/sage-combinat-devel/gWVx1It60ao/discussion).\n\nSee here for the confirmation that this works: http://trac.sagemath.org/sage_trac/ticket/8899#comment:31",
    "created_at": "2012-08-23T01:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84625",
    "user": "saliola"
}
```

This patch also fixes an issue that came up in #8899 regarding documentation of nested classes not appearing in the reference manual.

See here for a description of the issue, see the [thread on sage-combinat-devel](https://groups.google.com/d/topic/sage-combinat-devel/gWVx1It60ao/discussion).

See here for the confirmation that this works: http://trac.sagemath.org/sage_trac/ticket/8899#comment:31



---

archive/issue_comments_084626.json:
```json
{
    "body": "LGTM!",
    "created_at": "2012-11-27T10:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84626",
    "user": "vbraun"
}
```

LGTM!



---

archive/issue_comments_084627.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-11-27T10:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84627",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084628.json:
```json
{
    "body": "This causes trouble when building the documentation from scratch (i.e. after deleting 'devel/sage/doc/output`):\n\n```\n/usr/local/src/sage-5.5.rc1/local/lib/python2.7/site-packages/sage/categories/algebras_with_basis.py:docstring of sage.categories.algebras_with_basis.AlgebrasWithBasis.CartesianProducts.ParentMethods.one_from_cartesian_product_of_one_basis:3: WARNING: more than one target found for cross-reference u'one_basis': sage.combinat.sf.new_kschur.KBoundedSubspaceBases.ParentMethods.one_basis, sage.categories.algebras_with_basis.AlgebrasWithBasis.ParentMethods.one_basis, sage.combinat.ncsf_qsym.generic_basis_code.BasesOfQSymOrNCSF.ParentMethods.one_basis, sage.algebras.steenrod.steenrod_algebra.SteenrodAlgebra_generic.one_basis, sage.categories.examples.with_realizations.SubsetAlgebra.Fundamental.one_basis, sage.combinat.root_system.weyl_characters.WeightRing.one_basis, sage.categories.monoids.Monoids.Algebras.ParentMethods.one_basis, sage.categories.examples.hopf_algebras_with_basis.MyGroupAlgebra.one_basis, sage.categories.algebras_with_basis.AlgebrasWithBasis.TensorProducts.ParentMethods.one_basis, sage.algebras.affine_nil_temperley_lieb.AffineNilTemperleyLiebTypeA.one_basis, sage.categories.examples.algebras_with_basis.FreeAlgebra.one_basis, sage.combinat.symmetric_group_algebra.SymmetricGroupAlgebra_n.one_basis, sage.algebras.iwahori_hecke_algebra.IwahoriHeckeAlgebraT.one_basis, sage.algebras.group_algebra_new.GroupAlgebra.one_basis, sage.combinat.sf.sfa.SymmetricFunctionsBases.ParentMethods.one_basis, sage.combinat.root_system.weyl_characters.WeylCharacterRing.one_basis, sage.combinat.combinatorial_algebra.CombinatorialAlgebra.one_basis\n```\n",
    "created_at": "2012-12-19T15:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84628",
    "user": "jdemeyer"
}
```

This causes trouble when building the documentation from scratch (i.e. after deleting 'devel/sage/doc/output`):

```
/usr/local/src/sage-5.5.rc1/local/lib/python2.7/site-packages/sage/categories/algebras_with_basis.py:docstring of sage.categories.algebras_with_basis.AlgebrasWithBasis.CartesianProducts.ParentMethods.one_from_cartesian_product_of_one_basis:3: WARNING: more than one target found for cross-reference u'one_basis': sage.combinat.sf.new_kschur.KBoundedSubspaceBases.ParentMethods.one_basis, sage.categories.algebras_with_basis.AlgebrasWithBasis.ParentMethods.one_basis, sage.combinat.ncsf_qsym.generic_basis_code.BasesOfQSymOrNCSF.ParentMethods.one_basis, sage.algebras.steenrod.steenrod_algebra.SteenrodAlgebra_generic.one_basis, sage.categories.examples.with_realizations.SubsetAlgebra.Fundamental.one_basis, sage.combinat.root_system.weyl_characters.WeightRing.one_basis, sage.categories.monoids.Monoids.Algebras.ParentMethods.one_basis, sage.categories.examples.hopf_algebras_with_basis.MyGroupAlgebra.one_basis, sage.categories.algebras_with_basis.AlgebrasWithBasis.TensorProducts.ParentMethods.one_basis, sage.algebras.affine_nil_temperley_lieb.AffineNilTemperleyLiebTypeA.one_basis, sage.categories.examples.algebras_with_basis.FreeAlgebra.one_basis, sage.combinat.symmetric_group_algebra.SymmetricGroupAlgebra_n.one_basis, sage.algebras.iwahori_hecke_algebra.IwahoriHeckeAlgebraT.one_basis, sage.algebras.group_algebra_new.GroupAlgebra.one_basis, sage.combinat.sf.sfa.SymmetricFunctionsBases.ParentMethods.one_basis, sage.combinat.root_system.weyl_characters.WeylCharacterRing.one_basis, sage.combinat.combinatorial_algebra.CombinatorialAlgebra.one_basis
```




---

archive/issue_comments_084629.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-12-19T15:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84629",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084630.json:
```json
{
    "body": "Jeroen, can you elaborate a bit what went wrong?",
    "created_at": "2013-01-19T18:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84630",
    "user": "SimonKing"
}
```

Jeroen, can you elaborate a bit what went wrong?



---

archive/issue_comments_084631.json:
```json
{
    "body": "Aha, now I see that the very long single line contains warnings about cross references that were not found. I'll try to identify them.",
    "created_at": "2013-01-19T20:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84631",
    "user": "SimonKing"
}
```

Aha, now I see that the very long single line contains warnings about cross references that were not found. I'll try to identify them.



---

archive/issue_comments_084632.json:
```json
{
    "body": "Aha, here is an example:\n\nThe docstring of `sage.categories.algebras_with_basis.AlgebrasWithBasis.CartesianProducts.ParentMethods.one_from_cartesian_product_of_one_basis` is as follows:\n\n```\n            @cached_method   # todo: reinstate once #5843 is fixed\n            def one_from_cartesian_product_of_one_basis(self):\n                \"\"\"\n                Returns the one of this cartesian product of algebras, as per ``Monoids.ParentMethods.one``\n\n                It is constructed as the cartesian product of the ones of the\n                summands, using their :meth:`.one_basis` methods.\n\n                This implementation does not require multiplication by\n                scalars nor calling cartesian_product. This might help keeping\n                things as lazy as possible upon initialization.\n...\n```\n\n\nCould this simply be a misspelling? Note that it is written\n\n```\n:meth:`.one_basis`\n```\n\nbut should certainly be\n\n```\n:meth:`one_basis`\n```\n\n\nIf that's the case for the other warnings as well, then my patch would just uncover mistakes that happened earlier.",
    "created_at": "2013-01-19T20:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84632",
    "user": "SimonKing"
}
```

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

archive/issue_comments_084633.json:
```json
{
    "body": "The same issue arose in #13851 (see [comment 10](http://trac.sagemath.org/sage_trac/ticket/13851#comment:10)). I'm not sure why those dots are there, and I personally think they should be removed, but someone intentionally put them there.",
    "created_at": "2013-01-19T20:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84633",
    "user": "jhpalmieri"
}
```

The same issue arose in #13851 (see [comment 10](http://trac.sagemath.org/sage_trac/ticket/13851#comment:10)). I'm not sure why those dots are there, and I personally think they should be removed, but someone intentionally put them there.



---

archive/issue_comments_084634.json:
```json
{
    "body": "Replying to [comment:14 jhpalmieri]:\n> The same issue arose in #13851 (see [comment 10](http://trac.sagemath.org/sage_trac/ticket/13851#comment:10)). I'm not sure why those dots are there, and I personally think they should be removed, but someone intentionally put them there.\n\nI think the dot is simply wrong - or is it ignored by Sphinx?\n\nActually here it is even worse. The text is documentation of a functorial construction, but refers to a parent method - that can't possibly work without an explicit reference to the method which must include the class which the method belongs to.",
    "created_at": "2013-01-19T20:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84634",
    "user": "SimonKing"
}
```

Replying to [comment:14 jhpalmieri]:
> The same issue arose in #13851 (see [comment 10](http://trac.sagemath.org/sage_trac/ticket/13851#comment:10)). I'm not sure why those dots are there, and I personally think they should be removed, but someone intentionally put them there.

I think the dot is simply wrong - or is it ignored by Sphinx?

Actually here it is even worse. The text is documentation of a functorial construction, but refers to a parent method - that can't possibly work without an explicit reference to the method which must include the class which the method belongs to.



---

archive/issue_comments_084635.json:
```json
{
    "body": "Attachment\n\nFix a cross reference in some functorial construction",
    "created_at": "2013-01-19T21:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84635",
    "user": "SimonKing"
}
```

Attachment

Fix a cross reference in some functorial construction



---

archive/issue_comments_084636.json:
```json
{
    "body": "Does the second patch fix the problem? I am now explicitly referring to the `one_basis` method of `AlgebrasWithBasis.ParentMethods`.",
    "created_at": "2013-01-19T21:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84636",
    "user": "SimonKing"
}
```

Does the second patch fix the problem? I am now explicitly referring to the `one_basis` method of `AlgebrasWithBasis.ParentMethods`.



---

archive/issue_comments_084637.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-01-19T21:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84637",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084638.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-20T15:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84638",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084639.json:
```json
{
    "body": "Hi Simon,\n\nI again hit this one compiling the doc. Your patches look all good to me, including the one problem.\n\nThanks,\n\nFlorent",
    "created_at": "2013-03-20T15:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84639",
    "user": "hivert"
}
```

Hi Simon,

I again hit this one compiling the doc. Your patches look all good to me, including the one problem.

Thanks,

Florent



---

archive/issue_comments_084640.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-03-21T06:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84640",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084641.json:
```json
{
    "body": "Applying this patch causes the PDF docbuilder to hang after it's done building all documents. All documents are built but there are still 6 (I'm building with `MAKE=\"make -j6\"`) child processes which are stuck in the `multiprocessing.Pool` code. Interrupting those child processes simply causes new child processes to start which are then stuck again. It might be a bug in `multiprocessing.Pool` which is somehow triggered, I have no idea...",
    "created_at": "2013-03-21T06:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84641",
    "user": "jdemeyer"
}
```

Applying this patch causes the PDF docbuilder to hang after it's done building all documents. All documents are built but there are still 6 (I'm building with `MAKE="make -j6"`) child processes which are stuck in the `multiprocessing.Pool` code. Interrupting those child processes simply causes new child processes to start which are then stuck again. It might be a bug in `multiprocessing.Pool` which is somehow triggered, I have no idea...



---

archive/issue_comments_084642.json:
```json
{
    "body": "Perhaps an instance of #14323 (wild guess)?",
    "created_at": "2013-03-21T06:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84642",
    "user": "jdemeyer"
}
```

Perhaps an instance of #14323 (wild guess)?



---

archive/issue_comments_084643.json:
```json
{
    "body": "No, #14323 doesn't help.",
    "created_at": "2013-03-24T12:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84643",
    "user": "jdemeyer"
}
```

No, #14323 doesn't help.



---

archive/issue_comments_084644.json:
```json
{
    "body": "Jeroen, does the problem persist with the new doc builder? I have just applied the two patches, and succeeded with `export MAKE=\"make -j2\"` followed by `make`.\n\nHowever, there is continuation by `...` that needs fixing.",
    "created_at": "2013-05-22T11:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84644",
    "user": "SimonKing"
}
```

Jeroen, does the problem persist with the new doc builder? I have just applied the two patches, and succeeded with `export MAKE="make -j2"` followed by `make`.

However, there is continuation by `...` that needs fixing.



---

archive/issue_comments_084645.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-05-22T12:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84645",
    "user": "SimonKing"
}
```

Attachment



---

archive/issue_comments_084646.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-05-22T13:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84646",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084647.json:
```json
{
    "body": "Building the docs works for me, and the `...` should be fixed now. Hence: Needs review!\n\nApply trac9107_nesting_nested_classes.patch trac_9107_fix_cross_reference.patch",
    "created_at": "2013-05-22T13:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84647",
    "user": "SimonKing"
}
```

Building the docs works for me, and the `...` should be fixed now. Hence: Needs review!

Apply trac9107_nesting_nested_classes.patch trac_9107_fix_cross_reference.patch



---

archive/issue_comments_084648.json:
```json
{
    "body": "Replying to [comment:22 SimonKing]:\n> Building the docs works for me\nAlso the PDF docs?",
    "created_at": "2013-05-22T15:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84648",
    "user": "jdemeyer"
}
```

Replying to [comment:22 SimonKing]:
> Building the docs works for me
Also the PDF docs?



---

archive/issue_comments_084649.json:
```json
{
    "body": "There is a problem with latex and the fact that the docbuilder *hangs* is a bug in the new docbuilder: #14626\n\n```\n! LaTeX Error: Too deeply nested.\n\nSee the LaTeX manual or LaTeX Companion for explanation.\nType  H <return>  for immediate help.\n ...                                              \n                                                  \nl.27819 \\begin{Verbatim}[commandchars=\\\\\\{\\}]\n                                             \n? \nImplicit mode ON; LaTeX internals redefined\n(/usr/share/texmf-texlive/tex/latex/ltxmisc/url.sty\n(/usr/share/texmf-texlive/tex/latex/base/t1enc.def)\n! Emergency stop.\n ...                                              \n                                                  \nl.27819 \\begin{Verbatim}[commandchars=\\\\\\{\\}]\n                                             \n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on categories.log.\n)make[1]: *** [categories.pdf] Error 1\n```\n",
    "created_at": "2013-05-22T15:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84649",
    "user": "jdemeyer"
}
```

There is a problem with latex and the fact that the docbuilder *hangs* is a bug in the new docbuilder: #14626

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

archive/issue_comments_084650.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-05-22T15:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84650",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084651.json:
```json
{
    "body": "Yes, I did not consider the pdf docs.\n\nIf I understand correctly, we have two problems. The first problem is that with this patch, `LaTeX` is produced that can not be processed because it is two deeply nested. The second problem is independent, namely if latex fails, then the docbuilder hangs.\n\nDo you have any clue what object is being processed when things hang?",
    "created_at": "2013-05-22T15:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84651",
    "user": "SimonKing"
}
```

Yes, I did not consider the pdf docs.

If I understand correctly, we have two problems. The first problem is that with this patch, `LaTeX` is produced that can not be processed because it is two deeply nested. The second problem is independent, namely if latex fails, then the docbuilder hangs.

Do you have any clue what object is being processed when things hang?



---

archive/issue_comments_084652.json:
```json
{
    "body": "Replying to [comment:26 SimonKing]:\n> The second problem is independent, namely if latex fails, then the docbuilder hangs.\nWhich is #14626 and indeed has nothing to do with this ticket.\n\n> Do you have any clue what object is being processed when things hang?\nNot yet, I will reproduce the `.tex` file and then it should be clear.",
    "created_at": "2013-05-22T15:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84652",
    "user": "jdemeyer"
}
```

Replying to [comment:26 SimonKing]:
> The second problem is independent, namely if latex fails, then the docbuilder hangs.
Which is #14626 and indeed has nothing to do with this ticket.

> Do you have any clue what object is being processed when things hang?
Not yet, I will reproduce the `.tex` file and then it should be clear.



---

archive/issue_comments_084653.json:
```json
{
    "body": "Offending `.tex` file: [http://boxen.math.washington.edu/home/jdemeyer/badlatex/categories.tex](http://boxen.math.washington.edu/home/jdemeyer/badlatex/categories.tex)\n\nThe relevant lines are\n\n```\n\\begin{fulllineitems}\n\\phantomsection\\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods}\\pysigline{\\strong{class }\\bfcode{ParentMethods}}~\\index{Sets.WithRealizations.ParentMethods.Realizations (class in sage.categories.sets\\_cat)}\n\n\\begin{fulllineitems}\n\\phantomsection\\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods.Realizations}\\pysiglinewithargsret{\\strong{class }\\bfcode{Realizations}}{\\emph{parent\\_with\\_realization}}{}\nBases: {\\hyperref[sage/categories/realizations:sage.categories.realizations.Category_realization_of_parent]{\\code{sage.categories.realizations.Category\\_realization\\_of\\_parent}}}\n\nTESTS:\n\n\\begin{Verbatim}[commandchars=\\\\\\{\\}]\n\\PYG{g+gp}{sage: }\\PYG{k+kn}{from} \\PYG{n+nn}{sage.categories.realizations} \\PYG{k+kn}{import} \\PYG{n}{Category\\PYGZus{}realization\\PYGZus{}of\\PYGZus{}parent}\n\\PYG{g+gp}{sage: }\\PYG{n}{A} \\PYG{o}{=} \\PYG{n}{Sets}\\PYG{p}{(}\\PYG{p}{)}\\PYG{o}{.}\\PYG{n}{WithRealizations}\\PYG{p}{(}\\PYG{p}{)}\\PYG{o}{.}\\PYG{n}{example}\\PYG{p}{(}\\PYG{p}{)}\\PYG{p}{;} \\PYG{n}{A}\n\\PYG{g+go}{The subset algebra of \\PYGZob{}1, 2, 3\\PYGZcb{} over Rational Field}\n\\PYG{g+gp}{sage: }\\PYG{n}{C} \\PYG{o}{=} \\PYG{n}{A}\\PYG{o}{.}\\PYG{n}{Realizations}\\PYG{p}{(}\\PYG{p}{)}\\PYG{p}{;} \\PYG{n}{C}\n\\PYG{g+go}{Category of realizations of The subset algebra of \\PYGZob{}1, 2, 3\\PYGZcb{} over Rational Field}\n\\PYG{g+gp}{sage: }\\PYG{n+nb}{isinstance}\\PYG{p}{(}\\PYG{n}{C}\\PYG{p}{,} \\PYG{n}{Category\\PYGZus{}realization\\PYGZus{}of\\PYGZus{}parent}\\PYG{p}{)}\n\\PYG{g+go}{True}\n\\PYG{g+gp}{sage: }\\PYG{n}{C}\\PYG{o}{.}\\PYG{n}{parent\\PYGZus{}with\\PYGZus{}realization}\n\\PYG{g+go}{The subset algebra of \\PYGZob{}1, 2, 3\\PYGZcb{} over Rational Field}\n\\PYG{g+gp}{sage: }\\PYG{n}{TestSuite}\\PYG{p}{(}\\PYG{n}{C}\\PYG{p}{)}\\PYG{o}{.}\\PYG{n}{run}\\PYG{p}{(}\\PYG{p}{)}\n\\end{Verbatim}\n\\index{super\\_categories() (sage.categories.sets\\_cat.Sets.WithRealizations.ParentMethods.Realizations method)}\n\n\\begin{fulllineitems}\n\\phantomsection\\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods.Realizations.super_categories}\\pysiglinewithargsret{\\bfcode{super\\_categories}}{}{}\nEXAMPLES:\n\n\\begin{Verbatim}[commandchars=\\\\\\{\\}]   %% PROBLEM IS THIS LINE %%\n\\PYG{g+gp}{sage: }\\PYG{n}{A} \\PYG{o}{=} \\PYG{n}{Sets}\\PYG{p}{(}\\PYG{p}{)}\\PYG{o}{.}\\PYG{n}{WithRealizations}\\PYG{p}{(}\\PYG{p}{)}\\PYG{o}{.}\\PYG{n}{example}\\PYG{p}{(}\\PYG{p}{)}\\PYG{p}{;} \\PYG{n}{A}\n\\PYG{g+go}{The subset algebra of \\PYGZob{}1, 2, 3\\PYGZcb{} over Rational Field}\n\\PYG{g+gp}{sage: }\\PYG{n}{A}\\PYG{o}{.}\\PYG{n}{Realizations}\\PYG{p}{(}\\PYG{p}{)}\\PYG{o}{.}\\PYG{n}{super\\PYGZus{}categories}\\PYG{p}{(}\\PYG{p}{)}\n\\PYG{g+go}{[Category of realizations of sets]}\n\\end{Verbatim}\n\n\\end{fulllineitems}\n\n\n\\end{fulllineitems}\n\n\\index{facade\\_for() (sage.categories.sets\\_cat.Sets.WithRealizations.ParentMethods method)}\n```\n",
    "created_at": "2013-05-22T15:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84653",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_084654.json:
```json
{
    "body": "**before** this patch (good):\n\n```\n\\phantomsection\\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods}\\pysigline{\\bfcode{ParentMethods}}\nalias of \\code{WithRealizations.ParentMethods}\n```\n\n**after** this patch (bad):\n\n```\n\\phantomsection\\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods.Realizations}\\pysiglinewithargsret{\\strong{class }\\bfcode{Realizations}}{\\emph{parent\\_with\\_realization}}{}\nBases: {\\hyperref[sage/categories/realizations:sage.categories.realizations.Category_realization_of_parent]{\\code{sage.categories.realizations.Category\\_realization\\_of\\_parent}}}\n```\n",
    "created_at": "2013-05-22T15:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84654",
    "user": "jdemeyer"
}
```

**before** this patch (good):

```
\phantomsection\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods}\pysigline{\bfcode{ParentMethods}}
alias of \code{WithRealizations.ParentMethods}
```

**after** this patch (bad):

```
\phantomsection\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods.Realizations}\pysiglinewithargsret{\strong{class }\bfcode{Realizations}}{\emph{parent\_with\_realization}}{}
Bases: {\hyperref[sage/categories/realizations:sage.categories.realizations.Category_realization_of_parent]{\code{sage.categories.realizations.Category\_realization\_of\_parent}}}
```




---

archive/issue_comments_084655.json:
```json
{
    "body": "Replying to [comment:29 jdemeyer]:\n> **before** this patch (good):\n> {{{\n> \\phantomsection\\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods}\\pysigline{\\bfcode{ParentMethods}}\n> alias of \\code{WithRealizations.ParentMethods}\n> }}}\n> **after** this patch (bad):\n> {{{\n> \\phantomsection\\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods.Realizations}\\pysiglinewithargsret{\\strong{class }\\bfcode{Realizations}}{\\emph{parent\\_with\\_realization}}{}\n> Bases: {\\hyperref[sage/categories/realizations:sage.categories.realizations.Category_realization_of_parent]{\\code{sage.categories.realizations.Category\\_realization\\_of\\_parent}}}\n> }}}\n\nThree questions:\n\n1. Why is it bad? I don't see why latex should have a problem with it.\n2. Isn't the \"good\" output without my patch just plain wrong? After all, we do have\n   {{{\nsage: sage.categories.sets_cat.Sets.WithRealizations.ParentMethods.Realizations.__bases__\n(sage.categories.realizations.Category_realization_of_parent,)\n   }}}\n   and also `sage.categories.sets_cat.Sets.WithRealizations.ParentMethods.Realizations` is certainly *not* simply an alias of `WithRealizations.ParentMethods`.\n3. Can you also point me to the code that created the latex output?",
    "created_at": "2013-05-22T19:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84655",
    "user": "SimonKing"
}
```

Replying to [comment:29 jdemeyer]:
> **before** this patch (good):
> {{{
> \phantomsection\label{sage/categories/sets_cat:sage.categories.sets_cat.Sets.WithRealizations.ParentMethods}\pysigline{\bfcode{ParentMethods}}
> alias of \code{WithRealizations.ParentMethods}
> }}}
> **after** this patch (bad):
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
   and also `sage.categories.sets_cat.Sets.WithRealizations.ParentMethods.Realizations` is certainly *not* simply an alias of `WithRealizations.ParentMethods`.
3. Can you also point me to the code that created the latex output?



---

archive/issue_comments_084656.json:
```json
{
    "body": "When I build the pdf docs, it works. On what machine do you see the failure? If it's on sage.math, it might have to do with the fact that the LaTeX installation is quite old...\n\nEdit: maybe I'm seeing the failure now. Never mind.",
    "created_at": "2013-05-22T22:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84656",
    "user": "jhpalmieri"
}
```

When I build the pdf docs, it works. On what machine do you see the failure? If it's on sage.math, it might have to do with the fact that the LaTeX installation is quite old...

Edit: maybe I'm seeing the failure now. Never mind.



---

archive/issue_comments_084657.json:
```json
{
    "body": "OK, I see it, too.\n\n```\n../../sage -docbuild reference pdf\n...\nOutput written on tensor.pdf (24 pages, 144532 bytes).\nTranscript written on tensor.log.\nBuild finished.  The built documents can be found in /home/simon/SAGE/prerelease/sage-5.9.rc0/devel/sage/doc/output/pdf/en/reference/tensor\n```\n\nand then it hangs.\n\nNevertheless, I have no clue what is happening here. See my three questions in comment:30.",
    "created_at": "2013-05-23T05:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84657",
    "user": "SimonKing"
}
```

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

archive/issue_comments_084658.json:
```json
{
    "body": "Replying to [comment:30 SimonKing]:\n> 1. Why is it bad?\nI just used \"bad\" because `latex` doesn't compile it correctly.\n\n> 3. Can you also point me to the code that created the latex output?\nI guess that's Sphinx, but I don't know much about it.",
    "created_at": "2013-05-23T08:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84658",
    "user": "jdemeyer"
}
```

Replying to [comment:30 SimonKing]:
> 1. Why is it bad?
I just used "bad" because `latex` doesn't compile it correctly.

> 3. Can you also point me to the code that created the latex output?
I guess that's Sphinx, but I don't know much about it.



---

archive/issue_comments_084659.json:
```json
{
    "body": "Replying to [comment:33 jdemeyer]:\n> Replying to [comment:30 SimonKing]:\n> > 1. Why is it bad?\n> I just used \"bad\" because `latex` doesn't compile it correctly.\n\nThat was my question: Why does `latex` not compile it correctly?\n\nAnd we should keep in mind that the old output has simply been wrong.",
    "created_at": "2013-05-23T09:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84659",
    "user": "SimonKing"
}
```

Replying to [comment:33 jdemeyer]:
> Replying to [comment:30 SimonKing]:
> > 1. Why is it bad?
> I just used "bad" because `latex` doesn't compile it correctly.

That was my question: Why does `latex` not compile it correctly?

And we should keep in mind that the old output has simply been wrong.



---

archive/issue_comments_084660.json:
```json
{
    "body": "I think that the first line in the LaTeX error message is correct:\n\n```\n! LaTeX Error: Too deeply nested.\n```\n\nI think that there are too many levels of nesting of lists (from the `fulllineitems` environment). If I comment out the `Verbatim` environment that it's complaining about, I don't get an error message any more.",
    "created_at": "2013-05-23T19:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84660",
    "user": "jhpalmieri"
}
```

I think that the first line in the LaTeX error message is correct:

```
! LaTeX Error: Too deeply nested.
```

I think that there are too many levels of nesting of lists (from the `fulllineitems` environment). If I comment out the `Verbatim` environment that it's complaining about, I don't get an error message any more.



---

archive/issue_comments_084661.json:
```json
{
    "body": "Replying to [comment:35 jhpalmieri]:\n> I think that the first line in the LaTeX error message is correct:\n> {{{\n> ! LaTeX Error: Too deeply nested.\n> }}}\n> I think that there are too many levels of nesting of lists (from the `fulllineitems` environment). If I comment out the `Verbatim` environment that it's complaining about, I don't get an error message any more.\n\nPlease, where is the nesting? I suppose by \"comment out the `Verbatim` environment that it's complaining about\", you mean one of two `Verbatim` environments that were cited in comment:28.\n\nThe first is\n\n```\n\\begin{Verbatim}[commandchars=\\\\\\{\\}]\n\\PYG{g+gp}{sage: }\\PYG{k+kn}{from} \\PYG{n+nn}{sage.categories.realizations} \\PYG{k+kn}{import} \\PYG{n}{Category\\PYGZus{}realization\\PYGZus{}of\\PYGZus{}parent}\n\\PYG{g+gp}{sage: }\\PYG{n}{A} \\PYG{o}{=} \\PYG{n}{Sets}\\PYG{p}{(}\\PYG{p}{)}\\PYG{o}{.}\\PYG{n}{WithRealizations}\\PYG{p}{(}\\PYG{p}{)}\\PYG{o}{.}\\PYG{n}{example}\\PYG{p}{(}\\PYG{p}{)}\\PYG{p}{;} \\PYG{n}{A}\n\\PYG{g+go}{The subset algebra of \\PYGZob{}1, 2, 3\\PYGZcb{} over Rational Field}\n\\PYG{g+gp}{sage: }\\PYG{n}{C} \\PYG{o}{=} \\PYG{n}{A}\\PYG{o}{.}\\PYG{n}{Realizations}\\PYG{p}{(}\\PYG{p}{)}\\PYG{p}{;} \\PYG{n}{C}\n\\PYG{g+go}{Category of realizations of The subset algebra of \\PYGZob{}1, 2, 3\\PYGZcb{} over Rational Field}\n\\PYG{g+gp}{sage: }\\PYG{n+nb}{isinstance}\\PYG{p}{(}\\PYG{n}{C}\\PYG{p}{,} \\PYG{n}{Category\\PYGZus{}realization\\PYGZus{}of\\PYGZus{}parent}\\PYG{p}{)}\n\\PYG{g+go}{True}\n\\PYG{g+gp}{sage: }\\PYG{n}{C}\\PYG{o}{.}\\PYG{n}{parent\\PYGZus{}with\\PYGZus{}realization}\n\\PYG{g+go}{The subset algebra of \\PYGZob{}1, 2, 3\\PYGZcb{} over Rational Field}\n\\PYG{g+gp}{sage: }\\PYG{n}{TestSuite}\\PYG{p}{(}\\PYG{n}{C}\\PYG{p}{)}\\PYG{o}{.}\\PYG{n}{run}\\PYG{p}{(}\\PYG{p}{)}\n\\end{Verbatim}\n```\n\nthe second is\n\n```\n\\begin{Verbatim}[commandchars=\\\\\\{\\}]   %% PROBLEM IS THIS LINE %%\n\\PYG{g+gp}{sage: }\\PYG{n}{A} \\PYG{o}{=} \\PYG{n}{Sets}\\PYG{p}{(}\\PYG{p}{)}\\PYG{o}{.}\\PYG{n}{WithRealizations}\\PYG{p}{(}\\PYG{p}{)}\\PYG{o}{.}\\PYG{n}{example}\\PYG{p}{(}\\PYG{p}{)}\\PYG{p}{;} \\PYG{n}{A}\n\\PYG{g+go}{The subset algebra of \\PYGZob{}1, 2, 3\\PYGZcb{} over Rational Field}\n\\PYG{g+gp}{sage: }\\PYG{n}{A}\\PYG{o}{.}\\PYG{n}{Realizations}\\PYG{p}{(}\\PYG{p}{)}\\PYG{o}{.}\\PYG{n}{super\\PYGZus{}categories}\\PYG{p}{(}\\PYG{p}{)}\n\\PYG{g+go}{[Category of realizations of sets]}\n\\end{Verbatim}\n```\n\n\nI suppose `%% PROBLEM IS THIS LINE %%` in the second environment was Jeroen's addition.\n\nSo, what is \"too deeply nested\"? I can't believe that such a short piece of text has even enough characters to nest too deeply for latex!",
    "created_at": "2013-05-23T20:35:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84661",
    "user": "SimonKing"
}
```

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

archive/issue_comments_084662.json:
```json
{
    "body": "If I take the file categories.tex in `SAGE_ROOT/devel/sage/doc/output/latex/en/reference/categories/` and truncate it just before the line starting `\\index{facade\\_for() ...`, then I need to add in a few lines of the form\n\n```\n\\end{fulllineitems}\n```\n\nto get it to compile (after I comment out the last Verbatim block before the line `\\index{facade\\_for() ...`). So there are several `fulllineitems` environments nested within each other. Maybe too many, and maybe that's the problem. That's my current guess.",
    "created_at": "2013-05-23T23:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84662",
    "user": "jhpalmieri"
}
```

If I take the file categories.tex in `SAGE_ROOT/devel/sage/doc/output/latex/en/reference/categories/` and truncate it just before the line starting `\index{facade\_for() ...`, then I need to add in a few lines of the form

```
\end{fulllineitems}
```

to get it to compile (after I comment out the last Verbatim block before the line `\index{facade\_for() ...`). So there are several `fulllineitems` environments nested within each other. Maybe too many, and maybe that's the problem. That's my current guess.



---

archive/issue_comments_084663.json:
```json
{
    "body": "Hey Nicolas and Simon,\n\nThe problem comes from the fact that there is a 4 level deep class nesting with a method (which is 5 levels deep) in the `Sets.WithRealizations.ParentMethods.Realizations.super_categories`. I've tried moving this subclass into a separate class, and this solves the pdf build issue but introduces some doctesting errors. I don't think there is a  to extend the nesting level since that is a latex thing, nor do I think we should try since 4 nested classes is a lot IMO. I'm guessing beforehand because of the improper naming, latex did the environments differently...?\n\nAnyways the fix for the pdf build is to remove a level (or two) of class nesting.\n\nBest,\n\nTravis\n\nEdit: Here are the errors I get when I move `Sets.WithRealizations` out as a separate class and then assign it into `Sets`:\n\n```\nsage -t ../categories/sets_cat.py\n**********************************************************************\nFile \"../categories/sets_cat.py\", line 1408, in sage.categories.sets_cat.ParentMethodsForWithRealizations.realizations\nFailed example:\n    A.realizations()\nExpected:\n    [The subset algebra of {1, 2, 3} over Rational Field in the Fundamental basis, The subset algebra of {1, 2, 3} over Rational Field in the In basis, The subset algebra of {1, 2, 3} over Rational Field in the Out basis]\nGot:\n    [The subset algebra of {1, 2, 3} over Rational Field in the Fundamental basis, The subset algebra of {1, 2, 3} over Rational Field in the In basis, The subset algebra of {1, 2, 3} over Rational Field in the Out basis, The subset algebra of {1, 2, 3} over Rational Field in the realization Blah]\n**********************************************************************\nFile \"../categories/sets_cat.py\", line 1428, in sage.categories.sets_cat.ParentMethodsForWithRealizations.facade_for\nFailed example:\n    A.facade_for()\nExpected:\n    [The subset algebra of {1, 2, 3} over Rational Field in the Fundamental basis, The subset algebra of {1, 2, 3} over Rational Field in the In basis, The subset algebra of {1, 2, 3} over Rational Field in the Out basis]\nGot:\n    [The subset algebra of {1, 2, 3} over Rational Field in the Fundamental basis, The subset algebra of {1, 2, 3} over Rational Field in the In basis, The subset algebra of {1, 2, 3} over Rational Field in the Out basis, The subset algebra of {1, 2, 3} over Rational Field in the realization Blah]\n**********************************************************************\n2 items had failures:\n   1 of   8 in sage.categories.sets_cat.ParentMethodsForWithRealizations.facade_for\n   1 of   3 in sage.categories.sets_cat.ParentMethodsForWithRealizations.realizations\n    [241 tests, 2 failures, 0.76 s]\n----------------------------------------------------------------------\nsage -t ../categories/sets_cat.py  # 2 doctests failed\n----------------------------------------------------------------------\n```\n\nAny ideas why moving the class out of the nesting doesn't work?",
    "created_at": "2013-08-22T19:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84663",
    "user": "tscrim"
}
```

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

archive/issue_comments_084664.json:
```json
{
    "body": "Replying to [comment:39 tscrim]:\n> I don't think there is a  to extend the nesting level since that is a latex thing,\n\nShame on LaTeX!\n\n> Anyways the fix for the pdf build is to remove a level (or two) of class nesting.\n\nWhat exactly are we talking about? `Sets.WithRealizations.ParentMethods.Realizations`?\n\nInterestingly, there is the comment\n\n```\n# Do we really want this feature?\n```\n\n\nSo, can we do without this feature? Nicolas?",
    "created_at": "2013-08-22T19:27:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84664",
    "user": "SimonKing"
}
```

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

archive/issue_comments_084665.json:
```json
{
    "body": "Replying to [comment:40 SimonKing]:\n> Replying to [comment:39 tscrim]:\n> > Anyways the fix for the pdf build is to remove a level (or two) of class nesting.\n> \n> What exactly are we talking about? `Sets.WithRealizations.ParentMethods.Realizations`?\n\nYes. Removing a level of nesting allowed the pdf for categories to build for me.",
    "created_at": "2013-08-23T04:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84665",
    "user": "tscrim"
}
```

Replying to [comment:40 SimonKing]:
> Replying to [comment:39 tscrim]:
> > Anyways the fix for the pdf build is to remove a level (or two) of class nesting.
> 
> What exactly are we talking about? `Sets.WithRealizations.ParentMethods.Realizations`?

Yes. Removing a level of nesting allowed the pdf for categories to build for me.



---

archive/issue_comments_084666.json:
```json
{
    "body": "Thanks much Travis for investigating!\n\nI agree that there should be a recommendation for not nesting classes\ntoo deep, for the sake of readability. But having a hard arbitrary\nlimit -- especially that small -- is annoying. Shame on LaTeX. Of\ncourse, one can always spin off a subtree of nested classes into a\nseparate tree, but there are cases where one has a deep tree with very\nfew lines and no natural splitting point. For example, #10963\nintroduces\n\n```\n    DistributiveMagmasAndAdditiveMagmas.AdditiveAssociative.AdditiveCommutative.AdditiveUnital.AdditiveInverse\n```\n\n\nHmm. Altogether, I would call this a LaTeX arbitrary hard\nlimitation. Luckily there seems to be an easy solution to increase\nthis limitation to something large enough to cover our current use\ncases, namely to use the package enumitem [1]. By itself, it brings\nthe nesting level to 6, and we could even increase it further (10\nshould be really safe) using \\setlistdepth{9}.\n\nI have attached the little latex file I used for testing.\n\nWhat do you think? Shall we add enumitems to the list of latex\npackages loaded by Sphinx? Is this standard enough, or shall we add\nenumitem.sty to the Sage distribution?\n\nCheers,\n                                     Nicolas\n\n[1] http://stackoverflow.com/questions/1935952/maximum-nesting-level-of-lists-in-latex",
    "created_at": "2013-08-23T08:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84666",
    "user": "nthiery"
}
```

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

archive/issue_comments_084667.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-08-23T08:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84667",
    "user": "nthiery"
}
```

Attachment



---

archive/issue_comments_084668.json:
```json
{
    "body": "`enumitem.sty` looks pretty standard, so I'd say it's fine to use it.",
    "created_at": "2013-08-23T09:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84668",
    "user": "jdemeyer"
}
```

`enumitem.sty` looks pretty standard, so I'd say it's fine to use it.



---

archive/issue_comments_084669.json:
```json
{
    "body": "Replying to [comment:43 jdemeyer]:\n> `enumitem.sty` looks pretty standard, so I'd say it's fine to use it.\n\n... which means there should be a separate ticket for adding it?",
    "created_at": "2013-08-23T10:31:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84669",
    "user": "SimonKing"
}
```

Replying to [comment:43 jdemeyer]:
> `enumitem.sty` looks pretty standard, so I'd say it's fine to use it.

... which means there should be a separate ticket for adding it?



---

archive/issue_comments_084670.json:
```json
{
    "body": "Replying to [comment:44 SimonKing]:\n\n> ... which means there should be a separate ticket for adding it?\nAdding an `\\usepackage{}` somewhere (don't ask me where) should be trivial enough that it can be done on this ticket.",
    "created_at": "2013-08-23T11:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84670",
    "user": "jdemeyer"
}
```

Replying to [comment:44 SimonKing]:

> ... which means there should be a separate ticket for adding it?
Adding an `\usepackage{}` somewhere (don't ask me where) should be trivial enough that it can be done on this ticket.



---

archive/issue_comments_084671.json:
```json
{
    "body": "Replying to [comment:45 jdemeyer]:\n> Replying to [comment:44 SimonKing]:\n> > ... which means there should be a separate ticket for adding it?\n> Adding an `\\usepackage{}` somewhere (don't ask me where) should be trivial enough that it can be done on this ticket.\n\nSo, whom *do* we ask?",
    "created_at": "2013-08-23T11:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84671",
    "user": "SimonKing"
}
```

Replying to [comment:45 jdemeyer]:
> Replying to [comment:44 SimonKing]:
> > ... which means there should be a separate ticket for adding it?
> Adding an `\usepackage{}` somewhere (don't ask me where) should be trivial enough that it can be done on this ticket.

So, whom *do* we ask?



---

archive/issue_comments_084672.json:
```json
{
    "body": "Me; I just did this with Ben on #14787. You need to add it to `doc/common/conf.py`, and we also added it to `misc/latex.py`, which might be some overkill, but it doesn't really hurt to be extra safe here.",
    "created_at": "2013-08-23T15:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84672",
    "user": "tscrim"
}
```

Me; I just did this with Ben on #14787. You need to add it to `doc/common/conf.py`, and we also added it to `misc/latex.py`, which might be some overkill, but it doesn't really hurt to be extra safe here.



---

archive/issue_comments_084673.json:
```json
{
    "body": "Replying to [comment:47 tscrim]:\n> Me; I just did this with Ben on #14787. You need to add it to `doc/common/conf.py`, and we also added it to `misc/latex.py`, which might be some overkill, but it doesn't really hurt to be extra safe here.\n\nAre you saying that the problem is fixed by #14787? Then I suggest to add it as dependency.",
    "created_at": "2013-08-23T19:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84673",
    "user": "SimonKing"
}
```

Replying to [comment:47 tscrim]:
> Me; I just did this with Ben on #14787. You need to add it to `doc/common/conf.py`, and we also added it to `misc/latex.py`, which might be some overkill, but it doesn't really hurt to be extra safe here.

Are you saying that the problem is fixed by #14787? Then I suggest to add it as dependency.



---

archive/issue_comments_084674.json:
```json
{
    "body": "Replying to [comment:48 SimonKing]:\n> Replying to [comment:47 tscrim]:\n> > Me; I just did this with Ben on #14787. You need to add it to `doc/common/conf.py`, and we also added it to `misc/latex.py`, which might be some overkill, but it doesn't really hurt to be extra safe here.\n> \n> Are you saying that the problem is fixed by #14787? Then I suggest to add it as dependency.\n\nSorry, that was phrased badly. Ben and I added a latex package to the pdf builder in #14787, but it was not `enumitem.sty`.",
    "created_at": "2013-08-23T23:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84674",
    "user": "tscrim"
}
```

Replying to [comment:48 SimonKing]:
> Replying to [comment:47 tscrim]:
> > Me; I just did this with Ben on #14787. You need to add it to `doc/common/conf.py`, and we also added it to `misc/latex.py`, which might be some overkill, but it doesn't really hurt to be extra safe here.
> 
> Are you saying that the problem is fixed by #14787? Then I suggest to add it as dependency.

Sorry, that was phrased badly. Ben and I added a latex package to the pdf builder in #14787, but it was not `enumitem.sty`.



---

archive/issue_comments_084675.json:
```json
{
    "body": "For the record: someone else got a similar issue when using sphinx [1], and suggested the same fix. Alas this fix does not seem to be enough. I am still getting a \"Too deeply nested\" with the attached file categories.tex (obtained by reducing that produced by sphinx). I am working on reducing it further.\n\n\n[1] http://mail.scipy.org/pipermail/ipython-user/2012-May/010144.html",
    "created_at": "2013-08-27T11:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84675",
    "user": "nthiery"
}
```

For the record: someone else got a similar issue when using sphinx [1], and suggested the same fix. Alas this fix does not seem to be enough. I am still getting a "Too deeply nested" with the attached file categories.tex (obtained by reducing that produced by sphinx). I am working on reducing it further.


[1] http://mail.scipy.org/pipermail/ipython-user/2012-May/010144.html



---

archive/issue_comments_084676.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-08-27T11:05:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84676",
    "user": "nthiery"
}
```

Attachment



---

archive/issue_comments_084677.json:
```json
{
    "body": "Hi Nicolas,\n\nReplying to [comment:51 nthiery]:\n> For the record: someone else got a similar issue when using sphinx [1], and suggested the same fix. Alas this fix does not seem to be enough.\n\nWhat exactly did you do? Change sphinx.sty, as in the source you are giving? Or change doc/common/conf.py and misc/latex.py, as advised by Travis in comment:47?\n\nCould it be that the following comment from [the page you are citing](http://mail.scipy.org/pipermail/ipython-user/2012-May/010144.html) applies?\n\n```\nHowever this requires version 3.0 of enumitem, which doesn't yet ship\nwith many linux latex distributions.\n```\n",
    "created_at": "2013-08-27T11:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84677",
    "user": "SimonKing"
}
```

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

archive/issue_comments_084678.json:
```json
{
    "body": "Replying to [comment:52 SimonKing]:\n> Replying to [comment:51 nthiery]:\n> > For the record: someone else got a similar issue when using sphinx [1], and suggested the same fix. Alas this fix does not seem to be enough.\n> \n> What exactly did you do? Change sphinx.sty, as in the source you are giving? Or change doc/common/conf.py and misc/latex.py, as advised by Travis in comment:47?\n\nI changed conf.py which properly added it to the generated\ncategories.tex file (see the top of that file).\n\n> Could it be that the following comment from [the page you are citing](http://mail.scipy.org/pipermail/ipython-user/2012-May/010144.html) applies?\n> {{{\n> However this requires version 3.0 of enumitem, which doesn't yet ship\n> with many linux latex distributions.\n> }}}\n> \n\nI have 3.5.2 ...",
    "created_at": "2013-08-27T12:36:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84678",
    "user": "nthiery"
}
```

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

archive/issue_comments_084679.json:
```json
{
    "body": "Replying to [comment:53 nthiery]:\n> Replying to [comment:52 SimonKing]:\n> > What exactly did you do? Change sphinx.sty, as in the source you are giving? Or change doc/common/conf.py and misc/latex.py, as advised by Travis in comment:47?\n> \n> I changed conf.py which properly added it to the generated\n> categories.tex file (see the top of that file).\n\nHm. Then, we are back to the question: What the heck is going wrong? Could we\nperhaps ask on some `LaTeX` forum about the problem? I mean, if we have a tex\nfile that does not compile, even though nesting should not be the problem any\nmore, then I think `LaTeX` people should be made aware.",
    "created_at": "2013-08-27T12:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84679",
    "user": "SimonKing"
}
```

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

archive/issue_comments_084680.json:
```json
{
    "body": "How can one test [attachment:categories.tex]? I can not run pdflatex on it, because it can't find `sphinxmanual.cls`. Where do I get this file (and probably other files) from?",
    "created_at": "2013-08-27T12:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84680",
    "user": "SimonKing"
}
```

How can one test [attachment:categories.tex]? I can not run pdflatex on it, because it can't find `sphinxmanual.cls`. Where do I get this file (and probably other files) from?



---

archive/issue_comments_084681.json:
```json
{
    "body": "Replying to [comment:55 SimonKing]:\n> How can one test [attachment:categories.tex]? I can not run pdflatex on it, because it can't find `sphinxmanual.cls`. Where do I get this file (and probably other files) from?\n\nWhen I do `declare -x TEXINPUTS=.:$SAGE_ROOT/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/texinputs/` then it does find sphinxmanual.cls, but the next attempt to call pdflatex on categories.tex fails as well. This time, it can't find `report.cls`.\n\nSo, please tell me how one is supposed to run pdflatex on this file, so that I can reproduce the problem.",
    "created_at": "2013-08-27T14:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84681",
    "user": "SimonKing"
}
```

Replying to [comment:55 SimonKing]:
> How can one test [attachment:categories.tex]? I can not run pdflatex on it, because it can't find `sphinxmanual.cls`. Where do I get this file (and probably other files) from?

When I do `declare -x TEXINPUTS=.:$SAGE_ROOT/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/texinputs/` then it does find sphinxmanual.cls, but the next attempt to call pdflatex on categories.tex fails as well. This time, it can't find `report.cls`.

So, please tell me how one is supposed to run pdflatex on this file, so that I can reproduce the problem.



---

archive/issue_comments_084682.json:
```json
{
    "body": "Replying to [comment:56 SimonKing]:\n> Replying to [comment:55 SimonKing]:\n> > How can one test [attachment:categories.tex]? I can not run pdflatex on it, because it can't find `sphinxmanual.cls`. Where do I get this file (and probably other files) from?\n\n> When I do `declare -x TEXINPUTS=.:$SAGE_ROOT/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/texinputs/` then it does find sphinxmanual.cls, but the next attempt to call pdflatex on categories.tex fails as well. This time, it can't find `report.cls`.\n\nYou are missing a : at the end of TEXINPUT to let latex use its own library (report.cls is a standard class). \n\nOr you can just be lazy and put the categories.tex file in the directory \n\n```\n        <SAGE>/devel/sage/doc/output/latex/en/reference/categories\n```\n\nand run pdflatex from there.",
    "created_at": "2013-08-28T09:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84682",
    "user": "nthiery"
}
```

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

archive/issue_comments_084683.json:
```json
{
    "body": "Replying to [comment:57 nthiery]:\n> Replying to [comment:56 SimonKing]:\n> > When I do `declare -x TEXINPUTS=.:$SAGE_ROOT/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/texinputs/` then it does find sphinxmanual.cls, but the next attempt to call pdflatex on categories.tex fails as well. This time, it can't find `report.cls`.\n>\n> You are missing a : at the end of TEXINPUT to let latex use its own library (report.cls is a standard class). \n\nNope. After\n\n```\ndeclare -x TEXINPUTS=.:~/SAGE/prerelease/sage-5.11.beta3/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/texinputs/:\n```\n\n`pdflatex categories.tex` results in\n\n```\n! Undefined control sequence.\n<recently read> \\setlistdepth \n                              \nl.19 \\setlistdepth\n                  {9}\n? \n! Emergency stop.\n<recently read> \\setlistdepth \n                              \nl.19 \\setlistdepth\n                  {9}\n!  ==> Fatal error occurred, no output PDF file produced!\n```\n\n\n > Or you can just be lazy and put the categories.tex file in the directory \n> {{{\n>         <SAGE>/devel/sage/doc/output/latex/en/reference/categories\n> }}}\n> and run pdflatex from there.\n\nNope, because this folder doesn't exist. Do I need to attempt building the pdf documentation first?",
    "created_at": "2013-08-28T09:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84683",
    "user": "SimonKing"
}
```

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

archive/issue_comments_084684.json:
```json
{
    "body": "PS: Changing\n\n```\n\\RequirePackage{enumitem}\n```\n\ninto\n\n```\n\\usepackage{enumitem}\n```\n\ndid not help.",
    "created_at": "2013-08-28T09:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84684",
    "user": "SimonKing"
}
```

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

archive/issue_comments_084685.json:
```json
{
    "body": "Aha. The log shows:\n\n```\nenumitem 2009/05/18 v2.2 Customized lists\n```\n\nand I guess that's too old.",
    "created_at": "2013-08-28T10:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84685",
    "user": "SimonKing"
}
```

Aha. The log shows:

```
enumitem 2009/05/18 v2.2 Customized lists
```

and I guess that's too old.



---

archive/issue_comments_084686.json:
```json
{
    "body": "OK, after getting a more recent version of the enumitem package, I first get a \"too deeply nested\" error on [attachment:categories.tex]. However, after doing\n\n```\n\\setlistdepth{10}\n```\n\n(and not just depth 9), it compiles fine.\n\nSo, in other words, the problem *can* be solved. But I really wonder about the requirement that the user has to have a latex installation with a very recent enumitem. Can this be really required? Or would we be allowed to ship enumitem.sty with Sage?",
    "created_at": "2013-08-28T10:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84686",
    "user": "SimonKing"
}
```

OK, after getting a more recent version of the enumitem package, I first get a "too deeply nested" error on [attachment:categories.tex]. However, after doing

```
\setlistdepth{10}
```

(and not just depth 9), it compiles fine.

So, in other words, the problem *can* be solved. But I really wonder about the requirement that the user has to have a latex installation with a very recent enumitem. Can this be really required? Or would we be allowed to ship enumitem.sty with Sage?



---

archive/issue_comments_084687.json:
```json
{
    "body": "Output of pdflatex after doing setlistdept(10) in categories.tex",
    "created_at": "2013-08-28T10:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84687",
    "user": "SimonKing"
}
```

Output of pdflatex after doing setlistdept(10) in categories.tex



---

archive/issue_comments_084688.json:
```json
{
    "body": "Attachment\n\nWell, it does compile, but it does not work. Look at the ugly output in [attachment:categories.pdf].",
    "created_at": "2013-08-28T10:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84688",
    "user": "SimonKing"
}
```

Attachment

Well, it does compile, but it does not work. Look at the ugly output in [attachment:categories.pdf].



---

archive/issue_comments_084689.json:
```json
{
    "body": "Replying to [comment:61 SimonKing]:\n> OK, after getting a more recent version of the enumitem package, I first get a \"too deeply nested\" error on [attachment:categories.tex]. However, after doing\n> {{{\n> \\setlistdepth{10}\n> }}}\n> (and not just depth 9), it compiles fine.\n> So, in other words, the problem *can* be solved.\n\nWhat? Really? I thought I had tried that. Ah, I see, the level that\nyou have to put seems to actually have nothing to do with the actual\ndepth of your itemize. Now I can compile the full categories\ndocumentation, but that requires `\\setlistdepth{275`}!!! There\nmust be something wrong in the depth-counting logic of enumitem ...\n\n> But I really wonder about the requirement that the user has to have\n> a latex installation with a very recent enumitem. Can this be really\n> required? Or would we be allowed to ship enumitem.sty with Sage?\n\nI would vote for shipping enumitem.sty if that's easy. Jeroen/Volker/..., can we just throw it in\n`/opt/sage-dev/local/share/texmf/tex/generic` ?\n\n\nCheers,\n                                Nicolas",
    "created_at": "2013-08-28T12:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84689",
    "user": "nthiery"
}
```

Replying to [comment:61 SimonKing]:
> OK, after getting a more recent version of the enumitem package, I first get a "too deeply nested" error on [attachment:categories.tex]. However, after doing
> {{{
> \setlistdepth{10}
> }}}
> (and not just depth 9), it compiles fine.
> So, in other words, the problem *can* be solved.

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

archive/issue_comments_084690.json:
```json
{
    "body": "Replying to [comment:62 SimonKing]:\n> Well, it does compile, but it does not work. Look at the ugly output in [attachment:categories.pdf].\n\nNothing to worry about: this filed was obtained by stripping lots of stuff from an actual tex file; I am not surprised it does not look good. On the other hand, I had a look at the full categories.pdf produced by sphinx, and it looked reasonable.",
    "created_at": "2013-08-28T12:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84690",
    "user": "nthiery"
}
```

Replying to [comment:62 SimonKing]:
> Well, it does compile, but it does not work. Look at the ugly output in [attachment:categories.pdf].

Nothing to worry about: this filed was obtained by stripping lots of stuff from an actual tex file; I am not surprised it does not look good. On the other hand, I had a look at the full categories.pdf produced by sphinx, and it looked reasonable.



---

archive/issue_comments_084691.json:
```json
{
    "body": "Replying to [comment:63 nthiery]:\n> Now I can compile the full categories\n> documentation, but that requires `\\setlistdepth{275`}!!! There\n> must be something wrong in the depth-counting logic of enumitem ...\n\nOuch. So, if it really turns out that the depth-counting is broken (did you check that the nesting of lists in the created tex file are not broken?), then we should perhaps consider to search for an alternative solution.\n\nFor example, is it really needed to use nesting in the resulting tex file? Or could one create a nice layout without nesting? If I understand correctly, *we* (i.e., Sage) are creating the tex file. Hence, we can control what happens.\n\n> I would vote for shipping enumitem.sty if that's easy. Jeroen/Volker/..., can we just throw it in\n> `/opt/sage-dev/local/share/texmf/tex/generic` ?\n\nI have already asked on [sage-devel](https://groups.google.com/forum/#!topic/sage-devel/8Q-I0e2OESE)...",
    "created_at": "2013-08-28T13:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84691",
    "user": "SimonKing"
}
```

Replying to [comment:63 nthiery]:
> Now I can compile the full categories
> documentation, but that requires `\setlistdepth{275`}!!! There
> must be something wrong in the depth-counting logic of enumitem ...

Ouch. So, if it really turns out that the depth-counting is broken (did you check that the nesting of lists in the created tex file are not broken?), then we should perhaps consider to search for an alternative solution.

For example, is it really needed to use nesting in the resulting tex file? Or could one create a nice layout without nesting? If I understand correctly, *we* (i.e., Sage) are creating the tex file. Hence, we can control what happens.

> I would vote for shipping enumitem.sty if that's easy. Jeroen/Volker/..., can we just throw it in
> `/opt/sage-dev/local/share/texmf/tex/generic` ?

I have already asked on [sage-devel](https://groups.google.com/forum/#!topic/sage-devel/8Q-I0e2OESE)...



---

archive/issue_comments_084692.json:
```json
{
    "body": "Replying to [comment:65 SimonKing]:\n> I have already asked on [sage-devel](https://groups.google.com/forum/#!topic/sage-devel/8Q-I0e2OESE)...\n\nThanks for the pointer. I answered there.",
    "created_at": "2013-08-29T16:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84692",
    "user": "nthiery"
}
```

Replying to [comment:65 SimonKing]:
> I have already asked on [sage-devel](https://groups.google.com/forum/#!topic/sage-devel/8Q-I0e2OESE)...

Thanks for the pointer. I answered there.



---

archive/issue_comments_084693.json:
```json
{
    "body": "Just require enumitems, geez... Afair we already require a number of packages that are not part of a \"small\"/\"medium\" TeXLive install. One more doesn't make a difference.",
    "created_at": "2014-06-12T14:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84693",
    "user": "vbraun"
}
```

Just require enumitems, geez... Afair we already require a number of packages that are not part of a "small"/"medium" TeXLive install. One more doesn't make a difference.



---

archive/issue_comments_084694.json:
```json
{
    "body": "Yeah, you are right, let's make it simple. I for example had to install a bunch of language packages (russian, ...) to get the pdf doc to install a couple days ago.\n\nFirst attempt pushed. Compiling the doc and running the tests now.\n\nCheers,\n                            Nicolas",
    "created_at": "2014-06-12T14:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84694",
    "user": "nthiery"
}
```

Yeah, you are right, let's make it simple. I for example had to install a bunch of language packages (russian, ...) to get the pdf doc to install a couple days ago.

First attempt pushed. Compiling the doc and running the tests now.

Cheers,
                            Nicolas



---

archive/issue_comments_084695.json:
```json
{
    "body": "Replying to [comment:69 vbraun]:\n> Just require enumitems, geez... \n\nWhat exactly do you mean? Would it be sufficient to let Sage insert `usepackage{enumitem}` (I have not heard about the plural, `enumitems`), or will we also need to change the latex code emitted for nested classes? And how?",
    "created_at": "2014-06-12T15:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84695",
    "user": "SimonKing"
}
```

Replying to [comment:69 vbraun]:
> Just require enumitems, geez... 

What exactly do you mean? Would it be sufficient to let Sage insert `usepackage{enumitem}` (I have not heard about the plural, `enumitems`), or will we also need to change the latex code emitted for nested classes? And how?



---

archive/issue_comments_084696.json:
```json
{
    "body": "Replying to [comment:72 SimonKing]:\n> What exactly do you mean? Would it be sufficient to let Sage insert `usepackage{enumitem}`\n\nThat's my understanding and what I did in my latest commit. Plus raising the depth limit to a stupidly high value.\n\nThere seems to still be some compilation issue, but I guess they are just due to more stuff getting compiled, hence catching glitches that had gone unnoticed so far. I'll check this out tomorrow.\n\nCheers,\n                                Nicolas",
    "created_at": "2014-06-12T21:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84696",
    "user": "nthiery"
}
```

Replying to [comment:72 SimonKing]:
> What exactly do you mean? Would it be sufficient to let Sage insert `usepackage{enumitem}`

That's my understanding and what I did in my latest commit. Plus raising the depth limit to a stupidly high value.

There seems to still be some compilation issue, but I guess they are just due to more stuff getting compiled, hence catching glitches that had gone unnoticed so far. I'll check this out tomorrow.

Cheers,
                                Nicolas



---

archive/issue_comments_084697.json:
```json
{
    "body": "Gosh, it turned out that using `\\setlistdepth{275}` was not sufficient\nanymore: I had to use `\\setlistdepth{2000}`! This meant the problem\nwould just keep going to be worst and worst with time.\n\nSo I investigated a further and got lucky this time: if we replace\nlist by trivlist in the customized Verbatim defined by `sphinx.sty`,\nthen our documenation compiles smoothly, without even using enumitem.\n\nI proposed this fix upstream:\n\nhttps://bitbucket.org/birkenfeld/sphinx/issue/777/latex-output-too-deeply-nested\n\nFor the time being, I tweaked our conf.py to redefine and fix sphinx's\nVerbatim.\n\nOk, now there just remains to check that all tests pass, and this will\nbe a needs review.\n\nCheers,\n                              Nicolas\n----\nNew commits:",
    "created_at": "2014-06-13T09:24:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84697",
    "user": "nthiery"
}
```

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

archive/issue_comments_084698.json:
```json
{
    "body": "Is there a reason why you don't patch the sphinx spkg directly?",
    "created_at": "2014-06-13T16:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84698",
    "user": "tscrim"
}
```

Is there a reason why you don't patch the sphinx spkg directly?



---

archive/issue_comments_084699.json:
```json
{
    "body": "Replying to [comment:76 tscrim]:\n> Is there a reason why you don't patch the sphinx spkg directly?\n\nLazyness mostly. If someone whats to create a patch, adapt the spkg, ... please go ahead!",
    "created_at": "2014-06-13T19:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84699",
    "user": "nthiery"
}
```

Replying to [comment:76 tscrim]:
> Is there a reason why you don't patch the sphinx spkg directly?

Lazyness mostly. If someone whats to create a patch, adapt the spkg, ... please go ahead!



---

archive/issue_comments_084700.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-06-13T19:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84700",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_084701.json:
```json
{
    "body": "Ok, there were a couple doctest failures, all to be expected since nested classes now have a correct name. Fixed now. So that's a needs review!",
    "created_at": "2014-06-13T19:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84701",
    "user": "nthiery"
}
```

Ok, there were a couple doctest failures, all to be expected since nested classes now have a correct name. Fixed now. So that's a needs review!



---

archive/issue_comments_084702.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-06-13T19:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84702",
    "user": "nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084703.json:
```json
{
    "body": "Here's a version with a patched version of the sphinx spkg. Although I think your pull request is based on v1.2 (but it still applied (for me) to our current v1.1). Could someone check to make sure I created the patch correctly (and tell me what I should do instead if it isn't right).\n----\nNew commits:",
    "created_at": "2014-06-13T21:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84703",
    "user": "tscrim"
}
```

Here's a version with a patched version of the sphinx spkg. Although I think your pull request is based on v1.2 (but it still applied (for me) to our current v1.1). Could someone check to make sure I created the patch correctly (and tell me what I should do instead if it isn't right).
----
New commits:



---

archive/issue_comments_084704.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-06-16T19:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84704",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_084705.json:
```json
{
    "body": "Replying to [comment:80 tscrim]:\n> Here's a version with a patched version of the sphinx spkg.\n\nAh, that's nice: modifying standard spkgs is much simpler now that we have a single repository. Thanks!\n\n> Although I think your pull request is based on v1.2 (but it still applied (for me) to our current v1.1). Could someone check to make sure I created the patch correctly (and tell me what I should do instead if it isn't right).\n\nIt seems to apply as it's supposed to (modulo trivial line offset).\n\nI have made some minor improvement to the patch description.\n\nI am a bit nervous about the removal of the former change log in SPKG.txt. But if someone can confirm that this is the right thing to do, that's ok for me.\n\nOther than this, this sounds good to go!\n\nThanks again,\n                                            Nicolas",
    "created_at": "2014-06-16T20:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84705",
    "user": "nthiery"
}
```

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

archive/issue_comments_084706.json:
```json
{
    "body": "Replying to [comment:82 nthiery]:\n> I am a bit nervous about the removal of the former change log in SPKG.txt. But if someone can confirm that this is the right thing to do, that's ok for me.\n\nDo it! ;-)",
    "created_at": "2014-06-16T21:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84706",
    "user": "vbraun"
}
```

Replying to [comment:82 nthiery]:
> I am a bit nervous about the removal of the former change log in SPKG.txt. But if someone can confirm that this is the right thing to do, that's ok for me.

Do it! ;-)



---

archive/issue_comments_084707.json:
```json
{
    "body": "Then away we go.",
    "created_at": "2014-06-17T02:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84707",
    "user": "tscrim"
}
```

Then away we go.



---

archive/issue_comments_084708.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-06-17T02:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84708",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084709.json:
```json
{
    "body": "Thanks for fixing this !!!",
    "created_at": "2014-06-18T12:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84709",
    "user": "ncohen"
}
```

Thanks for fixing this !!!



---

archive/issue_comments_084710.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-06-18T14:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9107#issuecomment-84710",
    "user": "vbraun"
}
```

Resolution: fixed
