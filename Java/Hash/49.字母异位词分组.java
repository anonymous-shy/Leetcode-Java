/*
 * @lc app=leetcode.cn id=49 lang=java
 *
 * [49] 字母异位词分组
 */

// @lc code=start
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0)
            return new ArrayList();
        Map<String, List> ans = new HashMap<>();
        for (String s : strs) {
            char[] sc = s.toCharArray();
            Arrays.sort(sc);
            String k = String.valueOf(sc);
            if (!ans.containsKey(k))
                ans.put(k, new ArrayList());
            ans.get(k).add(s);
        }
        return new ArrayList(ans.values());
    }
}
// @lc code=end

