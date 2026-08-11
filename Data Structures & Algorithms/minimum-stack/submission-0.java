class MinStack {
    int top=-1;
    int []stack=new int[10000];
    public MinStack() {

        
    }
    
    public void push(int val) {
        top++;
        stack[top]=val;
    }
    
    public void pop() {
        top--;
        
    }
    
    public int top() {
        return stack[top];
    }
    
    public int getMin() {
        int x=stack[0];
        for(int i=0;i<=top;i++){
            x=Math.min(stack[i],x);
        }return x;
        }
    }

