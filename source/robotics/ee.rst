End effector 制御
====================

接触の運動学モデル
--------------------

物体座標系 :math:`C-\xi\eta\zeta` ，空間座標系 :math:`O-xyz` を設定する．空間座標系で表した点 :math:`C` の位置ベクトルを :math:`\mathbf{x}_o` ，指 :math:`i` の接触点 :math:`P_i` の位置ベクトルを :math:`\mathbf{x}_i` とした場合，

.. math::

   \dot{\mathbf{x}_i} = \dot{\mathbf{x}}_o + \mathbf{\omega}\times(\mathbf{x}_i-\mathbf{x}_0)

となる，ここで， :math:`\mathbf{\omega}` は物体の角速度ベクトルである．指が物体と干渉しないためには，

.. math::

    \mathbf{n}_i\cdot\dot{\mathbf{x}}_i \leq 0

でなくれはならない．ここで， :math:`\mathbf{n}_i` は点 :math:`P_i` における物体表面の外向き法線ベクトルである．この関係より，

.. math::

    \mathbf{n}_i^\top\cdot\dot{\mathbf{x}}_o + \mathbf{n}_i^\top\cdot(\mathbf{\omega}\times(\mathbf{x}_i-\mathbf{x}_o)) \leq 0

となり，スカラー三重積の公式を用いて，

.. math::

    \begin{bmatrix}
    \mathbf{n}_i\\
    (\mathbf{x}_i-\mathbf{x}_o)\times\mathbf{n}_i
    \end{bmatrix}^\top
    \begin{bmatrix}
    \dot{\mathbf{x}}_o \\
    \mathbf{\omega}
    \end{bmatrix} \leq 0

を得る．ここで，wrench および twist

.. math::

    \mathbf{w}_i \equiv \begin{bmatrix}
    \mathbf{n}_i\\
    (\mathbf{x}_i-\mathbf{x}_o)\times\mathbf{n}_i
    \end{bmatrix}
    ,\quad
    \dot{\mathbf{x}} \equiv \begin{bmatrix}
    \dot{\mathbf{x}}_o \\
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


接触の静力学モデル
-------------------

指 :math:`i` が物体と点接触しているとき，垂直抗力は，

.. math::

    \mathbf{f}_i = R_i(-\mathbf{n}_i)

である．ここで， :math:`R_i\geq 0` は垂直抗力の大きさ， :math:`n_i` は法線ベクトルである．摩擦がないと仮定すると，

.. math::

    \begin{bmatrix}
    \mathbf{f}_i\\
    (\mathbf{x}_i-\mathbf{x}_o)\times\mathbf{f}_i
    \end{bmatrix}
    =-R_i\mathbf{w}_i

を得る．外力と外モーメントをまとめて :math:`\mathbf{p}` とすると，力とモーメントの釣り合いより，

.. math::

    \mathbf{p}+\sum_{i=1}^n(-R_i\mathbf{w}_i)=\mathbf{0}

となる．釣り合いが保たれる外力と外モーメントの集合は，

.. math::

    P=\left\{ \sum_{i=1}^n R_i\mathbf{w}_i\in\mathbb{R}^6 \mid \forall i\in\{1,2,\ldots,n\}, R_i \geq 0 \right\} .

この集合は :math:`P` を許容力集合と呼ぶ．span形式で，

.. math::

    P=\text{span}\{\mathbf{w}_1,\mathbf{w}_2,\cdots,\mathbf{w}_n\}

と書くこともある．摩擦がある場合は，摩擦係数が一定であるとし，合力の集合は摩擦円錐で与えられる．指 :math:`i` に対する摩擦円錐を :math:`m` 個の稜線をもつ凸多面推で近似すると，稜線に沿うベクトル :math:`\mathbf{d}_{i,j}` を用いて，

.. math::

    \mathbf{f}_i = \sum_{j=1}^m R_{i,j}(-\mathbf{d}_{i,j}),\quad R_{i,j}\geq 0

となる．ここで，

.. math::

    \mathbf{w}_{i,j} \equiv
    \begin{bmatrix}
    \mathbf{d}_{i,j}\\
    (\mathbf{x}_i-\mathbf{o})\times \mathbf{d}_{i,j}
    \end{bmatrix}

とし，許容力集合

.. math::

    P = \text{span} \{ \mathbf{w}_{1,1},\mathbf{w}_{1,2},\cdots,\mathbf{w}_{1,m},
    
    \cdots,\mathbf{w}_{n,1},\mathbf{w}_{n,2},\cdots,\mathbf{w}_{n,m} \}

を得る．face形式とspan形式は互い双対であり，凸多面錐 :math:`C` の双対凸多面体錐を :math:`C^*` で表す．摩擦がない場合は特に，

.. math::

    P=V^*, \quad V=P^*

が成り立つ．
