BCDEdit
========

BCDEdit は Windows のブート構成データ（Boot Configuration Data; BCD）を管理するためのコマンドラインツールである．UEFI ブートエントリの確認や削除など，ブート関連の操作を行う際に使用される．ここでは，Windows と Linux のデュアルブート環境で Linux を削除した後，UEFI に残る不要なブートエントリ（ex: ubuntu）を削除する手順を示したい．まず，管理者権限でコマンドプロンプトを起動し，ファームウェアのブートエントリを確認する．

.. code-block:: powershell

    bcdedit /enum firmware

出力結果の中から不要なエントリ（ex: `description ubuntu`）を特定し，その `identifier` （GUID）を控える．

不要なブートエントリを削除する．

.. code-block:: powershell

    bcdedit /delete {GUID}

なお， `{GUID}` は対象エントリの identifier に置き換える．

削除後，再度エントリ一覧を確認し，不要な項目が消えていることを確認する．

.. code-block:: powershell

    bcdedit /enum firmware

必要に応じて，EFI システムパーティション内に残っている関連ディレクトリ（ex: `\\EFI\\ubuntu\\` ）も削除する．

EFI パーティションをマウントする．

.. code-block:: powershell

    mountvol S: /s

対象ディレクトリを削除する．

.. code-block:: powershell

    rmdir /s S:\EFI\ubuntu

EFI パーティションをアンマウントする．

.. code-block:: powershell

    mountvol S: /d

以上により，Linux 削除後に残る不要な UEFI ブートエントリおよび関連ファイルを整理できる．

BCDEdit コマンドの詳細については，Microsoft の公式ドキュメントを参照されたい．

* https://learn.microsoft.com/ja-jp/windows-hardware/manufacture/desktop/bcdedit-command-line-options?view=windows-11
