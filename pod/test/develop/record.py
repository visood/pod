"""Test develop Record"""

from pod.record import Record

rxy = Record(x=1, y="two")
assert rxy.get("z") is None
rxyz = rxy.plus(z=3)
assert rxyz.get("z") == 3
assert "z" in rxyz
