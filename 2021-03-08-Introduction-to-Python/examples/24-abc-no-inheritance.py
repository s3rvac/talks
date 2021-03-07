from collections import abc

class Answer:
    def __len__(self):
        return 42

# Passes, even though Answer does not inherit from abc.Sized:
assert isinstance(Answer(), abc.Sized)

# This is achieved by abc.Sized's override of __subclasshook__(), see
# https://docs.python.org/3/library/abc.html#abc.ABCMeta.__subclasshook__
