# Issue 6602: [with SPKG, need review] GLPK for SAGE

archive/issues_006602.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  wstein mvngu\n\nGLPK ( http://www.gnu.org/software/glpk/ ) is a Linear Program solver from GNU. It can also solve Mixed Integer Programs, and is needed for :\nhttp://trac.sagemath.org/sage_trac/ticket/6502\n\nMore informations on :\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/9da47e06bcdfc49f\n\nIssue created by migration from https://trac.sagemath.org/ticket/6602\n\n",
    "created_at": "2009-07-23T14:08:35Z",
    "labels": [
        "component: numerical"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with SPKG, need review] GLPK for SAGE",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6602",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jkantor

CC:  wstein mvngu

GLPK ( http://www.gnu.org/software/glpk/ ) is a Linear Program solver from GNU. It can also solve Mixed Integer Programs, and is needed for :
http://trac.sagemath.org/sage_trac/ticket/6502

More informations on :
http://groups.google.com/group/sage-devel/browse_thread/thread/9da47e06bcdfc49f

Issue created by migration from https://trac.sagemath.org/ticket/6602





---

archive/issue_comments_053931.json:
```json
{
    "body": "I'm not sure what needs to be checked here. It installs fine on an amd64 ubuntu 9.04 machine and passes sage -testall.\n\nAre there any tests I should run? I saw nothing on the url given in the ticket but I am not an OR person.\n\nPositive review from me as far as I can tell, as an optional package.",
    "created_at": "2009-07-25T23:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53931",
    "user": "https://github.com/wdjoyner"
}
```

I'm not sure what needs to be checked here. It installs fine on an amd64 ubuntu 9.04 machine and passes sage -testall.

Are there any tests I should run? I saw nothing on the url given in the ticket but I am not an OR person.

Positive review from me as far as I can tell, as an optional package.



---

archive/issue_comments_053932.json:
```json
{
    "body": "I think that most of the tests of this spkg will be done in http://trac.sagemath.org/sage_trac/ticket/6502\n\nI hope it will be possible to quickly include all of this into SAGE !! ( Oh, and this spkg is meant to be standard, not just optional !! )",
    "created_at": "2009-07-26T00:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53932",
    "user": "https://github.com/nathanncohen"
}
```

I think that most of the tests of this spkg will be done in http://trac.sagemath.org/sage_trac/ticket/6502

I hope it will be possible to quickly include all of this into SAGE !! ( Oh, and this spkg is meant to be standard, not just optional !! )



---

archive/issue_comments_053933.json:
```json
{
    "body": "It's rather difficult to include this SPKG when there are (as yet) no functions in the Sage library to test its functionalities. Once #6502 gets positive review, this SPKG could then be merged in the Sage standard packages repository.",
    "created_at": "2009-07-26T02:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53933",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

It's rather difficult to include this SPKG when there are (as yet) no functions in the Sage library to test its functionalities. Once #6502 gets positive review, this SPKG could then be merged in the Sage standard packages repository.



---

archive/issue_comments_053934.json:
```json
{
    "body": "We no longer use \"SAGE\". The days of that capitalization are over. Now use \"Sage\" instead.",
    "created_at": "2009-07-26T02:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53934",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

We no longer use "SAGE". The days of that capitalization are over. Now use "Sage" instead.



---

archive/issue_comments_053935.json:
```json
{
    "body": "I object to including this as standard just because of consistency concerns - I think this needs a vote on sage-devel.",
    "created_at": "2009-07-31T23:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53935",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I object to including this as standard just because of consistency concerns - I think this needs a vote on sage-devel.



---

archive/issue_comments_053936.json:
```json
{
    "body": "Note: I said \"Positive review from me as far as I can tell, as an optional package. \"",
    "created_at": "2009-07-31T23:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53936",
    "user": "https://github.com/wdjoyner"
}
```

Note: I said "Positive review from me as far as I can tell, as an optional package. "



---

archive/issue_comments_053937.json:
```json
{
    "body": "The proposal here is to merge the SPKG in the **optional** packages repository.",
    "created_at": "2009-07-31T23:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53937",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The proposal here is to merge the SPKG in the **optional** packages repository.



---

archive/issue_comments_053938.json:
```json
{
    "body": "I forgot all about the voting process I immediately send a message on Sage-devel about it.\n\nThis package has to be included in the --standard-- package repository if we want Sage to have any native LP feature ( see #6502 ). Coin-or and Cplex are both GPL-uncompatible ;-)",
    "created_at": "2009-08-01T07:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53938",
    "user": "https://github.com/nathanncohen"
}
```

I forgot all about the voting process I immediately send a message on Sage-devel about it.

This package has to be included in the --standard-- package repository if we want Sage to have any native LP feature ( see #6502 ). Coin-or and Cplex are both GPL-uncompatible ;-)



---

archive/issue_comments_053939.json:
```json
{
    "body": "The vote is going on there :\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/fed15c54478e8d5",
    "created_at": "2009-08-01T07:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53939",
    "user": "https://github.com/nathanncohen"
}
```

The vote is going on there :
http://groups.google.com/group/sage-devel/browse_thread/thread/fed15c54478e8d5



---

archive/issue_comments_053940.json:
```json
{
    "body": "I could be wrong but I think trac is for optional packages. IIRC, once it is optional (ie, posted to http://www.sagemath.org/packages/optional/) then a public vote is carried out on sage-devel.",
    "created_at": "2009-08-01T13:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53940",
    "user": "https://github.com/wdjoyner"
}
```

I could be wrong but I think trac is for optional packages. IIRC, once it is optional (ie, posted to http://www.sagemath.org/packages/optional/) then a public vote is carried out on sage-devel.



---

archive/issue_comments_053941.json:
```json
{
    "body": "I did not know that !!!\n\nI'm pretty new aboard, and the only thing I wrote for Sage was an interface for Cliquer, which has seemingly found a shortcut through all these steps ;-)\n\nI may be in a hurry, but it is just because :\n* I am impatient to see this patch accepted \n* I have already written several graph functions waiting to be included in the Graph class that I will not post until MIP is included into Sage \n\nSorry again ! I'll try to be a bit more patient ;-)",
    "created_at": "2009-08-01T15:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53941",
    "user": "https://github.com/nathanncohen"
}
```

I did not know that !!!

I'm pretty new aboard, and the only thing I wrote for Sage was an interface for Cliquer, which has seemingly found a shortcut through all these steps ;-)

I may be in a hurry, but it is just because :
* I am impatient to see this patch accepted 
* I have already written several graph functions waiting to be included in the Graph class that I will not post until MIP is included into Sage 

Sorry again ! I'll try to be a bit more patient ;-)



---

archive/issue_comments_053942.json:
```json
{
    "body": "Changing component from numerical to optional packages.",
    "created_at": "2009-08-02T08:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53942",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing component from numerical to optional packages.



---

archive/issue_comments_053943.json:
```json
{
    "body": "Changing assignee from jkantor to tbd.",
    "created_at": "2009-08-02T08:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53943",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing assignee from jkantor to tbd.



---

archive/issue_comments_053944.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-04T09:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53944",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053945.json:
```json
{
    "body": "Merged in optional packages repository. The new optional package can be found here:\n\nhttp://www.sagemath.org/packages/optional/glpk-4.38.spkg",
    "created_at": "2009-08-04T09:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6602#issuecomment-53945",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in optional packages repository. The new optional package can be found here:

http://www.sagemath.org/packages/optional/glpk-4.38.spkg
