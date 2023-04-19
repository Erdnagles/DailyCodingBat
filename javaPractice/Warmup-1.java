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
