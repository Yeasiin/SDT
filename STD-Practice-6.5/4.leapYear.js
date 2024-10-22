function isLeapYear(year) {
  if (year % 4 == 0) {
    console.log(year, " is a Leap Year");
  } else {
    console.log(year, "is Not a Leap Year");
  }
}

isLeapYear(2000);
isLeapYear(2020);
isLeapYear(2024);
isLeapYear(2025);
isLeapYear(2011);
isLeapYear(2012);
