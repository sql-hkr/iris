勾配降下法
===============

順伝搬型ネットワークの学習は，訓練データ

.. math::

    \mathcal{D} = \{(\mathbf{x}_n, \mathbf{d}_n)\}_{n=1}^N

に対して定義される損失関数 :math:`\mathcal{E}(\mathbf{w})` の最小化問題として定式化される．この最適化の基本アルゴリズムが勾配降下法である．理想的には，大域的最小点

.. math::

    \mathbf{w}^* = \arg\min_{\mathbf{w}} \mathcal{E}(\mathbf{w})

を求めたいが，非凸損失を持つネットワークでは局所解や鞍点近傍に停留し得る．勾配は

.. math::

    \nabla \mathcal{E} \equiv \frac{\partial \mathcal{E}}{\partial \mathbf{w}}
    = \begin{bmatrix} \frac{\partial \mathcal{E}}{\partial w_1} \\ \frac{\partial \mathcal{E}}{\partial w_2} \\ \vdots \\ \frac{\partial \mathcal{E}}{\partial w_M} \end{bmatrix}

である．勾配降下法の基本更新式は，

.. math::

    \mathbf{w}_{t+1} = \mathbf{w}_t - \epsilon \nabla \mathcal{E}

である．ここで， :math:`\epsilon > 0` は学習率である．

バッチ学習では，訓練データ :math:`\mathcal{D}` 全体に対する損失の平均に基づいて更新する．すなわち，

.. math::

    \mathcal{E}(\mathbf{w}) = \frac{1}{N} \sum_{n=1}^N \mathcal{E}_n(\mathbf{w}).

一方，確率的勾配降下法では，単一サンプルの損失 :math:`\mathcal{E}_n(\mathbf{w})` に基づいて更新する．すなわち，

.. math::

    \mathbf{w}_{t+1} = \mathbf{w}_t - \epsilon \nabla \mathcal{E}_n.

ニューラルネットワークの学習は計算負荷が大きく，並列計算資源の活用が不可欠である．そのため，一般には有限個のサンプルからなる部分集合ごとに重みを更新するミニバッチ学習が用いられる．各ミニバッチを :math:`\mathcal{D}_t` とすると， :math:`t` 回目の損失

.. math::

    \mathcal{E}_t(\mathbf{w}) = \frac{1}{|\mathcal{D}_t|} \sum_{n \in \mathcal{D}_t} \mathcal{E}_n(\mathbf{w})

を計算し，その負勾配方向へパラメータを1回更新する．ミニバッチを :math:`\mathcal{D}_1, \mathcal{D}_2, \ldots` と順に処理し，全てを一巡することをエポック（epoch）と呼ぶ．

ニューラルネットワークでは，二重降下が観測される場合はあるものの，概してバイアス・分散のトレードオフが成り立ち，パラメータ数の増加に伴って過剰適合が生じやすくなる．そこで，学習時にパラメータへ制約を課してモデルの自由度を抑える正則化が有効である．典型例が，次のように損失関数へ二乗ノルム項を付加するL2正則化である．

.. math::

    \mathcal{E}_t(\mathbf{w}) \equiv \frac{1}{|\mathcal{D}_t|} \sum_{n \in \mathcal{D}_t} \mathcal{E}_n(\mathbf{w}) + \frac{\lambda}{2} \|\mathbf{w}\|^2

ここで， :math:`\lambda > 0` は正則化パラメータである．更新式は，

.. math::

    \mathbf{w}_{t+1} = \mathbf{w}_t - \epsilon \left(\frac{1}{|\mathcal{D}_t|} \sum_{n \in \mathcal{D}_t} \nabla \mathcal{E}_n(\mathbf{w}_t) + \lambda \mathbf{w}_t\right)

となり，各重みはその大きさに比例して縮小するため，weight decay とも呼ばれる．なお，バイアス項は大きなオフセットを担う場合があるため，一般に正則化の対象から除外される．また，学習時にユニットを確率的に無効化するドロップアウトも，有効な正則化手法である．

