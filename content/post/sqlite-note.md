---
title: "Sqlite Note"
date: 2015-04-24 18:55:57
tags: ["sqlite","note"]
categories: ["software"]
---

常用查询函数
------------

    def query_db(self, sql, args=(), one=False):
        cur = self.cx.execute(sql, args)
        rv = [dict((cur.description[idx][0], value)
            for idx, value in enumerate(row)) for row in cur.fetchall()]
        return (rv[0] if rv else None) if one else rv

清空表的内容，并重置自增字段
----------------------------

    delete from your_table;
    delete from sqlite_sequence where name='your_table';

如何将两个字段字符串合并
------------------------

使用 `||` 符号。

内置函数
--------

### 核心函数

An application may define additional functions written in C and added to
the database engine using the sqlite3\_create\_function() API.

abs(X)

该函数返回数值参数 X 的绝对值。如果 X 为 NULL ，则返回 NULL。如果 X
是无法转换 为数值的字符串或 blob ，则返回 0.0 。如果 X 是整数
-9223372036854775808 ，那么 因为值超出 Integer 的上限，抛出 Integer
Overflow 异常。

The abs(X) function returns the absolute value of the numeric argument
X. Abs(X) returns NULL if X is NULL. Abs(X) returns 0.0 if X is a string
or blob that cannot be converted to a numeric value. If X is the integer
-9223372036854775808 then abs(X) throws an integer overflow error since
there is no equivalent positive 64-bit two complement value.

changes()

该函数返回最近执行完毕的 INSERT 、 DELETE 和 UPDATE
语句所影响的数据行数，它是 sqlite3\_changes() C/C++ 函数的封装。

The changes() function returns the number of database rows that were
changed or inserted or deleted by the most recently completed INSERT,
DELETE, or UPDATE statement, exclusive of statements in lower-level
triggers. The changes() SQL function is a wrapper around the
sqlite3\_changes() C/C++ function and hence follows the same rules for
counting changes.

char(X1,X2,...,XN)

The char(X1,X2,...,XN) function returns a string composed of characters
having the unicode code point values of integers X1 through XN,
respectively.

coalesce(X,Y,...)

The coalesce() function returns a copy of its first non-NULL argument,
or NULL if all arguments are NULL. Coalesce() must have at least 2
arguments.

glob(X,Y)

The glob(X,Y) function is equivalent to the expression "Y GLOB X". Note
that the X and Y arguments are reversed in the glob() function relative
to the infix GLOB operator. If the sqlite3\_create\_function() interface
is used to override the glob(X,Y) function with an alternative
implementation then the GLOB operator will invoke the alternative
implementation.

ifnull(X,Y)

The ifnull() function returns a copy of its first non-NULL argument, or
NULL if both arguments are NULL. Ifnull() must have exactly 2 arguments.
The ifnull() function is equivalent to coalesce() with two arguments.

instr(X,Y)

The instr(X,Y) function finds the first occurrence of string Y within
string X and returns the number of prior characters plus 1, or 0 if Y is
nowhere found within X. Or, if X and Y are both BLOBs, then instr(X,Y)
returns one more than the number bytes prior to the first occurrence of
Y, or 0 if Y does not occur anywhere within X. If both arguments X and Y
to instr(X,Y) are non-NULL and are not BLOBs then both are interpreted
as strings. If either X or Y are NULL in instr(X,Y) then the result is
NULL.

hex(X)

The hex() function interprets its argument as a BLOB and returns a
string which is the upper-case hexadecimal rendering of the content of
that blob.

last\_insert\_rowid() The last\_insert\_rowid() function returns the
ROWID of the last row insert from the database connection which invoked
the function. The last\_insert\_rowid() SQL function is a wrapper around
the sqlite3\_last\_insert\_rowid() C/C++ interface function.

length(X) For a string value X, the length(X) function returns the
number of characters (not bytes) in X prior to the first NUL character.
Since SQLite strings do not normally contain NUL characters, the
length(X) function will usually return the total number of characters in
the string X. For a blob value X, length(X) returns the number of bytes
in the blob. If X is NULL then length(X) is NULL. If X is numeric then
length(X) returns the length of a string representation of X.

