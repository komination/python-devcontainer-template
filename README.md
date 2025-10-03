# Python Development Startup Template

これは、Dev Containerと`uv`を使用したモダンなPython開発のためのスタートアップテンプレートです。

## ✨ 特徴

- **開発環境のコンテナ化**: DockerとVSCode Dev Containerを使用して、一貫性のある開発環境をすぐに利用できます。
- **高速なパッケージ管理**: `uv`を利用して、依存関係のインストールや管理を高速に行います。
- **テスト**: `pytest`によるテストフレームワークがセットアップ済みです。
- **静的解析とフォーマッティング**: `ruff`を導入し、コードの品質と一貫性を保ちます。

## 🚀 はじめ方

### 前提条件

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Dev Containers extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### 起動手順

1. このリポジトリをクローンします。
2. VSCodeでリポジトリを開きます。
3. `F1`キーを押してコマンドパレットを開き、`Dev Containers: Reopen in Container`を選択します。

初回起動時、`postCreateCommand`が実行され、`pyproject.toml`に定義されたすべての依存関係（開発用も含む）が自動的にインストールされます。

## 🛠 使い方

### 依存関係の管理

- 新しいライブラリを追加する場合:
  ```bash
  uv pip install <library-name>
  ```
- 開発用のライブラリを追加する場合:
  ```bash
  uv pip install <library-name> -e .[dev]
  ```

### コマンドの実行

- **テストの実行**:
  ```bash
  pytest
  ```

- **リンターの実行**:
  ```bash
  ruff check .
  ```

- **コードのフォーマット**:
  ```bash
  ruff format .
  ```