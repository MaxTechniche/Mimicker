# Mimicker

## **Goal**

Mimic (backup) a folder archetecture in another place.
(Essentially File History)

### **BUGS**

* Permission Error when overwriting files rapidly (Very Uncommon)

### **TODO**

* ~~[x] Full Copy folder archetecture~~
* ~~[x] on_created() (**file**)~~
  * ~~[x] get file location relative to the top level folder (e.g. `'\sub_folder_name\file_name.txt'`)~~
  * ~~[x] copy file to same relative path in mimicked folder~~
    * ~~[x] if folder already exists in base and mimic folders~~
    * ~~[x] if folder does not exist in mimic archetecture. Create folder tree.~~
* [ ] If file is no longer found in mimicked folder, move the micked file into an "other" folder
OR
* [ ] create file history numbers. (If the file was edited, create a new file with the number 1 higher than the previous)
