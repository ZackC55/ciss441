# Assignment A5

This is an app that displays and moves electoral college data from a CSV to a SQLite Database:

```
processing!!!   1  ID: 1       Year: 1788     State: Alabama           Votes: 0
processing!!!   2  ID: 2       Year: 1788     State: Alaska            Votes: 0
processing!!!   3  ID: 3       Year: 1788     State: Arizona           Votes: 0
processing!!!   4  ID: 4       Year: 1788     State: Arkansas          Votes: 0
processing!!!   5  ID: 5       Year: 1788     State: California        Votes: 0
processing!!!   6  ID: 6       Year: 1788     State: Colorado          Votes: 0
processing!!!   7  ID: 7       Year: 1788     State: Connecticut       Votes: 7
processing!!!   8  ID: 8       Year: 1788     State: D.C.              Votes: 0
processing!!!   9  ID: 9       Year: 1788     State: Delaware          Votes: 3
processing!!!  10  ID: 10      Year: 1788     State: Florida           Votes: 0
processing!!!  11  ID: 11      Year: 1788     State: Georgia           Votes: 5
processing!!!  12  ID: 12      Year: 1788     State: Hawaii            Votes: 0
processing!!!  13  ID: 13      Year: 1788     State: Idaho             Votes: 0
processing!!!  14  ID: 14      Year: 1788     State: Illinois          Votes: 0
processing!!!  15  ID: 15      Year: 1788     State: Indiana           Votes: 0
processing!!!  16  ID: 16      Year: 1788     State: Iowa              Votes: 0
processing!!!  17  ID: 17      Year: 1788     State: Kansas            Votes: 0
processing!!!  18  ID: 18      Year: 1788     State: Kentucky          Votes: 0
processing!!!  19  ID: 19      Year: 1788     State: Louisiana         Votes: 0
processing!!!  20  ID: 20      Year: 1788     State: Maine             Votes: 0
processing!!!  21  ID: 21      Year: 1788     State: Maryland          Votes: 8
processing!!!  22  ID: 22      Year: 1788     State: Massachusetts     Votes: 10
processing!!!  23  ID: 23      Year: 1788     State: Michigan          Votes: 0
processing!!!  24  ID: 24      Year: 1788     State: Minnesota         Votes: 0
processing!!!  25  ID: 25      Year: 1788     State: Mississippi       Votes: 0
processing!!!  26  ID: 26      Year: 1788     State: Missouri          Votes: 0
processing!!!  27  ID: 27      Year: 1788     State: Montana           Votes: 0
processing!!!  28  ID: 28      Year: 1788     State: Nebraska          Votes: 0
processing!!!  29  ID: 29      Year: 1788     State: Nevada            Votes: 0
processing!!!  30  ID: 30      Year: 1788     State: New Hampshire     Votes: 5
processing!!!  31  ID: 31      Year: 1788     State: New Jersey        Votes: 6
processing!!!  32  ID: 32      Year: 1788     State: New Mexico        Votes: 0
processing!!!  33  ID: 33      Year: 1788     State: New York          Votes: 8
processing!!!  34  ID: 34      Year: 1788     State: North Carolina    Votes: 0
processing!!!  35  ID: 35      Year: 1788     State: North Dakota      Votes: 0
processing!!!  36  ID: 36      Year: 1788     State: Ohio              Votes: 0
processing!!!  37  ID: 37      Year: 1788     State: Oklahoma          Votes: 0
processing!!!  38  ID: 38      Year: 1788     State: Oregon            Votes: 0
processing!!!  39  ID: 39      Year: 1788     State: Pennsylvania      Votes: 10
processing!!!  40  ID: 40      Year: 1788     State: Rhode Island      Votes: 0
processing!!!  41  ID: 41      Year: 1788     State: South Carolina    Votes: 7
processing!!!  42  ID: 42      Year: 1788     State: South Dakota      Votes: 0
processing!!!  43  ID: 43      Year: 1788     State: Tennessee         Votes: 0
processing!!!  44  ID: 44      Year: 1788     State: Texas             Votes: 0
processing!!!  45  ID: 45      Year: 1788     State: Utah              Votes: 0
processing!!!  46  ID: 46      Year: 1788     State: Vermont           Votes: 0
processing!!!  47  ID: 47      Year: 1788     State: Virginia          Votes: 12
processing!!!  48  ID: 48      Year: 1788     State: Washington        Votes: 0
processing!!!  49  ID: 49      Year: 1788     State: West Virginia     Votes: 0
processing!!!  50  ID: 50      Year: 1788     State: Wisconsin         Votes: 0
processing!!!  51  ID: 51      Year: 1788     State: Wyoming           Votes: 0
processing!!!  52  ID: 52      Year: 1792     State: Alabama           Votes: 0
processing!!!  53  ID: 53      Year: 1792     State: Alaska            Votes: 0
processing!!!  54  ID: 54      Year: 1792     State: Arizona           Votes: 0
processing!!!  55  ID: 55      Year: 1792     State: Arkansas          Votes: 0
processing!!!  56  ID: 56      Year: 1792     State: California        Votes: 0
processing!!!  57  ID: 57      Year: 1792     State: Colorado          Votes: 0
processing!!!  58  ID: 58      Year: 1792     State: Connecticut       Votes: 9
processing!!!  59  ID: 59      Year: 1792     State: D.C.              Votes: 0
processing!!!  60  ID: 60      Year: 1792     State: Delaware          Votes: 3
processing!!!  61  ID: 61      Year: 1792     State: Florida           Votes: 0
processing!!!  62  ID: 62      Year: 1792     State: Georgia           Votes: 4
processing!!!  63  ID: 63      Year: 1792     State: Hawaii            Votes: 0
processing!!!  64  ID: 64      Year: 1792     State: Idaho             Votes: 0
processing!!!  65  ID: 65      Year: 1792     State: Illinois          Votes: 0
processing!!!  66  ID: 66      Year: 1792     State: Indiana           Votes: 0
processing!!!  67  ID: 67      Year: 1792     State: Iowa              Votes: 0
processing!!!  68  ID: 68      Year: 1792     State: Kansas            Votes: 0
processing!!!  69  ID: 69      Year: 1792     State: Kentucky          Votes: 4
processing!!!  70  ID: 70      Year: 1792     State: Louisiana         Votes: 0
processing!!!  71  ID: 71      Year: 1792     State: Maine             Votes: 0
processing!!!  72  ID: 72      Year: 1792     State: Maryland          Votes: 10
processing!!!  73  ID: 73      Year: 1792     State: Massachusetts     Votes: 16
processing!!!  74  ID: 74      Year: 1792     State: Michigan          Votes: 0
processing!!!  75  ID: 75      Year: 1792     State: Minnesota         Votes: 0
processing!!!  76  ID: 76      Year: 1792     State: Mississippi       Votes: 0
processing!!!  77  ID: 77      Year: 1792     State: Missouri          Votes: 0
processing!!!  78  ID: 78      Year: 1792     State: Montana           Votes: 0
processing!!!  79  ID: 79      Year: 1792     State: Nebraska          Votes: 0
processing!!!  80  ID: 80      Year: 1792     State: Nevada            Votes: 0
processing!!!  81  ID: 81      Year: 1792     State: New Hampshire     Votes: 6
processing!!!  82  ID: 82      Year: 1792     State: New Jersey        Votes: 7
processing!!!  83  ID: 83      Year: 1792     State: New Mexico        Votes: 0
processing!!!  84  ID: 84      Year: 1792     State: New York          Votes: 12
processing!!!  85  ID: 85      Year: 1792     State: North Carolina    Votes: 12
processing!!!  86  ID: 86      Year: 1792     State: North Dakota      Votes: 0
processing!!!  87  ID: 87      Year: 1792     State: Ohio              Votes: 0
processing!!!  88  ID: 88      Year: 1792     State: Oklahoma          Votes: 0
processing!!!  89  ID: 89      Year: 1792     State: Oregon            Votes: 0
processing!!!  90  ID: 90      Year: 1792     State: Pennsylvania      Votes: 15
processing!!!  91  ID: 91      Year: 1792     State: Rhode Island      Votes: 4
processing!!!  92  ID: 92      Year: 1792     State: South Carolina    Votes: 8
processing!!!  93  ID: 93      Year: 1792     State: South Dakota      Votes: 0
processing!!!  94  ID: 94      Year: 1792     State: Tennessee         Votes: 0
processing!!!  95  ID: 95      Year: 1792     State: Texas             Votes: 0
processing!!!  96  ID: 96      Year: 1792     State: Utah              Votes: 0
processing!!!  97  ID: 97      Year: 1792     State: Vermont           Votes: 4
processing!!!  98  ID: 98      Year: 1792     State: Virginia          Votes: 21
processing!!!  99  ID: 99      Year: 1792     State: Washington        Votes: 0
processing!!! 100  ID: 100     Year: 1792     State: West Virginia     Votes: 0
processing!!! 101  ID: 101     Year: 1792     State: Wisconsin         Votes: 0
processing!!! 102  ID: 102     Year: 1792     State: Wyoming           Votes: 0

 ELECTORAL COLLEGE REPORT by Year: 2016
Year: 2016    State: Alabama          Votes: 9
Year: 2016    State: Alaska           Votes: 3
Year: 2016    State: Arizona          Votes: 11
Year: 2016    State: Arkansas         Votes: 6
Year: 2016    State: California       Votes: 55
Year: 2016    State: Colorado         Votes: 9
Year: 2016    State: Connecticut      Votes: 7
Year: 2016    State: D.C.             Votes: 3
Year: 2016    State: Delaware         Votes: 3
Year: 2016    State: Florida          Votes: 29
Year: 2016    State: Georgia          Votes: 16
Year: 2016    State: Hawaii           Votes: 4
Year: 2016    State: Idaho            Votes: 4
Year: 2016    State: Illinois         Votes: 20
Year: 2016    State: Indiana          Votes: 11
Year: 2016    State: Iowa             Votes: 6
Year: 2016    State: Kansas           Votes: 6
Year: 2016    State: Kentucky         Votes: 8
Year: 2016    State: Louisiana        Votes: 8
Year: 2016    State: Maine            Votes: 4
Year: 2016    State: Maryland         Votes: 10
Year: 2016    State: Massachusetts    Votes: 11
Year: 2016    State: Michigan         Votes: 16
Year: 2016    State: Minnesota        Votes: 10
Year: 2016    State: Mississippi      Votes: 6
Year: 2016    State: Missouri         Votes: 10
Year: 2016    State: Montana          Votes: 3
Year: 2016    State: Nebraska         Votes: 5
Year: 2016    State: Nevada           Votes: 6
Year: 2016    State: New Hampshire    Votes: 4
Year: 2016    State: New Jersey       Votes: 14
Year: 2016    State: New Mexico       Votes: 5
Year: 2016    State: New York         Votes: 29
Year: 2016    State: North Carolina   Votes: 15
Year: 2016    State: North Dakota     Votes: 3
Year: 2016    State: Ohio             Votes: 18
Year: 2016    State: Oklahoma         Votes: 7
Year: 2016    State: Oregon           Votes: 7
Year: 2016    State: Pennsylvania     Votes: 20
Year: 2016    State: Rhode Island     Votes: 4
Year: 2016    State: South Carolina   Votes: 9
Year: 2016    State: South Dakota     Votes: 3
Year: 2016    State: Tennessee        Votes: 11
Year: 2016    State: Texas            Votes: 38
Year: 2016    State: Utah             Votes: 6
Year: 2016    State: Vermont          Votes: 3
Year: 2016    State: Virginia         Votes: 13
Year: 2016    State: Washington       Votes: 12
Year: 2016    State: West Virginia    Votes: 5
Year: 2016    State: Wisconsin        Votes: 10
Year: 2016    State: Wyoming          Votes: 3

 ELECTORAL COLLEGE REPORT by Year: 2020
Year: 2020    State: Alabama          Votes: 9
Year: 2020    State: Alaska           Votes: 3
Year: 2020    State: Arizona          Votes: 11
Year: 2020    State: Arkansas         Votes: 6
Year: 2020    State: California       Votes: 55
Year: 2020    State: Colorado         Votes: 9
Year: 2020    State: Connecticut      Votes: 7
Year: 2020    State: D.C.             Votes: 3
Year: 2020    State: Delaware         Votes: 3
Year: 2020    State: Florida          Votes: 29
Year: 2020    State: Georgia          Votes: 16
Year: 2020    State: Hawaii           Votes: 4
Year: 2020    State: Idaho            Votes: 4
Year: 2020    State: Illinois         Votes: 20
Year: 2020    State: Indiana          Votes: 11
Year: 2020    State: Iowa             Votes: 6
Year: 2020    State: Kansas           Votes: 6
Year: 2020    State: Kentucky         Votes: 8
Year: 2020    State: Louisiana        Votes: 8
Year: 2020    State: Maine            Votes: 4
Year: 2020    State: Maryland         Votes: 10
Year: 2020    State: Massachusetts    Votes: 11
Year: 2020    State: Michigan         Votes: 16
Year: 2020    State: Minnesota        Votes: 10
Year: 2020    State: Mississippi      Votes: 6
Year: 2020    State: Missouri         Votes: 10
Year: 2020    State: Montana          Votes: 3
Year: 2020    State: Nebraska         Votes: 5
Year: 2020    State: Nevada           Votes: 6
Year: 2020    State: New Hampshire    Votes: 4
Year: 2020    State: New Jersey       Votes: 14
Year: 2020    State: New Mexico       Votes: 5
Year: 2020    State: New York         Votes: 29
Year: 2020    State: North Carolina   Votes: 15
Year: 2020    State: North Dakota     Votes: 3
Year: 2020    State: Ohio             Votes: 18
Year: 2020    State: Oklahoma         Votes: 7
Year: 2020    State: Oregon           Votes: 7
Year: 2020    State: Pennsylvania     Votes: 20
Year: 2020    State: Rhode Island     Votes: 4
Year: 2020    State: South Carolina   Votes: 9
Year: 2020    State: South Dakota     Votes: 3
Year: 2020    State: Tennessee        Votes: 11
Year: 2020    State: Texas            Votes: 38
Year: 2020    State: Utah             Votes: 6
Year: 2020    State: Vermont          Votes: 3
Year: 2020    State: Virginia         Votes: 13
Year: 2020    State: Washington       Votes: 12
Year: 2020    State: West Virginia    Votes: 5
Year: 2020    State: Wisconsin        Votes: 10
Year: 2020    State: Wyoming          Votes: 3
```
