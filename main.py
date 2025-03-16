from twitchio import Channel, Message
from twitchio.ext import commands
import requests
import os
from dotenv import load_dotenv

load_dotenv()


bot = commands.Bot(
    token=os.getenv("TWITCH_ACCESS_TOKEN"),
    initial_channels=["tor1pp"],
    prefix="!",
    nick="tor1pp",
)

url = "https://api.beta.chakoshi.ntt.com/v1/judge/text"
chakoshi_api_key = os.getenv("CHAKOSHI_API_KEY")


@bot.event()
async def event_ready():
    """Botが初期設定完了し、Twitchに接続したときに実行されます"""
    print(f"Botの初期設定が完了しました: {bot.nick}")
    # print(f'接続チャンネル: {", ".join(bot.initial_channels)}')
    print("チャットの監視を開始します...")


@bot.event()
async def event_message(message):
    # ボット自身のメッセージは無視（エコー回避）
    # if message.echo:
    #     return

    # メッセージ情報にアクセス
    print(f"チャンネル: {message.channel.name}")
    if message.author:
        print(f"送信者: {message.author.name}")
    print(f"メッセージ内容: {message.content}")
    print(f"タイムスタンプ: {message.timestamp}")

    # リクエストヘッダーの設定
    headers = {
        "Authorization": f"Bearer {chakoshi_api_key}",
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    # リクエストボディの設定
    data = {
        "input": message.content,
        "model": "chakoshi-moderation-241223",
    }

    response = requests.post(url, headers=headers, json=data)

    # レスポンスの内容を取得
    try:
        response_json = response.json()

        # 必要に応じて、レスポンスの内容を解析して処理
        if "results" in response_json:

            results = response_json["results"]
            print(results)

            print(f"判定カテゴリ: {results["unsafe_category"]}")
            print(f"スコア: {results["unsafe_score"]}")
            print(f"判定: {"不適切" if results["unsafe_flag"] else "適切"}")
    except Exception as e:
        # JSONとして解析できない場合はテキストとして表示
        print(f"レスポンス解析エラー: {e}")
        print(f"レスポンス本文: {response.text}")


# !testというコマンドの例
@bot.command(name="test")
async def test_command(ctx):
    await ctx.send(f"テストコマンドが実行されました！こんにちは {ctx.author.name}！")


def main():
    bot.run()


if __name__ == "__main__":
    main()
