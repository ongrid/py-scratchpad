import asyncio
import logging

class Server:

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.serve())

    async def main_loop(self):
        i = 0
        while True:
            await asyncio.sleep(1)
            i += 1
            print("main %s" % i)

    async def serve(self, sockets=None):
        print("start serve")
        await self.main_loop()
        await self.shutdown()

    async def startup(self, sockets=None):
        loop = asyncio.get_event_loop()

    async def shutdown(self, sockets=None):
        print("Shutting down")

def main():
    server = Server()
    server.run()
    

if __name__ == "__main__":
    main()