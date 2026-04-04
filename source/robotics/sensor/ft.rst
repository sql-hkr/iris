力覚センサ
=============

ロボットにおける力覚の原理はひずみ計測に基づいており，その基礎は弾性論である．多軸力覚センサは，複数のひずみゲージを組み合わせて構成される．起歪体に :math:`N` 枚のひずみゲージが配置され， :math:`i` 番目のひずみゲージの電圧を :math:`v_i` とする．この起歪体に，力 :math:`\mathbf{f}=[f_x, f_y, f_z]^\top \in \mathbb{R}^3` およびモーメント :math:`\mathbf{m}=[m_x, m_y, m_z]^\top \in \mathbb{R}^3` が作用すると，

.. math::

    v_i = \mathbf{k}_i^\top
    \begin{bmatrix}
    \mathbf{f}\\ \mathbf{m}
    \end{bmatrix}, \quad i=1,2,\ldots,N

である．ここで， :math:`\mathbf{k}_i` は，力センサの構造，ひずみゲージの配置箇所によって定まる6次元の定数ベクトルである．より，一般に，

.. math::

    \mathbf{v} \equiv [v_1, v_2, \ldots , v_N]^\top \in \mathbb{R}^N

    K\equiv [\mathbf{k}_1, \mathbf{k}_2, \ldots, \mathbf{k}_N]^\top \in \mathbb{R}^{N\times 6}

とすれば，

.. math::

    \mathbf{v} = K
    \begin{bmatrix}
    \mathbf{f}\\ \mathbf{m}
    \end{bmatrix}

と表される．多軸力覚センシングで重要なことは，行列 :math:`K` の階数が，力・モーメント成分と等しい6となるように，ひずみゲージの配置を工夫することである．センサ信号 :math:`\mathbf{v}` から，擬似逆行列 :math:`K^+ = (K^\top K)^{-1} K^\top` を用いて，力・モーメント成分を推定することができる．

.. math::

    \begin{bmatrix}
    \mathbf{f}\\ \mathbf{m}
    \end{bmatrix}
    =
    K^+ \mathbf{v}
    =
    (K^\top K)^{-1} K^\top \mathbf{v}

