# Streaming Utility Scripts

This repository contains two essential utility scripts for streamers. These scripts help in tracking the "First" channel redeem event and generating shareable lobby IDs for games like Monster Hunter World. Below is a detailed explanation of each script and how to use them.

## Scripts Overview

### 1. `first_script.py`

The `first_script.py` script is designed to track the "First" channel redeem event. This event is popular in many streams where viewers compete to be the first to redeem a specific channel point reward. The script keeps track of how many times each user has been the first to redeem this reward.

#### How It Works:
- **Input:** The script prompts for a username when someone redeems the "First" channel reward.
- **Check & Update:** It checks if the username is already present in the `first_redeems.csv` file.
  - If the username **is not** in the CSV file, it adds the username and initializes a counter to track how many times this user has redeemed "First."
  - If the username **is** already in the CSV file, it simply increments the counter associated with that username.
- **Output:** The script updates the `first_redeems.csv` file with the latest count.

#### Example Usage:
```bash
python first_script.py username 
```

Upon running, enter the username of the viewer who redeemed "First" when prompted. The script will automatically handle the rest, updating the `*.csv` file accordingly.

## 2. `lobby_id_script.py`

The `lobby_id_script.py` is a specialized script designed to find the shareable lobby ID in Monster Hunter World. It employs a technique known as address magic, which involves accessing specific memory addresses within the game to retrieve the lobby ID that can be shared with other players.

### Shoutout:
A big thanks to **flutespine** for providing the original concept and techniques used in this MHW script.

### How It Works:

- **Address Magic:** The script locates the in-game memory address where the lobby ID is stored. By pinpointing this address, it can accurately retrieve the necessary data.
  
- **Extraction:** Once the address is located, the script extracts the lobby ID and formats it into a shareable form, making it easy for you to distribute it to others.

### Example Usage:
```bash
python lobby_id_script.py
