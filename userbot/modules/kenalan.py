from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.kenalan(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Hai Perkenalkan Namaku Lodwyg Antameng Biasa Dipanggil Alexs`")
    sleep(3)
    await typew.edit("17 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di Manado, Terima Kasih, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`SEMANGAT YOO!!!`")
    sleep(1)
    await typew.edit("`BISA YOO!!!`")
    sleep(1)
    await typew.edit("`BISA GILA :))`")
# Create by myself @localheart
