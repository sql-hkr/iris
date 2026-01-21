運動学
=============

自由度
-----------------

ロボットの自由度 :math:`F` は，運動の自由度 :math:`D` ，関節数 :math:`J` ，各関節の自由度 :math:`f_i` を用いて，

.. math::

   F = DN - \sum_{i=1}^{J} (D-f_i) = D(N-J) + \sum_{i=1}^{J} f_i.

閉ループがある場合は，閉ループ数 :math:`L` を用いて，

.. math::

   F = \sum_{i=1}^{J} f_i - LD.

姿勢表現
--------------

(ZYZ)オイラー角は，座標系 :math:`\Sigma_A` から座標系 :math:`\Sigma_B` への回転を，

.. math::

    \begin{aligned}
    {}^AR_B
    = \text{Rot}(\mathbf{z}_A,\phi)\text{Rot}(\mathbf{y}_{A'},\theta)\text{Rot}(\mathbf{z}_{A''},\psi)=&\\
    = \begin{bmatrix}
    C_\phi C_\theta C_\psi - S_\phi S_\psi & -C_\phi C_\theta S_\psi - S_\phi C_\psi & C_\phi S_\theta \\
    S_\phi C_\theta C_\psi + C_\phi S_\psi & -S_\phi C_\theta S_\psi + C_\phi C_\psi & S_\phi S_\theta \\
    -S_\theta C_\psi & S_\theta S_\psi & C_\theta
    \end{bmatrix} &
    \end{aligned}

と表現する．ここで， :math:`C_\alpha = \cos\alpha` ， :math:`S_\alpha = \sin\alpha` である．

また，ロール・ピッチ・ヨー角(ZYXオイラー角)は，座標系 :math:`\Sigma_A` から座標系 :math:`\Sigma_B` への回転を，

.. math::

    \begin{aligned}
    {}^AR_B
    = \text{Rot}(\mathbf{z}_A,\phi)\text{Rot}(\mathbf{y}_{A'},\theta)\text{Rot}(\mathbf{x}_{A''},\psi)=&\\
    = \begin{bmatrix}
    C_\phi C_\theta & C_\phi S_\theta S_\psi - S_\phi C_\psi & C_\phi S_\theta C_\psi + S_\phi S_\psi \\
    S_\phi C_\theta & S_\phi S_\theta S_\psi + C_\phi C_\psi & S_\phi S_\theta C_\psi - C_\phi S_\psi \\
    -S_\theta & C_\theta S_\psi & C_\theta C_\psi
    \end{bmatrix} &
    \end{aligned}

と表現する．

四元数は，

.. math::

   \tilde{q} = q_0 + q_1i + q_2j + q_3k

であり，基底 :math:`i,j,k` は，

.. math::

   i^2 = j^2 = k^2 = ijk = -1

の関係を満たす．四元数 :math:`\tilde{q},\tilde{p}` の積は，

.. math::

   \tilde{q}\tilde{p} = (q_0p_0 - q_1p_1 - q_2p_2 - q_3p_3) + (q_0p_1 + q_1p_0 + q_2p_3 - q_3p_2)i \\
   + (q_0p_2 - q_1p_3 + q_2p_0 + q_3p_1)j + (q_0p_3 + q_1p_2 - q_2p_1 + q_3p_0)k.

四元数 :math:`\tilde{q}` の共役は，

.. math::

   \tilde{q}^* = q_0 - q_1i - q_2j - q_3k = q_0 - \mathbf{q} .

絶対値は，

.. math::

   |\tilde{q}| = \sqrt{\tilde{q}\tilde{q}^*} = \sqrt{q_0^2 + q_1^2 + q_2^2 + q_3^2} .

逆数は，

.. math::

   \tilde{q}^{-1} = \frac{\tilde{q}^*}{|\tilde{q}|^2} .

四元数を用いた回転は，原点を通る単位ベクトル :math:`\mathbf{n}` を軸とし，角度 :math:`\theta` だけ回転する場合，

.. math::

   \tilde{q} = \cos\frac{\theta}{2} + \mathbf{n}\sin\frac{\theta}{2}

となり，ある座標系の位置ベクトル :math:`\mathbf{r}` を回転させた位置ベクトル :math:`\mathbf{r}'` に対応する四元数 :math:`\tilde{r}'` は，

.. math::

   \tilde{r}' = \tilde{q}\tilde{r}\tilde{q}^{-1} .

なお， :math:`\tilde{r} = r_x i + r_y j + r_z k` である．

四元数の時間微分は，

.. math::

   \frac{d\tilde{q}}{dt}
   = \lim_{\Delta t \to 0} \frac{\tilde{q}(t + \Delta t) - \tilde{q}(t)}{\Delta t}
   = \lim_{\Delta t \to 0} \frac{\tilde{q}(t)\tilde{q}(\Delta t) - \tilde{q}(t)}{\Delta t}
   = \lim_{\Delta t \to 0} \frac{\Delta \theta}{2\Delta t}\mathbf{n}\tilde{q}
   = \frac{1}{2}\mathbf{\omega}\tilde{q} .

これを行列で表すと，

.. math::

   \frac{d}{dt}
   \begin{bmatrix}
   q_0 \\ q_1 \\ q_2 \\ q_3
   \end{bmatrix}
   = \frac{1}{2}
   \begin{bmatrix}
   0 & -\omega_1 & -\omega_2 & -\omega_3 \\
   \omega_1 & 0 & -\omega_3 & \omega_2 \\
   \omega_2 & \omega_3 & 0 & -\omega_1 \\
   \omega_3 & -\omega_2 & \omega_1 & 0
   \end{bmatrix}
   \begin{bmatrix}
   q_0 \\ q_1 \\ q_2 \\ q_3
   \end{bmatrix} .

同次変換
-----------------

:math:`\Sigma_A` から :math:`\Sigma_B` への同次変換行列 :math:`{}^AT_B` は，

.. math::

   {}^AT_B \equiv
   \begin{bmatrix}
   {}^AR_B & {}^A\mathbf{p}_B \\
   \mathbf{0}^T & 1
   \end{bmatrix}
   =
   \begin{bmatrix}
   I & {}^A\mathbf{p}_B \\
   \mathbf{0}^T & 1
   \end{bmatrix}
   \begin{bmatrix}
   {}^AR_B & \mathbf{0} \\
   \mathbf{0}^T & 1
   \end{bmatrix}

で表される．ここで， :math:`{}^AR_B` は回転行列， :math:`{}^A\mathbf{p}_B` は位置ベクトルである．

:math:`{}^AT_B` の逆行列は，

.. math::

   {}^AT_B^{-1} = {}^BT_A =
   \begin{bmatrix}
   {}^BR_A & {}^B\mathbf{p}_A \\
   \mathbf{0}^T & 1
   \end{bmatrix}
   =
   \begin{bmatrix}
   {}^AR_B^T & -{}^AR_B^T {}^A\mathbf{p}_B \\
   \mathbf{0}^T & 1
   \end{bmatrix}

座標系の速度，加速度
-----------------

原点位置の移動速度は，単純に

.. math::
   
   {}^A\dot{\mathbf{p}}_B = \frac{d}{dt}{}^A\mathbf{p}_B

と時間微分すればよい．姿勢の変化速度（角速度ベクトル）は， :math:`{}^A\mathbf{\phi}_B` をオイラー角とすると，

.. math::

   {}^A\mathbf{\omega}_B = \begin{bmatrix}
   0 & -S_{\phi} & -C_{\phi}S_{\theta} \\
   0 & C_{\phi} & S_{\phi}S_{\theta} \\
   1 & 0 & C_{\theta}
   \end{bmatrix}
   {}^A\dot{\mathbf{\phi}}_B

と表現できる．これは，直交座標系の各軸回りの回転速度の合成となっており，どんな姿勢変化でも表すことができる．しかし，回転軸が変化するとき角速度ベクトルの積分値には意味がない．

次に，移動する座標系上の点について考える．

.. math::

   {}^A\mathrm{r} = {}^A\mathbf{p}_B + {}^AR_B {}^B\mathrm{r}

の時間微分を取ると，

.. math::

   {}^A\dot{\mathrm{r}} = {}^A\dot{\mathbf{p}}_B + \frac{d}{dt}({}^AR_B{}^B\mathrm{r})
   = {}^A\dot{\mathbf{p}}_B + {}^A\dot{R}_B {}^B\mathrm{r} + {}^AR_B {}^B\dot{\mathrm{r}}=

   = {}^A\dot{\mathbf{p}}_B + {}^A\omega_B \times ({}^AR_B {}^B\mathrm{r}) + {}^AR_B {}^B\dot{\mathrm{r}}.

さらに時間微分を取ると，

.. math::

   {}^A\ddot{\mathrm{r}} = {}^A\ddot{\mathbf{p}}_B + {}^A\dot{\omega}_B \times ({}^AR_B {}^B\mathrm{r}) + {}^A\omega_B \times [{}^A\omega_B \times ({}^AR_B {}^B\mathrm{r})] + 2{}^A\omega_B \times ({}^AR_B {}^B\dot{\mathrm{r}}) + {}^AR_B {}^B\ddot{\mathrm{r}}.

角速度は，

.. math::

   {}^A\mathbf{\omega} = {}^AR_B {}^B\mathbf{\omega} + {}^A\omega_B .

さらに時間微分を取ると，

.. math::

   {}^A\dot{\mathbf{\omega}} = {}^A\dot{\omega}_B + {}^AR_B {}^B\dot{\mathbf{\omega}} + {}^A\omega_B \times ({}^AR_B {}^B\mathbf{\omega}) .