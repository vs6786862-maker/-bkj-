# Lead Parser

Telegram lead parser for extracting and analyzing leads from Telegram channels.

## Features

- Parse leads from Telegram channels
- Filter and categorize leads by niche
- Export to CSV/JSON formats
- Track parsed leads to avoid duplicates

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create `lead_config.json` with your API credentials:

```json
{
  "api_id": YOUR_API_ID,
  "api_hash": "YOUR_API_HASH",
  "phone": "YOUR_PHONE_NUMBER"
}
```

## Usage

```bash
python lead_parser.py
```

## Project Structure

- `lead_parser.py` - Main parser script
- `tg_login.py` - Telegram authentication helper
- `requirements.txt` - Python dependencies
- `leads_backup/` - Backup directory for leads data