# Issue 7270: numerical.MIP : named constraints and variables, methods, structure, etc ...

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-10-23 15:28:31

Assignee: jkantor

Hello everybody !!!

This is the last "fundamental" modification of class numerical.MIP. From now on, the methods' names should not change anymore, and the patches based upon this class should not have to be updated each time an update is sent for numerical.mip.

This patch changes mainly comports changes of structure in this class. Here is the list of what is includes :

   * {{{ 
     from sage.numerical.mip import * 
     }}}
     has been replaced by 
     {{{
     from sage.numerical.mip import MixedIntegerLinearProgram
     }}}
     as asked in #7012

   * Private variables have been renamed with a '_' in front of their names. The user is not interested in them
       * ``x`` to ``_x``
       * ``values`` to ``_values``
       * all the variables defining the Linear Program ( variables types, bounds, name, objective, etc ) have been renamed. The new structure is easier to understand, and the code includes as a comment a Tree of these variables to explain it better.
       
   * The ``__eq__``  method has been added ( asked in #6913 )
   * Names in the Linear Program 
       * Methods have been added to define names for :
           * The whole problem : ``set_problem_same``
	   * The objective function : ``set_objective_name``
       * Methods have been modified to define names for :
           * The variables : ``new_variable`` now can take a ``name`` as part of its input
	   * The constraints : similarly for ``add_constraint``
   * A function ``_update_variables_name``. The name of variables are only computed before
     the LP is written to a file. They are obviously useless in the solving process.
   * A function ``constraints`` to list the constraints of the LP.
   * Function ``write_mps`` and ``write_lp`` to export the problem to MPS and LP file format ( see the docstrings for more information )
   * Class ``MIPSolverException`` includes doctests of exceptions for GLPK ( CBC will follow )

Some comments have been added to the code to ease reviews :-)

Nathann


---

Attachment


---

Comment by ncohen created at 2009-10-23 15:31:02

Changing status from new to needs_review.


---

Comment by malb created at 2009-12-01 17:15:15

Looks good, positive review.


---

Comment by malb created at 2009-12-01 17:15:15

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-02 08:00:34

I had to add a missing #optional on line 550.


---

Comment by mhansen created at 2009-12-02 08:00:34

Resolution: fixed
