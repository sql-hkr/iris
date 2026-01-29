四端子回路網
===================

Y, Z, F, G, Hパラメータ
----------------------

アドミタンス行列は，

.. math::

    \begin{bmatrix}
        \dot{I}_1 \\
        \dot{I}_2
    \end{bmatrix}
    =
    \begin{bmatrix}
        \dot{Y}_{11} & \dot{Y}_{12} \\
        \dot{Y}_{21} & \dot{Y}_{22}
    \end{bmatrix}
    \begin{bmatrix}
        \dot{V}_1 \\
        \dot{V}_2
    \end{bmatrix}
    \equiv
    \mathbf{Y}
    \begin{bmatrix}
        \dot{V}_1 \\
        \dot{V}_2
    \end{bmatrix} .


インピーダンス行列は，

.. math::

    \begin{bmatrix}
        \dot{V}_1 \\
        \dot{V}_2
    \end{bmatrix}
    =
    \begin{bmatrix}
        \dot{Z}_{11} & \dot{Z}_{12} \\
        \dot{Z}_{21} & \dot{Z}_{22}
    \end{bmatrix}
    \begin{bmatrix}
        \dot{I}_1 \\
        \dot{I}_2
    \end{bmatrix}
    \equiv
    \mathbf{Z}
    \begin{bmatrix}
        \dot{I}_1 \\
        \dot{I}_2
    \end{bmatrix} .


四端子行列は，

.. math::

    \begin{bmatrix}
        \dot{V}_1 \\
        \dot{I}_1
    \end{bmatrix}
    =
    \begin{bmatrix}
        \dot{A} & \dot{B} \\
        \dot{C} & \dot{D}
    \end{bmatrix}
    \begin{bmatrix}
        \dot{V}_2 \\
        \dot{I}_2
    \end{bmatrix}
    \equiv
    \mathbf{F}
    \begin{bmatrix}
        \dot{V}_2 \\
        \dot{I}_2
    \end{bmatrix} .

線形の受動素子で構成される可逆定理の成り立つ可逆四端子網に対しては，

.. math::

    \dot{A}\dot{D} - \dot{B}\dot{C} = 1

の関係がある．


G行列は，

.. math::

    \begin{bmatrix}
        \dot{I}_1 \\
        \dot{V}_2
    \end{bmatrix}
    =
    \begin{bmatrix}
        \dot{G}_{11} & \dot{G}_{12} \\
        \dot{G}_{21} & \dot{G}_{22}
    \end{bmatrix}
    \begin{bmatrix}
        \dot{V}_1 \\
        \dot{I}_2
    \end{bmatrix}
    \equiv
    \mathbf{G}
    \begin{bmatrix}
        \dot{V}_1 \\
        \dot{I}_2
    \end{bmatrix} .


H行列は，

.. math::

    \begin{bmatrix}
        \dot{V}_1 \\
        \dot{I}_2
    \end{bmatrix}
    =
    \begin{bmatrix}
        \dot{H}_{11} & \dot{H}_{12} \\
        \dot{H}_{21} & \dot{H}_{22}
    \end{bmatrix}
    \begin{bmatrix}
        \dot{I}_1 \\
        \dot{V}_2
    \end{bmatrix}
    \equiv
    \mathbf{H}
    \begin{bmatrix}
        \dot{I}_1 \\
        \dot{V}_2
    \end{bmatrix} .


影像パラメータ
---------------

四端子回路網の 1-1'端子に内部インピーダンス :math:`\dot{Z}_{01}` の電源を接続し，2-2'端子に負荷インピーダンス :math:`\dot{Z}_{02}` を接続した場合，1-1'端子の電圧電流の比が，

.. math::

    \frac{\dot{V}_1}{\dot{I}_1} = \dot{Z}_{01}

であり，2-2'端子に内部インピーダンス :math:`\dot{Z}_{02}` の電源を接続し，1-1'端子に負荷インピーダンス :math:`\dot{Z}_{01}` を接続した場合，2-2'端子の電圧電流の比が，

.. math::

    \frac{\dot{V}_2}{\dot{I}_2} = \dot{Z}_{02}

となるとき，このようなインピーダンス :math:`\dot{Z}_{01}` および :math:`\dot{Z}_{02}` を影像パラメータという．四端子行列の要素を用いると，影像パラメータは，

.. math::

   \dot{Z}_{01} = \sqrt{\frac{\dot{A}\dot{B}}{\dot{C}\dot{D}}} = \sqrt{\dot{Z}_{1f}\dot{Z}_{1s}}
   
   \dot{Z}_{02} = \sqrt{\frac{\dot{B}\dot{D}}{\dot{C}\dot{A}}} = \sqrt{\dot{Z}_{2f}\dot{Z}_{2s}}

となる．ここで， :math:`\dot{Z}_{1f}, \dot{Z}_{1s}` は1-1'端子からみた開放および短絡駆動点インピーダンス， :math:`\dot{Z}_{2f}, \dot{Z}_{2s}` は2-2'端子からみた開放および短絡駆動点インピーダンスである． 

また，1-1'端子と2-2'端子の電圧，電流の比は，

.. math::

    e^{\dot{\theta}_1} = \frac{\dot{V}_1}{\dot{V}_2} = \sqrt{\frac{\dot{A}}{\dot{D}}}\left(\sqrt{\dot{A}\dot{D}} + \sqrt{\dot{B}\dot{C}}\right)

    e^{\dot{\theta}_2} = \frac{\dot{I}_1}{\dot{I}_2} = \sqrt{\frac{\dot{D}}{\dot{A}}}\left(\sqrt{\dot{A}\dot{D}} + \sqrt{\dot{B}\dot{C}}\right)

したがって， :math:`\dot{\theta}` を :math:`\theta_1, \theta_2` の算術平均とすれば，

.. math::

    \dot{\theta} = \frac{\dot{\theta}_1 + \dot{\theta}_2}{2} = \frac{1}{2}\ln \frac{\dot{V}_1\dot{I}_1}{\dot{V}_2\dot{I}_2} = \ln \left(\sqrt{\dot{A}\dot{D}} + \sqrt{\dot{B}\dot{C}}\right)

:math:`\dot{\theta}` は伝達定数であり，影像パラメータの一つである．双曲線関数を用いると便利であり，特に次は重要な関係である．

.. math::

    \tanh \dot{\theta} = \sqrt{\frac{\dot{B}\dot{C}}{\dot{A}\dot{D}}} = \sqrt{\frac{\dot{Z}_{1s}}{\dot{Z}_{1f}}} = \sqrt{\frac{\dot{Z}_{2s}}{\dot{Z}_{2f}}}

四端子行列を影像パラメータを用いて表すと，

.. math::

    \begin{bmatrix}
        \dot{A} & \dot{B} \\
        \dot{C} & \dot{D}
    \end{bmatrix}
    =
    \begin{bmatrix}
        \sqrt{\frac{\dot{Z}_{01}}{\dot{Z}_{02}}}\cosh \dot{\theta} & \sqrt{\dot{Z}_{01}\dot{Z}_{02}}\sinh \dot{\theta} \\
        \sqrt{\frac{1}{\dot{Z}_{01}\dot{Z}_{02}}}\sinh \dot{\theta}& \sqrt{\frac{\dot{Z}_{02}}{\dot{Z}_{01}}}\cosh \dot{\theta}
    \end{bmatrix} .
