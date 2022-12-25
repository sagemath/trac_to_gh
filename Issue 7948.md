# Issue 7948: fix docstring processing errors in 4.3.1.rc0

archive/issues_007948.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @jhpalmieri\n\nBuilding the docs for 4.3.1.rc0 produces these errors:\n\n```\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/algebras/quatalg/quaternion_algebra.py:docstring of sage.algebras.quatalg.quaternion_algebra:15: (ERROR/3) Unexpected indentation.\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/algebras/quatalg/quaternion_algebra_element.rst:6: (WARNING/2) error while formatting signature for sage.algebras.quatalg.quaternion_algebra_element.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/algebras/quatalg/quaternion_algebra_element.rst:6: (WARNING/2) error while formatting signature for sage.algebras.quatalg.quaternion_algebra_element.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/category.rst:6: (WARNING/2) error while formatting signature for sage.categories.category.Category.element_class: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/category.rst:6: (WARNING/2) error while formatting signature for sage.categories.category.Category.parent_class: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/dual.rst:6: (WARNING/2) error while formatting signature for sage.categories.dual.DualityCategory.dual: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/examples/semigroups_cython.rst:6: (WARNING/2) error while formatting signature for sage.categories.examples.semigroups_cython.DummyClass.method: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/examples/semigroups_cython.rst:6: (WARNING/2) error while formatting signature for sage.categories.examples.semigroups_cython.IdempotentSemigroups.super_categories: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/homset.rst:6: (WARNING/2) error while formatting signature for sage.categories.homset.Homset.element_class_set_morphism: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/hopf_algebras.rst:6: (WARNING/2) autodoc can't import/find class 'sage.categories.hopf_algebras.DualCategory.ParentMethods', it reported error: \"DualCategory\", please check your spelling and sys.path\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/semigroups.rst:6: (WARNING/2) autodoc can't import/find class 'sage.categories.semigroups.SubQuotients.ElementMethods', it reported error: \"SubQuotients\", please check your spelling and sys.path\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/semigroups.rst:6: (WARNING/2) autodoc can't import/find class 'sage.categories.semigroups.SubQuotients.ParentMethods', it reported error: \"SubQuotients\", please check your spelling and sys.path\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/combinat.rst:6: (WARNING/2) error while formatting signature for sage.combinat.combinat.CombinatorialClass.element_class: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/expnums.rst:6: (WARNING/2) error while formatting signature for sage.combinat.expnums.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/expnums.rst:6: (WARNING/2) error while formatting signature for sage.combinat.expnums.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/free_module.rst:6: (WARNING/2) error while formatting signature for sage.combinat.free_module.CombinatorialFreeModuleInterface.sum_of_terms: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/free_module.rst:6: (WARNING/2) error while formatting signature for sage.combinat.free_module.CombinatorialFreeModuleInterface.term: obj is not a code object\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/constructors.py:docstring of sage.combinat.iet.constructors.IET:26: (WARNING/2) Literal block expected; none found.\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/constructors.py:docstring of sage.combinat.iet.constructors.IntervalExchangeTransformation:26: (WARNING/2) Literal block expected; none found.\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/constructors.py:docstring of sage.combinat.iet.constructors.RauzyDiagram:83: (WARNING/2) Explicit markup ends without a blank line; unexpected unindent.\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/reduced.py:docstring of sage.combinat.iet.reduced.ReducedPermutationsIET_iterator:10: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/strata.py:docstring of sage.combinat.iet.strata.AbelianStratum:17: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/template.py:docstring of sage.combinat.iet.template.Permutation.rauzy_move:8: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/template.py:docstring of sage.combinat.iet.template:2: (ERROR/3) Unexpected indentation.\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/template.py:docstring of sage.combinat.iet.template.PermutationLI.is_irreducible:7: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/template.py:docstring of sage.combinat.iet.template.PermutationLI.is_irreducible:19: (WARNING/2) Definition list ends without a blank line; unexpected unindent.\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/template.py:docstring of sage.combinat.iet.template.RauzyDiagram.Path.composition:9: (WARNING/2) Inline emphasis start-string without end-string.\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/integer_vector.py:docstring of sage.combinat.integer_vector.gale_ryser_theorem:47: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/integer_vector.py:docstring of sage.combinat.integer_vector.gale_ryser_theorem:54: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/integer_vector.py:docstring of sage.combinat.integer_vector.is_gale_ryser:25: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/integer_vector.py:docstring of sage.combinat.integer_vector.is_gale_ryser:28: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/posets/poset_examples.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.poset_examples.random: arg is not a module, class, method, function, traceback, frame, or code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/posets/posets.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.posets.random: arg is not a module, class, method, function, traceback, frame, or code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_abstract.coxeter_diagram: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_abstract.index_set: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_abstract.is_affine: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_abstract.is_finite: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_abstract.rank: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_affine.classical: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_affine.special_node: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_crystalographic.dynkin_diagram: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/weyl_group.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.weyl_group.WeylGroup_gens.reflections: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/words/words.rst:6: (WARNING/2) error while formatting signature for sage.combinat.words.words.Words_all.cmp_letters: arg is not a module, class, method, function, traceback, frame, or code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/crypto/boolean_function.rst:6: (WARNING/2) error while formatting signature for sage.crypto.boolean_function.BooleanFunctionIterator.next: arg is not a module, class, method, function, traceback, frame, or code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.add_vertex: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.add_vertices: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.bidirectional_dijkstra: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.breadth_first_search: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.degree: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.del_vertex: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.del_vertices: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.depth_first_search: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.has_vertex: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.is_connected: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.is_strongly_connected: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.iterator_in_nbrs: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.iterator_nbrs: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.iterator_out_nbrs: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.iterator_verts: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.loops: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.name: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.num_edges: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.num_verts: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.relabel: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.shortest_path: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.Search_iterator.next: arg is not a module, class, method, function, traceback, frame, or code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.add_edge: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.add_edges: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.del_edge: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.get_edge_label: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.has_edge: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.iterator_edges: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.iterator_in_edges: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.iterator_out_edges: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.multiple_edges: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.set_edge_label: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.random_stress: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.add_edge: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.add_edges: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.del_edge: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.get_edge_label: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.has_edge: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.iterator_edges: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.iterator_in_edges: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.iterator_out_edges: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.multiple_edges: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.set_edge_label: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.random_stress: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.Graph.degree_constrained_subgraph:30: (WARNING/2) Literal block expected; none found.\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/matrix2.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix2.Matrix.integer_kernel: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/matrix_integer_dense.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix_integer_dense.Matrix_integer_dense.LLL: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/matrix_integer_dense.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix_integer_dense.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/matrix_integer_dense.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix_integer_dense.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/matrix_rational_dense.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix_rational_dense.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/matrix_rational_dense.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix_rational_dense.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/strassen.rst:6: (WARNING/2) error while formatting signature for sage.matrix.strassen.int_range.intervals: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/strassen.rst:6: (WARNING/2) error while formatting signature for sage.matrix.strassen.int_range.to_list: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/modules/free_module_element.rst:6: (WARNING/2) error while formatting signature for sage.modules.free_module_element.FreeModuleElement.norm: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.depth: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.items: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.keys: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.values: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.add_constraint: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.constraints: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.get_max: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.get_min: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.get_values: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.is_binary: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.is_integer: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.is_real: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.new_variable: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_binary: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_integer: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_max: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_min: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_objective: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_objective_name: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_problem_name: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_real: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.show: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.solve: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.write_lp: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.write_mps: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/complex_plot.rst:6: (WARNING/2) error while formatting signature for sage.plot.complex_plot.ComplexPlot.get_minmax_data: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.BoundingSphere.transform: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3d.export_jmol: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.bounding_box: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.flatten: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.jmol_repr: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.json_repr: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.obj_repr: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.set_texture: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.tachyon_repr: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.texture_set: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.transform: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.x3d_str: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.RenderParams.pop_transform: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.RenderParams.push_transform: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.RenderParams.unique_name: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.bounding_box: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.flatten: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.get_transformation: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.jmol_repr: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.json_repr: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.obj_repr: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.tachyon_repr: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.transform: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.x3d_str: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Viewpoint.x3d_str: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/arith.rst:: (ERROR/3) Content block expected for the \"note\" directive; none found.\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/arith.rst:: (ERROR/3) Content block expected for the \"note\" directive; none found.\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/complex_double.rst:6: (WARNING/2) error while formatting signature for sage.rings.complex_double.ComplexDoubleField: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/integer.rst:6: (WARNING/2) error while formatting signature for sage.rings.integer.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/integer.rst:6: (WARNING/2) error while formatting signature for sage.rings.integer.free_integer_pool: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/integer.rst:6: (WARNING/2) error while formatting signature for sage.rings.integer.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/integer_ring.rst:6: (WARNING/2) error while formatting signature for sage.rings.integer_ring.IntegerRing: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/integer_ring.rst:6: (WARNING/2) error while formatting signature for sage.rings.integer_ring.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/integer_ring.rst:6: (WARNING/2) error while formatting signature for sage.rings.integer_ring.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/number_field/number_field_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.number_field.number_field_element.CoordinateFunction.alpha: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_capped_absolute_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_capped_absolute_element.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_capped_absolute_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_capped_absolute_element.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_capped_relative_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_capped_relative_element.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_capped_relative_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_capped_relative_element.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_fixed_mod_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_fixed_mod_element.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_fixed_mod_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_fixed_mod_element.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_generic_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_generic_element.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_generic_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_generic_element.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.pAdicPrinterDefaults.allow_negatives: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.pAdicPrinterDefaults.alphabet: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.pAdicPrinterDefaults.max_poly_terms: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.pAdicPrinterDefaults.max_series_terms: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.pAdicPrinterDefaults.max_unram_terms: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.pAdicPrinterDefaults.mode: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.pAdicPrinterDefaults.sep: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/pow_computer.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.pow_computer.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/pow_computer.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.pow_computer.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/pow_computer_ext.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.pow_computer_ext.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/pow_computer_ext.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.pow_computer_ext.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/multi_polynomial_ring_generic.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.multi_polynomial_ring_generic.MPolynomialRing_generic.variable_names_recursive: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleSetIterator.next: arg is not a module, class, method, function, traceback, frame, or code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanMonomialIterator.next: arg is not a module, class, method, function, traceback, frame, or code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanMonomialMonoid.gen: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanMonomialMonoid.gens: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanMonomialMonoid.ngens: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanMonomialVariableIterator.next: arg is not a module, class, method, function, traceback, frame, or code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanPolynomialIdeal.groebner_basis: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanPolynomialIdeal.interreduced_basis: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanPolynomialIdeal.reduce: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanPolynomialIterator.next: arg is not a module, class, method, function, traceback, frame, or code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanPolynomialVectorIterator.next: arg is not a module, class, method, function, traceback, frame, or code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.get_cring: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.get_order_code: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.have_degree_order: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/polydict.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.polydict.ETupleIter.next: arg is not a module, class, method, function, traceback, frame, or code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/polynomial_integer_dense_flint.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.polynomial_integer_dense_flint.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/polynomial_integer_dense_flint.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.polynomial_integer_dense_flint.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/polynomial_modn_dense_ntl.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_n.lcm: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory.lsign: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory.usign: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory_ar.bernstein_polynomial: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory_ar.coeffs_bitsize: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory_intlist.bernstein_polynomial: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory_intlist.coeffs_bitsize: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory_ratlist.bernstein_polynomial: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory_ratlist.coeffs_bitsize: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.linear_map.from_ocean: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.linear_map.to_ocean: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.mk_ibpf: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.mk_ibpi: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.warp_map.from_ocean: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.warp_map.to_ocean: arg is not a Python function\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/power_series_ring_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.power_series_ring_element.PowerSeries.solve_linear_de: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/power_series_ring_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.power_series_ring_element.PowerSeries.truncate: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/rational.rst:6: (WARNING/2) error while formatting signature for sage.rings.rational.clear_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/rational.rst:6: (WARNING/2) error while formatting signature for sage.rings.rational.init_mpz_globals: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/real_double.rst:6: (WARNING/2) error while formatting signature for sage.rings.real_double.RealDoubleField: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/real_double.rst:6: (WARNING/2) error while formatting signature for sage.rings.real_double.pool_stats: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/real_mpfr.rst:6: (WARNING/2) error while formatting signature for sage.rings.real_mpfr.mpfr_prec_max: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/real_mpfr.rst:6: (WARNING/2) error while formatting signature for sage.rings.real_mpfr.mpfr_prec_min: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/ring.rst:6: (WARNING/2) error while formatting signature for sage.rings.ring.FiniteFieldIterator.next: arg is not a module, class, method, function, traceback, frame, or code object\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py:docstring of sage.schemes.elliptic_curves.ell_rational_field.EllipticCurve_rational_field.antilogarithm:18: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/structure/coerce.rst:6: (WARNING/2) error while formatting signature for sage.structure.coerce.CoercionModel_cache_maps.analyse: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/structure/coerce.rst:6: (WARNING/2) error while formatting signature for sage.structure.coerce.CoercionModel_cache_maps.explain: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/structure/element.rst:6: (WARNING/2) error while formatting signature for sage.structure.element.get_coercion_model: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/structure/parent.rst:6: (WARNING/2) error while formatting signature for sage.structure.parent.Parent.element_class: obj is not a code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/structure/parent.rst:6: (WARNING/2) error while formatting signature for sage.structure.parent.Parent.get_action: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/symbolic/expression.rst:6: (WARNING/2) error while formatting signature for sage.symbolic.expression.ExpressionIterator.next: arg is not a module, class, method, function, traceback, frame, or code object\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/symbolic/ring.rst:6: (WARNING/2) error while formatting signature for sage.symbolic.ring.the_SymbolicRing: Could not parse cython argspec\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sagenb-0.5-py2.6.egg/sagenb/notebook/config.py:docstring of sagenb.notebook.config:26: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sagenb/notebook/twist.rst:6: (WARNING/2) autodoc can't import/find class 'sagenb.notebook.twist.UserToplevel.userchild_download_worksheets.zip', it reported error: \"userchild_download_worksheets\", please check your spelling and sys.path\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sagenb-0.5-py2.6.egg/sagenb/storage/abstract_storage.py:docstring of sagenb.storage.abstract_storage.Datastore.worksheets:7: (WARNING/2) Literal block expected; none found.\n/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sagenb-0.5-py2.6.egg/sagenb/storage/filesystem_storage.py:docstring of sagenb.storage.filesystem_storage.FilesystemDatastore.worksheets:7: (WARNING/2) Literal block expected; none found.\nlooking for now-outdated files... none found\npickling environment... done\nchecking consistency... /home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/misc/attach.rst:: WARNING: document isn't included in any toctree\n```\n\n\nThese should all be fixed before the release.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7948\n\n",
    "created_at": "2010-01-16T16:33:36Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "fix docstring processing errors in 4.3.1.rc0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7948",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: mvngu

CC:  @jhpalmieri

Building the docs for 4.3.1.rc0 produces these errors:

```
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/algebras/quatalg/quaternion_algebra.py:docstring of sage.algebras.quatalg.quaternion_algebra:15: (ERROR/3) Unexpected indentation.
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/algebras/quatalg/quaternion_algebra_element.rst:6: (WARNING/2) error while formatting signature for sage.algebras.quatalg.quaternion_algebra_element.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/algebras/quatalg/quaternion_algebra_element.rst:6: (WARNING/2) error while formatting signature for sage.algebras.quatalg.quaternion_algebra_element.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/category.rst:6: (WARNING/2) error while formatting signature for sage.categories.category.Category.element_class: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/category.rst:6: (WARNING/2) error while formatting signature for sage.categories.category.Category.parent_class: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/dual.rst:6: (WARNING/2) error while formatting signature for sage.categories.dual.DualityCategory.dual: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/examples/semigroups_cython.rst:6: (WARNING/2) error while formatting signature for sage.categories.examples.semigroups_cython.DummyClass.method: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/examples/semigroups_cython.rst:6: (WARNING/2) error while formatting signature for sage.categories.examples.semigroups_cython.IdempotentSemigroups.super_categories: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/homset.rst:6: (WARNING/2) error while formatting signature for sage.categories.homset.Homset.element_class_set_morphism: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/hopf_algebras.rst:6: (WARNING/2) autodoc can't import/find class 'sage.categories.hopf_algebras.DualCategory.ParentMethods', it reported error: "DualCategory", please check your spelling and sys.path
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/semigroups.rst:6: (WARNING/2) autodoc can't import/find class 'sage.categories.semigroups.SubQuotients.ElementMethods', it reported error: "SubQuotients", please check your spelling and sys.path
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/semigroups.rst:6: (WARNING/2) autodoc can't import/find class 'sage.categories.semigroups.SubQuotients.ParentMethods', it reported error: "SubQuotients", please check your spelling and sys.path
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/combinat.rst:6: (WARNING/2) error while formatting signature for sage.combinat.combinat.CombinatorialClass.element_class: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/expnums.rst:6: (WARNING/2) error while formatting signature for sage.combinat.expnums.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/expnums.rst:6: (WARNING/2) error while formatting signature for sage.combinat.expnums.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/free_module.rst:6: (WARNING/2) error while formatting signature for sage.combinat.free_module.CombinatorialFreeModuleInterface.sum_of_terms: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/free_module.rst:6: (WARNING/2) error while formatting signature for sage.combinat.free_module.CombinatorialFreeModuleInterface.term: obj is not a code object
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/constructors.py:docstring of sage.combinat.iet.constructors.IET:26: (WARNING/2) Literal block expected; none found.
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/constructors.py:docstring of sage.combinat.iet.constructors.IntervalExchangeTransformation:26: (WARNING/2) Literal block expected; none found.
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/constructors.py:docstring of sage.combinat.iet.constructors.RauzyDiagram:83: (WARNING/2) Explicit markup ends without a blank line; unexpected unindent.
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/reduced.py:docstring of sage.combinat.iet.reduced.ReducedPermutationsIET_iterator:10: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/strata.py:docstring of sage.combinat.iet.strata.AbelianStratum:17: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/template.py:docstring of sage.combinat.iet.template.Permutation.rauzy_move:8: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/template.py:docstring of sage.combinat.iet.template:2: (ERROR/3) Unexpected indentation.
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/template.py:docstring of sage.combinat.iet.template.PermutationLI.is_irreducible:7: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/template.py:docstring of sage.combinat.iet.template.PermutationLI.is_irreducible:19: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/iet/template.py:docstring of sage.combinat.iet.template.RauzyDiagram.Path.composition:9: (WARNING/2) Inline emphasis start-string without end-string.
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/integer_vector.py:docstring of sage.combinat.integer_vector.gale_ryser_theorem:47: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/integer_vector.py:docstring of sage.combinat.integer_vector.gale_ryser_theorem:54: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/integer_vector.py:docstring of sage.combinat.integer_vector.is_gale_ryser:25: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/combinat/integer_vector.py:docstring of sage.combinat.integer_vector.is_gale_ryser:28: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/posets/poset_examples.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.poset_examples.random: arg is not a module, class, method, function, traceback, frame, or code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/posets/posets.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.posets.random: arg is not a module, class, method, function, traceback, frame, or code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_abstract.coxeter_diagram: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_abstract.index_set: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_abstract.is_affine: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_abstract.is_finite: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_abstract.rank: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_affine.classical: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_affine.special_node: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/cartan_type.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_crystalographic.dynkin_diagram: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/root_system/weyl_group.rst:6: (WARNING/2) error while formatting signature for sage.combinat.root_system.weyl_group.WeylGroup_gens.reflections: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/combinat/words/words.rst:6: (WARNING/2) error while formatting signature for sage.combinat.words.words.Words_all.cmp_letters: arg is not a module, class, method, function, traceback, frame, or code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/crypto/boolean_function.rst:6: (WARNING/2) error while formatting signature for sage.crypto.boolean_function.BooleanFunctionIterator.next: arg is not a module, class, method, function, traceback, frame, or code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.add_vertex: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.add_vertices: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.bidirectional_dijkstra: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.breadth_first_search: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.degree: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.del_vertex: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.del_vertices: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.depth_first_search: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.has_vertex: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.is_connected: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.is_strongly_connected: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.iterator_in_nbrs: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.iterator_nbrs: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.iterator_out_nbrs: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.iterator_verts: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.loops: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.name: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.num_edges: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.num_verts: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.relabel: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.shortest_path: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.Search_iterator.next: arg is not a module, class, method, function, traceback, frame, or code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.add_edge: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.add_edges: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.del_edge: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.get_edge_label: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.has_edge: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.iterator_edges: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.iterator_in_edges: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.iterator_out_edges: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.multiple_edges: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.DenseGraphBackend.set_edge_label: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/dense_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.dense_graph.random_stress: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.add_edge: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.add_edges: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.del_edge: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.get_edge_label: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.has_edge: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.iterator_edges: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.iterator_in_edges: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.iterator_out_edges: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.multiple_edges: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.SparseGraphBackend.set_edge_label: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/sparse_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.sparse_graph.random_stress: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.Graph.degree_constrained_subgraph:30: (WARNING/2) Literal block expected; none found.
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/matrix2.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix2.Matrix.integer_kernel: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/matrix_integer_dense.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix_integer_dense.Matrix_integer_dense.LLL: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/matrix_integer_dense.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix_integer_dense.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/matrix_integer_dense.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix_integer_dense.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/matrix_rational_dense.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix_rational_dense.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/matrix_rational_dense.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix_rational_dense.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/strassen.rst:6: (WARNING/2) error while formatting signature for sage.matrix.strassen.int_range.intervals: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/strassen.rst:6: (WARNING/2) error while formatting signature for sage.matrix.strassen.int_range.to_list: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/modules/free_module_element.rst:6: (WARNING/2) error while formatting signature for sage.modules.free_module_element.FreeModuleElement.norm: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.depth: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.items: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.keys: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.values: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.add_constraint: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.constraints: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.get_max: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.get_min: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.get_values: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.is_binary: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.is_integer: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.is_real: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.new_variable: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_binary: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_integer: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_max: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_min: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_objective: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_objective_name: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_problem_name: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_real: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.show: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.solve: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.write_lp: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.write_mps: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/complex_plot.rst:6: (WARNING/2) error while formatting signature for sage.plot.complex_plot.ComplexPlot.get_minmax_data: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.BoundingSphere.transform: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3d.export_jmol: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.bounding_box: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.flatten: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.jmol_repr: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.json_repr: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.obj_repr: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.set_texture: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.tachyon_repr: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.texture_set: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.transform: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3dGroup.x3d_str: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.RenderParams.pop_transform: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.RenderParams.push_transform: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.RenderParams.unique_name: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.bounding_box: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.flatten: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.get_transformation: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.jmol_repr: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.json_repr: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.obj_repr: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.tachyon_repr: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.transform: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.TransformGroup.x3d_str: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Viewpoint.x3d_str: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/arith.rst:: (ERROR/3) Content block expected for the "note" directive; none found.
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/arith.rst:: (ERROR/3) Content block expected for the "note" directive; none found.
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/complex_double.rst:6: (WARNING/2) error while formatting signature for sage.rings.complex_double.ComplexDoubleField: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/integer.rst:6: (WARNING/2) error while formatting signature for sage.rings.integer.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/integer.rst:6: (WARNING/2) error while formatting signature for sage.rings.integer.free_integer_pool: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/integer.rst:6: (WARNING/2) error while formatting signature for sage.rings.integer.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/integer_ring.rst:6: (WARNING/2) error while formatting signature for sage.rings.integer_ring.IntegerRing: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/integer_ring.rst:6: (WARNING/2) error while formatting signature for sage.rings.integer_ring.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/integer_ring.rst:6: (WARNING/2) error while formatting signature for sage.rings.integer_ring.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/number_field/number_field_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.number_field.number_field_element.CoordinateFunction.alpha: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_capped_absolute_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_capped_absolute_element.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_capped_absolute_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_capped_absolute_element.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_capped_relative_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_capped_relative_element.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_capped_relative_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_capped_relative_element.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_fixed_mod_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_fixed_mod_element.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_fixed_mod_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_fixed_mod_element.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_generic_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_generic_element.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_generic_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_generic_element.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.pAdicPrinterDefaults.allow_negatives: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.pAdicPrinterDefaults.alphabet: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.pAdicPrinterDefaults.max_poly_terms: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.pAdicPrinterDefaults.max_series_terms: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.pAdicPrinterDefaults.max_unram_terms: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.pAdicPrinterDefaults.mode: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/padic_printing.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.padic_printing.pAdicPrinterDefaults.sep: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/pow_computer.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.pow_computer.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/pow_computer.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.pow_computer.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/pow_computer_ext.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.pow_computer_ext.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/padics/pow_computer_ext.rst:6: (WARNING/2) error while formatting signature for sage.rings.padics.pow_computer_ext.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/multi_polynomial_ring_generic.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.multi_polynomial_ring_generic.MPolynomialRing_generic.variable_names_recursive: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleSetIterator.next: arg is not a module, class, method, function, traceback, frame, or code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanMonomialIterator.next: arg is not a module, class, method, function, traceback, frame, or code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanMonomialMonoid.gen: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanMonomialMonoid.gens: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanMonomialMonoid.ngens: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanMonomialVariableIterator.next: arg is not a module, class, method, function, traceback, frame, or code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanPolynomialIdeal.groebner_basis: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanPolynomialIdeal.interreduced_basis: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanPolynomialIdeal.reduce: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanPolynomialIterator.next: arg is not a module, class, method, function, traceback, frame, or code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.BooleanPolynomialVectorIterator.next: arg is not a module, class, method, function, traceback, frame, or code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.get_cring: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.get_order_code: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/pbori.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.pbori.have_degree_order: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/polydict.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.polydict.ETupleIter.next: arg is not a module, class, method, function, traceback, frame, or code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/polynomial_integer_dense_flint.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.polynomial_integer_dense_flint.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/polynomial_integer_dense_flint.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.polynomial_integer_dense_flint.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/polynomial_modn_dense_ntl.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_n.lcm: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory.lsign: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory.usign: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory_ar.bernstein_polynomial: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory_ar.coeffs_bitsize: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory_intlist.bernstein_polynomial: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory_intlist.coeffs_bitsize: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory_ratlist.bernstein_polynomial: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.bernstein_polynomial_factory_ratlist.coeffs_bitsize: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.linear_map.from_ocean: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.linear_map.to_ocean: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.mk_ibpf: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.mk_ibpi: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.warp_map.from_ocean: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/polynomial/real_roots.rst:6: (WARNING/2) error while formatting signature for sage.rings.polynomial.real_roots.warp_map.to_ocean: arg is not a Python function
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/power_series_ring_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.power_series_ring_element.PowerSeries.solve_linear_de: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/power_series_ring_element.rst:6: (WARNING/2) error while formatting signature for sage.rings.power_series_ring_element.PowerSeries.truncate: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/rational.rst:6: (WARNING/2) error while formatting signature for sage.rings.rational.clear_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/rational.rst:6: (WARNING/2) error while formatting signature for sage.rings.rational.init_mpz_globals: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/real_double.rst:6: (WARNING/2) error while formatting signature for sage.rings.real_double.RealDoubleField: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/real_double.rst:6: (WARNING/2) error while formatting signature for sage.rings.real_double.pool_stats: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/real_mpfr.rst:6: (WARNING/2) error while formatting signature for sage.rings.real_mpfr.mpfr_prec_max: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/real_mpfr.rst:6: (WARNING/2) error while formatting signature for sage.rings.real_mpfr.mpfr_prec_min: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/rings/ring.rst:6: (WARNING/2) error while formatting signature for sage.rings.ring.FiniteFieldIterator.next: arg is not a module, class, method, function, traceback, frame, or code object
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py:docstring of sage.schemes.elliptic_curves.ell_rational_field.EllipticCurve_rational_field.antilogarithm:18: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/structure/coerce.rst:6: (WARNING/2) error while formatting signature for sage.structure.coerce.CoercionModel_cache_maps.analyse: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/structure/coerce.rst:6: (WARNING/2) error while formatting signature for sage.structure.coerce.CoercionModel_cache_maps.explain: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/structure/element.rst:6: (WARNING/2) error while formatting signature for sage.structure.element.get_coercion_model: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/structure/parent.rst:6: (WARNING/2) error while formatting signature for sage.structure.parent.Parent.element_class: obj is not a code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/structure/parent.rst:6: (WARNING/2) error while formatting signature for sage.structure.parent.Parent.get_action: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/symbolic/expression.rst:6: (WARNING/2) error while formatting signature for sage.symbolic.expression.ExpressionIterator.next: arg is not a module, class, method, function, traceback, frame, or code object
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/symbolic/ring.rst:6: (WARNING/2) error while formatting signature for sage.symbolic.ring.the_SymbolicRing: Could not parse cython argspec
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sagenb-0.5-py2.6.egg/sagenb/notebook/config.py:docstring of sagenb.notebook.config:26: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sagenb/notebook/twist.rst:6: (WARNING/2) autodoc can't import/find class 'sagenb.notebook.twist.UserToplevel.userchild_download_worksheets.zip', it reported error: "userchild_download_worksheets", please check your spelling and sys.path
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sagenb-0.5-py2.6.egg/sagenb/storage/abstract_storage.py:docstring of sagenb.storage.abstract_storage.Datastore.worksheets:7: (WARNING/2) Literal block expected; none found.
/home/john/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sagenb-0.5-py2.6.egg/sagenb/storage/filesystem_storage.py:docstring of sagenb.storage.filesystem_storage.FilesystemDatastore.worksheets:7: (WARNING/2) Literal block expected; none found.
looking for now-outdated files... none found
pickling environment... done
checking consistency... /home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/misc/attach.rst:: WARNING: document isn't included in any toctree
```


