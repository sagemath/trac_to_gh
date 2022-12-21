# Issue 4422: create new optional sympow_data.spkg

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-02 02:35:04

Assignee: mabshoff

CC:  mjo dimpase isuruf

Sympow can use additional data files, but we do not install them. So create an optional spkg that recreates those data since they might be dependent on the big size as well as the endianess of the box. To get various optional doctests to pass run 

```
sympow -new_data 2
sympow -new_data 1d0
sympow -new_data 1d1
sympow -new_data 1d2
```

from $SAGE_LOCAL. There might be other useful sets of data to create. We should ping Mark Watkins about the issue.

Cheers,

Michael


---

Comment by mderickx created at 2017-09-13 12:27:55

Changing type from defect to enhancement.


---

Comment by mkoeppe created at 2020-06-19 18:16:00

Setting spkg proposals that have not seen recent activity to "sage-wishlist".


---

Comment by mkoeppe created at 2020-06-19 18:16:00

Changing status from new to needs_info.


---

Comment by mjo created at 2020-06-26 22:49:48

I think this might be obsolete. When we upgrade sympow, the new version will install some architecture-independent data files by default, and generate the others as needed (caching them in `$HOME/.sympow`). The following is what I have installed from the Gentoo package, and the new sympow SPKG will be similar:


```
$ equery f sympow
 * Searching for sympow ...
 * Contents of sci-mathematics/sympow-2.023.6:
...
/usr/share/sympow/datafiles
/usr/share/sympow/datafiles/A012M.txt
/usr/share/sympow/datafiles/A012S.txt
/usr/share/sympow/datafiles/A013M.txt
/usr/share/sympow/datafiles/A013S.txt
/usr/share/sympow/datafiles/A014M.txt
/usr/share/sympow/datafiles/A014S.txt
/usr/share/sympow/datafiles/A015M.txt
/usr/share/sympow/datafiles/A015S.txt
/usr/share/sympow/datafiles/A016M.txt
/usr/share/sympow/datafiles/A016S.txt
/usr/share/sympow/datafiles/A017M.txt
/usr/share/sympow/datafiles/A017S.txt
/usr/share/sympow/datafiles/A018M.txt
/usr/share/sympow/datafiles/A018S.txt
/usr/share/sympow/datafiles/A019M.txt
/usr/share/sympow/datafiles/A019S.txt
/usr/share/sympow/datafiles/A01OM.txt
/usr/share/sympow/datafiles/A01OS.txt
/usr/share/sympow/datafiles/M02HM.txt
/usr/share/sympow/datafiles/M02HS.txt
/usr/share/sympow/datafiles/M02LM.txt
/usr/share/sympow/datafiles/M02LS.txt
/usr/share/sympow/datafiles/m01EM.txt
/usr/share/sympow/datafiles/m01ES.txt
/usr/share/sympow/datafiles/m02EM.txt
/usr/share/sympow/datafiles/m02ES.txt
/usr/share/sympow/datafiles/param_data
/usr/share/sympow/standard1.gp
/usr/share/sympow/standard2.gp
/usr/share/sympow/standard3.gp
```


```
$ find ~/.sympow/
/home/mjo/.sympow/
/home/mjo/.sympow/datafiles
/home/mjo/.sympow/datafiles/le64
/home/mjo/.sympow/datafiles/le64/A014M.bin
/home/mjo/.sympow/datafiles/le64/A01OM.bin
/home/mjo/.sympow/datafiles/le64/A015M.bin
/home/mjo/.sympow/datafiles/le64/M02LM.bin
/home/mjo/.sympow/datafiles/le64/M02HM.bin
/home/mjo/.sympow/datafiles/le64/A017M.bin
/home/mjo/.sympow/datafiles/le64/A012M.bin
/home/mjo/.sympow/datafiles/le64/m01EM.bin
/home/mjo/.sympow/datafiles/le64/A016M.bin
/home/mjo/.sympow/datafiles/le64/A013M.bin
/home/mjo/.sympow/datafiles/le64/A018M.bin
/home/mjo/.sympow/datafiles/param_data
```

