# Check if Python is installed
if (Test-Path $env:ProgramFiles\Python39) {
    Write-Host "Python is already installed."
}
else {
    Write-Host "Python not found. Installing Python..."
    # Download and install Python (adjust the download link based on your Python version)
    Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe -OutFile python_installer.exe
    Start-Process -Wait -FilePath python_installer.exe -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1 Include_test=0"
    Remove-Item -Path python_installer.exe
}

# Check if pip is installed
if (Test-Path $env:ProgramFiles\Python39\Scripts\pip.exe) {
    Write-Host "pip is already installed."
}
else {
    Write-Host "pip not found. Installing pip..."
    Invoke-Expression "& $env:ProgramFiles\Python39\python.exe -m ensurepip"
}

# Install required Python packages
Write-Host "Installing required Python packages..."
pip install tkinterdnd2

Write-Host "Dependencies installation complete."
