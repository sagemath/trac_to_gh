# Issue 7091: sqlachemy test suite fails when building with SAGE_CHECK

Issue created by migration from https://trac.sagemath.org/ticket/7091

Original creator: davidloeffler

Original creation time: 2009-10-01 16:01:30

Assignee: tbd

CC:  drkirkby jsp

Keywords: sqlalchemy

Building 4.1.2.rc0 under 64-bit SuSE Linux with SAGE_CHECK set to "yes", I got the following errors in the sqlalchemy test suite:


```

======================================================================
ERROR: testbasic (sql.testtypes.UnicodeTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/test/sql/testtypes.py", line 327, in testbasic
    plain_varchar=rawdata)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/sql/expression.py", line 1087, in execute
    return e.execute_clauseelement(self, multiparams, params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 1219, in execute_clauseelement
    return connection.execute_clauseelement(elem, multiparams, params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 895, in execute_clauseelement
    return self._execute_compiled(elem.compile(dialect=self.dialect, column_keys=keys, inline=len(params) > 1), distilled_params=params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 907, in _execute_compiled
    self.__execute_raw(context)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 916, in __execute_raw
    self._cursor_execute(context.cursor, context.statement, context.parameters[0], context=context)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 960, in _cursor_execute
    self._handle_dbapi_exception(e, statement, parameters, cursor)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 942, in _handle_dbapi_exception
    raise exceptions.DBAPIError.instance(statement, parameters, e, connection_invalidated=is_disconnect)
ProgrammingError: (ProgrammingError) You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str). It is highly recommended that you instead just switch your application to Unicode strings. u'INSERT INTO unicode_table (unicode_varchar, unicode_text, plain_varchar) VALUES (?, ?, ?)' ['Alors vous imaginez ma surprise, au lever du jour, quand une dr\xc3\xb4le de petit voix m\xe2\x80\x99a r\xc3\xa9veill\xc3\xa9. Elle disait: \xc2\xab S\xe2\x80\x99il vous pla\xc3\xaet\xe2\x80\xa6 dessine-moi un mouton! \xc2\xbb\n', 'Alors vous imaginez ma surprise, au lever du jour, quand une dr\xc3\xb4le de petit voix m\xe2\x80\x99a r\xc3\xa9veill\xc3\xa9. Elle disait: \xc2\xab S\xe2\x80\x99il vous pla\xc3\xaet\xe2\x80\xa6 dessine-moi un mouton! \xc2\xbb\n', 'Alors vous imaginez ma surprise, au lever du jour, quand une dr\xc3\xb4le de petit voix m\xe2\x80\x99a r\xc3\xa9veill\xc3\xa9. Elle disait: \xc2\xab S\xe2\x80\x99il vous pla\xc3\xaet\xe2\x80\xa6 dessine-moi un mouton! \xc2\xbb\n']

======================================================================
ERROR: testengineparam (sql.testtypes.UnicodeTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/test/sql/testtypes.py", line 385, in testengineparam
    plain_varchar=rawdata)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/sql/expression.py", line 1087, in execute
    return e.execute_clauseelement(self, multiparams, params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 1219, in execute_clauseelement
    return connection.execute_clauseelement(elem, multiparams, params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 895, in execute_clauseelement
    return self._execute_compiled(elem.compile(dialect=self.dialect, column_keys=keys, inline=len(params) > 1), distilled_params=params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 907, in _execute_compiled
    self.__execute_raw(context)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 916, in __execute_raw
    self._cursor_execute(context.cursor, context.statement, context.parameters[0], context=context)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 960, in _cursor_execute
    self._handle_dbapi_exception(e, statement, parameters, cursor)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 942, in _handle_dbapi_exception
    raise exceptions.DBAPIError.instance(statement, parameters, e, connection_invalidated=is_disconnect)
ProgrammingError: (ProgrammingError) You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str). It is highly recommended that you instead just switch your application to Unicode strings. u'INSERT INTO unicode_table (unicode_varchar, unicode_text, plain_varchar) VALUES (?, ?, ?)' ['Alors vous imaginez ma surprise, au lever du jour, quand une dr\xc3\xb4le de petit voix m\xe2\x80\x99a r\xc3\xa9veill\xc3\xa9. Elle disait: \xc2\xab S\xe2\x80\x99il vous pla\xc3\xaet\xe2\x80\xa6 dessine-moi un mouton! \xc2\xbb\n', 'Alors vous imaginez ma surprise, au lever du jour, quand une dr\xc3\xb4le de petit voix m\xe2\x80\x99a r\xc3\xa9veill\xc3\xa9. Elle disait: \xc2\xab S\xe2\x80\x99il vous pla\xc3\xaet\xe2\x80\xa6 dessine-moi un mouton! \xc2\xbb\n', 'Alors vous imaginez ma surprise, au lever du jour, quand une dr\xc3\xb4le de petit voix m\xe2\x80\x99a r\xc3\xa9veill\xc3\xa9. Elle disait: \xc2\xab S\xe2\x80\x99il vous pla\xc3\xaet\xe2\x80\xa6 dessine-moi un mouton! \xc2\xbb\n']

======================================================================
ERROR: test_unicode (orm.query.GetTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/test/testlib/testing.py", line 174, in maybe
    return fn(*args, **kw)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/test/orm/query.py", line 155, in test_unicode
    table.insert().execute(id=ustring, data=ustring)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/sql/expression.py", line 1087, in execute
    return e.execute_clauseelement(self, multiparams, params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 1219, in execute_clauseelement
    return connection.execute_clauseelement(elem, multiparams, params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 895, in execute_clauseelement
    return self._execute_compiled(elem.compile(dialect=self.dialect, column_keys=keys, inline=len(params) > 1), distilled_params=params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 907, in _execute_compiled
    self.__execute_raw(context)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 916, in __execute_raw
    self._cursor_execute(context.cursor, context.statement, context.parameters[0], context=context)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 960, in _cursor_execute
    self._handle_dbapi_exception(e, statement, parameters, cursor)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 942, in _handle_dbapi_exception
    raise exceptions.DBAPIError.instance(statement, parameters, e, connection_invalidated=is_disconnect)
ProgrammingError: (ProgrammingError) You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str). It is highly recommended that you instead just switch your application to Unicode strings. u'INSERT INTO unicode_data (id, data) VALUES (?, ?)' ['petit voix m\xe2\x80\x99a', 'petit voix m\xe2\x80\x99a']

======================================================================
ERROR: test_basic (orm.unitofwork.UnicodeTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/test/orm/unitofwork.py", line 168, in test_basic
    Session.commit()
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/scoping.py", line 98, in do
    return getattr(self.registry(), name)(*args, **kwargs)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/session.py", line 554, in commit
    self.transaction.commit()
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/session.py", line 259, in commit
    self._prepare_impl()
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/session.py", line 243, in _prepare_impl
    self.session.flush()
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/session.py", line 786, in flush
    self.uow.flush(self, objects)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/unitofwork.py", line 233, in flush
    flush_context.execute()
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/unitofwork.py", line 445, in execute
    UOWExecutor().execute(self, tasks)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/unitofwork.py", line 930, in execute
    self.execute_save_steps(trans, task)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/unitofwork.py", line 945, in execute_save_steps
    self.save_objects(trans, task)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/unitofwork.py", line 936, in save_objects
    task.mapper._save_obj(task.polymorphic_tosave_objects, trans)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/mapper.py", line 1161, in _save_obj
    c = connection.execute(statement.values(value_params), params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 844, in execute
    return Connection.executors[c](self, object, multiparams, params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 895, in execute_clauseelement
    return self._execute_compiled(elem.compile(dialect=self.dialect, column_keys=keys, inline=len(params) > 1), distilled_params=params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 907, in _execute_compiled
    self.__execute_raw(context)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 916, in __execute_raw
    self._cursor_execute(context.cursor, context.statement, context.parameters[0], context=context)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 960, in _cursor_execute
    self._handle_dbapi_exception(e, statement, parameters, cursor)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 942, in _handle_dbapi_exception
    raise exceptions.DBAPIError.instance(statement, parameters, e, connection_invalidated=is_disconnect)
ProgrammingError: (ProgrammingError) You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str). It is highly recommended that you instead just switch your application to Unicode strings. u'INSERT INTO uni_test (id, txt) VALUES (?, ?)' [1, '\xc5\xa0\xc4\x90\xc4\x86\xc4\x8c\xc5\xbd']

======================================================================
ERROR: test_relation (orm.unitofwork.UnicodeTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/test/orm/unitofwork.py", line 186, in test_relation
    Session.commit()
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/scoping.py", line 98, in do
    return getattr(self.registry(), name)(*args, **kwargs)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/session.py", line 554, in commit
    self.transaction.commit()
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/session.py", line 259, in commit
    self._prepare_impl()
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/session.py", line 243, in _prepare_impl
    self.session.flush()
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/session.py", line 786, in flush
    self.uow.flush(self, objects)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/unitofwork.py", line 233, in flush
    flush_context.execute()
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/unitofwork.py", line 445, in execute
    UOWExecutor().execute(self, tasks)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/unitofwork.py", line 930, in execute
    self.execute_save_steps(trans, task)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/unitofwork.py", line 945, in execute_save_steps
    self.save_objects(trans, task)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/unitofwork.py", line 936, in save_objects
    task.mapper._save_obj(task.polymorphic_tosave_objects, trans)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/orm/mapper.py", line 1161, in _save_obj
    c = connection.execute(statement.values(value_params), params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 844, in execute
    return Connection.executors[c](self, object, multiparams, params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 895, in execute_clauseelement
    return self._execute_compiled(elem.compile(dialect=self.dialect, column_keys=keys, inline=len(params) > 1), distilled_params=params)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 907, in _execute_compiled
    self.__execute_raw(context)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 916, in __execute_raw
    self._cursor_execute(context.cursor, context.statement, context.parameters[0], context=context)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 960, in _cursor_execute
    self._handle_dbapi_exception(e, statement, parameters, cursor)
  File "/home/david/sage-4.1.2.rc0/spkg/build/sqlalchemy-0.4.6.p1/src/lib/sqlalchemy/engine/base.py", line 942, in _handle_dbapi_exception
    raise exceptions.DBAPIError.instance(statement, parameters, e, connection_invalidated=is_disconnect)
ProgrammingError: (ProgrammingError) You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str). It is highly recommended that you instead just switch your application to Unicode strings. u'INSERT INTO uni_test (txt) VALUES (?)' ['\xc5\xa0\xc4\x90\xc4\x86\xc4\x8c\xc5\xbd']

----------------------------------------------------------------------
Ran 1369 tests in 59.812s

FAILED (errors=5)
There was a problem during the SQLAlchemy unit tests
*************************************
Error testing package ** sqlalchemy-0.4.6.p1 **
*************************************
```



