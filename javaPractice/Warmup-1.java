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

// 13 backAround

public String backAround(String str) {
  int length = str.length();
  return str.charAt(length - 1) + str + str.charAt(length - 1);
}

// 14 or35

public boolean or35(int n) {
  if (n % 3 == 0 || n % 5 == 0 ){
    return true;
  } else {
    return false;
  }
}

// 15 front22

public String front22(String str) {
  if (str.length() <= 2) {
    return str + str + str;
  } else {
    return str.substring(0, 2) + str + str.substring(0, 2);
  }
}

// 16 startHi

public boolean startHi(String str) {
  if (str.startsWith("hi"))
    return true;
  return false;
}

// 17 icyHot

public boolean icyHot(int temp1, int temp2) {
  return temp1 < 0 && temp2 > 100 || temp1 > 100 && temp2 < 0;
}

// 18 in1020

public boolean in1020(int a, int b) {
  return a >= 10 && a <= 20 || b >= 10 && b <= 20 ? true : false;
}

// 19 hasTeen

public boolean hasTeen(int a, int b, int c) {
  int[] teenAges = {13, 14, 15, 16, 17, 18, 19};
  for (int age : teenAges) {
    if ( age == a || age == b || age == c) {
      return true;
    }
  }
  return false;
}

// 20 loneTeen

public boolean loneTeen(int a, int b) {
  boolean aTeen = (a >= 13 && a <= 19);
  boolean bTeen = (b >= 13 && b <= 19);
  
  return (aTeen && !bTeen) || (!aTeen && bTeen);
}

// 21 delDel

public String delDel(String str) {
  if (str.length() >= 4 && str.substring(1, 4).equals("del")) {
    return str.charAt(0) + str.substring(4);
  }
  return str;
}

// 22 mixStart

public boolean mixStart(String str) {
  return str.length() >= 3 && str.substring(1, 3).equals("ix") ? true : false;
}

// 23 startOz

public String startOz(String str) {
  String newStr = "";
  if (str.length() > 0 && str.charAt(0) == 'o') newStr += 'o';
  if (str.length() > 1 && str.charAt(1) == 'z') newStr += 'z';
  return newStr;
}

// 24 intMax 

public int intMax(int a, int b, int c) {
    int max = a;
    if (b > max) {
      max = b;
    }
    if (c > max) {
      max = c;
    }
    return max;
}
