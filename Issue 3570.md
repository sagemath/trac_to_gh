# Issue 3570: more import improvements to db.py

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-07-06 20:15:50

Assignee: cwitty




---

Attachment

I checked the source tree and db.Storage is never used anywhere.


---

Comment by was created at 2008-07-06 20:34:10

BEFORE (on osx with caching):

```
teragon-2:misc was$ sage -startuptime|grep db
   pdb: 0.010 (misc)
    cmd: 0.001 (pdb)
    bdb: 0.001 (pdb)
    repr: 0.003 (pdb)
    pprint: 0.003 (pdb)
    traceback: 0.001 (pdb)
         IPython.iplib: 0.025 (pydb)
         IPython.ipmaker: 0.001 (pydb)
       sage.databases.db: 0.132 (sage.databases.conway)
        BTrees.OOBTree: 0.123 (sage.databases.db)
        ZODB.FileStorage.FileStorage: 0.008 (sage.databases.db)
        sage.databases.compressed_storage: 0.000 (sage.databases.db)
      sage.misc.db: 0.000 (modform.all)
       sage.databases.db_class_polynomials: 0.001 (ssmod)
       sage.databases.db_modular_polynomials: 0.000 (ssmod)
       dbapi2: 0.021 (sqlite3)
        datetime: 0.002 (dbapi2)
        _sqlite3: 0.018 (dbapi2)
      db_modular_polynomials: 0.000 (sage.databases.all)
      db_class_polynomials: 0.000 (sage.databases.all)
0.132 sage.databases.db (sage.databases.conway)
0.123 BTrees.OOBTree (sage.databases.db)
```


AFTER:

```
   pdb: 0.010 (misc)
    cmd: 0.001 (pdb)
    bdb: 0.001 (pdb)
    repr: 0.003 (pdb)
    pprint: 0.003 (pdb)
    traceback: 0.001 (pdb)
         codeop: 0.001 (pydb)
         new: 0.001 (pydb)
         sets: 0.004 (pydb)
         IPython.wildcard: 0.000 (pydb)
         IPython.Extensions: 0.003 (pydb)
         IPython.FakeModule: 0.000 (pydb)
         IPython.Logger: 0.000 (pydb)
         IPython.Magic: 0.007 (pydb)
         IPython.Prompts: 0.001 (pydb)
         IPython.background_jobs: 0.001 (pydb)
         IPython.usage: 0.000 (pydb)
         IPython.strdispatch: 0.001 (pydb)
         IPython.history: 0.000 (pydb)
         IPython.prefilter: 0.003 (pydb)
         IPython.shadowns: 0.000 (pydb)
         IPython.ipmaker: 0.001 (pydb)
       sage.databases.db: 0.005 (sage.databases.conway)
        sage.databases.compressed_storage: 0.001 (sage.databases.db)
        logging: 0.004 (sage.databases.db)
      sage.misc.db: 0.000 (modform.all)
       sage.databases.db_class_polynomials: 0.000 (ssmod)
       sage.databases.db_modular_polynomials: 0.000 (ssmod)
       dbapi2: 0.020 (sqlite3)
        datetime: 0.002 (dbapi2)
        _sqlite3: 0.018 (dbapi2)
      db_modular_polynomials: 0.000 (sage.databases.all)
      db_class_polynomials: 0.000 (sage.databases.all)
```


w00t!  Positive review.


---

Comment by mabshoff created at 2008-07-07 02:34:39

Resolution: fixed


---

Comment by mabshoff created at 2008-07-07 02:34:39

Merged in Sage 3.0.4.alpha2
