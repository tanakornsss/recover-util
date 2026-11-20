# File Recover Util

---

## 1. Remove Thumbnail
- Remove file with the naming convention  of ```t*.jpg```
- Only works with files recovered via ```photorec```
- **Be aware that it will remove file with said convention unrelated to the thumbnail if used with other directory**

### Steps
1. Run ```python remove_thumbnail.py```
2. Input the root path of generated recovery folder.\
   Example ```D:\Backup```
3. Review the list of files to be removed generated in the text file named ```to_remove.txt```
4. Confirm your decision by typing ```yes``` (case-sensitive).