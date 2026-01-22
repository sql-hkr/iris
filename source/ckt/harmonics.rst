ひずみ波交流
====================

ひずみ波交流の実行値は，

.. math::

    E=\sqrt{\frac{1}{T}\int_0^T e^2(t)dt}
    =\sqrt{\sum_{n=1}^{\infty} E_n^2}

    I=\sqrt{\frac{1}{T}\int_0^T i^2(t)dt}
    =\sqrt{\sum_{n=1}^{\infty} I_n^2} .

高調波成分全体と基本波成分の比を全高調波歪みは，

.. math::

   \text{THD}_E \equiv \frac{\sqrt{\sum_{n=2}^{\infty} E_n^2}}{E_1}

   \text{THD}_I \equiv \frac{\sqrt{\sum_{n=2}^{\infty} I_n^2}}{I_1}  .

電力は，

.. math::

    P = \frac{1}{T}\int_0^T v(t)i(t)dt
    = E_0I_0 + \sum_{n=1}^{\infty} E_n I_n \cos\theta_n .

ひずみ波の力率は，

.. math::

    \text{PF} = \frac{P}{EI} = \frac{E_0I_0 + \sum_{n=1}^{\infty} E_n I_n \cos\theta_n}{\sqrt{\sum_{n=1}^{\infty} E_n^2}\sqrt{\sum_{n=1}^{\infty} I_n^2}}.

対称三相ひずみ波起電力
------------------------

三相起電力 :math:`e_a(t), e_b(t), e_c(t)` が対称ひずみ波（対称波は，直流分ならびに偶数調波は含まない）である場合は，

.. math::

   e_a(t) = \sqrt{2}E_1 \sin\omega t + \sqrt{2}E_3 \sin(3\omega t + \phi_3)
   
   + \sqrt{2}E_5 \sin(5\omega t + \phi_5) + \cdots

   e_b(t) = \sqrt{2}E_1 \sin\left(\omega t - \frac{2\pi}{3}\right) + \sqrt{2}E_3 \sin\left(3\omega t + \phi_3\right)
   
   + \sqrt{2}E_5 \sin\left(5\omega t + \phi_5 - \frac{4\pi}{3}\right) + \cdots

   e_c(t) = \sqrt{2}E_1 \sin\left(\omega t - \frac{4\pi}{3}\right) + \sqrt{2}E_3 \sin\left(3\omega t + \phi_3\right)
   
   + \sqrt{2}E_5 \sin\left(5\omega t + \phi_5 - \frac{2\pi}{3}\right) + \cdots

となることから，三相起電力を三角形に接続すると，基本波，第5長波，第7長波などのように対称起電力となる各調波の和は零となる．しかし，直流分，第3長波およびその倍数の長波は各相が同相となるから，その和は零とならず大きさが3倍となって現れ，これにより循環電流が流れる．これが普通，交流発電機で電機子巻線に三角形結線が採用されない理由の一つである．

参考文献
----------

.. [#f1] 小郷 寛，小亀 英己，石亀 篤司，『基礎からの交流理論』，オーム社，2002年．
