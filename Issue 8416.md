# Issue 8416: long doctest elliptic_curves/ell_modular_symbols.py fails on Solaris 10 (SPARC)

archive/issues_008416.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nApplying all the patches at #8409, Sage 4.3.3 builds and passes all the normal doctests on Solaris 10 (SPARC) using the following hardware:\n\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler)\n\nRunning the long doctests there was one failure:\n\n\n```\nsage -t  -long \"devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py\"\nA mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.\n         [3.0 s]\n```\n\n\nThis needs to be investigated. I've no idea if this is troublesome on any other platform.\n\n\nPS, Using the hardware above, the time taken for the longest test was 1764.9 s.\n\n\n```\nsage -t  -long \"devel/sage/sage/modular/ssmod/ssmod.py\"\n         [1764.9 s]\n```\n\n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/8416\n\n",
    "created_at": "2010-03-02T10:58:15Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "long doctest elliptic_curves/ell_modular_symbols.py fails on Solaris 10 (SPARC)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8416",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: @JohnCremona

Applying all the patches at #8409, Sage 4.3.3 builds and passes all the normal doctests on Solaris 10 (SPARC) using the following hardware:

* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM
* Solaris 10 03/2005 (first release of Solaris 10)
* gcc 4.4.3 (uses Sun linker and assembler)

Running the long doctests there was one failure:


```
sage -t  -long "devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py"
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [3.0 s]
```


This needs to be investigated. I've no idea if this is troublesome on any other platform.


PS, Using the hardware above, the time taken for the longest test was 1764.9 s.


```
sage -t  -long "devel/sage/sage/modular/ssmod/ssmod.py"
         [1764.9 s]
```


Dave 

Issue created by migration from https://trac.sagemath.org/ticket/8416





---

archive/issue_comments_075295.json:
```json
{
    "body": "For reasons unknown, after I rebuilt the Sage library fully \n\n$ ./sage -ba\n\nso the problem went away. I wont request the ticket is closed yet, until it has been tested again, as I can't understand why this should have happened. \n\n\n```\ndrkirkby@redstart:~/fresh/sage-4.3.3$ ./sage -t  -long \"devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py\"\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py\"\n\t [190.8 s]\n\n```\n\n\nDave",
    "created_at": "2010-03-02T14:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8416#issuecomment-75295",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

For reasons unknown, after I rebuilt the Sage library fully 

$ ./sage -ba

so the problem went away. I wont request the ticket is closed yet, until it has been tested again, as I can't understand why this should have happened. 


```
drkirkby@redstart:~/fresh/sage-4.3.3$ ./sage -t  -long "devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py"
sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py"
	 [190.8 s]

```


Dave



---

archive/issue_comments_075296.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-03-02T14:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8416#issuecomment-75296",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_075297.json:
```json
{
    "body": "This can now be closed - it was solved ages ago now.",
    "created_at": "2010-06-05T19:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8416#issuecomment-75297",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This can now be closed - it was solved ages ago now.



---

archive/issue_comments_075298.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T19:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8416#issuecomment-75298",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_020166.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-06-05T19:30:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8416",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8416#event-20166"
}
```
