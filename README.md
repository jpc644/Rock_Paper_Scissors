# Rock_Paper_Scissors
Rock Paper Scissors Assignment for Python Coding Class (Class 2, Assignment 1)

# Installation Process
    Clone or download the Rock Paper Scissors repo onto your local device in a directory you can easily navigate to...
    Navigate to the repo using your command line application so subsequent commands assume you are running them from the local repository's root directory:

    '''sh
    cd Rock_Paper_Scissors
    '''

    ## Setup

    Setup a vritual environment

    '''sh 
    conda create -n my-rps-game-env python=3.8
    conda activate my-rps-game-env
    '''

    Install the required packages:

    '''sh
    pip install -r requirements.txt
    '''

    ### Configuration of Environment Variables

    Add a new ".env" file to the root directory of this repo, and place contents like the following inside:


    '''
    PLAYER_NAME = 'Input Your Player Name'

    ## Usage

    Run the Game:

    '''sh
    python game.py
    '''

# Payer must specify in .env file what their PLAYER_NAME is
# Install the dotenv package
# Load the appropriate dotenv variable