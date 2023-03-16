# SIS-ICS-Compositor
A python script to composite ICS calendar exported from SIS of CUHK-Shenzhen

## Pain point
The Student Information System (SIS) CUHK-Shenzhen uses supports the feature of exporting all enrolled classes schedule as `.ics` files.
However, the generated files are seperate into one class per file(e.g., CSC1001 on Tue in file A, CSC1001 on Thu in file B, Tut of CSC1001 in file C). And Outlook can only import one ics file at a time, and it's not easy to copy a series of events into a seperate calendar folder.

## Function
The script read all ICS files exported from SIS and put them into one ICS file with the compatibility of double-click to import all classes.

## Environment
Written and Tested under `Python 3.11.2`. Should be functional under any version of `Python 3`

## Usage
Run the script, then drag the folder of the unziped ICS files downloaded from SIS to the terminal window(equivalent to copy and paste the **FULL** path of the folder path). Press Enter and wait for its finish.

Find the result in your ICS folder: `{folder}/composite.ICS`

## Detailed Info
Copy one of the generated `VTIMEZONE` modules and all `VEVENT` modules to a single file. When copying one attribute disabled:

`X-MS-OLK-FORCEINSPECTOROPEN:TRUE` → `X-MS-OLK-FORCEINSPECTOROPEN:FALSE`

This allows importing all events into Microsoft Outlook as a single calendar object.

Not using iCalendar module because of laziness(?)

For more details please check Reference:
[Property: X-MS-OLK-FORCEINSPECTOROPEN](https://learn.microsoft.com/en-us/openspecs/exchange_server_protocols/ms-oxcical/d2a0a079-02a6-4643-9e78-0ac35998e1fb)

## Apendix
This part is tutorial for who is not familiar with SIS ICS exporting, Outlook ICS importing and so on.

[How To Get The ICS?](ExportICS.md)

[How To Import *composite.ics* To Outlook(Web & Client)](ImportICS.md)

[DLC: How To Subscribe Blackboard Calendar](Blackboard.md)