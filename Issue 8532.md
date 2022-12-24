# Issue 8532: Optional package mpi4py-1.1.0 fails to install on Solaris 10 SPARC

archive/issues_008532.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jhpalmieri @fchapoton @dimpase\n\n## Hardware & associated software\n\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler)\n\n == Sage version ==\n* 4.3.4.alpha1\n* Patch #8509 removing the -o option to grep to allow packages to install. \n\n == The problem with the optional package mpi4py-1.1.0  ==\n\nThis might be because MPI fails to install - see #8522. \n\n\n```\nsrc/mpi4py.MPI.c:79127: error: 'MPI_VERSION' undeclared (first use in this function)\nsrc/mpi4py.MPI.c:79139: error: 'MPI_SUBVERSION' undeclared (first use in this function)\nsrc/mpi4py.MPI.c:79151: error: 'MPI_MAX_PROCESSOR_NAME' undeclared (first use in this function)\nsrc/mpi4py.MPI.c:79163: error: 'MPI_MAX_ERROR_STRING' undeclared (first use in this function)\nsrc/mpi4py.MPI.c:79175: error: 'MPI_MAX_PORT_NAME' undeclared (first use in this function)\nsrc/mpi4py.MPI.c:79187: error: 'MPI_MAX_INFO_KEY' undeclared (first use in this function)\nsrc/mpi4py.MPI.c:79199: error: 'MPI_MAX_INFO_VAL' undeclared (first use in this function)\nsrc/mpi4py.MPI.c:79211: error: 'MPI_MAX_OBJECT_NAME' undeclared (first use in this function)\nsrc/mpi4py.MPI.c:79223: error: 'MPI_MAX_DATAREP_STRING' undeclared (first use in this function)\nerror: command 'gcc' failed with exit status 1\n\nreal    0m5.609s\nuser    0m5.111s\nsys     0m0.434s\nsage: An error occurred while installing mpi4py-1.1.0\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8532\n\n",
    "created_at": "2010-03-13T23:24:05Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Optional package mpi4py-1.1.0 fails to install on Solaris 10 SPARC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8532",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  @jhpalmieri @fchapoton @dimpase

## Hardware & associated software

* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM
* Solaris 10 03/2005 (first release of Solaris 10)
* gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
* 4.3.4.alpha1
* Patch #8509 removing the -o option to grep to allow packages to install. 

 == The problem with the optional package mpi4py-1.1.0  ==

This might be because MPI fails to install - see #8522. 


```
src/mpi4py.MPI.c:79127: error: 'MPI_VERSION' undeclared (first use in this function)
src/mpi4py.MPI.c:79139: error: 'MPI_SUBVERSION' undeclared (first use in this function)
src/mpi4py.MPI.c:79151: error: 'MPI_MAX_PROCESSOR_NAME' undeclared (first use in this function)
src/mpi4py.MPI.c:79163: error: 'MPI_MAX_ERROR_STRING' undeclared (first use in this function)
src/mpi4py.MPI.c:79175: error: 'MPI_MAX_PORT_NAME' undeclared (first use in this function)
src/mpi4py.MPI.c:79187: error: 'MPI_MAX_INFO_KEY' undeclared (first use in this function)
src/mpi4py.MPI.c:79199: error: 'MPI_MAX_INFO_VAL' undeclared (first use in this function)
src/mpi4py.MPI.c:79211: error: 'MPI_MAX_OBJECT_NAME' undeclared (first use in this function)
src/mpi4py.MPI.c:79223: error: 'MPI_MAX_DATAREP_STRING' undeclared (first use in this function)
error: command 'gcc' failed with exit status 1

real    0m5.609s
user    0m5.111s
sys     0m0.434s
sage: An error occurred while installing mpi4py-1.1.0
```



Issue created by migration from https://trac.sagemath.org/ticket/8532





---

archive/issue_comments_077107.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-19T18:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8532#issuecomment-77107",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077108.json:
```json
{
    "body": "solaris tickets should be closed as outdated",
    "created_at": "2020-06-19T18:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8532#issuecomment-77108",
    "user": "@mkoeppe"
}
```

solaris tickets should be closed as outdated



---

archive/issue_comments_077109.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-19T18:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8532#issuecomment-77109",
    "user": "@fchapoton"
}
```

Resolution: invalid
