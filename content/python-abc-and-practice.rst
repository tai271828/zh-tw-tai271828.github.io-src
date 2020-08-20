Python 語言與應用 - ABCs 與實例
###############################

:date: 2020-08-20 13:00
:tags: python, cirq, ABCs
:category: python, quantum computing
:slug: python-abc-cirq


你大概不會用到的 ABCs
*********************

經典的 Python 書籍 `Fluent Python` 第十一章中提到：

    ABCs, like descriptors and metaclasses, are tools for building frameworks. Therefore, only a very small minority of Python developers can create ABCs without imposing unreasonable limitations and needless work on fellow programmers.

大意就是說除非是要開發框架 (framework) 否則大概不需要用到抽象基本類別 (abstract base class) (我亂自行翻譯的；不知道中文是什麼。)。這似乎也暗示了如果自己不是框架開發者，卻用了 ABC 相關的技巧，大概就是 over-engineering XD


不管我就是要用用看
******************

關於 Python 中 ABC 的用法，呂大用中文整理過一篇 `abc — 抽象類別 — 你所不知道的 Python 標準函式庫用法 03`_ ，我不能整理得更好了，所以推薦直接收看呂大整理的那篇。這篇文中包括了下面幾個重點：

- 在 Python 實作 ABC 的時空脈落；包括對應的 PEP 與 mailing list 討論。
- 使用語法的方法，包括 ABCMeta 和 register 。


  .. _abc — 抽象類別 — 你所不知道的 Python 標準函式庫用法 03: https://blog.louie.lu/2017/07/28/%E4%BD%A0%E6%89%80%E4%B8%8D%E7%9F%A5%E9%81%93%E7%9A%84-python-%E6%A8%99%E6%BA%96%E5%87%BD%E5%BC%8F%E5%BA%AB%E7%94%A8%E6%B3%95-03-abc/


真實世界中的例子
****************

上面介紹了這個語法本身的實做、特質與應用方式。這裡舉用兩個 Quantum Information 領域裡註明的框架 `Cirq` 為例，來瞧瞧這樣的語法被用在什麼樣的地方。值得注意一點的是，範例的應用場景「都是實做框架本身」，呼應了本文最一開頭從 Fluent Python 一書中提到的觀念：大概只有框架開發者才會用到。

在實際看程式碼前，我們先假定你已經讀過前面「不管我就是要用用看」對於 ABC 的介紹，所以在未來看到 ABC 的使用時，可以解讀程式碼大概有三個對你的暗示：

- 這類東西大概有一些共通的屬性，不可能會不一樣的。少一樣他就不是這個東西。
- 這類東西會被到處使用。
- 有些已經存在的類別可以也被看成這類東西。（換個觀點、視角的意思）


Pauli Gate of Cirq
==================

因為在數學上我們已經知道 `Pauli Matrices`_  又分成 X 、Y 、Z 三種，並且用在 Quantum Computing 的情境下時， X 、Y 、Z 有一些共通的屬性，像是只用在 qubit 的運算。所以在 Cirq 裡面我們可以看到在實做 `Pauli Matrices`_ 的時候，可以看到 `num_qubits` 總是回傳 1；底下甚至可以在 `on` 方法中，亦即「讓這個 Pauli 操作對輸入的 qubit 作用」，看到 `on` 方法會特別去檢查輸入的 qubit 數量：一次就是指操作一個 qubit，輸入過多的話，就表示使用方法有問題囉！


.. _Pauli Matrices: https://en.wikipedia.org/wiki/Pauli_matrices


.. code-block:: python
    :linenos:

    class Pauli(raw_types.Gate, metaclass=abc.ABCMeta):
        """Represents the Pauli gates.

        This is an abstract class with no public subclasses. The only instances
        of private subclasses are the X, Y, or Z Pauli gates defined below.
        """
        _XYZ = None  # type: Tuple[Pauli, Pauli, Pauli]

        @staticmethod
        def by_index(index: int) -> 'Pauli':
            return Pauli._XYZ[index % 3]

        @staticmethod
        def by_relative_index(p: 'Pauli', relative_index: int) -> 'Pauli':
            return Pauli._XYZ[(p._index + relative_index) % 3]

        def __init__(self, index: int, name: str) -> None:
            self._index = index
            self._name = name

        def num_qubits(self):
            return 1

        def _commutes_(self, other: Any,
                       atol: float) -> Union[bool, NotImplementedType, None]:
            if not isinstance(other, Pauli):
                return NotImplemented
            return self is other

        def third(self, second: 'Pauli') -> 'Pauli':
            return Pauli._XYZ[(-self._index - second._index) % 3]

        def relative_index(self, second: 'Pauli') -> int:
            """Relative index of self w.r.t. second in the (X, Y, Z) cycle."""
            return (self._index - second._index + 1) % 3 - 1

        def phased_pauli_product(
                self, other: Union['cirq.Pauli', 'identity.IdentityGate']
        ) -> Tuple[complex, Union['cirq.Pauli', 'identity.IdentityGate']]:
            if self == other:
                return 1, identity.I
            if other is identity.I:
                return 1, self
            return 1j**cast(Pauli, other).relative_index(self), self.third(
                cast(Pauli, other))

        def __gt__(self, other):
            if not isinstance(other, Pauli):
                return NotImplemented
            return (self._index - other._index) % 3 == 1

        def __lt__(self, other):
            if not isinstance(other, Pauli):
                return NotImplemented
            return (other._index - self._index) % 3 == 1

        def on(self, *qubits: 'cirq.Qid') -> 'SingleQubitPauliStringGateOperation':
            """Returns an application of this gate to the given qubits.

            Args:
                *qubits: The collection of qubits to potentially apply the gate to.
            """
            if len(qubits) != 1:
                raise ValueError(
                    'Expected a single qubit, got <{!r}>.'.format(qubits))
            from cirq.ops.pauli_string import SingleQubitPauliStringGateOperation
            return SingleQubitPauliStringGateOperation(self, qubits[0])

        @property
        def _canonical_exponent(self):
            """Overrides EigenGate._canonical_exponent in subclasses."""
            return 1




小結就是真的沒事不要用
**********************

結尾我們用 Python Cookbook 一書中 David Beazley 與 Brian Jones 提到的概念來收尾。

  Although ABCs facilitate type checking, it’s not something that you should overuse in a program. At its heart, Python is a dynamic language that gives you great flexibility. Trying to enforce type constraints everywhere tends to result in code that is more complicated than it needs to be. You should embrace Python’s flexibility.


大意就是要人們不要本末倒置； Python 語言本身的特性就是靈活與彈性，如果沒有特別理由就想要實做嚴格的 type checking ，只會導致過於且不必要的複雜程式碼。所以如果各位的 repository 像是 `PyCon TW 官方網站`_ 一樣一個 ABC 都沒有的話，那實在是太好了呢（？）！！


.. _PyCon TW 官方網站: https://github.com/pycontw/pycon.tw
