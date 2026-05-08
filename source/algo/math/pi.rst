:math:`\pi` の計算
=====================

円周率 :math:`\pi` は，

.. math::

    \pi = \frac{C}{d}

として定義される．ここで :math:`C` は円周の長さ，:math:`d` は円の直径である．その具体的な値は，

.. math::

    \pi = 3.1415926535\; 8979323846\; 2643383279\; 5028841971\; 6939937510\;\ldots

と無限に続く数として知られている．

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

を用いて，ビエトの公式

.. math::

    \frac{2}{\pi} = \prod_{j=0}^\infty\cos\frac{\pi}{4\cdot 2^j}
    = \sqrt{\frac{1}{2}}\sqrt{\frac{1}{2}+\frac{1}{2}\sqrt{\frac{1}{2}}}\sqrt{\frac{1}{2}+\frac{1}{2}\sqrt{\frac{1}{2}+\frac{1}{2}\sqrt{\frac{1}{2}}}}\cdots

を得る．なお， :math:`n=4` とした．
