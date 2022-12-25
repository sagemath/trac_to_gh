# Issue 4461: fricas-1.0.5 update

archive/issues_004461.json:
```json
{
    "body": "Assignee: @mwhansen\n\nKeywords: axiom interface\n\nThe fricas project [http://groups.google.com/group/fricas-devel/t/813c8e04c3052043?hl=en](http://groups.google.com/group/fricas-devel/t/813c8e04c3052043?hl=en) has a new release (1.0.4) which includes enhancements specifically related to the Sage interface. A new version of the optional fricas package (current verson fricas-1.0.3.p0) needs to be created.\n\nThe procedure involves first building fricas on some convenient platform to generate cached lisp code. This might take about 1 - 2 hours on a fast machine.  This generated code can than be included in a new source distribution created by running\n\n  ../fricas/src/scripts/mkdist.sh --copy_lisp\n\nThe contents of the ./dist directory can be moved to the ./src directory of the spkg. The use of cached lisp allows fricas to be built in about 12 minutes or less on a the target machine.\n\nNote: There may be a problem with clisp support of FFI in Sage. A patch to allow fricas to build without FFI is attached (not yet tested with fricas-1.0.4).\n\nIssue created by migration from https://trac.sagemath.org/ticket/4461\n\n",
    "closed_at": "2009-08-12T16:48:45Z",
    "created_at": "2008-11-07T16:45:58Z",
    "labels": [
        "component: packages: optional",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "fricas-1.0.5 update",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4461",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```
Assignee: @mwhansen

Keywords: axiom interface

