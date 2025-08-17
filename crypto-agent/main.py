import os, requests
from dotenv import load_dotenv
from agents import (
    Agent,
    OpenAIChatCompletionsModel,
    AsyncOpenAI,
    set_tracing_disabled,
    function_tool,
)
from typing import TypedDict, Optional, List
from dataclasses import dataclass

# loading env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:  # raises error if the api key is not found
    raise ValueError("Not able to load the api key")

# used uppercase for constants. following the standard way
MODEL = "gemini-2.5-flash"  # the model to be used for the agent
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=BASE_URL,
)

model = OpenAIChatCompletionsModel(model=MODEL, openai_client=client)

set_tracing_disabled(disabled=True)


@dataclass
class CryptoCoinDict(TypedDict):
    id: str
    symbol: str
    name: str
    nameid: str
    rank: int
    price_usd: str
    percent_change_1h: str
    percent_change_24h: str
    percent_change_7d: str
    price_btc: str
    market_cap_usd: str
    volume24: float
    volume24a: float
    csupply: str
    tsupply: str
    msupply: Optional[str]


@dataclass
class ExchangeInfo:
    name: str
    base: str
    quote: str
    price: float
    price_usd: float
    volume: float
    volume_usd: float
    time: int


@function_tool
def get_coins(names: List[str]) -> List[CryptoCoinDict]:
    try:
        response = requests.get(
            "https://api.coinlore.net/api/tickers/",
            headers={"User-Agent": "CryptoAgent"},
            timeout=10,
        )
        coins = response.json().get("data", [])
    except Exception as e:
        return [f"Not able to fetch data: {e}"]

    results = []
    name_set = set(name.lower() for name in names)

    for coin in coins:
        coin_keys = {
            coin["id"].lower(),
            coin["symbol"].lower(),
            coin["nameid"],
        }
        if name_set & coin_keys:
            results.append(coin)

    return results if results else [f"No matching coins found for: {names}"]


@function_tool
def get_info(exchange_names: List[str]) -> List[ExchangeInfo]:
    try:
        response = requests.get(
            "https://api.coinlore.net/api/coin/markets/?id=90",
            headers={"User-Agent": "CryptoAgent"},
            timeout=10,
        )
        exchanges = response.json()
    except Exception as e:
        return [f"Not able to fetch data: {e}"]

    results = []
    name_set = set(name.lower() for name in exchange_names)

    for exchange in exchanges:
        if exchange["name"].lower() in name_set:
            results.append(exchange)

    return (
        results if results else [f"No matching exchanges found for: {exchange_names}"]
    )


agent = Agent(
    name="CryptoAgent",
    instructions=(
        "You are a crypto agent. You can fetch real-time coin data using get_coins, "
        "and exchange info using get_info. These tools accept lists, so when the user "
        "asks about multiple coins or exchanges, call the tool once with all names."
    ),
    model=model,
    tools=[get_coins, get_info],
)
