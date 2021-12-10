import ast
import sys
import unittest
import textwrap

# These come from
# https://github.com/stroxler/callable_syntax_notes/tree/main/typeshed_examples
# and originally from
# https://github.com/pradeep90/annotation_collector/blob/master/data/typeshed-callables.txt
CASES = """
() -> Any
() -> Awaitable[Any]
() -> BaseBrowser
() -> BaseHandler
() -> DOMImplementation
() -> Generator[str, None, None]
() -> Message
() -> None
() -> Optional[_T]
() -> Optional[bytes]
() -> Text
() -> Tuple[Tuple[str, str, str], BaseException, BaseException, str]
() -> _AggregateProtocol
() -> _Dict
() -> _M
() -> _T
() -> _VT
() -> _V
() -> bool
() -> bytes
() -> email.message.Message
() -> float
() -> int
() -> str
() -> streams.StreamReaderProtocol
(AnyStr) -> AnyStr
(AnyStr) -> Any
(Any) -> Any
(Any) -> None
(Any) -> Optional[MutableMapping[_KT, Any]]
(Any) -> _R
(Any) -> _T
(Any) -> _reducedtype
(Any) -> bool
(Any) -> str
(BaseException) -> None
((...) -> Any) -> (...) -> Any
((...) -> Any) -> Command
((...) -> Any) -> Group
((...) -> Generator[Any, Any, Any]) -> (...) -> None
((...) -> _T) -> (...) -> _T
((...) -> _T) -> _lru_cache_wrapper[_T]
(Channel) -> None
(ContentRange) -> Any
(Dict[Any, Any]) -> Any
(Dict[str, Any]) -> Any
(Dict[str, Any]) -> None
(Distribution) -> None
(DocTest) -> Any
(Element) -> Text
(Event[Canvas]) -> Any
(Event[Misc]) -> Any
(Event[Text]) -> Any
(Event[_W]) -> Any
(Future[_T]) -> Any
(HeaderSet) -> Any
(IO[Any]) -> BabylMessage
(IO[Any]) -> MHMessage
(IO[Any]) -> MMDFMessage
(IO[Any]) -> MaildirMessage
(IO[Any]) -> _MessageT
(IO[Any]) -> mboxMessage
(Iterable[Tuple[Text, Text]]) -> _T
(List[Any]) -> _T
(List[TestCase]) -> TestSuite
(List[Tuple[Any, Any]]) -> Any
(List[Tuple[str, Any]]) -> Any
(List[Tuple[str, Any]]) -> _T
(MIMEApplication) -> None
(MIMEAudio) -> None
(MIMEImage) -> None
(Match[AnyStr]) -> AnyStr
(Match[_AnyStr2]) -> _AnyStr2
(Message) -> None
(None) -> Any
(None) -> None
(OSError) -> Any
(Optional[BaseException]) -> None
(Optional[Exception]) -> Any
(Optional[Exception]) -> _T
(Optional[List[Tuple[str, float]]]) -> _T
(Optional[float]) -> struct_time
(Optional[str]) -> Any
(Path) -> bool
(PreparedRequest) -> PreparedRequest
(ReadableBuffer) -> _Hash
(ReferenceType[_T]) -> Any
(RequestCacheControl) -> Any
(Requirement) -> _T
(Response) -> Response
(Sequence[_KT]) -> _KT
(Sequence[_T]) -> _T
(Sequence[int]) -> bytes
(Sized) -> int
(StringVar) -> Any
(TarInfo) -> Optional[TarInfo]
(Tuple[int, str, _Pos, _Pos, str]) -> None
(Type[_T]) -> Type[_T]
(UnicodeError) -> Tuple[Union[str, bytes], int]
(Unpickler) -> None
(UnraisableHookArgs) -> Any
(WWWAuthenticate) -> Any
(_AnyCallable) -> _AnyCallable
(_C) -> Any
(_ExceptHookArgs) -> Any
(_FT) -> _FT
(_F) -> _F
(_KT) -> None
(_KT) -> _VT
(_Reduce[_TypeT]) -> _TypeT
(_ReprFunc) -> _ReprFunc
(_S) -> Any
(_S) -> _T
(_T1) -> SupportsLessThan
(_T1) -> _S
(_T1) -> _T2
(_T) -> Any
(_T) -> None
(_T) -> SupportsLessThan
(_T) -> Union[int, float, str, bytes]
(_T) -> _S
(_T) -> _T
(_T) -> bool
(_T) -> str
(_TypeT) -> Union[str, _Reduce[_TypeT]]
(_VT) -> _VT
(_VT) -> float
(_V) -> _R
(_str) -> float
(_timerFunc) -> _timerFunc
(bool) -> None
(bytes) -> Any
(bytes) -> None
(bytes) -> Optional[bytes]
(bytes) -> _HashType
(bytes) -> bytes
(float) -> None
(float) -> _ScoreCastFuncReturn
(futures.Future[Any]) -> None
(int) -> Any
(int) -> None
(int) -> Tuple[_Text, ...]
(int) -> Tuple[str, ...]
(int) -> int
(object) -> Any
(object) -> str
(str) -> Any
(str) -> None
(str) -> Optional[CodecInfo]
(str) -> _R
(str) -> _T
(str) -> bool
(str) -> float
(str) -> importlib.abc.PathEntryFinder
(str) -> int
(str) -> str
(text_type) -> Markup
(tkinter.Event[Treeview]) -> Any
(tkinter.StringVar) -> Any
(types.MethodType) -> Any
(types.ModuleType) -> IResourceProvider
(AbstractEventLoop, Generator[Any, None, _T]) -> Future[_T]
(Action, Iterable[Tuple[Text, Action]]) -> Any
(Action, Iterable[Tuple[str, Action]]) -> Any
(Any, Any) -> None
(Any, List[_AnyStr]) -> Set[_AnyStr]
(Any, List[str]) -> Set[str]
(AnyStr, AnyStr) -> None
(AnyStr, (AnyStr, AnyStr, AnyStr) -> AnyStr) -> AnyStr
(AnyStr, List[AnyStr]) -> Iterable[AnyStr]
(BaseRepresenter, Any) -> Node
(Channel, Tuple[str, int]) -> None
(Dict[Text, Optional[Text]], None) -> _U
(Dict[Text, Optional[Text]], _T) -> _U
(Iterable[str], str) -> str
(Loader, Node) -> Any
(Optional[str], Tuple[_Marshallable, ...]) -> Union[Fault, Tuple[_Marshallable, ...]]
(Port, bool) -> None
(Status, str) -> None
(StrOrBytesPath, str) -> IO[AnyStr]
(StrOrBytesPath, str) -> IO[Any]
(StrPath, List[str]) -> Iterable[str]
(Text, str) -> IO[AnyStr]
(Text, str) -> IO[Any]
(Union[int, str], str) -> int
(Unmarshaller, str) -> None
(Unpickler, Any) -> None
(_KT, _VT) -> None
(_R, _T) -> Node
(_T, _S) -> _T
(_T, _T) -> Any
(_T, _T) -> _T
(_T, _T) -> int
(_T1, _T2) -> _S
(_next, _token) -> _callback
(bytes, Optional[BinaryIO]) -> Optional[str]
(float, float) -> Any
(int, _JackPositionT) -> None
(int, float) -> Any
(int, int) -> Any
(str, Any) -> None
(str, (Iterable[str], str) -> str) -> None
(str, Sequence[Tuple[str, str]]) -> None
(str, Tuple[Any, ...]) -> Any
(str, Tuple[_Marshallable, ...]) -> _Marshallable
(str, _Model) -> Any
(str, bool) -> None
(str, int) -> Optional[str]
(str, str) -> Any
(str, str) -> None
(str, str) -> int
(str, str) -> str
(type, Attribute) -> Any
(Any, Any, Any) -> Any
(Any, _AnyPath, Any) -> Any
(AnyStr, AnyStr, AnyStr) -> AnyStr
(BaseException, int, BaseException) -> BaseException
(Channel, _Addr, _Addr) -> None
(Context, List[str], str) -> Iterable[Union[str, Tuple[str, str]]]
(Context, Parameter, Optional[str]) -> Any
(Context, Parameter, str) -> Any
(Context, Union[Option, Parameter], Union[bool, int, str]) -> _T
(Context, Union[Option, Parameter], int) -> Any
(Context, Union[Option, Parameter], str) -> Any
(FrameType, str, Any) -> Any
(Marshaller, Any, (str) -> Any) -> None
(Marshaller, str, (str) -> None) -> None
(Optional[str], str, str) -> None
(Port, Port, bool) -> None
(Port, str, str) -> None
(SSLObject, str, SSLContext) -> Union[None, int]
(Type[BaseException], BaseException, TracebackType) -> Any
(_T, AnyStr, List[AnyStr]) -> Any
(_T1, _T2, _T3) -> _S
(int, int, int) -> None
(int, int, int) -> object
(int, str, int) -> None
(socket.socket, bytes, bytes) -> Any
(str, Optional[str], int) -> Any
(str, Union[Dict[str, str]], List[str]) -> Any
(str, str, str) -> Any
(_T1, _T2, _T3, _T4) -> _S
(int, int, _JackPositionT, bool) -> None
(str, AnyStr, str, str) -> str
(str, Optional[str], Optional[str], Optional[str]) -> int
(str, Optional[str], Optional[str], bool) -> Any
(str, Optional[str], str, Optional[str]) -> Any
(str, Union[str, Sequence[str]], str, str) -> None
(Connection, X509, int, int, int) -> bool
(_T1, _T2, _T3, _T4, _T5) -> _S
(str, Optional[str], str, Optional[str], str) -> Any
(str, str, str, Optional[str], bool) -> Any
(...) -> Any
(...) -> Awaitable[Any]
(...) -> Awaitable[_T]
(...) -> BaseHTTPRequestHandler
(...) -> BaseRequestHandler
(...) -> ContextManager[_T]
(...) -> Element
(...) -> Generator[Any, Any, Any]
(...) -> IO[AnyStr]
(...) -> Iterator[_T]
(...) -> LazyLoader
(...) -> LogRecord
(...) -> None
(...) -> Optional[Tuple[float, float]]
(...) -> SSLContext
(...) -> Sequence[Any]
(...) -> Signer
(...) -> Union[str, Element]
(...) -> _Freezable
(...) -> _KT
(...) -> _R
(...) -> _S
(...) -> _T
(...) -> _Text
(...) -> bytes
(...) -> object
(...) -> str
(...) -> types.ModuleType
(**_P) -> AsyncContextManager[_T]
(**_P) -> AsyncIterator[_T]
(**_P) -> Iterator[_T]
(**_P) -> _GeneratorContextManager[_T]
"""


class CallableTypeOperatorBindingTests(unittest.TestCase):

    def test_typeshed_examples(self):
        examples = CASES.strip().split("\n")
        for example in examples:
            # For now this is just a smoke test that everything
            # parses okay. This test will become much more meaningful
            # when we add an unparser.
            ast.parse(example)


if __name__ == "__main__":
    unittest.main()
