# How to Delete Microsoft Edge Profile Account on Mac

___Edge doesn't really remove your account___ even you choose to remove your account. Everyone with access to login into MacOS Account (maybe it's not you) can login again without asking any credentials. Use this command line to delete the leftover of Microsoft Edge profiles on Mac:
```bash
rm -rf /Applications/Microsoft\ Edge.app
rm -rf ~/Library/Application\ Support/Microsoft\ Edge/
rm -rf ~/Library/Saved\ Application\ State/com.microsoft.edgemac.savedState
rm -rf ~/Library/WebKit/com.microsoft.edgemac
rm -rf ~/Library/Preferences/com.microsoft.edgemac.plist
```

___Steps above alone will not solve the problem___, you have to go to your account setting: https://account.live.com/proofs/manage/additional and click `Sign me out` button in the bottom to sign out your account on any devices.
