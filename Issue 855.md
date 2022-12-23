# Issue 855: lists of optional and experimental packages should have descriptions

Issue created by migration from https://trac.sagemath.org/ticket/855

Original creator: cwitty

Original creation time: 2007-10-12 01:06:43

Assignee: was

It would be very helpful if "sage -optional" and "sage -experimental" listed one- or two-sentence descriptions of each package.  (Several of the packages I had to look up using Google.  Also, it was only by accident that I discovered that "axiom4sage" was the complete axiom distribution, rather than just an axiom interface.)


---

Comment by jhpalmieri created at 2008-12-03 20:12:29

Here are descriptions of the current optional packages, except that I don't actually know what "database_symbolic_data" is.  I was able to do a number of them in a single line; is that helpful?  Also, how do we actually incorporate these?  (Should each description be added, somehow, to the SPKG.txt file for each package?)


ace: Todd-Coxeter coset enumeration via the Advanced Coset Enumerator

biopython: Python tools for computational molecular biology

boehm: The Boehm-Demers-Weiser conservative garbage collector

database_cremona_ellcurve: Cremona's huge database of elliptic curves

database-gap: GAP's databases of finite groups and table of marks

database_jones_numfield: Jones' database of number fields

database_kohel: Kohel's database of modular polynomials

database_odlyzko_zeta: Odlyzko's database for the Riemann zeta function

database_sloane_oeis: Sloane's database from the online encyclopedia of integer sequences

database_stein_watkins_mini: Stein-Watkins database of elliptic curves

database_symbolic_data: ??

dvipng: make PNG and/or GIF graphics from DVI files

extra_docs: documentation for components of Sage (e.g. maxima, singular, etc.)

fricas: an advanced computer algebra system

frobby: provides a number of computations on monomial ideals

gap_packages: several "official" and "undeposited" GAP packages

gcc: GNU C compiler

gdbm: GNU dbm, a set of database routines using extendible hashing

ginv: GINV implements the Gröbner bases method for systems of equations

gmpy: General MultiPrecision arithmetic for Python

gnuplotpy: A pipe-based interface to the gnuplot plotting program

graphviz: Graph Drawing Programs from AT&T Research and Lucent Bell Labs

guppy: Guppy-PE is a library and programming environment for Python,
currently providing in particular the Heapy subsystem, which supports
object and heap memory sizing, profiling and debugging. 

hermes: a semantic XML e-publishing tool for LaTeX authored scientific
articles (for linux only)

java3d: Java 3d libraries

jmol: a Java molecular viewer for three-dimensional chemical
structures (includes source code). 

jsmath-image-fonts: used for rendering TeX characters on computers
that do not have the TeX fonts installed

kash3_linux: sophisticated computations in number fields, in global
function fields, and in local fields (for linux only)

kash3_osx: sophisticated computations in number fields, in global
function fields, and in local fields (for Mac OS X only)

knoboo: Programming notebook for the web

lie: computations with reductive Lie groups and their representations

lrs: reverse search vertex enumeration program/CH package

mpc: a C library for multiple-precision floating-point computations
with correct rounding

mpi4py: MPI is the Message Passing Interface, a standardized and
portable message-passing system designed to function on a wide variety
of parallel computers.  This package is a Python-based implementation
of MPI.

nauty: various tools for finding the automorphism group of a graph,
generating non-isomorphic graphs with certain properties, etc.

nzmath: Python based number theory oriented calculation system

openmpi: an open-source implementation of MPI

openssl: implementation of the Secure Sockets Layer (SSL v2/v3) and
Transport Layer Security (TLS v1) protocols as well as a full-strength
general purpose cryptography library

phc: a solver for polynomial systems by homotopy continuation

pil: Python Imaging Library

polymake: algorithmic treatment of convex polyhedra, finite simplicial
complexes, tight spans of finite metric spaces, polyhedral surfaces,
and other objects

pyopenssl: a Python wrapper around the OpenSSL library

pyx: a Python package for the creation of PostScript and PDF files

trac: web-based software project management and bug/issue tracking system

valgrind: an instrumentation framework for building dynamic analysis tools


---

Comment by malb created at 2008-12-05 02:35:44

> database_symbolic_data: ??

This is the database from http://www.symbolicdata.org/:

"The SymbolicData project is set out to develop concepts and tools for testing Computer Algebra Software (CAS) and to collect relevant data from different areas of Computer Algebra. Tools and data are designed to be used both on a local site for special testing purposes and to manage a central repository at www.symbolicdata.org."


---

Comment by was created at 2009-12-18 04:03:41

This should be done by automatically extracting the first line from the Description section of the SPKG.txt, if it is there. Use a line like this:

```
sage@sagemath:~/www-files/packages/optional$ tar xvf biopython-1.53.p0.spkg biopython-1.53.p0/SPKG.txt
```

or better yet, write a Python script using the tarfile module. 

I'm currently working on this, and hope to close this ticket soon :-)


---

Comment by was created at 2009-12-18 06:02:08

Resolution: fixed


---

Comment by was created at 2009-12-18 06:02:08

OK, I made it so gen_html automatically extracts the SPKG.txt files.   The HTML isn't pretty, but making it so should be another ticket.
