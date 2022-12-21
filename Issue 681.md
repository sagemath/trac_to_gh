# Issue 681: new MQ submodule for sage.crypto [with patch]

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-09-17 16:00:55

Assignee: was

The attached patch implements a *MPolynomialSystem*, a *MPolynomialSystemGenerator* class, and as a generator for small scale AES variants.


*MPolynomialSystem* is supposed to model multivariate polynomial systems as they appear in e.g. algebraic cryptanalysis. The implemented design is as follows: There is a class *MPolynomialSystem* which models the actual polynomial system. This class contains a list of *MPolynomialRoundSystems* to model the rounds of a cipher to add some structure. *MPolynomialSystem* is furthermore specialised to *MPolynomialSystem_gf2[e]* classes which have additional features. E.g. systems over `GF(2^e)` can be projected down to `GF(2)` and systems over `GF(2)` may eventually contain rountines for ANF-CNF conversion.

Also there is a class called *MPolynomialSystemGenerator* which is meant as a base class for specific generators for polynomial systems like AES or the Courtois Toy Cipher (CTC).

The patch also contains a generator for polynomial systems for small scale AES variants (SR) over `GF(2)` and `GF(2^e)` as introduced in http://www.isg.rhul.ac.uk/~sean/smallAES-fse05.pdf .



---

Attachment


---

Comment by malb created at 2007-09-17 17:18:26

Great, first bugfix already. See second attachment.


---

Attachment


---

Comment by was created at 2007-09-21 01:55:05

Resolution: fixed
