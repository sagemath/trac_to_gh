# Issue 7308: cliquer's spkg-install does not work on cygwin

archive/issues_007308.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  dkirkby @williamstein\n\nKeywords: cliquer\n\nThe section where SAGESOFLAGS are set assumes that the operating system is Linux, OS X, or Solaris.  The spkg-install script exists even if SAGE_PORT is set to yes.\n\n\nI'll post a patch and a new SPKG here shortly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7308\n\n",
    "created_at": "2009-10-26T09:23:36Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "cliquer's spkg-install does not work on cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7308",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tbd

CC:  dkirkby @williamstein

Keywords: cliquer

The section where SAGESOFLAGS are set assumes that the operating system is Linux, OS X, or Solaris.  The spkg-install script exists even if SAGE_PORT is set to yes.


I'll post a patch and a new SPKG here shortly.

Issue created by migration from https://trac.sagemath.org/ticket/7308





---

archive/issue_comments_060915.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-26T09:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7308#issuecomment-60915",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060916.json:
```json
{
    "body": "Attachment [trac_7308.patch](tarball://root/attachments/some-uuid/ticket7308/trac_7308.patch) by @mwhansen created at 2009-10-27 13:49:28",
    "created_at": "2009-10-27T13:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7308#issuecomment-60916",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7308.patch](tarball://root/attachments/some-uuid/ticket7308/trac_7308.patch) by @mwhansen created at 2009-10-27 13:49:28



---

archive/issue_comments_060917.json:
```json
{
    "body": "I'm not in a position to test this, but if you need to make any changes, I would suggest the following would be helpful. Some are I admit code I introduced, which is probaby not necessary. None are particularly important. \n\n* There is no longer any need to have \n\n\n```\nif [ -n \"$SAGE_FORTRAN_LIB\" ] && [ ! -e \"$SAGE_FORTRAN_LIB\" ]; then\n    echo \"SAGE_FORTRAN_LIB is defined as $SAGE_FORTRAN_LIB, but does not exist\"\n    exit 1\nfi\n```\n \nsince code in the recent *prereq-0.4* (#7021) script checks this, so the above code is redundant. \n\n* There is no need to have the following line\n\n` if [ \"x$SAGE64\" = \"xyes\" ] || [ \"x$SAGE64\" = \"x1\" ]; then `\n\nIt should instead be replaced by\n\n   ` if [ \"x$SAGE64\" = \"xyes\" ]; then `\n\nsince some earlier code in the *prereq-0.3* script written by William only allows SAGE64 to be unset, or set to *yes* or *no*. It is not possible to set it to *1*, so there is no point testing if it is *1*. The same behaviour is followed in my recent updated to prereq-0.4 (#7021) and also to prereq-0.5 which I have awaiting review (#7352)\n\n* There is no need to have \n  {{{\n   # We exit here, since we are possibly on an unsupported platform.\n   if [ -n \"${SAGE_PORT:-x}\" ]; then\n       echo \"Cannot determine your platform or it is not supported... exiting\"\n       exit 1\n   else\n  }}}\nsince the recent *prereq-0.4* update will exit for **all** unsupported platforms unless SAGE_PORT is set to 'yes'.",
    "created_at": "2009-10-30T14:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7308#issuecomment-60917",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm not in a position to test this, but if you need to make any changes, I would suggest the following would be helpful. Some are I admit code I introduced, which is probaby not necessary. None are particularly important. 

* There is no longer any need to have 


```
if [ -n "$SAGE_FORTRAN_LIB" ] && [ ! -e "$SAGE_FORTRAN_LIB" ]; then
    echo "SAGE_FORTRAN_LIB is defined as $SAGE_FORTRAN_LIB, but does not exist"
    exit 1
fi
```
 
since code in the recent *prereq-0.4* (#7021) script checks this, so the above code is redundant. 

* There is no need to have the following line

` if [ "x$SAGE64" = "xyes" ] || [ "x$SAGE64" = "x1" ]; then `

It should instead be replaced by

   ` if [ "x$SAGE64" = "xyes" ]; then `

since some earlier code in the *prereq-0.3* script written by William only allows SAGE64 to be unset, or set to *yes* or *no*. It is not possible to set it to *1*, so there is no point testing if it is *1*. The same behaviour is followed in my recent updated to prereq-0.4 (#7021) and also to prereq-0.5 which I have awaiting review (#7352)

* There is no need to have 
  {{{
   # We exit here, since we are possibly on an unsupported platform.
   if [ -n "${SAGE_PORT:-x}" ]; then
       echo "Cannot determine your platform or it is not supported... exiting"
       exit 1
   else
  }}}
since the recent *prereq-0.4* update will exit for **all** unsupported platforms unless SAGE_PORT is set to 'yes'.



---

archive/issue_comments_060918.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-07T05:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7308#issuecomment-60918",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060919.json:
```json
{
    "body": "The actual patch looks fine to me.    Kirkby's comments are all fine, but of course shouldn't be part of this ticket.  There is no point in confusing things by doing too much at once.",
    "created_at": "2010-02-07T05:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7308#issuecomment-60919",
    "user": "https://github.com/williamstein"
}
```

The actual patch looks fine to me.    Kirkby's comments are all fine, but of course shouldn't be part of this ticket.  There is no point in confusing things by doing too much at once.



---

archive/issue_comments_060920.json:
```json
{
    "body": "I think the existing package is called `cliquer-1.2.p3`.  Should we make the new one `p4`?",
    "created_at": "2010-02-10T16:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7308#issuecomment-60920",
    "user": "https://github.com/qed777"
}
```

I think the existing package is called `cliquer-1.2.p3`.  Should we make the new one `p4`?



---

archive/issue_comments_060921.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-10T23:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7308#issuecomment-60921",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_060922.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-13T06:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7308#issuecomment-60922",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060923.json:
```json
{
    "body": "I rebased Mike's patch, refereed it, and posted a new spkg with the rebased patch here:\n\n   http://wstein.org/home/wstein/ports/cygwin/cliquer-1.2.p4.spkg",
    "created_at": "2010-02-13T06:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7308#issuecomment-60923",
    "user": "https://github.com/williamstein"
}
```

I rebased Mike's patch, refereed it, and posted a new spkg with the rebased patch here:

   http://wstein.org/home/wstein/ports/cygwin/cliquer-1.2.p4.spkg



---

archive/issue_comments_060924.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-13T06:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7308#issuecomment-60924",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060925.json:
```json
{
    "body": "Feel free to open another ticket to address the issues that drkirkby raised.",
    "created_at": "2010-02-16T04:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7308#issuecomment-60925",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Feel free to open another ticket to address the issues that drkirkby raised.



---

archive/issue_comments_060926.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-16T04:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7308#issuecomment-60926",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
