# Issue 4470: Merge Jon Hanke's qudratic forms code into Sage

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-08 21:29:34

Assignee: tbd

CC:  justin cremona tornaria

Jon Hanke wrote some substantial amount of code that is still based on Sage 2.8.14. Get the code ready for review and merge it 

#4120 is relevant here since Justin works on binary quadratic forms.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-08 21:30:09

Changing assignee from tbd to justin.


---

Comment by mabshoff created at 2008-11-08 21:30:09

Changing component from algebra to quadratic forms.


---

Comment by mabshoff created at 2008-11-08 21:43:33

There are large tables in Jon's commit:

```
sage [quadratic_forms]> wc -l tables/*
   39745 tables/brandt-intrau_even_ternaries.html
   30967 tables/brandt-intrau_even_ternaries.py
    1526 tables/brandt-intrau_even_ternaries.sobj
    8366 tables/brandt-intrau_odd_ternaries.html
    5474 tables/brandt-intrau_odd_ternaries.py
     277 tables/brandt-intrau_odd_ternaries.sobj
    4471 tables/Nipp_quaternary_forms__d1080.html
    4519 tables/Nipp_quaternary_forms__d1161.html
    4535 tables/Nipp_quaternary_forms__d1236.html
    4561 tables/Nipp_quaternary_forms__d1308.html
    4446 tables/Nipp_quaternary_forms__d1373.html
    4475 tables/Nipp_quaternary_forms__d1433.html
    4530 tables/Nipp_quaternary_forms__d1492.html
    4533 tables/Nipp_quaternary_forms__d1549.html
    4520 tables/Nipp_quaternary_forms__d1604.html
    4544 tables/Nipp_quaternary_forms__d1656.html
    4518 tables/Nipp_quaternary_forms__d1705.html
    2636 tables/Nipp_quaternary_forms__d1732.html
    4519 tables/Nipp_quaternary_forms__d4to457.html
    4528 tables/Nipp_quaternary_forms__d641.html
    4483 tables/Nipp_quaternary_forms__d777.html
    4490 tables/Nipp_quaternary_forms__d893.html
    4515 tables/Nipp_quaternary_forms__d992.html
   74095 tables/Nipp_quaternary_forms_table.py
    4572 tables/Nipp_quaternary_forms_table.sobj
   45295 tables/Nipp_quaternary_table_as_Hanke_table.sobj
  285140 total
```

These should be moved into its own database spkg.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-08 21:49:10

Some more remaks:

 * commit 10629 is mostly the AUTO code by Bernd Souvignier - the code has been made available under a GPL V2+ compatible license, but that needs to be formalized. It is called via pexpect, but probably can be called via Cython directly. It is only one file. If we keep using the pexpect interface it should be moved into its own spkg.
 * commit 10630 are the tables, which should not go into the history. As mentioned above these should be moved into its own database spkg and probably already be pickled

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-09 00:05:35

For the four extracted patches from Jon's code see

http://sage.math.washington.edu/home/mabshoff/hanke-qf-merge/

There is also some comments in the thread at

http://groups.google.com/group/sage-devel/t/17612419fefaf4d9

Cheers,

Michael


---

Attachment

Changes to existing files in Jon's 2.8.14 quadratic forms patch


---

Comment by tornaria created at 2008-11-09 04:00:11

I've attached a diff with the changed files between stock 2.8.14 and Jon's quadratic forms branch. Note there are several new files in `sage/quadratic_forms/` directory which are not included in this patch. The plan was to pick the relevant changes from this patch, but most of it is already included in 3.1.4 with the following exceptions:
 - `setup.py`: adds extension modules for new files
 - `sage/quadratic_forms/all.py`: adds imports for new files
 - `sage/quadratic_forms/binary_qf.py`: adds comment/todo in docstring for the file
 - `integer_mod.{pxd,pyx`}: implement classes `IntegerMod_gmp_power_of_2`, `IntegerMod_int_power_of_2` and `IntegerMod_int64_power_of_2`, but this are _not_ used in quadratic forms code, so it's irrelevant and can be ignored.


---

Comment by mabshoff created at 2008-11-09 07:11:20

Coverage definitely needs to be improved:

