from flask import Flask, render_template
import werkzeug

PAGE_SZIE = 25

def create_app(test_config=None):
    app = Flask(__name__)
    if test_config is not None:
        app.config.from_mapping(test_config)

    # Sample HTTP error handling
    @app.errorhandler(werkzeug.exceptions.BadRequest)
    def not_found(error):
        return render_template('error.html', code=400, message="That's an error"), 400

    @app.errorhandler(werkzeug.exceptions.NotFound)
    def not_found(error):
        return render_template('error.html', code=404, message="The page you're looking for no longer exists"), 404

    @app.errorhandler(werkzeug.exceptions.InternalServerError)
    def not_found(error):
        return render_template('error.html', code=500, message="It's not you it's us."), 500

    # TODO: This is hardcoded, If template name changes, all imports must be changed
    from . import list_tickets, show_ticket
    app.register_blueprint(list_tickets.bp)
    app.register_blueprint(show_ticket.bp)
    
    return app