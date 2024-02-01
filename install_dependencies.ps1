# Specify the desired Python version
$pythonVersion = "3.9.7"

# Check if Python is installed
$pythonPath = Join-Path $env:ProgramFiles "Python$pythonVersion"
if (Test-Path $pythonPath) {
    Write-Host "Python $pythonVersion is already installed."
}
else {
    Write-Host "Python not found. Installing Python $pythonVersion..."
    
    # Download and install Python
    $pythonInstallerUrl = "https://www.python.org/ftp/python/$pythonVersion/python-$pythonVersion-amd64.exe"
    Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile python_installer.exe
    Start-Process -Wait -FilePath python_installer.exe -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1 Include_test=0"
    Remove-Item -Path python_installer.exe
}

# Check if pip is installed
$pipPath = Join-Path $pythonPath "Scripts\pip.exe"
if (Test-Path $pipPath) {
    Write-Host "pip is already installed."
}
else {
    Write-Host "pip not found. Installing pip..."
    Invoke-Expression "& $pythonPath\python.exe -m ensurepip"
}

# Upgrade pip and install required Python packages using Python's pip
Write-Host "Upgrading pip..."
& $pipPath install --upgrade pip

# Install required Python packages using Python's pip
Write-Host "Installing required Python packages..."
& $pipPath install tkinterdnd2

# Add the Scripts directory to the system's PATH
$scriptsPath = Join-Path $pythonPath "Scripts"
[Environment]::SetEnvironmentVariable("Path", "$($env:Path);$scriptsPath", [System.EnvironmentVariableTarget]::Machine)

Write-Host "Dependencies installation complete."
