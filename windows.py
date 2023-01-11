import os
import platform
#R4c0d3 @author
# Check if we are running on a Windows-based operating system
if platform.system() == "Windows":
    # Run the "powershell" command to view Windows Defender Settings
    output = os.popen("powershell Get-MpPreference").read()

    # output
    print(output)