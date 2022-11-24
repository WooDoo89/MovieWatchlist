from flask import Blueprint, render_template, session, redirect, request


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/")
def index():
    return render_template(
        "index.html",
        title="Movies Watchlist",
    )
    
    
@pages.route("/toggle-theme")
def toggle_theme():
    currrent_theme = session.get("theme")
    if currrent_theme == "dark":
        session["theme"] = "light"
    else:
        session["theme"] = "dark"
        
    return redirect(request.args.get("current_page"))