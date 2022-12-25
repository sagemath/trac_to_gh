# Issue 9134: sage-4.4.3.alpha3: os x ppc 10.4 -- error building pynac

archive/issues_009134.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\n\n```\n\nlibtool: link: g++ -dynamiclib  -o .libs/libpynac-0.2.0.dylib  .libs/py_funcs.o .libs/add.o .libs/archive.o .libs/basic.o .libs/clifford.o .libs/color.o .libs/constant.o .libs/ex.o .libs/expair.o .libs/expairseq.o .libs/exprseq.o .libs/fail.o .libs/fderivative.o .libs/function.o .libs/idx.o .libs/indexed.o .libs/inifcns.o .libs/inifcns_trans.o .libs/inifcns_gamma.o .libs/inifcns_nstdsums.o .libs/integral.o .libs/lst.o .libs/matrix.o .libs/mul.o .libs/ncmul.o .libs/normal.o .libs/numeric.o .libs/operators.o .libs/power.o .libs/registrar.o .libs/relational.o .libs/remember.o .libs/pseries.o .libs/print.o .libs/symbol.o .libs/symmetry.o .libs/tensor.o .libs/utils.o .libs/wildcard.o   -L/home/wstein/screen/varro/sage-4.4.3.alpha3/local/lib/python2.6/config -lpython2.6 -ldl    -install_name  /home/wstein/screen/varro/sage-4.4.3.alpha3/local/lib/libpynac-0.2.0.dylib -compatibility_version 1 -current_version 1.0 -Wl,-single_module\nld: Undefined symbols:\n_environ\n/usr/libexec/gcc/powerpc-apple-darwin8/4.0.1/libtool: internal link edit command failed\nmake[4]: *** [libpynac.la] Error 1\nmake[3]: *** [all-recursive] Error 1\nmake[2]: *** [all] Error 2   \nError building pynac.\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9134\n\n",
    "created_at": "2010-06-03T19:57:32Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage-4.4.3.alpha3: os x ppc 10.4 -- error building pynac",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9134",
    "user": "https://github.com/williamstein"
}
```
Assignee: GeorgSWeber


```

libtool: link: g++ -dynamiclib  -o .libs/libpynac-0.2.0.dylib  .libs/py_funcs.o .libs/add.o .libs/archive.o .libs/basic.o .libs/clifford.o .libs/color.o .libs/constant.o .libs/ex.o .libs/expair.o .libs/expairseq.o .libs/exprseq.o .libs/fail.o .libs/fderivative.o .libs/function.o .libs/idx.o .libs/indexed.o .libs/inifcns.o .libs/inifcns_trans.o .libs/inifcns_gamma.o .libs/inifcns_nstdsums.o .libs/integral.o .libs/lst.o .libs/matrix.o .libs/mul.o .libs/ncmul.o .libs/normal.o .libs/numeric.o .libs/operators.o .libs/power.o .libs/registrar.o .libs/relational.o .libs/remember.o .libs/pseries.o .libs/print.o .libs/symbol.o .libs/symmetry.o .libs/tensor.o .libs/utils.o .libs/wildcard.o   -L/home/wstein/screen/varro/sage-4.4.3.alpha3/local/lib/python2.6/config -lpython2.6 -ldl    -install_name  /home/wstein/screen/varro/sage-4.4.3.alpha3/local/lib/libpynac-0.2.0.dylib -compatibility_version 1 -current_version 1.0 -Wl,-single_module
ld: Undefined symbols:
_environ
/usr/libexec/gcc/powerpc-apple-darwin8/4.0.1/libtool: internal link edit command failed
make[4]: *** [libpynac.la] Error 1
make[3]: *** [all-recursive] Error 1
make[2]: *** [all] Error 2   
Error building pynac.

```


Issue created by migration from https://trac.sagemath.org/ticket/9134





---

archive/issue_comments_084994.json:
```json
{
    "body": "Duplicate to #9135 (where a more informative error message is pasted), please close one of the two, preferably this one here.",
    "created_at": "2010-06-04T08:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9134#issuecomment-84994",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Duplicate to #9135 (where a more informative error message is pasted), please close one of the two, preferably this one here.



---

archive/issue_comments_084995.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-06-04T14:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9134#issuecomment-84995",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate
