# Issue 9134: sage-4.4.3.alpha3: os x ppc 10.4 -- error building pynac

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-03 19:57:32

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



---

Comment by GeorgSWeber created at 2010-06-04 08:27:14

Duplicate to #9135 (where a more informative error message is pasted), please close one of the two, preferably this one here.


---

Comment by was created at 2010-06-04 14:25:50

Resolution: duplicate
