# Roadmap for Optimization and Polyhedral Geometry softwares interactions in Sage

## (around Sage, (PyQ)Normaliz, SCIP, e-antic, Polymake, and others)

This page is intended to describe the current tickets related to optimization and polyhedral geometry.

## Future & Current Projects

* Extend the usage of Normaliz in Sage
* Extend the polyhedral geometry component of Sage
* Polyhedral arrangements and complexes

## Tickets

Here are some practical search lists of tickets:

[Tickets from the Sage Days 84 March 2017](https://trac.sagemath.org/query?status=closed&status=needs_info&status=needs_review&status=needs_work&status=new&status=positive_review&keywords=~days84&col=id&col=summary&col=status&col=time&col=changetime&col=author&col=reviewer&order=status)

[Tickets from the IMA Coding Sprint - April 2018](https://trac.sagemath.org/query?status=closed&status=needs_info&status=needs_review&status=needs_work&status=new&status=positive_review&keywords=~IMA-PolyGeom&col=id&col=summary&col=keywords&col=status&col=author&col=reviewer&order=status)

[Tickets with keyword polytope](https://trac.sagemath.org/query?status=needs_info&status=needs_review&status=needs_work&status=new&status=positive_review&keywords=~polytopes&keywords=~polytope&order=status)

[Current tickets of the Geometry component](https://trac.sagemath.org/query?status=needs_info&status=needs_review&status=needs_work&status=new&component=geometry&col=id&col=summary&col=status&col=owner&col=type&col=priority&col=keywords&order=status)

## Meta-tickets

There are already a few meta-tickets related to this topic:

* #22420: Polyhedron: new features and known bugs
* #20875: Polytopes, lattice (integer) point counting / enumeration, and their applications
* #20302: Improvements to MixedIntegerLinearProgram, its backends, and InteractiveLinearProgram
* #20877: Piecewise functions, polyhedral complexes, piecewise functions of several variables, periodic piecewise functions
* #22710: Polymake
* #22827: Expose all normaliz features
* #27063: Transition of combinatorial computations of Polyhedron to Combinatorial Type
* #29799: Vector spaces and algebras of polyhedra

## To do

* Thematic Tutorial for Py(Q)Normaliz installation/Usage in Sage
* Increase documentation in Py(Q)Normaliz
* #21984: Deprecate the opacity argument for plot3d and use alpha
* Make Pynormaliz a feature in the PythonModule framework
* #27736: Polymake: Turn polymake applications into objects with directories
* #27728: Add Perles and irrational polytopes to library
* Euclidean automorphisms group of polytopes in Normaliz 
* The integration of automorphisms into [SageMath](SageMath)
* The remaining main computation goal, Hilbert and Ehrhart series turned out to be a very difficult task since it would require the precise construction of a fundamental domain of the group action.
* Once interactive H-representation in normaliz is possible ("redund-like") make it work with the "A & B" operation in Sage!

## Current Tickets

The following tickets have been created and should be worked on:

* #25114: Cannot plot Cone that is a halfplane in 2d
* #27728: Add Perles and irrational polytopes to library
* #28230: Thematic Tutorial on algebraic polytopes in Sage using Normaliz 
* #29169: Maximal and critical angles for cones 
* #30198: Polyhedra in vector spaces without distinguished basis 
* #30438: Improve face iterator for almost simple/simplicial polytopes
* #30699: Improve triangulate and volume methods for polytopes over inexact rings
* #30749: Characteristic polynomial of central Hyperplane arrangement results wrong result?
* #30772: induced volume for polytopes defined over algebraic fields
* #31660: Polyhedron.relative_interior_manifold
* #31730: Polyhedron.affine_hull: New option 'unimodular'
* #31799: From CombinatorialPolyhedron and H-representation to Polyhedron (with double description) 
* #31800: CombinatorialPolyhedron indexed by non-minimal H-representations 
* #31801: PolyhedronFace.as_polyhedron: Provide double description to backends that support it 
* #31802: Bug in plotting 3d polyhedron with rays 
* #31803: Make CombinatorialPolyhedron an element class 
* #31804: Parent (set) of polyhedra with prescribed vertices or facets
* #33611: Improve edges/ridges for simple/simplicial polytopes
* #33644: CombinatorialPolyhedron: Cache is_simple, is_simplicial
* #33645: Another improvement for face iterator of simple/simplicial polytopes  
* #33646: face_iter/face_generator of polyhedra: Specify algorithm instead of dual=False/True

* Task #27063: Transition of combinatorial computations of Polyhedron to combinatorial type:
  * #33008: facet_adjacency_matrix
  * #33009: is_prism, is_bipyramid

* Task #29191: Polytopal constructions for combinatorial polyhedra:

* Task #29199: Set up polyhedra with both Vrep and Hrep:
  * #31801: PolyhedronFace.as_polyhedron.
  * #33653: join

* Task #29842: Run a more stable test suite on polyhedra:

* #32651: Split sage.geometry.polyhedron.base:
  * #33123
  * #33449
  * #33583

* Mutable and interactive backends:
  * #33666: Mutable polyhedron (ppl) saves incorrect Vrepresentation 
  * #33678: Make representation integers exportable and small improvements to backend ppl 
  * #33679: Use abstract_method for Polyhedra
  * #33709: Implement adding generators or constraints to ppl polyhedron 

## Short Sage Release Notes

### Sage 9.5

Improvements:

* #27744: Make pynormaliz a Feature
* #32666: Polyhedron_base.vertex_adjacency_matrix: Do not use face_lattice
* #32667: Fix incorrect documentation from #32498 
* #32767, #32776, #32884, #32889: Split sage.geometry.polyhedron.base

New features:

* #32498: Implement edge polytope and symmetric edge polytope of a graph

### Sage 9.4

Bug fixes:
* #31820: Fix pickling of normaliz representation objects

Improvements:
* #25122: Construct `RationalPolyhedralFan` from possibly overlapping cones
* #29811: PolyhedronFace: Add methods to compute cones of feasible directions and affine tangent cones
* #31819: Only subfaces/supfaces for polyhedral face iterator
* #31822: Check containment for combinatorial faces
* #31823: Obtain flexible maximal chains of a combinatorial polyhedron 
* #31834: Make Hrepresentation of `CombinatorialPolyhedron` bit more consistent
* #31245: Implement parallel f-vector for polytopes
* #32150: Set up polyhedra with both Vrep and Hrep: prism
* #32151: Set up polyhedra with both Vrep and Hrep: pyramid
* #32152: Set up polyhedra with both Vrep and Hrep: bipyramid
* #31821: Run the test suite of self.combinatorial_polyhedron() 
* #32157: Small improvements for ppl backend
* #32158: Make ppl backend somewhat lazy

New features:
* #29683: "look up" a face in the face lattice of a polyhedron
* #31659: Polyhedron.affine_hull_manifold
* #31748: `PolyhedralComplex`: preliminary implementation

### Sage 9.3

Bug fixes:
* #30015: Schlegel projection breaks convexity
* #30319: wrong intersection of polytopes
* #30545: A 1-dimensional polytope has no edge
* #30891: Normaliz cone from precomputed data has lattice messed up
* #31253: Put equations in stable position for backend cdd

Improvements:
* #30040: Improve face iterator for simple/simplicial polytopes
* #30445: Merge duplications in edges, ridges and f-vector of combinatorial polyhedron
* #30458: Outsource some functions in bit_vector_operations.cc
* #30524: Remove `maybe_newfaces` in combinatorial polyhedron
* #30528: Remove basic access to bitsets in combinatorial polyhedron
* #30529: Use reference instead of pointer to simplify code
* #30549: Remove all the bitset access from cython files in combinatorial polyhedron
* #30587: Remove import of 'ppl' at startup using lazy_import with feature
* #30878: some flake8 details in backend normaliz
* #31262: Implement non zero chunks for sparse bitsets 

New features:
* #30704: Upgrade to Normaliz 3.8.9 and PyNormaliz 2.13
* #30946: Add "minimal=True" option to affine_hull_projection
* #30954: Implement a proper equality check for polyhedron representation objects
* #31038: Improve the zonotope construction

### Sage 9.2

Improvements:
* #28894: Parallel f-vector for polyhedra: Move most important attributes of `FaceIterator` to a structure
* #28982: Use `CombinatorialPolyhedron` to obtain faces lattice of polyhedra
* #29196: Make Ehrhart series related function cached
* #29325: precomputed double description for permutahedron
* #29565: Transition of combinatorial computations of Polyhedron to combinatorial type: Migrate neighborly to combinatorial polyhedron 
* #29566: CombinatorialPolyhedron: Store incidence matrix on initialization
* #29568: Initialize polyhedra with backend cdd with both Vrepresentation and Hrepresentation
* #29654: Improve face generator of polyhedra by exposing `FaceIterator` class
* #29661: Some optimizations for method regions of hyperplane arrangements
* #29676: Make a nogil version of the most important methods of FaceIterator
* #29679: Cleanup of 28757
* #29681: Small improvements for `FaceIterator_base`
* #29800: Make categories of Polyhedra parent more precise
* #29836: normaliz backend isn't ready for generators
* #29837: Improvement for incidence matrix of polyhedra
* #29840: Document choice of base ring of incidence matrix and adjacency matrices
* #29841: Improve obtaining combinatorial polyhedron
* #29843: Set up linear transformation with precomputed data if injective
* #29898: vertex facet graph for trivial polyhedra fails
* #29899: Two bugs with dilation
* #29904: Broken double description of hypercube
* #30146: #29843 introduces a bug in Polyhedron().linear_transformation
* #30204: Prepare Polyhedra parent factory to handle more general ambient spaces
* #30248: Normaliz backend is broken with double description input
* #30292: is_pyramid returns a wrong certificate
* #30293: bug in lawrence_extension
* #30321: Improve tikz picture methods of Polyhedron
* #30328: Need to convert values before passing them to `cdd`
* #30330: `cdd` backend fails to initialize empty polyhedron from double description
* #30428: More direct check for simple/simplicial polytopes
* #30429: Standardize `intersection` in `combinatorial_polyhedron/bit_vector_operations.cc`
* #30435: Improve count vertices of combinatorial faces
* #30443: Simplify setting and getting "edges" of edges, ridges, incidences in `CombinatorialPolyhedron`
* #30531: Polyhedron_normaliz._triangulate_normaliz should not use NmzResult directly
* #30571: Remove doctests in `combinatorial_polyhedron/conversions.pyx` that depend on implementation details
* #30605: improve cone containment tests

New features:
* #29506: Backend for Hyperplane Arrangements
* #29838: Implement slack matrix for polyhedra
* #29843: Set up polyhedra with both Vrep and Hrep: linear transformation
* #29569: Set up polyhedra with both Vrep and Hrep: Obtain polar with both Vrep and Hrep (if backend supports it)
* #29583: Set up polyhedra with both Vrep and Hrep: product
* #30440: Pyramid for combinatorial polyhedra

Testing Framework:
* #29903: Run many test suite examples for polyhedra
* #29905: test basic properties of polyhedra
* #29906: Run tests for `an_affine_basis`
* #29907: Run test suite to check method dilation
* #29908: Test method `is_combinatorially_isomorphic`
* #29918: Run test suite for gale transform

Finished Task:

* #28280: Task: CombinatorialPolyhedron: replace attributes by methods, make names more consistent with Polyhedron

### Sage 9.1

Improvements:
* #19803: difference of behavior in polyhedra with different backends
* #28626: Compute graph of polyhedron with `CombinatorialPolyhedron`
* #28757: `CombinatorialPolyhedron`: Remove empty folder
* #28873: Implement ambient volume of polyhedron with normaliz
* #28866: doctest killed due to abort in geometry/polyhedron/base.py 
* #28880: Prepare setting up polyhedron from both Vrep and Hrep for different backends
* #29057: make stack method of Polyhedron use fraction_field
* #29073: `gale_transform` does not work for `RDF`
* #29074: Better error message for polar of non-full dimensional polyhedra
* #29078: Move `is_simple` and `is_simplicial` to `CombinatorialPolyhedron` 
* #29116: affine_basis does not always work when used with orthogonal or orthonormal
* #29125: `is_inscribed` depends on order of vertices
* #29155: Full-dimensional face of Polyhedron should have equations
* #29176: Bug in Voronoi Diagram
* #29186: Add simplicity and simpliciality to polyhedra
* #29188: Move vertex facet graph to combinatorial polyhedron 
* #29189: Migrate `is_lawrence_polytope` and `is_pyramid` to combinatorial polyhedron
* #29198: Set up hypercube with both Vrep and Hrep (if backend supports it) 
* #29200: Dilation of polyhedron with both Vrep and Hrep (if backend supports it)
* #29223: Pickle cached value of volume and f-vector
* #29229: Improvements for is_reflexive for polyhedra over the integers
* #29242: `CombinatorialPolyhedron`: bit_repr_ -> bit_rep_
* #29323: Set up cross polytope with both Vrep and Hrep (if backend supports it) 
* #29324: Translation with both Vrep and Hrep
* #29326: Improvements for projection into affine hull
* #29382: Compute the centroid of a polytope
* #29455: Bug in incidence_matrix of CombinatorialPolyhedron
 
New features:
* #17215: Normal cone of faces of polyhedra
* #26363: Polyhedron_normaliz.save
* #26623: Constructions for common polyhedral cones
* #27086: Simplicity and simpliciality for CombinatorialPolyhedron
* #28247: Parametrize the cube/hypercube functions in the library of polytopes
* #28413: Add .h_star_vector to compact rational polytopes
* #28646: A face generator for polyhedra (using CombinatorialPolyhedron)
* #28724: Polyhedron._acted_upon_ should handle left multiplication by matrices, linear transformations
* #28960: Initialize CombinatorialPolyhedron? from incidence matrix of cone or lattice polytope
* #29065: Inverse function for gale_transform
* #29085: CombinatorialPolyhedron: Expose `is_bounded`
* #29112: Implement incidence matrix for combinatorial polyhedron
* #29117: Implement a maximal chain for combinatorial polyhedron
* #29127: Implement an affine basis for polytopes
* #29382: Compute the centroid of a polytope
* #29190: polar/dual for combinatorial polyhedra
* #29224: `flag_f_vector` for polyhedra

### Sage 9.0

Improvements:
* #17339: Polyhedron class mistreats empty inputs
* #18861: Three apparently useless polyhedron methods
* #25183: Bug in the associahedron object
* #26922: Wrong f-vector for unbounded polyhedra
* #28311: Random failure in combinatorial_polyhedron/base.pyx
* #28463: .neighbors() error in polyhedron.representation
* #28464: .is_inscribed() makes a bad assumption in Polyhedron
* #28506: Direct sum of polyhedron is broken, so is minkowski difference and face truncation
* #28625: Let CombinatorialPolyhedron handle f_vector of polyhedra 
* #28643: Speed up incidence matrix of polyhedra
* #28650: Fix the dimension of PolyhedronFace
* #28654: A Bug in the backend `field`
* #28655: Fix typos in the method 'is_combinatorially_isomorphic' of Polyhedron
* #28662: Missing edges when visualizing Polyhedra with threejs
* #28668: fix the base_ring of face_split
* #28678: Bug in CombinatorialPolyhedron of empty Lattice polytope
* #28725: fix lawrence_extension and lawrence_polytope for backend field
* #28741: Lattice Polytopes: `compute_facets` does not check dimension when setting is_reflexive
* #28770: Polyhedra coercion of base rings fails for number fields
* #28828: Attributes of polyhedra are exposed
* #28850: Polar of polytopes does not check if polytope is full-dimensional
* #28851: Polar of integer polytopes does not respect backend
* #28872: Wrong usage of normaliz/pynormaliz makes sage crash hard
* #28876: Polyhedron: Let affine hull fully respect backend

New features:

* #18957: ehrhart_polynomial should be made available for polytopes defined over QQ
* #28621: Add CombinatorialPolyhedron method to Polyhedron objects
* #28245: Implement center of a HyperplaneArrangement
* #28248: Add .boundary_complex() method for simplicial polytopes
* #28429: Add the classical construction of the 120-cell
* #28743: Lattice Polytopes: Implement incidence matrix
* #28766: Implement incidence matrix for cones

### Sage 8.9

The polyhedron folder is now py3 compatible with all optional packages!

Improvements:
* #24877: bug in polyhedron over RDF 
* #27798: Add `backend` option to associahedron and flow polytope
* #27926: Preserve backend for polytopal constructions
* #27987: CombinatorialPolyhedron? improve initialization, remove bug for unbounded polyhedra
* #27993: NormalFan?: issue with inner and outer normal vectors
* #28235: py3: polyhedron folder with optional packages
* #28240: Move rational methods of the backend normaliz to the _QQ class
* #28430: Polyhedron: Preserve backend for barycentric subdivision

New features:
* #25091: Expose some normaliz features
* #25097: Algebraic polyhedra with QNormaliz / e-antic (in the normaliz backend)
* #26887: Implement the class CombinatorialPolyhedron
* #27689: Implement is_pyramid, is_bipyramid, is_prism for polytopes
* #27760: Generalized Permutohedra and type H4 4-uniform polytopes
* #27973: Implement wedge over a face of Polyhedron
* #27974: Implement facets method for Polyhedron
* #28256: Add .is_self_dual method for polytopes

### Sage 8.8

Improvements:
* #20181: `number_field_elements_from_algebraics` should create embedded number field elements [Sage-devel discussion](https://groups.google.com/forum/#!topic/sage-devel/iy72Q_EKKFs)
* #21161: repr of NumberFields (the parents) should indicate its embedding if there is one
* #22704: Create a variant of the polymake interface using polymake's callable library (polymake::Main) via JuPyMake
* #26340: polytopes.snub_cube should be set up with base_ring=QQ
* #27071: Make indices of V_representation of faces of polyhedron accessible through a new method
* #27533: Improve Polyhedron.is_simple()
* #27673: AttributeError? of Polyhedron.volume()
* #27682: upgrade normaliz to 3.7.1, pynormaliz to 2.1 and package e-antic
* #27700: Fix is_simplicial for non-full-dimensional polytopes
* #27709: The attribute _vector of H and V representation is exposed
* #27716: Refactor backend_normaliz 
* #27722: Remove old deprecation warning of Minkowski -> minkowski
* #27731: upgrade normaliz to 3.7.2, pynormaliz to 2.5
* #27840: Bug in the ppl backend of polyhedron

New methods for polyhedron:
* #27534: Implement Lawrence extension for polytopes

### Sage 8.7

Improvements:
* #18214: Bug in volume computation of polyhedron

New methods for polyhedron:
* #22574: Add .change_ring() method for polyhedra 

### Sage 8.4

Improvements:
* #22701: Setting up a Polyhedron from both Vrep and Hrep
* #24837: Improve the output of repr_pretty for Polyhedron 
* #25090: Upgrade pynormaliz to 1.15 or higher (2.0?) 
* #26077: Document and doctest constructing polyhedra over number fields
* #26365: Library of polytopes should allow specifying backend=... (follow-up) 

New methods for polyhedron
* #22575: Add .change_backend() method for polyhedra 
* #24847: Implement stacking onto a face of a polyhedron

### Sage 8.3

Improvements:
* #22572: Add a thematic tutorial on the polyhedron class
* #22984: Upgrade normaliz to 3.5.3 and pynormaliz to 1.12
* #24152: Bug when converting a Sage polyhedron into Polymake pexpect
* #24662: Upgrade scipoptsuite to 5.0.1
* #24835: Change error message in construction of polyhedron object
* #24846: Make the face lattice of a polyhedron a lattice
* #25081: The polar of a polyhedron should carry the backend used
* #25095: polygon3d ignores the "alpha" (and equivalent "opacity") argument

New methods for polyhedron:
* #24848: join of polytopes
* #24849: (sub)direct sums of polytopes
* #24886: one-point suspension and face split of polyhedron

### Sage 8.2

Improvements:
* #21937: Library of polytopes accepts a backend parameter
* #22455: Fixed _facet_adjacency_matrix of non-full-dim. polyhedron
* #22524: Optimize computing points of lattice polytopes
* #23555: Bounding box bug in Polyhedron plots
* #23685: Minkowski -> minkowski
* #24047: Fixed Polyhedron.affine_hull() raises AssertionError
  
New methods for polyhedron:
* #24451: get_integral_point
 
### Sage 8.1

Improvements:
* #16045: Polytope volume function engines produce different results
* #22391: Always use PPL for facet normals of lattice polytopes
* #22400: Transpose text databases of reflexive polytopes for PALP
* #22552: 2 bugs creating a simple 2-point Polytope
* #22558: Fixed: Volume of polyhedron does not handle unbounded polyhedron properly
* #22565: Fixed sage_input to include the backend used
* #22605: Improved the polyhedron constructor
* #23355: Fixed: affine hull of one point polyhedron
* #24154: Fixed equation handling in .to_linear_program and integral_points_count

### Sage 8.0

Here is a sample of changes related to Polyhedral Geometry in this release.

Highlights:
* #13517: New class for Voronoi Diagrams
* #22522: Integration with Latte (function .integrate() )
* #22683: Backend polymake for polyhedron
* #22824: Add see also section to integrate over a polytope

Improvements:
* #11759: octahedron() and icosahedron() produce "non-enclosed" polyhedra
* #15253: Cartesian product of polyhedra with different dimension fails
* #20887: Integration of polynomials over polytopes with LattE
* #21270: Polyhedron RDF face lattice bug / intersection of polyhedra
* #21993: Fixed overflow in integral_points()
* #22310: Use PPL for facet normals of full-dimensional polytopes
* #22498: Add .normal_fan() and .face_fan() methods for rational bounded polyhedra
* #22562: Lattice point count with preprocessing
* #22578: Polyhedron.bounding_box: New keyword argument integral_hull, use it in .integral_points
* #22568: Polyhedron_ZZ should inherit from Polyhedron_QQ, not Polyhedron_base
* #22622: Inconsistency in the .is_lattice_polytope() method
* #22804: Add isometry feature to affine_hull of polyhedra
* #22824: Add see also section to integrate over a polytope
* #22938: Fixed normaliz backend with empty polyhedron

### Sage 7.6

Improvements:
* #17264: Polyhedron function broken with floats in sage-6.3 (worked in sage-6.2)
* #18220: disallow non exact fields for the 'field' backend
* #22122: Remove deprecated code in geometry
* #22275: Implement duality of faces for reflexive polytopes
* #22309: Use PPL for computing vertices of LatticePolytope
* #22469: Deprecate/remove sage/geometry/polytope.py
* #22496: documentation of Combinatorial and Discrete Geometry
* #22497: generic latte_int interface to count
* #22505: perl_term_readline_gnu fails to install
* #22534: Add "long time" to doctests in the geometry component
* #22546: Improve combinatorial_automorphism_group in polyhedra class
* #22551: Deprecate the old .field() method from polyhedron class
* #22578: Polyhedron.bounding_box: New keyword argument integral_hull, use it in .integral_points

New methods for Polyhedron:
* #18128: Add a face truncation method to Polyhedron class
* #20887: Integration of polynomials over polytopes with LattE
* #22416: Add .is_inscribed() method to polytopes
* #22417: .neighborliness() and .is_neighborly(): Add neighborly methods for polyhedra
* #22500: Add .is_combinatorially_isomorphic() method to polyhedra

New methods for SimplicialComplexes:
* #22466: Implement star and stellar subdivision of a face of simplicial complex