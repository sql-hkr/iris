Behavior Tree
==============

Behavior Tree（BT）を状態空間上の写像として捉え，効率性・ロバスト性・安全性を数理的に評価する考え方を示す．ここでいう効率性は目標達成までの時間上界，ロバスト性は吸引領域の大きさで評価され，安全性は障害領域を避け続けられることを意味する．

状態空間によるBTの定式化
------------------------

BTを，状態更新則，返り値，時間刻みからなる三つ組として表す．

.. math::

	\mathcal{T}_i=\{f_i,r_i, \Delta t\},

ここで， :math:`f_i: \mathbb{R}^n \rightarrow  \mathbb{R}^n` は差分方程式の右辺，
:math:`r_i: \mathbb{R}^n \rightarrow  \{\mathcal{R},\mathcal{S},\mathcal{F}\}` は返り値であり，
それぞれ Running，Success，Failure を表す．

返り値に応じて状態空間を次の 3 領域に分割する．

.. math::

	R_i=\{x: r_i(x)=\mathcal{R} \}

	S_i=\{x: r_i(x)=\mathcal{S} \}

	F_i=\{x: r_i(x)=\mathcal{F} \}.

実行は通常の差分方程式として書ける．

.. math::

	x_{k+1}=f_i( x_{k}),

	t_{k+1}=t_{k}+\Delta t.

この表現を使うと，BT の合成が状態空間上でどのような性質を持つかを直接議論できる．

合成ノード
-----------

Sequence と Fallback は，子BTの Success / Failure に応じて次に実行する部分木を切り替える．

Sequence 合成
~~~~~~~~~~~~~

.. math::

	\mathcal{T}_0=\mbox{Sequence}(\mathcal{T}_1,\mathcal{T}_2).

.. math::

	\mbox{If }x_k\in S_1

	r_0(x_k) =  r_2(x_k)

	f_0(x_k) =  f_2(x_k)

	\mbox{ else }

	r_0(x_k) =  r_1(x_k)

	f_0(x_k) =  f_1(x_k).

第1子が Success を返したときだけ第2子を実行するので，「前段の条件が満たされたら次へ進む」構造になる．

Fallback 合成
~~~~~~~~~~~~~

.. math::

	\mathcal{T}_0=\mbox{Fallback}(\mathcal{T}_1,\mathcal{T}_2).

.. math::

	\mbox{If }x_k\in {F}_1

	r_0(x_k) =  r_2(x_k)

	f_0(x_k) =  f_2(x_k)

	\mbox{ else }

	r_0(x_k) =  r_1(x_k)

	f_0(x_k) =  f_1(x_k).

第1子が Failure のときだけ第2子へフォールバックするため，「まず優先度の高い方を試し，だめなら代替手段へ移る」構造として解釈できる．

Parallel 合成
~~~~~~~~~~~~~

状態空間を :math:`x=(x_1,x_2)` に分けて互いに別の部分を制御するなら，Parallel は同時実行として表せる．

.. math::

	\mathcal{T}_0=\mbox{Parallel}(\mathcal{T}_1,\mathcal{T}_2).

このとき :math:`f_0(x)=(f_{11}(x),f_{22}(x))` であり，返り値は閾値 :math:`M` により決まる．

.. math::

	\mbox{If } M=1

	r_0(x) =  \mathcal{S}  \mbox{ If } r_1(x)=\mathcal{S} \vee r_2(x)=\mathcal{S}

	r_0(x) =  \mathcal{F}  \mbox{ If } r_1(x)=\mathcal{F} \wedge r_2(x)=\mathcal{F}

	r_0(x) =  \mathcal{R}  \mbox{ else }

	\mbox{If } M=2

	r_0(x) =  \mathcal{S}  \mbox{ If } r_1(x)=\mathcal{S} \wedge r_2(x)=\mathcal{S}

	r_0(x) =  \mathcal{F}  \mbox{ If } r_1(x)=\mathcal{F} \vee r_2(x)=\mathcal{F}

	r_0(x) =  \mathcal{R}  \mbox{ else }

効率性とロバスト性
------------------

効率性を「有限時間で Success に到達するまでの時間上界 :math:`\tau`」，ロバスト性を「Success に到達できる初期値集合 :math:`R'` の大きさ」として定義する．

有限時間成功
~~~~~~~~~~~~

.. math::

	x(t)\in R'  \ \mbox{for all } t\in [0,\tau')

	x(t)\in S \ \mbox{for } t = \tau'

BT が吸引領域 :math:`R'` をもつ有限時間成功（FTS, Finite Time Successful）であるとは，任意の :math:`x(0)\in R'\subset R` に対して，
ある一様上界 :math:`\tau` と到達時刻 :math:`\tau'(x(0))\leq \tau` が存在し，到達前は :math:`R'` から出ず，到達時刻で Success 領域 :math:`S` に入ることをいう．

