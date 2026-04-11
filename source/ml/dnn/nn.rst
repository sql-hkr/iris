ニューラルネットワーク
==========================

ニューラルネットワークを構成する最小の要素であるユニットは，

.. math::

    u_j = \sum_{i=1}^I w_{ji} x_i + b_j,\quad
    z_j = f(u_j)

    i \in \{1, 2, \ldots, I\},\quad
    j \in \{1, 2, \ldots, J\}

である．ここで， :math:`x_i` は入力， :math:`w_{ji}` は重み， :math:`b_j` はバイアス， :math:`f` は活性化関数である．ベクトル，行列を用いて表すと，

.. math::

    \mathbf{u} = \mathbf{W} \mathbf{x} + \mathbf{b},\quad
    \mathbf{z} = f(\mathbf{u})

となる．ここで，

.. math::

    \mathbf{u} \equiv \begin{bmatrix} u_1 \\ u_2 \\ \vdots \\ u_J \end{bmatrix},\quad
    \mathbf{x} \equiv \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_I \end{bmatrix},\quad
    \mathbf{b} \equiv \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_J \end{bmatrix},\quad
    \mathbf{z} \equiv \begin{bmatrix} z_1 \\ z_2 \\ \vdots \\ z_J \end{bmatrix}

    \mathbf{W} \equiv \begin{bmatrix} w_{11} & w_{12} & \cdots & w_{1I} \\ w_{21} & w_{22} & \cdots & w_{2I} \\ \vdots & \vdots & \ddots & \vdots \\ w_{J1} & w_{J2} & \cdots & w_{JI} \end{bmatrix},\quad
    \mathbf{f}(\mathbf{u}) \equiv \begin{bmatrix} f(u_1) \\ f(u_2) \\ \vdots \\ f(u_J) \end{bmatrix} .

活性化関数は，様々な種類があり，代表的なものには以下がある．最も基本的なものとしてReLU関数，

.. math::

    f(u) = \max(u,0)

があり，歴史的にはsigmoid関数，

.. math::

    f(u) = \frac{1}{1 + e^{-u}}

が用いらてきた．また，tanh関数

.. math::

    f(u) = \tanh(u) \equiv \frac{e^u - e^{-u}}{e^u + e^{-u}}

やleaky ReLU関数などもよく用いられる．

.. math::

    f(u) = \begin{cases} u & (u \geq 0) \\ \alpha u & (u < 0) \end{cases}

なお， :math:`\alpha` は小さな正の定数である．次に，ユニットを多層化した順伝搬型ネットワークを考える．任意の :math:`L` 層のネットワークは，

.. math::

    \mathbf{u}^{(l+1)} = \mathbf{W}^{(l+1)} \mathbf{z}^{(l)} + \mathbf{b}^{(l+1)}

    \mathbf{z}^{(l+1)} = f(\mathbf{u}^{(l+1)})

    l \in \{1, 2, \ldots, L-1\}

である．特に， :math:`l=1` のときは入力層， :math:`l=L-1` のときは出力層，その間の層は隠れ層と呼ばれる．また，ネットワークの最終的な出力は，

.. math::

    \mathbf{y} \equiv \mathbf{z}^{(L)}

と表記する．重みやバイアスはネットワークのパラメータであり，明示的に :math:`\mathbf{y}(\mathbf{x}; \mathbf{w})` のように書くこともある．


