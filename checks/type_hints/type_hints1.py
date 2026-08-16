import inspect

annotations = globals().get("__annotations__")
if annotations is None and "__annotate__" in globals():
    # Python 3.14+ stores module annotations in a callable `__annotate__`
    # instead of the `__annotations__` dict. Read them in VALUE format.
    format_value = getattr(getattr(inspect, "Format", None), "VALUE", 1)
    annotations = globals()["__annotate__"](format_value)
annotations = annotations or {}
assert annotations.get("count") is int, "count should be annotated as int"
print("type_hints1 ✓")
