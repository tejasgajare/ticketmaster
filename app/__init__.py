from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is not None:
        app.config.from_mapping(test_config)

    # Sample HTTP error handling
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    # TODO: This is hardcoded, If template name changes, all imports must be changed
    from . import tickets
    app.register_blueprint(tickets.bp)

    return app