annotations = globals().get("__annotations__", {})
assert annotations.get("count") is int, "count should be annotated as int"
print("type_hints1 ✓")
