import os
import secrets
from importlib import import_module

from flask import (
    Flask,
    render_template,
    session,
    redirect,
    request,
    url_for,
    abort,
)

app = Flask(__name__)
secret_key = os.environ.get("CHATBOT_SECRET_KEY", secrets.token_bytes(32))
app.config.update(
    TEMPLATES_AUTO_RELOAD=True,
    SECRET_KEY=secret_key,
    SESSION_COOKIE_SAMESITE="Lax",
    REPLY_DELAY_MS=int(os.environ.get("CHATBOT_REPLY_DELAY_MS", 2000)),
)


@app.route("/", methods=["GET", "POST"])
def dispatcher():
    url_flow = request.args.get("flow")
    print(globals()["session"])

    if url_flow is not None:
        # a scenario was set via the URL's query string -> start a new conversation
        session.clear()
        session["flow"] = url_flow
        try:
            import_module(url_flow)
        except ImportError:
            session["page"] = "not_found"
        return redirect(url_for("dispatcher"))
    elif session.get("flow") is None:
        # starting a conversation without setting a scenario is forbidden -> 403 error
        session["page"] = "no_access"
        return render_template("no_access.html"), 403

    page = session.setdefault("page", "intro")
    handler = globals().get(page)
    if handler is None:
        abort(404)
    return handler()


def not_found():
    return render_template("not_found.html", flow=session["flow"].capitalize()), 404


def intro():
    if request.method == "GET":
        return render_template("intro.html", flow=session["flow"].capitalize())
    elif request.method == "POST":
        session["page"] = "chat"
        return redirect(url_for("dispatcher"))


def chat():
    user_reply = request.form.get("answer")
    cs = session.setdefault("cs", {})
    flow = import_module(session["flow"])
    bot_reply = flow.reply(user_reply, cs)
    session.modified = True
    if bot_reply is None:
        session["page"] = "outro"
        response = redirect(url_for("dispatcher"))
    else:
        response = render_template("chat.html", bot_reply=bot_reply, flow=flow.__name__.capitalize())
    return response  # render_template("chat.html", flow=session["flow"].capitalize(), botReply=bot_reply)


if __name__ == "__main__":
    app.run(debug=True)
