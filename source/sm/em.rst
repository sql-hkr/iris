古典電磁気学
================

Maxwell方程式
------------------

:math:`c=\epsilon_0=\mu_0=1` と単位を選ぶと，Maxwell方程式は以下のように表される．

.. math::

    \nabla\cdot\mathbf{E} = \rho

    \nabla\cdot\mathbf{B} = 0

    \nabla\times\mathbf{E} + \frac{\partial \mathbf{B}}{\partial t} = 0

    \nabla\times\mathbf{B} - \frac{\partial \mathbf{E}}{\partial t} = \mathbf{J}

ここで， :math:`\mathbf{E}` は電場， :math:`\mathbf{B}` は磁場， :math:`\rho` は電荷密度， :math:`\mathbf{J}` は電流密度である．非斉次な方程式は，連続の方程式の局所的な電荷保存の事実と整合している．

.. math::

    \frac{\partial \rho}{\partial t} + \nabla\cdot\mathbf{J} = 0

また，Lorentz共変な形で書くと，

.. math::

    \partial_\mu F^{\mu\nu} = J^\nu

ここで， :math:`J^\nu` は，4元電流密度であり，

.. math::

    J^\nu = \begin{bmatrix}
    \rho \\
    \mathbf{J}
    \end{bmatrix}

であるものと仮定する．スカラーポテンシャル :math:`\phi` とベクトルポテンシャル :math:`\mathbf{A}` を導入すると，斉次式は，

.. math::

    \mathbf{E} = -\nabla\phi - \frac{\partial \mathbf{A}}{\partial t}

    \mathbf{B} = \nabla\times\mathbf{A}

により自動的に満たされる．ここで， :math:`A^\mu` を4元ポテンシャルといい，

.. math::

    A^\mu = \begin{bmatrix}
    \phi \\
    \mathbf{A}
    \end{bmatrix}

であることを仮定する．Maxwell方程式は，反対称テンソル :math:`F^{\mu\nu}` を用いて書き直せる．

.. math::

    F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu
    = \begin{bmatrix}
    0 & -E_x & -E_y & -E_z \\
    E_x & 0 & -B_z & B_y \\
    E_y & B_z & 0 & -B_x \\
    E_z & -B_y & B_x & 0
    \end{bmatrix}

Maxwell方程式の2つの斉次式は，

.. math::

    \partial_\lambda F_{\mu\nu} + \partial_\mu F_{\nu\lambda} + \partial_\nu F_{\lambda\mu} = 0

残りの非斉次式は，共変な形で，

.. math::

    \partial_\mu F^{\mu\nu} = J^\nu

となる．

電磁場のLagrangian密度
-------------------------

Hamiltonの原理を用いてMaxwell方程式が導かれるようなLagrangian密度 :math:`\mathcal{L}` を求めてみよう． :math:`\mathcal{L}` がLorentz不変であれば，

.. math::

    S = \int d^4x \mathcal{L}

も :math:`d^4x` が不変なのでLorentz不変である．そして， :math:`\delta S=0` の条件から任意の慣性系においても同じ式になる． :math:`\mathcal{L}` は，Lorentz不変な量であって，かつ， :math:`A^\mu` とその微分の関数でなければならない．さらに，Maxwell方程式は線形であることから， :math:`\mathcal{L}` は二次式でなければならない．これらの条件を満たす量は，

.. math::

    \mathcal{L} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu} - J^\mu A_\mu

が見出される．作用は，

.. math::

    S = \int d^4x \left(-\frac{1}{4}F_{\mu\nu}F^{\mu\nu} - J^\mu A_\mu\right) .

その変分をとると，

.. math::

    \delta S = \int d^4x \left(-\frac{1}{2}F_{\mu\nu}\delta F^{\mu\nu} - J^\mu \delta A_\mu\right) =

    = \int d^4x \left[-\frac{1}{2}F_{\mu\nu}(\partial^\mu \delta A^\nu - \partial^\nu \delta A^\mu) - J^\mu \delta A_\mu\right] =

    = \int d^4x \left(-F_{\mu\nu}\partial^\mu \delta A^\nu - J^\mu \delta A_\mu\right)

第1項に対して部分積分をして，場に適当な条件を与え，境界項をゼロにすると，

.. math::

    \delta S = \int d^4x \left(\partial_\mu F^{\mu\nu} - J^\nu\right)\delta A_\nu

を得る．任意の :math:`\delta A_\nu` に対して :math:`\delta S=0` であるためには，

.. math::

    \partial_\mu F^{\mu\nu} = J^\nu

でなければならない．この式はMaxwell方程式の非斉次式と同値である．


