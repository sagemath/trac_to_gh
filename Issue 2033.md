# Issue 2033: dsage -- startall is broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-02 10:22:40

Assignee: yi

On OS X (my laptop) this frequently happens, where I get the traceback
after a pause.  I've also seen this on Linux machines, but not on sage.math. 


```
teragon:sage-2.10.1.rc4 was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.1.rc4, Release Date: 2008-01-31                  |
| Type notebook() for the GUI, and license() for information.        |
sage: dsage.start_all()
Spawned dsage_server.py -d /Users/was/.sage/dsage/db/dsage.db -p 8081 -l 0 -f /Users/was/.sage/dsage/server.log -c /Users/was/.sage/dsage/pubcert.pem -k /Users/was/.sage/dsage/cacert.pem --jobfailures 3 --statsfile=/Users/was/.sage/dsage/dsage.xml --ssl --noblock (pid = 13314)

Spawned dsage_worker.py -s localhost -p 8081 -u was -w 2 --poll 1.0 -l 0 -f /Users/was/.sage/dsage/worker.log --privkey=/Users/was/.sage/dsage/dsage_key --pubkey=/Users/was/.sage/dsage/dsage_key.pub --priority=20  --ssl --noblock (pid = 13317)

---------------------------------------------------------------------------
<class 'sage.dsage.errors.exceptions.NotConnectedException'>Traceback (most recent call last)

/Users/was/build/sage-2.10.1.rc4/<ipython console> in <module>()

/Users/was/build/sage-2.10.1.rc4/local/lib/python2.5/site-packages/IPython/Prompts.py in __call__(self, arg)
    521 
    522             # and now call a possibly user-defined print mechanism
--> 523             manipulated_val = self.display(arg)
    524             
    525             # user display hooks can change the variable to be stored in

/Users/was/build/sage-2.10.1.rc4/local/lib/python2.5/site-packages/IPython/Prompts.py in _display(self, arg)
    545         """
    546 
--> 547         return self.shell.hooks.result_display(arg)
    548 
    549     # Assign the default display method:

/Users/was/build/sage-2.10.1.rc4/local/lib/python2.5/site-packages/IPython/hooks.py in __call__(self, *args, **kw)
    132             #print "prio",prio,"cmd",cmd #dbg
    133             try:
--> 134                 ret = cmd(*args, **kw)
    135                 return ret
    136             except ipapi.TryNext, exc:

/Users/was/build/sage-2.10.1.rc4/local/lib/python2.5/site-packages/IPython/hooks.py in result_display(self, arg)
    160     
    161     if self.rc.pprint:
--> 162         out = pformat(arg)
    163         if '\n' in out:
    164             # So that multi-line strings line up with the left column of

/Users/was/build/sage-2.10.1.rc4/local/lib/python2.5/pprint.py in pformat(self, object)
    109     def pformat(self, object):
    110         sio = _StringIO()
--> 111         self._format(object, sio, 0, 0, {}, 0)
    112         return sio.getvalue()
    113 

/Users/was/build/sage-2.10.1.rc4/local/lib/python2.5/pprint.py in _format(self, object, stream, indent, allowance, context, level)
    127             self._readable = False
    128             return
--> 129         rep = self._repr(object, context, level - 1)
    130         typ = _type(object)
    131         sepLines = _len(rep) > (self._width - 1 - indent - allowance)

/Users/was/build/sage-2.10.1.rc4/local/lib/python2.5/pprint.py in _repr(self, object, context, level)
    193     def _repr(self, object, context, level):
    194         repr, readable, recursive = self.format(object, context.copy(),
--> 195                                                 self._depth, level)
    196         if not readable:
    197             self._readable = False

/Users/was/build/sage-2.10.1.rc4/local/lib/python2.5/pprint.py in format(self, object, context, maxlevels, level)
    205         and whether the object represents a recursive construct.
    206         """
--> 207         return _safe_repr(object, context, maxlevels, level)
    208 
    209 

/Users/was/build/sage-2.10.1.rc4/local/lib/python2.5/pprint.py in _safe_repr(object, context, maxlevels, level)
    290         return format % _commajoin(components), readable, recursive
    291 
--> 292     rep = repr(object)
    293     return rep, (rep and not rep.startswith('<')), False
    294 

/Users/was/build/sage-2.10.1.rc4/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py in __repr__(self)
    114 
    115     def __repr__(self):
--> 116         return self.__str__()
    117         
    118     def __str__(self):

/Users/was/build/sage-2.10.1.rc4/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py in __str__(self)
    117         
    118     def __str__(self):
--> 119         self.check_connected()
    120         return self.info_str % (self.server, self.port)
    121 

/Users/was/build/sage-2.10.1.rc4/local/lib/python2.5/site-packages/sage/dsage/interface/dsage_interface.py in check_connected(self)
    352         
    353         if self.remoteobj == None:
--> 354             raise NotConnectedException
    355         if self.remoteobj.broker.disconnected:
    356             raise NotConnectedException

<class 'sage.dsage.errors.exceptions.NotConnectedException'>: Not connected to a remote server.
sage: 
```



---

Comment by yi created at 2008-02-03 23:45:41

Can you please apply this bundle and see if it fixes your startall problem? You need to do

sage: d = dsage.start_all()

Unfortunately I haven't figured out how to make the dsage() object callable yet. There is some funny business going on with defining the __call__ method and using a twisted reactor in a separate thread.

http://sage.math.washington.edu/home/yqiang/dsage-2008-02-03.hg


---

Comment by yi created at 2008-02-03 23:45:41

Changing status from new to assigned.


---

Comment by yi created at 2008-02-27 22:35:33

This issue can be closed when #2322 is closed.


---

Comment by mabshoff created at 2008-03-24 16:58:33

Resolution: fixed


---

Comment by mabshoff created at 2008-03-24 16:58:33

Acaccording to Yi this is fixed, so close this.
