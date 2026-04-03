移動ロボット
=================

運動学
---------

独立二輪駆動型移動機構は，左右輪の回転速度 :math:`\omega_l, \omega_r` ，車輪半径 :math:`R` ，トレッド :math:`T` より，移動体の並進速度 :math:`v` と回転速度 :math:`\omega` をもとめることを順運動学といい，その関係は，

.. math::
    
    \begin{bmatrix}
    v \\ \omega
    \end{bmatrix}
    =\begin{bmatrix}
    \frac{R}{2} & \frac{R}{2} \\
    \frac{R}{T} & -\frac{R}{T}
    \end{bmatrix} \begin{bmatrix}
    \omega_l \\ \omega_r
    \end{bmatrix}

である，逆運動学は，その逆であり，

.. math::

    \begin{bmatrix}
    \omega_l \\ \omega_r
    \end{bmatrix}
    =\begin{bmatrix}
    \frac{R}{2} & \frac{R}{2} \\
    \frac{R}{T} & -\frac{R}{T}
    \end{bmatrix}^\top \begin{bmatrix}
    v \\ \omega
    \end{bmatrix}


    =\begin{bmatrix}
    \frac{1}{R} & \frac{T}{2R} \\
    \frac{1}{R} & -\frac{T}{2R}
    \end{bmatrix} \begin{bmatrix}
    v \\ \omega
    \end{bmatrix}

である．