import os

import anyio
from signalstickers_client import StickersClient
from signalstickers_client.models import LocalStickerPack, Sticker


async def main():
    def add_sticker(path, emoji):

        stick = Sticker()
        stick.id = pack.nb_stickers
        stick.emoji = emoji

        with open(path, "rb") as f_in:
            stick.image_data = f_in.read()

        pack._addsticker(stick)


    pack = LocalStickerPack()

    # Set here the pack title and author
    pack.title = 'Cult of the Party Parrot'
    pack.author = "PARTY OR DIE"
    # pack.title = 'Test'
    # pack.author = "Test"

    # Add the stickers here, with their emoji
    # Accepted format:
    # - Non-animated webp
    # - PNG
    # - GIF <100kb for animated stickers

    add_sticker("apng/60fpsparrot.png", "🦜")
    add_sticker("apng/accessibleparrot.png", "♿")
    add_sticker("apng/angryparrot.png", "💢")
    add_sticker("apng/aussiecongaparrot.png", "🇦🇺")
    add_sticker("apng/aussieparrot.png", "🇦🇺")
    add_sticker("apng/aussiereversecongaparrot.png", "🇦🇺")
    add_sticker("apng/backwardsparrot.png", "🦜")
    add_sticker("apng/balconyparrot.png", "🦜")
    add_sticker("apng/beerparrot.png", "🍺")
    add_sticker("apng/beretparrot.png", "🇫🇷")
    add_sticker("apng/bikerparrot.png", "🏴‍☠️")
    add_sticker("apng/birthdaypartyparrot.png", "🥳")
    add_sticker("apng/bluntparrot.png", "🚬")
    add_sticker("apng/bobaparrot.png", "🧋")
    add_sticker("apng/boredparrot.png", "😐")
    add_sticker("apng/bouncingparrot.png", "😀")
    add_sticker("apng/brazilianfanparrot.png", "🇧🇷")
    add_sticker("apng/brazilianplayerparrot.png", "🇧🇷")
    add_sticker("apng/bunnyparrot.png", "🐇")
    add_sticker("apng/cakeparrot.png", "🎂")
    add_sticker("apng/ceilingparrot.png", "👆")
    add_sticker("apng/chicoparrot.png", "🤠")
    add_sticker("apng/christmasparrot.png", "🎅")
    add_sticker("apng/confusedparrot.png", "😕")
    add_sticker("apng/congaparrot.png", "🇨🇬")
    add_sticker("apng/congapartyparrot.png", "😎")
    add_sticker("apng/copparrot.png", "👮‍♂️")
    add_sticker("apng/covid19parrot.png", "🤧")
    add_sticker("apng/darkmodeparrot.png", "🕶️")
    add_sticker("apng/dealwithitnowparrot.png", "😎")
    add_sticker("apng/dealwithitparrot.png", "😎")
    add_sticker("apng/discoparrot.png", "🕺")
    add_sticker("apng/docparrot.png", "😷")
    add_sticker("apng/donutparrot.png", "🍩")
    add_sticker("apng/everythingsfineparrot.png", "🔥")
    add_sticker("apng/evilparrot.png", "😈")
    add_sticker("apng/fastparrot.png", "🏃")
    add_sticker("apng/flowerparrot.png", "🌻")
    add_sticker("apng/flyingmoneyparrot.png", "💸")
    add_sticker("apng/footballparrot.png", "🏈")
    add_sticker("apng/gentlemanparrot.png", "🎩")
    add_sticker("apng/glimpseparrot.png", "🙈")
    add_sticker("apng/gothparrot.png", "🧛")
    add_sticker("apng/grouchoparrot.png", "🧓")
    add_sticker("apng/hanamiparrot.png", "🌳")
    add_sticker("apng/hardhatparrot.png", "👷")
    add_sticker("apng/harpoparrot.png", "🎩")
    add_sticker("apng/headbangingparrot.png", "🤘")
    add_sticker("apng/headingparrot.png", "⚽")
    add_sticker("apng/headsetparrot.png", "🎧")
    add_sticker("apng/hmmparrot.png", "🤔")
    add_sticker("apng/horizontalparrot.png", "🦜")
    add_sticker("apng/hypnoparrot.png", "🍭")
    add_sticker("apng/hypnoparrotdark.png", "🍭")
    add_sticker("apng/hypnoparrotlight.png", "🍭")
    add_sticker("apng/imposterparrot.png", "🤔")
    add_sticker("apng/innersourceparrot.png", "🦓")
    add_sticker("apng/inverseparrot.png", "🌃")
    add_sticker("apng/jediparrot.png", "⚔️")
    add_sticker("apng/jumpingparrot.png", "⛹️‍♂️")
    add_sticker("apng/jumpingparrotjr.png", "⛹️‍♂️")
    add_sticker("apng/kindasusparrot.png", "🤔")
    add_sticker("apng/laptop_parrot.png", "💻")
    add_sticker("apng/levitationparrot.png", "⛹️‍♀️")
    add_sticker("apng/maracasparrot.png", "🥳")
    add_sticker("apng/mardigrasparrot.png", "🤡")
    add_sticker("apng/marshmallowparrot.png", "🏕️")
    add_sticker("apng/mateparrot.png", "🧉")
    add_sticker("apng/meldparrot.png", "2️⃣")
    add_sticker("apng/middleparrot.png", "🦜")
    add_sticker("apng/moonparrot.png", "🌔")
    add_sticker("apng/moonwalkingparrot.png", "🔙")
    add_sticker("apng/mustacheparrot.png", "🧔")
    add_sticker("apng/norwegianblueparrot.png", "⚰️")
    add_sticker("apng/nyanparrot.png", "🐱")
    add_sticker("apng/originalparrot.png", "🦜")
    add_sticker("apng/parrot.png", "🦜")
    add_sticker("apng/parrotnotfound.png", "⁉️")
    add_sticker("apng/partyblobcat.png", "🐱")
    add_sticker("apng/partyparrot.png", "😎")
    add_sticker("apng/picassoparrot.png", "🧑‍🎨")
    add_sticker("apng/pingpongparrot.png", "🏓")
    add_sticker("apng/pirateparrot.png", "🏴‍☠️")
    add_sticker("apng/playcatchleftparrot.png", "⚾")
    add_sticker("apng/playcatchrightparrot.png", "⚾")
    add_sticker("apng/pokeparrot.png", "🇯🇵")
    add_sticker("apng/popcornparrot.png", "🍿")
    add_sticker("apng/portalblueparrot.png", "🚪")
    add_sticker("apng/portalorangeparrot.png", "🚪")
    add_sticker("apng/pumpkinparrot.png", "🎃")
    add_sticker("apng/quadparrot.png", "👪")
    add_sticker("apng/redbullparrot.png", "🥤")
    add_sticker("apng/redenvelopeparrot.png", "✉")
    add_sticker("apng/redhatparrot.png", "👲")
    add_sticker("apng/rythmicalparrot.png", "🎶")
    add_sticker("apng/sadparrot.png", "😢")
    add_sticker("apng/sassyparrot.png", "🦜")
    add_sticker("apng/scienceparrot.png", "🥼")
    add_sticker("apng/sherlockholmesparrot.png", "🕵️‍♂️")
    add_sticker("apng/shortparrot.png", "🦜")
    add_sticker("apng/shuffleparrot.png", "🦜")
    add_sticker("apng/sidewaysparrot.png", "↕")
    add_sticker("apng/sintparrot.png", "✝")
    add_sticker("apng/sithparrot.png", "😈")
    add_sticker("apng/sleepingparrot.png", "😴")
    add_sticker("apng/slowparrot.png", "🦥")
    add_sticker("apng/sneezyparrot.png", "🤧")
    add_sticker("apng/spinningparrot.png", "🔁")
    add_sticker("apng/spyparrot.png", "🕵️‍♂️")
    add_sticker("apng/stayhomeparrot.png", "🏠")
    add_sticker("apng/stayhomeparrotcloser.png", "🏠")
    add_sticker("apng/staytfhomeparrot.png", "🏠")
    add_sticker("apng/sushiparrot.png", "🍣")
    add_sticker("apng/tennisparrot.png", "🎾")
    add_sticker("apng/thefastestparrot.png", "⏩")
    add_sticker("apng/thumbsupparrot.png", "👍")
    add_sticker("apng/tiedyeparrot.png", "🌈")
    add_sticker("apng/tinfoilhatparrot.png", "🤪")
    add_sticker("apng/tpparrot.png", "🧻")
    add_sticker("apng/transparront.png", "🌃")
    add_sticker("apng/turndownforwatchparrot.png", "😎")
    add_sticker("apng/twinsparrot.png", "👫")
    add_sticker("apng/ultrafastparrot.png", "⏩")
    add_sticker("apng/verticalparrot.png", "🦜")
    add_sticker("apng/vikingparrot.png", "⚔")
    add_sticker("apng/wendyparrot.png", "🍔")
    add_sticker("apng/wfhparrot.png", "🏠")
    add_sticker("apng/whitewalkerparrot.png", "🦹‍♂️")
    add_sticker("apng/yosemitesamparrot.png", "🧛‍♀️")
    add_sticker("apng/zombieparrot.png", "💀")
    add_sticker("apng/zoukparrot.png", "💃")


    # Specifying a cover is optionnal
    # By default, the first sticker is the cover
    cover = Sticker()
    cover.id = pack.nb_stickers
    # Set the cover file here
    with open("apng/60fpsparrot.png", "rb") as f_in:
        cover.image_data = f_in.read()
    pack.cover = cover


    # Instanciate the client with your Signal crendentials
    async with StickersClient(os.environ['SIGNAL_USERNAME'], os.environ['SIGNAL_PASSWORD']) as client:
        # Upload the pack
        pack_id, pack_key = await client.upload_pack(pack)

    print("Pack uploaded!\n\nhttps://signal.art/addstickers/#pack_id={}&pack_key={}".format(pack_id, pack_key))

if __name__ == '__main__':
    anyio.run(main)
