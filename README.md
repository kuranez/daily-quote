# Daily Quote

A Python script that automatically updates your GitHub profile README with a random quote from your favorite franchises.

## Features

- 🎲 Randomly selects quotes from different franchises (Mass Effect, South Park, SpongeBob)
- 🤖 Automated daily updates via GitHub Actions
- 🎨 Beautiful HTML banner with character icons
- 🌍 Supports multiple languages (English and German quotes)

## Usage

### Manual Update

Run the script locally to update your README:

```bash
python quote_updater.py
```

### Automated Daily Updates

The GitHub Action workflow automatically updates the quote every day at midnight UTC.

To manually trigger an update:
1. Go to your repository on GitHub
2. Click the "Actions" tab
3. Select "Update Daily Quote" workflow
4. Click "Run workflow"

### Configuration

Edit `quote_updater.py` to select franchises:

```python
SELECTED_FRANCHISES = ["all"]  # All franchises
# OR
SELECTED_FRANCHISES = ["south_park", "spongebob"]  # Multiple franchises
# OR
SELECTED_FRANCHISES = ["mass_effect"]  # Single franchise
```

Available franchises: `mass_effect`, `south_park`, `spongebob`

### Adding New Quotes

1. Navigate to `collection/[franchise]/[character]/`
2. Edit `quotes.txt`:
   - First line: `- Character Name`
   - Following lines: One quote per line (wrapped in quotes)

Example:
```
- Commander Shepard
"I should go."
"We fight or we die. That's the plan."
```

## Setup for Your Profile

1. Create a repository with your GitHub username
2. Copy the following files:
   - `quote_updater.py`
   - `collection/` folder
   - `.github/workflows/update-quote.yml`
3. Create a README.md with `<!--QUOTE_START-->` and `<!--QUOTE_END-->` markers
4. Push to GitHub and enable GitHub Actions

### Sync Workflow (Optional)

To automatically sync updates from this repository to your profile repository:

1. **Create a Personal Access Token (PAT)**:
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token" → "Generate new token (classic)"
   - Name: `Workflow Sync Token`
   - Select scopes: `repo` and `workflow`
   - Generate and copy the token

2. **Add the token as a secret**:
   - Go to your profile repository settings: `https://github.com/[username]/[username]/settings/secrets/actions`
   - Click "New repository secret"
   - Name: `PAT_TOKEN`
   - Value: paste your token
   - Click "Add secret"

3. **Copy the sync workflow**:
   - Copy `.github/workflows/sync-from-daily-quote.yml` to your profile repository
   - The workflow will automatically sync `quote_updater.py` and `update-quote.yml` daily at 01:00 UTC
   - You can also manually trigger it from the Actions tab

This keeps your profile repository automatically updated with the latest script improvements and fixes from this repository, while preserving your own README.md.

## Example Quote

<!--QUOTE_START-->
<div align="center">
  <table>
    <tr>
      <td>
        <img src="collection/mass_effect/commander_shepard/icon.png" alt="Commander Shepard" width="100" height="100">
      </td>
      <td>
        <p style="font-size: 18px; margin: 0;">I'm not just the hero of the galaxy. I'm also the galaxy's worst babysitter.</p>
        <p style="font-size: 14px; margin: 5px 0 0 0;">- Commander Shepard</p>
      </td>
    </tr>
  </table>
</div>
<!--QUOTE_END-->
