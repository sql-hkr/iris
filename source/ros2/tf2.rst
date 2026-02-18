Tf2
=============

ロボットシステムでは，複数のセンサ・リンク・アクチュエータが異なる座標系で観測・制御を行うため，時刻整合性を保った座標変換管理が不可欠である．
tf2 は，時間依存剛体変換の動的グラフとして座標系間関係を表現し，分散ノード間で低遅延かつ一貫した変換取得を可能にするミドルウェア層である．

各フレーム間の関係は特殊ユークリッド群

.. math::

    {}^{A}T(t) \in SE(3)

で与えられ，変換行列は

.. math::

    {}^{A}T_{B} =
    \begin{bmatrix}
    R & \mathbf{p} \\
    0 & 1
    \end{bmatrix}

と表される．ここで回転 :math:`R` は :math:`SO(3)` に属し，並進 :math:`\mathbf{p}` は三次元ベクトルである．複数フレームを跨ぐ変換は

.. math::

    {}^{A}T_{C} =
    {}^{A}T_{B}{}^{B}T_{C}

により逐次積として計算されるため，tf2 の lookup 操作はグラフ探索と行列積の連鎖に帰着される．

姿勢は数値安定性の観点から単位クォータニオン

.. math::

    \mathbf{q}=(x,y,z,w), \quad |\mathbf{q}|=1

で保持される．履歴データ間の補間では並進にLerpを，回転にSlerpを適用することで，連続時間における :math:`SE(3)` 曲線が構成される．すなわち

.. math::

    \mathrm{lerp}(\mathbf{p}_0,\mathbf{p}_1; t)
    =
    (1-t)\mathbf{p}_0 + t\mathbf{p}_1

および

.. math::

    \mathrm{slerp}(\mathbf{q}_0,\mathbf{q}_1;t)
    =
    \frac{\sin[(1-t)\Omega]}{\sin\Omega}\mathbf{q}_0
    +
    \frac{\sin(t\Omega)}{\sin\Omega}\mathbf{q}_1

    \cos\Omega = \mathbf{q}_0 \cdot \mathbf{q}_1

が用いられる．これにより高周波センサ融合時にも幾何学的一貫性が維持される．

実装上，変換は時間順リングバッファとして保持され，問い合わせ時には最近傍二点の探索と補間が実行される．通信は DDS 上のトピック配信として実現され，動的変換と静的変換を分離する設計により帯域効率と初期化安定性が確保される．
したがって tf2 は単なる座標ユーティリティではなく，時間依存リー群演算と分散通信を統合した計算インフラとして理解すべきである．

参考までに，補完関数の一部を以下に示す．詳しくは， https://github.com/ros2/geometry2/tree/rolling を参照されたい．

.. code-block:: cpp

    void TimeCache::interpolate(
        const TransformStorage & one, const TransformStorage & two,
        TimePoint time, TransformStorage & output)
    {
        // Check for zero distance case
        if (two.stamp_ == one.stamp_) {
            output = two;
            return;
        }
        // Calculate the ratio
        tf2Scalar ratio = static_cast<double>((time - one.stamp_).count()) /
            static_cast<double>((two.stamp_ - one.stamp_).count());

        // Interpolate translation
        output.translation_.setInterpolate3(one.translation_, two.translation_, ratio);

        // Interpolate rotation
        output.rotation_ = slerp(one.rotation_, two.rotation_, ratio);

        output.stamp_ = one.stamp_;
        output.frame_id_ = one.frame_id_;
        output.child_frame_id_ = one.child_frame_id_;
    }