---

Comment by mpatel created at 2010-03-05 02:01:52

I've make a new package with [SQLAlchemy](http://www.sqlalchemy.org/) 0.5.8:

 * http://sage.math.washington.edu/home/mpatel/trac/7091/sqlalchemy-0.5.8.p0.spkg

There's no change in Sage 4.3.4.alpha0's long doctest results on sage.math.

But it seems that 0.5.8 now requires [nose](http://somethingaboutorange.com/mrl/projects/nose/0.11.2/) to run its tests.  I've commented them out in `spkg-check`, but I haven't yet "qfinished" the applied patch, in case I'm wrong or we should just delete `spkg-check`.

Thoughts?


---

Comment by mpatel created at 2010-03-05 02:01:52

Changing status from new to needs_work.


---

Comment by was created at 2010-03-06 23:01:44

This looks good.  

Can you change the spkg maintainer from:

```
## SPKG Maintainers

 * Yi Qiang
```


to you?  

Regarding nose, it's a bummer that they switched so that we can't run their test suite.  Oh well.  I can't think of any better solution though... until nose were to say get added to sage.  

So I say "positive review" (subject to you qfinishing this).   And it's *really* good that we're upgrading to the latest version, since the version of sqlalchemy in sage now is very out of date. 

William


---

Comment by was created at 2010-03-06 23:01:44

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-03-06 23:02:22

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-06 23:52:50

I've made an spkg with the changes William mentioned at http://sage.math.washington.edu/home/mhansen/sqlalchemy-0.5.8.spkg


---

Comment by mhansen created at 2010-03-08 20:50:25

Resolution: fixed
