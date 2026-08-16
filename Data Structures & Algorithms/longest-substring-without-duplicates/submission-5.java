
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int left=0;
        int right=0;
        int m=0;
        int count=0;

        HashSet<Character> set = new HashSet<>();

        while(right<n){
            if(!set.contains(s.charAt(right))){
                set.add(s.charAt(right));
                right++;
                count++;
            }else{
                set.remove(s.charAt(left));
                left++;
                count--;
            }
            m=Math.max(m,count);
        }return m;
    }}
