import asyncio, json, os, getpass
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

BASE = os.path.dirname(os.path.abspath(__file__))

async def main():
    cfg = json.load(open(os.path.join(BASE, "lead_config.json"), encoding="utf-8"))
    client = TelegramClient(os.path.join(BASE, "lead_session"), int(cfg["tg_api_id"]), cfg["tg_api_hash"])
    await client.connect()
    if await client.is_user_authorized():
        me = await client.get_me()
        print("Уже вошёл: +" + str(me.phone))
        await client.disconnect()
        return
    import qrcode
    ok = False
    for attempt in range(8):
        qr = await client.qr_login()
        q = qrcode.QRCode(border=2)
        q.add_data(qr.url)
        q.print_ascii(invert=True, tty=False)
        print("Телефон: Telegram -> Настройки -> Устройства -> ПРИВЯЗАТЬ УСТРОЙСТВО")
        print("Наведи камеру на квадрат. QR живёт ~30 сек, потом появится новый. (%d/8)" % (attempt + 1))
        try:
            await qr.wait()
            ok = True
            break
        except SessionPasswordNeededError:
            pwd = getpass.getpass("На аккаунте пароль 2FA — введи его: ")
            await client.sign_in(password=pwd)
            ok = True
            break
        except asyncio.TimeoutError:
            print("QR протух — рисую новый...\n")
    await client.disconnect()
    if ok:
        me = await client.get_me()
        print("ГОТОВО! Вошёл как: +" + str(me.phone) + " — сессия сохранена, lead_parser больше ничего не спросит.")
    else:
        print("Не вышло за 8 попыток — запусти ещё раз: python3 tg_login.py")

asyncio.run(main())
