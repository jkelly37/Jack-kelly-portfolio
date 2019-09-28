public class AssociationList<Key,Value> {
    private int size;
    private Node head;

    public AssociationList(){
        this.head = new Node();
        this.size=0;
    }

    public int getSize() {
        return size;
    }

    public boolean isEqual(Key left, Key right){
        if(left == null || right==null){
            return (left==right);
        }
        else{
            return left.equals(right);
        }
    }
    public void delete(Key key){
        int i = 0;
        Node parent = head;
        int tempSize=size;
        Node next = head.getNext();
        while(i<tempSize+1){


            if(isEqual(key,next.key)){
                parent.setNext(next.getNext());

                size=size-1;
                return;

            }
            parent=parent.getNext();
            next=next.getNext();
            i++;

        }



    }
    public boolean isIn(Key key){
        int i =0;

        Node temp = head.getNext();
        while(i<size){
            if(isEqual(temp.key,key)){
            return true;
            }
            i++;
            temp=temp.getNext();
        }
        return false;
    }

    public Value get(Key key) {
        int i =0;
        Node temp = head.getNext();
        while(i<size){
                if(isEqual(temp.key,key)){
                    return temp.value;
                }

            temp=temp.getNext();
            i++;


        }
        throw new IllegalArgumentException();
    }

    public void put(Key key, Value value){
        int i = 0;
        int sizetemp = size;
        size++;
        Node temp = head;
        if(key==null){
            Node temp3 = head;
            Node addnode1 = new Node(key,value, temp3.getNext());
            head.setNext(addnode1);
            if(key==null && value==null){
                size=size-1;
            }
            return;


        }
        while (i<sizetemp){
            if(isEqual(temp.key,key)){
                temp.value = value;
                size--;
                return;


            }
            i++;
            temp=temp.getNext();
        }

        int j = 0;
        Node temp2 = head;
        Node addnode = new Node(key,value, temp2.getNext());
        head.setNext(addnode);

    }
    public void makeString(){

        int i =0;
        Node dummy = head.getNext();
        while(i<size-1){

            i++;
            dummy=dummy.getNext();
        }
    }

    private class Node{
        private Key key;
        private Node next;
        private Value value;
        private Node(Key key,Value value,Node next){
            this.value = value;
            this.key = key;
            this.next = next;
        }
        private Node(){
            this.value = null;
            this.key = null;
            this.next = null;
        }

        public Node getNext() {
            return next;
        }

        public void setNext(Node next) {
            this.next = next;
        }


    }

}
