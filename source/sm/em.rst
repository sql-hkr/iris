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

    J^\nu \equiv \begin{bmatrix}
    \rho \\
    \mathbf{J}
    \end{bmatrix}

であるものと仮定する．スカラーポテンシャル :math:`\phi` とベクトルポテンシャル :math:`\mathbf{A}` を導入すると，斉次式は，

.. math::

    \mathbf{E} = -\nabla\phi - \frac{\partial \mathbf{A}}{\partial t}

    \mathbf{B} = \nabla\times\mathbf{A}

により自動的に満たされる．ここで， :math:`A^\mu` を4元ポテンシャルといい，

.. math::

    A^\mu \equiv \begin{bmatrix}
    \phi \\
    \mathbf{A}
    \end{bmatrix}

であることを仮定する．Maxwell方程式は，反対称テンソル :math:`F^{\mu\nu}` を用いて書き直せる．

.. math::

    F^{\mu\nu} \equiv \partial^\mu A^\nu - \partial^\nu A^\mu
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

も :math:`d^4x` が不変なのでLorentz不変である．そして， :math:`\delta S=0` の条件から任意の慣性系においても同じ式になる． :math:`\mathcal{L}` は，Lorentz不変性およびゲージ不変性を満たし，4元ポテンシャルの一次導関数から構成される最も低次のスカラーとして最も簡単なものとして，

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

ゲージ変換
--------------

4元ポテンシャル :math:`A^\mu = (\phi, \mathbf{A})` は一意ではない．ポテンシャルに対して以下の変換を施しても，同じ電磁場テンソル :math:`F^{\mu\nu}` を得る．

.. math::

    A^\mu + \partial^\mu \chi
    = \begin{bmatrix}
    \phi + \frac{\partial \chi}{\partial t} \\
    \mathbf{A} - \nabla\chi
    \end{bmatrix}

ここで， :math:`\chi` は任意のスカラー場である．この変換に伴う :math:`F^{\mu\nu}` の変化は，

.. math::

    \partial^\mu (A^\nu + \partial^\nu \chi) - \partial^\nu (A^\mu + \partial^\mu \chi)
    = F^{\mu\nu} + \partial^\mu\partial^\nu \chi - \partial^\nu\partial^\mu \chi
    = F^{\mu\nu}

となり，恒等的にゼロになる．このような変換

.. math::

    A^\mu \to A'^\mu = A^\mu + \partial^\mu \chi

をゲージ変換という．ゲージ変換に伴って，作用に加わる余分の項 :math:`\Delta S` は，

.. math::

    \Delta S = -\int d^4x J_\mu \partial^\mu \chi
    = \int d^4x (\partial^\mu J_\mu) \chi

である．なお，部分積分をして，境界項がゼロになることを仮定した．任意の :math:`\chi` に対して :math:`\Delta S` がゼロになるための唯一の条件は，

.. math::

    \partial^\mu J_\mu = \partial_\mu J^\mu = 0 .

すなわち，連続の方程式そのものである．作用がゲージ不変であるためには，電荷保存が要請され，電荷保存によって作用のゲージ不変性が保証される．

Maxwell方程式の解
---------------------

場の方程式 :math:`\partial_\mu F^{\mu\nu} = J^\nu` はポテンシャルを用いて，

.. math::

    \partial_\mu (\partial^\mu A^\nu - \partial^\nu A^\mu) = J^\nu

となる．放射ゲージ :math:`\nabla\cdot\mathbf{A}=0` のもとで， :math:`A^0` に関する方程式は，

.. math::

    (\partial_i\partial^i) A^0 = -\nabla^2 A^0 = J^0

で与えられる．この方程式の解は，

.. math::

    A^0(t, \mathbf{r}) = \frac{1}{4\pi}\int d^3\mathbf{r}' \frac{\rho(t, \mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}

である．ベクトル成分 :math:`A^i` は，次の非斉次波動方程式を満たす．

.. math::

    \frac{\partial^2 \mathbf{A}}{\partial t^2} - \nabla^2 \mathbf{A} = \mathbf{J} - \frac{\partial}{\partial t}\nabla A^0

自由空間では :math:`\mathbf{J}=0, \rho=0,A^0=0` であり，波数ベクトル :math:`\mathbf{k}` と振動数 :math:`\omega_\mathbf{k}=|\mathbf{k}|` の平面波解は，

.. math::

    \mathbf{A}(t,\mathbf{r}) = a\epsilon \cos(\mathbf{k}\cdot\mathbf{r}-\omega_\mathbf{k}t)

が基本解となり得る．ここで， :math:`a` は波の振幅， :math:`\epsilon` は単位ベクトルである．ゲージ条件から， :math:`\mathbf{k}\cdot\epsilon=0` でなければならない．したがって， :math:`\mathbf{k}` を決めると，独立な状態として選べるのは，これに垂直な2方向の偏極 :math:`\epsilon_1(\mathbf{k}), \epsilon_2(\mathbf{k})` を持つ2つの状態だけである．自由空間における一般解は，

.. math::

    \mathbf{A}(t,\mathbf{r}) = \frac{1}{\sqrt{V}}\sum_\mathbf{k}\sum_{\alpha=1,2} \frac{\epsilon_\alpha(\mathbf{k})}{\sqrt{2\omega_\mathbf{k}}} \left(a_{\mathbf{k}\alpha} e^{i(\mathbf{k}\cdot\mathbf{r}-\omega_\mathbf{k}t)} + a_{\mathbf{k}\alpha}^* e^{-i(\mathbf{k}\cdot\mathbf{r}-\omega_\mathbf{k}t)}\right)

と表される．複素数 :math:`a_{\mathbf{k}\alpha}` は，振幅と位相である．平面波は，体積 :math:`V` の空間内で規格化され，周期境界条件を課されている．

相対論的に不変なLorentzゲージ :math:`\partial_\mu A^\mu=0` を選ぶと，方程式は，

.. math::

    \left(\frac{\partial^2}{\partial t^2} - \nabla^2\right) A^\mu = J^\mu

となる．
