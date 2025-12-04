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

Edit `quote_updater.py` to change the franchise:

```python
SELECTED_FRANCHISE = "mass_effect"  # Options: "all", "mass_effect", "south_park", "spongebob"
```

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