like(X,Y)

like(X,Y,Z) The like() function is used to implement the "Y LIKE X
\[ESCAPE Z\]" expression. If the optional ESCAPE clause is present, then
the like() function is invoked with three arguments. Otherwise, it is
invoked with two arguments only. Note that the X and Y parameters are
reversed in the like() function relative to the infix LIKE operator. The
sqlite3\_create\_function() interface can be used to override the like()
function and thereby change the operation of the LIKE operator. When
overriding the like() function, it may be important to override both the
two and three argument versions of the like() function. Otherwise,
different code may be called to implement the LIKE operator depending on
whether or not an ESCAPE clause was specified.

likelihood(X,Y) The likelihood(X,Y) function returns argument X
unchanged. The value Y in likelihood(X,Y) must be a floating point
constant between 0.0 and 1.0, inclusive. The likelihood(X) function is a
no-op that the code generator optimizes away so that it consumes no CPU
cycles during run-time (that is, during calls to sqlite3\_step()). The
purpose of the likelihood(X,Y) function is to provide a hint to the
query planner that the argument X is a boolean that is true with a
probability of approximately Y. The unlikely(X) function is short-hand
for likelihood(X,0.0625). The likely(X) function is short-hand for
likelihood(X,0.9375).

likely(X) The likely(X) function returns the argument X unchanged. The
likely(X) function is a no-op that the code generator optimizes away so
that it consumes no CPU cycles at run-time (that is, during calls to
sqlite3\_step()). The purpose of the likely(X) function is to provide a
hint to the query planner that the argument X is a boolean value that is
usually true. The likely(X) function is equivalent to
likelihood(X,0.9375). See also: unlikely(X).

load\_extension(X)

load\_extension(X,Y) The load\_extension(X,Y) function loads SQLite
extensions out of the shared library file named X using the entry point
Y. The result of load\_extension() is always a NULL. If Y is omitted
then the default entry point name is used. The load\_extension()
function raises an exception if the extension fails to load or
initialize correctly.

The load\_extension() function will fail if the extension attempts to
modify or delete an SQL function or collating sequence. The extension
can add new functions or collating sequences, but cannot modify or
delete existing functions or collating sequences because those functions
and/or collating sequences might be used elsewhere in the currently
running SQL statement. To load an extension that changes or deletes
functions or collating sequences, use the sqlite3\_load\_extension()
C-language API.

For security reasons, extension loaded is turned off by default and must
be enabled by a prior call to sqlite3\_enable\_load\_extension().

lower(X) The lower(X) function returns a copy of string X with all ASCII
characters converted to lower case. The default built-in lower()
function works for ASCII characters only. To do case conversions on
non-ASCII characters, load the ICU extension.

ltrim(X)

ltrim(X,Y) The ltrim(X,Y) function returns a string formed by removing
any and all characters that appear in Y from the left side of X. If the
Y argument is omitted, ltrim(X) removes spaces from the left side of X.

max(X,Y,...) The multi-argument max() function returns the argument with
the maximum value, or return NULL if any argument is NULL. The
multi-argument max() function searches its arguments from left to right
for an argument that defines a collating function and uses that
collating function for all string comparisons. If none of the arguments
to max() define a collating function, then the BINARY collating function
is used. Note that max() is a simple function when it has 2 or more
arguments but operates as an aggregate function if given only a single
argument.

min(X,Y,...) The multi-argument min() function returns the argument with
the minimum value. The multi-argument min() function searches its
arguments from left to right for an argument that defines a collating
function and uses that collating function for all string comparisons. If
none of the arguments to min() define a collating function, then the
BINARY collating function is used. Note that min() is a simple function
when it has 2 or more arguments but operates as an aggregate function if
given only a single argument.

nullif(X,Y) The nullif(X,Y) function returns its first argument if the
arguments are different and NULL if the arguments are the same. The
nullif(X,Y) function searches its arguments from left to right for an
argument that defines a collating function and uses that collating
function for all string comparisons. If neither argument to nullif()
defines a collating function then the BINARY is used.

