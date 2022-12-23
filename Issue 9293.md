# Issue 9293: Better expose GAP's character tables from Sage

Issue created by migration from https://trac.sagemath.org/ticket/9293

Original creator: nthiery

Original creation time: 2010-06-21 08:49:18

Assignee: joyner

GAP's character tables could be better exposed from Sage. One
approach is to just improve the GAP interface: conversion of objects
back to Sage (see #7890), introspection, ... Another approach is to
implement an abstract class in Sage for character tables, with a
concrete subclass whose elements wraps GAP's character tables. The
later offers a more integrated user experience, at the price of
needing to explicitly wrap all GAP's functions.

Here is a rough draft of an abstract class, written during Sage Days 20:


```
class AbstractCharacterTable

    def row_indices()
        """
	That's irredinfo in Chevie (a Family of irreducible reps)
	"""

    def column_indices()
        classparam / classname in Chevie (a Family of conjugacy classes)

    def __getitem__(self, r,c)

    def powermap(self, c, n)
        """
	Specific to group

	INPUT:

	 - ``c`` - the index of a conjugacy class C

	Returns the index of the conjugacy class of x^n for x in C

	"""

    def irreducibles(self):
        """
        returns the character table as a matrix
	"""

    def orders(self):
        """
        orders of the conjugacy classes
        """

    def centralizer(self):
        """
	cardinality of the centralizer of the conjugacy classes
	"""
```


For the record, here is the data structure of a character table of a
Coxeter group in GAP3:


```
T := CharTable(CoxeterGroup("E",8));
RecFields(T.operations);
[ "name", "operations", "ScalarProduct", "NoMessageScalarProduct", "Print", 
  "Eigenvalues", "IsAbelian", "IsCyclic", "IsSimple", "IsSolvable", 
  "SupersolvableResiduum", "IsSupersolvable", "UpperCentralSeriesFactor", 
  "UpperCentralSeries", "LowerCentralSeries", "IsNilpotentFactor", 
  "IsNilpotent", "IsNilpotentNormalSubgroup", "AbelianInvariants", "Agemo", 
  "Automorphisms", "Centre", "CharacterDegrees", "DerivedSubgroup", 
  "ElementaryAbelianSeries", "Exponent", "FittingSubgroup", "InertiaSubgroup",
  "MaximalNormalSubgroups", "NormalClosure", "NormalSubgroups", "Size", 
  "FusionConjugacyClasses", "SizesConjugacyClasses", "*", "/", "mod", 
  "Restricted", "Induced", "Lattice", "Display", "CharNames", "StringEntry" ]
```