The fricas project [http://groups.google.com/group/fricas-devel/t/813c8e04c3052043?hl=en](http://groups.google.com/group/fricas-devel/t/813c8e04c3052043?hl=en) has a new release (1.0.4) which includes enhancements specifically related to the Sage interface. A new version of the optional fricas package (current verson fricas-1.0.3.p0) needs to be created.

The procedure involves first building fricas on some convenient platform to generate cached lisp code. This might take about 1 - 2 hours on a fast machine.  This generated code can than be included in a new source distribution created by running

  ../fricas/src/scripts/mkdist.sh --copy_lisp

The contents of the ./dist directory can be moved to the ./src directory of the spkg. The use of cached lisp allows fricas to be built in about 12 minutes or less on a the target machine.

Note: There may be a problem with clisp support of FFI in Sage. A patch to allow fricas to build without FFI is attached (not yet tested with fricas-1.0.4).

Issue created by migration from https://trac.sagemath.org/ticket/4461





---

archive/issue_comments_032869.json:
```json
{
    "body": "Attachment [disable-ffi.patch](tarball://root/attachments/some-uuid/ticket4461/disable-ffi.patch) by bpage created at 2008-11-07 16:46:29\n\ndisable FFI in fricas",
    "created_at": "2008-11-07T16:46:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4461#issuecomment-32869",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

Attachment [disable-ffi.patch](tarball://root/attachments/some-uuid/ticket4461/disable-ffi.patch) by bpage created at 2008-11-07 16:46:29

disable FFI in fricas



---

archive/issue_comments_032870.json:
```json
{
    "body": "I am not sure what to do about the Aldor interface, i.e. we discourage spkgs downloading content dynamically during build. For now I would prefer that the default for now does not attempt to build the Aldor interface and only does so if some env variable (like SAGE_FRICAS_ALDOR is equal to 'yes').\n\nCheers,\n\nMichael",
    "created_at": "2008-11-07T17:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4461#issuecomment-32870",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am not sure what to do about the Aldor interface, i.e. we discourage spkgs downloading content dynamically during build. For now I would prefer that the default for now does not attempt to build the Aldor interface and only does so if some env variable (like SAGE_FRICAS_ALDOR is equal to 'yes').

Cheers,

Michael



---

archive/issue_comments_032871.json:
```json
{
    "body": "No package for fricas release 1.0.4 was ever completed. Meanwhile there is a new version of FriCAS available.\n\nAn experimental package for fricas release 1.0.5 is available here:\n\n[http://sage.math.washington.edu/home/page/packages/fricas-1.0.5.spkg](http://sage.math.washington.edu/home/page/packages/fricas-1.0.5.spkg)\n\nSo far I have only tested this package with sage-3.1.2 on sage.math using the following commands:\n\n```\n  $ wget http://sage.math.washington.edu/home/page/packages/fricas-1.0.5.spkg\n  $ .../sage -f fricas-1.0.5.spkg\n```\n\nFor example with this version you can compute the following integral:\n\n```\nsage: ex1=axiom(2^x/sqrt(1+4^x));ex1\n\n       x\n      2\n  ---------\n   +------+\n   | x\n  \\|4  + 1\nsage: ex1.integrate(x)\n\n         +-----------------+\n         |   x log(2) 2          x log(2)\n    log(\\|(%e        )  + 1  - %e        )\n  - --------------------------------------\n                    log(2)\n\n```\n\n\nHelp testing on other platforms and versions of Sage would be appreciated.",
    "created_at": "2009-01-27T03:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4461#issuecomment-32871",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

No package for fricas release 1.0.4 was ever completed. Meanwhile there is a new version of FriCAS available.

An experimental package for fricas release 1.0.5 is available here:

[http://sage.math.washington.edu/home/page/packages/fricas-1.0.5.spkg](http://sage.math.washington.edu/home/page/packages/fricas-1.0.5.spkg)

So far I have only tested this package with sage-3.1.2 on sage.math using the following commands:

```
  $ wget http://sage.math.washington.edu/home/page/packages/fricas-1.0.5.spkg
  $ .../sage -f fricas-1.0.5.spkg
```

For example with this version you can compute the following integral:

```
sage: ex1=axiom(2^x/sqrt(1+4^x));ex1

       x
      2
  ---------
   +------+
   | x
  \|4  + 1
sage: ex1.integrate(x)

         +-----------------+
         |   x log(2) 2          x log(2)
    log(\|(%e        )  + 1  - %e        )
  - --------------------------------------
                    log(2)

```


Help testing on other platforms and versions of Sage would be appreciated.



---

archive/issue_comments_032872.json:
```json
{
    "body": "On Mon, 26 Jan 2009 21:56:44 -0800 William Stein wrote:\n\nIt fails the following tests (have you posted a patch to trac to update this)?\n\nBy the way, when using this, I repeatedly felt like I wished the\ncommand in Sage were \"fricas\" instead of \"axiom\" and the file to test\nwere \"fricas.py\" instead of \"axiom.py\".\n\n```\nwstein@sage:~/sage/devel/sage/sage/interfaces$ sage -t -optional axiom.py\nsage -t -optional \"devel/sage-main/sage/interfaces/axiom.py\"\n**********************************************************************\nFile \"/home/wstein/sage/devel/sage-main/sage/interfaces/axiom.py\", line 61:\n    sage: F.type()                              # optional\nExpected:\n    Factored Polynomial Integer\nGot:\n    Factored(Polynomial(Integer))\n**********************************************************************\nFile \"/home/wstein/sage/devel/sage-main/sage/interfaces/axiom.py\", line 80:\n    sage: print axiom.eval('factor(x^5 - y^5)')   # optional\nExpected:\n               4      3    2 2    3     4\n    - (y - x)(y  + x y  + x y  + x y + x )\n    <BLANKLINE>\n    Type: Factored Polynomial Integer\nGot:\n                 4      3    2 2    3     4\n      - (y - x)(y  + x y  + x y  + x y + x )\n\n\n                                                                 Type:\nFactored(Polynomial(Integer))\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/wstein/sage/devel/sage-main/sage/interfaces/axiom.py\", line 561:\n    sage: axiom(x+2).type()  #optional -- requires Axiom\nExpected:\n    Polynomial Integer\nGot:\n    Polynomial(Integer)\n**********************************************************************\nFile \"/home/wstein/sage/devel/sage-main/sage/interfaces/axiom.py\", line 623:\n    sage: _.type()        #optional\nExpected:\n    Tuple PositiveInteger\nGot:\n    Tuple(PositiveInteger)\n**********************************************************************\n3 items had failures:\n   2 of  21 in __main__.example_0\n   1 of   3 in __main__.example_19\n   1 of   6 in __main__.example_22\n\n```",
    "created_at": "2009-01-27T13:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4461#issuecomment-32872",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

On Mon, 26 Jan 2009 21:56:44 -0800 William Stein wrote:

It fails the following tests (have you posted a patch to trac to update this)?

By the way, when using this, I repeatedly felt like I wished the
command in Sage were "fricas" instead of "axiom" and the file to test
were "fricas.py" instead of "axiom.py".

```
wstein@sage:~/sage/devel/sage/sage/interfaces$ sage -t -optional axiom.py
sage -t -optional "devel/sage-main/sage/interfaces/axiom.py"
**********************************************************************
File "/home/wstein/sage/devel/sage-main/sage/interfaces/axiom.py", line 61:
    sage: F.type()                              # optional
Expected:
    Factored Polynomial Integer
Got:
    Factored(Polynomial(Integer))
**********************************************************************
File "/home/wstein/sage/devel/sage-main/sage/interfaces/axiom.py", line 80:
    sage: print axiom.eval('factor(x^5 - y^5)')   # optional
Expected:
               4      3    2 2    3     4
    - (y - x)(y  + x y  + x y  + x y + x )
    <BLANKLINE>
    Type: Factored Polynomial Integer
Got:
                 4      3    2 2    3     4
      - (y - x)(y  + x y  + x y  + x y + x )


                                                                 Type:
Factored(Polynomial(Integer))
    <BLANKLINE>
**********************************************************************
File "/home/wstein/sage/devel/sage-main/sage/interfaces/axiom.py", line 561:
    sage: axiom(x+2).type()  #optional -- requires Axiom
Expected:
    Polynomial Integer
Got:
    Polynomial(Integer)
**********************************************************************
File "/home/wstein/sage/devel/sage-main/sage/interfaces/axiom.py", line 623:
    sage: _.type()        #optional
Expected:
    Tuple PositiveInteger
Got:
    Tuple(PositiveInteger)
**********************************************************************
3 items had failures:
   2 of  21 in __main__.example_0
   1 of   3 in __main__.example_19
   1 of   6 in __main__.example_22

```



---

archive/issue_comments_032873.json:
```json
{
    "body": "Hi Bill, \n\nI made a patch at #5111 which separates the FriCAS and the Axiom interfaces.  Most of the functionality is still in axiom.py since it is common to both.  Also, the improvements at #4036 are in that patch.\n\nCould you make it so that the spkg does not install an executable named 'axiom'?  Then, we can put that spkg up when that patch goes in.\n\nThanks,\n--Mike",
    "created_at": "2009-02-19T20:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4461#issuecomment-32873",
    "user": "https://github.com/mwhansen"
}
```

Hi Bill, 

I made a patch at #5111 which separates the FriCAS and the Axiom interfaces.  Most of the functionality is still in axiom.py since it is common to both.  Also, the improvements at #4036 are in that patch.

Could you make it so that the spkg does not install an executable named 'axiom'?  Then, we can put that spkg up when that patch goes in.

Thanks,
--Mike



---

archive/issue_comments_032874.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-19T20:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4461#issuecomment-32874",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032875.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2009-02-19T20:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4461#issuecomment-32875",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_comments_032876.json:
```json
{
    "body": "It looks like this is being taken care of at http://groups.google.com/group/fricas-devel/browse_thread/thread/3f6186988dc9683e?hl=en",
    "created_at": "2009-02-19T22:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4461#issuecomment-32876",
    "user": "https://github.com/mwhansen"
}
```

It looks like this is being taken care of at http://groups.google.com/group/fricas-devel/browse_thread/thread/3f6186988dc9683e?hl=en



---

archive/issue_comments_032877.json:
```json
{
    "body": "Changing component from packages to optional packages.",
    "created_at": "2009-08-12T16:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4461#issuecomment-32877",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing component from packages to optional packages.



---

archive/issue_comments_032878.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2009-08-12T16:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4461#issuecomment-32878",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: wontfix



---

archive/issue_events_010076.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-12T16:48:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4461",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4461#event-10076"
}
```



---

archive/issue_events_010077.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-12T16:48:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4461",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4461#event-10077"
}
```



---

archive/issue_comments_032879.json:
```json
{
    "body": "Closing this as #6517 deals with a more recent version of FriCAS than the current ticket.",
    "created_at": "2009-08-12T16:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4461#issuecomment-32879",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Closing this as #6517 deals with a more recent version of FriCAS than the current ticket.
