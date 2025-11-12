Pico Project

This folder contains `main.py` for your Raspberry Pi Pico W.

Quick tasks (in VS Code):

- Run the upload task: Ctrl+Shift+P → Tasks: Run Task → select "Pico: Upload main.py". This runs:
  mpremote connect auto fs put "${workspaceFolder}/main.py" :/main.py

- Run the script on device: Ctrl+Shift+P → Tasks: Run Task → select "Pico: Run main.py". This runs:
  mpremote connect auto run :/main.py

If you want automatic upload on save, install the "Run on Save" extension (emeraldwalk.runonsave) and add a rule to run the upload task on save.

Install mpremote (if not already):

```powershell
python -m pip install --user mpremote
$env:Path += ";" + (python -m site --user-base) + "\Scripts"
mpremote --version
```

Notes:
- Use a USB data cable (not a charge-only cable).
- If `mpremote connect auto` fails, find the COM port in Device Manager and replace `auto` with the port (for example `COM3`).
