# Issue 3384: Issues a warning for all unsupported / poorly supported operating systems.

archive/issues_003384.json:
```json
{
    "body": "Assignee: mabshoff\n\nIf one tries to build Sage on Solaris, a warning is issued saying Solaris is not fully supported and difficult to compile on. An option to set the variable SAGE_PORT to a non zero value is then issued, which allows one to attept to build on Solaris. \n\nIn contrast, totally unsupported operating systems (e.g. HP-UX) generate no warning whatsoever. Trying to compile on HP-UX, will just start compiling with no warnings whatsoever. \n\nHence there needs to take 3, depending on operating system\n\n1) No message, if using a fully supported operating system such as Linux or OSX\n2) A warning that building is likely to be difficult if the system is not fully supported, but actively developed (e.g. Solaris)\n3) A clear warning that the operating system is totally unsupported, and therefore is likely to need some effort to port to, on any other operating system. I would suggest not testing for the OS, but leaving this as a default. \n\nie. in pseudo code. \n\nOS=uname\nif ($OS == Linux || $OS == OSX) {\n  dont print any message\n}\nelse if ($OS == Solaris) {\n  issues warning about not fully supported, set SAGE_PORT to non-zero. \n} \nelse {\n  issue warning the platform is not supported at all, and might need a porting effort. Again offer SAGE_PORT option\n} \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3384\n\n",
    "created_at": "2008-06-08T20:32:25Z",
    "labels": [
        "distribution",
        "minor",
        "enhancement"
    ],
    "title": "Issues a warning for all unsupported / poorly supported operating systems.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3384",
    "user": "drkirkby"
}
```
Assignee: mabshoff

If one tries to build Sage on Solaris, a warning is issued saying Solaris is not fully supported and difficult to compile on. An option to set the variable SAGE_PORT to a non zero value is then issued, which allows one to attept to build on Solaris. 

In contrast, totally unsupported operating systems (e.g. HP-UX) generate no warning whatsoever. Trying to compile on HP-UX, will just start compiling with no warnings whatsoever. 

Hence there needs to take 3, depending on operating system

1) No message, if using a fully supported operating system such as Linux or OSX
2) A warning that building is likely to be difficult if the system is not fully supported, but actively developed (e.g. Solaris)
3) A clear warning that the operating system is totally unsupported, and therefore is likely to need some effort to port to, on any other operating system. I would suggest not testing for the OS, but leaving this as a default. 

ie. in pseudo code. 

OS=uname
if ($OS == Linux || $OS == OSX) {
  dont print any message
}
else if ($OS == Solaris) {
  issues warning about not fully supported, set SAGE_PORT to non-zero. 
} 
else {
  issue warning the platform is not supported at all, and might need a porting effort. Again offer SAGE_PORT option
} 



Issue created by migration from https://trac.sagemath.org/ticket/3384





---

archive/issue_comments_023689.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-07T15:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3384#issuecomment-23689",
    "user": "was"
}
```

Resolution: fixed
