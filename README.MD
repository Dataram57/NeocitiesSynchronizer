# Neocities Website Synchronizer

Just like GIT, you can synchronize your neocities website files with the ones you have locally with just a click!

# Setup

### 1. Download scripts and prepare a Folder:

    git clone https://github.com/Dataram57/NeocitiesSynchronizer.git
    cd NeocitiesSynchronizer
    mkdir website

Your website files must be in a folder called `website`. <br> *Or just edit `push.py` & `fetch.py`, i don't care `¯\_(ツ)_/¯`*

### 2. Create and edit `config.json`:
    
    {
        "websiteUrl": "https://YOUR_USERNAME_HERE.neocities.org/"
        ,"apiKey": "YOUR_API_KEY_HERE"
    }

# Running

In terminal or cmd type:
- `python push.py` to push your website.
- `python fetch.py` to fetch your website.