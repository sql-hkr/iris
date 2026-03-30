動作ティーチング
=================

ダイレクトティーチング
-------------------------

一般に，ロボットマニピュレータのダイナミクスは，

.. math::

    M(\mathbf{q})\ddot{\mathbf{q}} + h(\dot{\mathbf{q}}, \mathbf{q}) + \mathbf{g}(\mathbf{q}) + \boldsymbol{\tau}_f = \boldsymbol{\tau}_{in}+\boldsymbol{\tau}_{ext}

である．ここで， :math:`\boldsymbol{\tau}_{f}, \boldsymbol{\tau}_{in}, \boldsymbol{\tau}_{ext} \in \mathbb{R}^n` はそれぞれ摩擦に対応するトルクベクトル，入力トルクベクトル，外力に対応するトルクベクトルである．なお，粘性減衰係数 :math:`D` ，クーロン摩擦項 :math:`\boldsymbol{\mu} \text{sgn}(\dot{\mathbf{q}})` を用いて，摩擦トルクベクトルは，

.. math::

    \boldsymbol{\tau}_f \equiv D\dot{\mathbf{q}} + \boldsymbol{\mu} \text{sgn}(\dot{\mathbf{q}})

である．サーボコントローサは，位置制御ループ，速度制御ループ，電流制御ループで構成されることが多く，速度・電流ループではPI制御が用いられている．よって， :math:`\boldsymbol{\tau}_{in}` は，

.. math::

    \boldsymbol{\tau}_{in} = K_\tau(K_V(K_P(\mathbf{q}_d-\mathbf{q})-\dot{\mathbf{q}})) + \mathbf{g}(\mathbf{q}) + \tau_f - \tau_{ext} .

ここで， :math:`\mathbf{q}_d` は目標間接角度， :math:`K_P, K_V, K_\tau` はそれぞれ位置制御ゲイン，速度制御ゲイン，電流制御ゲインである．以上より，ロボットマニピュレータのダイナミクスは，

.. math::

    M(\mathbf{q})\ddot{\mathbf{q}} + h(\dot{\mathbf{q}}, \mathbf{q}) = \mathbf{g}(\mathbf{q})) + K_\tau(K_V(K_P(\mathbf{q}_d-\mathbf{q})-\dot{\mathbf{q}}))

となる．Lyapunovの安定性理論と受動性に基づき評価すれば，時間を :math:`t` として， :math:`t\to\infty` で :math:`\mathbf{q}\to\mathbf{q}_d` となることを証明できる．
