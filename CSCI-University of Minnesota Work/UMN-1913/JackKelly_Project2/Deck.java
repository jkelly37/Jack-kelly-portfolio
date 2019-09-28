import java.util.Random;
public class Deck {
    private Card[] cards = new Card[52];
    private int count = 0;
    private boolean empty;
    private int index = 0;
    public Deck(){
        int suit = 1;
        while(suit<5){
            int rank = 1;
            while(rank<14){
                Card newCard = new Card(rank,suit);

                cards[count] = newCard;
                count++;
                rank++;
            }
            suit++;
        }
        empty=false;
        shuffle();
        //shuffle();


    }


    public void shuffle(){
        int i = cards.length-1;
        Random r = new Random();
        while(i>0){
            int j = r.nextInt(i+1);
            Card temp2 = cards[i];
            cards[i]=cards[j];
            cards[j]=temp2;
            i--;
        }
        /*while(i<count){
            int j = r.nextInt(i+1);
            Card temp1 = cards[j];
            Card temp2 = cards[i];
            cards[i]=cards[j];
            cards[j]=temp2;
            i=i+1;

        }
        */
        //System.out.println(count +"count");


    }


    public int cardsRemaining(){
        return count;
    }

    public boolean isEmpty(){
        if (count<1){
            empty=true;
        }
        else {
            empty=false;
        }
        return empty;
    }

    public Card draw(){
        if (count>0) {
            count=count-1;
            index++;
            //System.out.println("count is now "+cardsRemaining());
            return cards[index-1];

        }
        else{
            count = 52;
            shuffle();
            index=0;

            return draw();
        }

    }



}
