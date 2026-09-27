class Solution {
    public String reverseParentheses(String s) {
      int array[]=new int[s.length()];
      Stack<Integer> st=new Stack<>();
      StringBuilder sb=new StringBuilder();
      int i=0;
      int ind=0;
      int direction=1;
      while(i<s.length()){
        if(s.charAt(i)=='(')st.push(i);
        else if(s.charAt(i)==')'){
            array[i]=st.pop();
            array[array[i]]=i;
        }
        i++;
      }  
      while(ind<s.length()){
         if(s.charAt(ind)=='('||s.charAt(ind)==')'){
            ind=array[ind];
            direction=direction*-1;
         }else sb.append(s.charAt(ind));
         ind=ind+direction;
      }
      return sb.toString();
    }
}