// 1 
public Map<String, String> mapBully(Map<String, String> map) {
  if (map.containsKey("a")) {
    map.put("b", map.get("a"));
    map.put("a", "");
  }
  return map;
}

// 2
public Map<String, String> mapShare(Map<String, String> map) {
  map.remove("c");
  if (map.containsKey("a")) {
    map.put("b", map.get("a"));
  }
  return map;
}