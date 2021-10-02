#!/usr/bin/env python3
from random import randint as randomint, choice as choose
import asyncio as totally_async

try:
	errors=[[ BaseException, SystemExit, KeyboardInterrupt, GeneratorExit, Exception, StopIteration, StopAsyncIteration, ArithmeticError, FloatingPointError, OverflowError, ZeroDivisionError, AssertionError, AttributeError, BufferError, EOFError, ImportError, ModuleNotFoundError, LookupError, IndexError, KeyError, MemoryError, NameError, UnboundLocalError, OSError, BlockingIOError, ChildProcessError, ConnectionError, BrokenPipeError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError, FileExistsError, FileNotFoundError, InterruptedError, IsADirectoryError, NotADirectoryError, PermissionError, ProcessLookupError, TimeoutError, ReferenceError, RuntimeError, NotImplementedError, RecursionError, SyntaxError, IndentationError, TabError, SystemError, TypeError, ValueError, UnicodeError, UnicodeDecodeError, UnicodeEncodeError, UnicodeTranslateError, Warning, DeprecationWarning, PendingDeprecationWarning, RuntimeWarning, SyntaxWarning, UserWarning, FutureWarning, EnvironmentError, ImportWarning, UnicodeWarning, BytesWarning, ResourceWarning, WindowsError ]]
	raise errors[randomint(0,len(errors))]
except Exception as e:
	pass
else:
	"""
	docs
	"""
finally:
	pass # comments

string_prefixes = [Rb'', br"""""", Fr'''''', f"{hex(3)}", U"", b"", rB"", BR"", bR"", fr"", r"", RB"", RF"", R"", FR"", Rf"", u"", rb"", F"", Br"", rf"{oct(4)}", fR"", B"", rF""]

dunders = [__name__, __debug__, __loader__, __doc__, __import__, __build_class__, __package__, __spec__, __builtins__, __annotations__]

a = (a := 100) & a - a ^ a + a << a >> a * a ** a // a % a < a > a <= a >= a | a
a != a != a
a %= 0b1
a &= int(bin(a),2)
a **= pow(0o1,1)
a *= min(a,max(a, 10))
a |= a
a //= 0x1
a >>= a
a <<= a
a ^= hash(a)
a /= float(10e1)
a += round(0.0)
a -= complex(a+0j)
a, = [any((divmod(abs(a),2345678) + tuple([])))]


assert a == a

if a or a:
	a
elif bool(a) and ... ==  Ellipsis or False or True:
	a
elif a is not a:
	a=~a
elif issubclass(a,""):
	a
elif isinstance(a,""):
	a
else:
	a

while True:
	with open('/dev/null','w') as f:
		f.write(str(bytes(bytearray(ascii(ord(chr(a))), 'utf-8')).decode("utf-8").encode("utf-8")))
	break
	continue
else:
	~-1-~1

a = filter(all, map(callable,[breakpoint, license, credits, copyright, exit, help, input, quit]))

a=dict({ k:i for i,k in enumerate((["s" for s in dir(a)+[None]] )[3] )})
a=frozenset(set(a))
a=memoryview(bytes(str(a), 'utf-8'))
a=repr(type(sum(a)))
a = (sorted(zip(locals().items(), globals().items())))[slice(1,4)]

eval(compile("a=3", "<string>", "exec"))
exec("a")
a=format(a,"")



def f_factory():
	global dunders
	f=dunders[1:]
	rand: choose(dunders)
	def f2():
		nonlocal f
		for i in range(len(f)):
			yield id(f[i])
			break
		else:
			yield from f2()
	return f2

a=next(iter(reversed(list((lambda x: x()())(f_factory)))))


class dummy(type):
	pass

class A(object, metaclass=dummy):
	_a=0
	def __init__(self, *args, **kwargs):
		_a=totally_async.run(self.f2())
		super()

	@classmethod
	def fromlist(cls, l: list) -> list:
	  x = cls()
	  x = ','.join(str(s) for s in l)
	  return x

	async def f1(self):
		return 3
		print("async")

	async def f2(self):
		await self.f1()

	async def async_generator(self):
		yield 1

	@property
	def a(self):
		return self._a

	@staticmethod
	def f():
		return "static"

	def __matmul__(a,b):
		a._a *= -b._a
		return a

a=A(*[dict(**{str(k):v for k,v in zip(*[range(2<<-~1)]*2)if k%2})if True else None])
a @= a @ a
setattr(a, "__dict__", {a:a})
b=vars(a)
getattr(a, "b", 0)
hasattr(a, "b")
delattr(a, "__dict__"), 0
_=a.fromlist(['a'])