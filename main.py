import random
from website import create_app

app = create_app()

if __name__ == "__main__":  # Makes sure this is the main process
	app.run(debug=True, # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)