```
sage [sage-3.1.2]>  ./sage -coverageall devel//sage/sage/quadratic_forms/
binary_qf.py: 100% (16 of 16)
count_local_2.pyx: 0% (0 of 1)
cython_testing.pyx: 0% (0 of 4)
extras.py: 25% (2 of 8)
genera/genus.py: 0% (0 of 34)
mass_testing.py: 0% (0 of 3)
quadratic_form__automorphisms2.py: 60% (3 of 5)
quadratic_form__automorphisms.py: 75% (6 of 8)
quadratic_form__count_local_2.py: 0% (0 of 9)
quadratic_form__equivalence_testing.py: 25% (1 of 4)
quadratic_form__evaluate.pyx: 0% (0 of 2)
quadratic_form__genus.py: 0% (0 of 3)
quadratic_form__local_density_congruence.py: 9% (1 of 11)
quadratic_form__local_density_interfaces.py: 14% (1 of 7)
quadratic_form__local_field_invariants.py: 57% (8 of 14)
quadratic_form__local_normal_form.py: 75% (3 of 4)
quadratic_form__local_representation_conditions.py: 12% (2 of 16)
quadratic_form__mass__Conway_Sloane_masses.py: 26% (4 of 15)
quadratic_form__mass.py: 0% (0 of 3)
quadratic_form__mass__Siegel_densities.py: 20% (1 of 5)
quadratic_form__neighbors.py: 75% (3 of 4)
quadratic_form.py: 43% (14 of 32)
quadratic_form__reduction_theory.py: 40% (2 of 5)
quadratic_form__siegel_product.py: 100% (1 of 1)
quadratic_form__split_local_covering.py: 100% (3 of 3)
quadratic_form__ternary_Tornaria.py: 0% (0 of 17)
quadratic_form__theta.py: 50% (2 of 4)
quadratic_form__variable_substitutions.py: 71% (5 of 7)
random_quadraticform.py: 100% (2 of 2)
special_values.py: 60% (3 of 5)
table_conversion.py: 100% (4 of 4)
table_creation.py: 0% (0 of 2)
table_hanke.py: 12% (4 of 32)
table_hanke.pyx: 12% (4 of 32)
tables.py: 15% (5 of 33)
ternary_table_creation.py: 0% (0 of 7)
ternary_table.pyx: 0% (0 of 15)

Overall weighted coverage score:  26.3%
Total number of functions:  377
```

There are a bunch of doctest failures, but a lot of those will be sorted out hopefully by Sunday night:

```
The following tests failed:


	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__local_field_invariants.py
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__local_normal_form.py
	sage -t  devel/sage/sage/quadratic_forms/table_hanke.py
	sage -t  devel/sage/sage/quadratic_forms/special_values.py
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__neighbors.py
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__reduction_theory.py
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__automorphisms.py
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__local_representation_conditions.py
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form.py
	sage -t  devel/sage/sage/quadratic_forms/table_hanke.pyx
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__split_local_covering.py
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__mass__Conway_Sloane_masses.py
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__local_density_congruence.py
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__equivalence_testing.py
	sage -t  devel/sage/sage/quadratic_forms/random_quadraticform.py
	sage -t  devel/sage/sage/quadratic_forms/table_conversion.py
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__siegel_product.py
	sage -t  devel/sage/sage/quadratic_forms/tables.py
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__local_density_interfaces.py
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__automorphisms2.py
Total time for all tests: 129.5 seconds
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-11-11 14:28:11

Justin,

a preliminary diff can be found at
 
http://sage.math.washington.edu/home/mabshoff/john-hanke-qf.diff

There still are renames to be done, but I should have something in the next 24 hours. Feel free to start the review despite the comment in the summary.

Cheers,

Michael


---

Comment by tornaria created at 2009-02-23 03:35:15

Changing assignee from justin to tornaria.


---

Comment by tornaria created at 2009-02-23 03:35:15

Changing status from new to assigned.


---

Comment by tornaria created at 2009-02-23 03:36:23

Initial commit of Jon Hanke's quadratic forms code


---

Attachment

many fixes and doctests for quadratic forms code


---

Attachment

Attached patches:

 - attachment:patch.4470.01-inital_hanke_code: applies Jon Hanke's quadratic forms code into sage. The merge is based in mabshoff work during SD Austin, with some minor updates.
 - attachment:patch.4470.02-fixes_and_doctest: fixes and lots of doctests and documentation to be applied on top of the initial patch. This patch raises the doctest coverage from 33% to over 60%.

The patches apply cleanly on a 3.3 tree, all tests pass in sage.math and my core2 debian/64 laptop.


---

Comment by mabshoff created at 2009-02-23 09:47:48

Hi Gonzalo, Jon,

this patch needs a formal review, so either one of you can give a positive review to the other person's work. We will give an exception to the coverage requirements in this case, but I will open a followup ticket to get coverage up to 100%.

Cheers,

Michael


---

Comment by tornaria created at 2009-02-23 16:20:29

Jon Hanke and I have been working on reviewing the initial patch last week, improving and doctesting the code. Although the coverage is not 100%, and there's most certainly still bugs in the code, it is completely orthogonal to the rest of sage so it won't affect anything else. Given SD13 and AWS soon, we expect to improve it in the next couple of weeks.

I strongly recommend inclusion of this patch into sage.


---

Comment by mabshoff created at 2009-02-24 20:54:33

Ok, everything works, but some doctests need to be marked optional since they depend on ISOM:

```
        sage -t  devel/sage/sage/quadratic_forms/quadratic_form__equivalence_testing.py # 8 doctests failed
        sage -t  devel/sage/sage/quadratic_forms/quadratic_form__automorphisms.py # 6 doctests failed
```


Cheers,

Michael


---

Attachment

Merged 

 * patch.4470.01-inital_hanke_code
 * patch.4470.02-fixes_and_doctest 
 * trac_4770-reviewer.patch

in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-26 14:41:13

As mentioned above this code was merged in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-26 14:41:27

As mentioned above this code was merged in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-26 14:41:27

Resolution: fixed
