注意機構
===============

注意機構は，ニューラルネットワークを構成する重要な要素の1つであり，深層学習の中核をなす技術として位置付けられている．ここでいう注意とは，複数の要素からなる集合に対して，その時点での関心に応じた重要度を各要素に割り当てることをいう．

ソース :math:`\mathbf{z}_1, \mathbf{z}_2, \ldots, \mathbf{z}_N` に対して，ターゲット :math:`\mathbf{q}` から注意を計算する際には，各要素 :math:`\mathbf{z}_i` と :math:`\mathbf{q}` の関連性 :math:`r(\mathbf{z}_i,\mathbf{q})` をどのように定めるかが重要になる． :math:`r` にはさまざまな関数が用いられるが，最も一般的なのは :math:`\mathbf{z}` と :math:`\mathbf{q}` の内積

.. math::

    r(\mathbf{z},\mathbf{q}) = \frac{\mathbf{z}^\top \mathbf{q}}{\sqrt{D}}

である． :math:`\mathbf{z}` および :math:`\mathbf{q}` の各成分が同程度の分散をもつとき，内積 :math:`\mathbf{z}^\top\mathbf{q}` の分散は次元 :math:`D` に比例して大きくなる．そのままでは softmax への入力が過大になって飽和しやすく，勾配が小さくなりやすいため， :math:`\sqrt{D}` で割ってスケーリングする．この内積に重み :math:`\mathbf{W}\in \mathbb{R}^{D\times D}` を挿入し，学習可能なパラメータを導入した

.. math::
    
    r(\mathbf{z},\mathbf{q}) = \frac{\mathbf{z}^\top \mathbf{W} \mathbf{q}}{\sqrt{D}}

もよく用いられる．また，1層以上の順伝播型ネットワークを用いて

.. math::

    r(\mathbf{z},\mathbf{q}) = \mathrm{MLP}\left(\begin{bmatrix}\mathbf{z}\\\mathbf{q}\end{bmatrix}\right)

とすることもある．これは加法的注意を一般化した書き方とみなせる．一方で， :math:`\mathbf{q}` のみを使って :math:`\mathbf{a}=\text{softmax}(\mathbf{W}\mathbf{q})` のように， :math:`\mathbf{z}` に依存しない形で重みを求める方法もある．

Transformerは，上述の注意機構を中心に構成されたニューラルネットワークである．位置情報を明示的に加えない self-attention は，入力順序の置換に対して同変な写像となる．入力が系列である場合，各要素 :math:`\mathbf{x}_n (n=1,\cdots,N)` をトークンと呼び，中間層では各入力トークンに対応する内部表現ベクトルが更新される．

Transformerの内部では，次のような注意計算が行われる．入力を :math:`[\mathbf{x}_1,\cdots,\mathbf{x}_N], \mathbf{x}_i\in \mathbb{R}^D` ，query を :math:`\mathbf{q}\in \mathbb{R}^D` とする．さらに，行列 :math:`\mathbf{X}=[\mathbf{x}_1,\cdots,\mathbf{x}_N]^\top \in \mathbb{R}^{N\times D}` を定義すると，内積注意による注意の重みは

.. math::

    [a_1,\cdots,a_N] = \text{softmax}\left(\frac{\mathbf{q}^\top \mathbf{X}^\top}{\sqrt{D}}\right)

と定められる． :math:`\mathbf{x}_i` に注意を適用して得られるベクトルを :math:`\tilde{\mathbf{q}}` とすると，

.. math::

    \tilde{\mathbf{q}}^\top = \sum_{i=1}^N a_i \mathbf{x}_i^\top
    = \text{softmax}\left(\frac{\mathbf{q}^\top \mathbf{X}^\top}{\sqrt{D}}\right)\mathbf{X}

となる．次に，query が複数あり， :math:`\{\mathbf{q}_1,\cdots,\mathbf{q}_M\}` のように集合をなす場合を考える．これらを並べた行列を :math:`\mathbf{Q}=[\mathbf{q}_1,\cdots,\mathbf{q}_M]^\top \in \mathbb{R}^{M\times D}` とする．さらに，これらから誘導される :math:`\mathbf{X}` の注意適用後のベクトルを並べたものを :math:`\tilde{\mathbf{Q}}=[\tilde{\mathbf{q}}_1,\cdots,\tilde{\mathbf{q}}_M]^\top \in \mathbb{R}^{M\times D}` とおくと，これは次のように計算される．ここで，行列に対する softmax は各行に独立に適用されるものとする．

.. math::

    \tilde{\mathbf{Q}} = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{X}^\top}{\sqrt{D}}\right)\mathbf{X}

Transformerの self-attention では，query，key，value はいずれも同じ入力系列から線形変換によって生成される．すなわち， :math:`\mathbf{Q}=\mathbf{X}\mathbf{W}^Q, \mathbf{K}=\mathbf{X}\mathbf{W}^K, \mathbf{V}=\mathbf{X}\mathbf{W}^V` とする．Transformerでは，上のように複数の query :math:`\mathbf{q}_j (j=1,\cdots,M)` を扱うだけでなく，注意の重みも並行して複数生成し，ソースのベクトルに適用する．これをマルチヘッド注意と呼ぶ．マルチヘッド注意を説明するために， :math:`\mathbf{X}` を :math:`\mathbf{K},\mathbf{V}\in \mathbb{R}^{N\times D}` と置き換えた

