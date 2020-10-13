from flask import Flask

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()))

logger = logging.getLogger()

def create_app():
	logger.info(f'Starting app in {config.APP_ENV} enviroment')
	app = Flask(__name__)
	app.config.from_object('config')
	app.init_app(app)
	# initialize SQLAlchemy
	db.init_app(app)

	# define hellow world page
	def hello_world():
		return 'Hello, World!'
	return app

if __name__ == "__main__":
	app = create_app()
	app.run(host='0.0.0.0', debug=True)</td>
	</tr>
	<dr>
		<td>