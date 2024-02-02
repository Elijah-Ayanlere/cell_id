# Cell Tower Location Tracker

This Python script retrieves location information based on cell tower data using the Unwired Labs API.

## Usage

1. **Obtain Unwired Labs API Key:**
   - Sign up on the [Unwired Labs](https://unwiredlabs.com/) website to get your API key.

2. **Set API Key as an Environment Variable:**
   - Export your API key as an environment variable:
     ```bash
     export UNWIREDLABS_API_KEY="your_api_key_here"
     ```

3. **Run the Script:**
   - Replace `cell_id` and `lac` variables in the script with your cell tower information. Then, execute the script:
     ```bash
     python cell_tower_location_tracker.py
     ```

## Security Note

Ensure your API key is kept confidential. Avoid hardcoding it in the script and consider using environment variables.

## Error Handling

The script incorporates error handling for network requests and unexpected errors.

## Contributing

Feel free to contribute by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
