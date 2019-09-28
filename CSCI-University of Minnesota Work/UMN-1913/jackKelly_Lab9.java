//  ARRAY QUEUE. A fixed length queue represented as a circular array.
import java.util.Iterator;
class ArrayQueue<Base>
{
  private int    front;    //  Index of front object in OBJECTS. - 1 before next dequeue
  private int    rear;     //  Index of rear object in OBJECTS. - on last enqueue
  private Base[] objects;  //  The OBJECTs in the queue.

//  Constuctor. Make a new empty queue that can hold SIZE - 1 elements.

  public ArrayQueue(int size) {
    if (size <= 1) {
      throw new IllegalArgumentException("Illegal size.");
    } else {
      front   = 0;
      rear    = 0;
      objects = (Base []) new Object[size];
    }
  }

//  DEQUEUE. Remove an object from the queue.

  public Base dequeue(){
    if (front == rear) {
      throw new IllegalStateException("Queue is empty.");
    } else {
      front = nextIndex(front);
      Base temp = objects[front];
      objects[front] = null;
      return temp;
    }
  }

//  ENQUEUE. Add a new OBJECT to the queue.

  public void enqueue(Base object) {
    if (isFull()) {
      throw new IllegalStateException("Queue is full.");
    }
    rear = nextIndex(rear);
    objects[rear] = object;
  }

//  IS EMPTY. Test if the queue is empty.

  public boolean isEmpty() {
    return front == rear;
  }

//  IS FULL. Test if the queue is full.

  public boolean isFull() {
    return front == nextIndex(rear);
  }

  // private method to compute "next" indexes in a circular array.
  private int nextIndex(int index) {
    return (index+1) % objects.length;
  }

  public Iterator<Base> iterator() {
    return new QueueIter(this, front,rear,objects);
  }

    class QueueIter implements Iterator<Base>{
    private int front = 0;
    private int rear = 0;
    private ArrayQueue arrq;
    private Base[] obj;
    private int size = 0;
    private int checks = 0;


    public QueueIter(ArrayQueue arrq, int front, int rear, Base[] objects){
      this.front = front;
      this.rear = rear;
      this.arrq = arrq;
      this.obj = objects;
      int i = 0;
      while(i<obj.length){
        if( obj[i] !=null){
          size++;
        }
        i++;
      }


    }


    @Override
    public boolean hasNext() {
      if (size == checks){
        return false;
      }
      return true;

    }

    @Override
    public Base next() {
      //System.out.println(("te"));
      if(hasNext()) {
        //System.out.println(("taaaaa"));
        front = front + 1;
        checks++;
        return obj[ArrayQueue.this.nextIndex(front - 1)];
      }
      return null;
    }
  }


}
