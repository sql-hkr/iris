過渡現象
=============

Laplace変換
-------------

時間波形 :math:`f(t)` のLaplace変換 :math:`F(s)` は，

.. math::
    F(s)=\mathcal{L}[f(t)]\equiv \int_0^\infty f(t)e^{-st}dt

と定義される．この変換は，時間波形から複素周波数波形への変換である． :math:`s` は複素周波数

.. math::

    s=\sigma+j\omega

で与えられる． :math:`\omega` は角周波数， :math:`\sigma` は減衰定数である．逆Laplace変換は，

.. math::
    f(t)=\mathcal{L}^{-1}[F(s)]=\frac{1}{j2\pi}\int_{\sigma-j\infty}^{\sigma+j\infty}F(s)e^{st}ds

の複素積分で与えられる．

上式が成り立つことを確認してみよう．

.. math::
    
    \mathcal{L}^{-1}[\mathcal{L}[f(t)]]
    = \frac{1}{j2\pi}\int_{\sigma-j\infty}^{\sigma+j\infty}\left(\int_0^\infty f(\tau)e^{-s\tau}d\tau\right)e^{st}ds =

    = \int_0^\infty f(\tau)\left(\frac{1}{j2\pi}\int_{\sigma-j\infty}^{\sigma+j\infty}e^{s(t-\tau)}ds\right)d\tau
    = \int_0^\infty f(\tau)\delta(t-\tau)d\tau
    = f(t)

RL直列回路
--------------

KVLより，

.. math::

   L\frac{di}{dt} + Ri = E

Laplace変換を適用すると，

.. math::

   (Ls + R)I(s) = \frac{E}{s}

となる．なお， :math:`i(0)=0` とした． :math:`I(s)` について解くと，

.. math::

   I(s) = \frac{E}{s(Ls + R)} = \frac{E}{R}\left(\frac{1}{s} - \frac{1}{s + \frac{R}{L}}\right)

を得る．逆Laplace変換を適用すると，

.. math::

    i(t) = \mathcal{L}^{-1}[I(s)] = \frac{E}{R}\left(1 - e^{-\frac{R}{L}t}\right) .
