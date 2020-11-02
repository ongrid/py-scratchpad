import asyncio
import logging

class Server:

    counter = 0

    async def run(self):
        task_main_loop = asyncio.create_task(self.main_loop())
        task_sum_loop1 = asyncio.create_task(self.summator_loop(1,100))
        task_sum_loop2 = asyncio.create_task(self.summator_loop(2,100))
        task_sum_loop3 = asyncio.create_task(self.summator_loop(3,100))
        task_sum_loop4 = asyncio.create_task(self.summator_loop(4,100))
        await task_main_loop
        await task_sum_loop1
        await task_sum_loop2
        await task_sum_loop3
        await task_sum_loop4

    async def main_loop(self):
        i = 0
        for i in range(100):
            await asyncio.sleep(0.1)
            i += 1
            self.counter += 1
            print("main %s" % self.counter)
    
    async def summator_loop(self, name, amount):
        for i in range(amount):
            await asyncio.sleep(0.1)
            i += 1
            self.counter += 1
            print("summator %s %s" % (name, self.counter))


def main():
    server = Server()
    asyncio.run(server.run())
    

if __name__ == "__main__":
    main()