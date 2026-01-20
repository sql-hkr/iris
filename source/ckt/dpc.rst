分布定数回路
=============

基本方程式
----------

分布定数回路の基本方程式は，

.. math::

   -\frac{\partial v(x,t)}{\partial x} = L \frac{\partial i(x,t)}{\partial t} + R i(x,t)

   -\frac{\partial i(x,t)}{\partial x} = C \frac{\partial v(x,t)}{\partial t} + G v(x,t)

であり，電圧・電流分布を時間・空間の関数として表現する．信号を正弦波の場合に限ると，電圧および電流は，

.. math::

   v(x,t) = \sqrt{2} \Re\{\dot{V}(x)e^{j\omega t}\}

   i(x,t) = \sqrt{2} \Re\{\dot{I}(x)e^{j\omega t}\}

として，

.. math::

   \frac{d\dot{V}(x)}{dx} = -(R + j\omega L) \dot{I}(x) = -\dot{Z} \dot{I}(x)

   \frac{d\dot{I}(x)}{dx} = -(G + j\omega C) \dot{V}(x) = -\dot{Y} \dot{V}(x)

となる．さらに :math:`x` で微分すると，

.. math::

   \frac{d^2 \dot{V}(x)}{dx^2} = \dot{\gamma}^2 \dot{V}(x) , \frac{d^2 \dot{I}(x)}{dx^2} = \dot{\gamma}^2 \dot{I}(x)

が得られ，これは電信方程式と呼ばれる．ここで， :math:`\dot{\gamma} \equiv \sqrt{\dot{Z}\dot{Y}}` は伝搬定数である．

上式の一般解は，

.. math::

   \dot{V}(x) = \dot{A} e^{-\dot{\gamma} x} + \dot{B} e^{\dot{\gamma} x}

   \dot{I}(x) = \frac{1}{\dot{Z}_0}\left(\dot{A} e^{-\dot{\gamma} x} - \dot{B} e^{\dot{\gamma} x}\right)

となる．ここで， :math:`\dot{Z}_0\equiv\sqrt{\dot{Z}/\dot{Y}}` は特性インピーダンスであり， :math:`\dot{A}` および :math:`\dot{B}` は境界条件によって決まる定数である．

或いは， :math:`e^{\pm\dot{\gamma}x}=\cosh(\dot{\gamma}x) \pm \sinh(\dot{\gamma}x)` を用いて，

.. math::

    \dot{V}(x) = \dot{A}' \cosh(\dot{\gamma} x) + \dot{B}' \sinh(\dot{\gamma} x)

    \dot{I}(x) = \frac{1}{\dot{Z}_0}\left(\dot{A}' \sinh(\dot{\gamma} x) + \dot{B}' \cosh(\dot{\gamma} x)\right)

とも表せる．なお， :math:`\dot{A}'\equiv \dot{A} + \dot{B}` ， :math:`\dot{B}'\equiv \dot{B} - \dot{A}` である．

線路定数
----------

:math:`R,G,C,L` は線路の一次定数， :math:`\dot{\gamma}=\alpha+j\beta,\dot{Z}_0` などは線路の二次定数と呼ばれる．特に， :math:`\alpha` は減衰定数， :math:`\beta` は位相定数であり，

.. math::

    \alpha = \sqrt{\frac{1}{2}\left(\sqrt{(R^2 + \omega^2 L^2)(G^2 + \omega^2 C^2)} + (RG - \omega^2 LC)\right)}

    \beta = \sqrt{\frac{1}{2}\left(\sqrt{(R^2 + \omega^2 L^2)(G^2 + \omega^2 C^2)} - (RG - \omega^2 LC)\right)}.

特性インピーダンスは，

.. math::

    \dot{Z}_0 = \sqrt[4]{\frac{R^2 + \omega^2 L^2}{G^2 + \omega^2 C^2}}.

    \arg(\dot{Z}_0) = \frac{1}{2} \tan^{-1}\left(\frac{\omega L}{R}\right) - \frac{1}{2} \tan^{-1}\left(\frac{\omega C}{G}\right).

参考文献
----------

.. [#f1] 小郷 寛，小亀 英己，石亀 篤司，『基礎からの交流理論』，オーム社，2002年．