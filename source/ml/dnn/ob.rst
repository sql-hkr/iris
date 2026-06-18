物体検出
========

YOLO
----

YOLO (You Only Look Once) は，物体検出を単一の回帰問題として定式化し，end-to-end で最適化可能にした高速な検出モデルである．

定式化
~~~~~~

入力画像を :math:`S \times S` のグリッドセルに分割する．各セルについて， :math:`B` 個のバウンディングボックスのパラメータ :math:`(x, y, w, h)` ，その信頼度（confidence score） :math:`q` ，および :math:`N_C` 個の条件付きクラス確率 :math:`p(c) = P(c \mid \text{Obj})` を予測する．出力テンソルのサイズは :math:`S \times S \times (5B + N_C)` である（ :math:`N_C = |\mathcal{C}|` はクラス数）．

正解の信頼度（ターゲット） :math:`q_{ij}` は以下で定義される．

.. math::

    q_{ij} = \mathbb{I}_i^{\text{obj}} \text{IoU}_{\text{pred},ij}^{\text{truth}}

ここで， :math:`\mathbb{I}_i^{\text{obj}}` はセル :math:`i` に物体が存在する場合に1，そうでない場合に0となるインジケータ関数であり， :math:`\text{IoU}_{\text{pred},ij}^{\text{truth}}` は予測ボックスと正解ボックスの重なり比率（IoU）である．

検出時には，各クラスの予測スコア :math:`s_{ij}(c)` を計算し，非最大値抑制（NMS）により重複を除外して最終出力を得る．

.. math::

    s_{ij}(c) = \hat{p}_i(c) \hat{q}_{ij}

YOLOのネットワークは畳み込み層と全結合層で構成される．

損失関数
~~~~~~~~

学習は，予測値と正解値の2乗誤差の和である損失関数 :math:`E` を最小化することで行う．

.. math::

    E = J_{\text{bb}} + J_{\text{conf}} + J_{\text{class}}

各項は以下のように定義される．

.. math::

    J_{\text{bb}} = \lambda_{\text{bb}} \sum_{i=1}^{S^2} \sum_{j=1}^B \mathbb{I}_{ij}^{\text{obj}} \|\mathbf{r}_i - \hat{\mathbf{r}}_{ij}\|^2

    J_{\text{conf}} = \sum_{i=1}^{S^2} \sum_{j=1}^B \mathbb{I}_{ij}^{\text{obj}} \left( \text{IoU}_{\text{pred},ij}^{\text{truth}} - \hat{q}_{ij} \right)^2 + \lambda_{\text{noobj}} \sum_{i=1}^{S^2} \sum_{j=1}^B \mathbb{I}_{ij}^{\text{noobj}} \hat{q}_{ij}^2

    J_{\text{class}} = \sum_{i=1}^{S^2} \mathbb{I}_i^{\text{obj}} \sum_{c \in \mathcal{C}} (p_i(c) - \hat{p}_i(c))^2

ここで， :math:`\hat{}` は予測値を表す．また， :math:`\mathbf{r}_i = (x_i, y_i, \sqrt{w_i}, \sqrt{h_i})^\top` および :math:`\hat{\mathbf{r}}_{ij} = (\hat{x}_{ij}, \hat{y}_{ij}, \sqrt{\hat{w}_{ij}}, \sqrt{\hat{h}_{ij}})^\top` はバウンディングボックスの座標パラメータベクトルである．
:math:`\mathbb{I}_{ij}^{\text{obj}}` はセル :math:`i` の :math:`j` 番目の予測器が物体の検出を担当（正解とのIoUが最大）する場合に1，そうでない場合に0となり， :math:`\mathbb{I}_{ij}^{\text{noobj}}` はその逆を表す．
:math:`\lambda_{\text{bb}}` と :math:`\lambda_{\text{noobj}}` は各項の重要度のバランスを調整するハイパーパラメータである．


物体検出の評価
--------------

バウンディングボックスの一致度 (IoU)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

予測された領域 :math:`\mathcal{R}_p` と正解領域 :math:`\mathcal{R}_g` の一致度は IoU (Intersection over Union) で測定される．

.. math::

    \text{IoU}(\mathcal{R}_p, \mathcal{R}_g) = \frac{|\mathcal{R}_p \cap \mathcal{R}_g|}{|\mathcal{R}_p \cup \mathcal{R}_g|}

通常， :math:`\text{IoU} \ge 0.5` を満たす予測を真陽性 (TP) と判定する．


平均適合率 (AP / mAP)
~~~~~~~~~~~~~~~~~~~~~

モデルの検出性能は，クラスごとの AP (Average Precision) および全クラスの平均である mAP で評価される．

1. TP/FPの判定: 予測結果をスコア :math:`s_{ij}(c)` の降順にソートし，正解領域との :math:`\text{IoU} \ge \text{threshold}` を満たし，かつ未検出の正解に最も近い予測を真陽性 (TP)，それ以外を偽陽性 (FP) と判定する．
2. PR曲線の作成: 上位 :math:`k` 個の予測結果における精度 :math:`P(k)` と再現率 :math:`R(k)` を計算し，PR曲線を描く．

   .. math::

       P(k) = \frac{TP(k)}{TP(k) + FP(k)}, \quad R(k) = \frac{TP(k)}{N_{\text{gt}}}

   （ :math:`N_{\text{gt}}` は正解の総数）

3. APの計算: 精度を単調非増加に補間した :math:`P_{\text{interp}}(r)` を用いて，PR曲線の下側面積を算出する．

   .. math::

       P_{\text{interp}}(r) = \max_{\tilde{r} \ge r} P(\tilde{r}), \quad \text{AP} = \int_{0}^{1} P_{\text{interp}}(r) dr

4. mAPの算出: 全クラス数 :math:`K` に対する AP の平均値を求める．

   .. math::

       \text{mAP} = \frac{1}{K} \sum_{k=1}^K \text{AP}_k
