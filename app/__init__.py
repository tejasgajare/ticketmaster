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
        return render_template('error.html'), 404

    @app.errorhandler(werkzeug.exceptions.NotFound)
    def not_found(error):
        return render_template('error.html'), 404

    @app.errorhandler(werkzeug.exceptions.InternalServerError)
    def not_found(error):
        return render_template('error.html'), 404

    # TODO: This is hardcoded, If template name changes, all imports must be changed
    from . import list_tickets, show_ticket
    app.register_blueprint(list_tickets.bp)
    app.register_blueprint(show_ticket.bp)
    
    return app