printf(FORMAT,...) The printf(FORMAT,...) SQL function works like the
sqlite3\_mprintf() C-language function and the printf() function from
the standard C library. The first argument is a format string that
specifies how to construct the output string using values taken from
subsequent arguments. If the FORMAT argument is missing or NULL then the
result is NULL. The %n format is silently ignored and does not consume
an argument. The %p format is an alias for %X. The %z format is
interchangeable with %s. If there are too few arguments in the argument
list, missing arguments are assumed to have a NULL value, which is
translated into 0 or 0.0 for numeric formats or an empty string for %s.

quote(X) The quote(X) function returns the text of an SQL literal which
is the value of its argument suitable for inclusion into an SQL
statement. Strings are surrounded by single-quotes with escapes on
interior quotes as needed. BLOBs are encoded as hexadecimal literals.
Strings with embedded NUL characters cannot be represented as string
literals in SQL and hence the returned string literal is truncated prior
to the first NUL.

random() The random() function returns a pseudo-random integer between
-9223372036854775808 and +9223372036854775807.

randomblob(N) The randomblob(N) function return an N-byte blob
containing pseudo-random bytes. If N is less than 1 then a 1-byte random
blob is returned.

Hint: applications can generate globally unique identifiers using this
function together with hex() and/or lower() like this:

    hex(randomblob(16))

    lower(hex(randomblob(16)))

replace(X,Y,Z) The replace(X,Y,Z) function returns a string formed by
substituting string Z for every occurrence of string Y in string X. The
BINARY collating sequence is used for comparisons. If Y is an empty
string then return X unchanged. If Z is not initially a string, it is
cast to a UTF-8 string prior to processing.

round(X)

round(X,Y) The round(X,Y) function returns a floating-point value X
rounded to Y digits to the right of the decimal point. If the Y argument
is omitted, it is assumed to be 0.

rtrim(X)

rtrim(X,Y) The rtrim(X,Y) function returns a string formed by removing
any and all characters that appear in Y from the right side of X. If the
Y argument is omitted, rtrim(X) removes spaces from the right side of X.

soundex(X) The soundex(X) function returns a string that is the soundex
encoding of the string X. The string "?000" is returned if the argument
is NULL or contains no ASCII alphabetic characters. This function is
omitted from SQLite by default. It is only available if the
SQLITE\_SOUNDEX compile-time option is used when SQLite is built.

sqlite\_compileoption\_get(N) The sqlite\_compileoption\_get() SQL
function is a wrapper around the sqlite3\_compileoption\_get() C/C++
function. This routine returns the N-th compile-time option used to
build SQLite or NULL if N is out of range. See also the compile\_options
pragma.

sqlite\_compileoption\_used(X) The sqlite\_compileoption\_used() SQL
function is a wrapper around the sqlite3\_compileoption\_used() C/C++
function. When the argument X to sqlite\_compileoption\_used(X) is a
string which is the name of a compile-time option, this routine returns
true (1) or false (0) depending on whether or not that option was used
during the build.

sqlite\_source\_id() The sqlite\_source\_id() function returns a string
that identifies the specific version of the source code that was used to
build the SQLite library. The string returned by sqlite\_source\_id()
begins with the date and time that the source code was checked in and is
follows by an SHA1 hash that uniquely identifies the source tree. This
function is an SQL wrapper around the sqlite3\_sourceid() C interface.

sqlite\_version() The sqlite\_version() function returns the version
string for the SQLite library that is running. This function is an SQL
wrapper around the sqlite3\_libversion() C-interface.

substr(X,Y,Z)

substr(X,Y) The substr(X,Y,Z) function returns a substring of input
string X that begins with the Y-th character and which is Z characters
long. If Z is omitted then substr(X,Y) returns all characters through
the end of the string X beginning with the Y-th. The left-most character
of X is number 1. If Y is negative then the first character of the
substring is found by counting from the right rather than the left. If Z
is negative then the abs(Z) characters preceding the Y-th character are
returned. If X is a string then characters indices refer to actual UTF-8
characters. If X is a BLOB then the indices refer to bytes.

total\_changes() The total\_changes() function returns the number of row
changes caused by INSERT, UPDATE or DELETE statements since the current
database connection was opened. This function is a wrapper around the
sqlite3\_total\_changes() C/C++ interface.

