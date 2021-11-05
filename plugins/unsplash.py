# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• {i}unsplash <search query> ; <no of pics>
    Unsplash Image Search.
"""

from pyUltroid.functions.misc import unsplashsearch

from . import asyncio, download_file, eor, get_string, os, ultroid_cmd


@ultroid_cmd(pattern="unsplash ?(.*)")
async def searchunsl(ult):
    match = ult.pattern_match.group(1)
    if not match:
        return await eor(ult, "Give me Something to Search")
    num = 5
    if ";" in match:
        num = int(match.split(";")[1])
        match = match.split(";")[0]
    tep = await eor(ult, get_string("com_1"))
    res = await unsplashsearch(match, limit=num)
    if not res:
        return await eor(ult, get_string("unspl_1"), time=5)
    CL = []
    for e, rp in enumerate(res):
        CL.append(download_file(rp, f"{match}-{e}.png"))
    imgs = [z for z in (await asyncio.gather(*CL)) if z]
    await ult.client.send_file(
        ult.chat_id, imgs, caption=f"Uploaded {len(imgs)} Images!"
    )
    await tep.delete()
    [os.remove(img) for img in imgs]
