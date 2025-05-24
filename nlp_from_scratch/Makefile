#----------------------------------------
# Targets to run the model pipeline
#----------------------------------------

# Download data
download:
	python -m src.data.download

# Train the model
train:
	python -m src.model.train

# Run all: Run the model pipeline
all: download train

#----------------------------------------
# Cleaning folders
#----------------------------------------

# Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

# Delete all data
clean-data:
	rm -rf data/names/ 
	rm -rf data/data.zip
	rm -rf data/eng-fra.txt

# Delete all
clean-all: clean clean-data

# NOTE FOR WINDOWS USERS: Make is more challenging to install on Windows.
# I recommend using Chocolately guide here: 
# https://earthly.dev/blog/makefiles-on-windows/
