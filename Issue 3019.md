# Issue 3019: Integrate Frobby into Sage

Issue created by migration from Trac.

Original creator: broune

Original creation time: 2008-04-24 18:06:43

Assignee: broune

Keywords: monomial ideal, decomposition, frobby, spkg

This ticket is about improving the Frobby spkg (attached) enough that it is suitable for inclusion as a standard component of Sage. Frobby is a software system for performing computations on monomial ideals, such as computing minimal generators, colons, intersections, irreducible decomposition, maximal standard monomials, irreducible decomposition and Alexander dual.

The point of such a program is that these operations can be performed incomparably faster on monomial ideals than on general multivariate ideals, and performing these operations on monomial ideals is a useful computation. Frobby is the fastest program today on these kinds of problems. This is especially true for it current main feature, which is to compute irreducible decomposition of monomial ideals, which is documented in the Slice paper preprint at www.broune.com/papers

Frobby is written in C++ and is licensed as GPL v. 2.0 or later. It depends only on GMP, and is available at www.broune.com/frobby/ . It builds using a makefile with no user interaction, and there is a makefile target for creating a statically linked library. It is developed on Cygwin and Mac OS 10.5. It includes a large automated test suite available as a makefile target. The functionality is exposed as a command-line program, and as a C++ header file that references no internal data structures.


---

Comment by mabshoff created at 2008-04-24 21:13:26

Resolution: duplicate


---

Comment by mabshoff created at 2008-04-24 21:13:26

This is a dupe of #3018.

Cheers,

Michael
