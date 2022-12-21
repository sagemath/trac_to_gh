# Issue 4857: [with spkg, needs discussion] Example C Library

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2008-12-23 10:07:43

Assignee: GeorgSWeber

(see also the respective thread at sage-devel)

Although this spkg is pretty small, putting it in a trac ticket is probably not the best idea. But currently, I haven't got access to any other web space where I could place it.

Install with "sage -i exampleclib-1.0.0.spkg"; the documentation is the under

$SAGE_ROOT/devel/exampleclib/src/README.txt

$SAGE_ROOT/devel/exampleclib/src/doc/*


---

Comment by mabshoff created at 2008-12-23 10:14:39

-1 by a wide margin. This spkg does numerous things badly and introduces many "features" we don't need or are completely overdesigned. The idea about spkg-install and its friends is KISS and this certainly isn't it.

The place to have this is not trac either.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-23 10:43:28

I have removed the attached spkg. It can now be found at

http://sage.math.washington.edu/home/mabshoff/exampleclib-1.0.0.spkg

Cheers,

Michael


---

Attachment

a new script "sage-create-spkg" to go in the scripts repo /local/bin


---

Attachment

two example "upstream src" packages (sample spkg input) to go in the examples/ repo


---

Comment by GeorgSWeber created at 2008-12-30 12:36:55

rewritten and enhanced chapter about spkg in prog.tex resp. the doc/ repo (probably rather easily rebased after the ReST move)


---

Comment by GeorgSWeber created at 2008-12-30 12:47:53

Changing component from experimental package to documentation.


---

Attachment

The current documentation in the Sage Developer's Guide says in Chapter 2, subsection 8.1, item (f) about Creating a New spkg: ... Post a copy on the Sage trac server ...

This is outdated. I took the opportunitiy to rewrite subsection 8.1, add two subsections 8.2 and 8.3, and assemble two live examples (to go under the examples directory) and a script "sage-create-spkg" which e.g. creates a template SPKG.txt and the mandatory hg repo. The script called on the examples result in working spkg, that install fine.

Well, at least at the author's Mac. So it would be good if the referee could use and test it on a Linux machine.

The contents are based on a discussion with Michael Abshoff on sage-devel, half of the credit (at least) goes to him. All the remaining mistakes are mine, of course :-)


---

Comment by was created at 2009-03-16 10:54:55

MABSHOFF:

"I think in its current form 4857-examples.patch should not go in, in
fact it shouldn't go in at all IMHO.

4857-scripts.patch is too complicated IMHO, but salvageable."

So I change this to "needs work".


---

Comment by jhpalmieri created at 2009-05-05 18:34:20

See #5990 for a closely related ticket -- a patch to the documentation, based in large part on 4857-doc.patch.


---

Comment by mvngu created at 2010-02-02 06:07:38

Documentation on producing a new spkg is already in the Developers' Guide in the form of the section [Producing New Sage Packages](http://www.sagemath.org/doc/developer/producing_spkgs.html). Tickets #8079 and #8104 add documentation on patching an existing spkg. So I think the subject of this ticket can be changed to something else other than documentation on producing spkg's.


---

Comment by jdemeyer created at 2014-09-02 09:06:34

Obsolete by the git transition.


---

Comment by jdemeyer created at 2014-09-02 09:06:34

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2014-09-09 14:53:46

Resolution: wontfix
