import aiohttp
import asyncio

async def fetch_todos():
    url = "https://jsonplaceholder.typicode.com/todos/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            todos = await response.json()
            return todos

async def main():
    todos = await fetch_todos()
    print(todos)

if __name__ == "__main__":
    asyncio.run(main())
