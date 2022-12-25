# Issue 7270: numerical.MIP : named constraints and variables, methods, structure, etc ...

archive/issues_007270.json:
```json
{
    "body": "Assignee: jkantor\n\nHello everybody !!!\n\nThis is the last \"fundamental\" modification of class numerical.MIP. From now on, the methods' names should not change anymore, and the patches based upon this class should not have to be updated each time an update is sent for numerical.mip.\n\nThis patch changes mainly comports changes of structure in this class. Here is the list of what is includes :\n\n* {{{ \n  from sage.numerical.mip import * \n  }}}\n  has been replaced by \n  {{{\n  from sage.numerical.mip import MixedIntegerLinearProgram\n  }}}\n  as asked in #7012\n\n* Private variables have been renamed with a '_' in front of their names. The user is not interested in them\n    * ``x`` to ``_x``\n    * ``values`` to ``_values``\n    * all the variables defining the Linear Program ( variables types, bounds, name, objective, etc ) have been renamed. The new structure is easier to understand, and the code includes as a comment a Tree of these variables to explain it better.\n       \n* The ``__eq__``  method has been added ( asked in #6913 )\n* Names in the Linear Program \n    * Methods have been added to define names for :\n        * The whole problem : ``set_problem_same``\n  * The objective function : ``set_objective_name``\n    * Methods have been modified to define names for :\n        * The variables : ``new_variable`` now can take a ``name`` as part of its input\n  * The constraints : similarly for ``add_constraint``\n* A function ``_update_variables_name``. The name of variables are only computed before\n  the LP is written to a file. They are obviously useless in the solving process.\n* A function ``constraints`` to list the constraints of the LP.\n* Function ``write_mps`` and ``write_lp`` to export the problem to MPS and LP file format ( see the docstrings for more information )\n* Class ``MIPSolverException`` includes doctests of exceptions for GLPK ( CBC will follow )\n\nSome comments have been added to the code to ease reviews :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7270\n\n",
    "created_at": "2009-10-23T15:28:31Z",
    "labels": [
        "component: numerical"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "numerical.MIP : named constraints and variables, methods, structure, etc ...",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7270",
    "user": "https://github.com/nathanncohen"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/7270





---

archive/issue_comments_060356.json:
```json
{
    "body": "Attachment [trac_7270.patch](tarball://root/attachments/some-uuid/ticket7270/trac_7270.patch) by @nathanncohen created at 2009-10-23 15:29:11",
    "created_at": "2009-10-23T15:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7270#issuecomment-60356",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_7270.patch](tarball://root/attachments/some-uuid/ticket7270/trac_7270.patch) by @nathanncohen created at 2009-10-23 15:29:11



---

archive/issue_comments_060357.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-23T15:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7270#issuecomment-60357",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060358.json:
```json
{
    "body": "Looks good, positive review.",
    "created_at": "2009-12-01T17:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7270#issuecomment-60358",
    "user": "https://github.com/malb"
}
```

Looks good, positive review.



---

archive/issue_comments_060359.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-01T17:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7270#issuecomment-60359",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060360.json:
```json
{
    "body": "I had to add a missing #optional on line 550.",
    "created_at": "2009-12-02T08:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7270#issuecomment-60360",
    "user": "https://github.com/mwhansen"
}
```

I had to add a missing #optional on line 550.



---

archive/issue_comments_060361.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-02T08:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7270#issuecomment-60361",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017195.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-02T08:00:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7270",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7270#event-17195"
}
```
