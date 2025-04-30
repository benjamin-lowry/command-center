import asyncio
from commandcenter.app import get_app

async def main():
    app = get_app()
    app.listen(8000)
    print('Serving on http://localhost:8000')
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()

if __name__ == "__main__":
    asyncio.run(main())
