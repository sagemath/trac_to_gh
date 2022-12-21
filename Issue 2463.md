# Issue 2463: Linbox static commentator make sage crash on PPC

Issue created by migration from Trac.

Original creator: cpernet

Original creation time: 2008-03-10 22:09:33

Assignee: cpernet

Keywords: commentator static linbox

On Power PC, runing OS X, sage crashes at the start up, throwing a SIGBUS error.


```
Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_PROTECTION_FAILURE at address: 0x057e3090
0x91219bb0 in std::ios_base::ios_base ()
(gdb) bt
#0  0x91219bb0 in std::ios_base::ios_base ()
#1  0x91226114 in std::basic_ios<char, std::char_traits<char> >::basic_ios ()
#2  0x91224490 in std::basic_ofstream<char, std::char_traits<char> >::basic_ofstream ()
#3  0x05ad4220 in LinBox::Commentator::Commentator ()
#4  0x05ad4458 in LinBox::Commentator::Commentator ()
#5  0x0576bfa4 in __static_initialization_and_destruction_0 ()
#6  0x0576c104 in global constructors keyed to _Z5powerI7IntegerlET_S1_T0_ ()
#7  0x8fe1376c in __dyld__ZN16ImageLoaderMachO18doModInitFunctionsERKN11ImageLoader11LinkContextE ()
#8  0x8fe0f180 in __dyld__ZN11ImageLoader23recursiveInitializationERKNS_11LinkContextEj ()
#9  0x8fe0f0d0 in __dyld__ZN11ImageLoader23recursiveInitializationERKNS_11LinkContextEj ()
#10 0x8fe0f2a4 in __dyld__ZN11ImageLoader15runInitializersERKNS_11LinkContextE ()
#11 0x8fe0c12c in __dyld_dlopen ()
#12 0x934d75a8 in dlopen ()
#13 0x000e0cac in _PyImport_GetDynLoadFunc ()
#14 0x000cda5c in _PyImport_LoadDynamicModule ()
#15 0x000cb7a8 in import_submodule ()
#16 0x000cba50 in load_next ()
#17 0x000cc1b8 in import_module_level ()
#18 0x000cc548 in PyImport_ImportModuleLevel ()
#19 0x000a3038 in builtin___import__ ()
#20 0x00009500 in PyObject_CallFunctionObjArgs ()
#21 0x000cc80c in PyImport_Import ()
#22 0x05529804 in __Pyx_ImportType (module_name=0x5541e8c "sage.libs.linbox.linbox", class_name=0x5541ea4 "Linbox_modn_dense", size=28) at sage/matrix/matrix_modn_dense.c:9435
#23 0x0553e5cc in initmatrix_modn_dense () at sage/matrix/matrix_modn_dense.c:8878
```





---

Comment by cpernet created at 2008-03-10 22:28:23

William and I simply removed the static attribute to the instantiation of the null commentator (linbox/util/commentator.h:820), and this fixed the problem.

The new spkg is available at
[http://sage.math.washington.edu/home/pernet/linbox-1.1.5rc2.p3.spkg](http://sage.math.washington.edu/home/pernet/linbox-1.1.5rc2.p3.spkg)


---

Comment by cpernet created at 2008-03-10 23:59:01

Scratch that;
disabling the static make everything brake (eg sage -t modsym/space.py).
I am still working on it.


---

Comment by cpernet created at 2008-03-11 01:31:01

[http://sage.math.washington.edu/home/pernet/linbox-1.1.5rc2.p4.spkg](http://sage.math.washington.edu/home/pernet/linbox-1.1.5rc2.p4.spkg) fixes it.
Or more simply, the patch against linbox-1.1.5rc2.p2:
[http://sage.math.washington.edu/home/pernet/commentatorG5.patch](http://sage.math.washington.edu/home/pernet/commentatorG5.patch)


---

Comment by mabshoff created at 2008-03-11 02:41:53

Resolution: fixed


---

Comment by mabshoff created at 2008-03-11 02:41:53

Merged in Sage 2.10.3.rc5
