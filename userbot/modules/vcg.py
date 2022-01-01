# Thanks Full To Team Ultroid

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from telethon.tl.types import ChatAdminRights
from userbot import CMD_HELP
from userbot.events import register

NO_ADMIN = "`Maaf Kamu Bukan Admin 👮"


async def get_call(event):
    Kayzu = await event.client(getchat(event.chat_id))
    Kayzu = await event.client(getvc(Kayzu.full_chat.call))
    return Kayzu.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, pattern=r"^\.startvcg", groups_only=True)
async def _(e):
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await e.client(startvcg(e.chat_id))
        await e.edit("`Memulai Obrolan Suara`")
    except Exception as ex:
        await e.edit(f"`{str(ex)}`")


@register(outgoing=True, groups_only=True, pattern=r"^\.stopvcg")
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await c.client(stopvcg(await get_call(c)))
        await c.edit("`Mematikan Obrolan Suara`")
    except Exception as ex:
        await c.edit(f"**ERROR:** `{ex}`")


@register(outgoing=True, pattern=r"^\.vcginvite", groups_only=True)
async def _(e):
    await e.edit("`Sedang Mengivinte Jamet Tele...`")
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await e.edit(f"`Invited {z} users`")


@register(outgoing=True, pattern=r"^\.vctitle", groups_only=True)
async def _(Kayzu):
    title = e.pattern_match.group(1)
    chat = await diorbot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await Kayzu.edit("**Silahkan Masukan Title Obrolan Suara Grup**")

    if not admin and not creator:
        return await Kayzu.edit(f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
    try:
        await diorbot.edit(settitle(call=await get_call(e), title=title.strip()))
        await diorbot.edit(f"`Berhasil Mengubah Judul VCG Menjadi` `{title}`")
    except Exception as ex:
        await diorbot.edit(f"**ERROR:** `{ex}`")


CMD_HELP.update(
    {
        "vcg": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.startvcg`\
         \n↳ : Start Group Call in a group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stopvcg`\
         \n↳ : `Stop Group Call in a group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcginvite`\
         \n↳ : Invite all members of group in Group Call. (You must be joined)."
    }
)
