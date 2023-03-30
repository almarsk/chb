def reply(user_reply, cs):
    cs.setdefault("r", 0)

    if cs["r"] == 0:
        cs["r"] += 1
        return cs["r"]
    if cs["r"] == 1:
        cs["r"] += 1
        return cs["r"]

