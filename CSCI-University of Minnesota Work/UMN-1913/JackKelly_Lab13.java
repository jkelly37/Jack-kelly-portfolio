public class PriorityQueue<Base> {

    private class Node{
        private Base object;
        private int rank;
        private Node left;
        private Node right;

        private Node(Base object, int rank){
            this.object=object;
            this.rank=rank;
            this.left=null;
            this.right=null;

        }

    }
    private Node root;
    private Node parent;

    public PriorityQueue(){
        root=null;
    }

    public Base dequeue(){
        if(root==null){
            throw new IllegalStateException();
        }
        else{
            return dequeueHelper(root);
        }
    }
    //finds node to remove
    public Base dequeueHelper(Node root) {

        if(root.left == null){
            Base retVal = remove(root, parent);
            parent = null;
            return retVal;
            //delete
        }else {
            parent = root;
            return dequeueHelper(root.left);
        }


    }
    public Base remove(Node rem, Node parent) {
        if (root == rem && root.right == null){
            Base temp = root.object;
            root = null;
            return temp;
        }
        if(parent == null){
            Base temp = rem.object;
            root = rem.right;
            return temp;
        }else{
            Base temp = rem.object;
            parent.left = rem.right;
            return temp;
        }
    }



    public void enqueue(Base object, int rank){
        if(rank<0){
            throw new IllegalArgumentException();
        }
        else if(isEmpty()){
            root = new Node(object,rank);
        }
        else{
            enqueueHelper(object,rank,root);
        }
    }

    public void enqueueHelper(Base object, int rank, Node tree){

        if(tree.rank==rank && tree.left == null){
            tree.left = new Node(object,rank);
        }else if (tree.rank == rank){
            enqueueHelper(object,rank,tree.left);
        }
        else if(tree.rank>rank){
            if(tree.left!=null){
                enqueueHelper(object,rank,tree.left);
            }
            else{
                tree.left= new Node(object,rank);
            }

        }
        else{
            if(tree.right!=null){
                enqueueHelper(object,rank,tree.right);
            }
            else{
                tree.right= new Node(object,rank);

            }

        }
    }

    public boolean isEmpty(){ return root==null;
    }
}
