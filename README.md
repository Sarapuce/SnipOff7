# SnipOff7 - Get offset of CSGO function quickly

Just a little tool to retrieve offset of some important function in CSGO dll

## Example usage
```
PS C:\SnipOff7> python .\SnipOff7.py
[+] engine.dll+8e990 : ProcessConnectionlessPacket
[+] engine.dll+90c10 : HandleDefferedConnection
[+] engine.dll+8c510 : SendConnectPacket
[+] engine.dll+8d270 : Disconnect
```

## Config file

There is two types of object that can be found in the config file. You can find one in the project

### File object

```
[Name_of_the_librairy.dll]
path = Path to the dll
offset = Offset to add which is the difference between the base image and Offset to raw data for section. For exemple, in engine.dll, base image is 0x10001000 and raw data is 0x400 so the value will be 0xc00
```

Example :
```
[engine.dll] 
path = D:\Jeux\SteamLibrary\steamapps\common\Counter-Strike Global Offensive\bin\engine.dll
offset = 0xc00
```


### Function

```
[FunctionName]
file = Name of the file where this function can be found
pattern = Array of bytes which is at start of the function (must be unique)
```

Example :
```
[ProcessConnectionlessPacket]
file = engine.dll
pattern = 558BEC83E4F081EC280E0000
```
