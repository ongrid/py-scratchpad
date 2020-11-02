from aiohttp import web
import asyncio

class Model:
    counter = 0

model = Model()

async def incrementor(app, model):
    try:
        while True:
            model.counter += 1
            await asyncio.sleep(0.001)
            print(model.counter)
    except asyncio.CancelledError:
        pass
    finally:
        print("Die incrementor")

async def increaser(app, model):
    try:
        while True:
            model.counter += 1
            await asyncio.sleep(0.001)
            print(model.counter)
    except asyncio.CancelledError:
        pass
    finally:
        print("Die increaser")

async def handle(request):
    #name = request.match_info.get('name', "Anonymous")
    #text = "Hello, " + name
    return web.Response(text=str(request.app['model'].counter))

async def start_background_tasks(app):
    app['incrementor'] = asyncio.create_task(incrementor(app, model))
    app['increaser'] = asyncio.create_task(increaser(app, model))

async def cleanup_background_tasks(app):
    app['incrementor'].cancel()
    await app['incrementor']
    app['increaser'].cancel()
    await app['increaser']

app = web.Application()
app['model'] = model
app.add_routes([web.get('/', handle)])
app.on_startup.append(start_background_tasks)
app.on_cleanup.append(cleanup_background_tasks)

if __name__ == '__main__':
    web.run_app(app)