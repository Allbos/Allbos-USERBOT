from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.tmo(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`𝙏𝙈𝙊 𝙈𝙪𝙡𝙪 𝙇𝙪`")
    sleep(2)
    await typew.edit("`𝙅𝙖𝙙𝙞𝙖𝙣 𝙅𝙪𝙜𝙖 𝙆𝙖𝙜𝙖𝙠`")
    sleep(1)
    await typew.edit("`𝙏𝙖𝙥𝙞 𝙆𝙖𝙡𝙤 𝙇𝙪 𝙅𝙖𝙙𝙞𝙖𝙣, 𝙐𝙟𝙪𝙣𝙜-𝙐𝙟𝙪𝙣𝙜𝙣𝙮𝙖 𝙅𝙪𝙜𝙖 𝙆𝙚𝙣𝙖 𝙂𝙝𝙤𝙨𝙩𝙞𝙣𝙜`")


@register(outgoing=True, pattern='^.give(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`𝙒𝙤𝙞𝙞𝙞 𝘼𝙙𝙢𝙞𝙣 𝙂𝙞𝙫𝙚𝙬𝙚`")
    sleep(2)
    await typew.edit("`𝘼𝙙𝙢𝙞𝙣 𝙏𝙪𝙧𝙪𝙣𝙞𝙣 𝙂𝙞𝙫𝙚𝙬𝙚`")
    sleep(1)
    await typew.edit("`𝙎𝙚𝙢𝙤𝙜𝙖 𝘿𝙖𝙥𝙚𝙩 𝙂𝙞𝙫𝙚𝙬𝙚`")


@register(outgoing=True, pattern='^.uno(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")


CMD_HELP.update({
    "gabut3": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `tmo`\
    \n↳ : Cobain Sendiri\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.give`\
    \n↳ : Cobain Sendiri`\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.uno`\
    \n↳ : Cobain Sendiri."
})
