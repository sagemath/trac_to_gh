# Issue 3018: Integrate Frobby into Sage

Issue created by migration from Trac.

Original creator: broune

Original creation time: 2008-04-24 18:06:24

Assignee: broune

Keywords: monomial ideal, decomposition, frobby, spkg

This ticket is about improving the Frobby spkg (attached) enough that it is suitable for inclusion as a standard component of Sage. Frobby is a software system for performing computations on monomial ideals, such as computing minimal generators, colons, intersections, irreducible decomposition, maximal standard monomials, irreducible decomposition and Alexander dual.

The point of such a program is that these operations can be performed incomparably faster on monomial ideals than on general multivariate ideals, and performing these operations on monomial ideals is a useful computation. Frobby is the fastest program today on these kinds of problems. This is especially true for it current main feature, which is to compute irreducible decomposition of monomial ideals, which is documented in the Slice paper preprint at www.broune.com/papers

Frobby is written in C++ and is licensed as GPL v. 2.0 or later. It depends only on GMP, and is available at www.broune.com/frobby/ . It builds using a makefile with no user interaction, and there is a makefile target for creating a statically linked library. It is developed on Cygwin and Mac OS 10.5. It includes a large automated test suite available as a makefile target. The functionality is exposed as a command-line program, and as a C++ header file that references no internal data structures.


---

Comment by broune created at 2008-05-01 01:30:48

Changing status from new to assigned.


---

Comment by broune created at 2008-05-01 01:35:59

This is an interface to and spkg for Frobby that uses popen for communication in the same way that the gfan interface does. It currently implements irreducible decomposition for monomial ideals, which was the computation that initially motivated the development of Frobby.


---

Comment by mabshoff created at 2008-05-01 03:48:08

For the record: We usually do not attach spkgs to track ticket, but put them up on an external website and then link them from a ticket via the comment section.

Cheers,

Michael


---

Comment by broune created at 2008-05-20 00:20:04

New spkg available at

http://www.broune.com/frobby/frobby-0.7.6.spkg

This version has several improvements, most of which have been done by Michael Mabshoff.


---

Comment by broune created at 2008-05-20 00:51:55

This is the only patch needed.


---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2008-05-22 23:18:07

Mhansen gave the patch a positive review and the spkg is good according to me :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-22 23:18:20

Merged in Sage 3.0.2.rc0


---

Comment by mabshoff created at 2008-05-22 23:18:20

Resolution: fixed
