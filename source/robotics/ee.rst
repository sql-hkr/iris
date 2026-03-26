End effector 制御
====================

接触の運動学モデル
--------------------

物体座標系 :math:`C-\xi\eta\zeta` ，空間座標系 :math:`O-xyz` を設定する．空間座標系で表した点 :math:`C` の位置ベクトルを :math:`\mathbf{x}_0` ，指 :math:`i` と接触点 :math:`P_i` の位置ベクトルを :math:`\mathbf{x}_i` とした場合，

.. math::

   \dot{\mathbf{x}_i} = \dot{\mathbf{x}}_0 + \mathbf{\omega}\times(\mathbf{x}_i-\mathbf{x}_0)

となる，ここで， :math:`\mathbf{\omega}` は物体の角速度ベクトルである．指が物体と干渉しないためには，

.. math::

    \mathbf{n}_i\cdot\dot{\mathbf{x}}_i \leq 0

でなくれはならない．ここで， :math:`\mathbf{n}_i` は点 :math:`P_i` における物体表面の外向き法線ベクトルである．この関係より，

.. math::

    \mathbf{n}_i^\top\cdot\dot{\mathbf{x}}_0 + \mathbf{n}_i^\top\cdot(\mathbf{\omega}\times(\mathbf{x}_i-\mathbf{x}_0)) \leq 0

となり，スカラー三重積の公式を用いて，

.. math::

    \begin{bmatrix}
    \mathbf{n}_i\\
    (\mathbf{x}_i-\mathbf{x}_0)\times\mathbf{n}_i
    \end{bmatrix}^\top
    \begin{bmatrix}
    \dot{\mathbf{x}}_0 \\
    \mathbf{\omega}
    \end{bmatrix} \leq 0

を得る．ここで，wrench および twist

.. math::

    \mathbf{w}_i \equiv \begin{bmatrix}
    \mathbf{n}_i\\
    (\mathbf{x}_i-\mathbf{x}_0)\times\mathbf{n}_i
    \end{bmatrix}
    ,\quad
    \dot{\mathbf{x}} \equiv \begin{bmatrix}
    \dot{\mathbf{x}}_0 \\
    \mathbf{\omega}
    \end{bmatrix}

を導入し，

.. math::

    \mathbf{w}_i^\top\dot{\mathbf{x}} \leq 0

とも表される．これは，物体の運動に対する制約である．物体に :math:`n` 本の指が接触しているとき，物体の速度と角速度は連立一次方程式

.. math::

    \forall i\in\{1,2,\ldots,n\}, \mathbf{w}_i^\top\dot{\mathbf{x}} \leq 0

を満たす必要がある．よって，物体がとることが可能な速度と角速度の集合は，

.. math::

    V = \{\dot{\mathbf{x}}\in\mathbb{R}^6 \mid \forall i\in\{1,2,\ldots,n\}, \mathbf{w}_i^\top\dot{\mathbf{x}} \leq 0\}

である．この集合 :math:`V` を許容速度集合と呼ぶ．face形式で，

.. math::
    V = \text{face} \{\mathbf{w}_1, \mathbf{w}_2, \ldots, \mathbf{w}_n\}

と書くこともある．