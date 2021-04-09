# partyparrot-stickers
Stores GIFs from [cultofthepartyparrot.com](https://cultofthepartyparrot.com) to upload as Signal Stickers. #makeprivacystick

![parrot_gif](apng/60fpsparrot.png)

## Prerequisites
* Python 3
* [Python client for Signal stickers](https://github.com/signalstickers/signalstickers-client)

## Upload Sticker Pack
### Setup
1. `pip3 install --user signalstickers-client`
2. Get Signal U/PW:
> **You will need your Signal credentials** To obtain them, open the Developer
> Tools in Signal Desktop, and type `window.reduxStore.getState().items.uuid_id`
> to get your USER, and `window.reduxStore.getState().items.password` to get
> your PASSWORD.

### Upload
3. Make changes in `upload_stickers.py`
4. `python3 upload_stickers.py`
