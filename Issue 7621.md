# Issue 7621: usability issues with MIP

archive/issues_007621.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  ncohen\n\nI have two small usability issues to report for the MIP interface:\n\n* Why is `p_mipvariables` a semi-private variable? There should be a method to get the variables defined so far (e.g. `p.get_mip_variables`).\n\n* Why are `p.__INTEGER`,`p.__BINARY`,`p.__REAL` private? This way the user needs to remember the integer assignment, which is unnecessary. Just rename them `p.INTEGER` etc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7621\n\n",
    "created_at": "2009-12-08T13:49:57Z",
    "labels": [
        "numerical",
        "minor",
        "enhancement"
    ],
    "title": "usability issues with MIP",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7621",
    "user": "malb"
}
```
Assignee: jkantor

CC:  ncohen

I have two small usability issues to report for the MIP interface:

* Why is `p_mipvariables` a semi-private variable? There should be a method to get the variables defined so far (e.g. `p.get_mip_variables`).

* Why are `p.__INTEGER`,`p.__BINARY`,`p.__REAL` private? This way the user needs to remember the integer assignment, which is unnecessary. Just rename them `p.INTEGER` etc.

Issue created by migration from https://trac.sagemath.org/ticket/7621





---

archive/issue_comments_065125.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2009-12-08T14:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7621#issuecomment-65125",
    "user": "ncohen"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_065126.json:
```json
{
    "body": "* mipvariables is private because it is just meant to update the variable's name on the (rare) occasions when the users do nto want to solve the LP but want to export it to a LP file ( in which case the variables are expected to \"mean\" something, and not to be x_1 x_2 x_3 etc...\n\n      On which occasion do you think the user may be interested in getting the list of the variables ? I thought the only important thing was for the user to have one way to refer to them, but getting a variable \"back\" would not tell him what this variable means...\n\n    * Well, it is because the user can set variables to a type he chooses by using p.set_binary or p.set_integer, etc... Do you think they should be renamed to be public ?\n\nI know there are many ugly parts in this code that needs to be corrected, and I can not do this alone, as it needs different views to be improved... Thank you for your help !! :-)\n\nNathann",
    "created_at": "2009-12-08T14:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7621#issuecomment-65126",
    "user": "ncohen"
}
```

* mipvariables is private because it is just meant to update the variable's name on the (rare) occasions when the users do nto want to solve the LP but want to export it to a LP file ( in which case the variables are expected to "mean" something, and not to be x_1 x_2 x_3 etc...

      On which occasion do you think the user may be interested in getting the list of the variables ? I thought the only important thing was for the user to have one way to refer to them, but getting a variable "back" would not tell him what this variable means...

    * Well, it is because the user can set variables to a type he chooses by using p.set_binary or p.set_integer, etc... Do you think they should be renamed to be public ?

I know there are many ugly parts in this code that needs to be corrected, and I can not do this alone, as it needs different views to be improved... Thank you for your help !! :-)

Nathann



---

archive/issue_comments_065127.json:
```json
{
    "body": "This is 10 months old and the whole class is being rewritten in #10043. Besides the user has no need of the __REAL __INTEGER and __BINARY variables anymore (the method new_variable has been rewritten since).\n\nNathann",
    "created_at": "2010-10-09T08:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7621#issuecomment-65127",
    "user": "ncohen"
}
```

This is 10 months old and the whole class is being rewritten in #10043. Besides the user has no need of the __REAL __INTEGER and __BINARY variables anymore (the method new_variable has been rewritten since).

Nathann



---

archive/issue_comments_065128.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-10-09T08:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7621#issuecomment-65128",
    "user": "mpatel"
}
```

Resolution: invalid