.. math::

    \mathcal{A}_D(\mathbf{Q},\mathbf{K},\mathbf{V}) \equiv \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{D}}\right)\mathbf{V}

を定義する．このとき， :math:`\tilde{\mathbf{Q}}` は :math:`\mathcal{A}_D` を使って

.. math::

    \tilde{\mathbf{Q}} = \mathcal{A}_D(\mathbf{Q},\mathbf{X},\mathbf{X})

と表される．マルチヘッド注意では，この注意計算を :math:`H` 個並列に実行する．各注意 :math:`h=1,\cdots,H` では， :math:`\mathbf{Q},\mathbf{K},\mathbf{V}` の各行ベクトルを :math:`D` より小さい :math:`D'` 次元空間に線形写像する．そのために3つの行列 :math:`\mathbf{W}_h^Q,\mathbf{W}_h^K,\mathbf{W}_h^V \in \mathbb{R}^{D\times D'}` を導入し， :math:`\mathbf{Q}\to \mathbf{Q}\mathbf{W}_h^Q, \mathbf{K}\to \mathbf{K}\mathbf{W}_h^K, \mathbf{V}\to \mathbf{V}\mathbf{W}_h^V` と置き換える．このとき，内積のスケーリングには射影後の次元 :math:`D'` を用いるので，注意 :math:`h` では

.. math::

    \text{head}_h = \mathcal{A}_{D'}(\mathbf{Q}\mathbf{W}_h^Q,\mathbf{K}\mathbf{W}_h^K,\mathbf{V}\mathbf{W}_h^V)

を計算する．ここで， :math:`\text{head}_h \in \mathbb{R}^{M\times D'}` である．こうして得られた :math:`\text{head}_h` を連結し， :math:`\mathbf{W}^O \in \mathbb{R}^{D'H\times D}` による線形写像を施して得られる

.. math::

    \mathcal{A}^M(\mathbf{Q},\mathbf{K},\mathbf{V}) = [\text{head}_1,\cdots,\text{head}_H]\mathbf{W}^O

を， :math:`\mathcal{A}_D(\mathbf{Q},\mathbf{K},\mathbf{V})\in\mathbb{R}^{M\times D}` に代わる出力とする．なお， :math:`\mathcal{A}^M(\mathbf{Q},\mathbf{K},\mathbf{V})\in \mathbb{R}^{M\times D}` である．

Transformerでは，マルチヘッド注意にいくつかの演算を組み合わせてブロックを構成し，それを複数段積み重ねることで1つのネットワークを作る．ブロック内部では，まずマルチヘッド注意によって :math:`\tilde{\mathbf{Q}}=\mathcal{A}^M(\mathbf{Q},\mathbf{K},\mathbf{V})` を計算する．次に，ここへ残差接続を導入して :math:`\mathbf{Q}+\tilde{\mathbf{Q}}\in \mathbb{R}^{M\times D}` を得て，トークンごとに独立にレイヤー正規化を適用する．各トークンには同じ計算を適用するため，レイヤー正規化のパラメータ :math:`\gamma,\beta` はトークン間で共通である．トークン単位でレイヤー正規化を適用することを :math:`\text{LayerNorm}(\cdot)` と表記すると，

.. math::

    \mathbf{Q}' = \text{LayerNorm}(\mathbf{Q}+\tilde{\mathbf{Q}})

となる．この出力 :math:`\mathbf{Q}'` には，各トークンに独立に作用する2層の位置ごとの順伝播型ネットワークを適用し，その後で再び残差接続とレイヤー正規化を行う．

.. math::

    \tilde{\mathbf{Q}} = \text{LayerNorm}(\text{ReLU}(\mathbf{Q}'\mathbf{W}_1+\mathbf{1}_M\mathbf{b}_1^\top)\mathbf{W}_2+\mathbf{1}_M\mathbf{b}_2^\top+\mathbf{Q}')

ここで， :math:`\mathbf{W}_1\in\mathbb{R}^{D\times D_{\mathrm{ff}}}` ， :math:`\mathbf{W}_2\in\mathbb{R}^{D_{\mathrm{ff}}\times D}` であり，通常は :math:`D_{\mathrm{ff}}` は :math:`D` より十分大きく選ばれる．以上は post-LN 形式であり，各サブ層の出力に残差接続を加えた後で LayerNorm を適用している．一方，pre-LN 形式では各サブ層の入力側で LayerNorm を適用する．pre-LN は深いネットワークでも学習を安定させやすいため，現代の大規模言語モデルで広く用いられている．位置情報を与えない self-attention は，集合的な演算として解釈できるが，Transformer はもともと系列データ，とくに自然言語の文を対象として開発されたものである．文のような系列データでは要素の並び順が重要であり，その情報を入力 :math:`\mathbf{X}` に反映させる必要がある．そのため，系列内の各要素に，その位置を表す情報を付加する．これを位置符号化と呼ぶ．一般には， :math:`\mathbf{x}_i` が系列内で占める位置 :math:`i` を表す， :math:`\mathbf{x}_i` と同じ長さのベクトル :math:`\mathbf{p}_i\in \mathbb{R}^D` を用意し， :math:`\mathbf{x}_i` に加算して :math:`\mathbf{x}_i+\mathbf{p}_i` とする．場合によっては連結を用いることもある． :math:`\mathbf{p}_i` の値はあらかじめ定めることもあれば，学習によって自動的に決めることもある．
