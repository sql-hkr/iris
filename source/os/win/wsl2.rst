WSL2
=====

Windows Subsystem for Linux (WSL) は Windows の機能であり，別の仮想マシンやデュアル ブートを必要とせずに，Windows マシンで Linux 環境を実行することができる．ここでは，Ubuntu24.04を使用する例を示す．

.. code-block:: powershell

   wsl --install
   wsl --install Ubuntu-24.04

なお，オンラインストアからダウンロードできる利用可能な Linux ディストリビューションのリストは，次のコマンドで確認できる．

.. code-block:: powershell

   wsl --list --online

インストール済みの Linux ディストリビューションのリストは，次のコマンドで確認できる．

.. code-block:: powershell

   wsl --list --verbose

Docker Desktopをインストールしている場合は，

.. code-block:: powershell

    wsl -l -v
      NAME              STATE           VERSION
    * Ubuntu-24.04      Running         2
      docker-desktop    Running         2

のように，Docker DesktopもWSL2上で動作していることが確認できる．ここで， :code:`-l`, :code:`-v` はそれぞれ， :code:`--list`, :code:`--verbose` のショートオプションである．

Windows 上での Linux GUI アプリケーション (X11 および Wayland) の実行がサポートされたため，例えば，ROS2のGUIアプリケーションである :code:`rqt` や :code:`rviz` も WSL2 上で動作するようになった．ここでは，xeyes を動作させる例を示す．

.. code-block:: bash

    sudo apt update
    sudo apt install x11-apps -y
    xeyes

詳しくは，Microsoft の公式ドキュメントを参照されたい．

* https://learn.microsoft.com/ja-jp/windows/wsl/

