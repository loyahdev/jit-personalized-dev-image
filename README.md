# INCOMPLETE PDDI DO NOT WORK FOR ENABLING JIT ON IOS 17
## JIT-Personalized-Dev-Image
### Please note this is solely based on JIT enabling and not developer disk images and there uses. I do not have a deep understanding and some things said may be false
### I aim to create the ability to run JIT (Just In Time) Compilation on iOS devices running iOS 17 or use other sources and collect the info here

## Changes in iOS 17
With the beta release of iOS 17, Apple changed the standard Developer Disk Images for iOS releases to now Personal ones that are a per device basis. These personalized images aren't built the same with the file structure differences being:
```
- Xcode_iOS_DDI_Personalized (The Personalized Developer Disk Image)
    - Restore
     - 000-00000-000.dmg
     - BuildManifest.plist
     - Firmware
       - 000-00000-000.dmg.trustcache
     - Restore.plist
   - version.plist
```
I'm too lazy to list all of the files as there is a lot but the ones below are the base for the DMG file
```
- DeveloperDiskImage (An iOS 16.4 Developer Disk Image)
    - Applications
    - Library
    - System
    - usr
```

The files downloaded for the PDDI are
```
iOS_DDI.dmg
iOS_DDI-version.plist
```
The files downloaded for the DDI are
```
DeveloperDiskImage.dmg
DeveloperDiskImage.dmg.signature
```

## iOS 17 JIT Compilation
Currently, the only way to enable JIT on iOS 17 is through Apple and Xcode. The steps to do that are below:
1. Make sure all iPhoneOS 17 and iPadOS 17 simulators are installed
2. Make sure your iOS device is mounted in [] at the top menu bar:
```
Window/Devices and Simulators
```
3. Create a new iPhone App Xcode Project with any name and identifier
4. Go to [] in the top menu bar:
```
Debug/Attach to Process by PID or Name
```
5. Type in the app you want to enable JIT for and click attach with all the default options
6. On your iOS device open the app you attached the debug process for

### Troubleshooting
If you encounter a SIGBUS error type the following commands into the Xcode terminal:
```bash
process handle --pass true --stop false SIGBUS
```
```bash
continue
```
or press the continue button.


You will find if you're trying to run system-intensive apps such as emulators that it will run very slow.
I will use [Flycast](https://github.com/flyinghead/flycast) for example which is a Sega Dreamcast emulator for iOS devices.
Flycast can't run without JIT and you will find the app crashing when trying to run a game when JIT isn't enabled. When it is through Xcode the app may take extremely long to get to the loading and title screen. The game goes nearly unplayable but runs extremely slow and stops while playing.

The reason that JIT isn't seemingly making anything run faster on iOS is that Xcode doesn't just enable JIT it debugs the said software.
This means Xcode is looking at exactly what's happening in the app and shows you the data inevitably running the app slower.

The main difference I use to differentiate between Xcode JIT and other apps JIT is Xcode does JIT Compilation which debugs the app and JIT which enables the app with JIT and doesn't debug it.
If that makes sense.

## Current status for enabling JIT without using Xcode and using Personal Developer Disk Image with iOS 17
### The current status of this has used multiple sources for information on how to import and mount the PDDI. (Personalized Developer Disk Image)

This was made on my guessing so there may be steps not present
- [x] Getting the PDDI from Xcode
- [x] Mounting the PDDI's DMG file to MacOS
- [x] Getting the code signature for JIT (Different workaround)
- [ ] Mounting the PDDI's DMG file to JIT enabling software (Jitterbug, Jitstreamer, Sidetore, AltJIT, etc...)
- [ ] Enabling JIT through said software

The status may change at any time

Apple's API for iOS 17 has changed a lot makkng enabling JIT not at easy.

## iOS 16 and below JIT Compilation
With the release of iPadOS and iPhoneOS 17, the way to enable JIT on the devices has changed. The original way to enable it from iOS 11 - iOS 16 was to use a developer disk image and signature found in the Xcode files at the location 
```
Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/
```
 >The location is the same for the beta version of Xcode if you're running MacOS 14

The full instructions for iOS versions below iOS 17 excluding some versions such as 16.6 are at https://github.com/haikieu/xcode-developer-disk-image-all-platforms

<img width="760" alt="Screenshot 2023-08-03 at 8 39 42 PM" src="https://github.com/loyahdev/jit-personalized-dev-image/assets/68242406/4caf26aa-6bcc-4708-87be-47c155427f8c">

## Sources
