# How to Delete Microsoft Edge Profile Account on Mac

Use this command line to delete the leftover of Microsoft Edge profiles on Mac:
```bash
rm -rf /Applications/Microsoft\ Edge.app
rm -rf ~/Library/Application\ Support/Microsoft\ Edge/
rm -rf ~/Library/Saved\ Application\ State/com.microsoft.edgemac.savedState
rm -rf ~/Library/WebKit/com.microsoft.edgemac
rm -rf ~/Library/Preferences/com.microsoft.edgemac.plist
```
