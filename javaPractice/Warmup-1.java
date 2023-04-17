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
