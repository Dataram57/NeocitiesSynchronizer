# Neocities Website Synchronizer

Just like GIT, you can synchronize your neocities website files with the ones you have locally with just a click!

# Setup

### 1. Download scripts and prepare a Folder:

    git clone https://github.com/Dataram57/NeocitiesSynchronizer.git
    cd NeocitiesSynchronizer
    mkdir website

Your website files must be in a folder called `website`. <br> *Or just edit `push.py`, i don't care `¯\_(ツ)_/¯`*

### 2. Create and edit `config.json`:
    
    {
        "apiKey": "YOUR_API_KEY_HERE"
    }

### 3. Run `push.py`

    python push.py