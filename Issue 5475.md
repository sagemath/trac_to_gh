# Issue 5475: make it so ipython isn't imported when one does "sage -python"

Issue created by migration from https://trac.sagemath.org/ticket/5475

Original creator: was

Original creation time: 2009-03-10 21:39:27

Assignee: was

If one wants to use Sage from a C program, e.g., like this (see below), then it's important that "from sage.all import *" not import Ipython.  The point of this ticket is make the import of IPython lazy -- and only happen if needed.  This will also make "sage -python" and "sage -c" faster, since Ipython startup takes significant time. 


```
/*
sage -sh
gcc -I$SAGE_LOCAL/include/python2.5 $SAGE_LOCAL/lib/python/config/libpython2.5.a embed.c -o embed; ./embed

See http://docs.python.org/extending/embedding.html
*/


#include <Python.h>

int
main(int argc, char *argv[])
{
  Py_Initialize();
  printf("Loading the Sage library...\n");
  PyRun_SimpleString("from sage.all import *");
  printf("Factoring an integer:\n");
  PyRun_SimpleString("print factor(193048120380)");
  printf("Popping up plot of a function:\n");
  PyRun_SimpleString("x=var('x'); show(plot(sin(x)))");
  printf("Popping up plot of a 3-d function:\n");
  PyRun_SimpleString("x,y=var('x,y'); show(plot3d(sin(x*y)-cos(x-y), (x,-4,4),(y,-4,4)))");
  printf("Type 0 then return\n");
  int n;
  scanf("%d",&n);
  printf("Exiting...\n");
  Py_Finalize();
  return 0;
}
```



---

Attachment


---

Comment by mabshoff created at 2009-03-10 22:30:12

This patch causes some doctesting trouble:

```
        sage -t -long devel/sage/sage/misc/randstate.pyx # 3 doctests failed
        sage -t -long devel/sage/sage/interfaces/psage.py # 2 doctests failed
        sage -t -long devel/sage/sage/interfaces/sage0.py # 37 doctests failed
        sage -t -long devel/sage/sage/misc/trace.py # 2 doctests failed
```


Cheers,

Michael


---

Comment by mhansen created at 2013-07-22 14:38:45

Resolution: duplicate


---

Comment by mhansen created at 2013-07-22 14:38:45

This is a duplicate of #3685.