These should all be fixed before the release.

Issue created by migration from https://trac.sagemath.org/ticket/7948





---

archive/issue_comments_069221.json:
```json
{
    "body": "Applies to 4.3.1.rc0",
    "created_at": "2010-01-16T17:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69221",
    "user": "https://github.com/JohnCremona"
}
```

Applies to 4.3.1.rc0



---

archive/issue_comments_069222.json:
```json
{
    "body": "Attachment [trac_7948-docstrings.2.patch](tarball://root/attachments/some-uuid/ticket7948/trac_7948-docstrings.2.patch) by @JohnCremona created at 2010-01-16 17:59:39\n\nApplies to 4.3.1.rc0",
    "created_at": "2010-01-16T17:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69222",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_7948-docstrings.2.patch](tarball://root/attachments/some-uuid/ticket7948/trac_7948-docstrings.2.patch) by @JohnCremona created at 2010-01-16 17:59:39

Applies to 4.3.1.rc0



---

archive/issue_comments_069223.json:
```json
{
    "body": "The patch fixes quite a few of these, but there are several categories of error whcich I do not understand at all, for example these:\n\n```\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/category.rst:6: (WARNING/2) error while formatting signature for sage.categories.category.Category.element_class: obj is not a code object\n```\n\n\n```\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.depth_first_search: arg is not a Python function\n```\n\n\n```\n/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/matrix2.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix2.Matrix.integer_kernel: Could not parse cython argspec\n```\n\n\nStill, if the attached patch applies ok and the docs rebuild ok then it would be worth merging, even though there are outstanding errors.",
    "created_at": "2010-01-16T18:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69223",
    "user": "https://github.com/JohnCremona"
}
```

The patch fixes quite a few of these, but there are several categories of error whcich I do not understand at all, for example these:

```
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/categories/category.rst:6: (WARNING/2) error while formatting signature for sage.categories.category.Category.element_class: obj is not a code object
```


```
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/graphs/base/c_graph.rst:6: (WARNING/2) error while formatting signature for sage.graphs.base.c_graph.CGraphBackend.depth_first_search: arg is not a Python function
```


```
/home/john/sage-4.3.1.rc0/devel/sage/doc/en/reference/sage/matrix/matrix2.rst:6: (WARNING/2) error while formatting signature for sage.matrix.matrix2.Matrix.integer_kernel: Could not parse cython argspec
```


Still, if the attached patch applies ok and the docs rebuild ok then it would be worth merging, even though there are outstanding errors.



---

archive/issue_comments_069224.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T18:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69224",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069225.json:
```json
{
    "body": "I think that \"obj is not a code object\" arises for methods marked as \"lazy_attributes\".  These probably need to be dealt with in some special way, but I don't know how to do it.  Maybe it deserves its own ticket.\n\n\"Could not parse cython argspec\" happens for several reasons.  In lots of cases, it's for functions with no arguments in cython files: `def f():`.  There is a mistake in sageinspect.py which causes such functions to raise this error.  I'm working on a patch.  Actually, the code in sageinspect.py for producing docstrings for cython functions, and in particular for returning the list of arguments and their default values, has some problems and ought to be rewritten.  Again, maybe this belongs on another ticket.\n\n\"arg is not a Python function\": I don't know where this comes from.",
    "created_at": "2010-01-16T22:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69225",
    "user": "https://github.com/jhpalmieri"
}
```

I think that "obj is not a code object" arises for methods marked as "lazy_attributes".  These probably need to be dealt with in some special way, but I don't know how to do it.  Maybe it deserves its own ticket.

"Could not parse cython argspec" happens for several reasons.  In lots of cases, it's for functions with no arguments in cython files: `def f():`.  There is a mistake in sageinspect.py which causes such functions to raise this error.  I'm working on a patch.  Actually, the code in sageinspect.py for producing docstrings for cython functions, and in particular for returning the list of arguments and their default values, has some problems and ought to be rewritten.  Again, maybe this belongs on another ticket.

"arg is not a Python function": I don't know where this comes from.



---

archive/issue_comments_069226.json:
```json
{
    "body": "Two out of three is good going!  I'm in favour of branching this into separate tickets as specific problems are identified.\n\nMy patch could still do with a review!  (There's only one; for some reason it got attached twice, but I don't know how to delete the duplicate).",
    "created_at": "2010-01-16T22:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69226",
    "user": "https://github.com/JohnCremona"
}
```

Two out of three is good going!  I'm in favour of branching this into separate tickets as specific problems are identified.

My patch could still do with a review!  (There's only one; for some reason it got attached twice, but I don't know how to delete the duplicate).



---

archive/issue_comments_069227.json:
```json
{
    "body": "I'll give John Cremona's patch a positive review, and I'm attaching another one which should be applied either before or after his.  I'm running doctests to make sure it doesn't break anything.  Here's a summary of what happens when I build the reference manual:\n\n```\nno patches: 237 warnings \ncremona's patch: 220 warnings\njhpalmieri's patch: 179 warnings\nboth patches: 162 warnings\n```\n",
    "created_at": "2010-01-17T01:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69227",
    "user": "https://github.com/jhpalmieri"
}
```

I'll give John Cremona's patch a positive review, and I'm attaching another one which should be applied either before or after his.  I'm running doctests to make sure it doesn't break anything.  Here's a summary of what happens when I build the reference manual:

```
no patches: 237 warnings 
cremona's patch: 220 warnings
jhpalmieri's patch: 179 warnings
both patches: 162 warnings
```




---

archive/issue_comments_069228.json:
```json
{
    "body": "Attachment [trac_7948-cythonargspec.patch](tarball://root/attachments/some-uuid/ticket7948/trac_7948-cythonargspec.patch) by @jhpalmieri created at 2010-01-17 01:34:08",
    "created_at": "2010-01-17T01:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69228",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_7948-cythonargspec.patch](tarball://root/attachments/some-uuid/ticket7948/trac_7948-cythonargspec.patch) by @jhpalmieri created at 2010-01-17 01:34:08



---

archive/issue_comments_069229.json:
```json
{
    "body": "Here's a third patch; together with the others, this gets us down to 144 warnings.  One of the remaining warnings is because of the problems I mentioned earlier about the sageinspect.py code for cython functions -- the code essentially needs to parse the `def f(...):` part of the function to find the arguments.  Right now, it does some simple searching to find the part `(...)` in parentheses, and then it splits that up at each comma.  This breaks if there is a default argument like `(vec=(1,0,0))`, and leads to the message \"Could not parse cython argspec\".\n\nFor most of the other 143 warnings, I don't know what to do.  (There are some easy ones, but they're in sagenb, and I don't feel like working on that right now.  It should probably be a separate ticket, anyway.)\n\nSometimes, I also get the message\n\n```\nchecking consistency... /Applications/sage/devel/sage/doc/en/reference/sage/misc/attach.rst:: WARNING: document isn't included in any toctree\n```\n\nTo deal with this, delete (by hand) the file `SAGE_DOC/en/reference/sage/misc/attach.rst`.",
    "created_at": "2010-01-17T18:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69229",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a third patch; together with the others, this gets us down to 144 warnings.  One of the remaining warnings is because of the problems I mentioned earlier about the sageinspect.py code for cython functions -- the code essentially needs to parse the `def f(...):` part of the function to find the arguments.  Right now, it does some simple searching to find the part `(...)` in parentheses, and then it splits that up at each comma.  This breaks if there is a default argument like `(vec=(1,0,0))`, and leads to the message "Could not parse cython argspec".

For most of the other 143 warnings, I don't know what to do.  (There are some easy ones, but they're in sagenb, and I don't feel like working on that right now.  It should probably be a separate ticket, anyway.)

Sometimes, I also get the message

```
checking consistency... /Applications/sage/devel/sage/doc/en/reference/sage/misc/attach.rst:: WARNING: document isn't included in any toctree
```

To deal with this, delete (by hand) the file `SAGE_DOC/en/reference/sage/misc/attach.rst`.



---

archive/issue_comments_069230.json:
```json
{
    "body": "apply on top of the other two patches",
    "created_at": "2010-01-17T18:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69230",
    "user": "https://github.com/jhpalmieri"
}
```

apply on top of the other two patches



---

archive/issue_comments_069231.json:
```json
{
    "body": "Attachment [trac_7948-lazy.patch](tarball://root/attachments/some-uuid/ticket7948/trac_7948-lazy.patch) by @JohnCremona created at 2010-01-17 18:29:15\n\nI'm about to test John P's two patches on top of mine.  If all goes well I'll give the ticket a positive review (since John already positively reviewed my patch), and then we can make a new patch for what remains.",
    "created_at": "2010-01-17T18:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69231",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_7948-lazy.patch](tarball://root/attachments/some-uuid/ticket7948/trac_7948-lazy.patch) by @JohnCremona created at 2010-01-17 18:29:15

I'm about to test John P's two patches on top of mine.  If all goes well I'll give the ticket a positive review (since John already positively reviewed my patch), and then we can make a new patch for what remains.



---

archive/issue_comments_069232.json:
```json
{
    "body": "Attachment [trac_7948-part4.patch](tarball://root/attachments/some-uuid/ticket7948/trac_7948-part4.patch) by @JohnCremona created at 2010-01-17 19:03:18\n\nApply after previous",
    "created_at": "2010-01-17T19:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69232",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_7948-part4.patch](tarball://root/attachments/some-uuid/ticket7948/trac_7948-part4.patch) by @JohnCremona created at 2010-01-17 19:03:18

Apply after previous



---

archive/issue_comments_069233.json:
```json
{
    "body": "Positive review to John P's two patches.  In testing, I spotted one more \"easy\" one, whic hI had to fix since I had written that docstring (I think).  Hence the small \"part 4\" patch.",
    "created_at": "2010-01-17T19:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69233",
    "user": "https://github.com/JohnCremona"
}
```

Positive review to John P's two patches.  In testing, I spotted one more "easy" one, whic hI had to fix since I had written that docstring (I think).  Hence the small "part 4" patch.



---

archive/issue_comments_069234.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T19:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69234",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008164.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-18T17:18:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7948#event-8164"
}
```



---

archive/issue_comments_069235.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-18T17:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69235",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_069236.json:
```json
{
    "body": "Merged (in this order):\n\n```\ntrac_7948-docstrings.2.patch\ntrac_7948-cythonargspec.patch\ntrac_7948-lazy.patch\ntrac_7948-part4.patch\n```\n",
    "created_at": "2010-01-18T17:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7948#issuecomment-69236",
    "user": "https://github.com/rlmill"
}
```

Merged (in this order):

```
trac_7948-docstrings.2.patch
trac_7948-cythonargspec.patch
trac_7948-lazy.patch
trac_7948-part4.patch
```

