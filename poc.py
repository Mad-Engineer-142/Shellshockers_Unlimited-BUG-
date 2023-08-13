import asyncio
import websockets

URL              = "wss://shellshock.io/services/"
START_NUMBER     = 26887147
YOUR_FIREBASE_ID = ""

async def poc():
    for u in range(100):
        async with websockets.connect(URL) as websocket:

            nn1 = '{"cmd":"incentivizedVideoReward","token":null,'
            nn2 = f'"id":{START_NUMBER +u},'
            nn3 = f'"firebaseId":"{YOUR_FIREBASE_ID}",'
            nn4 ='"firstPlay":false,"status":"SUCCESS"}'

            payload = nn1 + nn2 + nn3 + nn4
            await websocket.send(payload)
            response = await websocket.recv()
            print(f"{START_NUMBER +u}", "Received:", response)
            await websocket.close()


asyncio.get_event_loop().run_until_complete(poc())