確率的勾配降下法では，更新ごとに異なるミニバッチ損失を用いるため，勾配推定の分散が大きくなりやすい．これを抑制して収束性を改善する方法としてMomentum法がある．ミニバッチ :math:`\mathcal{D}_t` に対する重みの修正量を :math:`\mathbf{v}_t \equiv \mathbf{w}_t - \mathbf{w}_{t-1}` と定義すると，更新式は

.. math::

    \mathbf{w}_{t+1} = \mathbf{w}_t - \epsilon \nabla \mathcal{E}_t + \mu \mathbf{v}_t

となる．

確率的勾配降下法による学習性能は，学習率の設定に敏感である．この依存を緩和するため，成分ごとの実効学習率を適応的に調整する手法が提案されている．代表例はAdaGrad，RMSProp，Adamである．表記を簡略化するために，更新量 :math:`\Delta \mathbf{w}_t \equiv \mathbf{w}_{t+1} - \mathbf{w}_t`，損失関数の勾配 :math:`\mathbf{g}_t \equiv \nabla \mathcal{E}_t`，その :math:`i` 成分を :math:`g_{t,i}` と定義する．AdaGradでは，重みを

.. math::

    \Delta w_{t,i} = -\frac{\epsilon}{\sqrt{\sum_{\tau=1}^t g_{\tau,i}^2 + \varepsilon}} g_{t,i}

と更新する．これは，累積二乗勾配の大きい成分ほど更新を抑制し，逆に小さい成分ほど相対的に大きく更新する成分ごとのスケーリングとみなせる．ただし，更新幅は学習開始時からの :math:`g_{t,i}^2` の総和に反比例するため，反復が進むにつれて単調に減少し，最終的には極めて小さくなる．RMSPropは，この問題を避けるために指数移動平均を用いる．すなわち， :math:`\Braket{g_i^2}_t = \gamma \Braket{g_i^2}_{t-1} + (1-\gamma) g_{t,i}^2` と定義し，更新式は

.. math::

    \Delta w_{t,i} = -\frac{\epsilon}{\sqrt{\Braket{g_i^2}_t + \varepsilon}} g_{t,i}

である．

Adadeltaは，更にパラメータ更新量 :math:`\Delta w_{t,i}` の二乗についても同様に移動平均 :math:`\Braket{\Delta w_i^2}_t = \gamma \Braket{\Delta w_i^2}_{t-1} + (1-\gamma) \Delta w_{t,i}^2` をとり，分子の :math:`\epsilon` を :math:`\Braket{\Delta w_i}_{t-1}` で置き換える．この操作は，パラメータと更新量の物理的次元を整合させるという考えに基づく．これにより， :math:`\epsilon` を明示的に指定する必要がなくなる．なお， :math:`\Braket{\Delta w_i}_t` は得られないので， :math:`t-1` の値で代用している．Adamは，更にMomentumを導入したもので，現在最も広く用いられている手法の1つである．その名はAdaptive Momentに由来する．Adamでは，勾配の1次および2次モーメントを次の移動平均で求める．

.. math::

    m_{t,i} = \beta_1 m_{t-1,i} + (1-\beta_1) g_{t,i}

    v_{t,i} = \beta_2 v_{t-1,i} + (1-\beta_2) g_{t,i}^2

これらの移動平均は初期時刻の影響により推定バイアスを含むため， :math:`\hat{m}_{t,i} = m_{t,i}/(1-\beta_1^t)` および :math:`\hat{v}_{t,i} = v_{t,i}/(1-\beta_2^t)` と偏り補正を施す．更新式は，

.. math::

    \Delta w_{t,i} = -\frac{\epsilon}{\sqrt{\hat{v}_{t,i}} + \varepsilon} \hat{m}_{t,i}

となる．

