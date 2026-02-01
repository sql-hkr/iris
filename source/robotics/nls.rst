状態空間表現
==============

状態方程式
--------------

状態方程式は，現在の状態 :math:`\mathbf{x}(t)\in\mathbb{R}^{n}` と制御入力 :math:`\mathbf{u}(t)\in\mathbb{R}={m}` により，

.. math::

    \dot{\mathbf{x}}(t) = F(\mathbf{x}(t), \mathbf{u}(t))

と定義される．ここで， :math:`F` とは，

.. math::

    F: \mathbb{R}^n\times\mathbb{R}^m \to \mathbb{R}^n

という，一般に非線形な写像である． :math:`\mathbf{x}(t)` とは別にシステムの出力 :math:`\mathbf{y}(t)\in\mathbb{R}^p` を定める場合は，出力方程式

.. math::

    \mathbf{y}(t) = h(\mathbf{x}(t), \mathbf{u}(t))

が付随する．一般に，制御入力，制御出力の数は状態より少なく， :math:`m\leq n, p\leq n` である．

Affine Systems
------------------------

応用上多くの場合は，写像 :math:`F(\mathbf{x},\mathbf{u})` が制御入力について線形であり，

.. math::

    \dot{\mathbf{x}} = f(\mathbf{x}) + G(\mathbf{x})u = f(\mathbf{x}) + \sum_{i=1}^m g_i(\mathbf{x})u_i

で表すことができる．

自律系
-----------

状態方程式の右辺が，

.. math::

    \dot{\mathbf{x}} = f(\mathbf{x})

のように，現在の状態 :math:`\mathbf{x}(t)` のみで決まるシステムを自律系という． 

状態方程式の解
-----------------

状態方程式の解とは，初期条件として :math:`\mathbf{x}_0\in\mathbb{R}^n` ，制御入力として :math:`\mathbf{u}(t), t\in[0,\infty)]` が与えられたとき，区間 :math:`T_I\subseteq \mathbb{R}, 0\in T_I` 上で定義された関数 :math:`\mathbf{x}(t), t\in T_I` で下式を満たすものである．

.. math::

    \dot{\mathbf{x}} = F(\mathbf{x}(t), \mathbf{u}(t))

    \mathbf{x}(0) = \mathbf{x}_0

:math:`T_I\subset \mathbb{R}` のときは局所解， :math:`T_I=\mathbb{R}` ととれるときは大域解という．