Sequence の性質
~~~~~~~~~~~~~~~

:math:`\mathcal{T}_1,\mathcal{T}_2` がともに FTS で，

.. math::

	S_1=R_2' \cup S_2

を満たすなら，

.. math::

	\mathcal{T}_0=\mbox{Sequence}(\mathcal{T}_1,\mathcal{T}_2)

も FTS であり，

.. math::

	\tau_0 = \tau_1+\tau_2

	R_0'= R_1' \cup R_2'

	S_0=S_1 \cap S_2 = S_2.

つまり，前段の Success 領域が後段の吸引領域を十分に含んでいれば，逐次実行しても時間上界は加算され，吸引領域は合成により拡張される．

Fallback の性質
~~~~~~~~~~~~~~~

:math:`\mathcal{T}_1,\mathcal{T}_2` がともに FTS で，

.. math::

	S_2 \subset  R_1'

を満たすなら，

.. math::

	\mathcal{T}_0=\mbox{Fallback}(\mathcal{T}_1,\mathcal{T}_2)

も FTS であり，

.. math::

	\tau_0 = \tau_1+\tau_2

	R_0'= R_1' \cup R_2'

	S_0=S_1.

これは，右側の代替行動が左側の主行動を「準備する」構造である．失敗したら別の行動で状態を整え，その後に本来の行動を再び成立させることで，BT 全体の吸引領域を広げられる．

Parallel の性質
~~~~~~~~~~~~~~~

:math:`\mathcal{T}_1,\mathcal{T}_2` がともに FTS なら，Parallel 合成も FTS である．

.. math::

	\mbox{If } M=1

	R_0' = \{R_1' \cup R_2'\} \setminus \{S_1 \cup S_2\}

	S_0 = S_1 \cup S_2

	\tau_0 = \min(\tau_1,\tau_2)

	\mbox{If } M=2

	R_0' =  \{R_1' \cap R_2'\} \setminus \{S_1 \cap S_2\}

	S_0 = S_1 \cap S_2

	\tau_0 = \max(\tau_1,\tau_2)

:math:`M=1` はどちらか一方が成功すれば十分な場合，:math:`M=2` は両方の成功が必要な場合に対応する．

安全性
------

安全性は，障害領域 :math:`O \subset \mathbb{R}^n` を決して踏まないこととして定義する．

安全の定義
~~~~~~~~~~~

初期化領域 :math:`I \subset R` に対し，任意の :math:`x(0)\in I` から出発してすべての :math:`t \geq 0` で :math:`x(t) \not \in O` が成り立つとき，その BT は安全である．

安全保証性の定義
~~~~~~~~~~~~~~~~~~

さらに，BT が安全であるだけでなく，FTS であり，その Success 領域 :math:`S` を取り巻く初期化領域 :math:`I` が次を満たすとき，その BT は安全保証性をもつという．

.. math::

	\{x\in X \subset \mathbb{R}^n: \inf_{s\in S} || x-s  || \leq d \} \subset I,

ここで :math:`d` は，他の BT が 1 ステップで動ける最大距離，:math:`X` は到達可能な状態空間である．
この条件があると，後段のBTが Success 領域 :math:`S` を出ても，ただちに安全マージン :math:`I` に入り，障害領域 :math:`O` に直接飛び込むことができない．

Sequence 合成の安全性
~~~~~~~~~~~~~~~~~~~~

:math:`\mathcal{T}_1` が障害領域 :math:`O_1`，初期化領域 :math:`I_1`，マージン :math:`d` に関して安全保証性をもち，
:math:`\mathcal{T}_2` が

.. math::

	\max_x ||x-f_2(x)||<d

を満たす任意の BT なら，

.. math::

	\mathcal{T}_0=\mbox{Sequence}(\mathcal{T}_1,\mathcal{T}_2)

は :math:`O_1` と :math:`I_1` に関して安全である．

要するに，前段の BT を「安全監視器」として置いておけば，後段のタスクBTが多少自由に動いても，1 ステップで安全領域を飛び越えない限り，全体の安全性を保てる．

チャタリング
-------------

BT の切替境界では，2 つの部分木が交互に選ばれてチャタリングが起こることがある．
Sequence 合成 :math:`\mathcal{T}_0=\mbox{Sequence}(\mathcal{T}_1,\mathcal{T}_2)` に対し，境界関数 :math:`s(x)` を用いて

.. math::

	\lambda_i(x)=\left(\frac{\partial s}{\partial x}\right)^\top (f_i(x)-x).

とおくと，十分小さい :math:`\Delta t` のもとで，境界上の点 :math:`x \in \delta S_1` が chatter free であるための十分条件は

.. math::

	\lambda_1(x)<0 \ \mbox{or} \ \lambda_2(x)>0

である．これは，少なくとも片側のベクトル場が切替境界から外向きに向いていれば，不要な往復切替を避けやすいことを意味する．
