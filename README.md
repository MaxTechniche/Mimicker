# Mimicker

## **Use**

Create a file in the base directory called `paths.yml` and configure it to have the source and destination directories.  

```yaml
source: <source-directory>
destination: <destination-directory>
```

## **Goal**

Mimic (backup) a folder architecture in another place.
(Essentially File History)

### **BUGS**

* Permission Error when overwriting files rapidly (Very Uncommon)

### **TODO**

* [ ] create file history numbers. (If the file was edited, create a new file with the number 1 higher than the previous)
