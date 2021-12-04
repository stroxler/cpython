import typing

T = typing.TypeVar("T")
S = typing.TypeVar("S")
P = typing.ParamSpec("P")

c = typing.Concatenate[int, T, P]
print(c)
print(c.__args__)
print(c.__parameters__)
print()

c = typing.Callable[..., bool]
print(c)
print(c.__args__)
print(c.__parameters__)
print()

c = typing.Callable[[], S]
print(c)
print(c.__args__)
print(c.__parameters__)
print()


c = typing.Callable[P, bool]
print(c)
print(c.__args__)
print(c.__parameters__)
print()

c = typing.Callable[typing.Concatenate[int, T, P], bool]
print(c)
print(c.__args__)
print(c.__parameters__)
print()