trim(X)

trim(X,Y) The trim(X,Y) function returns a string formed by removing any
and all characters that appear in Y from both ends of X. If the Y
argument is omitted, trim(X) removes spaces from both ends of X.

typeof(X) The typeof(X) function returns a string that indicates the
datatype of the expression X: "null", "integer", "real", "text", or
"blob".

unlikely(X) The unlikely(X) function returns the argument X unchanged.
The unlikely(X) function is a no-op that the code generator optimizes
away so that it consumes no CPU cycles at run-time (that is, during
calls to sqlite3\_step()). The purpose of the unlikely(X) function is to
provide a hint to the query planner that the argument X is a boolean
value that is usually not true. The unlikely(X) function is equivalent
to likelihood(X, 0.0625).

unicode(X) The unicode(X) function returns the numeric unicode code
point corresponding to the first character of the string X. If the
argument to unicode(X) is not a string then the result is undefined.

upper(X) The upper(X) function returns a copy of input string X in which
all lower-case ASCII characters are converted to their upper-case
equivalent.

zeroblob(N) The zeroblob(N) function returns a BLOB consisting of N
bytes of 0x00. SQLite manages these zeroblobs very efficiently.
Zeroblobs can be used to reserve space for a BLOB that is later written
using incremental BLOB I/O. This SQL function is implemented using the
sqlite3\_result\_zeroblob() routine from the C/C++ interface.

### Date And Time Functions

SQLite supports five date and time functions as follows:

    date(timestring, modifier, modifier, ...)
    time(timestring, modifier, modifier, ...)
    datetime(timestring, modifier, modifier, ...)
    julianday(timestring, modifier, modifier, ...)
    strftime(format, timestring, modifier, modifier, ...)

All five date and time functions take a time string as an argument. The
time string is followed by zero or more modifiers. The strftime()
function also takes a format string as its first argument.

The date and time functions use a subset of IS0-8601 date and time
formats. The date() function returns the date in this format:
YYYY-MM-DD. The time() function returns the time as HH:MM:SS. The
datetime() function returns "YYYY-MM-DD HH:MM:SS". The julianday()
function returns the Julian day - the number of days since noon in
Greenwich on November 24, 4714 B.C. (Proleptic Gregorian calendar). The
strftime() routine returns the date formatted according to the format
string specified as the first argument. The format string supports the
most common substitutions found in the strftime() function from the
standard C library plus two new substitutions, %f and %J. The following
is a complete list of valid strftime() substitutions:

  参数        |说明
  ----------- |--------------------------------
  %d          |day of month: 00
  %f          |fractional seconds: SS.SSS
  %H          |hour: 00-24
  %j          |day of year: 001-366
  %J          |Julian day number
  %m          |month: 01-12
  %M          |minute: 00-59
  %s          |seconds since 1970-01-01
  %S          |seconds: 00-59
  %w          |day of week 0-6 with Sunday==0
  %W          |week of year: 00-53
  %Y          |year: 0000-9999
  %%          |%

Notice that all other date and time functions can be expressed in terms
of strftime():

  Function         |Equivalent strftime()
  ---------------- |------------------------------------
  date(...)        |strftime('%Y-%m-%d', ...)
  time(...)        |strftime('%H:%M:%S', ...)
  datetime(...)    |strftime('%Y-%m-%d %H:%M:%S', ...)
  julianday(...)   |strftime('%J', ...)

The only reasons for providing functions other than strftime() is for
convenience and for efficiency.

Time Strings

A time string can be in any of the following formats:

    YYYY-MM-DD
    YYYY-MM-DD HH:MM
    YYYY-MM-DD HH:MM:SS
    YYYY-MM-DD HH:MM:SS.SSS
    YYYY-MM-DDTHH:MM
    YYYY-MM-DDTHH:MM:SS
    YYYY-MM-DDTHH:MM:SS.SSS
    HH:MM
    HH:MM:SS
    HH:MM:SS.SSS
    now
    DDDDDDDDDD

