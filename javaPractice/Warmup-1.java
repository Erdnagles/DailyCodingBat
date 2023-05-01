// 1 sleepIn

public boolean sleepIn(boolean weekday, boolean vacation) {
  boolean result = false;
  
  if (!weekday || vacation)
    result = true;
  
  return result;
}

public boolean sleepIn(boolean weekday, boolean vacation) {
  return (!weekday || vacation);
}

// 2 monkeyTrouble

public boolean monkeyTrouble(boolean aSmile, boolean bSmile) {
  return aSmile && bSmile || !aSmile && !bSmile;
}

// 3 sumDouble

public int sumDouble(int a, int b) {
  return (a == b) ? 2 * (a + b) : a + b;
}

// 4 diff21

public int diff21(int n) {
  if (n > 21)
    return (n-21)*2;
  return 21 - n;
}

public int diff21(int n) {
  return n > 21 ? 2 * (n-21) : 21-n;
}

// 5 parrotTrouble

public boolean parrotTrouble(boolean talking, int hour) {
  if (hour < 7 && talking || hour > 20 && talking)
    return true;
  return false;
}

// 6 makes10

public boolean makes10(int a, int b) {
  int c = 10;
  if (a == c || b == c || a + b == c)
    return true;
  return false;
}

// 7 nearHundred

public boolean nearHundred(int n) {
  int diff = Math.abs(100 - n);
  int diff2 = Math.abs(200 - n);
  if(diff <=  10 || diff2 <= 10)
    return true;
  return false;
}

// 8 posNeg

public boolean posNeg(int a, int b, boolean negative) {
  if (negative)
    return (a < 0 && b < 0);
  return (a < 0 && b >= 0 || a >= 0 && b < 0);
}

// 9 notString

public String notString(String str) {
  return str.startsWith("not") ? str : "not " + str;
}

// 10 missingChar

public String missingChar(String str, int n) {
  return str.substring(0,n) + str.substring(n+1, str.length());
}

// 11 frontBack

public String frontBack(String str) {
  int length = str.length();
  
  if (length <= 1) {
    return str;
  } else { 
    return str.charAt(length - 1) + str.substring(1, length - 1) + str.charAt(0);
  }
}

// 12 front3

public String front3(String str) {
  if (str.length() <= 3) {
    return str + str + str;
  }
  String newStr = str.substring(0, 3);
  return newStr + newStr + newStr;
}
