:math:`\pi` の計算
=====================

円周率 :math:`\pi` は，

.. math::

    \pi = \frac{C}{d}

として定義される．ここで :math:`C` は円周の長さ，:math:`d` は円の直径である．その具体的な値は，

.. math::

    \pi = 3.1415926535\; 8979323846\; 2643383279\; 5028841971\; 6939937510\;\ldots

と無限に続く数であり，正確には超越数である．

Proof.

:math:`\pi` が代数的数であると仮定すると， :math:`i\pi` も代数的数である．すると，Eulerの公式より， :math:`e^{i\pi}=-1` も代数的数である．しかし，Lindemannの定理により，代数的数 :math:`\alpha \neq 0` に対して :math:`e^\alpha` は超越数である．これは矛盾であるため， :math:`\pi` は超越数である． :math:`\square`

多角形近似
-------------

半径1の円に内接する正 :math:`n` 角形の周りの長さを :math:`2\pi_n` とすると，

.. math::

    \pi_n = n \sin\frac{\pi}{n}

となり，

.. math::

    \frac{\pi_n}{n} = \sin\frac{\pi}{n}
    = 2\sin\frac{\pi}{2n}\cos\frac{\pi}{2n}
    = 2\frac{\pi_{2n}}{2n}\cos\frac{\pi}{2n}.

これを再帰的に適用すると，

.. math::

    \pi_n = \lim_{k\rightarrow \infty} 2^kn\sin\frac{\pi}{2^kn}\prod_{j=1}^k\cos\frac{\pi}{2^jn}

    \frac{1}{\pi} = \lim_{k\rightarrow \infty}\frac{1}{\pi_n}\left(\frac{2^kn}{\pi}\sin\frac{\pi}{2^kn}\right)\prod_{j=1}^k\cos\frac{\pi}{2^jn}

となり，

.. math::

    \pi = \frac{n\sin\frac{\pi}{n}}{\prod_{j=1}^\infty\cos\frac{\pi}{2^jn}}

を得る．また，

.. math::

    \cos\frac{\pi}{2k} = \sqrt{\frac{1}{2}+\frac{1}{2}\cos\frac{\pi}{k}}

を用いて，Vièteの公式

.. math::

    \frac{2}{\pi} = \prod_{j=0}^\infty\cos\frac{\pi}{4\cdot 2^j}
    = \sqrt{\frac{1}{2}}\sqrt{\frac{1}{2}+\frac{1}{2}\sqrt{\frac{1}{2}}}\sqrt{\frac{1}{2}+\frac{1}{2}\sqrt{\frac{1}{2}+\frac{1}{2}\sqrt{\frac{1}{2}}}}\cdots

を得る．なお， :math:`n=4` とした．

:math:`\arctan` 系公式
----------------------------

:math:`\arctan x` の値はMaclaurin展開を利用して，

.. math::

    \arctan x = \sum_{k=0}^\infty\frac{(-1)^kx^{2k+1}}{2k+1} = x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots

となる． :math:`x=\frac{1}{n}` のように整数の逆数を代入すると，

.. math::

    \arctan\frac{1}{n} = \sum_{k=0}^\infty\frac{(-1)^k}{(2k+1)n^{2k+1}} = \frac{1}{n} - \frac{1}{3n^3} + \frac{1}{5n^5} - \cdots

になり， :math:`n` が大きいほど収束が速くなる．そのため，一般に :math:`\arctan` 系公式は，

.. math::

    \frac{\pi}{4} = \sum_{k=0}^\infty a_k\arctan\frac{1}{b_k}

の形をしている．ここで :math:`a_k` は整数，:math:`b_k` は正整数である．

有名なものとしてMachinの公式があり，次式を満たす．

.. math::

    \frac{\pi}{4} = 4\arctan\frac{1}{5} - \arctan\frac{1}{239}.

Proof.

.. math::

    4\arctan\frac{1}{5} = 2\left(2\arctan\frac{1}{5}\right)
    = 2\left(\arctan\frac{5}{12}\right)
    = \arctan\frac{120}{119}

であるから，

.. math::

    4\arctan\frac{1}{5} - \frac{\pi}{4} = 4\arctan\frac{1}{5} - 4\arctan\frac{1}{1} =

    = \arctan\frac{120}{119} - \arctan\frac{1}{1}
    = \arctan\frac{1}{239}. \quad \square

特に，2項しかないもの，

.. math::

    \frac{\pi}{4} = k\arctan\frac{1}{n} - l\arctan\frac{1}{m}

は4種類しかない．ただし， :math:`k,l` は自然数， :math:`n,m` は :math:`0` でない整数である．具体的には，

.. math::

    \frac{\pi}{4} = \arctan\frac{1}{2} + \arctan\frac{1}{3}

    = 2\arctan\frac{1}{2} - \arctan\frac{1}{7}

    = 2\arctan\frac{1}{3} + \arctan\frac{1}{7}

    = 4\arctan\frac{1}{5} - \arctan\frac{1}{239}.