In formats 5 through 7, the "T" is a literal character separating the
date and the time, as required by ISO-8601. Formats 8 through 10 that
specify only a time assume a date of 2000-01-01. Format 11, the string
'now', is converted into the current date and time as obtained from the
xCurrentTime method of the sqlite3\_vfs object in use. The 'now'
argument to date and time functions always returns exactly the same
value for multiple invocations within the same sqlite3\_step() call.
Universal Coordinated Time (UTC) is used. Format 12 is the Julian day
number expressed as a floating point value.

Formats 2 through 10 may be optionally followed by a timezone indicator
of the form "\[+-\]HH:MM" or just "Z". The date and time functions use
UTC or "zulu" time internally, and so the "Z" suffix is a no-op. Any
non-zero "HH:MM" suffix is subtracted from the indicated date and time
in order to compute zulu time. For example, all of the following time
strings are equivalent:

    2013-10-07 08:23:19.120
    2013-10-07T08:23:19.120Z
    2013-10-07 04:23:19.120-04:00
    2456572.84952685

In formats 4, 7, and 10, the fractional seconds value SS.SSS can have
one or more digits following the decimal point. Exactly three digits are
shown in the examples because only the first three digits are
significant to the result, but the input string can have fewer or more
than three digits and the date/time functions will still operate
correctly. Similarly, format 12 is shown with 10 significant digits, but
the date/time functions will really accept as many or as few digits as
are necessary to represent the Julian day number.

Modifiers

The time string can be followed by zero or more modifiers that alter
date and/or time. Each modifier is a transformation that is applied to
the time value to its left. Modifiers are applied from left to right;
order is important. The available modifiers are as follows.

    NNN days
    NNN hours
    NNN minutes
    NNN.NNNN seconds
    NNN months
    NNN years
    start of month
    start of year
    start of day
    weekday N
    unixepoch
    localtime
    utc

The first six modifiers (1 through 6) simply add the specified amount of
time to the date and time specified by the preceding timestring and
modifiers. The 's' character at the end of the modifier names is
optional. Note that "±NNN months" works by rendering the original date
into the YYYY-MM-DD format, adding the ±NNN to the MM month value, then
normalizing the result. Thus, for example, the data 2001-03-31 modified
by '+1 month' initially yields 2001-04-31, but April only has 30 days so
the date is normalized to 2001-05-01. A similar effect occurs when the
original date is February 29 of a leapyear and the modifier is ±N years
where N is not a multiple of four.

The "start of" modifiers (7 through 9) shift the date backwards to the
beginning of the current month, year or day.

The "weekday" modifier advances the date forward to the next date where
the weekday number is N. Sunday is 0, Monday is 1, and so forth.

The "unixepoch" modifier (11) only works if it immediately follows a
timestring in the DDDDDDDDDD format. This modifier causes the DDDDDDDDDD
to be interpreted not as a Julian day number as it normally would be,
but as Unix Time - the number of seconds since 1970. If the "unixepoch"
modifier does not follow a timestring of the form DDDDDDDDDD which
expresses the number of seconds since 1970 or if other modifiers
separate the "unixepoch" modifier from prior DDDDDDDDDD then the
behavior is undefined. Due to precision limitations imposed by the
implementations use of 64-bit integers, the "unixepoch" modifier only
works for dates between 0000-01-01 00:00:00 and 5352-11-01 10:52:47
(unix times of -62167219200 through 10675199167).

The "localtime" modifier (12) assumes the time string to its left is in
Universal Coordinated Time (UTC) and adjusts the time string so that it
displays localtime. If "localtime" follows a time that is not UTC, then
the behavior is undefined. The "utc" is the opposite of "localtime".
"utc" assumes that the string to its left is in the local timezone and
adjusts that string to be in UTC. If the prior string is not in
localtime, then the result of "utc" is undefined.

Examples

Compute the current date.

SELECT date('now');

Compute the last day of the current month.

SELECT date('now','start of month','+1 month','-1 day');

Compute the date and time given a unix timestamp 1092941466.

SELECT datetime(1092941466, 'unixepoch');

Compute the date and time given a unix timestamp 1092941466, and
compensate for your local timezone.

SELECT datetime(1092941466, 'unixepoch', 'localtime');

