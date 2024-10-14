# unhash what you need
from flask import (
    Blueprint,
    render_template,
    # render_template_string,
    # after_this_request,
    # current_app,
    # jsonify,
    # request,
    # session,
)
# from flask_security import (
#     auth_required,
#     hash_password,
#     permissions_accepted
# )

blueprint = Blueprint("views", __name__)


@blueprint.route("/")
def home():
    """
    The home page of the application.
    """
    return render_template("security/default.html")
