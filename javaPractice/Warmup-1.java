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
