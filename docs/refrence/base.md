# d6engine.resource.base
base class CharacterEntry CharacterComponent

d6Engine base classes used for resources


## default_check
```python
default_check(value:[<class 'int'>, <class 'str'>], entry:object) -> bool
```
default verifier for character attributes

Parameters
----------
value :
data :

Returns
-------
: bool


## CharacterEntry
```python
CharacterEntry(self, label:str, value:[<class 'int'>, <class 'str'>], checks:list=None)
```

base class character entry


...

Attributes
----------
label: str
    string identifying the entry
value: int, str
    data held in the entry
checks: list of func = default_check(value: [int, str], data: dict) -> bool
    list of functions used to verify value before setting
message: str
    last internal object message

Methods
-------
name: str
    (read-only) auto generated with slugify(label)
messages: list of str
    list of all internal object messages

Notes
-----
Check functions must take the new value and the entry object as parameters and only return a bool. The checks
will be run in serial based on the order given until all succeeded or a check fails by returning a False. If
a test fails an exception will be raised, if all pass the new value will be set. Each check and the final status
is stored as a message on the object.

.. def name(value: [int, str], entry: object) -> bool
..    if entry.name != 'something':
..        return False
..    else:
..        return True



