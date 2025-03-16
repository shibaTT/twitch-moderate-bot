# Twitch Moderate Bot

このリポジトリは、[Chakoshi](https://chakoshi.ntt.com/) を使って Twitch チャットを管理するためのモデレートボットを提供します。

## 特徴

-   不適切なメッセージの自動削除
-   カスタムキーワードフィルタリング
-   タイムアウトや BAN の自動実行
-   ユーザーごとのアクティビティログ

## 必要条件

-   Python (バージョン 3.8 以上)
-   Twitch アカウントと OAuth トークン
-   Chakoshi Token

## インストール

1. このリポジトリをクローンします:
    ```bash
    git clone https://github.com/shibaTT/twitch-moderate-bot.git
    ```
2. ディレクトリに移動します:
    ```bash
    cd twitch-moderate-bot
    ```
3. 必要な依存関係をインストールします:
    ```bash
    pip install -r requirements.txt
    ```

## Twitch クライアント ID の取得方法

1. [Twitch Developer Portal](https://dev.twitch.tv/) にアクセスします。
2. 自分のアカウントでログインします。
3. 「Your Console」ページに移動し、「Register Your Application」をクリックします。
4. 必要な情報を入力します:
    - **Name**: アプリケーションの名前を入力します。
    - **OAuth Redirect URLs**: `http://localhost` を入力します。
    - **Category**: 適切なカテゴリを選択します。
5. 「Create」をクリックすると、アプリケーションが作成され、クライアント ID が表示されます。
6. クライアント ID をコピーして、`.env`ファイルに記載してください。

## Chakoshi API キーの取得方法

1. [Chakoshi Platform](https://platform.beta.chakoshi.ntt.com/)にアクセスします。
2. アカウントを作成します。
3. 右上の歯車から設定を開きます。
4. API キーのタブに切り替えて、API キーを作成します。
5. API キーをコピーして、`.env` ファイルに記載してください。

## 使用方法

1. `.env`ファイルを作成し、以下の内容を記入します:
    ```
    CHAKOSHI_API_KEY=chakoshiのAPIキー
    TWITCH_CLIENT_ID=TwitchのクライアントID
    TWITCH_ACCESS_TOKEN=Twitchのアクセストークン
    ```
2. ボットを起動します:
    ```bash
    python main.py
    ```

## ライセンス

このプロジェクトは MIT ライセンスの下で提供されています。詳細は[LICENSE](./LICENSE)ファイルをご覧ください。