Compute the current unix timestamp.

SELECT strftime('%s','now');

Compute the number of days since the signing of the US Declaration of
Independence.

SELECT julianday('now') - julianday('1776-07-04');

Compute the number of seconds since a particular moment in 2004:

SELECT strftime('%s','now') - strftime('%s','2004-01-01 02:34:56');

Compute the date of the first Tuesday in October for the current year.

SELECT date('now','start of year','+9 months','weekday 2');

Compute the time since the unix epoch in seconds (like
strftime('%s','now') except includes fractional part):

SELECT (julianday('now') - 2440587.5)\*86400.0;

Caveats And Bugs

The computation of local time depends heavily on the whim of politicians
and is thus difficult to get correct for all locales. In this
implementation, the standard C library function localtime\_r() is used
to assist in the calculation of local time. The localtime\_r() C
function normally only works for years between 1970 and 2037. For dates
outside this range, SQLite attempts to map the year into an equivalent
year within this range, do the calculation, then map the year back.

These functions only work for dates between 0000-01-01 00:00:00 and
9999-12-31 23:59:59 (julidan day numbers 1721059.5 through 5373484.5).
For dates outside that range, the results of these functions are
undefined.

Non-Vista Windows platforms only support one set of DST rules. Vista
only supports two. Therefore, on these platforms, historical DST
calculations will be incorrect. For example, in the US, in 2007 the DST
rules changed. Non-Vista Windows platforms apply the new 2007 DST rules
to all previous years as well. Vista does somewhat better getting
results correct back to 1986, when the rules were also changed.

All internal computations assume the Gregorian calendar system. It is
also assumed that every day is exactly 86400 seconds in duration.

### Aggregate Functions

The aggregate functions shown below are available by default. Additional
aggregate functions written in C may be added using the
sqlite3\_create\_function() API.

In any aggregate function that takes a single argument, that argument
can be preceded by the keyword DISTINCT. In such cases, duplicate
elements are filtered before being passed into the aggregate function.
For example, the function "count(distinct X)" will return the number of
distinct values of column X instead of the total number of non-null
values in column X.

avg(X) The avg() function returns the average value of all non-NULL X
within a group. String and BLOB values that do not look like numbers are
interpreted as 0. The result of avg() is always a floating point value
as long as at there is at least one non-NULL input even if all inputs
are integers. The result of avg() is NULL if and only if there are no
non-NULL inputs.

count(X)

count(*) The count(X) function returns a count of the number of times
that X is not NULL in a group. The count(*) function (with no arguments)
returns the total number of rows in the group.

group\_concat(X)

group\_concat(X,Y) The group\_concat() function returns a string which
is the concatenation of all non-NULL values of X. If parameter Y is
present then it is used as the separator between instances of X. A comma
(",") is used as the separator if Y is omitted. The order of the
concatenated elements is arbitrary.

max(X) The max() aggregate function returns the maximum value of all
values in the group. The maximum value is the value that would be
returned last in an ORDER BY on the same column. Aggregate max() returns
NULL if and only if there are no non-NULL values in the group.

min(X) The min() aggregate function returns the minimum non-NULL value
of all values in the group. The minimum value is the first non-NULL
value that would appear in an ORDER BY of the column. Aggregate min()
returns NULL if and only if there are no non-NULL values in the group.

sum(X)

total(X) The sum() and total() aggregate functions return sum of all
non-NULL values in the group. If there are no non-NULL input rows then
sum() returns NULL but total() returns 0.0. NULL is not normally a
helpful result for the sum of no rows but the SQL standard requires it
and most other SQL database engines implement sum() that way so SQLite
does it in the same way in order to be compatible. The non-standard
total() function is provided as a convenient way to work around this
design problem in the SQL language.

The result of total() is always a floating point value. The result of
sum() is an integer value if all non-NULL inputs are integers. If any
input to sum() is neither an integer or a NULL then sum() returns a
floating point value which might be an approximation to the true sum.

Sum() will throw an "integer overflow" exception if all inputs are
integers or NULL and an integer overflow occurs at any point during the
computation. Total() never throws an integer overflow.
